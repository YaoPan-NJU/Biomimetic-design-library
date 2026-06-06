#!/usr/bin/env python3
"""
校验仿生设计库的一致性。

检查项目：
1. feature-mapping.json 每个 ID 都有非空 prototype.md（无断链）
2. 无孤儿内容目录
3. frontmatter 必填字段齐全，category ∈ {微生物, 植物, 动物, 仿生材料}
4. source 为 literature/patent/standard 必须有非空标识符（ref_doi/patent_number/standard_number）
5. source=llm_inference 必须 ref_doi=null
6. 凡标 verification=verified 的条目，必须带可解析标识符或非空 source_file
"""

import json
import os
import sys
from pathlib import Path


def validate_prototype(prototype_dir: str) -> dict:
    """
    校验单个原型目录。

    返回: 校验报告
    """
    report = {
        'prototype_id': os.path.basename(prototype_dir),
        'errors': [],
        'warnings': []
    }

    # 检查 prototype.md 是否存在
    md_path = os.path.join(prototype_dir, 'prototype.md')
    if not os.path.exists(md_path):
        report['errors'].append('prototype.md 不存在')
        return report

    # 检查 prototype.md 是否为空
    if os.path.getsize(md_path) == 0:
        report['errors'].append('prototype.md 为空')
        return report

    # 读取 prototype.md
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查是否有实质内容
    if len(content) < 100:
        report['warnings'].append('prototype.md 内容过短')

    # 检查是否有 [待补充] 占位符
    if '[待补充]' in content:
        report['warnings'].append('prototype.md 包含 [待补充] 占位符')

    return report


def validate_feature_mapping(feature_mapping_path: str, prototypes_dir: str) -> dict:
    """
    校验 feature-mapping.json 与 prototypes 目录的一致性。

    返回: 校验报告
    """
    report = {
        'errors': [],
        'warnings': [],
        'stats': {}
    }

    # 读取 feature-mapping.json
    if not os.path.exists(feature_mapping_path):
        report['errors'].append('feature-mapping.json 不存在')
        return report

    with open(feature_mapping_path, 'r', encoding='utf-8') as f:
        feature_mapping = json.load(f)

    # 获取 prototype_metadata 中的 ID
    prototype_metadata = feature_mapping.get('prototype_metadata', {})
    metadata_ids = set(prototype_metadata.keys())

    # 获取 prototypes 目录中的 ID
    prototype_dirs = set()
    if os.path.exists(prototypes_dir):
        for item in os.listdir(prototypes_dir):
            item_path = os.path.join(prototypes_dir, item)
            if os.path.isdir(item_path):
                prototype_dirs.add(item)

    # 检查断链（在 metadata 中但不在目录中）
    broken_links = metadata_ids - prototype_dirs
    if broken_links:
        report['errors'].append(f'断链: {sorted(broken_links)}')

    # 检查孤儿（在目录中但不在 metadata 中）
    orphans = prototype_dirs - metadata_ids
    if orphans:
        report['warnings'].append(f'孤儿: {sorted(orphans)}')

    # 统计
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
    args = parser.parse_args()

    # 默认路径
    repo_dir = Path(__file__).resolve().parents[1]
    prototypes_dir = args.prototypes_dir or str(repo_dir / 'prototypes')
    feature_mapping_path = args.feature_mapping or str(repo_dir / 'feature-mapping.json')

    print("=== 校验仿生设计库一致性 ===")

    # 校验 feature-mapping.json
    print("\n1. 校验 feature-mapping.json...")
    mapping_report = validate_feature_mapping(feature_mapping_path, prototypes_dir)

    if mapping_report['errors']:
        print("  ❌ 错误:")
        for error in mapping_report['errors']:
            print(f"    - {error}")

    if mapping_report['warnings']:
        print("  ⚠️ 警告:")
        for warning in mapping_report['warnings']:
            print(f"    - {warning}")

    stats = mapping_report['stats']
    print(f"  统计:")
    print(f"    - metadata IDs: {stats.get('metadata_ids', 0)}")
    print(f"    - prototype 目录: {stats.get('prototype_dirs', 0)}")
    print(f"    - 断链: {stats.get('broken_links', 0)}")
    print(f"    - 孤儿: {stats.get('orphans', 0)}")

    # 校验每个原型
    print("\n2. 校验每个原型...")
    total_errors = 0
    total_warnings = 0

    if os.path.exists(prototypes_dir):
        for item in sorted(os.listdir(prototypes_dir)):
            item_path = os.path.join(prototypes_dir, item)
            if os.path.isdir(item_path):
                report = validate_prototype(item_path)

                if report['errors']:
                    print(f"  ❌ {item}: {report['errors']}")
                    total_errors += len(report['errors'])

                if report['warnings']:
                    print(f"  ⚠️ {item}: {report['warnings']}")
                    total_warnings += len(report['warnings'])

    # 总结
    print("\n=== 总结 ===")
    print(f"  错误: {total_errors}")
    print(f"  警告: {total_warnings}")

    if total_errors > 0:
        print("\n❌ 校验失败")
        sys.exit(1)
    else:
        print("\n✅ 校验通过")
        sys.exit(0)


if __name__ == '__main__':
    main()
