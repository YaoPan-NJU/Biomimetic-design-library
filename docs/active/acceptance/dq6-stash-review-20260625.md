# DQ-6 Stash Review (2026-06-25)

## Stash: `stash@{0}: office-cc-phase0-20260625161722`
- Parent: `e4dc2d0` (pre-fast-forward HEAD)
- Current HEAD: `652ba0c` (post-fast-forward, 226 commits ahead of stash parent)

## Files in Stash (16 tracked + 5 untracked)

### Prototype DB (13 files)

| File | New Fields | Status | Action |
|------|-----------|--------|--------|
| cell-membrane-ion-channel.json | metric_type (14 rows) | **APPLIED** | +14 metric_type values |
| chlorella-cell-wall.json | evidence_type | Already in HEAD | SKIPPED |
| fish-scale-hydroxyapatite.json | scope_caveat | Already in HEAD | SKIPPED |
| materials_reference/cellulose-nanocrystal.json | scope_caveat | Already in HEAD | SKIPPED |
| materials_reference/starch-granule.json | — | Already in HEAD | SKIPPED |
| oyster-shell.json | scope_caveat | Already in HEAD | SKIPPED |
| pitcher-plant-slippery-surface.json | — | Already in HEAD | SKIPPED |
| plant-tannin.json | — | Already in HEAD | SKIPPED |
| polydopamine-coating.json | — | Already in HEAD | SKIPPED |
| scallop-shell.json | scope_caveat | Already in HEAD | SKIPPED |
| spider-silk.json | — | Already in HEAD | SKIPPED |
| superhydrophobic-artificial.json | — | Already in HEAD | SKIPPED |
| wood-xylem.json | applicability_note | **APPLIED** | +2 applicability_note values |

### Docs (3 files)

| File | Status | Action |
|------|--------|--------|
| phase5-chains.md | Stale (lists 0/773 qualified, current has 467/520) | SKIPPED |
| review-clcode-task23-validation.md | Stale (lists old validation results) | SKIPPED |
| review-v0.1-delivery-summary.md | Stale (lists old stats) | SKIPPED |

### Untracked Files (5 — already extracted in Phase 0)

| File | Status |
|------|--------|
| emerging-pollutants-20.json | Already extracted |
| emerging-pollutants-20.md | Already extracted |
| emerging-pollutants-20-source.xls | Already extracted |
| v0.2-acceptance-plan-officecc-20260625.md | Already in HEAD |
| review-clcode-task17-scope-caveats.md | New file, not yet in HEAD |

## Summary

- **Applied**: 2 files, 16 fields (metric_type + applicability_note)
- **Skipped (already in HEAD)**: 11 files — fast-forward merge already included the changes
- **Skipped (stale)**: 3 docs — outdated data, superseded by current HEAD
- **Stash preserved**: `stash@{0}` not popped or dropped

## Decision Queue

No new items. All stash changes either applied or skipped for clear reasons.
