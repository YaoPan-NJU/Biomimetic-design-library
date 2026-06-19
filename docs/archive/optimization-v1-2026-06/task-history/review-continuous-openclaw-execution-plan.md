# Full Evidence Audit Continuous Execution Plan

> **For agentic workers:** Use `mimo-v2.5-pro` for text-only work and `xiaomi/mimo-v2.5` for multimodal/OCR work. Track every task with the status fields in this document.

**Goal:** Complete the 24-active-prototype evidence audit while OpenClaw performs more than 99% of row-level work and Codex performs only dispatch, risk decisions, acceptance gates, and GitHub checkpoints.

**Architecture:** OpenClaw works in isolated task worktrees and produces a machine-readable report plus a commit. Codex never performs bulk PDF extraction or row-by-row editing; it accepts or rejects whole batches using deterministic checks and only spot-checks high-risk claims. Accepted task commits are integrated into `review` and pushed at meaningful checkpoints.

**Tech Stack:** Git worktrees, OpenClaw, `mimo-v2.5-pro` for text-only tasks, `xiaomi/mimo-v2.5` for multimodal/OCR tasks, local PDF/extraction corpus, Python validation scripts.

---

## Non-Negotiable Role Budget

- OpenClaw: more than 99% of PDF reading, OCR, path matching, row comparison, JSON editing, report generation, and test execution.
- Codex: less than 1%, limited to task design, acceptance criteria, automated-result review, high-risk spot checks, disputes, and checkpoint approval.
- Codex must not manually audit large tables or repair rows one by one.
- Text-only PDF extraction, path checks, JSON audits, and report work may use `mimo-v2.5-pro`.
- Any scanned PDF, page image, figure/table visual check, visual cache, or OCR task must use `xiaomi/mimo-v2.5`; using pro for multimodal work is expected to fail.
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

Status: completed

Worker branch/worktree: `openclaw/recovery-r01` / `/private/tmp/biomimetic-openclaw-r01`

- [x] Compare `30481e4` with current `review` without reverting whole files.
- [x] Restore 25 lost `design_translation` entries by prototype id.
- [x] Restore 27 lost mechanism `causal_chain` cards by stable identity, not array index.
- [x] Preserve every valid office cleanup and newly added row.
- [x] Report unmatched or ambiguous cards instead of guessing.
- [x] Run JSON parse, causal-chain, boundary, translation, consistency, chimera, ADRMATS, and hygiene checks.
- [x] Commit only the recovery changes and report.

Integrated commits: `cfdc0c1`, `79142b7`, `548061a`. All are ancestors of `review` at `2242cc9`.

### QW01: QoderWork Phase 0-4 Evidence Batches

Status: completed_pending_final_acceptance

Integrated checkpoints: `8ca0800` (Phase 0-2) and `2242cc9` (Batch 3-4 / Phase 3-4).

- [x] Preserve the pushed history; corrections must be additive commits.
- [x] Confirm both checkpoints are present on `review` and `origin/review`.
- [x] Recompute live JSON totals instead of trusting delivery-report summaries.
- [x] Record model provenance accurately: Phase 0-2 text-only work may use `mimo-v2.5-pro`, while multimodal/OCR evidence must come from `xiaomi/mimo-v2.5`.
- [ ] Resolve the final-acceptance failures listed under R02 before treating these batches as accepted.

Acceptance snapshot at `2242cc9`:

- 58 JSON files parse.
- Active performance rows: 406 total = 164 `verified`, 129 `partial`, 105 `needs_review`, 8 `missing_pdf`.
- 72 of the 164 `verified` performance rows lack either a quote or locator; the 164 upgrades remain unapproved by Yao.
- Active mechanisms: 530 total = 15 `verified`, 13 `partial`, 401 `needs_review`, 101 `unverified`.
- `git diff --check` fails for both pushed checkpoints because of trailing whitespace.
- Consistency has 1 R12 error; boundary validation lacks one active prototype; ADRMATS rejects `partial`; repository hygiene rejects root `CLAUDE.md` despite its regression test expecting it to be allowed.

### R02: Repair Validation Vocabulary And Reporting

Status: ready_for_openclaw_dispatch

- [ ] Derive and document one canonical verification vocabulary across stored JSON, `BiomimeticContext`, ADRMATS validation, boundary validation, and reports; resolve the current `partial` incompatibility without silently upgrading evidence.
- [ ] Re-audit the 164 unapproved performance `verified` values. Retain `verified` only with explicit Yao approval; otherwise downgrade to the strongest evidence-contract-compliant non-verified value.
- [ ] Correct delivery-summary counts from live JSON, reporting status, quote, locator, and quote-plus-locator counts separately.
- [ ] Correct report provenance so text-only pro runs and multimodal non-pro runs are distinguished; do not rewrite pushed history.
- [ ] Remove trailing whitespace introduced by `8ca0800` and `2242cc9`, then require `git diff --check` for every later batch.
- [ ] Fix the `CLAUDE.md` repository-hygiene allowlist conflict and make `tools/test_repo_hygiene.py` pass.
- [ ] Resolve or explicitly baseline the R12 bone-structure error, pitcher-plant boundary gap, and ADRMATS verification-tier failure.
- [ ] Re-run all validators without invoking the build script.

### N01-N04: Next OpenClaw Queue From Remaining Gaps

Status: prepared

Use `mimo-v2.5-pro` for text-only workers and `xiaomi/mimo-v2.5` for multimodal/OCR workers, at most two concurrently, in isolated worktrees.

- [ ] N01: Audit the isolated 91 auto-matched candidates: 48 chitosan mechanisms, 36 mussel mechanisms, and 7 diatom performance rows. Require real PDF paths, page plus section/table/figure/patent-paragraph locators, and exact short quotes; revert weak matches.
- [ ] N02: Resolve locally actionable missing-source items first: the seven diatom rows against the existing `2021-杜-硅藻-硅藻土-吸附-重金属 2.pdf` variant, then verify whether the reported PDA and oyster-shell path gaps are stale.
- [ ] N03: Produce an acquisition-only queue for genuinely absent sources: chitosan 70 rows, cell-membrane 14 rows, mussel patent rows, mycelium, pitcher-plant, lobster, and any residual oyster/PDA rows. Do not upgrade from review summaries or keyword matches.
- [ ] N04: Execute R02 deterministic vocabulary, statistics, hygiene, and validator repairs as a separate focused batch; keep evidence-row decisions out of that commit.

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
