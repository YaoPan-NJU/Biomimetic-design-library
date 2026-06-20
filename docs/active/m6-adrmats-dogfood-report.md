# M6 ADRMATS Dogfood Report

**Date**: 2026-06-21
**HEAD**: (to be updated after commit)
**Branch**: review

## Executive Summary

ADRMATS dogfood evaluation complete. 7 briefs generated covering PFOA, SMX, BPA, Pb(II), Cr(VI), Methylene Blue, and oil-water separation. Key finding: matching architecture works well for molecular pollutants but fails for use-case queries (oil-water). Design_translation deepened for 8 top prototypes.

## Dogfood Scorecard Summary

| Case | Candidates | Avg Score | Top Issue |
|------|-----------|-----------|-----------|
| PFOA | 4 | 3.0/10 | Low honesty_ledger, no boundaries |
| SMX | 4 | 3.0/10 | Low honesty_ledger, no boundaries |
| BPA | 4 | 3.0/10 | Low honesty_ledger, no boundaries |
| Pb(II) | 8 | 4.5/10 | Low DT actionability |
| Cr(VI) | 5 | 4.0/10 | Low honesty_ledger |
| Methylene Blue | 5 | 3.5/10 | Low honesty_ledger |
| oil-water | 0 | N/A | Matching architecture gap |

## Changes Made

### M6-B: Design Translation Deepening (8 prototypes)
Enhanced DT with: design_principle, implementation_example, constraints, failure_modes, evidence_tier.

| Prototype | Evidence Tier |
|-----------|--------------|
| chitosan | lead |
| plant-tannin | lead |
| polydopamine-coating | fact |
| mussel-foot-adhesion | fact |
| fish-scale-hydroxyapatite | fact |
| alginate | lead |
| starch-granule | lead |
| metal-organic-framework | lead |

### M6-C: Feature-Mapping Updates
- Added oil-water/superwetting features to lotus-leaf, superhydrophobic-artificial, water-strider-leg, shark-skin
- Oil-water brief still returns 0 candidates (architectural limitation — use-case vs molecular matching)

### M6-D: Briefs Regenerated
7 briefs in examples/adrmats_briefs/:
- PFOA, SMX, BPA, Pb(II) (existing)
- Cr(VI), Methylene Blue, oil-water (new)

## Failure Taxonomy

### F1: Oil-water matching gap
- **Issue**: `oil-water` is a use-case, not a molecular pollutant
- **Impact**: 0 candidates despite lotus-leaf being relevant
- **Fix**: Add use-case matching layer (architectural change, deferred)

### F2: Low honesty_ledger coverage
- **Issue**: Most candidates lack facts/leads/inferences separation
- **Fix**: P5-B added honesty_ledger to 36 root prototypes; briefs need to surface it better

### F3: Low boundary visibility
- **Issue**: Boundaries exist in prototypes but not surfaced in briefs
- **Fix**: Brief generation should include boundary_conditions

### F4: DT actionability gaps
- **Issue**: Some DTs lack material_handle
- **Fix**: M6-B deepened 8 top prototypes; remaining need work

## Validation Results

| Validator | Result |
|-----------|--------|
| validate_consistency --strict | 0 errors, 171 warnings |
| check_chimera --strict | 0 violations |
| check_boundary_guardrail | PASS |
| canon_metrics --guard | GREEN |
| canon_metrics --check-integrity | PASS |
| verify_adrmats_delivery | 6/6 PASS |

## Remaining Backlog

1. Use-case matching layer for oil-water/superwetting
2. Honesty_ledger surfacing in briefs
3. Boundary surfacing in briefs
4. DT deepening for remaining prototypes
5. Full 60-80 prototype expansion (requires Yao authorization)

## Next Steps

Await Codex review. If accepted, next milestone is ADRMATS usefulness iteration or expansion.
