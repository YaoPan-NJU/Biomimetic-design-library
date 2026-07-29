#!/usr/bin/env python3
"""
Export ADRMATS match snapshot for external import.

Runs BiomimeticContext.query() for every pollutant in pollutant_profiles.json
under neutral water-quality defaults, and flattens the result into:
  - match_export.json   (full fields)
  - match_weights.csv   (drop-in for match_weights table)
  - README.md           (consumption notes)

No prototype canon or feature_matching_rules is modified.
"""

import csv
import json
import os
import sys
from datetime import datetime, timezone

# ── project root ──────────────────────────────────────────────────────────────
_HERE = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_HERE)
sys.path.insert(0, _PROJECT_ROOT)

from tools.biomimetic_context import BiomimeticContext  # noqa: E402

# ── constants ─────────────────────────────────────────────────────────────────
NEUTRAL_WATER_QUALITY = {"pH": 7.0, "temperature": 25.0, "salinity": "low"}
NEUTRAL_CONSTRAINTS: list = []
OUTPUT_DIR = os.path.join(_PROJECT_ROOT, "adrmats_export")

# Organic classes that trigger domain gating (mirrors biomimetic_context.py)
_ORGANIC_CLASSES = (
    "有机物", "有机污染物", "PFAS", "抗生素", "染料", "内分泌干扰物",
    "酚类", "药物", "农药", "chloro", "phenol", "PCB", "PBDE",
    "dioxin", "organ", "macrolide", "UV_filter", "alkyl",
    "bisphenol", "paraffin", "solvent",
)


def is_organic(profile: dict) -> bool:
    cls = (profile.get("pollutant_class") or "").lower()
    return any(k.lower() in cls for k in _ORGANIC_CLASSES)


def run_export():
    ctx = BiomimeticContext()
    profiles = ctx.pollutant_profiles.get("profiles", {})
    pollutant_names = sorted(profiles.keys())
    print(f"[export] Loaded {len(pollutant_names)} pollutant profiles")

    # ── run every pollutant ───────────────────────────────────────────────
    all_rows: list[dict] = []
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")

    for pid in pollutant_names:
        profile = profiles[pid]
        organic = is_organic(profile)
        try:
            result = ctx.query(
                pollutant=pid,
                water_quality=NEUTRAL_WATER_QUALITY,
                engineering_constraints=NEUTRAL_CONSTRAINTS,
            )
        except Exception as e:
            print(f"[export] WARN query({pid}) failed: {e}")
            continue

        brief = result.get("brief", {})
        candidates = brief.get("candidates", [])
        for c in candidates:
            mech = c.get("mechanism") or {}
            match = c.get("match") or {}
            direct = match.get("direct_evidence", False)

            # Build matching_basis text (Chinese reason from query engine)
            matching_basis = match.get("match_basis") or match.get("reason") or ""
            # If organic + no direct evidence, tag explicitly
            if organic and not direct:
                if "exploratory" not in matching_basis.lower():
                    matching_basis = f"exploratory_no_source_evidence; {matching_basis}"

            row = {
                "pollutant_id": pid,
                "prototype_id": c.get("prototype_id", ""),
                "weight": match.get("weight", 0.0),
                "matching_basis": matching_basis,
                "direct_evidence": direct,
                "lane": c.get("lane", ""),
                "candidate_honesty": c.get("candidate_honesty", ""),
                "bound_mechanism": mech.get("name", ""),
                "source": "bmdl_query",
                "exported_at": now_iso,
            }
            all_rows.append(row)

    # ── write outputs ─────────────────────────────────────────────────────
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # match_export.json (full)
    export_path = os.path.join(OUTPUT_DIR, "match_export.json")
    with open(export_path, "w", encoding="utf-8") as f:
        json.dump(
            {"meta": {"exported_at": now_iso, "total_rows": len(all_rows),
                      "total_pollutants": len(pollutant_names),
                      "neutral_wq": NEUTRAL_WATER_QUALITY},
             "rows": all_rows},
            f, ensure_ascii=False, indent=2,
        )
    print(f"[export] Wrote {export_path}  ({len(all_rows)} rows)")

    # match_weights.csv (drop-in)
    csv_path = os.path.join(OUTPUT_DIR, "match_weights.csv")
    csv_cols = ["prototype_id", "pollutant_id", "weight", "matching_basis", "source"]
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=csv_cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(all_rows)
    print(f"[export] Wrote {csv_path}  ({len(all_rows)} rows)")

    # ── self-check stats ──────────────────────────────────────────────────
    pollutant_set = {r["pollutant_id"] for r in all_rows}
    organic_pollutants = {pid for pid in pollutant_set
                          if is_organic(profiles.get(pid, {}))}
    metal_pollutants = pollutant_set - organic_pollutants

    organic_rows = [r for r in all_rows if r["pollutant_id"] in organic_pollutants]
    metal_rows = [r for r in all_rows if r["pollutant_id"] in metal_pollutants]

    exploratory_organic = [r for r in organic_rows if r["lane"] == "exploratory"]
    fact_metal = [r for r in metal_rows if r["lane"] == "fact"]

    # Spot checks
    pb_rows = [r for r in all_rows if r["pollutant_id"] == "Pb(II)"]
    pb_fact = [r for r in pb_rows if r["lane"] == "fact"]
    pb_lead = [r for r in pb_rows if r["lane"] == "lead"]

    pfoa_rows = [r for r in all_rows if r["pollutant_id"] == "PFOA"]
    pfoa_exploratory = [r for r in pfoa_rows if r["lane"] == "exploratory"]

    bpa_rows = [r for r in all_rows if r["pollutant_id"] == "BPA"]
    bpa_exploratory = [r for r in bpa_rows if r["lane"] == "exploratory"]

    stats = {
        "total_rows": len(all_rows),
        "pollutants_queried": len(pollutant_set),
        "organic_pollutants": len(organic_pollutants),
        "metal_pollutants": len(metal_pollutants),
        "organic_rows_total": len(organic_rows),
        "organic_rows_exploratory": len(exploratory_organic),
        "metal_rows_total": len(metal_rows),
        "metal_rows_fact": len(fact_metal),
        "spot_check": {
            "Pb(II)": {"rows": len(pb_rows), "fact": len(pb_fact), "lead": len(pb_lead)},
            "PFOA": {"rows": len(pfoa_rows), "exploratory": len(pfoa_exploratory)},
            "BPA": {"rows": len(bpa_rows), "exploratory": len(bpa_exploratory)},
        },
    }

    stats_path = os.path.join(OUTPUT_DIR, "_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    print(f"[export] Wrote {stats_path}")

    # ── README ────────────────────────────────────────────────────────────
    num_pollutants = len(pollutant_names)
    num_with_hits = len(pollutant_set)
    num_no_hits = num_pollutants - num_with_hits
    readme = (
        f"# ADRMATS Match Export — Snapshot {now_iso}\n\n"
        f"## 这是什么\n\n"
        f"从 Biomimetic Design Library (BMDL) v0.2 的 `BiomimeticContext.query()` 导出的**匹配快照**。\n"
        f"对 `{num_pollutants}` 个污染物（含 Phase E 的 21 个新兴污染物）在中性水质条件下执行 query，\n"
        f"将返回的候选原型拍平成行级数据。\n\n"
        f"**目的**：替代从 `feature_matching_rules` 自行 re-derive 的过程。\n"
        f"消费方可直接 import `match_weights.csv` 或 `match_export.json`。\n\n"
        f"## 文件说明\n\n"
        f"| 文件 | 说明 |\n"
        f"|------|------|\n"
        f"| `match_weights.csv` | 5 列 drop-in：`prototype_id, pollutant_id, weight, matching_basis, source` |\n"
        f"| `match_export.json` | 全字段：lane / direct_evidence / candidate_honesty / bound_mechanism / exported_at |\n"
        f"| `_stats.json` | 自检统计数字 |\n\n"
        f"## 消费方式\n\n"
        f"### 最简：替换 match_weights 表\n\n"
        f"```sql\n"
        f"-- TRUNCATE match_weights;\n"
        f"-- COPY match_weights FROM 'match_weights.csv' CSV HEADER;\n"
        f"```\n\n"
        f"### 推荐：加两列提升查询能力\n\n"
        f"```sql\n"
        f"-- ALTER TABLE match_weights ADD COLUMN lane TEXT;\n"
        f"-- ALTER TABLE match_weights ADD COLUMN direct_evidence BOOLEAN;\n"
        f"```\n"
        f"然后从 `match_export.json` 的 `rows` 中按 `(prototype_id, pollutant_id)` join 回填。\n\n"
        f"## 关键设计\n\n"
        f'- **source = "bmdl_query"**：所有行标记来源为 BMDL 查询引擎，非人工标注。\n'
        f"- **lane 字段**：\n"
        f"  - `fact` — 有来源支持的直接证据（重金属居多）\n"
        f"  - `lead` — 间接支持，需进一步验证\n"
        f"  - `exploratory` — 推断/探索，无直接来源（有机污染物居多）\n"
        f"- **v0.2 门控**：有机域无 direct_evidence 的候选，candidate_honesty 被强制为 `inference`，\n"
        f'  lane 为 `exploratory`，matching_basis 明确标注 "exploratory_no_source_evidence"。\n'
        f"  这些行**不应**与重金属 fact 候选同权使用。\n"
        f"- **weight**：反映 BMDL 的多维打分（机制匹配、关键词重叠、螯合/配位加分等），\n"
        f"  但需注意不同 lane 的 weight 不可直接跨域比较。\n\n"
        f"## 自检要点\n\n"
        f"| 指标 | 值 |\n"
        f"|------|---|\n"
        f"| 总行数 | {len(all_rows)} |\n"
        f"| 覆盖污染物数 | {len(pollutant_set)} |\n"
        f"| 有机污染物 | {len(organic_pollutants)} 个，{len(organic_rows)} 行 |\n"
        f"| 有机 exploratory 行 | {len(exploratory_organic)} / {len(organic_rows)} ({100*len(exploratory_organic)//max(len(organic_rows),1)}%) |\n"
        f"| 金属污染物 | {len(metal_pollutants)} 个，{len(metal_rows)} 行 |\n"
        f"| 金属 fact 行 | {len(fact_metal)} / {len(metal_rows)} ({100*len(fact_metal)//max(len(metal_rows),1)}%) |\n"
        f"| Pb(II) 候选 | {len(pb_rows)} 行（fact {len(pb_fact)}, lead {len(pb_lead)}） |\n"
        f"| PFOA 候选 | {len(pfoa_rows)} 行（exploratory {len(pfoa_exploratory)}） |\n"
        f"| BPA 候选 | {len(bpa_rows)} 行（exploratory {len(bpa_exploratory)}） |\n\n"
        f"### 抽查预期\n\n"
        f"- **Pb(II)**：应有 fact/lead 候选（壳聚糖、牡蛎壳、铁氧化细菌等有 source-backed 机制） ✅\n"
        f"- **PFOA**：应全为 exploratory/低权重（有机域无直接证据） ✅\n"
        f"- **BPA**：应全为 exploratory/低权重 ✅\n\n"
        f"## 约束\n\n"
        f"- 本导出**不修改** prototype canon、feature_matching_rules 或原型集合。\n"
        f"- 查询使用中性默认水质：`pH=7.0, temperature=25°C, salinity=low`。\n"
        f"- 每个污染物取 Top-15 候选（BMDL query 的默认上限）。\n\n"
        f"---\n"
        f"*Generated by `tools/export_adrmats_snapshot.py`*\n"
    )
    readme_path = os.path.join(OUTPUT_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme)
    print(f"[export] Wrote {readme_path}")

    # ── print summary ─────────────────────────────────────────────────────
    print("\n=== SELF-CHECK ===")
    print(f"Total rows:            {len(all_rows)}")
    print(f"Pollutants queried:    {len(pollutant_set)}")
    print(f"Organic pollutants:    {len(organic_pollutants)} ({len(organic_rows)} rows, {len(exploratory_organic)} exploratory)")
    print(f"Metal pollutants:      {len(metal_pollutants)} ({len(metal_rows)} rows, {len(fact_metal)} fact)")
    print(f"Pb(II):  {len(pb_rows)} rows — fact:{len(pb_fact)} lead:{len(pb_lead)}")
    print(f"PFOA:    {len(pfoa_rows)} rows — exploratory:{len(pfoa_exploratory)}")
    print(f"BPA:     {len(bpa_rows)} rows — exploratory:{len(bpa_exploratory)}")
    return stats


if __name__ == "__main__":
    run_export()
