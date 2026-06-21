#!/usr/bin/env python3
"""Executable gold-set gate: comprehensive checks against v0.2 gold-set expectations."""
import json, glob, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRIEFS_DIR = os.path.join(REPO, 'examples', 'adrmats_briefs')
GOLD_SET_PATH = os.path.join(REPO, 'docs', 'active', 'v0.2-gold-set.json')

def load_gold_set():
    """Load gold-set expectations."""
    if os.path.exists(GOLD_SET_PATH):
        with open(GOLD_SET_PATH, encoding='utf-8') as f:
            return json.load(f)
    return {}

def check_brief(filepath, case_name, gold_set):
    """Check a single brief against gold-set expectations."""
    issues = []

    with open(filepath, encoding='utf-8') as f:
        d = json.load(f)

    brief = d.get('brief', d)
    candidates = brief.get('candidates', [])
    rbc = brief.get('rule_based_cautions', {})

    if case_name not in gold_set:
        return issues

    rules = gold_set[case_name]
    forbidden = set(rules.get('forbidden_normal', []))
    expected = set(rules.get('expected_candidates', []))
    expected_keywords = rules.get('expected_mechanism_keywords', {})

    candidate_pids = set()
    for c in candidates:
        pid = c.get('prototype_id', '')
        honesty = c.get('candidate_honesty', '')
        mech = c.get('mechanism', {})
        mech_name = (mech.get('name', '') or '').lower()
        candidate_pids.add(pid)

        # 1. Forbidden candidates in fact/lead lane
        if pid in forbidden and honesty in ('fact', 'lead'):
            issues.append(f"FORBIDDEN: {pid} appears as {honesty} in normal lane")

        # 2. Mechanism alignment: expected mechanism keywords
        if pid in expected_keywords:
            keywords = expected_keywords[pid]
            if not any(kw.lower() in mech_name for kw in keywords):
                issues.append(f"MECHANISM_MISMATCH: {pid} mechanism '{mech_name[:40]}' doesn't match expected keywords {keywords}")

        # 3. Fact candidates must have source attribution
        if honesty == 'fact':
            attr = mech.get('attribution', {})
            if not attr.get('ref') and not attr.get('source'):
                issues.append(f"FACT_NO_SOURCE: {pid} is fact but mechanism has no source ref")

    # 4. Expected candidates present
    missing_expected = expected - candidate_pids
    if missing_expected:
        issues.append(f"MISSING_EXPECTED: {missing_expected} not in candidates")

    # 5. Hard DO-NOT behavior check
    do_not = rbc.get('do_not', [])
    for dn in do_not:
        if dn.get('basis') != 'from_source':
            issues.append(f"INFERRED_HARD_DO_NOT: {dn.get('prototype_id','')} has basis={dn.get('basis','')}")

    return issues


def main():
    gold_set = load_gold_set()
    if not gold_set:
        print("❌ No gold-set found")
        return 1

    briefs = sorted(glob.glob(os.path.join(BRIEFS_DIR, '*.json')))
    if not briefs:
        print("❌ No briefs found")
        return 1

    total_issues = 0
    for f in briefs:
        fname = os.path.basename(f)
        case_name = fname.replace('.json', '')
        issues = check_brief(f, case_name, gold_set)
        if issues:
            print(f"❌ {fname}: {len(issues)} issues")
            for issue in issues:
                print(f"    - {issue}")
            total_issues += len(issues)
        else:
            print(f"✅ {fname}")

    print(f"\n总计: {len(briefs)} briefs, {total_issues} gold-set issues")
    return 1 if total_issues > 0 else 0


if __name__ == '__main__':
    sys.exit(main())
