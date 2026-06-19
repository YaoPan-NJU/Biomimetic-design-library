# Biomimetic Design Library Recovery Design

status: approved
date: 2026-06-19  
cloud_baseline: `origin/review@e4dc2d0`  
working_location: `/Users/panyao/Desktop/Biomimetic-design-library` on branch `review` (Yao directive 2026-06-19: the earlier `/private/tmp/biomimetic-recovery-docs` worktree + `codex/recovery-plan-20260619` branch requirement is OBSOLETE; recovery is performed directly in the Desktop `review` worktree)

## 1. Purpose

This document defines how to recover the Biomimetic Design Library without
discarding valuable work performed after destructive commits. It also defines
the operating model for expanding the library from 24 high-quality prototypes
to a tiered collection of roughly 60–80 prototypes.

The library remains a biomimetic water-treatment design reference for ADRMATS.
It provides biological mechanisms, transferable design principles, evidence,
and failure boundaries. It does not design or prescribe materials.

Review is the permanent project mainline. Recovery restores a trustworthy
review baseline; expansion supplies new review candidates. Neither activity is
successful unless it improves the reliability, explainability, and boundary
honesty of the ADRMATS calling library. Prototype count is therefore a catalogue
goal, not an acceptance metric.

## 2. Confirmed Failure History

The recovery must account for the following independently reproduced failures.

| Commit | Failure | Current consequence |
|---|---|---|
| `1e50581` | Office-side bulk JSON rewrite removed all root `design_translation`, root mechanism `causal_chain`, boundary registrations, and 63 quotes. Its validation report was produced from a different state than the committed tree. | Later recovery restored only part of the structured data. |
| `1313dd5` | `build_prototypes_db.py` was run against frozen canon and stripped 15 quotes from surviving chitosan performance rows. | Later evidence work replaced much of this loss, but the incident proves the build is destructive. |
| `13dfdbf` | Keyword-based PDF sentence matching upgraded 228 mechanisms to `partial`. Independent audits showed all 48 chitosan upgrades invalid and only 6 of 36 mussel upgrades acceptable. | Mechanism coverage at cloud HEAD is materially overstated. |
| `82fa2c0` | A canon rebuild rewrote all 24 root prototype files, removed 242 performance quotes, 242 mechanism quotes, locators, translations, causal chains, and boundary structures, and reintroduced an older 419/528 row set. | The latest cloud branch contains the largest unresolved evidence regression. |
| `e4dc2d0` | Prototype expansion added useful new prototypes, but inherited the damaged core, reintroduced 13 diatom performance rows, and added 12 root prototypes absent from `feature-mapping.json`. | Expansion is valuable, but cloud HEAD is not a correct canonical baseline. |

The immediate cause is destructive regeneration of frozen canon. The deeper
cause is that `build_prototypes_db.py` generates only a subset of the canon
schema and merges by unstable row keys. Empty or regenerated fields can replace
manually curated evidence, while the script has no invariant that rejects data
loss. Project documents had already prohibited running the script, but later
task files instructed workers to run it.

## 3. Recovery Principles

1. Preserve Git history. Repair by additive commits; do not force-push or
   rewrite `review`.
2. Work in isolated branches and worktrees. (2026-06-19 amendment) Recovery now
   executes directly in the Desktop `review` worktree at
   `/Users/panyao/Desktop/Biomimetic-design-library` per Yao authorization. The
   earlier "do not touch the Desktop worktree" rule is withdrawn; the worktree's
   uncommitted assets — `tools/litextract` (submodule) and the three untracked
   `_w1/_w2/_w3_doi_map.json` — are still preserved exactly and never staged.
3. Treat `prototypes_db/*.json` as frozen canon. Never reconstruct canon by
   replacing complete files from extraction outputs or old commits.
4. Restore fields, not files. Match records using stable identities and record
   every accepted field in a recovery ledger.
5. Evidence quality outranks commit recency. A later empty or auto-generated
   field cannot replace an earlier accepted quote.
6. Intentional wrong-source removal outranks historical presence. Recovery must
   not resurrect rejected rows.
7. Ambiguity is a result, not an invitation to guess. Unclear matches enter a
   decision queue and remain excluded from ranking.
8. No verification upgrade is accepted solely because a DOI maps to a PDF or a
   sentence shares keywords with a claim.
9. Every destructive operation must have a pre-change snapshot, a field-count
   guard, and a post-change validation report.

## 4. Two Delivery Milestones

### Milestone 1: v1 Deliverable

The first milestone makes ADRMATS outputs trustworthy before the full archive
is completely audited.

Completion requires:

- canonical data repaired and all known destructive regressions resolved;
- default ADRMATS results restricted to Core prototypes;
- every value used in recommendation or ranking backed by an accepted source,
  quote, and locator;
- unresolved or missing-source records downgraded and excluded from ranking;
- hard DO-NOT rules backed by direct evidence;
- all required consistency, chimera, interface, and evidence-gate checks pass;
- active documentation accurately describes the committed tree.

### Milestone 2: Full Audit

The second milestone resolves every remaining performance row, mechanism,
boundary, source gap, and exploratory prototype by one of four outcomes:

- accepted with source evidence;
- retained as explicitly soft background;
- parked as a documented knowledge gap;
- removed and recorded in the refuted log.

Milestone 2 is complete only when no unresolved record can silently enter
ADRMATS recommendation, ranking, causal explanation, or DO-NOT output.

## 5. Tiered Prototype Library

The target library contains roughly 60–80 distinct prototypes. Quantity and
evidence quality are represented separately.

### 5.1 Library tiers

| Tier | Initial target | Use |
|---|---:|---|
| `core` | 24 | Default ADRMATS recommendation, ranking, causal explanation, and boundary output. |
| `extended` | 24–36 | Inspiration search and conditional recommendation. Only individually qualified rows may enter quantitative ranking. |
| `exploratory` | 12–24 | Catalogue discovery and future work. Excluded from default recommendation and ranking. |

Every prototype receives two independent fields:

- `library_tier`: `core`, `extended`, or `exploratory`;
- `lifecycle_status`: `active`, `pending_extraction`, `parked`, or `deprecated`.

Evidence rows retain their own status. Prototype tier must never be inferred
from the strongest row in the file.

### 5.2 Promotion gates

Exploratory to Extended requires:

- a distinct biomimetic concept with duplicate ownership resolved;
- at least one direct source;
- at least one source-linked mechanism;
- an explicit scope statement and ranking exclusion policy;
- valid JSON, mapping, and consistency checks.

Extended to Core additionally requires:

- full PDF audit for all ADRMATS-visible claims;
- a qualified causal chain and at least one evidence-graded boundary;
- primary-source support for every ranked quantitative value;
- no unresolved wrong-source, duplicate-ownership, or metric-type issue;
- Claude Code acceptance and user approval.

Demotion preserves history and records the reason. It never silently deletes
the prototype.

## 6. Canon Recovery Architecture

### 6.1 Inputs

Recovery uses multiple historical sources because no single commit is both
latest and correct:

- `39aee26` / `2242cc9`: accepted audit-era core row set and performance
  evidence before unsafe mechanism bulk upgrades;
- `cfdc0c1` through `dbef652`: accepted causal-chain recovery, QoderWork
  performance evidence, path corrections, and later accepted metadata;
- `97f14f3` and its accepted predecessors: structured fields that were never
  fully recovered, including boundary registrations and two top-level fields;
- `3797c4b`, `21bfa76`, and `2b070a1`: only independently supportable Task
  52–68 additions;
- `e4dc2d0`: the 12 new root prototypes and other non-destructive expansion
  changes;
- `openclaw/audit-candidates-mussel-v3`: six independently checked mechanism
  quotes and locators.

### 6.2 Record identities

Performance rows are matched in this order:

1. prototype ID + normalized DOI/patent/standard ID + normalized parameter +
   normalized value + normalized material;
2. source basename + parameter + value + material;
3. normalized row fingerprint after excluding mutable evidence fields.

Mechanisms are matched in this order:

1. prototype ID + normalized DOI + normalized mechanism name + description
   fingerprint;
2. source basename + normalized mechanism name;
3. normalized name + description fingerprint.

Array index is never an identity. Zero or multiple matches are recorded as
ambiguous and left unchanged.

### 6.3 Field precedence

For a matched row:

1. accepted direct PDF/visual evidence with quote and locator;
2. accepted human or Claude Code review;
3. accepted OpenClaw candidate reviewed by Claude Code;
4. unreviewed automated extraction;
5. empty or inferred data.

An empty field never overwrites a non-empty field. A later `partial` label does
not override an earlier accepted `needs_review` unless the later record includes
claim-supporting evidence. Status is recomputed from the accepted evidence, not
copied mechanically.

### 6.4 Required corrections

The recovery must:

- restore accepted performance quotes and locators lost at `82fa2c0`;
- restore translations, causal chains, boundary structures, and accepted
  top-level fields;
- return the core diatom row set to the accepted deduplicated state;
- roll back all `13dfdbf` mechanism upgrades unless independently audited;
- retain the six valid mussel-v3 mechanism upgrades;
- retain accepted Task 52–73 performance evidence and path corrections where
  they improve, rather than replace, stronger evidence;
- retain the 12 expanded root prototypes and assign tiers/lifecycle states;
- add all root prototypes to the authoritative mapping without allowing a
  rebuild to overwrite pending or manually curated entries;
- produce a machine-readable recovery ledger for every restored, replaced,
  rejected, and ambiguous field.

## 7. Build and Import Safety

`build_prototypes_db.py` must no longer be an in-place canon generator.

The safe design is:

- default output is a candidate/staging directory;
- writing to canon requires an explicit guarded mode and a clean worktree;
- pre/post invariant checks reject drops in rows, quotes, locators, causal
  chains, translations, boundary IDs, scope notes, and tier metadata unless a
  reviewed allowlist explains each drop;
- stable matching detects duplicate keys and refuses ambiguous merges;
- pending-extraction and manually activated prototypes cannot be overwritten by
  absent extraction data;
- all generated changes are presented as a diff for review before application.

Until those protections exist and pass tests, project instructions must state
that the build script is forbidden for canon writes.

## 8. Evidence Quality Standard

### 8.1 Row grades

- `verified`: claim and metric are directly supported by an accepted source;
  quote and locator are present; source identity and scope match; required human
  approval is complete.
- `partial`: a source supports a narrower or condition-specific claim, or only
  one source is available; the limitation is explicit.
- `needs_review`: source may exist, but the claim has not passed direct review.
- `missing_pdf`: source identity is known but the source file is unavailable.
- `unverified`: no accepted evidence review has been completed.
- `knowledge_gap`: a material question is known to lack sufficient evidence.
- `scope_mismatch`: evidence is real but belongs to another prototype, metric,
  or application domain.

Keyword overlap, DOI presence, a paper title, an abstract-only paraphrase, or an
LLM-generated sentence cannot by itself qualify a row as `partial` or
`verified`.

### 8.2 Ranking gate

A row may enter quantitative ranking only when:

- source identity, quote, and locator are present;
- metric type and unit are normalized;
- prototype/material ownership is explicit;
- duplicate and review-maximum exclusions are resolved;
- test conditions are represented or the row is marked condition-specific.

### 8.3 Boundary gate

Hard DO-NOT requires direct source evidence and a valid locator. Soft boundaries
may be condition-specific or single-source. Inferred limits remain knowledge
gaps and cannot block a design.

## 9. Literature Acquisition

Literature expansion is a required project stream.

Minimum source gates are:

- Core: at least two independent sources for key mechanisms; every ranked value
  traced to a primary paper or patent; direct evidence for hard DO-NOT rules.
- Extended: at least one direct source, one source-linked mechanism, and an
  explicit applicability boundary. Unverified values remain ranking-excluded.
- Exploratory: a bibliographic discovery record is sufficient, but no
  deterministic performance claim may be exposed.

The source workflow is:

1. register DOI/title/prototype/source path/file hash/text-or-OCR status;
2. deduplicate files and resolve extraction-to-PDF mappings;
3. create a tier-prioritized missing-source queue;
4. acquire sources through open-access repositories, publishers, patent
   databases, or institutional access;
5. extract into a candidate area;
6. verify text or visual evidence;
7. accept through Claude Code review before canon write.

Unavailable sources remain `missing_pdf` or `knowledge_gap`; secondary summaries
must not be represented as the unavailable primary source.

## 10. Claude Code and OpenClaw Operating Model

Claude Code is the sole coordinator. It owns task decomposition, model routing,
branch control, conflict decisions, acceptance, validation, commits, and pushes.

OpenClaw is a controlled worker. It may inspect sources, extract evidence,
produce candidate patches, and write reports in its assigned worktree. It may
not independently upgrade evidence grades, merge branches, push `review`, run
the destructive build, or replace whole canon files.

### 10.1 Mandatory model routing

- Use `mimo-v2.5` whenever a task may require visual information: scanned PDFs,
  images, tables, curves, captions, layout, visual cache, uncertain OCR, patent
  figures, or multimodal file inspection.
- Use `mimo-v2.5-pro` only when the task is certainly text-only: JSON/code/Git
  analysis, Markdown synthesis, structured text comparison, and planning.
- Split mixed tasks into text and visual sub-tasks.
- If a pro worker discovers visual evidence is needed, it stops that evidence
  item and hands it to a `mimo-v2.5` worker. It must not infer the visual result.
- Every worker report declares model, modality requirement, input types, and
  routing reason. A routing violation is an acceptance failure.

Maximum concurrency is three. Only one worker may write a given JSON file at a
time.

### 10.2 Dispatch contract

Every task specifies:

- task ID, objective, and success criteria;
- baseline commit and isolated worktree;
- exact allowed files and prohibited files;
- selected model and routing reason;
- input sources;
- required report and machine-readable artifacts;
- validation commands;
- stop conditions;
- prohibition on direct push and unreviewed evidence upgrades.

### 10.3 Coordinator decision playbook

The coordinator evaluates evidence with five questions, in order:

1. Does the quoted source directly support the complete claim, rather than
   merely mention the same topic?
2. Does the source describe the same biological prototype, material class, and
   application domain?
3. Does the metric mean what the row claims: qmax, observed uptake, removal
   percentage, rejection, system-level removal, selectivity, sensor response,
   or a figure estimate?
4. Are the quote, locator, source identity, and local file mapping sufficient
   for another reviewer to reproduce the decision?
5. Are the tested conditions and failure boundary represented honestly?

If any answer is no, the record cannot be `verified`. A narrower supported claim
may be `partial`; otherwise it remains `needs_review`, `knowledge_gap`, or
`scope_mismatch`.

Operational heuristics:

- Latest is not the same as healthiest. Compare field evidence and accepted
  decisions, not commit timestamps.
- A report is not proof. Re-run checks against the exact committed tree named in
  the report, preferably from a temporary detached worktree.
- A quote must support the whole stored claim. Keyword overlap and DOI equality
  only establish a candidate relationship.
- Never confuse design inspiration with measured material performance. Keep
  biological mechanism, engineered implementation, and test result ownership
  explicit.
- Review-table maxima, concentration-dependent uptake ranges, sensor LOD/Kd,
  removal percentages, and system-scale percentages are not interchangeable
  with adsorption qmax.
- Exact duplicates and shared PDA/mussel or shell/HAp evidence must have one
  ranking owner or an explicit duplicate exclusion.
- Use hard DO-NOT only for directly supported failure constraints or clear
  wrong-source/domain contamination. Unquoted engineering intuition stays soft
  or a knowledge gap.
- Pilot a worker on a small sample before a large batch. Reject the batch early
  if the sample shows paraphrased quotes, weak locators, scope drift, or wrong
  model routing.
- Require workers to report unchanged, rejected, ambiguous, and failed items;
  success-only reports conceal risk.
- Recalculate all statistics from committed JSON. Never copy coverage numbers
  from an earlier report.
- Review diffs by semantic field counts and record identities, not only line
  counts. JSON reformatting can hide destructive rewrites.
- Validate after the final write and again against the commit object. A check
  run before serialization does not validate the committed result.
- Stage and commit explicit files. Avoid broad `git add -A` when unrelated
  worker artifacts or ignored-source changes may be present.
- Keep data recovery, evidence upgrades, schema changes, and documentation moves
  in separate commits so each can be audited or reverted independently.

OpenClaw acceptance uses a two-stage gate:

1. Contract review: correct baseline, model, allowed files, report schema,
   changed paths, and clean diff.
2. Evidence review: reproduce a risk-based sample, including every hard DO-NOT,
   every top-ranking value, every scanned/visual claim, every cross-prototype
   ownership decision, and every status upgrade without a primary source.

When uncertainty remains, the safe action is no canon change plus a precise
decision-queue entry. Progress is measured by trustworthy dispositions, not by
the number of upgraded rows.

## 11. Documentation Architecture

Documentation is reorganized without deleting historical evidence:

```text
docs/
├── README.md
├── active/
├── registries/
├── references/
├── imported/
└── archive/
    ├── pre-optimization/
    └── optimization-v1-2026-06/
        ├── phase-reports/
        ├── task-history/
        ├── evidence-reports/
        ├── old-handoffs/
        └── generated-logs/
```

Files move with `git mv`. An archive manifest records original path, new path,
reason, date, and replacement document. Active references in README, CLAUDE.md,
and scripts are updated and checked. Archived snapshots may retain historical
internal links but must be clearly marked non-operational.

New operational documentation consists of:

- recovery master plan;
- commit audit and root-cause report;
- canon recovery specification and ledger schema;
- evidence quality standard;
- collaboration and model-routing protocol;
- execution roadmap and acceptance runbook;
- Claude Code takeover guide.

## 12. Branch and Commit Policy

- Develop in isolated branches from the current cloud baseline.
- Use small commits separated by concern: documentation archive, audit tooling,
  canon recovery, build safety, mapping/tiering, and evidence acceptance.
- Do not mix evidence-grade changes with formatting or broad regeneration.
- Each canon commit includes before/after metrics and the ledger subset it
  applies.
- Claude Code accepts worker commits by review or selective cherry-pick. It does
  not merge an unreviewed worker branch wholesale.
- After all checks pass, correction commits are fast-forwarded or merged into
  `review` without history rewriting.

## 13. Validation and Stop Conditions

Every recovery checkpoint runs:

- JSON parsing for all database files;
- recovery-ledger completeness and ambiguity checks;
- quote/locator/causal/translation/boundary count regression guards;
- `validate_consistency.py`;
- `check_chimera.py --strict`;
- causal-chain and boundary-guardrail checks;
- ADRMATS interface and ranking-honesty tests;
- documentation link and active-reference checks;
- `git diff --check` and repository hygiene checks.

Work stops and escalates when:

- a stable identity has multiple plausible matches;
- a source contradicts an accepted claim;
- a proposed merge would reintroduce refuted data;
- a worker used the wrong model modality;
- a validation count drops without an approved ledger entry;
- a required PDF cannot be legally or institutionally obtained;
- a change requires a user decision about prototype ownership or scope.

## 14. Success Criteria

The recovery design succeeds when:

- the exact origin and disposition of every known regression are documented;
- no accepted evidence is lost and no refuted row is resurrected;
- unsafe auto-verification is removed or independently revalidated;
- the 24 Core prototypes are trustworthy and ADRMATS-safe;
- the expanded 60–80 prototype catalogue has explicit tiers and promotion
  gates;
- documentation has one operational entry point and historical records remain
  traceable;
- Claude Code can coordinate work immediately using deterministic dispatch,
  model-routing, acceptance, and rollback rules.
