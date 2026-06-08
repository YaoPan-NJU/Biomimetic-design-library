#!/usr/bin/env python3
"""
ADRMATS 交付验收脚本

用法：
    python tools/verify_adrmats_delivery.py

验收标准：
1. PFOA/SMX/BPA 不允许伪装成 direct evidence
2. Pb(II) 如果有 direct evidence，可以标 direct_evidence=true，但每条 evidence 必须带 verification_tier
3. candidates 里的每个候选必须能说清楚：污染物分子特征 -> 可能作用机制 -> 仿生原型机制/结构/特征 -> 传给下游的设计思路
4. needs_review 条目不得进入强排序
5. validate_consistency.py 必须 0 error
6. check_chimera.py 必须 0 violation
"""

import json
import sys
import os
import subprocess

# 设置环境变量确保 UTF-8 编码
os.environ['PYTHONUTF8'] = '1'

# 添加项目根目录到 path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.biomimetic_context import BiomimeticContext


def safe_print(text):
    """安全打印，处理编码问题"""
    try:
        print(text)
    except UnicodeEncodeError:
        # 如果编码错误，用 replace 模式
        print(text.encode('utf-8', errors='replace').decode('utf-8'))


def print_section(title):
    """打印带分隔线的标题"""
    safe_print(f"\n{'='*60}")
    safe_print(f"  {title}")
    safe_print(f"{'='*60}\n")


def validate_brief_structure(brief, test_name):
    """验证 brief 结构是否符合 schema"""
    errors = []

    # 检查 brief 外壳
    if 'brief' not in brief:
        errors.append("缺少 brief 外壳")
        return errors

    b = brief['brief']

    # 检查 context
    if 'context' not in b:
        errors.append("缺少 context")
    else:
        context = b['context']
        required_fields = ['water_quality', 'removal_target', 'pollutant_profile', 'engineering_constraints']
        for field in required_fields:
            if field not in context:
                errors.append(f"context 缺少 {field}")

        # 检查 pollutant_profile
        if 'pollutant_profile' in context:
            pp = context['pollutant_profile']
            pp_fields = ['canonical_name', 'pollutant_class', 'molecular_features', 'likely_interactions', 'profile_basis']
            for field in pp_fields:
                if field not in pp:
                    errors.append(f"pollutant_profile 缺少 {field}")

    # 检查 candidates
    if 'candidates' not in b:
        errors.append("缺少 candidates")
    else:
        candidates = b['candidates']
        if not candidates:
            errors.append("candidates 为空")

        for i, c in enumerate(candidates):
            # 检查必填字段
            required_fields = ['prototype_id', 'organism', 'match', 'mechanism', 'design_translation', 'evidence_context']
            for field in required_fields:
                if field not in c:
                    errors.append(f"candidate[{i}] 缺少 {field}")

            # 检查 match
            if 'match' in c:
                m = c['match']
                match_fields = ['reason', 'weight', 'applicability_fit', 'match_basis', 'direct_evidence']
                for field in match_fields:
                    if field not in m:
                        errors.append(f"candidate[{i}].match 缺少 {field}")

                # 检查 match_basis 是否有效
                valid_basis = ['direct_pollutant_evidence', 'pollutant_class_evidence',
                              'molecular_feature_inference', 'mechanism_feature_bridge',
                              'llm_suggested_low_confidence']
                if m.get('match_basis') not in valid_basis:
                    errors.append(f"candidate[{i}].match_basis 无效: {m.get('match_basis')}")

            # 检查 mechanism
            if 'mechanism' in c:
                mech = c['mechanism']
                mech_fields = ['name', '基本原理', 'key_structures', 'functional_groups',
                              'molecular_feature_links', 'attribution']
                for field in mech_fields:
                    if field not in mech:
                        errors.append(f"candidate[{i}].mechanism 缺少 {field}")

                # 检查 attribution
                if 'attribution' in mech:
                    attr = mech['attribution']
                    attr_fields = ['source', 'ref', 'verification_tier']
                    for field in attr_fields:
                        if field not in attr:
                            errors.append(f"candidate[{i}].mechanism.attribution 缺少 {field}")

                    # 检查 verification_tier 是否有效
                    valid_tiers = ['verified', 'corroborated', 'single_source', 'unverified', 'needs_review']
                    if attr.get('verification_tier') not in valid_tiers:
                        errors.append(f"candidate[{i}].mechanism.attribution.verification_tier 无效: {attr.get('verification_tier')}")

            # 检查 design_translation
            if 'design_translation' in c:
                dt = c['design_translation']
                dt_fields = ['idea', 'material_realization_examples', 'source_tier']
                for field in dt_fields:
                    if field not in dt:
                        errors.append(f"candidate[{i}].design_translation 缺少 {field}")

                # 检查 source_tier 是否有效
                valid_source_tiers = ['literature', 'llm_inference']
                if dt.get('source_tier') not in valid_source_tiers:
                    errors.append(f"candidate[{i}].design_translation.source_tier 无效: {dt.get('source_tier')}")

    # 检查 honesty_ledger
    if 'honesty_ledger' not in b:
        errors.append("缺少 honesty_ledger")
    else:
        hl = b['honesty_ledger']
        hl_fields = ['facts', 'leads', 'inferences']
        for field in hl_fields:
            if field not in hl:
                errors.append(f"honesty_ledger 缺少 {field}")

    return errors


def validate_direct_evidence_rules(brief, pollutant, test_name):
    """验证 direct evidence 规则"""
    errors = []

    if 'brief' not in brief:
        return errors

    b = brief['brief']
    candidates = b.get('candidates', [])

    for i, c in enumerate(candidates):
        match = c.get('match', {})
        match_basis = match.get('match_basis', '')
        direct_evidence = match.get('direct_evidence', False)

        # 规则：PFOA/SMX/BPA 不允许伪装成 direct evidence
        if pollutant in ['PFOA', 'SMX', 'BPA']:
            if direct_evidence == True:
                errors.append(f"candidate[{i}] ({c.get('prototype_id')}): {pollutant} 不允许 direct_evidence=true")
            if match_basis == 'direct_pollutant_evidence':
                errors.append(f"candidate[{i}] ({c.get('prototype_id')}): {pollutant} 不允许 match_basis=direct_pollutant_evidence")

        # 规则：direct evidence 必须带 verification_tier
        if direct_evidence == True:
            mechanism = c.get('mechanism', {})
            attribution = mechanism.get('attribution', {})
            verification_tier = attribution.get('verification_tier', '')

            if not verification_tier:
                errors.append(f"candidate[{i}] ({c.get('prototype_id')}): direct evidence 缺少 verification_tier")

    return errors


def validate_no_needs_review_in_strong_ranking(brief, test_name):
    """验证 needs_review 条目不得进入强排序"""
    errors = []

    if 'brief' not in brief:
        return errors

    b = brief['brief']
    candidates = b.get('candidates', [])

    # 检查前 5 个候选（强排序）
    for i, c in enumerate(candidates[:5]):
        mechanism = c.get('mechanism', {})
        attribution = mechanism.get('attribution', {})
        verification_tier = attribution.get('verification_tier', '')

        if verification_tier == 'needs_review':
            errors.append(f"candidate[{i}] ({c.get('prototype_id')}): needs_review 条目进入强排序")

    return errors


def run_test(pollutant, water_quality, engineering_constraints, test_name):
    """运行单个测试"""
    safe_print(f"\n--- 测试: {test_name} ---")
    safe_print(f"污染物: {pollutant}")
    safe_print(f"水质: {json.dumps(water_quality, ensure_ascii=False)}")
    safe_print(f"约束: {engineering_constraints}")

    ctx = BiomimeticContext()
    brief = ctx.query(
        pollutant=pollutant,
        water_quality=water_quality,
        engineering_constraints=engineering_constraints
    )

    # 验证结构
    structure_errors = validate_brief_structure(brief, test_name)
    evidence_errors = validate_direct_evidence_rules(brief, pollutant, test_name)
    ranking_errors = validate_no_needs_review_in_strong_ranking(brief, test_name)

    all_errors = structure_errors + evidence_errors + ranking_errors

    if all_errors:
        safe_print(f"\n[FAIL] 测试失败:")
        for error in all_errors:
            safe_print(f"  - {error}")
        return False, all_errors
    else:
        safe_print(f"\n[PASS] 测试通过")

        # 打印关键信息
        b = brief['brief']
        candidates = b.get('candidates', [])

        safe_print(f"\ncandidates 数量: {len(candidates)}")
        for i, c in enumerate(candidates[:3]):
            match = c.get('match', {})
            safe_print(f"  {i+1}. {c.get('prototype_id')}: match_basis={match.get('match_basis')}, direct_evidence={match.get('direct_evidence')}")

        # 打印 honesty_ledger
        hl = b.get('honesty_ledger', {})
        safe_print(f"\nhonesty_ledger:")
        safe_print(f"  facts: {len(hl.get('facts', []))} 条")
        safe_print(f"  leads: {len(hl.get('leads', []))} 条")
        safe_print(f"  inferences: {len(hl.get('inferences', []))} 条")

        return True, []


def main():
    """主函数"""
    print_section("ADRMATS 交付验收")

    # 测试用例
    test_cases = [
        {
            "pollutant": "PFOA",
            "water_quality": {"pH": 7, "temperature": 25, "salinity": "medium"},
            "engineering_constraints": ["水稳定性", "可再生", "低二次污染"],
            "test_name": "PFOA 痕量吸附去除"
        },
        {
            "pollutant": "SMX",
            "water_quality": {"pH": 7, "temperature": 25, "salinity": "low"},
            "engineering_constraints": [],
            "test_name": "SMX 抗生素吸附去除"
        },
        {
            "pollutant": "BPA",
            "water_quality": {"pH": 7, "temperature": 25, "salinity": "medium"},
            "engineering_constraints": [],
            "test_name": "BPA 内分泌干扰物去除"
        },
        {
            "pollutant": "Pb(II)",
            "water_quality": {"pH": 6, "temperature": 25, "salinity": "low"},
            "engineering_constraints": [],
            "test_name": "Pb(II) 重金属离子去除"
        }
    ]

    # 运行测试
    results = []
    for tc in test_cases:
        passed, errors = run_test(
            tc["pollutant"],
            tc["water_quality"],
            tc["engineering_constraints"],
            tc["test_name"]
        )
        results.append({
            "test_name": tc["test_name"],
            "passed": passed,
            "errors": errors
        })

    # 运行 validate_consistency.py
    print_section("运行 validate_consistency.py")
    try:
        result = subprocess.run(
            ["python", "tools/validate_consistency.py"],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        if "错误: 0" in result.stdout:
            safe_print("[PASS] validate_consistency.py: 0 error")
            results.append({"test_name": "validate_consistency.py", "passed": True, "errors": []})
        else:
            safe_print("[FAIL] validate_consistency.py 有错误")
            safe_print(result.stdout[-500:])
            results.append({"test_name": "validate_consistency.py", "passed": False, "errors": ["有错误"]})
    except Exception as e:
        safe_print(f"[FAIL] 运行 validate_consistency.py 失败: {e}")
        results.append({"test_name": "validate_consistency.py", "passed": False, "errors": [str(e)]})

    # 运行 check_chimera.py
    print_section("运行 check_chimera.py")
    try:
        result = subprocess.run(
            ["python", "tools/check_chimera.py"],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        if "违规原型: 0" in result.stdout:
            safe_print("[PASS] check_chimera.py: 0 violation")
            results.append({"test_name": "check_chimera.py", "passed": True, "errors": []})
        else:
            safe_print("[FAIL] check_chimera.py 有违规")
            safe_print(result.stdout[-500:])
            results.append({"test_name": "check_chimera.py", "passed": False, "errors": ["有违规"]})
    except Exception as e:
        safe_print(f"[FAIL] 运行 check_chimera.py 失败: {e}")
        results.append({"test_name": "check_chimera.py", "passed": False, "errors": [str(e)]})

    # 汇总结果
    print_section("验收结果汇总")

    passed_count = sum(1 for r in results if r["passed"])
    failed_count = len(results) - passed_count

    for r in results:
        status = "[PASS]" if r["passed"] else "[FAIL]"
        safe_print(f"{status} {r['test_name']}")
        if r["errors"]:
            for error in r["errors"]:
                safe_print(f"    - {error}")

    safe_print(f"\n总计: {passed_count} 通过, {failed_count} 失败")

    if failed_count > 0:
        safe_print("\n[FAIL] 验收失败")
        return 1
    else:
        safe_print("\n[PASS] 验收通过")
        return 0


if __name__ == "__main__":
    sys.exit(main())
