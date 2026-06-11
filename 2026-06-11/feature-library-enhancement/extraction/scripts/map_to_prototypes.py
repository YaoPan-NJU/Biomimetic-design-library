#!/usr/bin/env python3
"""Map extraction results to biomimetic prototypes and aggregate by prototype.

Usage:
    python3 map_to_prototypes.py --input-dir outputs/extractions --output-dir outputs/aggregated
"""

import argparse
import json
import re
import sys
from pathlib import Path
from collections import defaultdict


def load_vocabulary(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_prototype_routing(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def normalize_feature(raw: str, vocab: dict) -> str:
    """Map a raw feature string to standard label via vocabulary_mapping."""
    fm = vocab.get("feature_mapping", {})
    lower = raw.lower().strip()
    if lower in fm:
        return fm[lower]
    for key, val in fm.items():
        if key.lower() in lower or lower in key.lower():
            return val
    return raw


def normalize_mechanism(raw: str, vocab: dict) -> str:
    mm = vocab.get("mechanism_mapping", {})
    lower = raw.lower().strip()
    if lower in mm:
        return mm[lower]
    for key, val in mm.items():
        if key.lower() in lower or lower in key.lower():
            return val
    return raw


def normalize_pollutant(raw: str, vocab: dict) -> str:
    pm = vocab.get("pollutant_mapping", {})
    lower = raw.lower().strip()
    if lower in pm:
        return pm[lower]
    for key, val in pm.items():
        if key.lower() in lower or lower in key.lower():
            return val
    return raw


def match_prototypes(text: str, routing: dict) -> list:
    """Match free text against prototype keywords. Return top matches."""
    rules = routing.get("routing_rules", {})
    threshold = rules.get("match_threshold", 2)
    max_proto = rules.get("max_prototypes_per_paper", 3)
    case_insensitive = rules.get("case_insensitive", True)

    if case_insensitive:
        text_lower = text.lower()
    else:
        text_lower = text

    scores = []
    for proto_id, proto_cfg in routing.get("prototypes", {}).items():
        count = 0
        keywords = proto_cfg.get("keywords_en", []) + proto_cfg.get("keywords_cn", [])
        for kw in keywords:
            kw_check = kw.lower() if case_insensitive else kw
            if kw_check in text_lower:
                count += 1
        if count >= threshold:
            confidence = "high" if count >= threshold * 2 else "medium"
            scores.append({
                "prototype_id": proto_id,
                "match_confidence": confidence,
                "keyword_hits": count,
            })

    scores.sort(key=lambda x: x["keyword_hits"], reverse=True)
    return scores[:max_proto]


def normalize_extraction(result: dict, vocab: dict) -> dict:
    """Normalize vocabulary terms in an extraction result (in-place)."""
    for perf in result.get("performance_data", []):
        if perf.get("pollutant"):
            perf["pollutant"] = normalize_pollutant(perf["pollutant"], vocab)

    for mech in result.get("mechanism_analysis", []):
        if mech.get("mechanism_name"):
            mech["mechanism_name"] = normalize_mechanism(mech["mechanism_name"], vocab)

    chain = result.get("biomimetic_design_chain", {})
    for fg in chain.get("key_functional_groups", []):
        if fg.get("group"):
            fg["group"] = normalize_feature(fg["group"], vocab)

    return result


def aggregate_by_prototype(results: list, vocab: dict = None) -> dict:
    """Group extraction results by prototype_id.

    Each result may have prototype_associations; we group by those.
    Returns {prototype_id: {performance_data: [], mechanism_analysis: [], ...}}
    """
    aggregated = defaultdict(lambda: {
        "performance_data": [],
        "mechanism_analysis": [],
        "biomimetic_design_chains": [],
        "structural_features": [],
        "engineering_constraints": [],
        "papers": [],
    })

    for result in results:
        if vocab:
            normalize_extraction(result, vocab)

        paper_id = result.get("paper_id", "unknown")
        associations = result.get("prototype_associations", [])

        for assoc in associations:
            pid = assoc.get("prototype_id")
            if not pid:
                continue

            bucket = aggregated[pid]
            bucket["papers"].append({
                "paper_id": paper_id,
                "confidence": assoc.get("match_confidence", "low"),
            })

            bucket["performance_data"].extend(
                result.get("performance_data", [])
            )
            bucket["mechanism_analysis"].extend(
                result.get("mechanism_analysis", [])
            )

            chain = result.get("biomimetic_design_chain")
            if chain:
                bucket["biomimetic_design_chains"].append({
                    "paper_id": paper_id,
                    "chain": chain,
                })

            sf = result.get("structural_features")
            if sf:
                bucket["structural_features"].append({
                    "paper_id": paper_id,
                    "features": sf,
                })

            bucket["engineering_constraints"].extend(
                result.get("engineering_constraints", [])
            )

    return dict(aggregated)


def load_extraction_results(input_dir: Path) -> list:
    """Load all JSON extraction results from a directory."""
    results = []
    if not input_dir.exists():
        return results
    for json_file in sorted(input_dir.rglob("*.json")):
        try:
            with open(json_file, encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict) and data.get("schema_version") == "biomimetic-v1":
                results.append(data)
        except (json.JSONDecodeError, KeyError):
            continue
    return results


def main():
    parser = argparse.ArgumentParser(description="Map extraction results to prototypes")
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument(
        "--vocab",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "config" / "vocabulary_mapping.json",
    )
    parser.add_argument(
        "--routing",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "config" / "prototype_routing.json",
    )
    args = parser.parse_args()

    vocab = load_vocabulary(args.vocab)
    routing = load_prototype_routing(args.routing)
    results = load_extraction_results(args.input_dir)
    print(f"Loaded {len(results)} extraction results from {args.input_dir}")

    # For results without prototype_associations, try keyword matching
    for result in results:
        if not result.get("prototype_associations"):
            text = " ".join([
                result.get("bibliographic_metadata", {}).get("title", ""),
                result.get("bibliographic_metadata", {}).get("abstract", ""),
                " ".join(result.get("bibliographic_metadata", {}).get("keywords", [])),
            ])
            matches = match_prototypes(text, routing)
            result["prototype_associations"] = [
                {"prototype_id": m["prototype_id"], "match_confidence": m["match_confidence"]}
                for m in matches
            ]

    aggregated = aggregate_by_prototype(results, vocab=vocab)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for proto_id, data in aggregated.items():
        out_path = args.output_dir / f"{proto_id}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        n_papers = len(data["papers"])
        n_perf = len(data["performance_data"])
        print(f"  {proto_id}: {n_papers} papers, {n_perf} performance records")

    print(f"\nAggregated {len(aggregated)} prototypes -> {args.output_dir}")


if __name__ == "__main__":
    main()
