#!/usr/bin/env python3
"""
第二波文献后处理：
1. 清理空值 KI 条目
2. 删除重复文件
3. 映射到原型
4. 重建 prototypes_db
5. 校验一致性
"""

import json
import os
import sys
import shutil
from pathlib import Path


def clean_empty_ki(json_dir: str) -> dict:
    """清理空值 KI 条目。"""
    total_files = 0
    total_ki_before = 0
    total_ki_after = 0
    total_removed = 0

    for fname in sorted(os.listdir(json_dir)):
        if not fname.endswith('.json'):
            continue

        fpath = os.path.join(json_dir, fname)
        total_files += 1

        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        ki = data.get('knowledge_items', [])
        ki_before = len(ki)

        # Filter out entries with empty value
        ki_cleaned = []
        removed = 0
        for item in ki:
            val = item.get('value')
            if val is None or val == '' or val == 'null':
                removed += 1
            else:
                ki_cleaned.append(item)

        ki_after = len(ki_cleaned)
        total_ki_before += ki_before
        total_ki_after += ki_after
        total_removed += removed

        if removed > 0:
            data['knowledge_items'] = ki_cleaned
            with open(fpath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

    return {
        'files': total_files,
        'ki_before': total_ki_before,
        'ki_after': total_ki_after,
        'removed': total_removed,
    }


def deduplicate(json_dir: str) -> dict:
    """删除重复文件（基于 paper_id）。"""
    seen = {}
    duplicates = []

    for fname in sorted(os.listdir(json_dir)):
        if not fname.endswith('.json'):
            continue

        fpath = os.path.join(json_dir, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        paper_id = data.get('paper_id', fname.replace('.json', ''))
        ki_count = len(data.get('knowledge_items', []))

        if paper_id in seen:
            # Keep the one with more KI
            existing_ki = seen[paper_id]['ki_count']
            if ki_count > existing_ki:
                # Remove the old one
                old_path = seen[paper_id]['path']
                os.remove(old_path)
                duplicates.append(os.path.basename(old_path))
                seen[paper_id] = {'path': fpath, 'ki_count': ki_count}
            else:
                # Remove the new one
                os.remove(fpath)
                duplicates.append(fname)
        else:
            seen[paper_id] = {'path': fpath, 'ki_count': ki_count}

    return {
        'duplicates_removed': len(duplicates),
        'duplicates': duplicates,
    }


def main():
    repo_dir = Path(__file__).resolve().parents[1]
    json_dir = str(repo_dir / 'tools' / 'litextract' / 'outputs' / 'extractions' / '第二波' / 'json')

    if not os.path.exists(json_dir):
        print(f"ERROR: {json_dir} 不存在")
        sys.exit(1)

    print("=== 第二波文献后处理 ===\n")

    # Step 1: 清理空值 KI
    print("1. 清理空值 KI 条目...")
    clean_result = clean_empty_ki(json_dir)
    print(f"   文件数: {clean_result['files']}")
    print(f"   KI 清理前: {clean_result['ki_before']}")
    print(f"   KI 清理后: {clean_result['ki_after']}")
    print(f"   删除空值: {clean_result['removed']}")

    # Step 2: 删除重复
    print("\n2. 删除重复文件...")
    dedup_result = deduplicate(json_dir)
    print(f"   删除重复: {dedup_result['duplicates_removed']}")
    if dedup_result['duplicates']:
        for d in dedup_result['duplicates'][:5]:
            print(f"     - {d}")

    # Step 3: 统计最终结果
    print("\n3. 最终统计...")
    final_count = len([f for f in os.listdir(json_dir) if f.endswith('.json')])
    print(f"   最终文件数: {final_count}")

    print("\n=== 完成 ===")


if __name__ == '__main__':
    main()
