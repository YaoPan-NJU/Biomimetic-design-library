#!/usr/bin/env python3
"""
Phase 8: 导出 ADRMATS DO-NOT / caution 边界

用法：
    python -X utf8 tools/export_do_not.py

输出：
    exports/adrmats_do_not.json — 汇总所有 active 原型的边界条件
"""

import json
import glob
import os
import sys

os.environ['PYTHONUTF8'] = '1'


def safe_print(text):
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode('utf-8', errors='replace').decode('utf-8'))


def export_do_not():
    safe_print("=== Phase 8: 导出 DO-NOT / caution ===\n")

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    proto_dir = os.path.join(project_root, 'prototypes_db')
    export_dir = os.path.join(project_root, 'exports')

    # 加载 active 原型
    active_files = sorted(glob.glob(os.path.join(proto_dir, '*.json')))

    # 排除 parked 和 materials_reference
    excluded_ids = set()
    for subdir in ['parked', 'materials_reference']:
        for f in glob.glob(os.path.join(proto_dir, subdir, '*.json')):
            with open(f, encoding='utf-8') as fp:
                d = json.load(fp)
                excluded_ids.add(d.get('id', ''))

    # 遍历收集边界
    all_boundaries = []
    prototype_counts = {}

    for f in active_files:
        with open(f, encoding='utf-8') as fp:
            d = json.load(fp)
        pid = d.get('id', '')
        if pid in excluded_ids:
            continue

        count = 0
        for m in d.get('mechanisms', []):
            cc = m.get('causal_chain', {})
            if not cc or not cc.get('transferable_principle'):
                continue
            mech_name = m.get('name', '')
            for bc in cc.get('boundary_conditions', []):
                entry = {
                    'prototype_id': pid,
                    'mechanism_name': mech_name,
                    'parameter': bc.get('parameter', 'other'),
                    'condition': bc.get('condition', {}),
                    'text': bc.get('text', ''),
                    'gate_level': bc.get('gate_level', 'soft'),
                    'basis': bc.get('basis', ''),
                    'verification': bc.get('verification', ''),
                    'locator': bc.get('locator'),
                    'source_asset': bc.get('source_asset')
                }
                all_boundaries.append(entry)
                count += 1
        if count > 0:
            prototype_counts[pid] = count

    # 写入 exports 目录
    os.makedirs(export_dir, exist_ok=True)
    output_path = os.path.join(export_dir, 'adrmats_do_not.json')
    with open(output_path, 'w', encoding='utf-8') as fp:
        json.dump(all_boundaries, fp, ensure_ascii=False, indent=2)

    # 统计
    hard_count = sum(1 for b in all_boundaries if b['gate_level'] == 'hard')
    soft_count = sum(1 for b in all_boundaries if b['gate_level'] == 'soft')

    safe_print(f"导出完成: {output_path}")
    safe_print(f"总边界条数: {len(all_boundaries)}")
    safe_print(f"  硬 DO-NOT (hard): {hard_count}")
    safe_print(f"  软 caution (soft): {soft_count}")
    safe_print(f"涉及原型: {len(prototype_counts)}")
    safe_print(f"\n各原型边界数:")
    for pid, count in sorted(prototype_counts.items()):
        safe_print(f"  {pid}: {count}")

    return 0


if __name__ == '__main__':
    sys.exit(export_do_not())
