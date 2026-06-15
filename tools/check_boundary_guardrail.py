#!/usr/bin/env python3
"""
Phase 8 校验脚本：边界护栏 + gate_level 一致性

用法：
    python -X utf8 tools/check_boundary_guardrail.py

检查项目：
1. 每个 active 原型 ≥1 条 boundary（在 qualified 机制中）
2. basis≠from_source 却含数字阈值 → 数值护栏违规
3. gate_level 与 basis/verification 不一致 → 不一致
4. verification=verified 但缺少 locator → 违规
"""

import json
import glob
import re
import os
import sys

os.environ['PYTHONUTF8'] = '1'


def safe_print(text):
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode('utf-8', errors='replace').decode('utf-8'))


def check_boundary_guardrail():
    safe_print("=== Phase 8: 边界护栏校验 ===\n")

    # 加载 active 原型
    proto_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'prototypes_db')
    active_files = sorted(glob.glob(os.path.join(proto_dir, '*.json')))

    # 加载 parked 和 materials_reference 目录下的 ID，排除它们
    excluded_ids = set()
    for subdir in ['parked', 'materials_reference']:
        for f in glob.glob(os.path.join(proto_dir, subdir, '*.json')):
            with open(f, encoding='utf-8') as fp:
                d = json.load(fp)
                excluded_ids.add(d.get('id', ''))

    # 数值正则：匹配 pH 值、浓度、温度、循环次数等
    num_pattern = re.compile(
        r'pH\s*[<>]?\s*\d+\.?\d*'  # pH 值
        r'|\d+\.?\d*\s*M'           # 摩尔浓度
        r'|\d+\.?\d*\s*‰'           # 千分比浓度
        r'|\d+\.?\d*\s*°C'          # 温度
        r'|\d+\s*次循环'             # 循环次数
        r'|>\s*\d+\.?\d*'           # 大于某值
        r'|<\s*\d+\.?\d*'           # 小于某值
    )

    # 结果统计
    total_active = 0
    prototypes_without_bc = []
    numerical_violations = []
    gate_inconsistencies = []
    verified_without_locator = []
    total_bc = 0
    hard_do_not = 0
    soft_caution = 0

    for f in active_files:
        with open(f, encoding='utf-8') as fp:
            d = json.load(fp)
        pid = d.get('id', '')
        if pid in excluded_ids:
            continue
        total_active += 1

        # 找 qualified 机制（有 causal_chain 且有 transferable_principle）
        qualified_mechs = []
        for m in d.get('mechanisms', []):
            cc = m.get('causal_chain', {})
            if cc and cc.get('transferable_principle'):
                qualified_mechs.append(m)

        if not qualified_mechs:
            prototypes_without_bc.append(pid)
            continue

        # 检查 qualified 机制是否有 BC
        has_any_bc = False
        for m in qualified_mechs:
            cc = m.get('causal_chain', {})
            bcs = cc.get('boundary_conditions', [])
            if bcs:
                has_any_bc = True
            for bc in bcs:
                total_bc += 1
                bc_basis = bc.get('basis', '')
                bc_verification = bc.get('verification', '')
                bc_gate = bc.get('gate_level', '')
                bc_text = bc.get('text', '')
                locator = bc.get('locator')

                if bc_gate == 'hard':
                    hard_do_not += 1
                else:
                    soft_caution += 1

                # Check 1: numerical guardrail
                if bc_basis != 'from_source' and num_pattern.search(bc_text):
                    numerical_violations.append(f'{pid}: basis={bc_basis} 含数字 "{bc_text[:60]}"')

                # Check 2: gate_level consistency
                expected_gate = 'hard' if (bc_basis == 'from_source' and bc_verification in ('verified', 'corroborated')) else 'soft'
                if bc_gate != expected_gate:
                    gate_inconsistencies.append(f'{pid}: gate={bc_gate} 期望={expected_gate} (basis={bc_basis}, verif={bc_verification})')

                # Check 3: verified without locator
                if bc_verification == 'verified' and not locator:
                    verified_without_locator.append(f'{pid}: verification=verified 但 locator 缺失')

        if not has_any_bc:
            prototypes_without_bc.append(pid)

    # 输出结果
    safe_print(f"active 原型数: {total_active}")
    safe_print(f"总 BC 条数: {total_bc}")
    safe_print(f"  硬 DO-NOT (hard): {hard_do_not}")
    soft_with_review = 0
    # re-count for soft needs_review
    for f in active_files:
        with open(f, encoding='utf-8') as fp:
            d = json.load(fp)
        pid = d.get('id', '')
        if pid in excluded_ids:
            continue
        for m in d.get('mechanisms', []):
            cc = m.get('causal_chain', {})
            if not cc or not cc.get('transferable_principle'):
                continue
            for bc in cc.get('boundary_conditions', []):
                if bc.get('gate_level') == 'soft' and bc.get('verification') == 'needs_review':
                    soft_with_review += 1
    safe_print(f"  软 caution (soft, needs_review): {soft_with_review}")

    safe_print(f"\n--- 检查结果 ---")

    # Check: no prototype without BC
    if prototypes_without_bc:
        safe_print(f"❌ 缺少 BC 的原型 ({len(prototypes_without_bc)}): {prototypes_without_bc}")
    else:
        safe_print(f"✅ 所有 active 原型 ≥1 条 boundary")

    # Check: numerical guardrail
    if numerical_violations:
        safe_print(f"❌ 数值护栏违规 ({len(numerical_violations)}):")
        for v in numerical_violations:
            safe_print(f"  {v}")
    else:
        safe_print(f"✅ 数值阈值护栏违规=0")

    # Check: gate_level consistency
    if gate_inconsistencies:
        safe_print(f"❌ gate_level 不一致 ({len(gate_inconsistencies)}):")
        for g in gate_inconsistencies:
            safe_print(f"  {g}")
    else:
        safe_print(f"✅ gate_level 一致性: 无不一致")

    # Check: verified without locator
    if verified_without_locator:
        safe_print(f"⚠️ verified 但缺 locator ({len(verified_without_locator)}):")
        for v in verified_without_locator:
            safe_print(f"  {v}")
    else:
        safe_print(f"✅ 所有 verified BC 有 locator")

    # Summary
    safe_print(f"\n--- 总结 ---")
    issues = len(prototypes_without_bc) + len(numerical_violations) + len(gate_inconsistencies)
    if issues == 0:
        safe_print("✅ 验收通过")
        return 0
    else:
        safe_print(f"❌ 发现 {issues} 个问题")
        return 1


if __name__ == '__main__':
    sys.exit(check_boundary_guardrail())
