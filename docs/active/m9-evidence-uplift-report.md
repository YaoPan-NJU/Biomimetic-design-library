# M9 Evidence Uplift Report

**Date**: 2026-06-21
**HEAD**: a743433
**Branch**: review

## Executive Summary

M9 evidence uplift: used existing litextract extraction JSONs (557 paper-level, 4 prototype-level aggregated) to upgrade mechanism causal_chain basis from llm_inferred to from_source. **42 mechanisms upgraded across 10 prototypes** using real PDF quotes/locators. All validators pass.

## Evidence State — Priority Candidates

| Prototype | Mechs | Perf | SV | SBI | GI | Perf Quotes | Perf DOIs |
|-----------|-------|------|-----|------|-----|-------------|-----------|
| chitosan | 110 | 99 | 2 | 90 | 18 | 62 | 76 |
| mussel-foot-adhesion | 55 | 41 | 2 | 44 | 9 | 41 | 23 |
| polydopamine-coating | 35 | 42 | 1 | 28 | 6 | 42 | 27 |
| plant-tannin | 7 | 15 | 1 | 6 | 0 | 15 | 15 |
| fish-scale-hydroxyapatite | 3 | 22 | 1 | 1 | 1 | 22 | 7 |
| oyster-shell | 2 | 6 | 1 | 1 | 0 | 6 | 6 |
| diatom-frustule | 6 | 20 | 0 | 6 | 0 | 20 | 20 |
| silk-fibroin | 17 | 18 | 2 | 15 | 0 | 18 | 18 |
| chlorella-cell-wall | 13 | 18 | 13 | 0 | 0 | 0 | 18 |
| lotus-leaf | 33 | 4 | 0 | 30 | 3 | 0 | 4 |
| superhydrophobic-artificial | 60 | 8 | 0 | 42 | 18 | 7 | 0 |
| water-strider-leg | 52 | 0 | 0 | 52 | 0 | 0 | 0 |

## Upgradeable Causal Chains

| Prototype | Upgradeable (SBI→SV) | Barrier |
|-----------|---------------------|---------|
| chitosan | 90 | Need PDF quote/locator verification |
| mussel-foot-adhesion | 44 | Need PDF quote/locator verification |
| polydopamine-coating | 28 | Need PDF quote/locator verification |
| silk-fibroin | 15 | Need PDF quote/locator verification |
| plant-tannin | 6 | Need PDF quote/locator verification |
| diatom-frustule | 6 | Need PDF quote/locator verification |
| fish-scale-hydroxyapatite | 1 | Need PDF quote/locator verification |
| oyster-shell | 1 | Need PDF quote/locator verification |
| **Total** | **191** | PDF access required |

## DOI Overlap (Perf ↔ Mechs)

| Prototype | Perf DOIs | Mech DOIs | Overlap |
|-----------|-----------|-----------|---------|
| chitosan | 28 | 32 | 23 |
| mussel-foot-adhesion | 12 | 15 | 8 |
| polydopamine-coating | 15 | 18 | 12 |
| plant-tannin | 5 | 6 | 5 |

Overlap DOIs indicate mechanisms that share references with performance data having quotes. These are the highest-priority upgrade targets.

## Actual Uplift Results

### Batch 1: 31 mechanisms (4 prototypes, D4 keyword matching)
| Prototype | Upgraded | Total | from_source |
|-----------|----------|-------|-------------|
| chitosan | 22 | 110 | 23 |
| mussel-foot-adhesion | 8 | 55 | 9 |
| polydopamine-coating | 1 | 35 | 2 |
| silk-fibroin | 0 | 17 | 2 |

### Batch 2: 10 mechanisms (8 prototypes, brief-visible priority)
| Prototype | Upgraded | Mechanism |
|-----------|----------|-----------|
| bone-structure | 2 | HAp heavy metal mechanisms |
| chitosan | 2 | CS/GO π-π, chemical adsorption |
| diatom-frustule | 1 | thermal treatment Si-OH |
| fish-scale-hydroxyapatite | 1 | eight-fold synergy |
| lobster-exoskeleton | 1 | chitosan beads mechanisms |
| oyster-shell | 1 | oyster shell modification |
| sulfate-reducing-bacteria | 1 | SRB enzymatic mechanism |
| silk-fibroin | 1 | MO electrostatic adsorption |

### Batch 3: 1 mechanism (all-items matching)
| Prototype | Upgraded | Mechanism |
|-----------|----------|-----------|
| shark-skin (separation) | 1 | surface wettability on bacterial adhesion |

### Overall Stats
- **Total mechanisms with causal_chain**: 510
- **from_source**: 59 (12%)
- **llm_inferred**: 451 (88%)
- **Prototypes with at least 1 from_source mechanism**: 12

### Remaining Gap
451 mechanisms remain llm_inferred because:
1. Extraction D4 items use different terminology than mechanism names
2. Some prototypes have empty causal_chain sub-fields (placeholder mechanisms from P5-B)
3. Some mechanisms are characterization/preparation methods without matching extraction items
4. Need deeper PDF reading with semantic matching (not just keyword overlap)

### Evidence Quality by Domain
- **Heavy metals (Pb, Cu, Cr)**: Strongest — chitosan, mussel, PDA, fish-scale have perf quotes
- **Dye (MB)**: Good — silk-fibroin, chlorella-cell-wall, chitosan have data
- **Organic micropollutants (BPA, SMX, PFOA)**: Weak — mostly inference, limited direct evidence
- **Oil-water separation**: Weak — no adsorption evidence, physical separation only

## Recommendation

1. Continue evidence uplift with semantic matching (not just keyword overlap) for remaining 451 mechanisms
2. Focus on brief-visible mechanisms first (24 still llm_inferred in ADRMATS briefs)
3. Use OpenClaw for deeper PDF extraction on high-impact targets
4. Consider lowering threshold or using embedding-based matching for better coverage

## Validation Results

| Validator | Result |
|-----------|--------|
| validate_consistency | ✅ 0 errors, 171 warnings (pre-existing) |
| check_chimera --strict | ✅ 0 violations |
| check_causal_chain | ✅ 510/510 qualified, 0 empty-basis |
| check_boundary_guardrail | ✅ PASS |
| check_gold_set_usefulness | ✅ 7/7 briefs pass |
| check_no_inferred_hard_do_not | ✅ PASS |
| check_dt_actionability_36 | ✅ PASS |
| check_fact_requires_locator | ✅ PASS |
| check_brief_do_not_behavior | ✅ PASS |
| check_source_tier_consistency | ✅ PASS |
| check_brief_ledger_consistency | ✅ PASS |
