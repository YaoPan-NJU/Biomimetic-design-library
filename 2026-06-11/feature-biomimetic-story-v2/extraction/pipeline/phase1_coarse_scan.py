# extraction/pipeline/phase1_coarse_scan.py
"""Phase 1: Coarse Scan - lightweight extraction from all papers.

Produces: coarse-profiles/<prototype_id>.json + coverage-heatmap.md

Uses concurrent LLM calls for speed: papers within a prototype run in parallel,
and multiple prototypes run in parallel via ThreadPoolExecutor.
"""

from __future__ import annotations

import json
import time
import threading
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

from config import LITERATURE_DIR, OUTPUT_DIR, PAPER_GROUPS
from filename_parser import parse_filename
from pdf_utils import extract_first_page_text
from prototype_mapper import PrototypeMapper
from llm_client import LLMClient
from jinja2 import Environment, FileSystemLoader

_env = Environment(loader=FileSystemLoader(str(Path(__file__).parent.parent / "prompts")))
_coarse_prompt = _env.get_template("coarse_extract.j2")

# Concurrency config - 3 APIs load-balanced, can be more aggressive
MAX_PROTO_WORKERS = 6   # parallel prototypes (requests spread across 3 APIs)
MAX_PAPER_WORKERS = 3   # parallel papers per prototype
MAX_RETRIES = 4         # retry count for rate-limited requests
RETRY_BASE_DELAY = 2.0  # seconds between retries (exponential backoff)

# Track per-provider usage for logging
_provider_stats_lock = threading.Lock()
_provider_stats: dict[str, int] = {}

# Thread-safe progress counter
_progress_lock = threading.Lock()
_progress = {"done": 0, "total": 0, "errors": 0, "retries": 0}


def scan_literature_library(literature_dir: Path = None) -> dict:
    """Walk the literature directory and parse all paper filenames."""
    literature_dir = literature_dir or LITERATURE_DIR
    papers_dir = literature_dir / "论文"
    mapper_result = defaultdict(list)

    if not papers_dir.exists():
        return mapper_result

    for group_dir in sorted(papers_dir.iterdir()):
        if not group_dir.is_dir():
            continue
        group_key = None
        for cn_name, en_name in PAPER_GROUPS.items():
            if cn_name in group_dir.name:
                group_key = en_name
                break
        if group_key is None:
            continue

        for pdf_path in sorted(group_dir.glob("*.pdf")):
            meta = parse_filename(pdf_path.name)
            mapper_result[group_key].append((pdf_path, meta))

    return dict(mapper_result)


def map_papers_to_prototypes(papers_by_group: dict) -> dict:
    """Map all papers to prototypes."""
    mapper = PrototypeMapper()
    prototype_papers = defaultdict(list)

    for group_key, papers in papers_by_group.items():
        for pdf_path, meta in papers:
            mappings = mapper.map_paper(meta, group=group_key)
            for m in mappings:
                prototype_papers[m["prototype_id"]].append({
                    "path": str(pdf_path),
                    "filename": pdf_path.name,
                    "year": meta.year,
                    "author": meta.author,
                    "keywords": meta.keywords,
                    "is_review": meta.is_review,
                    "association": m["association"],
                    "matched_keywords": m["matched_keywords"],
                    "group": group_key,
                })

    return dict(prototype_papers)


def _extract_single_paper(paper: dict, prototype_id: str) -> dict | None:
    """Extract structured fields from a single paper (thread-safe, with retry, load-balanced)."""
    pdf_path = Path(paper["path"])
    first_page = extract_first_page_text(pdf_path)
    if not first_page or len(first_page.strip()) < 50:
        return None

    prompt = _coarse_prompt.render(
        filename_info=f"{paper['year']}-{paper['author']}-{'-'.join(paper['keywords'])}",
        abstract_text=first_page[:3000],
    )

    llm = LLMClient.from_task_type("coarse_scan")
    provider = llm.provider  # which API this call routed to

    for attempt in range(MAX_RETRIES + 1):
        try:
            result = llm.chat_json(prompt)
            result["_source_paper"] = paper["filename"]
            result["_provider"] = provider
            with _progress_lock:
                _progress["done"] += 1
                done, total = _progress["done"], _progress["total"]
            with _provider_stats_lock:
                _provider_stats[provider] = _provider_stats.get(provider, 0) + 1
            if done % 10 == 0 or done == total:
                elapsed = time.time() - _progress.get("start", 0)
                print(f"  [{done}/{total}] {prototype_id} via {provider} ({elapsed:.0f}s)")
            return result
        except Exception as e:
            err_str = str(e)
            if "429" in err_str and attempt < MAX_RETRIES:
                delay = RETRY_BASE_DELAY * (2 ** attempt)
                with _progress_lock:
                    _progress["retries"] += 1
                time.sleep(delay)
                # On 429, switch to a DIFFERENT provider to avoid the rate-limited one
                llm = LLMClient.from_task_type("coarse_scan", exclude_provider=provider)
                provider = llm.provider
                continue
            with _progress_lock:
                _progress["done"] += 1
                _progress["errors"] += 1
            return {"_source_paper": paper["filename"], "_error": err_str[:200]}


def extract_coarse_profile(prototype_id: str, papers: list[dict]) -> dict:
    """Extract a coarse profile for one prototype using concurrent paper processing."""
    priority_papers = sorted(
        papers,
        key=lambda p: (0 if p["association"] == "direct" else 1, 0 if p["is_review"] else 1),
    )[:5]

    profile = {
        "prototype_id": prototype_id,
        "paper_count": len(papers),
        "direct_papers": [p for p in papers if p["association"] == "direct"],
        "indirect_papers": [p for p in papers if p["association"] == "indirect"],
        "extracted_fields": [],
        "coverage": {"pollutants": set(), "mechanisms": set(), "materials": set()},
    }

    # Process papers concurrently within this prototype
    with ThreadPoolExecutor(max_workers=MAX_PAPER_WORKERS) as pool:
        futures = {pool.submit(_extract_single_paper, paper, prototype_id): paper for paper in priority_papers}
        for future in as_completed(futures):
            result = future.result()
            if result is None:
                continue
            profile["extracted_fields"].append(result)
            if "_error" in result:
                continue
            if result.get("target_pollutants"):
                profile["coverage"]["pollutants"].update(result["target_pollutants"])
            if result.get("adsorption_mechanisms"):
                profile["coverage"]["mechanisms"].update(result["adsorption_mechanisms"])
            if result.get("material_type"):
                profile["coverage"]["materials"].add(result["material_type"])

    profile["coverage"] = {k: sorted(v) for k, v in profile["coverage"].items()}
    return profile


def _process_one_prototype(prototype_id: str, papers: list[dict], profiles_dir: Path) -> dict:
    """Process one prototype: extract profile, save JSON, return coverage summary."""
    profile = extract_coarse_profile(prototype_id, papers)

    profile_path = profiles_dir / f"{prototype_id}.json"
    with open(profile_path, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)

    return {
        "prototype_id": prototype_id,
        "total_papers": profile["paper_count"],
        "direct_papers": len(profile["direct_papers"]),
        "indirect_papers": len(profile["indirect_papers"]),
        "pollutants": profile["coverage"]["pollutants"],
        "mechanisms": profile["coverage"]["mechanisms"],
    }


def run_phase1(literature_dir: Path = None, output_dir: Path = None, max_workers: int = None) -> None:
    """Execute Phase 1: Coarse Scan with concurrent execution."""
    output_dir = output_dir or OUTPUT_DIR
    profiles_dir = output_dir / "coarse-profiles"
    profiles_dir.mkdir(parents=True, exist_ok=True)

    workers = max_workers or MAX_PROTO_WORKERS

    print("Phase 1: Scanning literature library...")
    papers_by_group = scan_literature_library(literature_dir)
    total_papers = sum(len(v) for v in papers_by_group.values())
    print(f"  Found {total_papers} papers in {len(papers_by_group)} groups")

    print("Phase 1: Mapping papers to prototypes...")
    prototype_papers = map_papers_to_prototypes(papers_by_group)
    print(f"  Mapped to {len(prototype_papers)} prototypes")

    # Count total LLM calls for progress tracking
    total_calls = sum(min(len(papers), 5) for papers in prototype_papers.values())
    with _progress_lock:
        _progress["done"] = 0
        _progress["total"] = total_calls
        _progress["errors"] = 0
        _progress["start"] = time.time()

    print(f"Phase 1: Extracting coarse profiles ({total_calls} LLM calls, {workers} parallel prototypes, 2 papers each)...")

    coverage_summary = {}
    items = sorted(prototype_papers.items())

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(_process_one_prototype, proto_id, papers, profiles_dir): proto_id
            for proto_id, papers in items
        }
        for future in as_completed(futures):
            proto_id = futures[future]
            try:
                summary = future.result()
                coverage_summary[summary["prototype_id"]] = summary
            except Exception as e:
                print(f"  ERROR processing {proto_id}: {e}")

    elapsed = time.time() - _progress["start"]
    print(f"\nPhase 1: {_progress['done']}/{_progress['total']} calls done, {_progress['errors']} errors, {_progress['retries']} retries, {elapsed:.1f}s total")

    heatmap_path = profiles_dir / "coverage-heatmap.md"
    _write_coverage_heatmap(coverage_summary, heatmap_path)
    print(f"Phase 1 complete. Output written to {profiles_dir}")


def _write_coverage_heatmap(summary: dict, output_path: Path) -> None:
    lines = ["## Coverage Heatmap (Phase 1 Coarse Scan)\n"]
    lines.append("| Prototype | Total Papers | Direct | Pollutants | Mechanisms |")
    lines.append("|-----------|-------------|--------|------------|------------|")

    for proto_id, data in sorted(summary.items()):
        pollutants = ", ".join(data["pollutants"][:5])
        if len(data["pollutants"]) > 5:
            pollutants += f" (+{len(data['pollutants']) - 5})"
        mechanisms = ", ".join(data["mechanisms"][:3])
        if len(data["mechanisms"]) > 3:
            mechanisms += f" (+{len(data['mechanisms']) - 3})"
        lines.append(f"| {proto_id} | {data['total_papers']} | {data['direct_papers']} | {pollutants} | {mechanisms} |")

    output_path.write_text("\n".join(lines), encoding="utf-8")
