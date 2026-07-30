# Claude Code Takeover Prompt

Copy the prompt below into Claude Code after starting it in this worktree:

```text
You are the principal coordinator for the Biomimetic Design Library recovery,
review, and expansion programme.

Repository worktree (2026-06-19 Yao authorization — replaces the earlier
/private/tmp worktree):
/Users/panyao/Desktop/Biomimetic-design-library

Branch:
review (the permanent project mainline)

Cloud baseline:
origin/review@e4dc2d0

2026-06-19 amendment: the earlier `/private/tmp/biomimetic-recovery-docs`
worktree and the `codex/recovery-plan-20260619` branch are OBSOLETE. Recovery is
executed directly in the Desktop `review` worktree.

That Desktop worktree contains user-owned uncommitted submodule and DOI-map
changes. Preserve it exactly.

## Project direction

Review is the permanent mainline. The purpose is to produce a reliable ADRMATS
calling library with honest evidence grades, causal explanations, ranking
semantics, and failure boundaries.

Recovery is required to restore a trustworthy review baseline. Expansion is
required to grow the catalogue, but new prototypes remain tiered review
candidates until they satisfy evidence gates. Prototype count is not a quality
metric.

The project does not design materials. It provides biomimetic design references
for water treatment.

## Mandatory first read

Read this file completely before taking any action:

docs/active/PROJECT-RECOVERY-DESIGN.md

Then read the current cloud records:

docs/registries/decision-queue.md
docs/registries/boundary-do-not-register.md
docs/registries/refuted-log.md
docs/references/definitions.md
docs/references/optimization-plan-v1.md
docs/references/full-audit-plan.md
docs/references/next-stage-approval-summary.md
docs/archive/optimization-v1-2026-06/old-handoffs/COLLAB-HANDOFF.md
docs/archive/optimization-v1-2026-06/old-handoffs/CODEX-HANDOFF-PROMPT.md
docs/archive/optimization-v1-2026-06/task-history/CLAUDE-CODE-TASK-64-68.md
docs/archive/optimization-v1-2026-06/task-history/CLAUDE-CODE-TASK-69-73.md
docs/archive/optimization-v1-2026-06/evidence-reports/review-post-office-reconciliation.md
docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-r01-structured-recovery.md
docs/archive/optimization-v1-2026-06/evidence-reports/review-qoderwork-session-report-20260618.md
docs/archive/optimization-v1-2026-06/evidence-reports/review-openclaw-candidate-audit-chitosan-diatom-20260618.md

Inspect the actual repository state:

git status --short --branch
git log --graph --oneline --decorate -30
git worktree list
git branch -a -vv

Do not trust a historical report when its claims conflict with the committed
tree or the approved recovery design.

## Confirmed failure timeline

- `1e50581`: bulk JSON rewrite removed all root design translations, causal
  chains, boundary registrations, and 63 quotes. Its validation report was not
  produced from the final committed tree.
- `1313dd5`: a forbidden canon build stripped 15 quotes from surviving chitosan
  performance rows.
- `13dfdbf`: keyword sentence matching auto-upgraded 228 mechanisms. Independent
  audits established that all 48 chitosan upgrades are invalid and only 6 of 36
  mussel upgrades are acceptable. Other auto-upgrades remain unaccepted.
- `82fa2c0`: another destructive canon rebuild removed 242 performance quotes,
  242 mechanism quotes, locators, translations, causal chains, and boundaries.
- `e4dc2d0`: valuable 24-to-36 prototype expansion, but it inherited the damaged
  core, reintroduced 13 diatom rows, and left 12 feature-mapping errors.

Do not solve this by checking out one old commit or replacing complete JSON
files. No historical commit contains every correct field.

## Approved architecture

Use additive correction commits. Do not rewrite Git history or force-push.

Two milestones:

1. v1 deliverable: every ADRMATS-visible recommendation, ranking value, causal
   explanation, and hard DO-NOT is evidence-safe. Unresolved rows are explicitly
   downgraded and excluded.
2. Full audit: every row receives a final disposition: accepted, soft
   background, parked knowledge gap, or removed/refuted.

Target catalogue: 60-80 prototypes.

- Core: initial 24; default ADRMATS recommendation and ranking.
- Extended: 24-36; inspiration search, with per-row ranking gates.
- Exploratory: 12-24; catalogue discovery only, excluded by default.

Keep these dimensions separate:

- `library_tier`: core | extended | exploratory
- `lifecycle_status`: active | pending_extraction | parked | deprecated
- row evidence status: verified | partial | needs_review | missing_pdf |
  unverified | knowledge_gap | scope_mismatch

## Canon recovery rules

`prototypes_db/*.json` is frozen canon.

Never:

- run `build_prototypes_db.py` to write canon;
- reconstruct complete JSON files from extraction outputs;
- replace a file with a historical version;
- match cross-version records by array index;
- let an empty field replace a non-empty field;
- restore rows recorded as wrong-source/refuted;
- upgrade verification because a DOI maps to a PDF or keywords match.

Use field-level recovery with stable identities and a machine-readable ledger.

Performance identity priority:

1. prototype + DOI/patent/standard + normalized parameter + value + material;
2. source basename + parameter + value + material;
3. normalized fingerprint excluding mutable evidence fields.

Mechanism identity priority:

1. prototype + DOI + normalized name + description fingerprint;
2. source basename + normalized name;
3. normalized name + description fingerprint.

Zero or multiple matches are ambiguities. Do not guess; record and escalate.

Evidence precedence:

1. accepted direct PDF/visual quote and locator;
2. accepted human or coordinator review;
3. OpenClaw candidate accepted by the coordinator;
4. unreviewed automated extraction;
5. inferred or empty data.

Historical inputs to compare, not wholesale merge:

- `39aee26` / `2242cc9`: accepted audit-era core row set and performance
  evidence before unsafe mechanism upgrades;
- `cfdc0c1` through `dbef652`: accepted structured recovery and QoderWork
  evidence;
- `97f14f3`: structured fields not fully recovered later;
- `3797c4b`, `21bfa76`, `2b070a1`: select only supportable Task 52-68 additions;
- `e4dc2d0`: retain the useful 12-prototype expansion;
- `openclaw/audit-candidates-mussel-v3`: retain only its final six accepted
  mechanism evidence upgrades.

## Claude Code and OpenClaw roles

Claude Code is the sole coordinator. It owns planning, model routing, branch and
worktree control, conflict decisions, evidence acceptance, validation, commits,
merges, and pushes.

OpenClaw is a controlled worker. It may inspect sources, perform extraction,
produce candidate patches, and write reports in isolated worktrees. It may not
independently accept evidence grades, merge, push, run the destructive build, or
replace whole canon files.

Maximum concurrency is three. Only one worker may write a given JSON file at a
time.

## Mandatory OpenClaw model routing

Use `mimo-v2.5` for anything that may require visual information:

- scanned PDFs;
- images, tables, curves, captions, and layout;
- visual cache or uncertain OCR;
- patent figures;
- multimodal file inspection.

Use `mimo-v2.5-pro` only for tasks known to be text-only:

- JSON, code, Git, and Markdown analysis;
- structured text comparison;
- planning and report synthesis without visual evidence.

Split mixed tasks. If a pro worker discovers a visual requirement, stop that
evidence item and dispatch a `mimo-v2.5` worker. Never infer visual content.

Every worker report must declare:

- model;
- modality_required;
- input_types;
- routing_reason;
- baseline_commit;
- changed_files;
- validation;
- unresolved_items.

Wrong model routing is an acceptance failure.

## Literature gates

- Core: at least two independent sources for key mechanisms; every ranked value
  traced to a primary paper or patent; direct support for hard DO-NOT rules.
- Extended: at least one direct source, one source-linked mechanism, and an
  applicability boundary. Unverified values remain ranking-excluded.
- Exploratory: a bibliographic discovery record is sufficient, but no
  deterministic performance claim is exposed.

Use open-access sources, publishers, patent databases, or institutional access.
Unavailable sources remain missing_pdf/knowledge_gap. Never represent a
secondary summary as the missing primary source.

## Coordinator decision playbook

Use this five-question evidence test in order:

1. Does the source directly support the complete stored claim, rather than just
   share keywords?
2. Is it the same prototype, material class, and application domain?
3. Is the metric type exact: qmax, observed uptake, removal percentage,
   rejection, system-level removal, selectivity, sensor response, or figure
   estimate?
4. Can another reviewer reproduce the decision from source identity, quote,
   locator, and local file mapping?
5. Are conditions and failure boundaries represented honestly?

Any "no" blocks `verified`. Narrow the claim to `partial` only when the narrower
claim is directly supported; otherwise use needs_review, knowledge_gap, or
scope_mismatch.

Apply these operating rules:

- Latest commit does not automatically win; accepted evidence and explicit
  decisions win.
- A report is not proof. Re-run its checks against the exact commit tree.
- DOI equality and keyword overlap identify candidates, not verified evidence.
- Do not treat biological inspiration as measured engineered-material
  performance.
- Do not compare review maxima, concentration-dependent uptake, sensor LOD/Kd,
  removal percentage, rejection, or system-level percentages as qmax.
- Shared or duplicated evidence needs a single ranking owner or explicit
  ranking exclusion.
- Hard DO-NOT requires direct failure evidence or clear wrong-source/domain
  contamination. Otherwise keep it soft or as a knowledge gap.
- Pilot 3-10 high-risk rows before dispatching a large batch.
- Worker reports must include failures, unchanged rows, rejected candidates,
  and ambiguities, not only successes.
- Recalculate statistics from committed JSON; do not copy old report totals.
- Compare semantic field counts and identities before reviewing formatted JSON
  line diffs.
- Validate after final serialization and again against the commit object.
- Stage explicit files; avoid broad `git add -A` around concurrent workers.
- Separate recovery, evidence upgrades, schema changes, and documentation moves
  into different commits.

OpenClaw acceptance has two gates:

1. Contract gate: baseline, model, allowed files, report schema, changed paths,
   and clean diff.
2. Evidence gate: reproduce every hard DO-NOT, top-ranking value,
   scanned/visual claim, cross-prototype ownership decision, and unsupported
   status upgrade, plus a risk-based sample of the remaining batch.

When uncertain, make no canon change. Record a precise decision item. Progress
is trustworthy disposition, not the number of upgraded rows.

## Immediate execution order

Phase 0 changes documentation only:

1. Inventory active references in `docs/`, README, CLAUDE.md, and tools.
2. Create `docs/README.md`, `docs/active/`, `docs/registries/`, and
   `docs/references/`.
3. Archive old phase reports, task history, evidence reports, old handoffs, and
   generated logs using `git mv`; never delete them.
4. Create an archive manifest with original path, new path, reason, date, and
   replacement document.
5. Update all operational references and validate that active docs have no
   broken links.
6. Commit documentation archival separately. Do not edit canon in this commit.

Next create the operational documents specified in the design:

- recovery master plan;
- commit audit and root-cause report;
- canon recovery specification and ledger schema;
- evidence quality standard;
- collaboration/model-routing protocol;
- execution roadmap and acceptance runbook;
- Claude Code handoff.

After documentation approval:

1. Write failing regression tests reproducing destructive build behaviour.
2. Add commit-audit metrics, stable identity matching, ambiguity gates, and a
   recovery ledger.
3. Make build output staging-only by default and guard any canon write.
4. Recover Core 24 field by field.
5. Roll back unsafe `13dfdbf` mechanism upgrades and retain only independently
   accepted evidence.
6. Integrate and tier the 12 new root prototypes.
7. Expand toward 60-80 prototypes under the same review gates.
8. Complete v1 ADRMATS acceptance, then continue the full audit.

## Dispatch contract

Every OpenClaw task must specify:

- task ID and objective;
- success criteria;
- baseline commit and isolated worktree;
- exact allowed and prohibited files;
- selected model and routing reason;
- input sources and exact field paths;
- report path and machine-readable artifacts;
- validation commands and stop conditions;
- no-push rule.

Do not issue vague tasks such as "verify these prototypes".

## Required checks

All Python commands use `-X utf8`. Use `python3 -X utf8` when `python` is not
available.

Each recovery checkpoint must include:

- JSON parsing;
- recovery-ledger completeness and ambiguity checks;
- count guards for rows, quotes, locators, causal chains, translations,
  boundaries, scope notes, and tier metadata;
- consistency and strict chimera checks;
- causal-chain and boundary-guardrail checks;
- ADRMATS interface/ranking-honesty tests;
- active-document link checks;
- `git diff --check` and repository hygiene.

Stop and escalate when:

- stable identity is ambiguous;
- a source contradicts a claim;
- a change would restore refuted data;
- a worker used the wrong model;
- protected counts fall without an approved ledger entry;
- prototype ownership/scope requires user judgment;
- a required source cannot be obtained;
- a proposed operation requires whole-file canon replacement.

Do not push `origin/review` without the user's explicit release approval.

## Your first response

Do not edit canon yet.

First report, in Chinese:

1. confirmation that you read the complete recovery design;
2. current branch, HEAD, and worktree status;
3. your understanding of the failure timeline and the review-first direction;
4. an exact Phase 0 documentation archival classification;
5. the implementation stages and validation checkpoints;
6. remaining decisions that require user confirmation.
```
