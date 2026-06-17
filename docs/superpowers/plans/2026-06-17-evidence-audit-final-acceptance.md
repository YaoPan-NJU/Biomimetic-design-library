# Evidence Audit Final Acceptance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete the full evidence audit, reconcile review records with the canonical JSON state, resolve remaining evidence gaps, and produce a review branch that is ready for Yao's final approval and merge into `adsorption/dev`.

**Architecture:** OpenClaw/mimo-v2.5 performs bulk PDF, OCR, path, and row-level evidence checks. Codex controls scope, independently spot-checks high-impact findings, curates decision and boundary records, runs deterministic validation, and creates GitHub checkpoints. Canonical JSON changes are allowed only for explicitly approved decisions and are always preceded by a dry run.

**Tech Stack:** Markdown audit records, JSON canon under `prototypes_db/`, Python validation tools, Git/GitHub, OpenClaw with `xiaomi/mimo-v2.5`.

---

### Task 1: Establish A Reconciled Baseline

**Files:**
- Modify: `docs/optimization-v1/review-full-audit-decision-queue.md`
- Modify: `docs/optimization-v1/review-boundary-do-not-register.md`
- Modify: `docs/optimization-v1/review-full-audit-worklog.md`
- Modify: `docs/optimization-v1/review-sync-summary.md`
- Create: `docs/optimization-v1/review-post-office-reconciliation.md`

- [ ] **Step 1: Validate every canonical JSON file without writing it**

Run:

```bash
python3 -X utf8 -m json.tool prototypes_db/<file>.json >/dev/null
```

Apply the same parse check to every tracked `prototypes_db/**/*.json`. Expected: zero parse failures.

- [ ] **Step 2: Run the existing non-destructive acceptance checks**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -X utf8 tools/validate_consistency.py
PYTHONDONTWRITEBYTECODE=1 python3 -X utf8 tools/check_chimera.py
PYTHONDONTWRITEBYTECODE=1 python3 -X utf8 tools/check_causal_chain.py
PYTHONDONTWRITEBYTECODE=1 python3 -X utf8 tools/check_boundary_guardrail.py
PYTHONDONTWRITEBYTECODE=1 python3 -X utf8 tools/check_translation_specificity.py
PYTHONDONTWRITEBYTECODE=1 python3 -X utf8 tools/check_repo_hygiene.py
```

Record actual output and inspect each script's scan scope. A green result is accepted only if the changed fields are in scope.

- [ ] **Step 3: Reconcile office changes against review records**

Compare commits `69bf698`, `2e181bf`, `8efea83`, and `ef5defe` with queue and boundary IDs. Mark an item applied only when its exact target/action exists in current JSON. Do not infer applied state from commit prose alone.

- [ ] **Step 4: Correct stale source-state records**

Resolve the known PDA `CN114887602A` contradiction, stale `pending_yao` boundary statuses, obsolete roadmap counts, and any queue item whose target row was removed or reindexed.

- [ ] **Step 5: Commit and push the documentation-only checkpoint**

Run:

```bash
git diff --check
git diff -- prototypes_db
git add docs/optimization-v1/review-post-office-reconciliation.md \
  docs/optimization-v1/review-full-audit-decision-queue.md \
  docs/optimization-v1/review-boundary-do-not-register.md \
  docs/optimization-v1/review-full-audit-worklog.md \
  docs/optimization-v1/review-sync-summary.md \
  docs/superpowers/plans/2026-06-17-evidence-audit-final-acceptance.md
git commit -m "docs: reconcile office audit changes"
git push origin review
```

Expected: only review documentation is committed; unrelated `tools/litextract` and local handoff files remain untouched.

### Task 2: Complete Remaining Bulk Evidence Audits

**Files:**
- Create: `docs/optimization-v1/review-full-audit-openclaw-batch-10-*.md` and later batch files
- Modify: `docs/optimization-v1/review-full-audit-decision-queue.md`
- Modify: `docs/optimization-v1/review-boundary-do-not-register.md`
- Modify: `docs/optimization-v1/review-full-audit-worklog.md`

- [ ] **Step 1: Generate one bounded OpenClaw task package**

Each task must name exact JSON fields, PDF/search scope, required quote/locator fields, and prohibited writes. Use `xiaomi/mimo-v2.5` only and no more than two concurrent workers.

- [ ] **Step 2: Require a decision-ready batch contract**

Every candidate must include `target_json`, `field_path`, a real local PDF path or explicit missing status, locator, verbatim quote or explicit impossibility reason, evidence label, and recommended action.

- [ ] **Step 3: Spot-check high-impact findings**

Codex checks every proposed wrong-source removal, hard boundary, top-ranking value, scanned-patent value, and unit/metric conversion against the source artifact.

- [ ] **Step 4: Accept, return, or park each candidate**

Queue only decision-ready items. Return unsupported items to OpenClaw with a precise correction request; classify unresolved source gaps as `knowledge_gap` or `needs_human_decision`.

- [ ] **Step 5: Commit and push each accepted batch**

Before every checkpoint run `git diff --check` and confirm no unapproved canonical JSON diff exists.

### Task 3: Present And Apply Minimal Yao Decisions

**Files:**
- Modify: `docs/optimization-v1/review-full-audit-decision-queue.md`
- Modify: approved `prototypes_db/**/*.json` files only
- Modify: `docs/optimization-v1/refuted-log.md` when rows are removed

- [ ] **Step 1: Collapse duplicate queue entries**

Group equivalent findings by action and target. Exclude already-applied, superseded, and accepted-no-change records.

- [ ] **Step 2: Present only material choices to Yao**

For each decision give a recommended option, alternatives, affected prototypes/rows, evidence grade, and ranking/design impact.

- [ ] **Step 3: Produce a dry-run for approved JSON edits**

The dry-run lists each file, field path, old value, new value, and approving decision ID. It must not write files.

- [ ] **Step 4: Apply only approved edits and validate them**

Do not run `tools/build_prototypes_db.py`. Re-run JSON parsing and all relevant checks after each bounded change set.

- [ ] **Step 5: Commit and push each approved package**

Use a commit message that names the approval package and update queue status in the same checkpoint.

### Task 4: Run Final Acceptance And Publish The Result

**Files:**
- Modify: `docs/optimization-v1/FINAL-report.md`
- Modify: `docs/optimization-v1/coverage-gaps.md`
- Modify: `docs/optimization-v1/literature-requests.md`
- Modify: `docs/optimization-v1/review-sync-summary.md`

- [ ] **Step 1: Recompute all final counts from canon**

Count prototypes, mechanisms, performance rows, verification levels, causal-chain card quality, boundary grades, source-path resolution, and unresolved knowledge gaps directly from current JSON.

- [ ] **Step 2: Run all acceptance commands and capture actual output**

Include JSON parse results, consistency, chimera, causal-chain, boundary guardrail, translation specificity, and repository hygiene checks. Explicitly document known scan limitations.

- [ ] **Step 3: Rewrite the final report from current data**

The report must distinguish verified evidence, soft/inferred boundaries, missing sources, placeholders, and excluded ranking rows. Do not reuse stale counts from the 2026-06-15 report.

- [ ] **Step 4: Verify repository scope and push the final review checkpoint**

Run:

```bash
git diff --check
git status --short
git log --oneline origin/adsorption/dev..review
git push origin review
```

- [ ] **Step 5: Deliver a merge-readiness decision**

State whether `review` is ready to merge into `adsorption/dev`, list any blocking decisions, and provide the exact compared commit IDs.
