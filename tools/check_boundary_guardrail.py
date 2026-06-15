#!/usr/bin/env python3
"""
Phase 8 校验脚本：边界护栏 + gate_level 一致性 + schema 完整性

用法：
    python -X utf8 tools/check_boundary_guardrail.py

检查项目：
1. 每个 active 原型 ≥1 条 boundary（在 qualified 机制中）
2. BC 必填字段完整性（text, parameter, condition, basis, gate_level, verification）
3. basis 合法值：from_source | llm_inferred
4. basis=llm_inferred 时 condition.value 必须为 null（数值护栏）
5. basis≠from_source 却含数字阈值文本 → 数值护栏违规
6. gate_level 与 basis/verification 不一致 → 不一致
7. basis=from_source 时 verification 必须为 verified/corroborated，且必须有 locator
8. locator="biology knowledge" 不算真实 locator
9. verification=verified 但缺少 locator → 违规
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


# 数值正则：匹配 pH 值、浓度、温度、循环次数等
NUM_PATTERN = re.compile(
    r'pH\s*[<>]?\s*\d+\.?\d*'   # pH 值
    r'|\d+\.?\d*\s*M'            # 摩尔浓度
    r'|\d+\.?\d*\s*‰'            # 千分比浓度
    r'|\d+\.?\d*\s*°C'           # 温度
    r'|\d+\s*次循环'              # 循环次数
    r'|>\s*\d+\.?\d*'            # 大于某值
    r'|<\s*\d+\.?\d*'            # 小于某值
)

# locator 无效值（不算真实来源定位）
FAKE_LOCATORS = {'biology knowledge', 'domain knowledge', 'general knowledge', ''}


def check_boundary_guardrail():
    safe_print("=== Phase 8: 边界护栏 + schema 校验 ===\n")

    # 加载 active 原型
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    proto_dir = os.path.join(project_root, 'prototypes_db')
    active_files = sorted(glob.glob(os.path.join(proto_dir, '*.json')))

    # 排除 parked / materials_reference
    excluded_ids = set()
    for subdir in ['parked', 'materials_reference']:
        for f in glob.glob(os.path.join(proto_dir, subdir, '*.json')):
            with open(f, encoding='utf-8') as fp:
                d = json.load(fp)
                excluded_ids.add(d.get('id', ''))

    # 结果收集
    total_active = 0
    prototypes_without_bc = []
    missing_fields = []       # BC 缺必填字段
    bad_basis = []            # basis 非法值
    hidden_numeric = []       # llm_inferred + condition.value 非 null
    text_numeric = []         # llm_inferred + text 含数字
    gate_inconsistencies = [] # gate_level 不一致
    from_source_no_locator = []  # from_source 但 locator 缺失或无效
    verified_no_locator = []  # verified 但 locator 缺失
    total_bc = 0
    hard_do_not = 0
    soft_caution = 0

    required_fields = ['text', 'parameter', 'condition', 'basis', 'gate_level', 'verification']
    valid_bases = {'from_source', 'llm_inferred'}
    valid_verifications = {'verified', 'corroborated', 'needs_review'}
    valid_gates = {'hard', 'soft'}

    for f in active_files:
        with open(f, encoding='utf-8') as fp:
            d = json.load(fp)
        pid = d.get('id', '')
        if pid in excluded_ids:
            continue
        total_active += 1

        # 找 qualified 机制
        qualified_mechs = []
        for m in d.get('mechanisms', []):
            cc = m.get('causal_chain', {})
            if cc and cc.get('transferable_principle'):
                qualified_mechs.append(m)

        if not qualified_mechs:
            prototypes_without_bc.append(pid)
            continue

        has_any_bc = False
        for m in qualified_mechs:
            cc = m.get('causal_chain', {})
            bcs = cc.get('boundary_conditions', [])
            if bcs:
                has_any_bc = True
            for bc in bcs:
                total_bc += 1
                mech_name = m.get('name', '?')[:40]

                # --- 必填字段检查 ---
                missing = [k for k in required_fields if k not in bc]
                if missing:
                    missing_fields.append(f'{pid}/{mech_name}: 缺字段 {missing}')
                    continue  # 字段不全，跳过后续检查

                bc_text = bc['text']
                bc_basis = bc['basis']
                bc_verification = bc['verification']
                bc_gate = bc['gate_level']
                condition = bc.get('condition', {})
                locator = bc.get('locator')

                if bc_gate == 'hard':
                    hard_do_not += 1
                else:
                    soft_caution += 1

                # --- basis 合法值 ---
                if bc_basis not in valid_bases:
                    bad_basis.append(f'{pid}/{mech_name}: basis="{bc_basis}" (非法)')
                    continue

                # --- verification 合法值 ---
                if bc_verification not in valid_verifications:
                    bad_basis.append(f'{pid}/{mech_name}: verification="{bc_verification}" (非法)')

                # --- gate_level 合法值 ---
                if bc_gate not in valid_gates:
                    gate_inconsistencies.append(f'{pid}/{mech_name}: gate_level="{bc_gate}" (非法)')

                # --- 数值护栏：condition.value ---
                if bc_basis != 'from_source':
                    if condition.get('value') is not None:
                        hidden_numeric.append(
                            f'{pid}/{mech_name}: basis={bc_basis} 但 condition.value={condition["value"]} (op={condition.get("operator")})'
                        )

                # --- 数值护栏：text 含数字 ---
                if bc_basis != 'from_source' and NUM_PATTERN.search(bc_text):
                    text_numeric.append(f'{pid}/{mech_name}: basis={bc_basis} 含数字 "{bc_text[:60]}"')

                # --- gate_level 一致性 ---
                expected_gate = 'hard' if (bc_basis == 'from_source' and bc_verification in ('verified', 'corroborated')) else 'soft'
                if bc_gate != expected_gate:
                    gate_inconsistencies.append(
                        f'{pid}/{mech_name}: gate={bc_gate} 期望={expected_gate} (basis={bc_basis}, verif={bc_verification})'
                    )

                # --- from_source 必须有真实 locator ---
                if bc_basis == 'from_source':
                    if not locator or locator in FAKE_LOCATORS:
                        from_source_no_locator.append(
                            f'{pid}/{mech_name}: from_source 但 locator="{locator}"'
                        )
                    if bc_verification not in ('verified', 'corroborated'):
                        from_source_no_locator.append(
                            f'{pid}/{mech_name}: from_source 但 verification={bc_verification} (应为 verified/corroborated)'
                        )

                # --- verified 必须有 locator ---
                if bc_verification == 'verified':
                    if not locator or locator in FAKE_LOCATORS:
                        verified_no_locator.append(f'{pid}/{mech_name}: verified 但 locator 缺失/无效')

        if not has_any_bc:
            prototypes_without_bc.append(pid)

    # === 输出 ===
    safe_print(f"active 原型数: {total_active}")
    safe_print(f"总 BC 条数: {total_bc}")
    safe_print(f"  硬 DO-NOT (hard): {hard_do_not}")
    safe_print(f"  软 caution (soft): {soft_caution}")

    safe_print(f"\n--- 检查结果 ---")
    all_ok = True

    def check(label, violations):
        nonlocal all_ok
        if violations:
            safe_print(f"❌ {label} ({len(violations)}):")
            for v in violations:
                safe_print(f"  {v}")
            all_ok = False
        else:
            safe_print(f"✅ {label}=0")

    check("缺少 BC 的原型", prototypes_without_bc)
    check("BC 缺必填字段", missing_fields)
    check("basis 非法值", bad_basis)
    check("隐藏数值阈值 (condition.value 非 null)", hidden_numeric)
    check("text 含数字 (basis≠from_source)", text_numeric)
    check("gate_level 不一致", gate_inconsistencies)
    check("from_source 但 locator 缺失/无效", from_source_no_locator)
    check("verified 但 locator 缺失/无效", verified_no_locator)

    safe_print(f"\n--- 总结 ---")
    if all_ok:
        safe_print("✅ 验收通过")
        return 0
    else:
        safe_print("❌ 发现问题，请修复后重跑")
        return 1


if __name__ == '__main__':
    sys.exit(check_boundary_guardrail())
