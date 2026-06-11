#!/usr/bin/env python3
"""Generate prototype.md files from aggregated extraction data.

Usage:
    python3 generate_prototype_md.py --input-dir outputs/aggregated --biomimetic-lib /path/to/Biomimetic-design-library
"""

import argparse
import json
import os
from pathlib import Path


def generate_frontmatter(prototype_id: str, data: dict) -> str:
    """Generate YAML frontmatter block."""
    pollutants = sorted(set(
        p.get("pollutant", "") for p in data.get("performance_data", [])
        if p.get("pollutant")
    ))
    mechanisms = sorted(set(
        m.get("mechanism_name", "") for m in data.get("mechanism_analysis", [])
        if m.get("mechanism_name")
    ))
    features = sorted(set(
        fg.get("group", "")
        for chain_item in data.get("biomimetic_design_chains", [])
        for fg in chain_item.get("chain", {}).get("key_functional_groups", [])
        if fg.get("group")
    ))

    # Determine qmax range
    qmax_values = [
        p.get("qmax_mg_g") for p in data.get("performance_data", [])
        if p.get("qmax_mg_g") is not None
    ]
    qmax_range = ""
    if qmax_values:
        qmax_range = f"{min(qmax_values):.1f}~{max(qmax_values):.1f} mg/g"

    # Determine engineering constraints
    constraints = data.get("engineering_constraints", [])
    constraint_lines = []
    for c in constraints:
        constraint_lines.append(
            f"  - constraint: {c.get('constraint', '')}\n"
            f"    relevance: {c.get('assessment', 'medium')}\n"
            f"    explanation: {c.get('explanation', '')}"
        )

    pollutants_str = json.dumps(pollutants, ensure_ascii=False) if pollutants else "[]"
    mechanisms_str = json.dumps(mechanisms, ensure_ascii=False) if mechanisms else "[]"
    features_str = json.dumps(features, ensure_ascii=False) if features else "[]"
    constraints_str = "\n".join(constraint_lines) if constraint_lines else "  []"

    lines = [
        "---",
        f"id: {prototype_id}",
        f"name: {prototype_id}",
        f"features: {features_str}",
        f"pollutants: {pollutants_str}",
        f"adsorption_mechanisms: {mechanisms_str}",
        f'qmax_range: "{qmax_range}"' if qmax_range else 'qmax_range: "待补充"',
        'removal_rate: "待补充"',
        "applicability:",
        "  pH_range: [待补充, 待补充]",
        "  temp_range: [待补充, 待补充]",
        "  salinity: 待补充",
        "evidence_level: medium",
        "engineering_constraints:",
        constraints_str,
        "---",
    ]
    return "\n".join(lines)


def generate_section1_intro(prototype_id: str, data: dict) -> str:
    """Section 1: Biological Prototype Introduction."""
    chains = data.get("biomimetic_design_chains", [])
    if chains:
        chain = chains[0].get("chain", {})
        challenge = chain.get("nature_challenge", "待补充")
        strategy = chain.get("evolutionary_strategy", "待补充")
        intro = f"{challenge}\n\n{strategy}"
    else:
        intro = "[待补充：生物原型简介，200-300字]"

    return f"## 1. 生物原型简介\n\n{intro}"


def generate_section2_mechanisms(data: dict) -> str:
    """Section 2: Adsorption Mechanism Details."""
    mechanisms = data.get("mechanism_analysis", [])
    if not mechanisms:
        return "## 2. 吸附机制详解\n\n[待补充]"

    sections = ["## 2. 吸附机制详解"]
    seen = set()
    for i, mech in enumerate(mechanisms, 1):
        name = mech.get("mechanism_name", f"机制{i}")
        if name in seen:
            continue
        seen.add(name)

        phenomenon = mech.get("phenomenon", "待补充")
        mol_basis = "\n".join(
            f"- {b}" for b in mech.get("molecular_basis", ["待补充"])
        )
        fg_lines = "\n".join(
            f"- {fg.get('group', '')} → {fg.get('role', '')}"
            for fg in mech.get("key_functional_groups", [])
        ) or "- 待补充"
        inspiration = mech.get("biomimetic_inspiration", "待补充")
        evidence = mech.get("supporting_evidence", "待补充")

        sections.append(
            f"\n### 机制{i}：{name}\n\n"
            f"**现象**：{phenomenon}\n\n"
            f"**分子基础**：\n{mol_basis}\n\n"
            f"**关键官能团**：\n{fg_lines}\n\n"
            f"**仿生设计启示**：\n- {inspiration}\n\n"
            f"**支持证据**：{evidence}"
        )
    return "\n".join(sections)


def generate_section3_structure(data: dict) -> str:
    """Section 3: Structural Features."""
    sf_list = data.get("structural_features", [])
    if not sf_list:
        return (
            "## 3. 结构特征与结构-功能关系\n\n"
            "### 多尺度结构描述\n\n"
            "| 尺度 | 特征 | 尺寸范围 | 功能作用 |\n"
            "|------|------|----------|----------|\n"
            "| 宏观 | 待补充 | 待补充 | 待补充 |\n"
            "| 介观 | 待补充 | 待补充 | 待补充 |\n"
            "| 微观 | 待补充 | 待补充 | 待补充 |\n"
            "| 纳米 | 待补充 | 待补充 | 待补充 |\n"
        )

    sf = sf_list[0].get("features", {})
    scales = ["macro_scale", "meso_scale", "micro_scale", "nano_scale"]
    scale_names = {"macro_scale": "宏观", "meso_scale": "介观", "micro_scale": "微观", "nano_scale": "纳米"}

    table_rows = []
    for s in scales:
        info = sf.get(s) or {}
        table_rows.append(
            f"| {scale_names[s]} | {info.get('feature', '待补充')} "
            f"| {info.get('size_range', '待补充')} "
            f"| {info.get('function', '待补充')} |"
        )

    sfr = sf.get("structure_function_relationship", "待补充")

    return (
        "## 3. 结构特征与结构-功能关系\n\n"
        "### 多尺度结构描述\n\n"
        "| 尺度 | 特征 | 尺寸范围 | 功能作用 |\n"
        "|------|------|----------|----------|\n"
        + "\n".join(table_rows) + "\n\n"
        f"### 结构-功能关系\n\n{sfr}"
    )


def generate_section4_performance(data: dict) -> str:
    """Section 4: Performance Data Table."""
    perf = data.get("performance_data", [])
    if not perf:
        return "## 4. 已报道性能数据\n\n[暂无可靠文献数据，待补充]"

    header = "| 污染物 | 材料形态 | 去除率(%) | qmax(mg/g) | pH | 温度(°C) | 数据来源 | 文献 |\n"
    header += "|--------|----------|-----------|------------|-----|----------|----------|------|\n"
    rows = []
    seen = set()
    for p in perf:
        key = (p.get("pollutant", ""), p.get("qmax_mg_g"), p.get("reference", ""))
        if key in seen:
            continue
        seen.add(key)
        qmax = f"{p['qmax_mg_g']:.1f}" if p.get("qmax_mg_g") is not None else "-"
        rr = f"{p['removal_rate_pct']:.1f}" if p.get("removal_rate_pct") is not None else "-"
        ph = f"{p['pH']:.1f}" if p.get("pH") is not None else "-"
        temp = f"{p['temperature_C']:.0f}" if p.get("temperature_C") is not None else "-"
        rows.append(
            f"| {p.get('pollutant', '-')} "
            f"| {p.get('material_form', '-')} "
            f"| {rr} "
            f"| {qmax} "
            f"| {ph} "
            f"| {temp} "
            f"| {p.get('data_source', '-')} "
            f"| {p.get('reference', '-')} |"
        )
    return "## 4. 已报道性能数据\n\n" + header + "\n".join(rows)


def generate_section5_narrative(data: dict) -> str:
    """Section 5: Biomimetic Design Narrative."""
    chains = data.get("biomimetic_design_chains", [])
    if not chains:
        return (
            "## 5. 仿生设计叙事\n\n"
            "### 5.1 问题定义\n\n[待补充]\n\n"
            "### 5.2 生物解决方案\n\n[待补充]\n\n"
            "### 5.3 关键特征提取\n\n[待补充]\n\n"
            "### 5.4 设计思路映射\n\n[待补充]\n\n"
            "### 5.5 可解释性锚点\n\n[待补充]"
        )

    chain = chains[0].get("chain", {})

    # 5.1 Problem
    nature_challenge = chain.get("nature_challenge", "待补充")

    # 5.2 Biological Solution
    evo_strategy = chain.get("evolutionary_strategy", "待补充")
    mechanisms = "\n".join(
        f"- {m}" for m in chain.get("key_mechanisms", ["待补充"])
    )

    # 5.3 Key Features
    must_keep = "\n".join(
        f"- **{f.get('feature', '')}**：{f.get('reason', '')}"
        for f in chain.get("must_keep_features", [])
    ) or "- 待补充"
    adjustable = "\n".join(
        f"- **{f.get('feature', '')}**：{f.get('adjustment_range', '')}"
        for f in chain.get("adjustable_features", [])
    ) or "- 待补充"

    # 5.4 Design Mapping
    bio_map = "\n".join(
        f"- {m.get('bio_feature', '')} → {m.get('material_design', '')}"
        for m in chain.get("bio_to_material_mapping", [])
    ) or "- 待补充"

    # 5.5 Explainability
    one_liner = chain.get("one_line_story", "待补充")
    trace = chain.get("design_traceability", "待补充")

    return (
        "## 5. 仿生设计叙事\n\n"
        f"### 5.1 问题定义\n\n**自然界中的挑战**：{nature_challenge}\n\n"
        f"### 5.2 生物解决方案\n\n**进化策略**：{evo_strategy}\n\n"
        f"**关键机制**：\n{mechanisms}\n\n"
        f"### 5.3 关键特征提取\n\n"
        f"**必须保留的特征**：\n{must_keep}\n\n"
        f"**可灵活调整的特征**：\n{adjustable}\n\n"
        f"### 5.4 设计思路映射\n\n**从生物到材料**：\n{bio_map}\n\n"
        f"### 5.5 可解释性锚点\n\n"
        f"**仿生故事线**：{one_liner}\n\n"
        f"**设计溯源**：{trace}"
    )


def generate_section6_scenarios(data: dict) -> str:
    """Section 6: Applicable Scenarios."""
    constraints = data.get("engineering_constraints", [])
    if constraints:
        suitable = [c["constraint"] for c in constraints if c.get("assessment") == "high"]
        suitable_str = "、".join(suitable) if suitable else "待补充"
    else:
        suitable_str = "待补充"

    return (
        "## 6. 适用场景\n\n"
        f"**最适合**：{suitable_str}\n\n"
        "**不适用的情况**：待补充"
    )


def generate_section7_related(data: dict) -> str:
    """Section 7: Related Prototypes."""
    return "## 7. 相关原型\n\n- 待补充"


def generate_references(data: dict) -> str:
    """References section from paper list."""
    papers = data.get("papers", [])
    if not papers:
        return "## 参考文献\n\n[待补充]"
    refs = [f"[{i+1}] {p.get('paper_id', 'unknown')}" for i, p in enumerate(papers)]
    return "## 参考文献\n\n" + "\n".join(refs)


def generate_prototype_md(prototype_id: str, data: dict) -> str:
    """Generate complete prototype.md content."""
    parts = [
        generate_frontmatter(prototype_id, data),
        "",
        f"# {prototype_id}",
        "",
        generate_section1_intro(prototype_id, data),
        "",
        generate_section2_mechanisms(data),
        "",
        generate_section3_structure(data),
        "",
        generate_section4_performance(data),
        "",
        generate_section5_narrative(data),
        "",
        generate_section6_scenarios(data),
        "",
        generate_section7_related(data),
        "",
        generate_references(data),
    ]
    return "\n".join(parts)


def main():
    parser = argparse.ArgumentParser(description="Generate prototype.md files")
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument(
        "--biomimetic-lib",
        type=Path,
        default=Path(os.environ.get(
            "BIOMIMETIC_LIB",
            Path(__file__).resolve().parent.parent.parent,
        )),
    )
    parser.add_argument("--dry-run", action="store_true", help="Print output instead of writing")
    args = parser.parse_args()

    proto_dir = args.biomimetic_lib / "prototypes"
    written = 0

    for json_file in sorted(args.input_dir.glob("*.json")):
        proto_id = json_file.stem
        with open(json_file, encoding="utf-8") as f:
            data = json.load(f)

        md = generate_prototype_md(proto_id, data)

        if args.dry_run:
            print(f"=== {proto_id} ===")
            print(md[:500])
            print("...")
        else:
            target_dir = proto_dir / proto_id
            target_dir.mkdir(parents=True, exist_ok=True)
            target_path = target_dir / "prototype.md"
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(md)
            written += 1
            print(f"  Written: {target_path}")

    if not args.dry_run:
        print(f"\nGenerated {written} prototype.md files")


if __name__ == "__main__":
    main()
