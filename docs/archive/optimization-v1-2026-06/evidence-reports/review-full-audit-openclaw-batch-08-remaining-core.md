---
status: ready_for_codex_acceptance
worker: OpenClaw/mimo-v2.5
completed_at: 2026-06-17 06:21 CST
batch: 08-remaining-core
scope:
  - prototypes_db/coral-skeleton.json
  - prototypes_db/lobster-exoskeleton.json
  - prototypes_db/magnetic-bacteria.json
  - prototypes_db/pitcher-plant-slippery-surface.json
  - prototypes_db/spider-silk.json
hard_limits:
  do_not_modify_prototypes_db_json: true
  do_not_run_build_prototypes_db: true
  do_not_change_verification_hard_do_not_soft_boundary: true
  do_not_git_commit: true
  do_not_modify_protected_docs_or_tools: true
notes: >
  Evidence preflight only. This audit is intentionally partial rather than a full line-by-line verification.
  It focuses on evidence-map construction, source-file traceability, likely Package A candidates,
  wrong-source/scope-mismatch exposure, enrichment mirror gaps, and Yao-decision hotspots.
---

# Batch 08 remaining core prototypes — targeted evidence preflight

## 1) Audit scope and method

This preflight inspects:

- `prototypes_db/coral-skeleton.json`
- `prototypes_db/lobster-exoskeleton.json`
- `prototypes_db/magnetic-bacteria.json`
- `prototypes_db/pitcher-plant-slippery-surface.json`
- `prototypes_db/spider-silk.json`
- corresponding enrichment files under `prototypes_db/enrichment/`
- local assets under `仿生文献库/` and `tools/litextract/outputs/extractions/`

Method:

1. Count `performance_data`, `mechanisms`, `narrative.entries`, and `engineering_constraints`.
2. Extract all `source_file`, `paper_id`, `ref_doi`, and explicit `source` fields.
3. Check whether each source maps to a local PDF, visual cache, or extraction JSON.
4. Flag zero-data prototypes, empty enrichment mirrors, mismatched provenance summaries, narrative/source-file normalization defects, and mechanism rows that are literature-review sweep rather than spider-silk-specific evidence.
5. Separate mechanical-safe Package A candidates from semantic/judgment items requiring Yao decision.

All edits are audit-only; no prototype JSONs, protected docs, or protected tools were modified.

## 2) Prototype Coverage Table

| prototype_id | target_json | performance_count | mechanism_count | constraint_count | narrative_count | provenance_summary_status | enrichment_status | overall_risk | notes |
|---|---|---|---|---|---|---|---|---|---|
| coral-skeleton | prototypes_db/coral-skeleton.json | 0 | 1 | 0 | 1 | mismatch | empty mirror | high | zero performance; narrative source is antifouling review, not coral CaCO3 adsorption; coverage=low |
| lobster-exoskeleton | prototypes_db/lobster-exoskeleton.json | 1 | 1 | 3 | 1 | plausible but incomplete | hollow causal_chain | medium | local PDF missing; enrichment causal chain is empty despite target JSON having text |
| magnetic-bacteria | prototypes_db/magnetic-bacteria.json | 0 | 1 | 3 | 1 | mismatch | empty mirror | high | zero performance; narrative is mineralization/review, not adsorption performance |
| pitcher-plant-slippery-surface | prototypes_db/pitcher-plant-slippery-surface.json | 1 | 22 | 1 | 4 | mismatch | hollow mirror rows | high | most mechanism rows are non-pitcher wetting/superhydrophobic/Janus scope creep |
| spider-silk | prototypes_db/spider-silk.json | 4 | 31 | 3 | 4 | mismatch | hollow mirror rows | very high | large sweep-literature spill; PDF traceability normalized but enrichment has zero filled causal chains |

## 3) Source Availability Table

| prototype_id | source_id | json_source_value | local_pdf | visual_cache | extraction_json | readability | source_status | notes |
|---|---|---|---|---|---|---|---|---|
| coral-skeleton | narrative entry | tools/litextract/outputs/extractions/论文/json/2020-Han-antifouling-review.json | none | none | exists | extraction-only | missing_pdf | source does not support coral-skeleton CaCO3 claim |
| lobster-exoskeleton | perf 0 | 仿生文献库/论文/第1组-配位螯合/2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.pdf | missing exact match | missing | exists | extraction-only | bare_filename_mismatch | local duplicate likely exists as `... 2.pdf` |
| lobster-exoskeleton | mechanism 0 | ref_doi 10.1016/j.polymer.2020.123316 | none | none | none | unknown | missing_pdf | local PDF not found |
| magnetic-bacteria | narrative entry | tools/litextract/outputs/extractions/论文/json/2022-Mtb-biomineralization-magnetic-heavy-metal-review.json | 2 local PDFs | visual cache exists | exists | pdf+visual+json | supported_in_local | narrative content is review-level, not performance-rich |
| magnetic-bacteria | constraints | ref_doi 10.1038/s41522-022-00304-0 | none | none | none | unknown | missing_pdf | constraint provenance exists but no local PDF |
| pitcher-plant-slippery-surface | perf 0 | 2021-Zeng-antifouling-porous-review.pdf | missing exact match | multiple caches | exists | cache+extraction | bare_filename_mismatch | local duplicate likely `... 2.pdf` |
| pitcher-plant-slippery-surface | mechanism 0-9 | ref_doi 10.1007/s42242-021-00133-8 | missing exact match | multiple caches | exists | cache+extraction | bare_filename_mismatch | broad anti-fouling review spill |
| pitcher-plant-slippery-surface | mechanism 10-18 | ref_doi 10.1007/s40242-021-0010-4 | none | none | none | unknown | missing_pdf | wetting/membrane review spill |
| pitcher-plant-slippery-surface | mechanism 19-20 | ref_doi 10.1002/adfm.202200359 | none | none | none | unknown | missing_pdf | fog-harvesting review spill |
| pitcher-plant-slippery-surface | mechanism 21 | llm_inference | none | none | none | inferred | inferred_only | acceptable only if kept clearly marked |
| spider-silk | perf 0-3 | 仿生文献库/论文/第5组-纤维结构/2021-Zhou-cellulose-silk-nanofiber-adsorption.pdf | 2 local PDFs | visual cache exists | exists | pdf+visual+json | supported_in_local | local files normalized as `... 2.pdf` / `... 3.pdf` |
| spider-silk | narrative 1 | tools/litextract/outputs/extractions/论文/json/2021-Li-silk-hierarchical-shell-review.json | 1 local PDF | visual caches | exists | pdf+visual+json | supported_in_local | narrative is strong for spider-silk hierarchy |
| spider-silk | narrative 2 | tools/litextract/outputs/extractions/论文/json/2021-Zhang-silk-separation-membrane-porous.json | 2 local PDFs | visual caches | exists | pdf+visual+json | supported_in_local | likely good for silk separation angle |
| spider-silk | narrative 3 | tools/litextract/outputs/extractions/论文/json/2021-Zhou-cellulose-silk-nanofiber-adsorption.json | 2 local PDFs | visual cache | exists | pdf+visual+json | supported_in_local | strong for amphoteric bionic fibers |
| spider-silk | narrative 4 | tools/litextract/outputs/extractions/论文/json/2023-Li-antifouling-separation-porous-adsorption-review.json | no local PDF | visual cache exists | exists | cache+extraction | no_local_pdf | useful, but no direct local PDF confirmed |
| spider-silk | mechanisms (multiple) | ref_doi 10.34133/2022/9895418 | none | none | none | unknown | missing_pdf | superhydrophobic / femtosecond-laser scope creep |
| spider-silk | mechanisms (multiple) | ref_doi 10.1016/j.ccr.2023.215234 | none | none | none | unknown | missing_pdf | uranium-coordination review scope creep |
| spider-silk | mechanisms (multiple) | ref_doi 10.1007/s40242-021-0010-4 | none | none | none | unknown | missing_pdf | electrospun/Janus review scope creep |

## 4) High-Risk Row Table

| candidate_id | prototype_id | target_json | field_path | claim_summary | source_path_or_missing_status | locator | quote_or_quote_gap | evidence_label | recommended_action | yao_decision_needed |
|---|---|---|---|---|---|---|---|---|---|---|
| HR-01 | coral-skeleton | prototypes_db/coral-skeleton.json | performance_data[ ] | zero performance entries for coral CaCO3 adsorption | no PDF / no performance extraction found | gap | gap | missing_pdf | keep empty performance block; do not fabricate | yes |
| HR-02 | coral-skeleton | prototypes_db/coral-skeleton.json | narrative.entries[0].source_file | narrative sourced from antifouling review rather than coral CaCO3 adsorption paper | tools/litextract/outputs/extractions/论文/json/2020-Han-antifouling-review.json | mismatch | mismatch | scope_mismatch | mark narrative as low-relevance inspiration only, not direct coral-skeleton support | yes |
| HR-03 | coral-skeleton | prototypes_db/coral-skeleton.json | mechanisms[0].source / verification | mechanism is llm_inference with needs_review, but may be misread as literature-backed | none | gap | gap | inferred_only | keep inferred, do not upgrade to verified | no |
| HR-04 | lobster-exoskeleton | prototypes_db/lobster-exoskeleton.json | performance_data[0].source_file | local path missing exact match | 仿生文献库/论文/第1组-配位螯合/2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.pdf | gap | gap | bare_filename_mismatch | normalize to local duplicate path (likely `... 2.pdf`) | no |
| HR-05 | lobster-exoskeleton | prototypes_db/lobster-exoskeleton.json | performance_data[0] / lobster scope | performance is chitosan/HAP review data, not lobster-specific adsorption performance | extraction JSON exists; no lobster-specific PDF | gap | gap | inferred_only | keep only as review-derived, not organism-primary evidence | yes |
| HR-06 | lobster-exoskeleton | prototypes_db/lobster-exoskeleton.json | mechanisms[0].source_file | mechanism lacks local source file | ref_doi 10.1016/j.polymer.2020.123316 only | gap | gap | missing_pdf | add local PDF path when available | yes |
| HR-07 | lobster-exoskeleton | prototypes_db/enrichment/lobster-exoskeleton.json | mechanisms["Chitosan beads的六种吸附机制"].causal_chain.* | enrichment causal chain fields are empty | none | gap | gap | enrichment_mirror_gap | mirror target JSON causal_chain or mark as unresolved gap | no |
| HR-08 | magnetic-bacteria | prototypes_db/magnetic-bacteria.json | performance_data[ ] | zero performance entries | none | gap | gap | missing_pdf | keep empty; do not invent values | yes |
| HR-09 | magnetic-bacteria | prototypes_db/magnetic-bacteria.json | mechanisms[0].verification + source | mechanism is llm_inference but not marked clearly against literature-backed claims | none | gap | gap | inferred_only | keep inferred only | no |
| HR-10 | magnetic-bacteria | prototypes_db/magnetic-bacteria.json | engineering_constraints[0-2] | constraints trace to 10.1038/s41522-022-00304-0 but no local PDF found | ref_doi only | gap | gap | missing_pdf | retain provenance but flag missing local PDF | yes |
| HR-11 | pitcher-plant-slippery-surface | prototypes_db/pitcher-plant-slippery-surface.json | performance_data[0].source_file | local source file missing exact match and pollutant field empty | 2021-Zeng-antifouling-porous-review.pdf | gap | gap | bare_filename_mismatch | normalize path to local duplicate (likely `... 2.pdf`) and flag empty pollutant for Yao | yes |
| HR-12 | pitcher-plant-slippery-surface | prototypes_db/pitcher-plant-slippery-surface.json | mechanisms[1-18] | non-pitcher wetting, Janus, electrospinning, membrane, fog-harvesting mechanisms imported into pitcher-plant prototype | multiple missing local PDFs | gap | gap | scope_mismatch / wrong_source | candidate for removal or relocation to separation/anti-fouling shared pool | yes |
| HR-13 | pitcher-plant-slippery-surface | prototypes_db/pitcher-plant-slippery-surface.json | mechanisms[21] | Nepenthes SLIPS mechanism is llm_inference | none | gap | gap | inferred_only | keep clearly marked as inferred | no |
| HR-14 | pitcher-plant-slippery-surface | prototypes_db/enrichment/pitcher-plant-slippery-surface.json | multiple mechanism causal chains | enrichment rows exist but causal_chain text is empty | none | gap | gap | enrichment_mirror_gap | mirror target JSON or mark unresolved | no |
| HR-15 | spider-silk | prototypes_db/spider-silk.json | mechanisms | very large literature sweep (31 mechanisms), many non-silk sources | multiple missing local PDFs | gap | gap | scope_mismatch / wrong_source | relocate broad wetting/uranium/femtosecond mechanisms out of spider-silk prototype | yes |
| HR-16 | spider-silk | prototypes_db/spider-silk.json | performance_data[0-3].source_file | local files exist but stored as normalized duplicates | 仿生文献库/论文/第5组-纤维结构/2021-Zhou-cellulose-silk-nanofiber-adsorption 2.pdf / 3.pdf | gap | gap | bare_filename_mismatch | normalize source_file paths to actual local files | no |
| HR-17 | spider-silk | prototypes_db/spider-silk.json | provenance_summary | provenance count does not align with actual distinct sources referenced in JSON | target JSON only | mismatch | mismatch | provenance_summary_mismatch | recompute provenance after scope cleanup | yes |
| HR-18 | spider-silk | prototypes_db/enrichment/spider-silk.json | multiple mechanism causal chains | enrichment mirror fields empty | none | gap | gap | enrichment_mirror_gap | mirror target JSON or mark unresolved | no |

## 5) Package A Candidate Table

These are mechanical-safe edits only: path normalization, empty-enrichment mirroring, and precise duplicate marking.

| candidate_id | prototype_id | target_json | field_path | current_value | proposed_value | evidence_for_mechanical_safety | recommended_action |
|---|---|---|---|---|---|---|---|
| PA-01 | lobster-exoskeleton | prototypes_db/lobster-exoskeleton.json | performance_data[0].source_file | 仿生文献库/论文/第1组-配位螯合/2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.pdf | 仿生文献库/论文/第1组-配位螯合/2023-Vo-chitosan-membrane-shell-hydroxyapatite-review 2.pdf | exact local duplicate exists and no semantic change | normalize path |
| PA-02 | pitcher-plant-slippery-surface | prototypes_db/pitcher-plant-slippery-surface.json | performance_data[0].source_file | 2021-Zeng-antifouling-porous-review.pdf | 仿生文献库/论文/第2组-超疏水/2021-Zeng-antifouling-porous-review 2.pdf | exact local duplicate exists and no semantic change | normalize path |
| PA-03 | spider-silk | prototypes_db/spider-silk.json | performance_data[0-3].source_file | 仿生文献库/论文/第5组-纤维结构/2021-Zhou-cellulose-silk-nanofiber-adsorption.pdf | 仿生文献库/论文/第5组-纤维结构/2021-Zhou-cellulose-silk-nanofiber-adsorption 2.pdf | local duplicate exists; value/pollutant semantics unchanged | normalize paths |
| PA-04 | lobster-exoskeleton | prototypes_db/enrichment/lobster-exoskeleton.json | mechanisms["Chitosan beads的六种吸附机制"].causal_chain.* | empty strings | mirror target JSON causal_chain text only | no semantic upgrade; mirror only | sync causal chain text |
| PA-05 | pitcher-plant-slippery-surface | prototypes_db/enrichment/pitcher-plant-slippery-surface.json | multiple mechanism causal_chain.* | empty strings | mirror target JSON causal_chain text only where already present | no semantic upgrade; mirror only | sync causal chain text |
| PA-06 | spider-silk | prototypes_db/enrichment/spider-silk.json | multiple mechanism causal_chain.* | empty strings | mirror target JSON causal_chain text only where already present | no semantic upgrade; mirror only | sync causal chain text |

## 6) Boundary / DO-NOT Candidate Table

These are not automatic upgrades. They are scope/boundary items for Yao review.

| boundary_id | prototype_id | target_field | boundary_type_candidate | rationale | source | locator | quote | evidence_label | recommended_action |
|---|---|---|---|---|---|---|---|---|---|
| BN-01 | coral-skeleton | mechanisms[0] | needs_human_decision | entire performance-free CaCO3 claim currently rests on llm_inference | none | gap | gap | inferred_only | keep inferred only or remove core claim; do not mark as hard_do_not |
| BN-02 | lobster-exoskeleton | performance_data[0] | needs_human_decision | chitosan-review performance is useful but organism-specific provenance is weak | extraction JSON exists | gap | gap | inferred_only | keep with explicit review-derived scope tag |
| BN-03 | magnetic-bacteria | mechanisms[0] + performance_data[ ] | needs_human_decision | prototype has no performance data and only one inferred mechanism | extraction JSON exists for review | gap | gap | inferred_only | keep only if prototype scope is clearly labeled as mechanism-placeholder |
| BN-04 | pitcher-plant-slippery-surface | mechanisms[1-18] | wrong_source / scope_mismatch | non-pitcher wetting/superhydrophobic/Janus/fog mechanisms imported by sweep | multiple missing local PDFs | gap | gap | scope_mismatch | relocate to shared review pool or remove from pitcher-plant prototype |
| BN-05 | pitcher-plant-slippery-surface | performance_data[0] | needs_human_decision | performance row contains anti-icing removal-force metric with empty pollutant field | 10.1007/s42242-021-00133-8 | gap | gap | scope_mismatch | decide whether to keep anti-icing metric outside adsorption scope |
| BN-06 | spider-silk | mechanisms (multiple) | wrong_source / scope_mismatch | 31 mechanisms include superhydrophobic, femtosecond-laser, uranium-coordination, and general wetting review spill | multiple missing local PDFs | gap | gap | wrong_source / scope_mismatch | relocate broad review-derived mechanisms out of spider-silk |
| BN-07 | spider-silk | provenance_summary | needs_human_decision | provenance summary should be recomputed after cleanup | target JSON only | gap | gap | provenance_summary_mismatch | recompute after scope cleanup |

## 7) Open Questions

Only items that genuinely require Codex or Yao decision:

1. **Coral-skeleton scope**: should the prototype remain as a low-coverage placeholder with only antifouling-review narrative and zero performance, or be parked until a coral/CaCO3-adsorption source is added?
2. **Lobster-exoskeleton provenance semantics**: should chitosan-review performance be retained with explicit review-derived scope, or should organism-specific adsorption evidence be required?
3. **Magnetic-bacteria status**: should the prototype remain active with only inferred mechanism and zero performance?
4. **Pitcher-plant scope split**: should broad wetting/Janus/superhydrophobic/fog-harvesting mechanisms be removed from `pitcher-plant-slippery-surface` and moved to a shared review/evidence pool?
5. **Pitcher-plant anti-icing performance**: should the anti-icing removal-force row stay inside an adsorption-focused prototype?
6. **Spider-silk scope cleanup**: should non-silk mechanisms (uranium coordination, femtosecond laser, general wetting) be relocated to shared review evidence instead of spider-silk mechanisms?
7. **Spider-silk provenance recomputation**: after cleanup, should provenance summary be recomputed before Codex acceptance?
8. **Path normalization only**: for PA-01 / PA-02 / PA-03, is mechanical normalization to local `... 2.pdf` / `... 3.pdf` duplicates acceptable without further semantic review?

## 8) incomplete_sections

- No full-text PDF quote verification was performed for every row.
- Enrichment mirroring was checked as a gap audit only; no sync writes were made.
- High-risk rows are evidence-map flags, not final acceptance verdicts.

## 9) Recommendation summary

**Acceptable immediately (mechanical only):**

- Normalize local source_file paths where exact match is missing but duplicate exists.
- Mirror empty enrichment causal_chain text from target JSON where already present.
- Mark enrichment gaps as unresolved rather than fabricating content.

**Needs Yao/Codex decision:**

- coral-skeleton scope
- lobster-exoskeleton and magnetic-bacteria provenance semantics
- pitcher-plant and spider-silk scope relocation/removal
- recomputation of provenance summaries after cleanup

## 10) Final acceptance statement

The file above is the written audit deliverable required for this batch.
`status: ready_for_codex_acceptance`
