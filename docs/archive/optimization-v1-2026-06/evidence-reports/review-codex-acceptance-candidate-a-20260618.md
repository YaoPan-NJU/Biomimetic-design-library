---
status: accepted
date: 2026-06-18
baseline: 2242cc9
worker_final: 7efdbf2
---

# Candidate Audit A Acceptance

- Scope: 48 chitosan mechanisms and 7 diatom performance rows.
- Accepted data changes: diatom `performance_data[0..6]`, `missing_pdf` to `partial`, all with non-empty quote and page/section locator.
- Chitosan result: all 48 automatic matches rejected and restored to baseline `needs_review`; no chitosan JSON delta remains.
- Out-of-scope changes: 0.
- `verified` upgrades: 0.
- `git diff --check`: pass.
- JSON parse: 58/58 pass.
- Validators: no new failures versus `2242cc9`; pre-existing R12, pitcher-plant boundary, and repository-hygiene failures remain.
- `tools/build_prototypes_db.py` was not run.

Worker history `697d478` was rejected for scope expansion. Additive correction `f41dc5e` restored the required final state; `7efdbf2` completed report metadata.
