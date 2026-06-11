#!/usr/bin/env python3
"""Update feature-mapping.json weights based on aggregated extraction results.

Usage:
    python3 update_feature_mapping.py --input-dir outputs/aggregated --biomimetic-lib /path/to/Biomimetic-design-library
"""

import argparse
import copy
import json
import os
from pathlib import Path


# Pollutant -> category mapping for locating the right section in pollutant_prototype_map
POLLUTANT_CATEGORIES = {
    "Hg2+": "重金属", "Cd2+": "重金属", "Pb2+": "重金属", "Cu2+": "重金属",
    "Zn2+": "重金属", "Ni2+": "重金属", "Cr3+/Cr6+": "重金属", "As3+/As5+": "重金属",
    "Fe3+": "重金属", "Mn2+": "重金属", "Co2+": "重金属",
    "阳离子染料": "有机污染物", "阴离子染料": "有机污染物",
    "芳香族化合物": "有机污染物", "抗生素": "有机污染物",
    "NH4+-N": "无机非金属污染物", "NO3-": "无机非金属污染物",
    "PO43-": "无机非金属污染物", "F-": "无机非金属污染物",
    "原油": "油类", "柴油": "油类", "乳化油": "油类",
    "U": "放射性元素", "Sr": "放射性元素", "Cs": "放射性元素",
}


def compute_evidence_weight(confidence, data_source, match_confidence) -> float:
    """Compute a weight value (0.1-1.0) based on evidence quality."""
    score = 0.1
    conf_map = {"high": 0.4, "medium": 0.2, "low": 0.1}
    source_map = {"experimental": 0.3, "reported": 0.15, "estimated": 0.05}
    match_map = {"high": 0.3, "medium": 0.15, "low": 0.05}

    score += conf_map.get(confidence, 0)
    score += source_map.get(data_source, 0)
    score += match_map.get(match_confidence, 0)
    return min(score, 1.0)


def find_pollutant_category(pollutant: str, fm: dict) -> str:
    """Find which category a pollutant belongs to in the feature-mapping."""
    if pollutant in POLLUTANT_CATEGORIES:
        return POLLUTANT_CATEGORIES[pollutant]
    ppm = fm.get("pollutant_prototype_map", {})
    for category, subcats in ppm.items():
        if isinstance(subcats, dict):
            for key in subcats:
                if pollutant in key or key in pollutant:
                    return category
    return None


def update_pollutant_weights(fm: dict, prototype_id: str, performance_data: list, mechanism_name: str = "") -> dict:
    """Update pollutant_prototype_map with new evidence."""
    fm = copy.deepcopy(fm)
    ppm = fm.get("pollutant_prototype_map", {})

    for perf in performance_data:
        pollutant = perf.get("pollutant", "")
        if not pollutant:
            continue

        weight = compute_evidence_weight(
            perf.get("confidence"), perf.get("data_source"), "medium"
        )

        category = find_pollutant_category(pollutant, fm)
        if not category:
            continue

        subcats = ppm.get(category, {})
        target_key = None
        for key in subcats:
            if pollutant in key or key in pollutant:
                target_key = key
                break
        if not target_key:
            continue

        proto_list = subcats[target_key].get("prototypes", [])
        existing = [p for p in proto_list if p.get("id") == prototype_id]

        if existing:
            if existing[0].get("weight", 0) >= weight:
                continue  # don't overwrite higher weight
            existing[0]["weight"] = weight
        else:
            proto_list.append({
                "id": prototype_id,
                "weight": round(weight, 2),
                "mechanism_summary": mechanism_name,
                "design_hint": "",
            })

    return fm


def update_feature_weights(fm: dict, prototype_id: str, features: list, weight: float) -> dict:
    """Update feature_prototype_map with new weights."""
    fm = copy.deepcopy(fm)
    fpm = fm.get("feature_prototype_map", {})

    for feature in features:
        if feature not in fpm:
            continue
        proto_list = fpm[feature].get("prototypes", [])
        existing = [p for p in proto_list if p.get("id") == prototype_id]

        if existing:
            if existing[0].get("weight", 0) >= weight:
                continue
            existing[0]["weight"] = round(weight, 2)
        else:
            proto_list.append({"id": prototype_id, "weight": round(weight, 2)})

    return fm


def update_feature_mapping(fm: dict, aggregated: dict) -> dict:
    """Main update function: process all prototypes and update feature-mapping."""
    fm = copy.deepcopy(fm)

    for proto_id, data in aggregated.items():
        # Update pollutant weights
        perf_data = data.get("performance_data", [])
        mechanisms = data.get("mechanism_analysis", [])
        mechanism_name = mechanisms[0].get("mechanism_name", "") if mechanisms else ""
        fm = update_pollutant_weights(fm, proto_id, perf_data, mechanism_name)

        # Update feature weights
        features = set()
        for chain_item in data.get("biomimetic_design_chains", []):
            chain = chain_item.get("chain", {})
            for fg in chain.get("key_functional_groups", []):
                if fg.get("group"):
                    features.add(fg["group"])
        for mech in mechanisms:
            for fg in mech.get("key_functional_groups", []):
                if fg.get("group"):
                    features.add(fg["group"])

        if features:
            weight = 0.7  # default weight for feature evidence
            fm = update_feature_weights(fm, proto_id, list(features), weight)

    return fm


def main():
    parser = argparse.ArgumentParser(description="Update feature-mapping.json")
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument(
        "--biomimetic-lib",
        type=Path,
        default=Path(os.environ.get(
            "BIOMIMETIC_LIB",
            Path(__file__).resolve().parent.parent.parent,
        )),
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    fm_path = args.biomimetic_lib / "feature-mapping.json"
    with open(fm_path, encoding="utf-8") as f:
        fm = json.load(f)
    print(f"Loaded feature-mapping.json (version {fm.get('version', '?')})")

    aggregated = {}
    for json_file in sorted(args.input_dir.glob("*.json")):
        with open(json_file, encoding="utf-8") as f:
            aggregated[json_file.stem] = json.load(f)
    print(f"Loaded {len(aggregated)} aggregated prototype files")

    updated_fm = update_feature_mapping(fm, aggregated)

    if args.dry_run:
        print("Dry run -- no changes written")
        print(json.dumps(updated_fm, ensure_ascii=False, indent=2)[:1000])
    else:
        backup_path = fm_path.with_suffix(".json.bak")
        with open(backup_path, "w", encoding="utf-8") as f:
            json.dump(fm, f, ensure_ascii=False, indent=2)
        print(f"Backup saved: {backup_path}")

        with open(fm_path, "w", encoding="utf-8") as f:
            json.dump(updated_fm, f, ensure_ascii=False, indent=2)
        print(f"Updated: {fm_path}")


if __name__ == "__main__":
    main()
