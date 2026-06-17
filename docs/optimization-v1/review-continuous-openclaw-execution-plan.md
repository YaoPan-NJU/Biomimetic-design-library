# Full Evidence Audit Continuous Execution Plan

> **For agentic workers:** Execute tasks through OpenClaw with `mimo-v2.5` only. Track every task with the status fields in this document.

**Goal:** Complete the 24-active-prototype evidence audit while OpenClaw performs more than 99% of row-level work and Codex performs only dispatch, risk decisions, acceptance gates, and GitHub checkpoints.

**Architecture:** OpenClaw works in isolated task worktrees and produces a machine-readable report plus a commit. Codex never performs bulk PDF extraction or row-by-row editing; it accepts or rejects whole batches using deterministic checks and only spot-checks high-risk claims. Accepted task commits are integrated into `review` and pushed at meaningful checkpoints.

**Tech Stack:** Git worktrees, OpenClaw, `xiaomi/mimo-v2.5`, local PDF/extraction corpus, Python validation scripts.

---

## Non-Negotiable Role Budget

- OpenClaw: more than 99% of PDF reading, OCR, path matching, row comparison, JSON editing, report generation, and test execution.
- Codex: less than 1%, limited to task design, acceptance criteria, automated-result review, high-risk spot checks, disputes, and checkpoint approval.
- Codex must not manually audit large tables or repair rows one by one.
- Workers must use `xiaomi/mimo-v2.5`; `mimo-v2.5-pro` is forbidden.
- Maximum concurrency: two workers, each in a separate worktree and non-overlapping file scope.
- Never run `tools/build_prototypes_db.py` during the audit.

## Evidence Contract

Every row claimed as evidence-grounded must include:

- existing local PDF path or explicit `missing_pdf`;
- page plus section/table/figure/patent paragraph locator;
- short verbatim quote supporting the exact claim;
- valid verification vocabulary defined by the current validators;
- metric type and conditions for performance values;
- scope caveat and boundary/DO-NOT candidate where applicable.

Review-table summaries cannot be treated as primary experimental evidence. Missing, OCR-uncertain, inferred, or scope-ambiguous evidence remains a knowledge gap.

## Acceptance Gates

Every OpenClaw task must produce:

1. one focused Git commit in its worker branch;
2. one report under `docs/optimization-v1/` with `status: ready_for_codex_acceptance`;
3. changed-file list and row counts;
4. exact validation commands and exit codes;
5. unresolved items and recommended disposition;
6. confirmation that `tools/build_prototypes_db.py` was not run.

Codex accepts a batch only when:

- `git diff --check` passes;
- all JSON parses;
- no unrelated file is changed;
- no evidence status is upgraded without the required quote and locator;
- all high-risk changes are explicitly listed;
- relevant validators pass, or every remaining failure is documented as pre-existing or intentionally deferred.

## Execution Queue

### R01: Recover Lost Structured Fields

Status: dispatched

Worker branch/worktree: `openclaw/recovery-r01` / `/private/tmp/biomimetic-openclaw-r01`

- [ ] Compare `30481e4` with current `review` without reverting whole files.
- [ ] Restore 25 lost `design_translation` entries by prototype id.
- [ ] Restore 27 lost mechanism `causal_chain` cards by stable identity, not array index.
- [ ] Preserve every valid office cleanup and newly added row.
- [ ] Report unmatched or ambiguous cards instead of guessing.
- [ ] Run JSON parse, causal-chain, boundary, translation, consistency, chimera, ADRMATS, and hygiene checks.
- [ ] Commit only the recovery changes and report.

### R02: Repair Validation Vocabulary And Reporting

Status: blocked_by_R01

- [ ] Replace unsupported verification values only after deriving the canonical vocabulary from validator code.
- [ ] Correct delivery-summary counts from live JSON, including quote and locator counts separately.
- [ ] Fix the `CLAUDE.md` repo-hygiene allowlist conflict with a focused regression test.
- [ ] Re-run all validators without invoking the build script.

### A01-A04: Active Prototype Full Evidence Audit

Status: blocked_by_R02

OpenClaw splits the 24 active prototypes into four non-overlapping batches of six. Each worker audits all mechanisms, performance rows, and engineering constraints against local PDFs/extractions and writes only evidence-supported changes.

- [ ] A01: first six prototypes in sorted id order.
- [ ] A02: next six prototypes.
- [ ] A03: next six prototypes.
- [ ] A04: final six prototypes.

Each batch must report row totals as `supported`, `partial`, `missing_pdf`, `wrong_source`, `duplicate`, `inferred_only`, or `needs_human_decision`. It must also propose causal cards, design translations, and evidence-graded boundary/DO-NOT items.

### M01: Materials, Enrichment, Separation And Parked Audit

Status: blocked_by_A01_A04

- [ ] Audit non-active JSON directories separately so their semantics are not mixed with the 24 active prototypes.
- [ ] Resolve enrichment mirror gaps without mechanical copying.
- [ ] Separate review-table leads from primary-source evidence.
- [ ] Ensure parked and separation registries cannot contaminate active ranking.

### F01: Final Acceptance And Delivery

Status: blocked_by_all_audits

- [ ] All JSON parses and repository diff checks pass.
- [ ] Consistency and chimera checks pass.
- [ ] Causal-chain, boundary, translation, ADRMATS, and hygiene checks pass.
- [ ] Decision queue has no silent approvals; unresolved items are explicitly deferred or presented to Yao.
- [ ] Final report states exact evidence coverage, remaining knowledge gaps, and DO-NOT applicability boundaries.
- [ ] Push final checkpoint to `origin/review` and mark merge readiness.

## GitHub Checkpoint Policy

- Push after each accepted recovery/repair task.
- During full audit, push after each accepted six-prototype batch.
- Never push raw worker output before Codex acceptance.
- Preserve unrelated local changes, especially `tools/litextract` and existing untracked artifacts.

