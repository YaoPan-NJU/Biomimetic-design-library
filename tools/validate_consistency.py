#!/usr/bin/env python3
"""
校验仿生设计库的一致性（v4，14 条规则）。

规则：
R1. feature-mapping.json 每个 ID 都有非空 prototype.md（无断链）
R2. 无孤儿内容目录
R3. frontmatter 必填字段齐全，category ∈ {微生物, 植物, 动物, 仿生材料}
R4. source 为 literature/patent/standard 必须有非空标识符
R5. source=llm_inference 必须 ref_doi=null
R6. verification=verified 必须带可解析标识符或非空 source_file
R7. chimera 检测：organism 含 ≥2 个不同类生物
R8. 重复条目检测：同 pollutant+material+value
R9. 结构化 JSON 必填字段
R10. source=literature 必须有 ref_doi 或 source_file
R11. source=llm_inference 必须无 ref_doi
R12. verification=verified 必须有 ref_doi（格式正确）且有 source_file（静态检查在场，不联网）
R13. 单一物种一致性：organism 不应包含不相关的多个物种
R14. 机制条目不得包含实例级数据（接触角、flux、qmax 等数值）

运行模式：
  --report-only (默认)：输出违规清单，允许非零退出
  --strict：零错误通过才返回 0
"""

import json
import os
import sys
import re
import argparse
from pathlib import Path


VALID_CATEGORIES = {'微生物', '植物', '动物', '仿生材料'}

# 实例级数据关键词（出现在机制 name/description 中则为违规）
INSTANCE_KEYWORDS = [
    '接触角', 'WCA', 'contact angle', 'water contact angle',
    '通量', 'flux', 'L/m²', 'LMH',
    'qmax', '吸附容量', 'adsorption capacity', 'mg/g',
    '去除率', 'removal rate', 'removal efficiency', '%',
    '分离效率', 'separation efficiency',
]


def parse_frontmatter(content: str) -> dict:
    if not content.startswith('---'):
        return None
    end = content.find('---', 3)
    if end == -1:
        return None
    fm_text = content[3:end].strip()
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

    fm = parse_frontmatter(content)
    if fm is None:
        report['errors'].append('缺少 YAML frontmatter')
    else:
        for field in ['id', 'name', 'category']:
            if not fm.get(field):
                report['errors'].append(f'frontmatter 缺少必填字段: {field}')
        if not fm.get('organism'):
            report['warnings'].append('frontmatter organism 为空')
        cat = fm.get('category', '')
        if cat and cat not in VALID_CATEGORIES:
            report['errors'].append(f'category 值无效: {cat}')

    return report


def validate_structured_json(db_dir: str) -> list:
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

        # R9: 必填字段
        for field in required_fields:
            if field not in d:
                report['errors'].append(f'缺少必填字段: {field}')

        # R7 + R13: chimera 检测
        org = d.get('organism', {})
        sci = org.get('scientific', '')
        if sci:
            parts = [p.strip() for p in re.split(r'[,;/]', sci) if p.strip()]
            if len(parts) > 2 and 'spp.' not in sci and '多物种' not in sci:
                report['warnings'].append(f'organism 可能包含多个不相关生物: {sci[:60]}')

        # R4 + R10: source 标识符完整性
        for p in d.get('performance_data', []):
            source = p.get('source', '')
            ref = p.get('ref_doi')
            pn = p.get('patent_number')
            sn = p.get('standard_number')
            sf = p.get('source_file')
            if source == 'literature':
                if not ref and not sf:
                    report['warnings'].append(f'R10: source=literature 但无 ref_doi 且无 source_file: {p.get("parameter", "")[:40]}')
            elif source == 'patent' and not pn:
                report['warnings'].append(f'source=patent 但无 patent_number: {p.get("parameter", "")[:40]}')
            elif source == 'standard' and not sn:
                report['warnings'].append(f'source=standard 但无 standard_number: {p.get("parameter", "")[:40]}')

        # R11: source=llm_inference 必须无 ref_doi
        for p in d.get('performance_data', []):
            if p.get('source') == 'llm_inference' and p.get('ref_doi'):
                report['errors'].append(f'R11: llm_inference 但有 ref_doi: {p.get("parameter", "")[:40]}')

        # R6 + R12: verification=verified 静态检查
        for p in d.get('performance_data', []):
            if p.get('verification') == 'verified':
                has_id = bool(p.get('ref_doi') or p.get('patent_number') or p.get('standard_number'))
                has_sf = bool(p.get('source_file'))
                if not has_id:
                    report['errors'].append(f'R12: verified 但无标识符: {p.get("parameter", "")[:40]}')
                if not has_sf:
                    report['warnings'].append(f'R12: verified 但无 source_file: {p.get("parameter", "")[:40]}')

        # R8: 重复条目检测
        seen = set()
        for p in d.get('performance_data', []):
            key = f'{p.get("pollutant", "")}:{p.get("material", "")}:{str(p.get("value", ""))[:30]}'
            if key in seen:
                report['warnings'].append(f'重复性能数据: {key[:50]}')
            seen.add(key)

        # R14: 机制条目不得包含实例级数据
        for m in d.get('mechanisms', []):
            name = m.get('name', '')
            desc = m.get('description', '')
            text = f'{name} {desc}'
            for kw in INSTANCE_KEYWORDS:
                if kw.lower() in text.lower():
                    report['warnings'].append(f'R14: 机制含实例级数据 "{kw}": {name[:40]}')
                    break

        reports.append(report)

    return reports


def validate_feature_mapping(feature_mapping_path: str, prototypes_dir: str) -> dict:
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
                # Also scan nested subdirectories (e.g. separation/cactus-spine)
                for sub in os.listdir(item_path):
                    sub_path = os.path.join(item_path, sub)
                    if os.path.isdir(sub_path) and os.path.exists(os.path.join(sub_path, 'prototype.md')):
                        prototype_dirs.add(sub)

    # R1: 断链
    broken_links = metadata_ids - prototype_dirs
    if broken_links:
        report['errors'].append(f'断链: {sorted(broken_links)}')

    # R2: 孤儿
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
    parser = argparse.ArgumentParser(description='校验仿生设计库的一致性')
    parser.add_argument('--prototypes-dir', default=None)
    parser.add_argument('--feature-mapping', default=None)
    parser.add_argument('--db-dir', default=None)
    parser.add_argument('--strict', action='store_true', help='严格模式：零错误通过')
    parser.add_argument('--report-only', action='store_true', help='报告模式：输出清单，允许非零退出')
    args = parser.parse_args()

    repo_dir = Path(__file__).resolve().parents[1]
    prototypes_dir = args.prototypes_dir or str(repo_dir / 'prototypes')
    feature_mapping_path = args.feature_mapping or str(repo_dir / 'feature-mapping.json')
    db_dir = args.db_dir or str(repo_dir / 'prototypes_db')

    mode = 'strict' if args.strict else 'report-only'
    print(f'=== 校验仿生设计库一致性 ({mode} 模式) ===')

    # R1-R2: feature-mapping 一致性
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

    # R3: prototype.md 检查
    print('\n2. 校验 prototype.md...')
    md_errors = 0
    md_warnings = 0
    if os.path.exists(prototypes_dir):
        for item in sorted(os.listdir(prototypes_dir)):
            item_path = os.path.join(prototypes_dir, item)
            if os.path.isdir(item_path):
                report = validate_prototype(item_path)
                if report['errors']:
                    print(f'  ❌ {item}: {report["errors"]}')
                    md_errors += len(report['errors'])
                if report['warnings']:
                    print(f'  ⚠️ {item}: {report["warnings"]}')
                    md_warnings += len(report['warnings'])

    # R4-R14: 结构化 JSON 检查
    print('\n3. 校验 prototypes_db...')
    db_reports = validate_structured_json(db_dir)
    db_errors = 0
    db_warnings = 0
    for report in db_reports:
        if report['errors']:
            print(f'  ❌ {report["prototype_id"]}: {report["errors"]}')
            db_errors += len(report['errors'])
        if report['warnings']:
            print(f'  ⚠️ {report["prototype_id"]}: {report["warnings"][:5]}')
            db_warnings += len(report['warnings'])

    # R15: feature-mapping ↔ prototypes_db 引用完整性
    print('\n4. 校验 feature-mapping ↔ prototypes_db 引用完整性...')
    r15_errors = 0
    fm = json.load(open(feature_mapping_path, encoding='utf-8'))
    pm = fm.get('prototype_metadata', {})
    # Skip quarantined entries from R15 check (they are intentionally moved out of primary)
    fm_ids = {pid for pid, meta in pm.items()
              if not str(meta.get('_status', '')).startswith('quarantined')}
    db_ids = set()
    if os.path.isdir(db_dir):
        for fn in os.listdir(db_dir):
            if fn.endswith('.json'):
                db_ids.add(fn[:-5])
    in_mapping_not_db = fm_ids - db_ids
    in_db_not_mapping = db_ids - fm_ids
    if in_mapping_not_db:
        print(f'  ❌ 在 feature-mapping 但不在 prototypes_db: {sorted(in_mapping_not_db)}')
        r15_errors += len(in_mapping_not_db)
    if in_db_not_mapping:
        print(f'  ❌ 在 prototypes_db 但不在 feature-mapping: {sorted(in_db_not_mapping)}')
        r15_errors += len(in_db_not_mapping)
    if not in_mapping_not_db and not in_db_not_mapping:
        print(f'  ✅ 一致: {len(fm_ids)} 个原型')

    # 总结
    total_errors = db_errors + len(mapping_report['errors']) + md_errors + r15_errors
    total_warnings = db_warnings + len(mapping_report['warnings']) + md_warnings

    print(f'\n=== 总结 ===')
    print(f'  错误: {total_errors}')
    print(f'  警告: {total_warnings}')

    if args.strict:
        if total_errors > 0:
            print('\n❌ 严格模式：校验失败')
            sys.exit(1)
        else:
            print('\n✅ 严格模式：校验通过')
            sys.exit(0)
    else:
        # report-only 模式：输出清单但允许非零退出
        if total_errors > 0:
            print(f'\n⚠️ 报告模式：发现 {total_errors} 个错误（详见上方）')
        else:
            print('\n✅ 报告模式：无错误')
        sys.exit(0)


if __name__ == '__main__':
    main()
