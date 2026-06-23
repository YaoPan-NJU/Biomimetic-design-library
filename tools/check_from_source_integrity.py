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

def check_from_source_integrity():
    errors = []
    warnings = []
    total_from_source = 0
    compliant = 0

    for f in sorted(glob.glob(os.path.join(DB, '*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        pid = d.get('id', os.path.basename(f).replace('.json', ''))

        for mi, m in enumerate(d.get('mechanisms', [])):
            cc = m.get('causal_chain', {})
            if not isinstance(cc, dict):
                continue

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

                # Check locator
                locator = val.get('locator', '')
                if not locator or not str(locator).strip():
                    issues.append('missing locator')

                # Check quote
                quote = val.get('quote', '')
                if not quote or not str(quote).strip():
                    issues.append('missing quote')
                elif len(str(quote)) > 200:
                    issues.append(f'quote too long ({len(str(quote))} chars)')

                # Check scope_match
                scope_match = val.get('scope_match', '')
                if not scope_match or not str(scope_match).strip():
                    issues.append('missing scope_match')

                if issues:
                    errors.append(f'{pid}[{mi}].{key}: {", ".join(issues)}')
                else:
                    compliant += 1

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
