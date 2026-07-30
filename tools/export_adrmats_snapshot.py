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
            lane = c.get("lane", "")

            # Build matching_basis text (Chinese reason from query engine)
            matching_basis = match.get("match_basis") or match.get("reason") or ""
            # If organic + no direct evidence, tag explicitly
            if organic and lane == "exploratory":
                if "exploratory" not in matching_basis.lower():
                    matching_basis = f"exploratory_no_source_evidence; {matching_basis}"

            row = {
                "pollutant_id": pid,
                "prototype_id": c.get("prototype_id", ""),
                "weight": match.get("weight", 0.0),
                "matching_basis": matching_basis,
                "direct_evidence": direct,
                "lane": lane,
                "candidate_honesty": c.get("candidate_honesty", ""),
                "performance_evidence_tier": match.get("performance_evidence_tier", "none"),
                "bound_mechanism_id": mech.get("mechanism_id", ""),
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
    fact_rows = [r for r in all_rows if r["lane"] == "fact"]
    lead_rows = [r for r in all_rows if r["lane"] == "lead"]
    exploratory_rows = [r for r in all_rows if r["lane"] == "exploratory"]

    # Spot checks
    pb_rows = [r for r in all_rows if r["pollutant_id"] == "Pb(II)"]
    pb_fact = [r for r in pb_rows if r["lane"] == "fact"]
    pb_lead = [r for r in pb_rows if r["lane"] == "lead"]

    pfoa_rows = [r for r in all_rows if r["pollutant_id"] == "PFOA"]
    pfoa_lead = [r for r in pfoa_rows if r["lane"] == "lead"]
    pfoa_exploratory = [r for r in pfoa_rows if r["lane"] == "exploratory"]

    bpa_rows = [r for r in all_rows if r["pollutant_id"] == "BPA"]
    bpa_lead = [r for r in bpa_rows if r["lane"] == "lead"]
    bpa_exploratory = [r for r in bpa_rows if r["lane"] == "exploratory"]

    stats = {
        "total_rows": len(all_rows),
        "lane_counts": {
            "fact": len(fact_rows),
            "lead": len(lead_rows),
            "exploratory": len(exploratory_rows),
        },
        "pollutants_queried": len(pollutant_set),
        "organic_pollutants": len(organic_pollutants),
        "metal_pollutants": len(metal_pollutants),
        "organic_rows_total": len(organic_rows),
        "organic_rows_exploratory": len(exploratory_organic),
        "metal_rows_total": len(metal_rows),
        "metal_rows_fact": len(fact_metal),
        "spot_check": {
            "Pb(II)": {"rows": len(pb_rows), "fact": len(pb_fact), "lead": len(pb_lead)},
            "PFOA": {"rows": len(pfoa_rows), "lead": len(pfoa_lead), "exploratory": len(pfoa_exploratory)},
            "BPA": {"rows": len(bpa_rows), "lead": len(bpa_lead), "exploratory": len(bpa_exploratory)},
        },
    }

    stats_path = os.path.join(OUTPUT_DIR, "_stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    print(f"[export] Wrote {stats_path}")

    # ── README ────────────────────────────────────────────────────────────
    readme = (
        f"# ADRMATS Match Export\n\n"
        f"由 `tools/export_adrmats_snapshot.py` 在 `{now_iso}` 从 `BiomimeticContext.query()` 生成。"
        f"这是下游集成的权威匹配快照；不要从规则文件重新推导。\n\n"
        f"## 文件\n\n"
        f"| 文件 | 用途 |\n"
        f"|---|---|\n"
        f"| `match_export.json` | 完整契约，含证据分级和绑定机制 |\n"
        f"| `match_weights.csv` | 仅用于兼容旧的五列表结构 |\n"
        f"| `_stats.json` | 行数、lane 分布和抽查统计 |\n\n"
        f"完整 JSON 的关键字段为 `lane`、`direct_evidence`、`performance_evidence_tier`、"
        f"`candidate_honesty`、`bound_mechanism_id`、`bound_mechanism`。\n\n"
        f"## 证据语义\n\n"
        f"| lane | 含义 |\n"
        f"|---|---|\n"
        f"| `fact` | 污染物特异材料去除性能严格核验，且所展示机制已核验 |\n"
        f"| `lead` | 实测去除性能有来源、定位和原文引文，但仍为 partial；或性能严格而机制待核验 |\n"
        f"| `exploratory` | 生物结合、传感、规则映射或机制类比，仅作设计启发 |\n\n"
        f"`direct_evidence=true` 只用于严格性能事实。`weight` 是同一 lane 内的相关性排序信号，"
        f"不是置信度，不应跨 lane 直接比较。\n\n"
        f"## 导出统计\n\n"
        f"- 污染物：{len(pollutant_set)}\n"
        f"- 候选行：{len(all_rows)}\n"
        f"- fact / lead / exploratory：{len(fact_rows)} / {len(lead_rows)} / {len(exploratory_rows)}\n"
        f"- Pb(II)：fact {len(pb_fact)}，lead {len(pb_lead)}\n"
        f"- PFOA：lead {len(pfoa_lead)}，exploratory {len(pfoa_exploratory)}\n"
        f"- BPA：lead {len(bpa_lead)}，exploratory {len(bpa_exploratory)}\n\n"
        f"查询条件固定为 `pH=7.0, temperature=25°C, salinity=low`，每个污染物最多返回 15 个候选。\n"
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
    print(f"PFOA:    {len(pfoa_rows)} rows — lead:{len(pfoa_lead)} exploratory:{len(pfoa_exploratory)}")
    print(f"BPA:     {len(bpa_rows)} rows — lead:{len(bpa_lead)} exploratory:{len(bpa_exploratory)}")
    return stats


if __name__ == "__main__":
    run_export()
