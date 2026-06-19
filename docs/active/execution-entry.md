---
status: active
owner: claude-code (coordinator)
date: 2026-06-19
---

# Execution Entry — current state & next action

> Live entry point. The static handoff prompt is `CLAUDE-CODE-TAKEOVER.md`; the
> architecture is `PROJECT-RECOVERY-DESIGN.md`. This file is the **current-state**
> companion: what is done, where things are, what to do next.

## Where we are

- **Branch:** `review` (Desktop worktree `/Users/panyao/Desktop/Biomimetic-design-library`).
- **HEAD:** `4987c0a` — Phase 0 documentation archive (local; **not pushed**).
- **Cloud baseline:** `origin/review@e4dc2d0` (3 local commits ahead: design, takeover, Phase 0).
- **Canon:** frozen & untouched. All five destructive commits remain in history —
  recovery is additive (no history rewrite).

## M0 — COMPLETE

- 176 docs archived (`docs/active/phase0-dispositions.json`, status `executed`).
- Live ledgers: `docs/registries/` (decision-queue, boundary-do-not-register, refuted-log).
- Standards: `docs/references/` (definitions, optimization-plan-v1, full-audit-plan, next-stage-approval-summary).
- Operational docs: `docs/active/` (this set).
- README/CLAUDE references fixed; `docs/README.md` index created.
- Verified: 0 broken links, `git diff --check` clean, hygiene = baseline (1 failure: CLAUDE.md).

## Next action — M1 (tool safety), awaiting authorization

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
