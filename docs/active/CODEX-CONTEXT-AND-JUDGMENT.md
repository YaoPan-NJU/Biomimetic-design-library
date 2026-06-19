---
title: Codex Context and Judgment Memory
status: decision_context_not_status_authority
date: 2026-06-19
author: codex-supervisor
baseline_observed: review@ceb7b7a
cloud_baseline_observed: origin/review@e4dc2d0
purpose: durable context for Claude Code, Codex replacements, and independent reviewers
authority: RECOVERY-EXECUTION-V2-DESIGN.md governs execution; live facts must be recomputed
---

# Codex Context and Judgment Memory

## 0. How to use this file

This file preserves Codex's project context, historical findings, engineering judgment,
and takeover instructions. It is not a substitute for measurements from the current
commit. A replacement supervisor must:

1. read this file completely;
2. read `RECOVERY-EXECUTION-V2-DESIGN.md` completely;
3. recompute HEAD, worktree state, canon metrics, and validation results;
4. treat differences as new evidence rather than forcing the repository to match this
   snapshot;
5. never use an old report as authority over committed JSON and current command output.

No API key, credential, or secret is recorded here.

## 1. Project purpose and product boundary

The Biomimetic Design Library is the biomimetic inspiration and evidence-retrieval
module for ADRMATS, a water-treatment design system. It does not design materials. It
accepts pollutant, water-quality, removal, and engineering constraints and returns a
`BiomimeticDesignBrief` containing:

- candidate biological prototypes;
- the biological structure or mechanism worth borrowing;
- transferable design principles and implementation handles;
- direct evidence versus feature-based inference;
- applicability limits, cautions, and hard DO-NOT conditions;
- an honesty ledger separating facts, leads, and inferences.

The product objective is not the largest possible catalogue. It is a library whose
ADRMATS-visible recommendations, rankings, mechanisms, and hard boundaries are honest
and reproducible. Expansion to 60-80 prototypes is required, but only through explicit
Core, Extended, and Exploratory tiers.

## 2. Authority and truth hierarchy

Use this order when documents conflict:

1. Yao's current explicit instruction;
2. current committed canon and current validation output;
3. `docs/active/RECOVERY-EXECUTION-V2-DESIGN.md`;
4. `docs/active/PROJECT-RECOVERY-DESIGN.md`;
5. current standards and registries under `docs/active/`, `docs/references/`, and
   `docs/registries/`;
6. archived reports only as historical evidence.

`docs/active/SESSION-HANDOFF.md`, `docs/active/m1-m4-recovery-report.md`, root README,
`docs/ADRMATS_DELIVERY_PLAN.md`, and `docs/SUPPORT_SCOPE_AND_RISKS.md` contain stale or
challenged completion claims. They are evidence about what prior agents believed, not
authority that a milestone passed.

The frozen canon is `prototypes_db/*.json` at the repository root. The nested
`enrichment/`, `separation/`, `materials_reference/`, and `parked/` trees are mirrors,
legacy collections, or scope layers. They do not add another 34 unique prototypes.

## 3. Repository and branch snapshot

Observed before this file was created:

- workspace: `/Users/panyao/Desktop/Biomimetic-design-library`;
- branch: `review@ceb7b7a`;
- cloud: `origin/review@e4dc2d0`;
- local branch ahead by 15 commits;
- no recovery commit had been pushed;
- user-owned dirty asset: modified `tools/litextract` submodule;
- user-owned untracked assets:
  - `docs/optimization-v1/_w1_doi_map.json`;
  - `docs/optimization-v1/_w2_doi_map.json`;
  - `docs/optimization-v1/_w3_doi_map.json`.

Never stage, clean, rewrite, or absorb those user assets without explicit scope. Never
use `git add -A`. Never push without Yao's explicit release approval.

The local literature tree contained 633 PDFs and 592 extraction JSON files. Git cannot
prove that this includes office-only PDFs and patents that were never synchronized.

## 4. Current library structure and measured maturity

### 4.1 Mapping and interface layers

- 25 pollutant profiles;
- 29 pollutant alias groups;
- 53 pollutant map entries and 63 recommendation references;
- 24 molecular-feature map entries;
- 36 `prototype_metadata` entries;
- 16 mechanism-feature bridges;
- four generated ADRMATS example briefs;
- `tools/biomimetic_context.py` passes the three interface-honesty tests at the
  observed baseline.

### 4.2 Root prototypes

- 36 root IDs total;
- 24 active Core;
- 9 active Extended;
- 1 parked Exploratory (`namib-beetle`);
- 2 deprecated aliases (`diatom-inspired-porous`, `silkworm-silk`).

Ten IDs had no performance or mechanism rows:

- four active Core shells: `biomineralization-template`, `coral-skeleton`,
  `dna-aptamer`, `magnetic-bacteria`;
- four active Extended extraction shells: `alginate`, `cellulose-nanocrystal`,
  `metal-organic-framework`, `starch-granule`;
- two deprecated extraction shells: `diatom-inspired-porous`, `silkworm-silk`.

The six `pending_extraction` labels include the four active Extended shells and the two
deprecated aliases. Do not treat all six as equal extraction priorities.

### 4.3 Evidence counts

At the observed baseline:

| class | total | verified | partial | unresolved/other | quote present |
|---|---:|---:|---:|---:|---:|
| performance | 418 | 163 | 221 | 34 | 326 |
| mechanisms | 771 | 13 | 22 | 736 | 262 |

Important interpretations:

- `verified + partial = 384/418` performance rows is grade coverage, not 92% strict
  verification;
- strict `verified` labels cover 163/418 performance rows;
- only 94 of those 163 currently contain `verification_quote`;
- mechanisms have only 35/771 verified-or-partial labels;
- 230 mechanism rows already have quotes but remain `needs_review`, so much of M5 is
  claim/source acceptance work rather than first-pass extraction;
- nine diatom mechanism promotions to `partial` are specifically challenged and must
  be corrected in R1 unless independent evidence acceptance proves them.

### 4.4 Causal cards, translations, and boundaries

- 24 qualified causal-chain cards across 20 prototypes;
- Core causal-card coverage: 20/24;
- Extended causal-card coverage: 0/9;
- 25 design-translation rows covering all 24 active Core prototypes;
- no design translation for the nine active Extended prototypes or parked Namib item;
- 57 nested boundary conditions across 20 prototypes;
- 5 direct-source hard rules;
- 52 inferred soft cautions;
- 220 engineering constraints across 23 prototypes.

The old statement that the library has zero hard DO-NOT rules is stale. The correct
observed count is five, but each still needs to survive the corrected ledger and M5
acceptance process.

## 5. Current validation truth

Observed command results at `ceb7b7a`:

- `validate_consistency.py`: 1 error and 293 warnings; its report-only path exits zero,
  which is not a strict acceptance result;
- the error is a presentation/mapping break: five separation prototype render
  directories are disconnected and `prototypes/separation` is an orphan;
- `check_chimera.py --strict`: zero violations;
- `check_causal_chain.py`: 24 qualified cards, 16 IDs without a qualified card;
- `check_boundary_guardrail.py`: fails because 11 checked prototypes lack boundaries;
- `check_translation_specificity.py`: all existing 25 rows pass, but 12 IDs have no
  translation; its success does not mean all tiers are covered;
- `verify_adrmats_delivery.py`: 3 pass, 3 fail;
- `test_interface_honesty.py`: 3/3 pass;
- `check_repo_hygiene.py`: two issues (`CLAUDE.md` at root and stale
  `docs/active/SESSION-HANDOFF.md`).

One checker generated `docs/optimization-v1/phase5-chains.md` as a side effect during a
read-only audit; Codex removed that generated file immediately. R1 must fix validators
that write to obsolete or user-owned paths.

## 6. Failure history and causal diagnosis

No historical commit is both fully correct and current. Recovery must be additive and
field-level on top of `review`, not a checkout of an old snapshot.

### 6.1 Destructive or unsafe commits

| commit | failure | durable lesson |
|---|---|---|
| `1e50581` | bulk office rewrite removed structured translations, causal elements, boundary registrations, and quotes | never accept broad rewrites of frozen canon |
| `1313dd5` | ran the build path against canon and stripped chitosan evidence | build must be physically staging-only |
| `13dfdbf` | keyword sentence matching upgraded 228 mechanisms without claim-level proof | DOI, keyword, title, or sentence overlap cannot upgrade evidence |
| `82fa2c0` | broad rebuild stripped hundreds of quotes, locators, translations, causal chains, and boundaries | whole-file reconstruction is not recovery |
| `e4dc2d0` | valuable 24-to-36 expansion inherited damaged Core data and incomplete mapping/tier integration | keep expansion value, correct inherited evidence state |

### 6.2 Valuable recovery inputs

Do not merge these branches wholesale. Inspect them as candidate evidence:

- `integration/candidate-audit-a@39aee26`;
- `openclaw/audit-candidates-mussel-v3@4c8762d`;
- `openclaw/recovery-r01@548061a` if still present;
- `openclaw/audit-candidates-chitosan-diatom@7efdbf2`;
- office/Qoder/OpenClaw audit commits and archived reports;
- stashes, reflogs, worktree heads, and unreachable-but-recoverable Git objects.

Selection must be by stable row identity, source scope, quote, locator, and explicit
decision. Branch ancestry or a report's statement that work was accepted is not enough.

## 7. The 69 `verified` performance rows without quotes

### 7.1 What is proven

The 69 rows are concentrated in five prototypes:

- `chitosan`: 35;
- `chlorella-cell-wall`: 24;
- `mangrove-root`: 5;
- `mycelium`: 1;
- `spider-silk`: 4.

All have source and locator-like fields, making repair plausible. However, a scan of
every reachable canon revision for those five prototype files found no historical
`verification_quote` for any of the 69 rows. Known pre-destruction snapshots also
contained zero recoverable quotes for them. Therefore these quotes cannot simply be
restored from historical canon.

The first `verified` labels entered as follows:

- 59 rows in `176cc27` (`Phase 1.5 full verification`);
- 10 rows in `8ca0800` (`QoderWork Phase 0-2 evidence audit`).

The `176cc27` verifier used `pdftotext`, searched numeric tokens, accepted a row when at
least half of extracted numbers appeared anywhere in the PDF, and sometimes used a
generic keyword. It did not capture a quote and did not prove claim, metric, material,
or scope. These 59 rows had PDF-text contact, but their `verified` grade is too strong
under the current standard. This is not primarily a quote-loss event.

The ten `8ca0800` rows are eight later chitosan rows and two mangrove rows. That work was
part of a more deliberate Qoder/OpenClaw audit, but the canon still lacks quotes. Their
archived reports, candidate artifacts, extraction JSON, and local PDFs should be
searched before rereading sources. They are stronger recovery candidates than the 59
numeric-match rows, but they are not automatically accepted.

### 7.2 Required disposition

Do not bulk downgrade all 69 and do not preserve them as trusted facts merely because
they say `verified`.

Use this order:

1. register all 69 by stable identity and prevent quote-incomplete rows from entering
   ranking or fact output;
2. search archived reports, all candidate refs, stashes, reflogs, extraction JSON, and
   current local source files for exact quote and locator artifacts;
3. recover candidate evidence with source hash and provenance when found;
4. send only the unresolved source-centred batches to OpenClaw;
5. accept, narrow to partial, mark scope mismatch, or downgrade through the corrected
   deterministic applier and ledger v2;
6. never fabricate a quote from the stored claim text.

This issue belongs after tool/ledger safety in R1 and then M5 evidence acceptance. A
safe interface should treat `verified` without mandatory evidence fields as ineligible
until repaired, regardless of the stored label.

## 8. Recovery work already performed but not accepted as complete

Local commits after `origin/review` include:

- M0 document archive and operational documents;
- attempted M1 canon safety tooling;
- M2 additive evidence recovery and rollback of unsafe upgrades;
- diatom deduplication;
- tier/lifecycle metadata for 36 IDs;
- an M4 report.

Useful data was recovered and should be preserved. The milestone claims are challenged
because:

- default `build_prototypes_db.py` crashes on `args.writeCanon`;
- the claimed post-build invariant guard is absent;
- tests do not exercise the actual guarded entry point;
- the real applier does not enforce multiple-match ambiguity;
- all 1,204 legacy ledger entries have `applied_commit=PENDING`;
- ledger identity and schema fields are inconsistent;
- nine diatom mechanism upgrades lack evidence acceptance;
- strict consistency, causal, boundary, ADRMATS, and hygiene checks are not green.

The recovered canon fields are candidates to retain, not a reason to reset the branch.
R1 must correct the machinery and attach valid dispositions without erasing valuable
work.

## 9. Operating model approved by Yao

### 9.1 Roles

- Claude Code is the sole continuous coordinator and canon writer.
- OpenClaw performs all PDF, patent, OCR, visual, table, figure, source-matching, and
  row-level evidence labour.
- OpenClaw writes candidate-only artifacts and never canon, mapping, ledger, commits,
  merges, or pushes.
- Codex or a replacement independent supervisor reviews G0-G4 engineering/evidence
  gates.
- Yao decides scope, ownership, deletion, deduplication, tier promotion, external
  source provenance, and push/release gates.

Claude Code must not consume its own context on bulk PDF reading even if its API quota
is unlimited.

### 9.2 Model routing

- any possible visual information: `mimo-v2.5`;
- certainly text-only reasoning, JSON, manifests, code, or extracted text:
  `mimo-v2.5-pro`;
- if a text worker discovers visual dependence, it stops and reroutes;
- fallback to Google or any unintended provider fails the task;
- maximum concurrency is three;
- batch by source, not one call per row.

### 9.3 File access

Claude Code owns diagnosis and repair of OpenClaw access problems. It may make a
byte-identical read-only task copy in a dedicated Biomimetic OpenClaw workspace. It
must record original path, task path, size, SHA-256, and page provenance; verify the
hash; preserve the original; and remove the temporary copy afterward. Access failure
is not permission for Claude Code to take over bulk PDF reading.

## 10. Milestones and mandatory gates

### R0 / Gate G0: OpenClaw capability

Claude Code must prove:

- both MIMO key slots independently;
- `mimo-v2.5-pro` text reasoning on both slots;
- genuine pixel-based `mimo-v2.5` inspection on both slots;
- explicit per-dispatch model switching;
- no fallback;
- dispatch, monitoring, artifact collection, timeout, retry, cancel, and three-worker
  isolation;
- reproducible workspace/media access.

Outputs:

- `docs/active/openclaw-capability-report.md`;
- `docs/active/openclaw-capability-report.json`.

Stop at G0 for independent review. Do not enter R1 if R0 fails.

### R1 / Gate G1: recovery machinery correction

R1 has five parts:

- R1-A: staging-only build and real integration tests;
- R1-B: stable identity and zero/multiple-match rejection;
- R1-C: ledger v2 and migration/correction semantics;
- R1-D: nine diatom corrections, 239-versus-228 reconciliation, and recovery audit;
- R1-E: strict validators, no side-effect reports, truthful live state and documents.

Stop at G1. No mass evidence application before review.

### M5 / Gates G2-G3: evidence audit

- run a nine-item pilot with text, quantitative, visual, scope mismatch, ambiguity,
  accepted control, and refuted control cases;
- Codex/replacement reviews all pilot items at G2;
- apply a first production batch and review at G3;
- then continue source-centred OpenClaw waves with deterministic application.

### ADRMATS v1 / Gate G4

Required outcome:

- strict consistency zero errors;
- chimera zero;
- every ADRMATS-visible Core candidate has an accepted causal card;
- boundary guard green and hard rules source-backed;
- all ADRMATS delivery tests green;
- unresolved rows excluded from facts/ranking;
- docs and execution state agree with the commit object.

### Expansion / Gates G5-G6

Only after Core v1 is credible:

- retain 24 high-quality Core references;
- grow Extended to 24-36 direct-source candidates;
- grow Exploratory to 12-24 discovery candidates;
- target 60-80 total reviewed prototypes;
- Yao reviews ownership/tier waves at G5;
- Yao explicitly approves any push at G6.

## 11. Cross-device and office-source policy

The office device may contain valuable PDFs, patents, extraction outputs, decisions,
or work that never reached Git. Do not infer that an absent current file never existed.

Create and maintain:

- a SHA-256 literature manifest;
- `docs/registries/external-input-gaps.jsonl`;
- inventories of refs, worktrees, stashes, reflogs, audit reports, DOI maps, and patent
  mappings.

Unknown office assets remain `external_source_pending` and are excluded from ranking,
hard DO-NOT, deterministic recommendation, and final full-audit closure. Core ADRMATS
v1 may ship with those rows excluded. Full audit cannot close them until the office
assets are reconciled.

## 12. Engineering and evidence judgment rules

1. Empty is better than false.
2. A DOI, title, keyword, numeric token, or abstract mention is not claim-level proof.
3. `verified` requires source identity, exact supporting quote, reproducible locator,
   correct prototype/material/scope, and metric compatibility.
4. `partial` means the source supports a narrower claim; it is not a convenient grade
   for uncertain evidence.
5. Review maxima, qmax, observed uptake, removal percentage, rejection, sensor response,
   and system-level removal are non-interchangeable.
6. Hard DO-NOT requires direct source evidence; inferred boundaries remain soft and
   cannot contain unsupported numeric thresholds.
7. Never resurrect a row in `refuted-log.md`.
8. Never identify a row only by array index.
9. Zero or multiple stable matches stop that item.
10. Never allow an empty recovered value to overwrite a non-empty current value.
11. Never replace a whole canon file to recover a field.
12. Never run a destructive build against canon.
13. Never report a command as passed merely because a report-only script exits zero.
14. Validation runs both on serialized working data and the resulting commit object.
15. Every count in a checkpoint is recomputed, not copied from an earlier report.
16. One writer per artifact and one concern per commit.
17. Preserve unrelated dirty work and user-owned untracked files.
18. All Python invocations use `python3 -X utf8` in this environment; `python` is not
    available despite old documents using that spelling.

## 13. Workload judgment and priority

The project has a strong structure but incomplete evidence trust.

- repository/interface structure: roughly 75% complete;
- 24-Core content skeleton: roughly 80% complete;
- strict Core evidence safety: roughly 30-40%;
- Extended/Exploratory quality: below 20%;
- raw 60-80 count target: roughly halfway by count, less than halfway by quality.

Priority order:

1. R0 OpenClaw capability;
2. R1 tool, identity, ledger, and false-completion correction;
3. ADRMATS-visible Core evidence and four missing Core causal/boundary packs;
4. full Core evidence audit;
5. cross-device source reconciliation in parallel;
6. tiered expansion to 60-80;
7. deduplication/deletion only through Yao decisions.

The largest evidence queues are chitosan, fish-scale hydroxyapatite, mussel adhesion,
superhydrophobic artificial, polydopamine, water-strider, and lotus. Together they
contain most unresolved mechanisms. Process them by source so one PDF resolves many
rows.

## 14. Stop and escalation conditions

Stop the affected item or Goal when:

- R0 routing, key isolation, visual proof, or fallback status cannot be proven;
- stable identity is absent or ambiguous;
- source and stored claim conflict;
- a change would resurrect refuted data;
- a protected metric drops without an accepted disposition;
- ownership, duplicate merge, tier, scope, or external provenance requires Yao;
- validation worsens or repeats the same failure three times;
- push, force-push, history rewrite, destructive cleanup, or branch-wide merge would be
  required.

Routine missing sources do not stop unrelated work. Register them and exclude them.

## 15. Exact Claude Code startup prompt and first Goal

Paste the following entire block into Claude Code from the Desktop repository session:

```text
Work only in /Users/panyao/Desktop/Biomimetic-design-library on the existing review
branch. You are the continuous coordinator. Before acting, read these files completely:

1. docs/active/CODEX-CONTEXT-AND-JUDGMENT.md
2. docs/active/RECOVERY-EXECUTION-V2-DESIGN.md
3. docs/active/PROJECT-RECOVERY-DESIGN.md
4. docs/active/CLAUDE-CODE-TAKEOVER.md
5. docs/active/evidence-quality-standard.md
6. docs/registries/refuted-log.md
7. docs/registries/decision-queue.md
8. docs/registries/prototype-duplication-record.md

Then perform a read-only preflight: report pwd, branch, HEAD, origin/review, ahead/behind,
worktree changes, worktrees, relevant refs/stashes, and current protected user assets.
Recompute current canon metrics and do not copy counts from handoff documents. Preserve
the modified tools/litextract submodule and the three untracked _w*_doi_map.json files;
never stage or modify them. Do not touch canon during preflight. Do not push.

Create a long Goal with this exact objective:

"Execute R0 OpenClaw Capability Qualification for the Biomimetic Design Library from
the current review HEAD. Independently diagnose and make only the minimum reversible,
non-canon fixes required for Claude Code to control OpenClaw. Prove both configured
MIMO key slots independently; mimo-v2.5-pro text reasoning on each; genuine pixel-based
mimo-v2.5 image or rendered scanned-PDF inspection on each; explicit per-dispatch model
switching; zero unintended fallback; reproducible project workspace/media access; and
dispatch, monitoring, artifact collection, timeout, retry, cancellation, and at most
three concurrent isolated workers. Never expose credentials. If repository or
literature files are inaccessible, create byte-identical read-only task copies in a
dedicated Biomimetic OpenClaw workspace with original path, copy path, size, SHA-256,
page provenance, post-run hash verification, and cleanup; never alter the original and
never take over bulk PDF reading yourself. Produce sanitized
docs/active/openclaw-capability-report.md and .json, validate them, make small scoped
local commits, and stop at Gate G0 with exact commands, runtime routing metadata,
artifact hashes, commit IDs, residual risks, and a clear pass/fail recommendation. Do
not enter R1, M5, canon repair, expansion, deduplication, or push before independent G0
review."

Goal execution rules:

- OpenClaw does all PDF, patent, OCR, image, table, and evidence labour.
- Use mimo-v2.5 for any possible visual input and mimo-v2.5-pro only for certainly
  text-only work.
- Reject any test with fallbackUsed=true or mismatched provider/model.
- Maximum concurrency is three and every worker has a unique task/artifact path.
- All Python commands use python3 -X utf8.
- Never use git add -A, reset --hard, checkout --, force-push, or branch-wide merge.
- Checkpoint durable state every completed batch or 60-90 minutes.
- If R0 cannot pass, diagnose, attempt the minimum safe fix, preserve evidence, and stop
  at G0; do not weaken the test.

Your first response must contain: confirmation that all eight files were read, measured
preflight facts, the exact Goal you created, the first R0 test matrix, files you may
change, protected files you will not touch, and explicit confirmation that no canon or
push occurs in this Goal. Then begin the Goal without waiting for routine approval.
```

## 16. Instructions for a replacement Codex/supervisor

If Codex quota is unavailable, another strong reasoning model may act as independent
supervisor. It must not become another bulk worker or accept Claude Code's self-report
at face value.

At each gate it should:

1. read the committed artifacts and diff, not only the narrative report;
2. rerun relevant commands from a clean view of the commit object;
3. sample raw worker artifacts and source locators;
4. verify model/provider/fallback metadata and source hashes;
5. look for untracked user assets accidentally staged;
6. challenge denominator changes and status-definition changes;
7. distinguish preserved valuable work from unsupported milestone claims;
8. issue findings by severity with file/line or row identity;
9. approve only the next gate, never the entire remaining programme;
10. leave push authority with Yao.

The replacement supervisor's default decision should be conservative about evidence
grades and permissive about reversible read-only investigation. The correct question is
not "did an agent work hard?" but "can another reviewer reproduce every exposed fact
and can the tooling prevent recurrence?"

