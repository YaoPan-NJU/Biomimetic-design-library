#!/usr/bin/env python3
"""Recover design_translation and mechanism causal_chain fields lost in office rewrite.
Stable matching: prototype id (filename) → restore baseline fields directly."""

import json
import subprocess
import os
import sys

BASELINE_COMMIT = "30481e4"
DB_DIR = "prototypes_db"

def get_baseline_file(path):
    """Read file at baseline commit."""
    result = subprocess.run(
        ["git", "show", f"{BASELINE_COMMIT}:{path}"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return None
    return json.loads(result.stdout)

def normalize_name(s):
    """Normalize a mechanism name for matching."""
    if not s:
        return ""
    return s.strip().lower()

def match_mechanism(baseline_mech, current_mechs):
    """Try to match baseline mechanism to current by name similarity."""
    b_name = normalize_name(baseline_mech.get("name", ""))
    b_desc = normalize_name(baseline_mech.get("description", ""))
    b_doi = normalize_name(baseline_mech.get("ref_doi", "")) if baseline_mech.get("ref_doi") else ""

    matches = []
    for cm in current_mechs:
        c_name = normalize_name(cm.get("name", ""))
        c_desc = normalize_name(cm.get("description", ""))
        c_doi = normalize_name(cm.get("ref_doi", "")) if cm.get("ref_doi") else ""

        # Match by DOI + name
        if b_doi and c_doi and b_doi == c_doi and b_name == c_name:
            return cm, "doi+name"

        # Match by name + description fingerprint (first 100 chars)
        # Never match across different non-empty DOIs.
        if b_name == c_name and b_desc[:100] == c_desc[:100]:
            if b_doi and c_doi and b_doi != c_doi:
                continue
            return cm, "name+desc"

    return None, None

def main():
    # Find all prototype JSON files at baseline
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", BASELINE_COMMIT, f"{DB_DIR}/"],
        capture_output=True, text=True
    )
    all_files = [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]
    proto_files = [f for f in all_files
                   if os.path.dirname(f) == DB_DIR and f.endswith(".json")
                   and "enrichment" not in f and "materials_reference" not in f
                   and "separation" not in f and "parked" not in f]

    # Process each file
    stats = {"dt_restored": 0, "cc_restored": 0, "cc_ambiguous": 0, "files_modified": 0}
    ambiguities = []

    for path in sorted(proto_files):
        baseline = get_baseline_file(path)
        if baseline is None:
            continue

        with open(path) as f:
            current = json.load(f)

        changed = False

        # 1. Restore design_translation
        baseline_dt = baseline.get("design_translation", [])
        current_dt = current.get("design_translation", [])

        if baseline_dt and not current_dt:
            current["design_translation"] = baseline_dt
            stats["dt_restored"] += len(baseline_dt)
            changed = True

        # 2. Restore mechanism causal_chain objects
        baseline_mechs = baseline.get("mechanisms", [])
        current_mechs = current.get("mechanisms", [])

        baseline_cc_mechs = [m for m in baseline_mechs if m.get("causal_chain")]

        if baseline_cc_mechs and current_mechs:
            for b_mech in baseline_cc_mechs:
                matched, method = match_mechanism(b_mech, current_mechs)
                if matched:
                    c_doi = normalize_name(matched.get("ref_doi", "")) if matched.get("ref_doi") else ""
                    b_doi = normalize_name(b_mech.get("ref_doi", "")) if b_mech.get("ref_doi") else ""
                    if b_doi and c_doi and b_doi != c_doi:
                        ambiguities.append({
                            "file": path,
                            "mechanism_name": b_mech.get("name", "UNKNOWN"),
                            "reason": "cross_doi_unsafe"
                        })
                        stats["cc_ambiguous"] += 1
                    elif not matched.get("causal_chain"):
                        matched["causal_chain"] = b_mech["causal_chain"]
                        stats["cc_restored"] += 1
                        changed = True
                    else:
                        ambiguities.append({
                            "file": path,
                            "mechanism_name": b_mech.get("name", "UNKNOWN"),
                            "reason": "already_has_causal_chain"
                        })
                        stats["cc_ambiguous"] += 1
                else:
                    ambiguities.append({
                        "file": path,
                        "mechanism_name": b_mech.get("name", "UNKNOWN"),
                        "reason": "no_current_match"
                    })
                    stats["cc_ambiguous"] += 1
        elif baseline_cc_mechs and not current_mechs:
            # Mechanisms were also removed - add them back
            current["mechanisms"] = baseline_mechs
            stats["cc_restored"] += len(baseline_cc_mechs)
            changed = True

        if changed:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(current, f, ensure_ascii=False, indent=2)
                f.write("\n")
            stats["files_modified"] += 1

    # Summary
    print(f"Files modified: {stats['files_modified']}")
    print(f"design_translation entries restored: {stats['dt_restored']}")
    print(f"causal_chain entries restored: {stats['cc_restored']}")
    print(f"causal_chain ambiguous/unmatched: {stats['cc_ambiguous']}")

    if ambiguities:
        print("\nAmbiguities:")
        for a in ambiguities:
            print(f"  {a['file']}: {a['mechanism_name']} - {a['reason']}")

    return stats

if __name__ == "__main__":
    main()
