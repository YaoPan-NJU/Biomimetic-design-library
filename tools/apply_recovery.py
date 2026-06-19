#!/usr/bin/env python3
"""
M2 deterministic canon-recovery applier.

R1-B corrected: Restores evidence fields present in git history but empty at HEAD,
matched by stable identity (design §6.2). PURELY ADDITIVE: only fills empty fields,
so no protected metric can decrease. Writes one ledger entry per restored field-group.
Refuses refuted-row resurrection. causal_chain restoration requires strong identity
(name + source), not a fingerprint-only match.

R1-B ambiguity gate: when multiple history entries provide DIFFERENT values for the
same field, the result is ambiguous — that field is rejected (not silently resolved
by "first strongest wins"). Ledger entries with disposition "ambiguous" are written
for each rejected field.

Run the count-guard (--guard) after this; it must show no decreases (only increases).

Usage:
    python3 -X utf8 tools/apply_recovery.py --dry-run    # plan only, no canon write
    python3 -X utf8 tools/apply_recovery.py               # apply + ledger
"""
import json
import os
import sys
import argparse
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from recovery_engine import SOURCE_COMMITS, git_json, load_head, _nonempty, _row_label

ROOT = os.path.dirname(HERE)
DB = os.path.join(ROOT, "prototypes_db")
LEDGER = os.path.join(ROOT, "docs", "registries", "canon-recovery-ledger.jsonl")
REFUTED = os.path.join(ROOT, "docs", "registries", "refuted-log.md")

PERF_FIELDS = ["verification_quote", "source_locator", "locator", "pollutant", "page", "conditions", "ph", "temperature"]
MECH_FIELDS = ["verification_quote", "source_file", "ref_doi", "page", "locator"]


def _refuted_tokens():
    toks = set()
    if os.path.exists(REFUTED):
        for line in open(REFUTED, encoding="utf-8"):
            if "wrong_source" in line:
                for t in line.split("|"):
                    t = t.strip()
                    if t:
                        toks.add(t)
    return toks


def _identity_strength(head_row, hist_row, kind):
    """Return identity level: 1 (strongest) .. 3 (fingerprint), or 0 (no match)."""
    from canon_recovery_lib import perf_fingerprint, mech_fingerprint
    if kind == "perf":
        h, _ = perf_fingerprint(head_row); g, _ = perf_fingerprint(hist_row)
        if h["source_id"] and h["source_id"] == g["source_id"] and h["parameter"] == g["parameter"] and h["value"] == g["value"] and h["material"] == g["material"]:
            return 1
        if h["source_basename"] and h["source_basename"] == g["source_basename"] and h["parameter"] == g["parameter"] and h["value"] == g["value"] and h["material"] == g["material"]:
            return 2
        if h["parameter"] == g["parameter"] and h["value"] == g["value"] and h["material"] == g["material"]:
            return 3
        return 0
    else:
        h, _ = mech_fingerprint(head_row); g, _ = mech_fingerprint(hist_row)
        if h["source_id"] and h["source_id"] == g["source_id"] and h["name"] == g["name"]:
            return 1
        if h["source_basename"] and h["source_basename"] == g["source_basename"] and h["name"] == g["name"]:
            return 2
        if h["name"] == g["name"] and h["desc"] == g["desc"] and h["desc"]:
            return 3
        return 0


def gather_history(pid):
    path = f"prototypes_db/{pid}.json"
    hp, hm, ht = [], [], {}
    for c in SOURCE_COMMITS:
        d = git_json(c, path)
        if not d:
            continue
        for p in (d.get("performance_data") or []):
            if isinstance(p, dict):
                p["_commit"] = c; hp.append(p)
        ms = d.get("mechanisms") or []
        if isinstance(ms, dict):
            ms = list(ms.values())
        for m in ms:
            if isinstance(m, dict):
                m["_commit"] = c; hm.append(m)
        dt = d.get("design_translation")
        if isinstance(dt, list) and dt and "design_translation" not in ht:
            ht["design_translation"] = (dt, c)
    return hp, hm, ht


def apply_perf(pid, head_row, hist_perf, refuted):
    """Fill empty perf evidence fields from history matches.

    R1-B: when multiple history entries provide DIFFERENT values for the same field,
    the result is ambiguous — reject that field (do not silently pick strongest).
    Only fill when exactly one non-refuted history entry provides a value.

    Returns (changes, ambiguous_fields).
    """
    changes = []
    ambiguous = []
    candidates = {}  # field -> list of (value, commit, level)
    for hr in hist_perf:
        lvl = _identity_strength(head_row, hr, "perf")
        if lvl == 0:
            continue
        for f in PERF_FIELDS:
            if not _nonempty(head_row, f) and _nonempty(hr, f):
                val = hr[f]
                if str(val) in refuted:
                    continue
                candidates.setdefault(f, []).append((val, hr["_commit"], lvl))
    for f, entries in sorted(candidates.items()):
        unique_vals = set(e[0] for e in entries)
        if len(unique_vals) > 1:
            ambiguous.append(f)
            continue
        # All entries agree on value; use the strongest identity
        best = min(entries, key=lambda e: e[2])
        head_row[f] = best[0]
        changes.append({"field": f, "value": best[0], "commit": best[1], "level": best[2]})
    return changes, ambiguous


def apply_mech(pid, head_mech, hist_mech, refuted):
    """Fill empty mechanism fields from history matches.

    R1-B: when multiple history entries provide DIFFERENT values for the same field,
    the result is ambiguous — reject that field. causal_chain also requires unambiguous
    single-source match at L1/L2 identity.

    Returns (changes, ambiguous_fields).
    """
    changes = []
    ambiguous = []
    candidates = {}  # field -> list of (value, commit, level)
    causal_candidates = []
    for hm in hist_mech:
        lvl = _identity_strength(head_mech, hm, "mech")
        if lvl == 0:
            continue
        for f in MECH_FIELDS:
            if not _nonempty(head_mech, f) and _nonempty(hm, f):
                val = hm[f]
                if str(val) in refuted:
                    continue
                candidates.setdefault(f, []).append((val, hm["_commit"], lvl))
        if lvl in (1, 2) and not _nonempty(head_mech, "causal_chain") and _nonempty(hm, "causal_chain"):
            causal_candidates.append((hm["causal_chain"], hm["_commit"], lvl))
    for f, entries in sorted(candidates.items()):
        unique_vals = set(e[0] for e in entries)
        if len(unique_vals) > 1:
            ambiguous.append(f)
            continue
        best = min(entries, key=lambda e: e[2])
        head_mech[f] = best[0]
        changes.append({"field": f, "value": best[0], "commit": best[1], "level": best[2]})
    # causal_chain: require single unambiguous source
    if causal_candidates:
        unique_causal = set(id(e[0]) for e in causal_candidates)
        if len(unique_causal) == 1:
            best_c = min(causal_candidates, key=lambda e: e[2])
            head_mech["causal_chain"] = best_c[0]
            changes.append({"field": "causal_chain", "value": "<object>", "commit": best_c[1], "level": best_c[2]})
        else:
            ambiguous.append("causal_chain")
    return changes, ambiguous


def ledger_entry(pid, field_path, rec_id_key, disposition, commit, basis, modality="text"):
    return {
        "id": f"R-{pid}-{abs(hash((pid,field_path,rec_id_key)))%100000}",
        "prototype_id": pid,
        "field_path": field_path,
        "record_identity": {"level": "perf_1", "key": rec_id_key},
        "disposition": disposition,
        "from_source_commit": commit,
        "evidence_precedence": "direct_quote" if "quote" in field_path else "extraction",
        "basis": basis,
        "quote": None,
        "locator": None,
        "local_file": None,
        "modality": modality,
        "notes": "M2 git-history field recovery (additive)",
        "applied_commit": "PENDING",
        "applied_at": "2026-06-19",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("prototype", nargs="?", default=None)
    args = ap.parse_args()

    import glob
    pids = [args.prototype] if args.prototype else sorted(os.path.basename(p)[:-5] for p in glob.glob(os.path.join(DB, "*.json")))
    refuted = _refuted_tokens()

    total_perf = total_mech = total_cc = total_dt = 0
    ledger_lines = []

    for pid in pids:
        head = load_head(pid)
        if head is None:
            continue
        hp, hm, ht = gather_history(pid)
        if not (hp or hm or ht):
            continue
        proto_changes = {"perf": 0, "mech": 0, "causal": 0, "dt": 0}

        perf = head.get("performance_data", []) or []
        for i, row in enumerate(perf):
            if not isinstance(row, dict):
                continue
            ch, amb = apply_perf(pid, row, hp, refuted)
            if amb:
                for f in amb:
                    ledger_lines.append(ledger_entry(pid, f"performance_data[{i}].{f}",
                                                     _row_label(row), "ambiguous", "none",
                                                     "ambiguity_gate"))
            if ch:
                proto_changes["perf"] += len(ch)
                for c in ch:
                    ledger_lines.append(ledger_entry(pid, f"performance_data[{i}].{c['field']}",
                                                     _row_label(row), "restored", c["commit"],
                                                     "extraction" if c["field"] not in ("verification_quote",) else "direct_quote"))

        mechs = head.get("mechanisms", []) or []
        if isinstance(mechs, dict):
            mechs = list(mechs.values())
        for i, m in enumerate(mechs):
            if not isinstance(m, dict):
                continue
            ch, amb = apply_mech(pid, m, hm, refuted)
            if amb:
                for f in amb:
                    ledger_lines.append(ledger_entry(pid, f"mechanisms[{i}].{f}",
                                                     _row_label(m), "ambiguous", "none",
                                                     "ambiguity_gate"))
            if ch:
                proto_changes["mech"] += len(ch)
                if any(c["field"] == "causal_chain" for c in ch):
                    proto_changes["causal"] += 1
                for c in ch:
                    ledger_lines.append(ledger_entry(pid, f"mechanisms[{i}].{c['field']}",
                                                     _row_label(m), "restored", c["commit"],
                                                     "direct_quote" if "quote" in c["field"] else "extraction"))

        # design_translation top-level
        if not _nonempty(head, "design_translation") and "design_translation" in ht:
            dt, commit = ht["design_translation"]
            head["design_translation"] = dt
            proto_changes["dt"] += len(dt)
            ledger_lines.append(ledger_entry(pid, "design_translation", pid, "restored", commit, "review"))

        if any(proto_changes.values()):
            total_perf += proto_changes["perf"]; total_mech += proto_changes["mech"]
            total_cc += proto_changes["causal"]; total_dt += proto_changes["dt"]
            if not args.dry_run:
                with open(os.path.join(DB, f"{pid}.json"), "w", encoding="utf-8") as f:
                    json.dump(head, f, ensure_ascii=False, indent=2)
                    f.write("\n")

    print(json.dumps({
        "prototypes": len(pids),
        "perf_fields_restored": total_perf,
        "mech_fields_restored": total_mech,
        "causal_chains_restored": total_cc,
        "design_translation_entries_restored": total_dt,
        "ledger_entries": len(ledger_lines),
        "dry_run": bool(args.dry_run),
    }, ensure_ascii=False, indent=2))

    if ledger_lines and not args.dry_run:
        os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
        with open(LEDGER, "a", encoding="utf-8") as f:
            for e in ledger_lines:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
