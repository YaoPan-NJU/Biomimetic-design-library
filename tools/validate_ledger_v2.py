#!/usr/bin/env python3
"""
Ledger v2 validator: validates canon-recovery-ledger.jsonl against the v2 schema
and reports statistics without modifying any files.

Usage:
    python3 -X utf8 tools/validate_ledger_v2.py
"""
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LEDGER_PATH = os.path.join(ROOT, "docs", "registries", "canon-recovery-ledger.jsonl")
SCHEMA_PATH = os.path.join(ROOT, "docs", "registries", "canon-recovery-ledger-v2.schema.json")

VALID_DISPOSITIONS = {
    "restored", "ambiguous", "refuted", "corrected", "downgraded",
    "removed", "unchanged", "scope_caveat"
}
VALID_BASIS = {"direct_quote", "extraction", "ambiguity_gate", "correction", "scope_review", "none"}
VALID_LEVELS = {"perf_1", "perf_2", "perf_3", "mech_1", "mech_2", "mech_3", "unknown"}


def validate():
    if not os.path.exists(LEDGER_PATH):
        print(f"ERROR: Ledger not found: {LEDGER_PATH}")
        return 1

    stats = {
        "total": 0,
        "valid": 0,
        "errors": [],
        "warnings": [],
        "disposition_counts": Counter(),
        "basis_counts": Counter(),
        "level_counts": Counter(),
        "pending_count": 0,
        "missing_commit": 0,
        "duplicate_ids": [],
        "missing_required": [],
        "bad_disposition": [],
        "bad_basis": [],
        "bad_level": [],
        "empty_identity": [],
        "weak_identity": [],
        "array_index_only": [],
        "orphan_entries": [],
    }

    seen_ids = Counter()
    entries_by_prototype = {}

    with open(LEDGER_PATH, encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            stats["total"] += 1

            try:
                entry = json.loads(line)
            except json.JSONDecodeError as e:
                stats["errors"].append(f"line {lineno}: JSON parse error: {e}")
                continue

            # Check required fields
            required = {"id", "prototype_id", "field_path", "record_identity", "disposition", "basis", "applied_commit"}
            missing = required - set(entry.keys())
            if missing:
                stats["missing_required"].append(f"line {lineno}: missing {missing}")
                continue

            eid = entry["id"]
            seen_ids[eid] += 1
            pid = entry["prototype_id"]
            entries_by_prototype.setdefault(pid, []).append(entry)

            # Check applied_commit
            if entry["applied_commit"] == "PENDING":
                stats["pending_count"] += 1

            # Check disposition
            disp = entry.get("disposition", "")
            stats["disposition_counts"][disp] += 1
            if disp not in VALID_DISPOSITIONS:
                stats["bad_disposition"].append(f"line {lineno}: invalid disposition '{disp}'")

            # Check basis
            basis = entry.get("basis", "")
            stats["basis_counts"][basis] += 1
            if basis not in VALID_BASIS:
                stats["bad_basis"].append(f"line {lineno}: invalid basis '{basis}'")

            # Check record_identity
            ident = entry.get("record_identity", {})
            if not ident or not isinstance(ident, dict):
                stats["empty_identity"].append(f"line {lineno}: missing or non-dict record_identity")
            else:
                level = ident.get("level", "")
                stats["level_counts"][level] += 1
                if level not in VALID_LEVELS:
                    stats["bad_level"].append(f"line {lineno}: invalid level '{level}'")
                key = ident.get("key", "")
                if not key:
                    stats["weak_identity"].append(f"line {lineno}: empty identity key")

            # Check field_path for array-index-only identity
            fp = entry.get("field_path", "")
            if fp and fp.startswith("[") and "." not in fp:
                stats["array_index_only"].append(f"line {lineno}: field_path is array index only '{fp}'")

    # Report duplicate IDs
    for eid, count in seen_ids.items():
        if count > 1:
            stats["duplicate_ids"].append(f"'{eid}' appears {count} times")

    # Report orphan entries (prototype_id doesn't exist in DB)
    db_dir = os.path.join(ROOT, "prototypes_db")
    valid_pids = set()
    if os.path.isdir(db_dir):
        for f in os.listdir(db_dir):
            if f.endswith(".json"):
                valid_pids.add(f[:-5])
    for pid in entries_by_prototype:
        if pid not in valid_pids:
            stats["orphan_entries"].append(f"prototype '{pid}' not in prototypes_db/")

    # Summary
    stats["valid"] = stats["total"] - len(stats["errors"]) - len(stats["missing_required"])

    print("=" * 60)
    print("LEDGER v2 VALIDATION REPORT")
    print("=" * 60)
    print(f"Total entries:     {stats['total']}")
    print(f"Valid entries:     {stats['valid']}")
    print(f"PENDING entries:   {stats['pending_count']}")
    print(f"Errors:            {len(stats['errors'])}")
    print(f"Warnings:          {len(stats['bad_disposition']) + len(stats['bad_basis']) + len(stats['bad_level'])}")
    print()
    print("--- Disposition distribution ---")
    for d, c in stats["disposition_counts"].most_common():
        print(f"  {d}: {c}")
    print()
    print("--- Basis distribution ---")
    for b, c in stats["basis_counts"].most_common():
        print(f"  {b}: {c}")
    print()
    print("--- Identity level distribution ---")
    for l, c in stats["level_counts"].most_common():
        print(f"  {l}: {c}")
    print()
    if stats["duplicate_ids"]:
        print(f"--- Duplicate IDs ({len(stats['duplicate_ids'])}) ---")
        for d in stats["duplicate_ids"][:10]:
            print(f"  {d}")
        print()
    if stats["missing_required"]:
        print(f"--- Missing required fields ({len(stats['missing_required'])}) ---")
        for m in stats["missing_required"][:10]:
            print(f"  {m}")
        print()
    if stats["bad_disposition"]:
        print(f"--- Invalid dispositions ({len(stats['bad_disposition'])}) ---")
        for b in stats["bad_disposition"][:10]:
            print(f"  {b}")
        print()
    if stats["bad_basis"]:
        print(f"--- Invalid bases ({len(stats['bad_basis'])}) ---")
        for b in stats["bad_basis"][:10]:
            print(f"  {b}")
        print()
    if stats["bad_level"]:
        print(f"--- Invalid identity levels ({len(stats['bad_level'])}) ---")
        for b in stats["bad_level"][:10]:
            print(f"  {b}")
        print()
    if stats["weak_identity"]:
        print(f"--- Weak identity (empty key) ({len(stats['weak_identity'])}) ---")
        print()
    if stats["orphan_entries"]:
        print(f"--- Orphan entries ({len(stats['orphan_entries'])}) ---")
        for o in stats["orphan_entries"][:10]:
            print(f"  {o}")
        print()

    total_issues = (len(stats["errors"]) + len(stats["missing_required"]) +
                    len(stats["bad_disposition"]) + len(stats["bad_basis"]) +
                    len(stats["bad_level"]))
    if total_issues == 0 and stats["pending_count"] == 0:
        print("✅ Ledger v2 validation PASSED")
    else:
        print(f"⚠️  Ledger v2 validation: {total_issues} issues, {stats['pending_count']} PENDING entries")
        print("   (PENDING entries are expected for unapplied v1 migration input)")

    return 0 if total_issues == 0 else 1


if __name__ == "__main__":
    sys.exit(validate())
