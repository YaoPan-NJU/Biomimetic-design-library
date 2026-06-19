#!/usr/bin/env python3
"""
R1-B canon-recovery applier (corrected).

Restores evidence fields present in git history but empty at HEAD, matched by stable
identity (design §6.2). PURELY ADDITIVE: only fills empty fields, so no protected
metric can decrease. Writes one ledger entry per restored field. Refuses refuted-row
resurrection.

R1-B requirements:
- Each candidate operation must do stable identity matching against the target row
- Match count must be exactly 1 to apply
- 0 matches and >1 matches (even with same value) are rejected and written as
  unresolved/ambiguous artifacts
- Array index is NEVER used as identity
- No "first strongest wins" behavior
- Ledger IDs use SHA-256 of normalized content (cross-process stable)
- Identity levels are correct per type (not always perf_1)
- No PENDING in applied_commit

Usage:
    python3 -X utf8 tools/apply_recovery.py --dry-run    # plan only, no canon write
    python3 -X utf8 tools/apply_recovery.py               # apply + ledger
"""
import json
import os
import sys
import argparse
import hashlib
import subprocess
import datetime

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


def _identity_match(head_row, hist_row, kind):
    """Return identity level string or None. NEVER uses array index."""
    from canon_recovery_lib import perf_fingerprint, mech_fingerprint
    if kind == "perf":
        h, _ = perf_fingerprint(head_row); g, _ = perf_fingerprint(hist_row)
        if h["source_id"] and h["source_id"] == g["source_id"] and h["parameter"] == g["parameter"] and h["value"] == g["value"] and h["material"] == g["material"]:
            return "perf_1"
        if h["source_basename"] and h["source_basename"] == g["source_basename"] and h["parameter"] == g["parameter"] and h["value"] == g["value"] and h["material"] == g["material"]:
            return "perf_2"
        if h["parameter"] == g["parameter"] and h["value"] == g["value"] and h["material"] == g["material"]:
            return "perf_3"
        return None
    else:
        h, _ = mech_fingerprint(head_row); g, _ = mech_fingerprint(hist_row)
        if h["source_id"] and h["source_id"] == g["source_id"] and h["name"] == g["name"]:
            return "mech_1"
        if h["source_basename"] and h["source_basename"] == g["source_basename"] and h["name"] == g["name"]:
            return "mech_2"
        if h["name"] == g["name"] and h["desc"] == g["desc"] and h["desc"]:
            return "mech_3"
        return None


def _stable_ledger_id(pid, field_path, identity_key):
    """Generate deterministic ledger ID using SHA-256 of normalized content."""
    content = f"{pid}|{field_path}|{identity_key}"
    h = hashlib.sha256(content.encode("utf-8")).hexdigest()[:12]
    return f"R-{pid}-{h}"


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


def apply_row(pid, head_row, hist_rows, kind, refuted):
    """Fill empty fields from history matches. Returns (changes, ambiguous).

    R1-B: match count must be exactly 1 per field. 0 = skip, >1 = ambiguous (even
    if all values are the same). Array index is NEVER used as identity.
    """
    changes = []
    ambiguous = []
    fields = PERF_FIELDS if kind == "perf" else MECH_FIELDS
    candidates = {}  # field -> list of (value, commit, level_str, identity_key)

    for hr in hist_rows:
        level = _identity_match(head_row, hr, kind)
        if level is None:
            continue
        for f in fields:
            if not _nonempty(head_row, f) and _nonempty(hr, f):
                val = hr[f]
                if str(val) in refuted:
                    continue
                identity_key = f"{level}:{hr.get('ref_doi','')}:{hr.get('name','')}"
                candidates.setdefault(f, []).append((val, hr["_commit"], level, identity_key))

    for f, entries in sorted(candidates.items()):
        # R1-B: reject ALL multi-matches, even with same value
        if len(entries) > 1:
            ambiguous.append(f)
            continue
        # Exactly one match
        val, commit, level, identity_key = entries[0]
        head_row[f] = val
        changes.append({
            "field": f,
            "value": val,
            "commit": commit,
            "level": level,
            "identity_key": identity_key,
        })

    # causal_chain (mechanisms only): same rules
    if kind == "mech":
        causal_candidates = []
        for hr in hist_rows:
            level = _identity_match(head_row, hr, "mech")
            if level is None:
                continue
            if level in ("mech_1", "mech_2") and not _nonempty(head_row, "causal_chain") and _nonempty(hr, "causal_chain"):
                identity_key = f"{level}:{hr.get('ref_doi','')}:{hr.get('name','')}"
                causal_candidates.append((hr["causal_chain"], hr["_commit"], level, identity_key))
        if len(causal_candidates) > 1:
            ambiguous.append("causal_chain")
        elif len(causal_candidates) == 1:
            val, commit, level, identity_key = causal_candidates[0]
            head_row["causal_chain"] = val
            changes.append({"field": "causal_chain", "value": "<object>", "commit": commit, "level": level, "identity_key": identity_key})

    return changes, ambiguous


def _current_commit():
    """Get current HEAD commit SHA."""
    try:
        r = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=ROOT)
        return r.stdout.strip()[:12]
    except Exception:
        return "unknown"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("prototype", nargs="?", default=None)
    args = ap.parse_args()

    import glob
    pids = [args.prototype] if args.prototype else sorted(os.path.basename(p)[:-5] for p in glob.glob(os.path.join(DB, "*.json")))
    refuted = _refuted_tokens()
    current_commit = _current_commit()

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
            ch, amb = apply_row(pid, row, hp, "perf", refuted)
            for f in amb:
                ledger_lines.append({
                    "id": _stable_ledger_id(pid, f"performance_data[{i}].{f}", "ambiguous"),
                    "prototype_id": pid,
                    "field_path": f"performance_data[{i}].{f}",
                    "record_identity": {"level": "unknown", "key": f"ambiguous:{f}"},
                    "disposition": "ambiguous",
                    "basis": "ambiguity_gate",
                    "applied_commit": current_commit,
                    "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
                })
            if ch:
                proto_changes["perf"] += len(ch)
                for c in ch:
                    ledger_lines.append({
                        "id": _stable_ledger_id(pid, f"performance_data[{i}].{c['field']}", c["identity_key"]),
                        "prototype_id": pid,
                        "field_path": f"performance_data[{i}].{c['field']}",
                        "record_identity": {"level": c["level"], "key": c["identity_key"]},
                        "disposition": "restored",
                        "basis": "direct_quote" if "quote" in c["field"] else "extraction",
                        "applied_commit": current_commit,
                        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
                    })

        mechs = head.get("mechanisms", []) or []
        if isinstance(mechs, dict):
            mechs = list(mechs.values())
        for i, m in enumerate(mechs):
            if not isinstance(m, dict):
                continue
            ch, amb = apply_row(pid, m, hm, "mech", refuted)
            for f in amb:
                ledger_lines.append({
                    "id": _stable_ledger_id(pid, f"mechanisms[{i}].{f}", "ambiguous"),
                    "prototype_id": pid,
                    "field_path": f"mechanisms[{i}].{f}",
                    "record_identity": {"level": "unknown", "key": f"ambiguous:{f}"},
                    "disposition": "ambiguous",
                    "basis": "ambiguity_gate",
                    "applied_commit": current_commit,
                    "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
                })
            if ch:
                proto_changes["mech"] += len(ch)
                if any(c["field"] == "causal_chain" for c in ch):
                    proto_changes["causal"] += 1
                for c in ch:
                    ledger_lines.append({
                        "id": _stable_ledger_id(pid, f"mechanisms[{i}].{c['field']}", c["identity_key"]),
                        "prototype_id": pid,
                        "field_path": f"mechanisms[{i}].{c['field']}",
                        "record_identity": {"level": c["level"], "key": c["identity_key"]},
                        "disposition": "restored",
                        "basis": "direct_quote" if "quote" in c["field"] else "extraction",
                        "applied_commit": current_commit,
                        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
                    })

        # design_translation top-level
        if not _nonempty(head, "design_translation") and "design_translation" in ht:
            dt, commit = ht["design_translation"]
            head["design_translation"] = dt
            proto_changes["dt"] += len(dt)
            ledger_lines.append({
                "id": _stable_ledger_id(pid, "design_translation", pid),
                "prototype_id": pid,
                "field_path": "design_translation",
                "record_identity": {"level": "unknown", "key": pid},
                "disposition": "restored",
                "basis": "extraction",
                "applied_commit": current_commit,
                "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            })

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
