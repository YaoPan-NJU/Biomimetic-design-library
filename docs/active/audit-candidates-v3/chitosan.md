# Chitosan Audit Report

**File**: `prototypes_db/chitosan.json`
**Date**: 2026-06-19
**Auditor**: Claude Code

## Summary Counts

| Section | Count |
|---------|-------|
| performance_data | 117 |
| mechanisms | 132 |
| design_translation | 1 |
| engineering_constraints | 60 |
| narrative_entries | 44 |
| **Total refuted DOI hits** | **42** (18 perf + 22 mech + 2 ec) |

## Verification Distribution

### mechanisms
| Level | Count |
|-------|-------|
| needs_review | 130 |
| verified | 2 |

### performance_data
| Level | Count |
|-------|-------|
| partial | 63 |
| verified | 46 |
| needs_review | 6 |
| unverified | 2 |

## Refuted DOI Contamination

Three refuted DOIs are present in this file:

| Refuted DOI | Source Type | Perf Hits | Mech Hits | EC Hits |
|-------------|-------------|-----------|-----------|---------|
| `10.1016/j.ijbiomac.2021.04.158` | Dye-removal review (Aramesh2021) | 14 (indices 22-35) | 2 (13-14) | 0 |
| `10.16490/j.cnki.issn.1001-3660.2023.02.015` | Chinese superhydrophobic membrane review | 0 | 10 (76-85) | 0 |
| `10.1016/j.cej.2024.149414` | BPA/membrane composite review (Cheng2024) | 4 (76-79) | 10 (90-99) | 2 (35-36) |

---

## Findings

### [F1] Dye-removal review contamination in performance_data
- **Type**: wrong-source
- **Severity**: high
- **Location**: `performance_data[22]` through `performance_data[35]` (14 entries)
- **Evidence**: All 14 entries have `ref_doi: "10.1016/j.ijbiomac.2021.04.158"`, sourced from `2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf`. This is a generic chitosan dye-removal review. While the entries do involve chitosan-based materials, the DOI is in the refuted list as a wrong-source token. The entries themselves describe chitosan composites for dye adsorption (RBR, MB, SO, CR, DY, AR, MG, SY, FA94, DR80), which are within chitosan scope but are secondhand review citations rather than primary sources.
- **Cross-ref**: Refuted DOI `10.1016/j.ijbiomac.2021.04.158` is on the refuted list
- **Recommended disposition**: Candidate for `wrong_source` removal OR re-annotate with primary source DOIs (the review cites original studies). These are chitosan-relevant data but cited through a review rather than primary literature. If the review is a legitimate chitosan source, the ref_doi may need removal from the refuted list; if the refuted classification is correct, these 14 entries should be removed or re-sourced.

### [F2] Superhydrophobic/membrane mechanisms in chitosan
- **Type**: wrong-source / scope-contamination
- **Severity**: high
- **Location**: `mechanisms[76]` through `mechanisms[85]` (10 entries)
- **Evidence**: All 10 entries have `ref_doi: "10.16490/j.cnki.issn.1001-3660.2023.02.015"` and describe:
  - [76] lotus leaf superhydrophobicity mechanism
  - [77-79] superwetting membrane separation mechanisms (emulsion oil/water)
  - [80-84] specific membrane materials (TiO2/PVDF/PDMS/PMMA/PNIPAAm)
  - [85] superwetting membrane classification
  None of these are chitosan-related. They describe PVDF, PDMS, PMMA, PNIPAAm, TiO2 membranes -- no chitosan involvement. This is clear wrong-source contamination from a Chinese review on superhydrophobic membrane separation.
- **Cross-ref**: Refuted DOI `10.16490/j.cnki.issn.1001-3660.2023.02.015`
- **Recommended disposition**: Remove all 10 mechanisms. They belong to a membrane/separation prototype (possibly `superhydrophobic-artificial` or a dedicated membrane prototype), not chitosan.

### [F3] BPA/membrane review contamination in mechanisms
- **Type**: wrong-source / scope-contamination
- **Severity**: high
- **Location**: `mechanisms[90]` through `mechanisms[99]` (10 entries)
- **Evidence**: All 10 entries have `ref_doi: "10.1016/j.cej.2024.149414"` and describe BPA adsorption on activated carbon, carbon nanotubes, and membrane separation (NF/MF/UF/RO). Topics include: activated carbon surface properties, CNT adsorption, DFT/MD simulation, membrane separation efficiency. None mention chitosan as the primary adsorbent material. The source file is `2024-Cheng-chitosan-cellulose-separation-membrane-review.pdf` -- a chitosan/cellulose membrane review, but these specific mechanisms describe non-chitosan materials.
- **Cross-ref**: Refuted DOI `10.1016/j.cej.2024.149414`
- **Recommended disposition**: Remove all 10 mechanisms. The review paper may contain some chitosan-relevant content, but these 10 extracted mechanisms describe generic BPA adsorption on AC/CNT/membranes, not chitosan-specific mechanisms.

### [F4] BPA/membrane review contamination in performance_data
- **Type**: wrong-source / scope-contamination
- **Severity**: high
- **Location**: `performance_data[76]` through `performance_data[79]` (4 entries)
- **Evidence**: All 4 entries have `ref_doi: "10.1016/j.cej.2024.149414"`:
  - [76] Activated carbon BPA adsorption capacity (>250 mg/g, PDA-C 1351 mg/g) -- not chitosan
  - [77] NF membrane BPA removal mechanism -- not chitosan
  - [78] MF membrane BPA removal mechanism -- not chitosan
  - [79] UF-AOP coupling BPA removal -- not chitosan
  All are verified with no verification_quote. The source is a chitosan/cellulose separation membrane review, but these performance data points describe non-chitosan materials.
- **Cross-ref**: Refuted DOI `10.1016/j.cej.2024.149414`
- **Recommended disposition**: Remove all 4 performance_data entries.

### [F5] BPA/membrane review contamination in engineering_constraints
- **Type**: wrong-source / scope-contamination
- **Severity**: medium
- **Location**: `engineering_constraints[35]` and `engineering_constraints[36]`
- **Evidence**: Both have `ref_doi: "10.1016/j.cej.2024.149414"`:
  - [35] pH effect on BPA adsorption (generic, not chitosan-specific)
  - [36] Temperature effect on BPA adsorption (generic, not chitosan-specific)
  These are generic BPA adsorption constraints from a membrane review, not chitosan-specific engineering constraints.
- **Cross-ref**: Refuted DOI `10.1016/j.cej.2024.149414`
- **Recommended disposition**: Remove or re-source. If chitosan-specific pH/temperature constraints exist in other sources, replace with those.

### [F6] Verified performance_data entries without verification_quote
- **Type**: ledger-inaccuracy
- **Severity**: medium
- **Location**: `performance_data` indices 3, 4, 15, 16, 46-54, 57-60, 65, 73, 74, 76-79 (24 entries total)
- **Evidence**: 24 performance_data entries have `verification: "verified"` but no `verification_quote` field. Per evidence-quality standards, "verified" requires a direct text quote from the source. Without a quote, these should be `partial` (single-source with quote) or `needs_review` (no quote). Notable clusters:
  - Indices 3-4: Bambaeero2020 chitosan bone/shell (no quote)
  - Indices 15-16: Xu2020 chitosan-cellulose (no quote)
  - Indices 46-54: 10.1007/s10924-021-02312-1 ENM review (no quote)
  - Indices 57-60: 10.1007/s13762-021-03603-9 electrospun review (no quote)
  - Indices 76-79: refuted CEJ review (no quote, also wrong-source -- see F4)
- **Cross-ref**: Ledger inaccuracy -- `provenance_summary.n_verified = 115` likely overcounts
- **Recommended disposition**: Downgrade all 24 entries from `verified` to `needs_review` (or add verification_quote to upgrade them properly). The 4 entries at indices 76-79 should be removed entirely (see F4).

### [F7] Design_translation source_tier is llm_inference
- **Type**: label-contradiction
- **Severity**: low
- **Location**: `design_translation[0]`
- **Evidence**: The single design_translation entry has `source_tier: "llm_inference"`. This is internally consistent (not contradicted by a "verified" label), but it means the design translation is ungrounded in literature. The entry describes chitosan amino/hydroxyl group complexation with pH-responsive adsorption/desorption, which is chemically plausible but not sourced from any specific paper.
- **Cross-ref**: None
- **Recommended disposition**: Accept as-is with caveat that design_translation is LLM-generated. Optionally ground in a specific chitosan modification review (e.g., Upadhyay2020 or Alves2021).

### [F8] 130/132 mechanisms lack source_file
- **Type**: ledger-inaccuracy
- **Severity**: medium
- **Location**: `mechanisms` (130 out of 132 entries)
- **Evidence**: Only 2 mechanisms have `source_file` populated. The remaining 130 have no `source_file`, making it impossible to trace claims back to local PDFs. This severely limits auditability. The two with source_file are both verified with quotes (indices from carbpol.2020.117000 and carbpol.2021.118625).
- **Cross-ref**: None
- **Recommended disposition**: For each mechanism, add `source_file` pointing to the local PDF. This is a bulk metadata gap.

### [F9] 23 performance_data entries lack ref_doi
- **Type**: ledger-inaccuracy
- **Severity**: low
- **Location**: `performance_data` (23 out of 117 entries have no `ref_doi`)
- **Evidence**: These entries have `source: "literature"` but no DOI. Some have source_file but no DOI. Without a DOI, the source cannot be independently verified.
- **Cross-ref**: None
- **Recommended disposition**: Add ref_doi where the source_file is known. For entries where the source is genuinely untraceable, mark as `knowledge_gap`.

### [F10] Provenance_summary n_verified likely inflated
- **Type**: ledger-inaccuracy
- **Severity**: low
- **Location**: `provenance_summary`
- **Evidence**: `provenance_summary.n_verified = 115` but verification distribution shows only 2 mechanisms are "verified" and 46 performance_data are "verified" (total 48). The n_verified count may include "partial" entries or may be stale from a previous build. Additionally, 24 of the 46 "verified" performance entries lack verification_quote (see F6), so true verified count is at most 22.
- **Cross-ref**: None
- **Recommended disposition**: Recompute provenance_summary from actual field states. True verified count (with quote) is approximately 2 (mechanisms) + 22 (performance) = 24.

---

## Clean Areas

- **performance_data[0-21]**: All from legitimate chitosan sources (Zhang2019, Bambaeero2020, Catenza2020, Sheth2020, Upadhyay2020, Xu2020). No refuted DOIs.
- **performance_data[36-75]**: All from legitimate chitosan sources (various chitosan review and primary papers). No refuted DOIs.
- **performance_data[80-116]**: All from legitimate chitosan sources. No refuted DOIs.
- **mechanisms[0-12]**: Legitimate chitosan mechanisms from various sources. No refuted DOIs.
- **mechanisms[15-75]**: Legitimate chitosan mechanisms. No refuted DOIs.
- **mechanisms[86-89]**: Legitimate chitosan mechanisms. No refuted DOIs.
- **mechanisms[100-131]**: Legitimate chitosan mechanisms. No refuted DOIs.
- **engineering_constraints[0-34]** and **[37-59]**: Legitimate chitosan constraints. No refuted DOIs.
- **No llm_inference entries** found in mechanisms or performance_data (clean on label contradictions).
- **No cross-prototype contamination** beyond the three refuted DOI clusters identified above.

---

## Summary of Recommended Actions (DO NOT apply)

| Finding | Action | Entries Affected |
|---------|--------|-----------------|
| F1 | Remove or re-source 14 dye-removal review perf_data | perf[22-35] |
| F2 | Remove 10 superhydrophobic/membrane mechanisms | mech[76-85] |
| F3 | Remove 10 BPA/membrane review mechanisms | mech[90-99] |
| F4 | Remove 4 BPA/membrane review perf_data | perf[76-79] |
| F5 | Remove 2 BPA/membrane review engineering_constraints | ec[35-36] |
| F6 | Downgrade 24 "verified" entries to "needs_review" | perf[3,4,15,16,46-54,57-60,65,73,74] |
| F7 | Accept LLM-generated design_translation as-is | dt[0] |
| F8 | Add source_file to 130 mechanisms | mech (bulk) |
| F9 | Add ref_doi to 23 perf_data entries | perf (bulk) |
| F10 | Recompute provenance_summary | provenance_summary |
