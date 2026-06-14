#!/usr/bin/env python3
"""Phase 0 baseline snapshot: stats for prototypes_db/*.json (including parked/ and enrichment/)."""
import json, glob, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(ROOT, "prototypes_db")

def load_prototypes(subdir=None):
    """Load prototype JSONs from a directory. Returns list of (filepath, data)."""
    if subdir:
        d = os.path.join(DB_DIR, subdir)
    else:
        d = DB_DIR
    if not os.path.isdir(d):
        return []
    pattern = os.path.join(d, "*.json")
    results = []
    for f in sorted(glob.glob(pattern)):
        with open(f, encoding="utf-8") as fh:
            results.append((os.path.basename(f), json.load(fh)))
    return results

def normalize_mechanisms(data):
    """Return mechanisms as a list (handle both list and dict formats)."""
    ms = data.get("mechanisms", [])
    if isinstance(ms, dict):
        # enrichment format: dict keyed by mechanism name
        result = []
        for name, val in ms.items():
            if isinstance(val, dict):
                result.append(val)
            elif isinstance(val, list):
                # some enrichment files have dict[name] = list of mechanisms
                result.extend(v for v in val if isinstance(v, dict))
        return result
    elif isinstance(ms, list):
        return [m for m in ms if isinstance(m, dict)]
    return []

def is_grounded(m):
    """§1.3: mechanism is grounded iff causal_chain has all 4 core elements non-empty and not needs_review."""
    cc = m.get("causal_chain")
    if not cc or not isinstance(cc, dict):
        return False
    for key in ("pollutant_feature", "bio_structure", "interaction", "why_it_works"):
        elem = cc.get(key)
        if not elem or not isinstance(elem, dict):
            return False
        text = (elem.get("text") or "").strip()
        if not text:
            return False
        # needs_review elements don't count as grounded
        basis = (elem.get("basis") or "").strip()
        # We check: if the field explicitly says needs_review, not grounded
        # But basis is from_source|llm_inferred; verification is the tier
        # The rule says "都不是 needs_review" — we interpret as the mechanism's overall verification
        # Actually §1.3 says the 4 elements themselves must not be needs_review.
        # Since elements don't have their own verification, we check the mechanism's verification.
        # If the mechanism itself is needs_review, it's not grounded.
    # Also check: mechanism verification must not be needs_review
    v = m.get("verification", "")
    if v == "needs_review":
        return False
    return True

def analyze_prototypes(prototypes):
    """Analyze a list of (filename, data) prototypes."""
    total_mechanisms = 0
    grounded_mechanisms = 0
    total_performance = 0
    verification_counts = collections.Counter()
    perf_verification_counts = collections.Counter()
    empty_pollutant_count = 0
    empty_pollutant_non_needs_review = 0
    empty_shells = []
    prototype_details = []

    for fname, data in prototypes:
        pid = data.get("id", fname.replace(".json", ""))
        mechanisms = normalize_mechanisms(data)
        perf = data.get("performance_data", [])
        if not isinstance(perf, list):
            perf = []
        n_mech = len(mechanisms)
        n_grounded = sum(1 for m in mechanisms if is_grounded(m))
        n_perf = len(perf)

        total_mechanisms += n_mech
        grounded_mechanisms += n_grounded
        total_performance += n_perf

        for m in mechanisms:
            v = m.get("verification", "unspecified")
            verification_counts[v] += 1

        empty_pollutant_this = 0
        for p in perf:
            pv = p.get("verification", "unspecified")
            perf_verification_counts[pv] += 1
            pol = (p.get("pollutant") or "").strip()
            if not pol:
                empty_pollutant_count += 1
                empty_pollutant_this += 1
                if pv != "needs_review":
                    empty_pollutant_non_needs_review += 1

        # Empty shell: 0 mechanisms AND 0 performance_data
        if n_mech == 0 and n_perf == 0:
            empty_shells.append(pid)

        prototype_details.append({
            "id": pid,
            "file": fname,
            "mechanisms": n_mech,
            "grounded": n_grounded,
            "performance": n_perf,
            "empty_pollutant": empty_pollutant_this,
            "has_causal_chain": sum(1 for m in mechanisms if "causal_chain" in m),
        })

    return {
        "total_prototypes": len(prototypes),
        "total_mechanisms": total_mechanisms,
        "grounded_mechanisms": grounded_mechanisms,
        "total_performance": total_performance,
        "verification_counts": dict(verification_counts),
        "perf_verification_counts": dict(perf_verification_counts),
        "empty_pollutant_total": empty_pollutant_count,
        "empty_pollutant_non_needs_review": empty_pollutant_non_needs_review,
        "empty_shells": empty_shells,
        "details": prototype_details,
    }

def format_report(main_stats, enrich_stats, parked_stats):
    lines = []
    lines.append("# Phase 0 — Baseline Snapshot")
    lines.append("")
    lines.append(f"> Generated by `tools/snapshot_stats.py`")
    lines.append("")

    def section(name, stats):
        lines.append(f"## {name}")
        lines.append("")
        lines.append(f"| Metric | Value |")
        lines.append(f"|--------|-------|")
        lines.append(f"| Prototypes | {stats['total_prototypes']} |")
        lines.append(f"| Mechanisms total | {stats['total_mechanisms']} |")
        lines.append(f"| Mechanisms grounded (§1.3) | {stats['grounded_mechanisms']} |")
        lines.append(f"| Mechanisms with causal_chain | {sum(d['has_causal_chain'] for d in stats['details'])} |")
        lines.append(f"| Performance data total | {stats['total_performance']} |")
        lines.append(f"| Empty pollutant (total) | {stats['empty_pollutant_total']} |")
        lines.append(f"| Empty pollutant (non-needs_review) | {stats['empty_pollutant_non_needs_review']} |")
        lines.append("")
        lines.append(f"### Verification distribution (mechanisms)")
        lines.append("")
        for k, v in sorted(stats['verification_counts'].items()):
            lines.append(f"| {k} | {v} |")
        lines.append("")
        lines.append(f"### Verification distribution (performance_data)")
        lines.append("")
        for k, v in sorted(stats['perf_verification_counts'].items()):
            lines.append(f"| {k} | {v} |")
        lines.append("")
        if stats['empty_shells']:
            lines.append(f"### Empty shells (0 mechanisms + 0 performance)")
            lines.append("")
            for s in stats['empty_shells']:
                lines.append(f"- `{s}`")
            lines.append("")
        lines.append(f"### Per-prototype details")
        lines.append("")
        lines.append(f"| id | mech | grounded | causal_chain | perf | empty_pol |")
        lines.append(f"|---|------|----------|-------------|------|-----------|")
        for d in stats['details']:
            lines.append(f"| {d['id']} | {d['mechanisms']} | {d['grounded']} | {d['has_causal_chain']} | {d['performance']} | {d['empty_pollutant']} |")
        lines.append("")

    section("Active prototypes (prototypes_db/*.json)", main_stats)
    section("Enrichment (prototypes_db/enrichment/*.json)", enrich_stats)
    section("Parked (prototypes_db/parked/*.json)", parked_stats)

    return "\n".join(lines)

if __name__ == "__main__":
    main = load_prototypes()
    enrich = load_prototypes("enrichment")
    parked = load_prototypes("parked")

    main_stats = analyze_prototypes(main)
    enrich_stats = analyze_prototypes(enrich)
    parked_stats = analyze_prototypes(parked)

    report = format_report(main_stats, enrich_stats, parked_stats)

    out_dir = os.path.join(ROOT, "docs", "optimization-v1")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "phase0-baseline.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Baseline written to {out_path}")
    print(f"Active prototypes: {main_stats['total_prototypes']}")
    print(f"Mechanisms: {main_stats['total_mechanisms']} total, {main_stats['grounded_mechanisms']} grounded")
    print(f"Performance: {main_stats['total_performance']}")
    print(f"Empty pollutant: {main_stats['empty_pollutant_total']} (non-needs_review: {main_stats['empty_pollutant_non_needs_review']})")
    print(f"Empty shells: {main_stats['empty_shells']}")
    print(f"Verification: {main_stats['verification_counts']}")
