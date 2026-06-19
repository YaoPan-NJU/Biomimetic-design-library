---
title: Recovery Execution V2 Design
status: proposed_for_yao_review
date: 2026-06-19
owner: codex-supervisor
baseline: review@63564fd
cloud_baseline: origin/review@e4dc2d0
authority: supersedes execution claims in SESSION-HANDOFF.md and m1-m4-recovery-report.md when they conflict with this design
scope: correction, evidence audit, external-input reconciliation, and expansion to 60-80 prototypes
---

# Recovery Execution V2 Design

## 1. Purpose

This design defines how the Biomimetic Design Library is corrected, reviewed, and
expanded without repeating the destructive rebuilds, unsupported evidence upgrades,
or single-agent self-acceptance failures already found in the repository.

The permanent project mainline remains `review`. The product objective is a reliable
ADRMATS calling library: every exposed recommendation, ranking value, causal
explanation, and hard DO-NOT must be evidence-safe. Prototype count is secondary to
that objective, although the reviewed catalogue should ultimately contain 60-80
explicitly tiered prototypes.

This design adds two requirements approved by Yao on 2026-06-19:

1. Claude Code runs long, low-interruption Goals and remains the continuous
   coordinator.
2. All PDF, patent, OCR, visual, and row-level evidence labour is OpenClaw-first.
   Claude Code does not perform bulk PDF review itself.

Codex and Yao intervene at defined gates, not during ordinary batch execution.

## 2. Current Truth and Safety Freeze

Current local state at design time:

- worktree: `/Users/panyao/Desktop/Biomimetic-design-library`;
- branch: `review@63564fd`, 13 local commits ahead of `origin/review@e4dc2d0`;
- no recovery commit has been pushed;
- user-owned `tools/litextract` changes and three untracked DOI maps must remain
  untouched;
- `docs/active/SESSION-HANDOFF.md` is committed but contains challenged completion
  claims and is not authoritative until corrected;
- M0 documentation work is broadly usable, but M1-M4 cannot be accepted as complete.

Confirmed blockers include:

- the default `build_prototypes_db.py` path crashes on `args.writeCanon`;
- the claimed post-build canon invariant guard is absent;
- existing tests do not execute the guarded build entry point;
- the 1,204-entry recovery ledger is not an auditable record: all entries have
  `applied_commit=PENDING`, many identities are weak or empty, array indexes dominate
  field paths, and quote/source fields and schema enums are inconsistent;
- the recovery applier does not enforce a multiple-match ambiguity stop;
- nine diatom mechanisms were promoted to `partial` without direct PDF acceptance;
- M4 validation did not pass: consistency, causal, boundary, and ADRMATS checks remain
  red;
- live execution documents still describe stale milestone states.

Therefore the next milestone is **R1 Correction**, not M5. No push, expansion, mass
verification, duplicate deletion, or canon promotion is allowed before Gate G1.

## 3. Operating Architecture

### 3.1 Control plane: Claude Code on MIMO

Claude Code is the continuous coordinator. It owns:

- the long Goal and durable execution state;
- task decomposition and OpenClaw dispatch;
- branch/worktree ownership and one-writer enforcement;
- deterministic tooling, tests, manifests, and candidate validation;
- acceptance-queue construction;
- applying already accepted field patches through a deterministic applier;
- local commits, checkpoint reports, and stop-gate escalation.

Claude Code may inspect JSON, code, Git, Markdown, manifests, and worker reports. It
must not bulk-read PDFs or decide hundreds of evidence rows inline. Unlimited API
quota does not justify unbounded context: context discipline is a quality control.

### 3.2 Work plane: OpenClaw-first

OpenClaw performs all evidence labour:

- born-digital PDF text inspection;
- scanned PDF and patent visual inspection;
- OCR, tables, figures, captions, curves, and page-layout interpretation;
- claim-to-source matching;
- source inventory and missing-source reconciliation;
- candidate evidence extraction;
- literature-supported causal-card and boundary candidates;
- candidate prototype evidence packs for expansion.

OpenClaw never:

- writes `prototypes_db/*.json` or `feature-mapping.json`;
- upgrades or accepts an evidence grade;
- edits the authoritative recovery ledger;
- merges, commits to `review`, pushes, or rewrites history;
- substitutes a secondary source for an unavailable primary source;
- infers content from a visual file without using the multimodal route.

### 3.3 Independent gates: Codex and Yao

Codex reviews high-risk engineering and evidence transitions. Yao resolves project
scope, ownership, deletion, external-source, and release decisions.

The coordinator may work continuously between gates. It must stop at a gate with a
short evidence-backed report, exact commit IDs, validation output, and unresolved
items.

## 4. Long-Goal Model

Long Goals are encouraged, but a Goal is a bounded programme rather than permission
to change anything until the repository is “finished.” Each Goal contains multiple
autonomous waves and durable checkpoints.

### 4.1 Goal duration and checkpoints

- A Goal may run for hours or multiple context windows.
- Checkpoint every completed batch or every 60-90 minutes, whichever comes first.
- Each checkpoint records current HEAD, changed files, worker tasks, accepted and
  rejected counts, validation status, and next batch.
- Create small local commits by concern; never use `git add -A`.
- At approximately 60% of the model context window, write durable state, finish the
  current atomic batch, and restart from that state instead of carrying the entire
  conversation.
- A context restart does not broaden authority or bypass a gate.

### 4.2 Durable state

Create one machine-readable live state file:

`docs/active/execution-state.json`

It records:

- baseline and current HEAD;
- active Goal ID and authorized milestones;
- current gate;
- completed and pending batch IDs;
- OpenClaw task IDs, models, sessions, and artifact paths;
- accepted/rejected/ambiguous counters;
- current validation results;
- external-input gap count;
- protected user assets;
- last checkpoint time.

Human-readable summaries are generated from this state. A stale handoff document may
not override it.

### 4.3 Mandatory stop gates

The Goal stops only when one of these occurs:

1. a Codex/Yao gate defined in Section 11 is reached;
2. stable identity has zero or multiple plausible matches;
3. source evidence contradicts the stored claim;
4. a change would resurrect refuted data or reduce a protected metric without an
   approved disposition;
5. prototype ownership, tier, deduplication, deletion, or external-source provenance
   needs Yao;
6. a worker used the wrong model/modality;
7. validation worsens, the same failure repeats three times, or a tool cannot prove
   its safety property;
8. push, force-push, history rewrite, branch-wide merge, or destructive cleanup would
   be required.

Routine missing sources do not stop the Goal. They are registered and excluded from
ADRMATS-visible outputs.

## 5. OpenClaw Dispatch Design

### 5.1 Runtime

Use the proven embedded path:

`openclaw agent --local ...`

The gateway path currently fails on a bundled plugin surface and is not used until
separately repaired. Create lean project-specific agents instead of reusing the
general `main` agent, whose trivial call carries roughly 23k prompt tokens.

Recommended agents:

- `bmdl-text`: `mimo-v2.5-pro`, pure text/code/JSON/PDF-text tasks;
- `bmdl-visual`: `mimo-v2.5`, scanned pages, figures, tables, captions, uncertain OCR;
- `bmdl-inventory`: `mimo-v2.5-pro`, filenames/DOIs/patent numbers/manifests only.

Maximum concurrency is three. Default allocation is two text workers and one visual
worker. Only one worker owns a candidate artifact path.

### 5.2 Routing

Use `mimo-v2.5` whenever a task may require visual information. Use
`mimo-v2.5-pro` only when the inputs are certainly text-only. If a text worker finds
visual dependence, it stops that item and emits a visual handoff; it does not guess.

### 5.3 Batch by source, not by row

One PDF or patent is inspected once and may resolve multiple rows across one or more
prototypes. A batch normally contains:

- one source and all linked rows; or
- one prototype and 5-20 rows sharing a small source set.

Avoid one API call per row. This reduces repeated system context, source parsing, and
inconsistent decisions.

### 5.4 Worker output

Each worker writes candidate-only artifacts under:

`docs/active/audit-candidates/<task-id>/`

Required files:

- `contract.json`: task ID, baseline, model, modality, allowed inputs and outputs;
- `candidates.jsonl`: one candidate disposition per row;
- `report.md`: concise human-readable summary;
- `unresolved.jsonl`: ambiguity, missing source, contradiction, or visual handoff;
- `run.json`: model, session, source hashes, timestamps, and validation.

Each candidate includes:

- prototype ID and target field kind;
- stable record identity, never only an array index;
- source identity and repository-relative source path;
- source SHA-256;
- exact quote and reproducible locator;
- claim and scope comparison;
- modality used;
- recommended disposition;
- explicit limitation;
- no canon-ready evidence grade unless the coordinator later accepts it.

## 6. R1 Correction Programme

R1 makes the recovery machinery trustworthy before any new evidence work.

### R1-A: Build safety

- reproduce the default `args.writeCanon` crash in an integration test;
- remove the invalid attribute access;
- make the build physically staging-only;
- do not retain a direct canon-write path in this script; any future promotion is a
  separate reviewed field-level operation;
- test that the canon tree hash is unchanged after a default build;
- test failure injection and staging-output validation;
- make staging validation inspect staging, not the current canon tree.

### R1-B: Identity and ambiguity

- ensure the real applier uses the same stable matcher tested by the library;
- reject zero and multiple matches;
- remove “first strongest candidate wins” behaviour;
- use deterministic identities containing source ID, normalized claim/metric, value,
  material/prototype ownership, and a fingerprint;
- array indexes may be recorded only as a transient location hint, never as identity.

### R1-C: Ledger v2

- validate every line against a corrected schema without optional external packages;
- replace `PENDING` with the actual applying commit or an explicit correction link;
- record actual quote, locator, local file, source hash, identity level, and decision;
- add correction semantics for legacy invalid entries without pretending the original
  entries were valid;
- prove one ledger disposition for every canon field change in R1 onward;
- report duplicate IDs, missing source, weak identity, enum error, and orphan change.

The existing 1,204 entries are treated as an untrusted v1 migration input, not as an
accepted audit trail.

### R1-D: M2 correction

- downgrade the nine unreviewed diatom `partial` promotions to `needs_review` through
  a corrective commit;
- reconcile 239 actual rollbacks against the 228 rows introduced by `13dfdbf` and
  explain the additional eleven;
- re-audit M2-a restored fields for ambiguity and refuted-source conflict;
- keep supportable additive fields, but do not expose their quotes as accepted evidence
  until M5;
- update all recovery reports with measured, not inherited, counts.

### R1-E: Strict validation and live state

- use `validate_consistency.py --strict`;
- fix tools that write reports into archived/obsolete directories during validation;
- distinguish “command executed” from “milestone accepted”;
- update `execution-entry.md`, `execution-roadmap.md`, `SESSION-HANDOFF.md`, and the M4
  report so they do not claim M4 passed;
- create `execution-state.json`.

R1 ends at Gate G1. No M5 candidate is applied before Codex reviews R1.

## 7. Cross-Device and External-Input Recovery Lane

### 7.1 Why this is separate

The literature library is ignored by Git. The current worktree contains 633 PDFs and
592 extraction JSON files, but Git cannot prove this is the complete office inventory.
Any office-only PDF or patent that was never committed cannot be reconstructed from the
remote repository.

Git history still contains useful office-side development and recoverable objects. The
repository also has multiple local candidate branches/worktrees and three stashes.
These are evidence inputs, not branches to merge wholesale.

### 7.2 Current provenance audit

Before M5 bulk execution, create read-only inventories for:

- all local and remote refs;
- all worktree HEADs;
- all stashes, inspected without popping into `review`;
- relevant reflog commits;
- known office commits and the archived post-office reconciliation;
- current 633-PDF literature tree;
- current extraction JSON tree;
- DOI and patent mappings.

For each branch/stash/commit, classify changes as:

- already integrated;
- valuable candidate not integrated;
- superseded;
- refuted/unsafe;
- ambiguous and requiring review.

No branch-wide merge is allowed. Accepted value is selected field-by-field or by
small reviewed commits.

### 7.3 External input gap register

Create:

`docs/registries/external-input-gaps.jsonl`

Each unavailable office asset records:

- gap ID;
- expected DOI, patent number, title, or filename if known;
- affected prototypes and row identities;
- last known device/location;
- evidence that the asset existed;
- current local search result;
- status: `office_unavailable`, `current_copy_found`, `recovered_from_git_object`,
  `received_pending_ingest`, `ingested`, or `not_recoverable`;
- ADRMATS impact and exclusion action.

An unavailable office asset is never silently treated as absent evidence or as a
refuted claim.

### 7.4 Literature manifest

Generate a repository-tracked manifest, not the PDFs themselves. For every current
PDF/patent record:

- repository-relative normalized path;
- size and SHA-256;
- DOI/patent number/title when derivable;
- text-extractable or visual-required classification;
- linked canon rows;
- ingestion source and date when known.

When the office files become available, generate the same manifest there and compare
by SHA-256 first, then DOI/patent/title. New files enter a quarantine/incoming area,
are scanned and deduplicated, and only then join the active library.

### 7.5 Progress while the office device is unavailable

R1 and M5 work backed by current local sources may continue. Rows that depend on
unknown office assets remain `external_source_pending` in the review registry and
`missing_pdf`/`knowledge_gap` in canon as appropriate. They are excluded from ranking,
causal explanation, hard DO-NOT, and deterministic recommendation.

The v1 ADRMATS milestone may pass with these rows excluded. The full-audit milestone
cannot mark them finally accepted or refuted until the external gap is resolved.

## 8. M5 Evidence Audit

### 8.1 Pilot

After Gate G1, OpenClaw runs a 9-item pilot covering:

- text mechanism claims;
- a quantitative performance claim;
- a scanned/visual patent item;
- a scope mismatch;
- an ambiguous identity;
- a known accepted control;
- a known refuted control.

Claude Code performs contract validation and a manual coordinator review of all pilot
items. Codex independently reviews the pilot at Gate G2. Bulk M5 begins only if the
false-accept and false-reject behaviour is acceptable and locators are reproducible.

### 8.2 Bulk audit

All currently resolvable rows are assigned to OpenClaw source-centred batches. Claude
Code does not divide the “easy remainder” among its own PDF-reading subagents.

Acceptance stages:

1. contract gate: correct model, baseline, inputs, hashes, paths, schema;
2. identity gate: exactly one stable target;
3. evidence gate: claim, prototype, material, metric, scope, quote, locator;
4. conflict gate: refuted and external-gap registries;
5. coordinator disposition: accept, narrow/partial, keep soft, missing, ambiguous,
   wrong-source, or reject;
6. deterministic apply with ledger v2;
7. strict validation against both working tree and commit object.

Every status upgrade, numeric ranking candidate, hard boundary, visual claim, and
cross-prototype ownership decision receives 100% coordinator review. Lower-risk
no-change/downgrade batches receive risk-based sampling.

## 9. ADRMATS v1 Acceptance

M4 is re-run only after R1 and enough M5 work to make Core outputs safe.

Required outcomes:

- `validate_consistency.py --strict`: zero errors;
- chimera strict: zero violations;
- every ADRMATS-visible Core recommendation has a qualified causal card;
- boundary guard passes; every hard rule has direct source support;
- ADRMATS delivery passes all tests;
- unresolved/external-pending rows are excluded;
- ranking uses only accepted, metric-compatible values;
- documentation and live state agree with committed data;
- no protected user asset is staged;
- Codex Gate G4 passes before any push request.

## 10. Expansion to 60-80 Prototypes

Expansion begins after Core v1 acceptance, while the full audit may continue in
parallel through separate candidate artifacts.

Target composition:

- Core: 24 high-quality default references;
- Extended: 24-36 source-backed inspiration prototypes;
- Exploratory: 12-24 discovery candidates excluded from default recommendation.

OpenClaw performs literature inventory, source packs, and candidate cards. Claude Code
enforces tier and promotion gates. External office-only sources may later strengthen a
candidate but are not assumed.

Promotion gates:

- Core: two independent sources for key mechanisms, primary source for ranked values,
  direct source for hard DO-NOT;
- Extended: at least one direct source, one source-linked mechanism, and an explicit
  applicability boundary;
- Exploratory: bibliographic discovery is sufficient, but deterministic performance
  and ranking are prohibited.

Duplicate and prototype-ownership decisions remain Yao gates. Expansion never deletes
or merges existing canon merely to reach a target count.

## 11. Review Gates

| Gate | Trigger | Reviewer | Required decision |
|---|---|---|---|
| G1 | R1 correction complete | Codex + Yao if scope changes | tools/ledger/recovery safe enough for M5 |
| G2 | 9-item OpenClaw pilot complete | Codex | worker quality and routing acceptable |
| G3 | first production M5 batch applied | Codex | scaling rules and sampling acceptable |
| G4 | ADRMATS v1 runbook all green | Codex + Yao | v1 release candidate |
| G5 | each expansion promotion wave | Codex + Yao for ownership/tier | promote/park/reject candidates |
| G6 | any push to `origin/review` | Yao | explicit release approval |

Claude Code continues automatically between gates and does not ask Yao to approve
routine batch scheduling, missing-source registration, report generation, or
validation reruns.

## 12. Failure Handling

- One worker failure: preserve artifacts, retry once with the same contract.
- Repeated worker failure: mark the item unresolved and continue other batches.
- Wrong modality: reject the item; reroute to `mimo-v2.5`.
- Rate limit: reduce concurrency; never create more than three workers.
- Conflicting evidence: no canon change; create a decision item.
- Validation regression: stop the current apply batch and revert only that batch via a
  corrective commit or uncommitted patch rollback; do not reset unrelated history.
- Context exhaustion: checkpoint and restart; do not compress away unresolved items.
- External office gap: register and exclude; do not block unrelated progress.

## 13. Success Criteria

The V2 programme is complete when:

- M1 safety properties are enforced by integration tests, not comments;
- the recovery ledger is machine-valid and traceable to real commits and sources;
- every previous M2 change has an accepted, corrected, or rejected disposition;
- all PDF evidence labour is traceable to an OpenClaw task and proper model route;
- Core ADRMATS outputs pass the strict v1 runbook;
- every residual row has a final full-audit disposition or an explicit external-input
  gap that prevents false closure;
- current and future office literature can be reconciled by manifest rather than
  filenames or memory;
- the catalogue contains 60-80 prototypes with honest tiers and promotion history;
- no push occurs without Yao's explicit approval.

## 14. Next Step After Approval

After Yao approves this design, create a detailed implementation plan and the first
long Goal for R1. That Goal may run continuously through R1-A to R1-E, use OpenClaw for
read-only audits, and stop only at Gate G1. It must not enter M5 or expansion.

