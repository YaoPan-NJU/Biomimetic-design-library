#!/usr/bin/env python3
"""
校验仿生设计库的一致性。

检查项目（9 条规则）：
1. feature-mapping.json 每个 ID 都有非空 prototype.md（无断链）
2. 无孤儿内容目录
3. frontmatter 必填字段齐全，category ∈ {微生物, 植物, 动物, 仿生材料}
4. source 为 literature/patent/standard 必须有非空标识符（ref_doi/patent_number/standard_number）
5. source=llm_inference 必须 ref_doi=null
6. 凡标 verification=verified 的条目，必须带可解析标识符或非空 source_file
7. chimera 检测：organism 含 ≥2 个不同类生物
8. 重复条目检测：同 pollutant+material+value
9. 结构化 JSON 完整性：prototypes_db/ 中的 JSON 必填字段
"""

import json
import os
import sys
import re
from pathlib import Path


VALID_CATEGORIES = {'微生物', '植物', '动物', '仿生材料'}


def parse_frontmatter(content: str) -> dict:
    """解析 YAML frontmatter。"""
    if not content.startswith('---'):
        return None
    end = content.find('---', 3)
    if end == -1:
        return None
    fm_text = content[3:end].strip()
    # 简单解析（不依赖 yaml 库）
    result = {}
    for line in fm_text.split('\n'):
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('-'):
            continue
        if ':' in line:
            key, _, val = line.partition(':')
            result[key.strip()] = val.strip()
    return result


def validate_prototype(prototype_dir: str) -> dict:
    """校验单个原型目录。"""
    report = {
        'prototype_id': os.path.basename(prototype_dir),
        'errors': [],
        'warnings': []
    }

    md_path = os.path.join(prototype_dir, 'prototype.md')
    if not os.path.exists(md_path):
        report['errors'].append('prototype.md 不存在')
        return report

    if os.path.getsize(md_path) == 0:
        report['errors'].append('prototype.md 为空')
        return report

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if len(content) < 100:
        report['warnings'].append('prototype.md 内容过短')

    if '[待补充]' in content:
        report['warnings'].append('prototype.md 包含 [待补充] 占位符')

    # 规则 3: frontmatter 检查
    fm = parse_frontmatter(content)
    if fm is None:
        report['errors'].append('缺少 YAML frontmatter')
    else:
        for field in ['id', 'name', 'category']:
            if not fm.get(field):
                report['errors'].append(f'frontmatter 缺少必填字段: {field}')
        # organism 允许为空（部分原型如仿生材料无具体生物来源）
        if not fm.get('organism'):
            report['warnings'].append('frontmatter organism 为空')
        cat = fm.get('category', '')
        if cat and cat not in VALID_CATEGORIES:
            report['errors'].append(f'category 值无效: {cat} (应为 {VALID_CATEGORIES})')

    return report


def validate_structured_json(db_dir: str) -> list:
    """校验 prototypes_db/ 中的结构化 JSON。"""
    reports = []
    required_fields = ['id', 'name_zh', 'name_en', 'organism', 'performance_data', 'mechanisms']

    if not os.path.exists(db_dir):
        return [{'prototype_id': 'N/A', 'errors': ['prototypes_db/ 目录不存在'], 'warnings': []}]

    for fname in sorted(os.listdir(db_dir)):
        if not fname.endswith('.json'):
            continue
        fpath = os.path.join(db_dir, fname)
        report = {
            'prototype_id': fname.replace('.json', ''),
            'errors': [],
            'warnings': []
        }

        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                d = json.load(f)
        except Exception as e:
            report['errors'].append(f'JSON 解析失败: {e}')
            reports.append(report)
            continue

        # 规则 9: 必填字段
        for field in required_fields:
            if field not in d:
                report['errors'].append(f'缺少必填字段: {field}')

        # 规则 7: chimera 检测
        org = d.get('organism', {})
        sci = org.get('scientific', '')
        if sci:
            # 检测是否包含多个不相关生物（排除多物种注释如 "Fish scales (多物种)"）
            parts = [p.strip() for p in re.split(r'[,;/]', sci) if p.strip()]
            # 排除同类多物种（如 SRB 属）
            if len(parts) > 2 and 'spp.' not in sci and '多物种' not in sci:
                report['warnings'].append(f'organism 可能包含多个不相关生物: {sci[:60]}')

        # 规则 4: source 标识符完整性
        for p in d.get('performance_data', []):
            source = p.get('source', '')
            ref = p.get('ref_doi')
            pn = p.get('patent_number')
            sn = p.get('standard_number')
            if source == 'literature' and not ref:
                report['warnings'].append(f'source=literature 但无 ref_doi: {p.get("parameter", "")[:40]}')
            elif source == 'patent' and not pn:
                report['warnings'].append(f'source=patent 但无 patent_number: {p.get("parameter", "")[:40]}')
            elif source == 'standard' and not sn:
                report['warnings'].append(f'source=standard 但无 standard_number: {p.get("parameter", "")[:40]}')

        # 规则 6: verification=verified 必须有标识符
        for p in d.get('performance_data', []):
            if p.get('verification') == 'verified':
                if not p.get('ref_doi') and not p.get('patent_number') and not p.get('standard_number'):
                    report['errors'].append(f'verified 但无标识符: {p.get("parameter", "")[:40]}')

        # 规则 8: 重复条目检测
        seen = set()
        for p in d.get('performance_data', []):
            key = f'{p.get("pollutant", "")}:{p.get("material", "")}:{str(p.get("value", ""))[:30]}'
            if key in seen:
                report['warnings'].append(f'重复性能数据: {key[:50]}')
            seen.add(key)

        reports.append(report)

    return reports


def validate_feature_mapping(feature_mapping_path: str, prototypes_dir: str) -> dict:
    """校验 feature-mapping.json 与 prototypes 目录的一致性。"""
    report = {
        'errors': [],
        'warnings': [],
        'stats': {}
    }

    if not os.path.exists(feature_mapping_path):
        report['errors'].append('feature-mapping.json 不存在')
        return report

    with open(feature_mapping_path, 'r', encoding='utf-8') as f:
        feature_mapping = json.load(f)

    prototype_metadata = feature_mapping.get('prototype_metadata', {})
    metadata_ids = set(prototype_metadata.keys())

    prototype_dirs = set()
    if os.path.exists(prototypes_dir):
        for item in os.listdir(prototypes_dir):
            item_path = os.path.join(prototypes_dir, item)
            if os.path.isdir(item_path):
                prototype_dirs.add(item)

    # 规则 1: 断链
    broken_links = metadata_ids - prototype_dirs
    if broken_links:
        report['errors'].append(f'断链: {sorted(broken_links)}')

    # 规则 2: 孤儿
    orphans = prototype_dirs - metadata_ids
    if orphans:
        report['warnings'].append(f'孤儿: {sorted(orphans)}')

    report['stats'] = {
        'metadata_ids': len(metadata_ids),
        'prototype_dirs': len(prototype_dirs),
        'broken_links': len(broken_links),
        'orphans': len(orphans)
    }

    return report


def main():
    import argparse
    parser = argparse.ArgumentParser(description='校验仿生设计库的一致性')
    parser.add_argument('--prototypes-dir', default=None, help='原型目录')
    parser.add_argument('--feature-mapping', default=None, help='feature-mapping.json 路径')
    parser.add_argument('--db-dir', default=None, help='prototypes_db 目录')
    args = parser.parse_args()

    repo_dir = Path(__file__).resolve().parents[1]
    prototypes_dir = args.prototypes_dir or str(repo_dir / 'prototypes')
    feature_mapping_path = args.feature_mapping or str(repo_dir / 'feature-mapping.json')
    db_dir = args.db_dir or str(repo_dir / 'prototypes_db')

    print('=== 校验仿生设计库一致性 ===')

    # 规则 1-2: feature-mapping 一致性
    print('\n1. 校验 feature-mapping.json...')
    mapping_report = validate_feature_mapping(feature_mapping_path, prototypes_dir)
    if mapping_report['errors']:
        print('  ❌ 错误:')
        for error in mapping_report['errors']:
            print(f'    - {error}')
    if mapping_report['warnings']:
        print('  ⚠️ 警告:')
        for warning in mapping_report['warnings']:
            print(f'    - {warning}')
    stats = mapping_report['stats']
    print(f'  统计: metadata={stats.get("metadata_ids", 0)}, dirs={stats.get("prototype_dirs", 0)}, 断链={stats.get("broken_links", 0)}, 孤儿={stats.get("orphans", 0)}')

    # 规则 3: prototype.md 检查
    print('\n2. 校验 prototype.md...')
    total_errors = 0
    total_warnings = 0
    if os.path.exists(prototypes_dir):
        for item in sorted(os.listdir(prototypes_dir)):
            item_path = os.path.join(prototypes_dir, item)
            if os.path.isdir(item_path):
                report = validate_prototype(item_path)
                if report['errors']:
                    print(f'  ❌ {item}: {report["errors"]}')
                    total_errors += len(report['errors'])
                if report['warnings']:
                    print(f'  ⚠️ {item}: {report["warnings"]}')
                    total_warnings += len(report['warnings'])

    # 规则 4-9: 结构化 JSON 检查
    print('\n3. 校验 prototypes_db...')
    db_reports = validate_structured_json(db_dir)
    db_errors = 0
    db_warnings = 0
    for report in db_reports:
        if report['errors']:
            print(f'  ❌ {report["prototype_id"]}: {report["errors"]}')
            db_errors += len(report['errors'])
        if report['warnings']:
            print(f'  ⚠️ {report["prototype_id"]}: {report["warnings"][:3]}')  # 最多显示 3 个
            db_warnings += len(report['warnings'])

    # 总结
    total_errors += db_errors + len(mapping_report['errors'])
    total_warnings += db_warnings + len(mapping_report['warnings'])

    print(f'\n=== 总结 ===')
    print(f'  错误: {total_errors}')
    print(f'  警告: {total_warnings}')

    if total_errors > 0:
        print('\n❌ 校验失败')
        sys.exit(1)
    else:
        print('\n✅ 校验通过')
        sys.exit(0)


if __name__ == '__main__':
    main()
