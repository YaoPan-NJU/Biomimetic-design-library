#!/usr/bin/env python3
"""
Validator: check_from_source_integrity.py

Ensures every basis=from_source element in causal_chain has:
1. source (non-empty DOI/patent/standard number)
2. locator (exact page N, non-empty)
3. quote (≤200 chars, non-empty, from source text)
4. scope_match (≥2 keywords from claim appear in quote)

Any violation = error. Prevents evidence label inflation.
"""
import json, glob, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(REPO, 'prototypes_db')

import re

def _has_page_reference(locator):
    """Check if locator contains a real page reference."""
    if not locator:
        return False
    loc = str(locator).strip()
    # Must contain a standalone number (page reference)
    # Accept: "page 5", "p.5", "pp.5-10", "5", etc.
    if re.search(r'\b\d+\b', loc):
        # Reject vague patterns
        vague_patterns = ['visual_cache', 'PDF text', 'text match', 'cache', 'search']
        for vp in vague_patterns:
            if vp in loc.lower():
                return False
        return True
    return False

def _verify_scope_match(scope_match, quote):
    """Verify that scope_match keywords actually appear in quote."""
    if not scope_match or not quote:
        return 0
    # Extract keywords from scope_match
    sm = str(scope_match)
    q = str(quote).lower()
    # Pattern: "Keywords: kw1, kw2, kw3" or similar
    kw_part = sm
    if 'Keywords:' in sm:
        kw_part = sm.split('Keywords:')[1]
    elif 'keywords:' in sm.lower():
        kw_part = sm.lower().split('keywords:')[1]
    # Split by comma, semicolon, or space
    keywords = re.split(r'[,;]\s*', kw_part.strip())
    matched = 0
    for kw in keywords:
        kw = kw.strip().lower()
        if len(kw) >= 2 and kw in q:
            matched += 1
    return matched

def check_from_source_integrity():
    errors = []
    warnings = []
    total_from_source = 0
    compliant = 0

    for f in sorted(glob.glob(os.path.join(DB, '*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        pid = d.get('id', os.path.basename(f).replace('.json', ''))

        # Track quotes per mechanism for duplicate detection
        mechanism_quotes = {}

        for mi, m in enumerate(d.get('mechanisms', [])):
            cc = m.get('causal_chain', {})
            if not isinstance(cc, dict):
                continue

            mech_quotes = []

            for key in ['pollutant_feature', 'bio_structure', 'interaction', 'why_it_works']:
                val = cc.get(key, {})
                if not isinstance(val, dict) or val.get('basis') != 'from_source':
                    continue

                total_from_source += 1
                issues = []

                # Check source
                source = val.get('source', '')
                if not source or not source.strip():
                    issues.append('missing source')

                # Check locator (QUALITY check)
                locator = val.get('locator', '')
                if not locator or not str(locator).strip():
                    issues.append('missing locator')
                elif not _has_page_reference(locator):
                    issues.append(f'vague locator: "{locator[:50]}"')

                # Check quote
                quote = val.get('quote', '')
                if not quote or not str(quote).strip():
                    issues.append('missing quote')
                elif len(str(quote)) > 200:
                    issues.append(f'quote too long ({len(str(quote))} chars)')

                # Check scope_match (QUALITY check)
                scope_match = val.get('scope_match', '')
                if not scope_match or not str(scope_match).strip():
                    issues.append('missing scope_match')
                elif quote:
                    matched_kw = _verify_scope_match(scope_match, quote)
                    if matched_kw < 2:
                        issues.append(f'scope_match keywords not in quote ({matched_kw} found)')

                if issues:
                    errors.append(f'{pid}[{mi}].{key}: {", ".join(issues)}')
                else:
                    compliant += 1

                # Track quote for duplicate detection
                if quote:
                    mech_quotes.append((key, str(quote)))

            # Duplicate quote warning
            if len(mech_quotes) >= 3:
                unique_quotes = set(q for _, q in mech_quotes)
                if len(unique_quotes) == 1:
                    warnings.append(f'{pid}[{mi}]: all {len(mech_quotes)} elements share same quote (copy-paste?)')

    return {
        'total_from_source': total_from_source,
        'compliant': compliant,
        'non_compliant': total_from_source - compliant,
        'errors': errors,
        'warnings': warnings
    }

def main():
    result = check_from_source_integrity()

    print(f'=== From Source Integrity Check ===')
    print(f'Total from_source: {result["total_from_source"]}')
    print(f'Compliant: {result["compliant"]}')
    print(f'Non-compliant: {result["non_compliant"]}')

    if result['errors']:
        print(f'\n❌ ERRORS ({len(result["errors"])}):')
        for e in result['errors'][:20]:
            print(f'  {e}')
        if len(result['errors']) > 20:
            print(f'  ... and {len(result["errors"]) - 20} more')
        sys.exit(1)
    else:
        print(f'\n✅ All from_source elements compliant')
        sys.exit(0)

if __name__ == '__main__':
    main()
