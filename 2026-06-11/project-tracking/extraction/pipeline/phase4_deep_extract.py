# extraction/pipeline/phase4_deep_extract.py
"""Phase 4: Deep Extraction - full extraction + weight assignment.

Produces: prototypes/<id>/prototype.md + updated feature-mapping.json

Uses concurrent processing across prototypes with load-balanced API calls.
"""

from __future__ import annotations

import json
import time
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

from config import OUTPUT_DIR, PROJECT_DIR
from llm_client import LLMClient
from pdf_utils import extract_full_text
from validators import validate_performance_data, validate_weights
from writer import generate_prototype_md, write_prototype_file, update_feature_mapping
from jinja2 import Environment, FileSystemLoader
import re

# Helper to extract numeric value from strings like "318.47 mg/g"
def _safe_float(val) -> float:
    if val is None:
        return 0.0
    if isinstance(val, (int, float)):
        return float(val)
    m = re.search(r"[\d.]+", str(val))
    return float(m.group()) if m else 0.0

_env = Environment(loader=FileSystemLoader(str(Path(__file__).parent.parent / "prompts")))
_perf_prompt = _env.get_template("deep_performance.j2")
_narr_prompt = _env.get_template("biomimetic_narrative.j2")
_weight_prompt = _env.get_template("weight_assign.j2")

# Concurrency config
MAX_PROTO_WORKERS = 4   # parallel prototypes
MAX_RETRIES = 4
RETRY_BASE_DELAY = 2.0

_progress_lock = threading.Lock()
_progress = {"done": 0, "total": 0, "errors": 0}
_write_lock = threading.Lock()  # protect feature-mapping.json writes


def _llm_call_with_retry(task_type: str, prompt: str, max_tokens: int = 4096) -> dict:
    """Make an LLM call with retry and provider switching on 429."""
    llm = LLMClient.from_task_type(task_type)
    provider = llm.provider

    for attempt in range(MAX_RETRIES + 1):
        try:
            result = llm.chat_json(prompt, max_tokens=max_tokens)
            if not isinstance(result, dict):
                result = {"_raw": str(result)[:200]}
            result["_provider"] = provider
            return result
        except Exception as e:
            err_str = str(e)
            if "429" in err_str and attempt < MAX_RETRIES:
                delay = RETRY_BASE_DELAY * (2 ** attempt)
                time.sleep(delay)
                llm = LLMClient.from_task_type(task_type, exclude_provider=provider)
                provider = llm.provider
                continue
            return {"_error": err_str[:300]}
    return {"_error": "all retries exhausted"}


def extract_performance(prototype_id: str, paper_paths: list[str]) -> dict:
    """Extract performance data concurrently from multiple papers."""
    all_results = []

    def _extract_one(path_str: str) -> dict:
        full_text = extract_full_text(Path(path_str))
        if not full_text or len(full_text.strip()) < 200:
            return None
        prompt = _perf_prompt.render(
            paper_meta=Path(path_str).stem,
            prototype_id=prototype_id,
            full_text=full_text[:8000],
        )
        return _llm_call_with_retry("performance_extract", prompt)

    with ThreadPoolExecutor(max_workers=min(len(paper_paths), 3)) as pool:
        futures = {pool.submit(_extract_one, p): p for p in paper_paths}
        for future in as_completed(futures):
            result = future.result()
            if result is not None:
                all_results.append(result)

    merged = {"_source_count": len(all_results), "_sources": [r for r in all_results if "_error" not in r]}
    if merged["_sources"]:
        # Safely extract qmax values, handling None from LLM
        qmax_values = []
        for s in merged["_sources"]:
            perf = s.get("performance_data") or {}
            qmax = perf.get("qmax") or {}
            qmax_values.append(qmax)
        best_qmax = max(qmax_values, key=lambda x: _safe_float((x or {}).get("value")), default={})
        merged["qmax"] = best_qmax
        all_mechanisms = set()
        for s in merged["_sources"]:
            m = s.get("mechanisms_identified") or []
            if m:
                all_mechanisms.update(m)
        merged["mechanisms_identified"] = list(all_mechanisms)
        for s in merged["_sources"]:
            applicability = s.get("applicability")
            if applicability and isinstance(applicability, dict):
                merged.setdefault("applicability", {}).update(applicability)
            mat_char = s.get("material_characterization")
            if mat_char and isinstance(mat_char, dict):
                merged.setdefault("material_characterization", {}).update(mat_char)
    return merged


def extract_narrative(prototype_id: str, paper_paths: list[str]) -> dict:
    """Extract biomimetic narrative from supplemented papers."""
    all_results = []
    for path_str in paper_paths:
        full_text = extract_full_text(Path(path_str))
        if not full_text or len(full_text.strip()) < 200:
            continue
        prompt = _narr_prompt.render(
            paper_meta=Path(path_str).stem,
            prototype_id=prototype_id,
            prototype_name=prototype_id.replace("-", " ").title(),
            full_text=full_text[:8000],
        )
        result = _llm_call_with_retry("biomimetic_extract", prompt, max_tokens=8192)
        all_results.append(result)

    merged = {}
    for key in ["problem_definition", "biological_solution", "key_feature_extraction", "design_mapping", "explainability_anchors", "engineering_constraints"]:
        for r in all_results:
            if key in r and r[key]:
                merged[key] = r[key]
                break
    return merged


def assign_weights(prototype_id: str, coarse_profile: dict, extraction_results: list[dict], mapping_entries: list[dict]) -> list[dict]:
    prompt = _weight_prompt.render(
        prototype_id=prototype_id, prototype_name=prototype_id.replace("-", " ").title(),
        coarse_profile_json=json.dumps(coarse_profile, ensure_ascii=False, indent=2)[:3000],
        extraction_results_json=json.dumps(extraction_results, ensure_ascii=False, indent=2)[:3000],
        mapping_entries_json=json.dumps(mapping_entries, ensure_ascii=False, indent=2)[:3000],
    )
    result = _llm_call_with_retry("weight_assign", prompt, max_tokens=8192)
    return result.get("weight_assignments", [{"_error": "no weight assignments returned"}])


def _process_one_prototype(profile_path: Path, project_dir: Path, output_dir: Path) -> dict:
    """Process one prototype: performance + narrative + weights (thread-safe)."""
    with open(profile_path, encoding="utf-8") as f:
        coarse_profile = json.load(f)

    prototype_id = coarse_profile["prototype_id"]

    # Fix: properly combine direct + indirect papers, take top 5
    all_papers = coarse_profile.get("direct_papers", []) + coarse_profile.get("indirect_papers", [])
    paper_paths = [p["path"] for p in all_papers[:5]]

    # Extract performance data
    performance = extract_performance(prototype_id, paper_paths)

    # Extract narrative from supplemented papers (if any)
    supplement_dir = Path(output_dir) / "supplemented-papers" / prototype_id
    supplement_paths = [str(p) for p in supplement_dir.glob("*.pdf")] if supplement_dir.exists() else []
    narrative = {}
    if supplement_paths:
        narrative = extract_narrative(prototype_id, supplement_paths)

    # Load mapping entries for weight assignment
    mapping_path = project_dir / "feature-mapping.json"
    try:
        with open(mapping_path, encoding="utf-8") as f:
            full_mapping = json.load(f)
        relevant_entries = [{"section": s, "entries": full_mapping.get(s, {})} for s in ["pollutant_prototype_map", "feature_prototype_map"]]
    except (FileNotFoundError, json.JSONDecodeError):
        relevant_entries = []

    # Assign weights
    extraction_results = [performance] + ([narrative] if narrative else [])
    weight_assignments = assign_weights(prototype_id, coarse_profile, extraction_results, relevant_entries)

    # Validate
    perf_errors = validate_performance_data(performance)
    weight_errors = validate_weights(weight_assignments)
    all_errors = perf_errors + weight_errors
    if all_errors:
        print(f"    WARNING: {len(all_errors)} validation errors for {prototype_id}")

    # Generate prototype.md
    applicability = performance.get("applicability", {})
    content = generate_prototype_md(prototype_id, performance, narrative, applicability)
    out_path = write_prototype_file(prototype_id, content, project_dir)

    # Update feature-mapping.json (thread-safe)
    if weight_assignments and not any("_error" in wa for wa in weight_assignments):
        with _write_lock:
            update_feature_mapping(prototype_id, weight_assignments, project_dir)

    with _progress_lock:
        _progress["done"] += 1
        done, total = _progress["done"], _progress["total"]
    print(f"  [{done}/{total}] {prototype_id} -> {out_path}")

    return {
        "prototype_id": prototype_id,
        "output_path": str(out_path),
        "performance_sources": performance.get("_source_count", 0),
        "narrative": bool(narrative),
        "weights": len(weight_assignments),
        "errors": len(all_errors),
    }


def run_phase4(output_dir: Path = None, project_dir: Path = None) -> None:
    """Execute Phase 4: Deep Extraction with concurrent prototype processing."""
    output_dir = output_dir or OUTPUT_DIR
    project_dir = project_dir or PROJECT_DIR
    profiles_dir = output_dir / "coarse-profiles"

    profile_paths = sorted(profiles_dir.glob("*.json"))
    total = len(profile_paths)

    with _progress_lock:
        _progress["done"] = 0
        _progress["total"] = total
        _progress["errors"] = 0

    print(f"Phase 4: Deep extraction on {total} prototypes ({MAX_PROTO_WORKERS} parallel)...")
    start_time = time.time()

    results = []
    with ThreadPoolExecutor(max_workers=MAX_PROTO_WORKERS) as pool:
        futures = {pool.submit(_process_one_prototype, pp, project_dir, output_dir): pp for pp in profile_paths}
        for future in as_completed(futures):
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                with _progress_lock:
                    _progress["errors"] += 1
                print(f"  ERROR: {e}")

    elapsed = time.time() - start_time
    total_errors = sum(r.get("errors", 0) for r in results)
    total_weights = sum(r.get("weights", 0) for r in results)
    print(f"\nPhase 4: {total} prototypes processed, {total_weights} weight assignments, {total_errors} validation errors, {elapsed:.1f}s total")
    print("Phase 4 complete.")
