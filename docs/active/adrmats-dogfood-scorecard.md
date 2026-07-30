# ADRMATS Dogfood Scorecard

**Date**: 2026-06-25 (re-scored after Phase 3 changes)
**Previous**: 2026-06-21 (all queries 3.0/10)
**Scoring**: 0-2 per dimension, max 10 per candidate

## Rubric
| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| candidate_quality | implausible | inference only | direct evidence |
| reason_validity | absent/vague | plausible | source-backed |
| DT actionability | absent | idea only | idea + material_handle |
| boundary_usefulness | absent | - | present |
| honesty_ledger | absent | inferences only | facts/leads present |

## Improvement Summary

| Query | 2026-06-21 | 2026-06-25 | Δ |
|-------|-----------|-----------|---|
| BPA | 3.0/10 | **6.0/10** | +3.0 |
| PFOA | 3.0/10 | **6.0/10** | +3.0 |
| SMX | 3.0/10 | **6.0/10** | +3.0 |
| Pb(II) | — | **6.8/10** | — |
| Cr(VI) | — | **6.6/10** | — |

**Key improvements**:
- BU: 0→1 (boundaries now surfaced in brief)
- HLC: 0→1 (honesty_summary now present per candidate)
- DTA: 1→2 (design_translation has material_handle)
- CQ: 1→2 for heavy-metal candidates (direct evidence)

## BPA (bpa_内分泌干扰物去除.json)

**Candidates**: 3, **Avg score**: 6.0/10

| Prototype | CQ | RV | DTA | BU | HLC | Total | Lane |
|-----------|----|----|-----|----|-----|-------|------|
| chitosan | 1 | 1 | 2 | 1 | 1 | 6 | exploratory |
| plant-tannin | 1 | 1 | 2 | 1 | 1 | 6 | exploratory |
| polydopamine-coating | 1 | 1 | 2 | 1 | 1 | 6 | exploratory |

All candidates correctly in exploratory lane (no direct BPA evidence).

## PFOA (pfoa_痕量吸附去除.json)

**Candidates**: 3, **Avg score**: 6.0/10

| Prototype | CQ | RV | DTA | BU | HLC | Total | Lane |
|-----------|----|----|-----|----|-----|-------|------|
| chitosan | 1 | 1 | 2 | 1 | 1 | 6 | exploratory |
| diatom-frustule | 1 | 1 | 2 | 1 | 1 | 6 | exploratory |
| polydopamine-coating | 1 | 1 | 2 | 1 | 1 | 6 | exploratory |

All candidates correctly in exploratory lane + "organic micropollutant evidence weak" caveat.

## SMX (smx_抗生素吸附去除.json)

**Candidates**: 3, **Avg score**: 6.0/10

| Prototype | CQ | RV | DTA | BU | HLC | Total | Lane |
|-----------|----|----|-----|----|-----|-------|------|
| plant-tannin | 1 | 1 | 2 | 1 | 1 | 6 | exploratory |
| chitosan | 1 | 1 | 2 | 1 | 1 | 6 | exploratory |
| polydopamine-coating | 1 | 1 | 2 | 1 | 1 | 6 | exploratory |

## Pb(II) (pb(ii)_重金属离子去除.json)

**Candidates**: 8, **Avg score**: 6.8/10

| Prototype | CQ | RV | DTA | BU | HLC | Total | Lane |
|-----------|----|----|-----|----|-----|-------|------|
| mussel-foot-adhesion | 2 | 1 | 2 | 1 | 1 | 7 | lead |
| fish-scale-hydroxyapatite | 2 | 1 | 2 | 1 | 1 | 7 | fact |
| oyster-shell | 2 | 1 | 2 | 1 | 1 | 7 | lead |
| diatom-frustule | 2 | 1 | 2 | 1 | 1 | 7 | lead |
| chitosan | 2 | 1 | 2 | 1 | 1 | 7 | lead |
| lobster-exoskeleton | 2 | 1 | 2 | 1 | 1 | 7 | lead |
| bone-structure | 1 | 1 | 2 | 1 | 1 | 6 | lead |
| sulfate-reducing-bacteria | 1 | 1 | 2 | 1 | 1 | 6 | inference |

Heavy-metal lane working: 1 fact + 5 leads + 1 inference.

## Cr(VI) (cr(vi)_六价铬去除.json)

**Candidates**: 5, **Avg score**: 6.6/10

| Prototype | CQ | RV | DTA | BU | HLC | Total | Lane |
|-----------|----|----|-----|----|-----|-------|------|
| chitosan | 2 | 1 | 2 | 1 | 1 | 7 | lead |
| iron-oxidizing-bacteria | 2 | 1 | 2 | 1 | 1 | 7 | lead |
| polydopamine-coating | 2 | 1 | 2 | 1 | 1 | 7 | lead |
| bone-structure | 1 | 1 | 2 | 1 | 1 | 6 | lead |
| oyster-shell | 1 | 1 | 2 | 1 | 1 | 6 | inference |
