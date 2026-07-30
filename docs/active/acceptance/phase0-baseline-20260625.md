# Phase 0 — Baseline Report (2026-06-25)

## Sync Status

| Item | Value |
|------|-------|
| Stash ref | `stash@{0}: office-cc-phase0-20260625161722` |
| Pre-sync HEAD | `e4dc2d0` (expand prototypes 24→36) |
| Post-sync HEAD | `652ba0c` (V1-A evidence uplift final state) |
| Merge method | `--ff-only` (success, 226 commits fast-forwarded) |
| Dirty files stashed | 21 files (16 tracked + 5 untracked) |
| Untracked files extracted | `emerging-pollutants-20.json/.md/.xls` |

## from_source Stats (from snapshot_stats.py)

| Metric | Value |
|--------|-------|
| Active prototypes | 44 |
| Mechanisms total | 520 |
| Mechanisms grounded | 367 |
| Performance data | 502 |
| Empty pollutant | 101 (non-needs_review: 79) |
| from_source elements | 1239/2080 (59.6%) |
| Non-compliant | 0 |

## Validator Results (§2.5)

### Data Layer

| Validator | Result | Errors | Warnings |
|-----------|--------|--------|----------|
| validate_consistency.py | ✅ PASS | 0 | 172 |
| check_chimera.py | ✅ PASS | 0 | 0 |
| check_causal_chain.py | ✅ PASS | 467/520 qualified | 0 |
| check_boundary_guardrail.py | ❌ FAIL | 41 illegal basis + 111 from_source/locator | 0 |
| check_no_inferred_hard_do_not.py | ✅ PASS | 0 | 0 |
| check_fact_requires_locator.py | ✅ PASS | 0 | 0 |
| check_from_source_integrity.py | ✅ PASS | 1239/1239 compliant | 0 |
| check_source_tier_consistency.py | ✅ PASS | 0 | 0 |
| check_translation_specificity.py | ❌ ERROR | Script crash: `str.get()` on line 29 | — |
| check_dt_actionability_36.py | ❌ ERROR | Script crash: `KeyError: 0` on line 25 | — |

### Brief / ADRMATS Layer

| Validator | Result | Errors |
|-----------|--------|--------|
| generate_adrmats_briefs.py | (not re-ran, using existing briefs) | — |
| check_gold_set_usefulness.py | ✅ PASS | 7 briefs, 0 issues |
| check_brief_do_not_behavior.py | ✅ PASS | 0 |
| check_brief_ledger_consistency.py | ✅ PASS | 0 |
| check_brief_usefulness.py | ✅ PASS | 7 briefs, 0 issues |
| verify_adrmats_delivery.py | ❌ FAIL | PFOA: `verification_tier=knowledge_gap` invalid |
| check_brief_mechanism_binding.py | (not yet created) | — |

## Dogfood Scorecard (2026-06-21)

| Query | Candidates | Avg Score | BU | HLC |
|-------|-----------|-----------|-----|-----|
| BPA | 3 | 3.0/10 | 0 | 0 |
| PFOA | 3 | 3.0/10 | 0 | 0 |
| SMX | — | 3.0/10 | 0 | 0 |

**Key problem**: All organic-domain candidates have BU=0, HLC=0 at candidate level.

## Gold-Set Current State

- 7 briefs exist: Pb(II), Cr(VI), PFOA, SMX, BPA, 亚甲基蓝, 油水分离
- 21 organic new pollutants NOT yet in gold-set (Phase E pending)
- PFOA brief fails verify_adrmats_delivery.py (knowledge_gap tier)

## Pre-existing Errors (NOT introduced by this session)

1. **check_boundary_guardrail.py**: 41 illegal basis values (e.g., `literature_backed` in chitosan BC, `partial` in cell-membrane BC) + 111 from_source with missing/invalid locator
2. **check_translation_specificity.py**: Script bug — assumes `translation` is dict but some entries are strings
3. **check_dt_actionability_36.py**: Script bug — assumes `design_translation` is list but some entries are dicts
4. **verify_adrmats_delivery.py**: PFOA brief `verification_tier=knowledge_gap` not in allowed set

## Decision Queue (deferred items)

None yet — all baseline observations are pre-existing, no Yao decisions needed for Phase 0.

---

**Phase 0 DONE**: ✅ Local HEAD == origin/review (`652ba0c`), baseline numbers recorded.
