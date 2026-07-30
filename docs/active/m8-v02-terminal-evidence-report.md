# M8 v0.2 Terminal Evidence Report

**Date**: 2026-06-21
**HEAD**: (to be updated after commit)
**Branch**: review

## Executive Summary

M8 terminal evidence + causal-chain completion for all 36 root prototypes. 510/510 mechanisms now have qualified causal_chain cards. All validators pass. ADRMATS briefs regenerated.

## Causal Chain Completion

| Metric | Before M8 | After M8 |
|--------|-----------|----------|
| Qualified causal cards | 88/510 (17%) | 510/510 (100%) |
| Empty-basis elements | 0 | 0 |
| Prototypes without card | 0 | 0 |

### Batch Processing Summary
| Batch | Prototypes | Mechanisms Updated |
|-------|-----------|-------------------|
| 1 | chitosan | 107 |
| 2 | superhydrophobic-artificial, mussel-foot-adhesion, water-strider-leg, polydopamine-coating, spider-silk, pitcher-plant-slippery-surface, shark-skin, silk-fibroin, cell-membrane-ion-channel | 281 |
| 3 | bone-structure, cactus-spine, fish-scale-hydroxyapatite, iron-oxidizing-bacteria, lotus-leaf, oyster-shell, plant-tannin, scallop-shell, wood-xylem | 34 |

### Basis Distribution
- `from_source`: mechanisms with DOI/patent reference
- `llm_inferred`: mechanisms without verified source (honest labeling)

## Boundary Guardrail Fixes

| Issue | Count Fixed |
|-------|------------|
| from_source without locator → llm_inferred | 61 |
| Hidden numeric thresholds removed | 1,710 |
| Boundary text with numbers → qualitative | 107 |

## Validation Results

| Validator | Result |
|-----------|--------|
| validate_consistency --strict | 0 errors, 171 warnings |
| check_chimera --strict | 0 violations |
| check_boundary_guardrail | PASS |
| check_causal_chain | 510/510 qualified, 0 empty-basis |
| canon_metrics --guard | GREEN |
| canon_metrics --check-integrity | PASS |
| verify_adrmats_delivery | 6/6 PASS |
| check_brief_usefulness | 7/7 PASS |

## DT Coverage

- 19/36 root prototypes with deepened DT (53%)
- 17/36 still need DT deepening (47%)

## Remaining Backlog (M9-M11)

1. **M9**: Deepen DT for remaining 17 prototypes, repair feature-mapping from dogfood failures
2. **M10**: Full release QA — all validators, source-integrity, duplicate/refuted/chimera guards
3. **M11**: v0.2 release packaging — release notes, final stats, known limitations

## Known Limitations

1. Causal chains for non-source mechanisms use `llm_inferred` basis — honest but not PDF-verified
2. Boundary conditions are mostly qualitative — specific numeric thresholds need PDF source
3. DT deepening incomplete for 17 prototypes
4. 171 validate_consistency warnings (pre-existing documentation issues)
