# Review Next-Stage Approval Summary

status: pending_yao_approval
date: 2026-06-16
branch: review
last_pushed_checkpoint: c4abb95

## Current State

- Evidence review docs are pushed through `c4abb95` on `origin/review`.
- OpenClaw targeted audits accepted so far: parked/registry, MOF verification semantics, DNA aptamer, diatom path/dedup, and starch extreme-value sanity check.
- `prototypes_db/*.json` has not been modified in this review stage.
- `tools/build_prototypes_db.py` has not been run.
- All queued edits remain approval-gated in `review-full-audit-decision-queue.md` and `review-boundary-do-not-register.md`.

## Can Continue

Yes. The next stage can continue, but it should switch from broad OpenClaw auditing to controlled cleanup packages. The evidence base is now strong enough to prepare edits, but not to apply them automatically without Yao approval because many changes alter ranking, provenance confidence, or prototype scope.

## Recommended Approval Packages

### Package A: Low-Risk Mechanical Cleanup

Approve these first because they mostly improve traceability without changing scientific meaning.

- Normalize known `source_file` path mismatches after confirming actual local PDFs.
- Remove exact duplicate rows already confirmed in diatom performance, mechanisms, constraints, and narrative entries.
- Fill missing pollutant fields only where the source quote is direct and unambiguous, such as plant-tannin BPA, wood-xylem phenol/chlorophenols/heavy metals, bone Cu(II), and oyster phosphate.
- Add quote/locator metadata for already supported rows without upgrading verification labels beyond the approved evidence grade.

Residual risk: low, provided each edit preserves the original source grade and does not promote inferred evidence.

### Package B: Clear Wrong-Source Removal Or Reassignment

Approve these when Yao is ready to remove contamination from direct prototype evidence.

- MOF: remove or reassign Aramesh pure-chitosan rows, Cheng membrane/BPA rows, Yan polydopamine rows, and exclude MOF-5 H2 storage from aqueous adsorption ranking.
- Fish-scale HAp: remove or reassign superwetting/membrane/Janus blocks and marine-shell/abalone rows that are not fish-scale HAp evidence.
- Chlorella: remove unrelated CaO, nZVI, magnetic graphene, and silica nanoparticle technology rows from Chlorella cell-wall evidence.
- Mycelium: remove or reassign cellulose, nanocellulose, lignin, PFAS, and oil rows unless the prototype scope is explicitly expanded.
- Plant-tannin: remove or reassign Li2022 fluoropolymer membrane-distillation items.
- Bone-structure: remove or reassign Chen2021 MOF dye/Cr(VI) review rows.
- Diatom: replace the Guo2022 Pb XPS source mismatch with Du2021, and replace microalgae cell-wall template wording in diatomite mineral-surface mechanisms.

Residual risk: medium. These edits improve correctness, but they change counts and may affect rankings/provenance summaries.

### Package C: Ranking Safety And Metric Demotion

Approve these before using the library for performance ranking or design recommendation.

- Starch: demote concentration-dependent uptake ranges and review-wide maxima from generic qmax ranking.
- Starch: convert or annotate mmol/g rows before comparing them with mg/g rows.
- Starch: isolate oil/aerogel/cryogel/hydrogel extreme values from generic starch-granule aqueous adsorption.
- DNA aptamer: exclude biosensor LOD/Kd values from adsorption capacity/removal performance.
- MOF: reinterpret `single_source` and `n_verified`; do not treat them as quote-and-locator verification.
- Material-reference set: require source grade, metric type, and material scope normalization before comparing with biological prototypes.

Residual risk: medium-high. These decisions change how downstream ranking and recommendations should interpret the database.

### Package D: Boundary And DO-NOT Register Application

Approve these after Package B/C, because boundaries should match the cleaned evidence.

- Apply only evidence-graded `hard_do_not` entries with direct source/domain support.
- Keep missing PDFs, scanned patents, inferred placeholders, and figure-only values as `knowledge_gap` or `needs_human_decision`.
- Apply `soft_boundary` as caveats, not exclusion rules.
- Keep DO-NOT rules visible in the library so downstream users know which source/prototype transfers are invalid.

Residual risk: medium. This is valuable for design reliability, but hard boundaries should remain conservative.

### Package E: Human Decisions Required

These need Yao's explicit decision before edits.

- Namib beetle: keep parked, retire, or require a dedicated evidence rebuild before promotion.
- DNA aptamer: whether to accept CN121588773A figure-derived adsorption capacity around 35 mg/g, or keep only textual Kd/application evidence.
- Diatom Arachnoidiscus wheel-hub paper: move to future structural-mechanics prototype, keep as soft narrative, or remove from adsorption-focused diatom.
- MOF chitosan-MOF hybrids from Aramesh: keep in MOF with hybrid/review caveat, move to chitosan/composite scope, or require primary-source verification.
- Fish-scale biochar rows: expand fish-scale HAp scope to fish-scale-derived biochar, or move rows elsewhere.
- Wood apple shell biochar rows: keep under wood-xylem with caveat, or move/narrow to biomass biochar evidence.
- Starch engineered oil sorbent/aerogel/cryogel/hydrogel rows: keep under starch-granule with class caveat, or split to engineered starch adsorbent/oil-sorbent scope.
- Mangrove root: keep constructed-wetland/system removal metrics as soft system evidence, or exclude from material adsorption ranking.

## Proposed Execution Order

1. Ask Yao to approve Package A, then apply mechanical cleanup in small commits.
2. Ask Yao to approve Package B, then remove or reassign wrong-source rows and update affected provenance notes.
3. Ask Yao to approve Package C, then add ranking-safety labels or demotions.
4. Ask Yao to decide Package E items, then handle scope changes one prototype family at a time.
5. Apply Package D boundaries only after the relevant evidence rows are cleaned.
6. Run validation and rebuild scripts only after Yao explicitly approves database edits.

## Not Approved Yet

- No automatic edits to `prototypes_db/*.json`.
- No automatic verification upgrades.
- No hard boundary upgrades from inferred-only, missing-PDF, scanned-patent, or figure-only evidence.
- No automatic build/regeneration of the prototype database.

