---
title: V3 Gate Operating Model — Long Runs, Concurrency, and Batched Review
status: approved_policy_pending_g1_freeze
date: 2026-06-19
decision_authority: Yao
primary_gate_reviewer: Codex
secondary_gate_reviewer: independent replacement supervisor
execution_coordinator: Claude Code
effective_from: after G1 is frozen and accepted
relationship:
  - Complements EXECUTION-PLAN-V3.md with the approved operating model.
  - Does not assert that G0 or G1 has passed.
  - Preserves the safety properties of RECOVERY-EXECUTION-V2-DESIGN.md.
  - The ADRMATS interface contract remains binding.
---

# V3 Gate Operating Model

## 1. Purpose and current-state rule

This document records the approved operating model for the remainder of the recovery,
Core v1 release, and expansion programme. It is designed to let Claude Code run for
long periods without requiring routine human supervision while keeping canon changes
transactional, attributable, and reviewable.

The worktree may still be changing while G0/R1 repairs are in progress. Therefore:

- this document does not certify the current HEAD;
- G0/G1 claims are provisional until Claude Code stops at a fixed G1 commit;
- formal G0/G1 verification is performed only against that immutable commit;
- the diatom downgrade count is evidence-derived, not fixed by an old report;
- no forward phase may rely on a report that has not been reproduced against its named
  commit.

## 2. Product direction locked by Yao

The Biomimetic Design Library is a heuristic candidate and evidence-retrieval module
for ADRMATS. It is not a material designer and does not rank candidates by performance.

The programme therefore prioritises:

1. correct prototype scope and source ownership;
2. honest evidence and verification labels;
3. an accurate `honesty_ledger` separating facts, leads, and inferences;
4. useful and scope-correct `design_translation`;
5. explicit failure boundaries and cautions;
6. performance values as honestly labelled leads, not ranking targets.

`verified` means one accepted direct source with quote, locator, and scope match.
`corroborated` means at least two independent accepted sources. A two-source Core tier
requirement does not redefine the row-level meaning of `verified`.

The delivery order is: trustworthy Core v1 first, then expansion to 60–80 tiered
prototypes through the same gated pipeline.

## 3. Gate topology: few human gates, frequent machine checkpoints

Human review is concentrated into four large gates. Between them, Claude Code may run
autonomously, make small local commits, retry workers, register source gaps, and repeat
validation without asking for routine approval.

### G1 — Foundation and recovery safety

Claude Code stops at a fixed commit after finishing the current G0/R1 repair round.
G1 is the combined formal review point for G0 and R1; passing an internal R0 test does
not require a separate user interruption.

G1 must prove:

- both configured MIMO key slots can send real pixel payloads directly to
  `mimo-v2.5` and receive traceable answers;
- no Tesseract, PDF text extraction, pre-OCR text, Gemini, or hidden fallback is used
  as a substitute for the direct-pixel capability test;
- canon builds can only write to staging; no direct canon-write flag or path remains;
- the real recovery applier rejects both zero and multiple stable-identity matches;
- ledger v2 schema, writer, validator, and existing R1 entries agree;
- no new canon mutation is represented by a `PENDING` or schema-invalid ledger entry;
- diatom content is restored without duplicates or collateral field loss;
- execution reports and state files describe the tested commit accurately;
- validation tools have no unintended writes into active or archived documentation;
- protected user assets remain untouched.

The diatom question is resolved by identity, not by choosing the number 8 or 9:

1. enumerate the intended rows from the accepted pre-corruption semantic baseline;
2. match every row to the current file by stable identity;
3. require exactly one current match per intended row;
4. require exactly one valid ledger entry per applied downgrade;
5. prove that all non-target semantic fields are preserved.

The resulting count is accepted only if those five conditions hold.

### G2 — Core v1 consolidated decision gate

After G1 passes, Claude Code is pre-authorised to continue directly to G2 without
waiting for another routine approval.

The G1-to-G2 long run covers all Core prototypes and prepares, but does not silently
apply, product-policy decisions concerning:

- scope and wrong-source findings;
- verification-label honesty;
- `honesty_ledger` classification;
- `design_translation` quality and attribution;
- ADRMATS-visible mechanism and caution fields;
- performance leads that must be excluded, narrowed, relabelled, or source-gapped.

OpenClaw performs all source/PDF/OCR/table reading and returns evidence candidates.
Claude Code evaluates JSON, brief behaviour, scope, labels, translation quality, and
the proposed disposition. Performance values are not exhaustively verified for ranking.

G2 delivers a dry-run candidate package and representative corrected-brief previews.
No ambiguous semantic correction is written to canon before G2 approval.

### G3 — Core v1 release candidate and expansion slate

After G2 decisions are approved, Claude Code may apply them transactionally and run
continuously through:

- Core v1 correction and full validation;
- ADRMATS representative brief generation and usefulness checks;
- Core release-candidate preparation;
- discovery and deduplication of the 60–80 prototype expansion slate;
- proposed Core, Extended, and Exploratory tier assignments;
- literature availability and external-input gap analysis.

G3 asks Yao to approve only unresolved product decisions, the Core v1 release
candidate, and the proposed expansion slate/tiering. It does not ask for row-by-row
approval where an approved policy can decide a whole class consistently.

### G4 — Expanded-library release gate

After the expansion slate is approved, Claude Code runs the same evidence, scope,
translation, ledger, and boundary pipeline for the accepted waves. G4 reviews:

- a 60–80 prototype tiered library;
- zero known wrong-source content in ADRMATS-visible output;
- honest treatment of missing or unavailable office literature;
- final consistency, chimera, causal-chain, boundary, brief, and repository checks;
- release notes and the exact commits proposed for push.

No push, force-push, history rewrite, destructive cleanup, or branch merge occurs
without Yao's explicit release approval at G4.

### Gate acceptance standards

G1 is `PASS` only when every item in its checklist is reproduced against the frozen
commit. A capability explanation, report, or green guard against an already-corrupted
HEAD is not sufficient.

G2 is `PASS` only when the Core audit package:

- covers every Core prototype and every ADRMATS-visible field;
- represents each actionable row by stable identity;
- contains machine-readable accepted, rejected, ambiguous, unchanged, failed, and
  source-missing dispositions;
- includes source hash, quote, locator, scope judgment, and model trace whenever the
  disposition relies on evidence;
- contains no invalid status enum, array-index identity, hidden fallback, or
  unsupported verification upgrade;
- groups repeated cases into policy decisions with explicit exception lists;
- produces representative brief previews with no known wrong-source content and an
  honesty ledger consistent with the previewed fields.

G3 Core v1 is `PASS` only when:

- all canon JSON parses and ledger v2 validation has no invalid post-G1 entries;
- consistency has zero unwaived errors and strict chimera checking reports zero
  violations;
- every Core prototype has explicit tier, lifecycle, scope, at least one accepted
  source-linked mechanism, and a scope-correct `design_translation`;
- all ADRMATS-visible verification labels are evidence-consistent;
- every hard boundary has direct source, quote, locator, and scope match;
- representative ADRMATS briefs contain no known cross-prototype contamination;
- brief facts, leads, and inferences reproduce from canon and the evidence ledger;
- feature-match ordering is independent of performance values;
- worktree and commit-object validation produce the same result.

G4 is `PASS` only when every active prototype has an explicit tier and lifecycle,
every promoted tier satisfies its literature and boundary gate, unresolved office-only
sources remain honestly excluded or pending, no Core invariant regresses, and the
release package identifies the exact commits and residual gaps. Reaching a numerical
prototype count alone is never a passing condition.

A gate verdict is either `PASS` or `FAIL`. A partial or conditional result remains
`FAIL` for forward canon work, although independent read-only work may continue when
its inputs do not depend on the failed property.

## 4. Machine checkpoints inside a long run

Machine checkpoints are not human gates. They run after every pilot, canon batch, and
commit and stop only the affected pipeline when they fail.

Required sequence:

1. pilot 3–10 representative rows before scaling a new policy or transformation;
2. validate worker contract, provider, model, key slot, inputs, output schema, and
   fallback trace;
3. validate stable identities and refuted-log exclusions;
4. render proposed canon changes in staging;
5. run pre-promotion invariants and ledger validation;
6. promote through the single canon writer;
7. run post-write invariants and the full relevant validation suite;
8. create a concern-scoped local commit only when the batch is green;
9. re-run critical validation against the commit object;
10. continue automatically or register the failure for the next gate package.

Routine missing sources are recorded and excluded from deterministic output; they do
not stop the entire long run. A source/claim conflict, ambiguous identity, refuted-row
resurrection, policy ambiguity, protected-field loss, or repeated infrastructure
failure does stop the affected pipeline.

## 5. Concurrency and key ownership

### 5.1 Claude Code

- Claude Code is the sole coordinator and sole canon writer.
- Claude Code uses MIMO key-1.
- At most three Claude Code subagents may exist concurrently; two is the normal
  operating level and the third slot is reserved for validation or recovery.
- Claude Code subagents work on non-overlapping artifacts and do not perform bulk PDF
  or source reading.

### 5.2 OpenClaw

- OpenClaw uses MIMO key-2 only.
- At most two OpenClaw workers may call key-2 concurrently.
- OpenClaw never falls back to key-1 and never writes canon, mapping, or ledger.
- Any task that may require pixels, layout, figures, tables, scans, uncertain OCR, or
  visual context uses `mimo-v2.5` with an actual image payload.
- `mimo-v2.5-pro` is permitted only when the input is certainly text-only.
- A mixed task is split; discovery of a visual dependency moves that item to
  `mimo-v2.5` rather than inferring from text.

The theoretical worker ceiling is three Claude Code subagents plus two OpenClaw
workers, but file ownership and API health determine the actual concurrency. More
workers must never be opened to compensate for rate limits.

### 5.3 Single-writer rule

- one artifact has one writer at a time;
- OpenClaw writes only isolated candidate/report artifacts;
- Claude Code merges accepted candidates;
- all canon promotion is serialised;
- explicit paths are staged; `git add -A` is prohibited during concurrent work.

## 6. Rate-limit and retry policy

For HTTP 429 or provider throttling:

1. honour `Retry-After` when present;
2. otherwise use exponential backoff with random jitter;
3. after repeated 429 responses, reduce that key's active concurrency to one;
4. retry on the same provider, model, and assigned key;
5. do not add workers, borrow the other key, enable fallback, or silently change model;
6. after three repeated cycles without progress, pause that queue, preserve its
   artifacts, and continue only independent work;
7. report the unresolved provider failure in the next gate package.

Credentials and literal key values must never appear in reports, raw committed
sessions, command output captured for review, or ledger entries. Reports identify only
the logical slot (`key-1` or `key-2`).

## 7. Canon transaction guard

No worker writes canon directly. Claude Code applies an accepted candidate through a
transactional promotion path.

### 7.1 Precondition checks

- acquire the single-writer lock;
- verify each target file still has its recorded preimage hash;
- require exactly one stable-identity row match;
- reject array-index-only identities;
- reject any match to the refuted registry unless an explicit Yao reversal exists;
- reject empty-over-nonempty replacement unless the disposition explicitly removes
  the field;
- require a schema-valid ledger v2 entry for every semantic field change;
- require source, quote, locator, scope, and model-routing facts claimed by the entry
  to be reproducible.

### 7.2 Staging invariants

The proposed full result is written outside canon and checked before promotion. Abort
the batch on:

- new stable-identity duplicates;
- an unexplained row, quote, locator, causal-chain, translation, boundary, scope-note,
  tier, or lifecycle count decrease;
- loss of a non-empty protected field;
- resurrection of a refuted row;
- a verification upgrade not authorised by accepted evidence;
- a hard boundary without direct source, quote, and locator;
- a changed file or field outside the candidate contract;
- ledger/schema/consistency/chimera/causal/boundary failure relative to the accepted
  baseline.

An intentional decrease is allowed only when the ledger records the exact identities,
fields, reason, evidence basis, and approving policy.

### 7.3 Promotion and post-write checks

- promote only the validated staged files;
- verify file hashes immediately after promotion;
- repeat all protected metrics and relevant validators;
- if a post-write check fails, restore only the transaction's recorded preimages,
  provided their hashes have not drifted, then stop canon writes;
- preserve the failed staged output and diagnostics for review;
- never use a broad checkout/reset that could erase unrelated user work.

Required regression tests include: default build leaves canon hashes unchanged;
zero/multiple identity matches fail; refuted resurrection fails; duplicate creation
fails; unexplained protected-count loss fails; invalid ledger fails; and an injected
post-write failure restores the exact preimage.

## 8. Gate review package

Every gate is bound to one immutable commit and contains both human-readable and
machine-readable artifacts.

Required artifacts:

- baseline and result commit hashes;
- exact changed files and semantic field counts;
- commands, exit codes, and commit-object validation results;
- `decision-summary.md` grouped by policy question;
- `decisions.jsonl` with stable identities, never actionable array indexes;
- accepted, rejected, ambiguous, unchanged, failed, and source-missing counts;
- model/provider/key-slot/fallback declarations for evidence work;
- representative ADRMATS brief previews and honesty-ledger checks;
- unresolved external assets, including office-only literature;
- rollback scope and residual risk.

Each decision item records: stable decision ID, affected prototype/row identities,
claim, evidence references, recommended disposition, alternatives, impact,
reversibility, and whether Yao's decision is required. Repeated row-level cases governed
by one policy are presented as one policy decision plus an exception list.

## 9. Independent dual review

At G0/G1/G2 and later technical gates:

1. Claude Code freezes a commit and stops modifying the review scope.
2. The replacement supervisor reviews that same commit independently and reports
   findings without applying fixes.
3. Codex independently re-runs the material checks against the same commit.
4. Codex reconciles both reviews and issues the final technical gate verdict.
5. A changed commit invalidates the old verdict; targeted fixes receive a delta review.
6. Yao decides product policy, irreversible scope/tier/merge/delete choices, release,
   and any dispute that cannot be resolved from evidence.

Codex is the primary gate reviewer and final technical decision-maker. The replacement
supervisor is the second independent pair of eyes, not a substitute authority.

## 10. Autonomous-run permissions and stop conditions

Between accepted gates, Claude Code may autonomously:

- dispatch and retry workers within the stated limits;
- copy inaccessible source inputs into an isolated worker workspace while preserving
  source hashes and provenance;
- produce candidates, reports, dry runs, validation snapshots, and local commits;
- register missing literature and continue independent work;
- apply already approved policy-class corrections through the canon transaction guard;
- run validation repeatedly and repair implementation defects within the approved
  scope.

Claude Code must stop and aggregate a decision when work requires:

- a new product or evidence policy;
- an ambiguous prototype identity or ownership decision;
- prototype merge, deletion, deduplication, tier promotion, or scope change not already
  governed by an approved rule;
- revival of refuted material;
- acceptance of conflicting sources;
- weakening an invariant or changing the ADRMATS interface contract;
- access to unavailable office assets that materially changes a decision;
- push, force-push, history rewrite, destructive cleanup, or branch merge.

The default operating rule approved by Yao is: after G1 passes, Claude Code continues
without another routine approval and stops at G2 with one consolidated decision and
review package.

## 11. Integration note

While the current G0/R1 repair round is active, this file remains a standalone policy
record and must not be folded into the same repair commit. At the frozen G1 commit,
Claude Code must reconcile `EXECUTION-PLAN-V3.md`, `model-routing-protocol.md`,
`openclaw-dispatch-rules.md`, and the execution entry/state with this approved model.
Any contradiction is resolved in favour of Yao's explicit decisions and this document,
without weakening V2 safety properties.
