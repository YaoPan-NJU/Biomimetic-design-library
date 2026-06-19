#!/usr/bin/env python3
"""
Canon count-guard metrics (M1).

A destructive canon operation is one that *silently* drops protected evidence
(rows, quotes, locators, causal chains, translations, boundaries, scope notes,
tier metadata). This module snapshots those counts for a prototype tree, and a
guard compares two snapshots — failing on any *unexplained* decrease.

Protected metrics: a decrease is a regression unless an allowlist entry explains
it (e.g. an approved wrong-source removal recorded in the recovery ledger).

Usage:
    python3 -X utf8 tools/canon_metrics.py                 # print working-tree snapshot
    python3 -X utf8 tools/canon_metrics.py --guard          # compare working tree vs HEAD; exit 1 on drops
    python3 -X utf8 tools/canon_metrics.py --guard --allowlist allowlist.json
    python3 -X utf8 tools/canon_metrics.py --commit 4987c0a # snapshot a commit
"""
import json
import os
import sys
import glob
import argparse
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(ROOT, "prototypes_db")


def _truthy(v):
    return bool(v) and str(v).strip() != ""


def _load_tree(path):
    """Load all prototype JSONs from a directory. Returns {prototype_id: data}."""
    out = {}
    if not path or not os.path.isdir(path):
        return out
    for f in sorted(glob.glob(os.path.join(path, "*.json"))):
        try:
            with open(f, encoding="utf-8") as fh:
                d = json.load(fh)
        except Exception:
            continue
        pid = d.get("id") or os.path.basename(f)[:-5]
        out[pid] = d
    return out


def _mech_list(data):
    ms = data.get("mechanisms", [])
    if isinstance(ms, dict):  # enrichment object-keyed mirror
        out = []
        for v in ms.values():
            if isinstance(v, dict):
                out.append(v)
            elif isinstance(v, list):
                out.extend(x for x in v if isinstance(x, dict))
        return out
    return [m for m in ms if isinstance(m, dict)]


def _perf_list(data):
    p = data.get("performance_data", [])
    return [x for x in p if isinstance(x, dict)] if isinstance(p, list) else []


def snapshot_data(data):
    """Compute protected-count snapshot for a single prototype dict."""
    s = {
        "prototypes": 0, "perf_rows": 0, "perf_quotes": 0, "perf_locators": 0,
        "mechanisms": 0, "mech_quotes": 0, "causal_chain_objects": 0,
        "causal_qualified_elements": 0, "boundary_conditions": 0,
        "design_translation_entries": 0, "narrative_entries": 0,
        "engineering_constraints": 0, "boundary_rules": 0, "scope_notes": 0,
        "tier_metadata": 0, "lifecycle_metadata": 0,
    }
    if not isinstance(data, dict):
        return s
    s["prototypes"] = 1
    for p in _perf_list(data):
        s["perf_rows"] += 1
        if _truthy(p.get("verification_quote")):
            s["perf_quotes"] += 1
        if _truthy(p.get("source_locator")) or _truthy(p.get("locator")):
            s["perf_locators"] += 1
    for m in _mech_list(data):
        s["mechanisms"] += 1
        cc = m.get("causal_chain")
        if _truthy(m.get("verification_quote")) or (isinstance(cc, dict) and _truthy(cc.get("verification_quote"))):
            s["mech_quotes"] += 1
        if isinstance(cc, dict) and cc:
            s["causal_chain_objects"] += 1
            for k in ("pollutant_feature", "bio_structure", "interaction", "why_it_works"):
                el = cc.get(k)
                if isinstance(el, dict) and _truthy(el.get("text")):
                    s["causal_qualified_elements"] += 1
            bc = cc.get("boundary_conditions")
            if isinstance(bc, list):
                s["boundary_conditions"] += len([b for b in bc if isinstance(b, dict)])
    dt = data.get("design_translation")
    if isinstance(dt, list):
        s["design_translation_entries"] += len(dt)
    ne = data.get("narrative", {})
    if isinstance(ne, dict):
        ents = ne.get("entries")
        if isinstance(ents, list):
            s["narrative_entries"] += len(ents)
    ec = data.get("engineering_constraints")
    if isinstance(ec, list):
        s["engineering_constraints"] += len(ec)
    ps = data.get("provenance_summary", {})
    if isinstance(ps, dict):
        br = ps.get("boundary_rules")
        if isinstance(br, list):
            s["boundary_rules"] += len(br)
    if any(_truthy(data.get(k)) for k in ("scope_note", "scope_caveat", "applicability_note")):
        s["scope_notes"] += 1
    if _truthy(data.get("library_tier")):
        s["tier_metadata"] += 1
    if _truthy(data.get("lifecycle_status")):
        s["lifecycle_metadata"] += 1
    return s


def _add(dst, src):
    for k, v in src.items():
        dst[k] = dst.get(k, 0) + v


def snapshot_dir(path):
    """Compute protected-count snapshot for a directory of prototype JSONs."""
    tree = _load_tree(path)
    s = {k: 0 for k in ["prototypes","perf_rows","perf_quotes","perf_locators","mechanisms","mech_quotes",
                        "causal_chain_objects","causal_qualified_elements","boundary_conditions",
                        "design_translation_entries","narrative_entries","engineering_constraints",
                        "boundary_rules","scope_notes","tier_metadata","lifecycle_metadata"]}
    for pid, d in tree.items():
        _add(s, snapshot_data(d))
    return s


def snapshot_commit(commit):
    """Snapshot a git commit's root-level canon (prototypes_db/*.json)."""
    r = subprocess.run(
        ["git", "-c", "core.quotepath=false", "ls-tree", "-r", "--name-only", commit, "prototypes_db/"],
        capture_output=True, text=True,
    )
    root_files = [x for x in r.stdout.splitlines()
                  if x.startswith("prototypes_db/") and x.endswith(".json") and x.count("/") == 1]
    s = {k: 0 for k in ["prototypes","perf_rows","perf_quotes","perf_locators","mechanisms","mech_quotes",
                        "causal_chain_objects","causal_qualified_elements","boundary_conditions",
                        "design_translation_entries","narrative_entries","engineering_constraints",
                        "boundary_rules","scope_notes","tier_metadata","lifecycle_metadata"]}
    for f in root_files:
        r = subprocess.run(["git", "show", f"{commit}:{f}"], capture_output=True)
        if r.returncode != 0:
            continue
        try:
            d = json.loads(r.stdout)
        except Exception:
            continue
        _add(s, snapshot_data(d))
    return s


# Protected metrics: a decrease is a regression unless allowlisted.
PROTECTED = [
    "prototypes", "perf_rows", "perf_quotes", "perf_locators", "mechanisms",
    "mech_quotes", "causal_chain_objects", "causal_qualified_elements",
    "boundary_conditions", "design_translation_entries", "narrative_entries",
    "engineering_constraints", "boundary_rules", "scope_notes", "tier_metadata",
]


def compare(before, after, allowlist=None):
    """Return list of regressions (metric decreased without allowlist explanation)."""
    allowlist = allowlist or []
    allowset = {a["metric"] for a in allowlist}
    regs = []
    for m in PROTECTED:
        b = before.get(m, 0)
        a = after.get(m, 0)
        if a < b and m not in allowset:
            regs.append({"metric": m, "before": b, "after": a, "delta": a - b})
    return regs


def main():
    ap = argparse.ArgumentParser(description="Canon count-guard metrics")
    ap.add_argument("--guard", action="store_true", help="compare working tree vs HEAD; exit 1 on unexplained drops")
    ap.add_argument("--commit", help="snapshot this commit instead of working tree")
    ap.add_argument("--allowlist", help="JSON list of {metric} entries permitted to decrease")
    args = ap.parse_args()

    if args.guard:
        before = snapshot_commit("HEAD")
        after = snapshot_dir(DB_DIR)
        allowlist = []
        if args.allowlist and os.path.exists(args.allowlist):
            allowlist = json.load(open(args.allowlist, encoding="utf-8"))
        regs = compare(before, after, allowlist)
        if regs:
            print("CANON GUARD: unexplained protected-metric decreases vs HEAD:")
            for r in regs:
                print(f"  {r['metric']}: {r['before']} -> {r['after']} (delta {r['delta']})")
            return 1
        print("CANON GUARD: no protected-metric decreases vs HEAD.")
        return 0

    if args.commit:
        print(json.dumps(snapshot_commit(args.commit), ensure_ascii=False, indent=2))
        return 0

    print(json.dumps(snapshot_dir(DB_DIR), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
