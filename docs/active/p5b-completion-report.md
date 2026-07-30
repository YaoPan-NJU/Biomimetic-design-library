# P5-B Completion Report — v0.1 Release Readiness

**Date**: 2026-06-21
**HEAD**: a74838a (to be updated after commit)
**Branch**: review

## Executive Summary

P5-B evidence completion batch is done. All validators pass green. The library is at v0.1 release readiness for ADRMATS as a heuristic candidate retrieval module.

## Changes Made

### 1. Boundary Conditions (7 prototypes fixed)
- **5 active empty-shell prototypes** (biomineralization-template, coral-skeleton, dna-aptamer, magnetic-bacteria, mycelium): Added placeholder mechanisms with causal_chain + boundary_conditions (gate_level=soft, basis=llm_inferred)
- **2 background-only prototypes** (diatom-inspired-porous, silkworm-silk): Re-added causal_chain with knowledge_gap markers after parking revert
- All 7 labeled honestly as `placeholder` or `background_only` with scope_notes
- **No deprecate/park/delete/merge/rename** performed (per constraint)

### 2. Causal Cards Added (5 active prototypes)
| Prototype | Mechanism | Basis | Causal Chain |
|-----------|-----------|-------|--------------|
| alginate | 海藻酸盐羧基/羟基螯合吸附 | literature (DOI) | ✅ qualified |
| cellulose-nanocrystal | 纤维素纳米晶表面官能团吸附 | llm_inferred | ✅ qualified |
| metal-organic-framework | MOF高比表面积孔道吸附 | literature (DOI) | ✅ qualified |
| starch-granule | 淀粉颗粒羟基吸附与改性增强 | literature (DOI) | ✅ qualified |
| mycelium | 菌丝体几丁质/葡聚糖生物吸附 | llm_inferred | ✅ qualified |

### 3. Placeholder/Narrow-Scope Labels
| Prototype | Label | Scope Note |
|-----------|-------|------------|
| biomineralization-template | placeholder | No verified adsorption data |
| coral-skeleton | placeholder | No verified adsorption data |
| diatom-inspired-porous | background_only | Superseded by diatom-frustule |
| dna-aptamer | placeholder | No verified adsorption data |
| magnetic-bacteria | placeholder | No verified adsorption data |
| silkworm-silk | background_only | Superseded by silk-fibroin |

### 4. Deep Evidence Supplementation (Extended tier, stayed Extended)
- **alginate**: honesty_ledger updated (70 perf rows, all needs_review), tested_conditions boundary added
- **starch-granule**: honesty_ledger updated (61 perf rows), tested pH range [4,7] boundary added
- **metal-organic-framework**: honesty_ledger updated (15 perf rows), knowledge_gap boundary added
- **Note**: All perf rows have DOI but lack verification_quote/locator. PDF access needed for quote extraction.

### 5. Lotus-leaf Core Promotion
- library_tier: `core` with narrow scope
- scope_note: "Core tier limited to superwetting / oil-water separation / surface design"
- Not a general adsorption prototype

### 6. Litextract Security Fix
- Submodule pointer updated from 203b0cf to 525de71
- Hardcoded tokens replaced with environment variable references

## Validation Results

| Validator | Result |
|-----------|--------|
| validate_consistency --strict | ✅ 0 errors, 171 warnings (documentation/instance-data, all pre-existing) |
| check_chimera --strict | ✅ 0 violations |
| check_causal_chain | ✅ 88 qualified, 0 empty-basis, 0 prototypes without card |
| check_boundary_guardrail | ✅ PASS (0 missing BC) |
| canon_metrics --guard | ✅ GREEN (no protected-metric decreases) |
| canon_metrics --check-integrity | ✅ PASS |
| validate_ledger_v2 | ✅ PASS (0 errors) |
| test_invariant_guard | ✅ 7/7 PASS |
| verify_adrmats_delivery | ✅ 6/6 PASS |

## Library Statistics

| Metric | Value |
|--------|-------|
| Total prototypes (all dirs) | 70 (36 root + 5 separation + 24 enrichment + 4 materials + 1 parked) |
| Root canon prototypes | 36 |
| Core tier | 26 |
| Extended tier | 9 |
| Exploratory tier | 1 |
| Active prototypes | 33 |
| Deprecated prototypes | 2 |
| Total mechanisms | 510 |
| Total performance_data | 498 |
| Qualified causal cards | 88 |
| Boundary conditions | 121 |
| Honesty ledgers | 36 |

## Worktree Status

- `.claude/settings.local.json`: Local-only user change, not part of canon commits
- `docs/active/NOTE-TO-CODEX-V3-RATIONALE.md`: Untracked, excluded from review
- `docs/optimization-v1/`: Untracked, excluded from review

## Known Limitations

1. **171 validate_consistency warnings**: All pre-existing — placeholder text in prototype.md (11), empty organism frontmatter (13), R14 instance-data in mechanisms (15+). Documentation issues, not data integrity.
2. **No verification_quote/locator on perf rows**: alginate (70), starch-granule (61), MOF (15) all have DOI but no quote. PDF access needed.
3. **6 placeholder prototypes**: No verified data, design_translation is llm_inference only.
4. **Full 60-80 expansion**: Deferred, requires Yao authorization.
5. **alginate/starch-granule/MOF**: Stay Extended. Need deeper evidence before Core promotion.

## Commits (to be made)

1. `fix(P5-B): causal chain cleanup + qualified cards for 5 active prototypes`
2. `fix(P5-B): placeholder labels + boundary conditions for empty-shell prototypes`
3. `docs(P5-B): completion report + execution-state update`

## Next Steps

1. Yao review of P5-B completion
2. If approved: full 60-80 prototype expansion (requires explicit authorization)
3. PDF access for quote extraction on alginate/starch-granule/MOF perf rows
