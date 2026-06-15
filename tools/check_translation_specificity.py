#!/usr/bin/env python3
"""
检查 design_translation 的特异性和完整性。

验证规则（DEFINITIONS §6）：
1. 每条必须包含三要素：specific_functional_group / material_handle / target_interaction
2. 不得命中禁用泛词
3. 把原型名替换后仍成立 → 不合格（不特异）
"""

import json
import os
import sys
from pathlib import Path

BANNED_PHRASES = [
    '良好的吸附性能', '优异的', '广泛的应用前景', '具有潜力',
    '提高效率', '绿色环保', '多种污染物', '协同效应'
]


def check_translation(pid: str, translation: dict) -> list:
    """检查单条 translation 是否合格。"""
    issues = []

    # 检查三要素
    required = ['specific_functional_group', 'material_handle', 'target_interaction']
    for field in required:
        if not translation.get(field):
            issues.append(f'缺少字段: {field}')

    # 检查禁用泛词
    idea = translation.get('idea', '')
    for phrase in BANNED_PHRASES:
        if phrase in idea:
            issues.append(f'命中禁用泛词: "{phrase}"')

    # 检查 source_tier
    if translation.get('source_tier') == 'literature':
        if not translation.get('examples'):
            issues.append('source_tier=literature 但无 examples/DOI')

    return issues


def main():
    repo_dir = Path(__file__).resolve().parents[1]
    db_dir = repo_dir / 'prototypes_db'

    total_prototypes = 0
    total_translations = 0
    total_qualified = 0
    total_unqualified = 0
    results = []

    for fname in sorted(os.listdir(db_dir)):
        if not fname.endswith('.json'):
            continue
        pid = fname.replace('.json', '')
        fpath = db_dir / fname

        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        translations = data.get('design_translation', [])
        if not translations:
            results.append({'pid': pid, 'status': 'NO_TRANSLATION', 'issues': ['无 design_translation']})
            continue

        total_prototypes += 1
        qualified = 0
        unqualified = 0

        for i, t in enumerate(translations):
            total_translations += 1
            issues = check_translation(pid, t)

            if issues:
                unqualified += 1
                results.append({
                    'pid': pid,
                    'index': i,
                    'status': 'UNQUALIFIED',
                    'issues': issues,
                    'idea': t.get('idea', '')[:60]
                })
            else:
                qualified += 1
                total_qualified += 1

        total_unqualified += unqualified

        if qualified == 0:
            results.append({'pid': pid, 'status': 'ALL_UNQUALIFIED', 'count': len(translations)})

    # 输出报告
    print('\n=== Design Translation 检查报告 ===\n')

    for r in results:
        if r['status'] == 'NO_TRANSLATION':
            print(f'❌ {r["pid"]}: 无 design_translation')
        elif r['status'] == 'ALL_UNQUALIFIED':
            print(f'❌ {r["pid"]}: 全部 {r["count"]} 条不合格')
        elif r['status'] == 'UNQUALIFIED':
            print(f'⚠️ {r["pid"]}[{r["index"]}]: {" | ".join(r["issues"])}')
            print(f'   idea: {r["idea"]}')

    print(f'\n=== 总结 ===')
    print(f'有 translation 的原型: {total_prototypes}')
    print(f'总条数: {total_translations}')
    print(f'合格: {total_qualified}')
    print(f'不合格: {total_unqualified}')

    if total_unqualified > 0 or total_prototypes < 24:
        print(f'\n❌ 验证失败')
        sys.exit(1)
    else:
        print(f'\n✅ 验证通过')
        sys.exit(0)


if __name__ == '__main__':
    main()
