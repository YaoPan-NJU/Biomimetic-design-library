---
status: stale_superseded_by_execution_state
owner: claude-code (coordinator)
date: 2026-06-19
---

# Execution Entry — STALE, see execution-state.json

> **This document is superseded.** See `docs/active/execution-state.json` for current state.

## Current State (corrected 2026-06-19)

- **Branch:** `review` @ `382bb91` (20 commits ahead of origin)
- **R0:** PASSED (OpenClaw capability, both MIMO slots, multimodal OCR, 3-worker)
- **R1:** COMPLETED (build safety, ambiguity gate, ledger v2, diatom correction, validation)
- **G1:** PENDING independent review
- **M4:** NOT PASSED (external audit found tool failures, ledger PENDING, validators fail)

## Canonical Source

For current state, always read: `docs/active/execution-state.json`

M1 implements tooling (regression tests, count guards, stable-identity + ambiguity,
ledger writer, staging-only build). It is **not** started; it is the recommended hand-off.

Do **not** begin M1 without explicit authorization. In-goal constraints until then:
- no `git push`;
- no `prototypes_db/**` edit, no `feature-mapping.json` edit;
- no `tools/` modification (including `build_prototypes_db.py` and `check_repo_hygiene.py`);
- no evidence-status upgrade;
- no data delete / branch merge / history rewrite.

## Reading order for a new session

1. `docs/active/PROJECT-RECOVERY-DESIGN.md` — architecture (authoritative).
2. `docs/active/recovery-master-plan.md` — milestone plan.
3. `docs/active/commit-audit-root-cause.md` — what broke and why.
4. `docs/active/canon-recovery-spec.md` — field-level rules + ledger.
5. `docs/active/evidence-quality-standard.md` — grading + acceptance.
6. `docs/active/model-routing-protocol.md` — worker + model rules.
7. `docs/active/execution-roadmap.md` — M1–M5 + acceptance runbook.
8. `docs/registries/` — the ledgers that constrain canon writes.

## Standing guards (always)

- `python3 -X utf8` for all Python.
- `git status --short` must show no `prototypes_db/`, `feature-mapping.json`,
  `tools/litextract`, or `_w*_doi_map.json` staged (the first three are canon/Yao assets;
  the DOI maps are Yao's untracked work).
- Never push `origin/review` without explicit release approval.
