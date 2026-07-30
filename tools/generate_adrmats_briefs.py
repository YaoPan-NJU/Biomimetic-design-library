#!/usr/bin/env python3
"""
生成 ADRMATS 真实接口 brief

用法：
    python tools/generate_adrmats_briefs.py

输出：
    examples/adrmats_briefs/ 目录下的 JSON 文件
"""

import json
import sys
import os

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
        print(text.encode('utf-8', errors='replace').decode('utf-8'))


def generate_brief(pollutant, water_quality, engineering_constraints, test_name, output_dir):
    """生成单个 brief"""
    safe_print(f"\n生成 {test_name}...")

    ctx = BiomimeticContext()
    result = ctx.query(
        pollutant=pollutant,
        water_quality=water_quality,
        engineering_constraints=engineering_constraints
    )

    # 保存到文件
    filename = f"{test_name.lower().replace(' ', '_')}.json"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    safe_print(f"  保存到: {filepath}")

    # 验证
    brief = result.get('brief', {})
    context = brief.get('context', {})
    pp = context.get('pollutant_profile', {})
    candidates = brief.get('candidates', [])
    hl = brief.get('honesty_ledger', {})

    safe_print(f"  canonical_name: {pp.get('canonical_name')}")
    safe_print(f"  candidates 数量: {len(candidates)}")
    safe_print(f"  facts: {len(hl.get('facts', []))} 条")
    safe_print(f"  leads: {len(hl.get('leads', []))} 条")
    safe_print(f"  inferences: {len(hl.get('inferences', []))} 条")

    # 检查 PFOA/SMX/BPA 是否保持 direct_evidence=false
    if pollutant in ['PFOA', 'SMX', 'BPA']:
        for c in candidates:
            match = c.get('match', {})
            if match.get('direct_evidence') == True:
                safe_print(f"  [ERROR] {pollutant} 不允许 direct_evidence=true")
                return False
        safe_print(f"  [PASS] {pollutant} 保持 direct_evidence=false")

    return True


def main():
    """主函数"""
    safe_print("=" * 60)
    safe_print("  生成 ADRMATS 真实接口 brief")
    safe_print("=" * 60)

    output_dir = "examples/adrmats_briefs"
    os.makedirs(output_dir, exist_ok=True)

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
        },
        {
            "pollutant": "Cr(VI)",
            "water_quality": {"pH": 3, "temperature": 25, "salinity": "low"},
            "engineering_constraints": ["酸性条件耐受"],
            "test_name": "Cr(VI) 六价铬去除"
        },
        {
            "pollutant": "Methylene Blue",
            "water_quality": {"pH": 7, "temperature": 25, "salinity": "low"},
            "engineering_constraints": [],
            "test_name": "亚甲基蓝染料去除"
        },
        {
            "pollutant": "oil-water",
            "water_quality": {"pH": 7, "temperature": 25, "salinity": "medium"},
            "engineering_constraints": ["超疏水/超亲油"],
            "test_name": "油水分离"
        }
    ]

    # 生成 brief
    results = []
    for tc in test_cases:
        passed = generate_brief(
            tc["pollutant"],
            tc["water_quality"],
            tc["engineering_constraints"],
            tc["test_name"],
            output_dir
        )
        results.append({
            "test_name": tc["test_name"],
            "passed": passed
        })

    # 汇总结果
    safe_print("\n" + "=" * 60)
    safe_print("  生成结果汇总")
    safe_print("=" * 60)

    passed_count = sum(1 for r in results if r["passed"])
    failed_count = len(results) - passed_count

    for r in results:
        status = "[PASS]" if r["passed"] else "[FAIL]"
        safe_print(f"{status} {r['test_name']}")

    safe_print(f"\n总计: {passed_count} 通过, {failed_count} 失败")

    if failed_count > 0:
        safe_print("\n[FAIL] 生成失败")
        return 1
    else:
        safe_print("\n[PASS] 所有 brief 生成成功")
        return 0


if __name__ == "__main__":
    sys.exit(main())
