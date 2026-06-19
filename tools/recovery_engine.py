#!/usr/bin/env python3
"""
M2 canon-recovery engine: enumerate fields present in git history but missing at HEAD,
matched by stable identity (design §6.2). Produces a per-prototype recovery plan.

It does NOT write canon. It computes candidate restores; canon_recovery_lib writes the
ledger and a separate applier edits the JSON. This keeps recovery auditable: every
restore is matched, never index-based, never resurrects refuted data.

Usage:
    python3 -X utf8 tools/recovery_engine.py                # enumerate all root prototypes
    python3 -X utf8 tools/recovery_engine.py chitosan         # one prototype
"""
import json
import os
import sys
import subprocess
import argparse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from canon_recovery_lib import match_perf, match_mech, perf_fingerprint, mech_fingerprint, _source_id, _basename, _norm, _norm_value

ROOT = os.path.dirname(HERE)
DB = os.path.join(ROOT, "prototypes_db")

# Historical input commits to compare (design §6.1) — richest evidence sources.
SOURCE_COMMITS = ["39aee26", "2242cc9", "cfdc0c1", "dbef652", "97f14f3", "82fa2c0^", "3797c4b", "21bfa76", "2b070a1"]

PERF_RECOVERABLE = ["verification_quote", "source_locator", "locator", "pollutant", "page", "conditions", "ph", "temperature"]
MECH_RECOVERABLE = ["verification_quote", "causal_chain", "source_file", "ref_doi", "page", "locator"]
TOP_RECOVERABLE = ["design_translation"]


def git_json(commit, path):
    r = subprocess.run(["git", "show", f"{commit}:{path}"], capture_output=True)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except Exception:
        return None


def load_head(pid):
    p = os.path.join(DB, f"{pid}.json")
    if not os.path.exists(p):
        return None
    return json.load(open(p, encoding="utf-8"))


def _truthy(v):
    return bool(v) and str(v).strip() != ""


def _nonempty(d, key):
    v = d.get(key) if isinstance(d, dict) else None
    return _truthy(v)


def recover_perf(head_row, hist_rows):
    """For one HEAD perf row, find stable-identity matches in history and list fields
    recoverable (truthy in history, empty in HEAD). Returns list of (field, hist_value, commit, level)."""
    out = []
    # match against the union of all history rows (stable identity)
    for hr in hist_rows:
        # build a pseudo-canon with just this hist row to test match
        hits = match_perf(hr.get("_proto", ""), hr, {"performance_data": [head_row]})
        if not hits:
            continue
        for field in PERF_RECOVERABLE:
            if not _nonempty(head_row, field) and _nonempty(hr, field):
                out.append({
                    "field": field,
                    "value": hr[field],
                    "source_commit": hr.get("_commit"),
                    "identity": "perf",
                })
    # dedup by (field, value)
    seen = set(); uniq = []
    for o in out:
        k = (o["field"], str(o["value"])[:60])
        if k not in seen:
            seen.add(k); uniq.append(o)
    return uniq


def recover_mech(head_mech, hist_mechs):
    out = []
    for hm in hist_mechs:
        hits = match_mech(hm.get("_proto", ""), hm, {"mechanisms": [head_mech]})
        if not hits:
            continue
        for field in MECH_RECOVERABLE:
            hv = hm.get(field)
            if field == "causal_chain":
                if (not _truthy(head_mech.get("causal_chain"))) and _truthy(hm.get("causal_chain")):
                    out.append({"field": "causal_chain", "value": "<object>", "source_commit": hm.get("_commit"), "identity": "mech"})
            else:
                if not _nonempty(head_mech, field) and _nonempty(hm, field):
                    out.append({"field": field, "value": hv, "source_commit": hm.get("_commit"), "identity": "mech"})
    seen = set(); uniq = []
    for o in out:
        k = (o["field"], str(o["value"])[:60])
        if k not in seen:
            seen.add(k); uniq.append(o)
    return uniq


def enumerate_prototype(pid, verbose=False):
    head = load_head(pid)
    if head is None:
        return None
    head_perf = head.get("performance_data", []) or []
    head_mech = head.get("mechanisms", []) or []
    if isinstance(head_mech, dict):
        head_mech = list(head_mech.values())

    # gather all history rows for this prototype across source commits
    hist_perf = []
    hist_mech = []
    hist_top = {}
    path = f"prototypes_db/{pid}.json"
    for c in SOURCE_COMMITS:
        d = git_json(c, path)
        if not d:
            continue
        for p in (d.get("performance_data") or []):
            if isinstance(p, dict):
                p["_commit"] = c; p["_proto"] = pid
                hist_perf.append(p)
        ms = d.get("mechanisms") or []
        if isinstance(ms, dict):
            ms = list(ms.values())
        for m in ms:
            if isinstance(m, dict):
                m["_commit"] = c; m["_proto"] = pid
                hist_mech.append(m)
        dt = d.get("design_translation")
        if isinstance(dt, list) and dt and "design_translation" not in hist_top:
            hist_top["design_translation"] = (dt, c)

    plan = {
        "prototype_id": pid,
        "head_perf_rows": len(head_perf),
        "head_mech_rows": len(head_mech),
        "hist_commits_with_file": sorted({p["_commit"] for p in hist_perf} | {m["_commit"] for m in hist_mech}),
        "perf_recoverable": [],
        "mech_recoverable": [],
        "design_translation_recoverable": None,
        "unmatched_hist_perf": 0,
    }

    # perf: for each HEAD row, find recoverable fields
    n_perf_recovered = 0
    for i, hp in enumerate(head_perf):
        recs = recover_perf(hp, hist_perf)
        if recs:
            plan["perf_recoverable"].append({"index": i, "row": _row_label(hp), "recovers": recs})
            n_perf_recovered += len(recs)
    plan["n_perf_fields_recoverable"] = n_perf_recovered

    # mech
    n_mech_recovered = 0
    for i, hm in enumerate(head_mech):
        recs = recover_mech(hm, hist_mech)
        if recs:
            plan["mech_recoverable"].append({"index": i, "row": _row_label(hm), "recovers": recs})
            n_mech_recovered += len(recs)
    plan["n_mech_fields_recoverable"] = n_mech_recovered

    # design_translation (top-level)
    if not _truthy(head.get("design_translation")) and "design_translation" in hist_top:
        dt, c = hist_top["design_translation"]
        plan["design_translation_recoverable"] = {"entries": len(dt), "source_commit": c}

    return plan


def _row_label(r):
    return f"{r.get('parameter','')[:30]}|{str(r.get('value',''))[:20]}|{r.get('material','')[:20]}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prototype", nargs="?", default=None)
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    pids = []
    if args.prototype:
        pids = [args.prototype]
    else:
        pids = sorted(os.path.basename(p)[:-5] for p in __import__("glob").glob(os.path.join(DB, "*.json")))

    summary = []
    for pid in pids:
        plan = enumerate_prototype(pid)
        if plan is None:
            continue
        summary.append(plan)

    total_perf = sum(p["n_perf_fields_recoverable"] for p in summary)
    total_mech = sum(p["n_mech_fields_recoverable"] for p in summary)
    dt_n = sum(1 for p in summary if p["design_translation_recoverable"])

    print(json.dumps({
        "prototypes_scanned": len(summary),
        "perf_fields_recoverable": total_perf,
        "mech_fields_recoverable": total_mech,
        "prototypes_with_translation_recoverable": dt_n,
        "per_prototype": [
            {
                "id": p["prototype_id"],
                "hist_commits": p["hist_commits_with_file"],
                "perf_recover": p["n_perf_fields_recoverable"],
                "mech_recover": p["n_mech_fields_recoverable"],
                "translation_recover": 1 if p["design_translation_recoverable"] else 0,
            } for p in summary
        ],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
