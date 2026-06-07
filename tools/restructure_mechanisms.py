#!/usr/bin/env python3
"""
机制建模重构：区分原理级机制和实例级机制。

原理级机制 → mechanisms[] (保留)
实例级机制 → mechanism_instances[] (移出)

active_features.type: functional_group | structural_feature | process_feature
"""

import json
import os
import sys
from pathlib import Path

# 实例级数据关键词
INSTANCE_KEYWORDS = [
    '接触角', 'WCA', 'contact angle', 'water contact angle',
    '通量', 'flux', 'L/m²', 'LMH',
    'qmax', '吸附容量', 'adsorption capacity', 'mg/g',
    '去除率', 'removal rate', 'removal efficiency',
    '分离效率', 'separation efficiency',
    '孔隙率', 'porosity', 'BET',
    '拉伸强度', 'tensile strength', 'MPa',
]

# 原理级关键词
PRINCIPLE_KEYWORDS = [
    'model', 'equation', 'isotherm', 'kinetics', 'mechanism',
    '模型', '方程', '等温线', '动力学', '机理',
    'Langmuir', 'Freundlich', 'pseudo-first', 'pseudo-second',
    'Cassie-Baxter', 'Wenzel', 'Young',
    'coordination', 'chelation', 'electrostatic', 'π-π',
    '配位', '螯合', '静电', '氢键', '离子交换',
]


def classify_mechanism(mech: dict) -> str:
    """判断机制是原理级还是实例级。"""
    name = mech.get('name', '') or ''
    desc = mech.get('description', '') or ''
    text = f'{name} {desc}'.lower()

    # 检查是否包含实例级关键词
    for kw in INSTANCE_KEYWORDS:
        if kw.lower() in text:
            return 'instance'

    # 检查是否包含原理级关键词
    for kw in PRINCIPLE_KEYWORDS:
        if kw.lower() in text:
            return 'principle'

    # 默认：如果描述较短，可能是原理级；较长可能是实例级
    if len(desc) < 200:
        return 'principle'
    else:
        return 'instance'


def infer_active_features(mech: dict) -> list:
    """从机制描述中推断 active_features。"""
    features = []
    name = mech.get('name', '') or ''
    desc = mech.get('description', '') or ''
    text = f'{name} {desc}'.lower()

    # functional_group 检测
    fg_patterns = {
        'amino group (-NH2)': ['amino', '氨基', '-nh2', 'nh2'],
        'carboxyl group (-COOH)': ['carboxyl', '羧基', '-cooh', 'cooh'],
        'hydroxyl group (-OH)': ['hydroxyl', '羟基', '-oh'],
        'catechol': ['catechol', '邻苯二酚', 'dopa'],
        'thiol (-SH)': ['thiol', '巯基', '-sh'],
        'phosphonate': ['phosphonate', '膦酸'],
        'sulfonate': ['sulfonate', '磺酸'],
        'quaternary ammonium': ['quaternary ammonium', '季铵'],
    }

    for feature_name, patterns in fg_patterns.items():
        for p in patterns:
            if p in text:
                features.append({
                    'type': 'functional_group',
                    'name': feature_name,
                    'evidence': f'Detected in mechanism: {name[:50]}'
                })
                break

    # structural_feature 检测
    sf_patterns = {
        'micro-nano hierarchical structure': ['micro-nano', '微纳', 'hierarchical', '层级'],
        'porous structure': ['porous', '多孔', 'mesoporous', 'microporous'],
        'fiber structure': ['fiber', '纤维', 'nanofiber'],
        'membrane': ['membrane', '膜'],
        'coating': ['coating', '涂层'],
    }

    for feature_name, patterns in sf_patterns.items():
        for p in patterns:
            if p in text:
                features.append({
                    'type': 'structural_feature',
                    'name': feature_name,
                    'evidence': f'Detected in mechanism: {name[:50]}'
                })
                break

    # process_feature 检测
    pf_patterns = {
        'self-assembly': ['self-assembly', '自组装'],
        'biomineralization': ['biomineralization', '生物矿化'],
        'precipitation': ['precipitation', '沉淀'],
        'adsorption': ['adsorption', '吸附'],
    }

    for feature_name, patterns in pf_patterns.items():
        for p in patterns:
            if p in text:
                features.append({
                    'type': 'process_feature',
                    'name': feature_name,
                    'evidence': f'Detected in mechanism: {name[:50]}'
                })
                break

    return features


def restructure_prototype(db_path: str, dry_run: bool = False) -> dict:
    """重构单个原型的机制。"""
    with open(db_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    mechanisms = data.get('mechanisms', [])
    if not mechanisms:
        return {'id': data.get('id', '?'), 'status': 'no_mechanisms'}

    # 分类
    principle_mechs = []
    instance_mechs = []

    for m in mechanisms:
        category = classify_mechanism(m)
        if category == 'principle':
            # 推断 active_features
            if not m.get('active_features'):
                m['active_features'] = infer_active_features(m)
            principle_mechs.append(m)
        else:
            # 转换为 mechanism_instance 格式
            instance = {
                'name': m.get('name', ''),
                'description': m.get('description', ''),
                'source': m.get('source', ''),
                'ref_doi': m.get('ref_doi'),
                'source_file': m.get('source_file'),
            }
            instance_mechs.append(instance)

    result = {
        'id': data.get('id', '?'),
        'before': len(mechanisms),
        'principle': len(principle_mechs),
        'instance': len(instance_mechs),
    }

    if not dry_run:
        data['mechanisms'] = principle_mechs
        data['mechanism_instances'] = instance_mechs
        with open(db_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        result['status'] = 'saved'
    else:
        result['status'] = 'dry_run'

    return result


def main():
    import argparse
    parser = argparse.ArgumentParser(description='机制建模重构')
    parser.add_argument('--db-dir', default=None)
    parser.add_argument('--prototypes', nargs='+', default=None, help='要处理的原型 ID')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    repo_dir = Path(__file__).resolve().parents[1]
    db_dir = args.db_dir or str(repo_dir / 'prototypes_db')

    # 默认处理第一批
    targets = args.prototypes or [
        'mussel-foot-adhesion',
        'polydopamine-coating',
        'metal-organic-framework',
    ]

    print(f'=== 机制建模重构 ===')
    print(f'目标原型: {targets}')
    print(f'模式: {"dry-run" if args.dry_run else "实际执行"}')
    print()

    for pid in targets:
        db_path = os.path.join(db_dir, f'{pid}.json')
        if not os.path.exists(db_path):
            print(f'  {pid}: 文件不存在')
            continue

        result = restructure_prototype(db_path, args.dry_run)
        print(f'  {pid}:')
        print(f'    重构前: {result["before"]} 条')
        print(f'    原理级: {result["principle"]} 条')
        print(f'    实例级: {result["instance"]} 条')
        print(f'    状态: {result["status"]}')
        print()


if __name__ == '__main__':
    main()
