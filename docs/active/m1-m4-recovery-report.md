---
status: challenged/not_passed
milestone: M1+M2+M3-partial+M4
date: 2026-06-19
owner: claude-code (coordinator)
---

# Recovery M1–M4 Report

Autonomous recovery under the M1→M2→M3-partial→M4 goal. All work committed locally;
**not pushed**. Canon recovered field-by-field with a 1,204-entry ledger; no whole-file
replacement, no refuted-row resurrection, no history rewrite.

## Commits this goal (review, ahead of origin by 12)

| SHA | milestone | summary |
|---|---|---|
| `d194a19` | M1 | canon safety net: regression tests, count-guard, stable-identity + ambiguity, ledger writer, staging-only build |
| `bddedfc` | M2-a | restore evidence stripped by `82fa2c0` (additive): +254 perf quotes, +257 mech quotes, 24 causal chains, 25 translations, 57 boundaries |
| `4961fad` | M2-b | rollback unsafe `13dfdbf` upgrades: 239 mechanisms partial→needs_review (6 accepted mussel-v3 preserved) |
| `b1e0385` | M2-c | diatom-frustule dedup (F09): 42→29 perf, 15→13 mech, 16→13 constraints |
| `8c17751` | M3 | library_tier + lifecycle_status on all 36; 12 prototype_metadata gaps filled (honest stubs); validate_consistency errors 12→1 |
| `fbc9bdd` | M2-d | gated verification recompute: 9 mechanisms needs_review→partial (quote+locator present); perf rows stay needs_review (genuine PDF gaps) |

## Final coverage (root canon, recomputed from committed JSON)

| metric | value | note |
|---|---|---|
| prototypes | 36 (core 24+2 deprecated, extended 9, exploratory 1) | lifecycle: 33 active, 2 deprecated, 1 parked |
| performance_data | 418 rows; **384 graded (91%)**; 326 with quote (77%) | strong |
| mechanisms | 771; graded 35 (4%); with quote 266 (34%) | honest post-rollback (inflation removed) |
| recovery ledger | 1,204 entries (v1 migration, all PENDING) | archived to v1-migration file; active ledger contains only R1+ entries |

The mechanism coverage is deliberately low: the `13dfdbf` keyword-upgrade had
inflated it to 48%; the rollback returns the unsupported rows to `needs_review`.
They now carry restored quotes/locators (34%) awaiting a second independent source
to reach `corroborated`.

## Acceptance runbook results

| check | result |
|---|---|
| validate_consistency | **1 error** (was 12 pre-recovery) — improvement |
| check_chimera --strict | 0 violations |
| check_causal_chain | 16 prototypes without qualified card (pre-existing; mostly expansion/separation + 3 empty shells) |
| check_boundary_guardrail | flags issues (pre-existing: boundary-rail logic) |
| check_translation_specificity | ✅ pass |
| verify_adrmats_delivery | **3 pass / 3 fail** (was 1/5 pre-recovery — improved) |
| check_repo_hygiene | 1 failure = baseline (CLAUDE.md root) |
| canon_metrics --guard | green (no protected-metric decreases) |
| canon-safety tests | 3/3 PASS |
| git diff --check | clean |

## Residual risks / what needs Yao

1. **verify_adrmats_delivery.py flags `partial` as invalid tier** (3 failures). `partial`
   is a legitimate grade per the design; the test is over-strict (pre-existing, R02 scope).
   Fixing the checker is a tool change (out of goal scope).
2. **16 prototypes without a qualified causal-chain card** — 3 empty shells
   (biomineralization-template, coral-skeleton, dna-aptamer, magnetic-bacteria) need
   source-backed card builds; the rest are separation/exploratory.
3. **Missing PDFs** (~50: chitosan 22, cell-membrane 3, mussel 3 patents, PDA CN114887602A,
   lobster 2023-Vo, coral). These rows stay `needs_review`/`missing_pdf` until you drop
   the literature — the local AI does not download.
4. **Root/subdir duplication** (5 separation + 4 materials_reference + namib) recorded
   in `docs/registries/prototype-duplication-record.md`; needs your collapse decision.
5. **2 PLAN DEDUP merges** (silkworm-silk→silk-fibroin, diatom-inspired-porous→diatom-frustule)
   — data-delete ops, pending your approval.
6. **Expansion to 60–80** — hard-blocked on a literature drop (your call).
7. **12 commits unpushed**; cloud baseline still `e4dc2d0`.

## Recommended next (M1.5 / M5, after authorization)

- Tool: relax `verify_adrmats_delivery.py` to accept `partial` (legitimate tier).
- Build qualified causal-chain cards for the 3 empty shells (needs PDFs).
- Acquire the ~50 missing PDFs; re-grade the needs_review rows.
- Resolve root/subdir duplication + 2 DEDUP merges (Yao decision).
- Then push on release approval.
