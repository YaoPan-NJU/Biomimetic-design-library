# extraction/pipeline/phase2_gap_analysis.py
"""Phase 2: Gap Analysis - identify knowledge gaps per prototype.

Produces: gap-analysis/gap-reports/<id>.json + supplementation-plan.md

Uses concurrent LLM calls for depth assessment across prototypes.
"""

from __future__ import annotations

import json
import time
import threading
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

from config import OUTPUT_DIR
from llm_client import LLMClient
from pdf_utils import extract_full_text

REQUIRED_FIELDS = {
    "performance": ["qmax", "removal_rate", "kinetics", "isotherm", "selectivity", "reusability"],
    "applicability": ["ph_range", "ph_optimal", "temperature_range", "temperature_optimal", "salinity_tolerance"],
    "biomimetic_narrative": ["problem_definition", "biological_solution", "key_feature_extraction", "design_mapping", "explainability_anchors"],
    "engineering_constraints": ["antibacterial", "acid_resistance", "alkali_resistance", "recyclability", "low_cost", "high_capacity", "fast_adsorption", "high_selectivity", "easy_synthesis", "environmentally_friendly"],
}

GAP_TYPE_DATA = "data_gap"
GAP_TYPE_KNOWLEDGE = "knowledge_gap"
GAP_TYPE_WEIGHT = "weight_gap"

# Concurrency config
MAX_WORKERS = 6
MAX_RETRIES = 4
RETRY_BASE_DELAY = 2.0

_progress_lock = threading.Lock()
_progress = {"done": 0, "total": 0, "errors": 0}


def assess_breadth(coarse_profile: dict) -> dict:
    direct_count = len(coarse_profile.get("direct_papers", []))
    indirect_count = len(coarse_profile.get("indirect_papers", []))
    pollutants = coarse_profile.get("coverage", {}).get("pollutants", [])
    mechanisms = coarse_profile.get("coverage", {}).get("mechanisms", [])
    return {
        "direct_papers": direct_count, "indirect_papers": indirect_count,
        "pollutant_coverage": len(pollutants), "mechanism_coverage": len(mechanisms),
        "breadth_score": min(1.0, (direct_count * 0.3 + indirect_count * 0.1 + len(pollutants) * 0.1 + len(mechanisms) * 0.1)),
        "assessment": "sufficient" if direct_count >= 3 else "sparse" if direct_count >= 1 else "empty",
    }


def _assess_single_paper(prototype_id: str, paper: dict) -> dict:
    """Assess a single paper's field fillability (thread-safe, with retry)."""
    pdf_path = Path(paper["path"])
    full_text = extract_full_text(pdf_path)
    if not full_text or len(full_text.strip()) < 200:
        return {}

    prompt = f"""请分析以下论文，判断哪些字段可以从中提取到有效信息。
原型ID: {prototype_id}
论文: {paper.get('filename', 'unknown')}
论文全文（前5000字）:
{full_text[:5000]}

请对以下每个字段判断：can_extract/partial/cannot_extract。
性能字段: {json.dumps(REQUIRED_FIELDS['performance'])}
适用性字段: {json.dumps(REQUIRED_FIELDS['applicability'])}
仿生叙事字段: {json.dumps(REQUIRED_FIELDS['biomimetic_narrative'])}
工程约束字段: {json.dumps(REQUIRED_FIELDS['engineering_constraints'])}

输出JSON: {{"field_assessment": {{"field_name": "can_extract|partial|cannot_extract"}}}}
"""

    llm = LLMClient.from_task_type("deep_read")
    provider = llm.provider

    for attempt in range(MAX_RETRIES + 1):
        try:
            result = llm.chat_json(prompt)
            return result.get("field_assessment", {})
        except Exception as e:
            err_str = str(e)
            if "429" in err_str and attempt < MAX_RETRIES:
                delay = RETRY_BASE_DELAY * (2 ** attempt)
                time.sleep(delay)
                llm = LLMClient.from_task_type("deep_read", exclude_provider=provider)
                provider = llm.provider
                continue
            return {}


def assess_depth(prototype_id: str, coarse_profile: dict) -> dict:
    """Assess depth by concurrently checking field fillability of sample papers."""
    all_papers = coarse_profile.get("direct_papers", []) + coarse_profile.get("indirect_papers", [])
    sample_papers = sorted(all_papers, key=lambda p: (0 if p["association"] == "direct" else 1, 0 if p.get("is_review") else 1))[:3]

    field_fillability = {}

    with ThreadPoolExecutor(max_workers=min(len(sample_papers), 3)) as pool:
        futures = {pool.submit(_assess_single_paper, prototype_id, paper): paper for paper in sample_papers}
        for future in as_completed(futures):
            assessment = future.result()
            for field_name, status in assessment.items():
                field_fillability.setdefault(field_name, []).append(status)

    depth_results = {}
    for field_name, statuses in field_fillability.items():
        if "can_extract" in statuses:
            depth_results[field_name] = "fillable"
        elif "partial" in statuses:
            depth_results[field_name] = "partially_fillable"
        else:
            depth_results[field_name] = "not_fillable"

    return {"sample_papers": [p.get("filename") for p in sample_papers], "field_fillability": depth_results}


def generate_gap_report(prototype_id: str, breadth: dict, depth: dict) -> dict:
    gap_report = {"prototype_id": prototype_id, "breadth": breadth, "gaps": []}
    fillability = depth.get("field_fillability", {})

    for category in ["performance", "applicability"]:
        for field_name in REQUIRED_FIELDS[category]:
            status = fillability.get(field_name, "not_assessed")
            if status == "fillable":
                continue
            gap_type = GAP_TYPE_DATA
            action = "deep_extract_from_existing" if status == "partially_fillable" else "supplement_literature"
            gap_report["gaps"].append({"field": field_name, "category": category, "status": status, "gap_type": gap_type, "recommended_action": action, "supplement_topic": None})

    for field_name in REQUIRED_FIELDS["biomimetic_narrative"]:
        status = fillability.get(field_name, "not_fillable")
        if status != "fillable":
            gap_report["gaps"].append({"field": field_name, "category": "biomimetic_narrative", "status": status, "gap_type": GAP_TYPE_KNOWLEDGE, "recommended_action": "supplement_biomimetic_literature", "supplement_topic": f"biomimetic design {field_name} for {prototype_id}"})

    for field_name in REQUIRED_FIELDS["engineering_constraints"]:
        gap_report["gaps"].append({"field": field_name, "category": "engineering_constraints", "status": "not_fillable", "gap_type": GAP_TYPE_KNOWLEDGE, "recommended_action": "supplement_biomimetic_literature", "supplement_topic": f"engineering constraint {field_name} for biomimetic adsorbents"})

    if breadth["direct_papers"] < 3:
        gap_report["gaps"].append({"field": "weight_assignment", "category": "weight", "status": "insufficient_evidence", "gap_type": GAP_TYPE_WEIGHT, "recommended_action": "supplement_comparative_studies", "supplement_topic": f"comparative biomimetic adsorption studies involving {prototype_id}"})

    return gap_report


def _process_one_prototype(profile_path: Path, gap_dir: Path) -> dict:
    """Process one prototype: breadth + depth + gap report (thread-safe)."""
    with open(profile_path, encoding="utf-8") as f:
        coarse_profile = json.load(f)

    prototype_id = coarse_profile["prototype_id"]

    breadth = assess_breadth(coarse_profile)
    depth = assess_depth(prototype_id, coarse_profile)
    gap_report = generate_gap_report(prototype_id, breadth, depth)

    with open(gap_dir / f"{prototype_id}.json", "w", encoding="utf-8") as f:
        json.dump(gap_report, f, ensure_ascii=False, indent=2)

    with _progress_lock:
        _progress["done"] += 1
        done, total = _progress["done"], _progress["total"]
    if done % 5 == 0 or done == total:
        print(f"  [{done}/{total}] {prototype_id} done")

    return {
        "prototype_id": prototype_id,
        "gaps": gap_report["gaps"],
        "breadth": breadth,
    }


def run_phase2(output_dir: Path = None) -> None:
    """Execute Phase 2: Gap Analysis with concurrent processing."""
    output_dir = output_dir or OUTPUT_DIR
    profiles_dir = output_dir / "coarse-profiles"
    gap_dir = output_dir / "gap-analysis" / "gap-reports"
    gap_dir.mkdir(parents=True, exist_ok=True)

    profile_paths = sorted(profiles_dir.glob("*.json"))
    total = len(profile_paths)

    with _progress_lock:
        _progress["done"] = 0
        _progress["total"] = total
        _progress["errors"] = 0

    print(f"Phase 2: Running gap analysis on {total} prototypes ({MAX_WORKERS} parallel)...")

    supplement_needs = defaultdict(list)
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(_process_one_prototype, pp, gap_dir): pp for pp in profile_paths}
        for future in as_completed(futures):
            try:
                result = future.result()
                for gap in result["gaps"]:
                    if gap.get("supplement_topic"):
                        supplement_needs[gap["gap_type"]].append({
                            "prototype_id": result["prototype_id"],
                            "field": gap["field"],
                            "topic": gap["supplement_topic"],
                        })
            except Exception as e:
                with _progress_lock:
                    _progress["errors"] += 1
                print(f"  ERROR: {e}")

    elapsed = time.time() - start_time
    print(f"\nPhase 2: {total} prototypes analyzed, {_progress['errors']} errors, {elapsed:.1f}s total")

    plan_path = output_dir / "gap-analysis" / "supplementation-plan.md"
    _write_supplementation_plan(supplement_needs, plan_path)
    print(f"Phase 2 complete. Gap reports written to {gap_dir}")


def _write_supplementation_plan(needs: dict, output_path: Path) -> None:
    lines = ["## Literature Supplementation Plan (Phase 2 Output)\n"]
    for gap_type, items in sorted(needs.items()):
        lines.append(f"### {gap_type} ({len(items)} needs)\n")
        topics = {}
        for item in items:
            topics.setdefault(item["topic"], []).append(item["prototype_id"])
        for topic, prototypes in sorted(topics.items()):
            lines.append(f"- **{topic}** -> prototypes: {', '.join(prototypes)}")
        lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")
