---
status: active
owner: claude-code (coordinator)
date: 2026-06-19
derived_from: PROJECT-RECOVERY-DESIGN.md
---

# Recovery Master Plan

The master plan for restoring a trustworthy `review` baseline and expanding the
catalogue under the same evidence gates. This is the operational sibling of
`PROJECT-RECOVERY-DESIGN.md` (the architecture). Read both; when they conflict on
process detail, the design is authoritative.

## 0. Current position (2026-06-19, after Phase 0)

- Cloud baseline: `origin/review@e4dc2d0` (cloud; not pushed since).
- Local: `review@4987c0a` (Phase 0 docs archive committed; **ahead of origin by 3**:
  recovery design, takeover guide, Phase 0 archive).
- Canon: untouched. `prototypes_db/*.json` (36 root + separation/materials_reference/parked)
  and `feature-mapping.json` carry all five destructive commits in their history.
- Phase 0: **complete**. 176 docs archived, live ledgers in `docs/registries/`,
  standards in `docs/references/`, operational docs in `docs/active/`.
- Open problem: `feature-mapping.json → prototype_metadata` lacks **12** entries
  (see `commit-audit-root-cause.md §5`). Repair is an M3 canon task, not Phase 0.

## 1. The two milestones (from design §4)

**Milestone 1 — v1 deliverable.** Every ADRMATS-visible recommendation, ranking value,
causal explanation, and hard DO-NOT is evidence-safe; unresolved rows are explicitly
downgraded and excluded from ranking.

**Milestone 2 — full audit.** Every performance row, mechanism, boundary, source gap,
and exploratory prototype has one of four dispositions: accepted (with source evidence),
soft background, parked knowledge gap, or removed/refuted.

Prototype count is a catalogue goal (60–80), not an acceptance metric.

## 2. Milestones of the recovery programme

| Milestone | Scope | Gate |
|---|---|---|
| **M0 Docs** ✅ | Phase 0 archive + this operational doc set | `check_repo_hygiene` ≤ baseline; no broken links |
| **M1 Tool safety** | Failing regression tests reproducing destructive build; staging-only build; stable-identity + ambiguity + ledger tooling | regression tests red-on-damage; build writes staging only |
| **M2 Canon recovery** | Core 24 field-by-field restore; rollback `13dfdbf` 228-mechanism auto-upgrades; restore lost quotes/locators/translations/causal/boundaries; diatom dedup | `validate_consistency` 0 errors; chimera 0; count guards green |
| **M3 Expansion & tiering** | Integrate 12 new root prototypes with `library_tier` + `lifecycle_status`; fix the 12 `prototype_metadata` gaps; expand toward 60–80 | promotion-gate checks pass; mapping complete |
| **M4 v1 acceptance** | ADRMATS results restricted to Core; every ranked value source-backed; hard DO-NOT evidence-backed | `verify_adrmats_delivery` 6/6; ranking-honesty tests pass |
| **M5 Full audit** | Disposition every residual row | no unresolved row can reach ADRMATS output |

## 3. Ordering rules

- Field-level, never file-level. Stable identities + ledger; never reconstruct a
  whole JSON, never match by array index, never let empty overwrite non-empty.
- Separate concerns per commit: recovery, evidence upgrades, schema changes,
  documentation moves — each independently revertible.
- Evidence precedence (design §6.3): accepted direct PDF/visual quote → accepted
  review → accepted OpenClaw candidate → unreviewed extraction → inferred/empty.
- Each canon checkpoint carries before/after metrics + the ledger subset it applies.

## 4. What M0 did NOT do (residual scope)

- No canon edit, no feature-mapping edit, no tool change.
- `docs/imported/library-enhancement/**` kept in place (runtime assets).
- `docs/archive/**` pre-existing files kept (no churn).
- The 7 operational docs (this set) are M0's final deliverable.

## 5. Hand-off to M1

M1 (tool safety) is the next milestone and **requires implementing tooling** — which
exceeds this goal's charter (no tool fixes in-goal). The recommended M1 task list is in
`execution-roadmap.md §M1`. Do not begin M1 work without explicit authorization.
