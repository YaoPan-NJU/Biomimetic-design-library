#!/usr/bin/env python3
"""
Check brief mechanism binding: for each candidate in a brief, verify that
the displayed mechanism's STRUCTURED FIELDS (molecular_feature_links,
functional_groups, key_structures) have non-empty overlap with the query's
molecular_features/likely_interactions.

Classification:
- ERROR: structured fields populated but zero overlap with query → real binding mismatch
- WARNING: all structured fields empty → data completeness gap (not a binding error)
- PASS: structured fields have overlap with query

Exit code 0 = 0 errors (warnings don't block), non-zero = errors found.
"""

import json
import sys
import os
import glob
import re

BRIEF_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                         'examples', 'adrmats_briefs')


def extract_keywords(text):
    """Extract meaningful keywords from Chinese/English text."""
    if not text:
        return set()
    text = text.lower()
    parts = re.split(r'[/,，、（）()\s\-→。；：「」【】《》]+', text)
    stop_words = {'的', '和', '与', '对', '在', '是', '有', '为', '等', '及', 'a', 'an', 'the', 'of', 'to', 'in', 'for', 'and'}
    return {p.strip() for p in parts if len(p.strip()) >= 2 and p.strip() not in stop_words}


def check_brief(filepath):
    """Check a single brief file for mechanism binding."""
    errors = []
    warnings = []
    with open(filepath, encoding='utf-8') as f:
        data = json.load(f)

    brief = data.get('brief', data)
    context = brief.get('context', {})
    pp = context.get('pollutant_profile', {})
    query_features = pp.get('molecular_features', [])
    query_interactions = pp.get('likely_interactions', [])
    query_all_text = ' '.join(query_features + query_interactions)
    query_keywords = extract_keywords(query_all_text)
    for feat in query_features:
        for part in feat.split('/'):
            part = part.strip()
            if len(part) >= 2:
                query_keywords.add(part.lower())
    for inter in query_interactions:
        for part in inter.split('/'):
            part = part.strip()
            if len(part) >= 2:
                query_keywords.add(part.lower())

    candidates = brief.get('candidates', [])
    for i, c in enumerate(candidates):
        mech = c.get('mechanism', {})
        pid = c.get('prototype_id', 'unknown')

        # Structured fields only
        mfl = set(x.lower() for x in mech.get('molecular_feature_links', []))
        fg_raw = mech.get('functional_groups', '')
        fg_text = (fg_raw if isinstance(fg_raw, str) else ' '.join(str(x) for x in fg_raw)).lower()
        fg_keywords = extract_keywords(fg_text)
        ks_raw = mech.get('key_structures', [])
        ks_text = (' '.join(str(x) for x in ks_raw) if isinstance(ks_raw, list) else str(ks_raw)).lower()
        ks_keywords = extract_keywords(ks_text)

        structured_keywords = mfl | fg_keywords | ks_keywords
        structured_text = fg_text + ' ' + ks_text
        has_structured_data = bool(mfl or fg_keywords or ks_keywords)

        # Check overlap
        matched = query_keywords & structured_keywords
        for qf in query_features:
            if len(qf) >= 3 and qf in structured_text:
                matched.add(qf)
        for qi in query_interactions:
            if len(qi) >= 2 and qi in structured_text:
                matched.add(qi)

        # Special case: oil-water / superwetting queries with empty features
        if not query_keywords:
            match_basis = c.get('match', {}).get('match_basis', '')
            if match_basis in ('direct_pollutant_evidence', 'molecular_feature_inference'):
                matched.add('domain-match-fallback')

        if not matched:
            if has_structured_data:
                # ERROR: structured data exists but doesn't match query
                errors.append({
                    'candidate_index': i,
                    'prototype_id': pid,
                    'mechanism_name': mech.get('name', ''),
                    'functional_groups': fg_raw,
                    'key_structures': ks_raw,
                    'molecular_feature_links': list(mfl),
                    'query_features': query_features,
                    'issue': 'BINDING_MISMATCH: structured fields populated but zero overlap with query features'
                })
            else:
                # WARNING: all structured fields empty — data completeness gap
                warnings.append({
                    'candidate_index': i,
                    'prototype_id': pid,
                    'mechanism_name': mech.get('name', ''),
                    'issue': 'NO_STRUCTURED_DATA: functional_groups, key_structures, molecular_feature_links all empty'
                })

    return errors, warnings


def main():
    briefs = sorted(glob.glob(os.path.join(BRIEF_DIR, '*.json')))
    if not briefs:
        print(f"❌ No briefs found in {BRIEF_DIR}")
        return 1

    total_errors = 0
    total_warnings = 0
    for bp in briefs:
        name = os.path.basename(bp)
        errors, warnings = check_brief(bp)
        if errors:
            print(f"❌ {name}: {len(errors)} errors, {len(warnings)} warnings")
            for e in errors:
                print(f"   ERROR [{e['candidate_index']}] {e['prototype_id']}: {e['issue']}")
                print(f"      mechanism: {e['mechanism_name'][:60]}")
                print(f"      functional_groups: {str(e['functional_groups'])[:80]}")
            total_errors += len(errors)
            total_warnings += len(warnings)
        elif warnings:
            print(f"⚠️  {name}: {len(warnings)} warnings (no errors)")
            total_warnings += len(warnings)
        else:
            print(f"✅ {name}")

    print(f"\n总计: {len(briefs)} briefs, {total_errors} errors, {total_warnings} warnings")
    if total_errors > 0:
        return 1
    else:
        print("✅ 0 errors — G2 PASS (warnings are data completeness gaps, not binding failures)")
        return 0


if __name__ == '__main__':
    sys.exit(main())
