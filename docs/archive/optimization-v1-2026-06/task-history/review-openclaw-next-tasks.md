# OpenClaw Next Evidence-Audit Tasks

status: active

Last updated: 2026-06-16

## Operating Mode

OpenClaw owns the bulk evidence work. Codex owns acceptance, key decisions, queue curation, and GitHub checkpoints.

Follow `docs/optimization-v1/review-openclaw-coordination.md`.

Hard constraints:

- Use `mimo-v2.5` only.
- Do not use `mimo-v2.5-pro`.
- Do not modify `prototypes_db/*.json`.
- Do not run `tools/build_prototypes_db.py`.
- Do not commit or push git.
- Write batch outputs under `docs/optimization-v1/`.
- Missing PDFs, scanned patents, review-only rows, and inferred boundaries are not hard evidence.

## Immediate Codex Gate

Before starting new OpenClaw bulk work, Codex must push the completed local checkpoint when Git write access is available:

- Batch 04 separation/superwetting surfaces preflight
- Batch 05 selective/material-reference preflight
- Batch 06 enrichment mirror crosscheck
- OpenClaw coordination protocol
- this next-tasks file

If Git write access is still blocked, OpenClaw may continue local-only work and write outputs, but Codex should not attempt database edits.

## Task 07: Parked And Registry Consistency

Output file:

`docs/optimization-v1/review-full-audit-openclaw-batch-07-parked-registry.md`

Scope:

- `prototypes_db/parked/namib-beetle.json`
- cross-directory duplicate source consistency
- PDF path and extraction JSON mapping for all audited batches

Questions to answer:

- Is `namib-beetle` parked because of weak evidence, duplicate scope, missing source, or unfinished curation?
- Which existing prototypes already contain Namib beetle / fog-harvesting evidence?
- Are any Batch 01-06 source files duplicated under different filenames, suffixes, or directories?
- Which high-impact rows still cite bare filenames where a local ` 2.pdf` or ` 3.pdf` exists?

Required tables:

- parked item audit table
- duplicate/cross-directory source table
- original PDF path to extraction JSON mapping table
- candidate queue items table
- boundary/DO-NOT candidate table

## Targeted Sub-Batch A: DNA Aptamer Evidence Build

Output file:

`docs/optimization-v1/review-full-audit-openclaw-dna-aptamer-evidence-build.md`

Scope:

- `prototypes_db/dna-aptamer.json`
- `prototypes_db/enrichment/dna-aptamer.json`
- local folder `仿生文献库/3rd/第B组-新方向/B1-DNA适配体/`
- local extraction JSONs under `tools/litextract/outputs/extractions/第三波/json/`
- patent `2026-CN121588773A-aptamer-aflatoxin-adsorbent.pdf`

Goal:

Build a source-grounded evidence map before proposing any JSON edits.

Required output:

- literature-to-path mapping table;
- which sources are detection/biosensor only versus adsorption/capture/removal;
- candidate performance values only if they are real adsorption/capture/removal metrics;
- candidate mechanisms with quote and locator;
- boundaries, including target specificity, matrix effects, regeneration, immobilization, and biosensor-vs-adsorbent scope.

Acceptance bar:

No candidate can enter Codex queue unless it has a source path, locator, quote, and a clear metric type.

## Targeted Sub-Batch B: Diatom Source Path And Dedup Cleanup

Output file:

`docs/optimization-v1/review-full-audit-openclaw-diatom-path-dedup.md`

Scope:

- `prototypes_db/diatom-frustule.json`
- `prototypes_db/enrichment/diatom-frustule.json`
- local diatom PDF folder `仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/`
- `2021-杜-硅藻-硅藻土-吸附-重金属 2.pdf`

Goal:

Do not verify all rows yet. First normalize the evidence map:

- duplicate performance rows;
- bare filename to full local PDF path;
- PDF to extraction JSON correspondence;
- which rows are diatom/frustule/diatomite evidence versus unrelated structural design.

Acceptance bar:

Codex wants a dedup recommendation table before any quote insertion decisions.

## Targeted Sub-Batch C: MOF Verification Semantics

Output file:

`docs/optimization-v1/review-full-audit-openclaw-mof-verification-semantics.md`

Scope:

- `prototypes_db/materials_reference/metal-organic-framework.json`

Goal:

Audit the registry semantics problem:

- `provenance_summary.n_verified = 252`
- many rows have `verification = single_source`
- most rows lack quotes/locators

Required output:

- define what `single_source` means in the current file;
- identify rows that are truly quote-verifiable from local PDFs;
- identify wrong-source rows already suspected by Codex:
  - Aramesh2021 chitosan dye-removal rows in MOF;
  - Cheng2024 membrane/catalytic BPA rows in MOF;
  - H2 storage row mixed into water-treatment adsorption ranking.

Acceptance bar:

Do not propose upgrading any row to verified. Propose only downgrade/semantics/queue actions with evidence.

## Targeted Sub-Batch D: Starch Extreme Value Sanity Check

Output file:

`docs/optimization-v1/review-full-audit-openclaw-starch-extreme-values.md`

Scope:

- `prototypes_db/materials_reference/starch-granule.json`

Priority rows:

- `performance_data[52-59]`
- `performance_data[66-77]`
- any row with value above 1000 mg/g or mixed `%`, `mg/g`, `g/g`, concentration-dependent ranges, or review maxima.

Goal:

Prevent false ranking from extreme review-table values.

Required output:

- exact source table/page/figure locator;
- whether the value is qmax, removal %, concentration-derived capacity, range, or review maximum;
- experimental conditions and pollutant concentration;
- whether the row should be kept, demoted, split, or flagged as needs_human_decision.

## OpenClaw Completion Signal

When a worker finishes, write at the top of the output file:

```text
status: ready_for_codex_acceptance
worker: OpenClaw/mimo-v2.5
completed_at: <local timestamp>
```

Codex will then:

- read the batch;
- spot-check fragile/high-impact claims;
- accept only decision-ready items into the decision queue;
- update boundary register/worklog/sync summary;
- commit and push when Git write access is available.
