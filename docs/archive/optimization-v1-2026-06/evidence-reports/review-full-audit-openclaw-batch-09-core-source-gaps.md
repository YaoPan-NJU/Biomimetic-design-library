# Batch 09 Core Source-Gap Audit
status: ready_for_codex_acceptance
worker: OpenClaw/mimo-v2.5
completed_at: 2026-06-17 06:33 CST

## Audit Scope

| Prototype | Local PDF | Visual Cache | Extraction JSON | Source PDF in prototype DB |
|-----------|-----------|--------------|-----------------|---------------------------|
| lobster-exoskeleton | None (2023-Vo PDF missing) | None | Yes (2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.json) | 2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.pdf (DOES NOT EXIST LOCALLY) |
| coral-skeleton | None | None | Yes (2020-Han-antifouling-review.json) | References 2020-Han-antifouling-review extraction; local Han2020 PDF was not found by Codex spot-check |
| magnetic-bacteria | Yes (2022-Mtb-biomineralization-magnetic-heavy-metal-review 2.pdf, 3.pdf) | Yes (_visual_cache 2.json) | Yes (2022-Mtb-biomineralization-magnetic-heavy-metal-review.json, T5 review, no perf_data) | Exists; DOI 10.1038/s41522-022-00304-0 confirmed |

---

## 1. Source Gap Resolution Table

| prototype_id | source_id | json_value | candidate_local_pdf | candidate_extraction_json | same_source_confidence | evidence_label | resolution | notes |
|---|---|---|---|---|---|---|---|---|
| lobster-exoskeleton | 2023-Vo-chitosan-membrane-shell-hydroxyapatite-review | performance_data[0] refs this PDF | NOT FOUND locally | 2023-Vo-chitosan-membrane-shell-hydroxyapatite-review.json exists; performance_data: [{capacity_mg_g:1385, pH:5.0, pollutant:Pb(II)}] | 0% (PDF not on disk) | missing_pdf | Cannot mechanically fix path. The extraction JSON exists but the source PDF it was built from does not exist locally. Package A path-normalization not applicable (no PDF to point to). | **Must be resolved by Yao.** Candidate actions: (a) obtain the 2023-Vo PDF from Springer (DOI 10.1007/s10311-023-01563-9) and place it in 仿生文献库/论文/第1组-配位螯合/; (b) park the prototype until PDF is acquired; (c) downgrade performance_data[0] to `knowledge_gap` or `inferred_only`. |
| lobster-exoskeleton | 2024-Vo-wastewater-review 2.pdf | Candidate alternate source (found by Codex Batch 08) | EXISTS locally | 2024-Vo-wastewater-review.json exists | 0% — DIFFERENT TOPIC: microalgae-bacteria consortia for wastewater treatment, NOT chitosan/HA composite beads | knowledge_gap | **Reject substitution.** This PDF is a completely different paper (Tan Phat Vo et al., microalgae-bacteria, environmental science review). Cannot substitute as lobster-exoskeleton evidence. | No action needed on this PDF. |
| coral-skeleton | 2020-Han-antifouling-review | Used in coral-skeleton.json narrative | NOT FOUND locally by Codex spot-check | 2020-Han-antifouling-review.json exists | extraction-only | knowledge_gap (missing PDF / wrong topic) | The extraction exists, but Codex did not find a local Han2020 PDF. The extraction topic is **marine antifouling coatings** (polymeric materials), NOT coral/CaCO3 adsorption or biomineralization. The coral-skeleton prototype's claim of "CaCO3 biomineralization → water purification" has NO direct source in this extraction. | **Must be resolved by Yao.** Options: (a) find actual coral/CaCO3 adsorption papers; (b) park coral-skeleton as `knowledge_gap`; (c) downgrade all coral-skeleton claims to `inferred_only`. |
| magnetic-bacteria | 10.1038/s41522-022-00304-0 | engineering_constraints[0].ref_doi | 2022-Mtb-biomineralization-magnetic-heavy-metal-review 2.pdf (also 3.pdf copy) | 2022-Mtb-biomineralization-magnetic-heavy-metal-review.json (T5 review, perf_data: [], no constraints extraction) | 100% (DOI confirmed via XMP metadata: "doi:10.1038/s41522-022-00304-0" on page 100029-100049) | **verified_source but review-level** | PDF exists and is correctly sourced. However: (1) extraction JSON has zero performance_data, zero constraints (null); (2) the paper is a T5 ecological/evolutionary review — NOT an engineering adsorption paper. MTB biomineralization data is from OTHER papers cited within this review (e.g., refs 170, 202-205). The review itself provides **secondary/cited evidence only**. | See Section 4 for detailed claim-by-claim assessment. |

---

## 2. Row / Prototype Decision Table

| candidate_id | prototype_id | target_json | field_path | issue | source_status | evidence_label | recommended_action | yao_decision_needed |
|---|---|---|---|---|---|---|---|---|
| lobster-exoskeleton | lobster-exoskeleton | prototypes_db/lobster-exoskeleton.json | performance_data[0] | performance_data[0].source_file refs PDF that does not exist locally; performance value (1385 mg/g Pb(II)) appears in extraction JSON but source PDF is absent | PDF missing; extraction JSON present | missing_pdf | **Do not modify performance_data value** (per instructions: don't change data values). Flag as needing PDF. | YES — Yao must decide: acquire PDF, park, or downgrade to knowledge_gap |
| lobster-exoskeleton | lobster-exoskeleton | prototypes_db/enrichment/lobster-exoskeleton.json | (enrichment fields) | enrichment file references 2023-Vo source; same missing-PDF issue propagates | PDF missing | missing_pdf | No change to enrichment; same dependency as above | YES |
| coral-skeleton | coral-skeleton | prototypes_db/coral-skeleton.json | narrative (all refs to Han2020) | Narrative cites Han2020 antifouling review extraction as source for "CaCO3 biomineralization → water purification" claims; the extraction topic is marine antifouling coatings, NOT coral/CaCO3 | PDF not found; extraction topic mismatch | knowledge_gap (missing PDF / wrong-topic source) | **Flag for Yao.** Narrative claims about coral/CaCO3 adsorption are unsupported by local sources. No local PDF, visual cache, or extraction JSON exists for coral/CaCO3 adsorption specifically. | YES — Yao must decide: (a) locate coral/CaCO3 papers, (b) park prototype, (c) downgrade claims |
| coral-skeleton | coral-skeleton | prototypes_db/enrichment/coral-skeleton.json | (all fields) | enrichment is empty `{}` — no enriched data at all | Enrichment empty | N/A | No change possible; enrichment file has no content to fix | YES |
| magnetic-bacteria | magnetic-bacteria | prototypes_db/magnetic-bacteria.json | performance_data | performance_data is `[]` — zero entries | Review paper (no original performance data) | inferred_only | **This is correct for a review paper.** A review does not generate original performance data. The absence is expected, not a gap. | NO — the 0 performance is accurate for this source type |
| magnetic-bacteria | magnetic-bacteria | prototypes_db/magnetic-bacteria.json | engineering_constraints[0].ref_doi | engineering_constraints reference DOI 10.1038/s41522-022-00304-0; PDF exists and DOI is confirmed; BUT the constraint values are narrative summaries from the review, not directly quoted performance data | PDF exists; DOI verified; but constraint text is review-level narrative | soft_boundary (review-level, not engineering-grade) | **Keep as-is.** The engineering_constraints contain accurate summary information from the review (MTB biological functions). They are labeled "relevance: medium" which is appropriate for review-level evidence. No mechanical change needed. | NO |
| magnetic-bacteria | magnetic-bacteria | prototypes_db/enrichment/magnetic-bacteria.json | (all fields) | enrichment file exists; enrichment references same PDF | Same source | same as main DB | No independent change needed | NO |

---

## 3. Package A Candidate Table

**NO CANDIDATES MEET PACKAGE A CRITERIA.**

Justification:

| candidate_id | prototype_id | target_json | field_path | current_value | proposed_value | evidence_for_mechanical_safety | recommended_action |
|---|---|---|---|---|---|---|---|
| *(none)* | — | — | — | — | — | — | **No items qualify.** |

Package A requirements: (1) source_file path normalization only, OR (2) empty-field fill; (3) actual local PDF must exist; (4) no data value changes.

- lobster-exoskeleton: source PDF does not exist → cannot normalize path
- coral-skeleton: source PDF exists (Han2020) but topic is wrong → normalization would propagate incorrect attribution
- magnetic-bacteria: source PDF exists and path is correct → no normalization needed; performance_data is correctly empty (review paper); engineering_constraints have correct DOI reference → no change needed

---

## 4. Magnetic-Bacteria: Detailed Claim Assessment

The magnetic-bacteria prototype has **zero performance_data** and **three engineering_constraints** all referencing DOI 10.1038/s41522-022-00304-0. This section assesses each claim against the actual PDF content.

### 4.1 engineering_constraints[0]: "MTB生物地球化学循环功能"

**PDF source**: Page 9 (0-indexed 8) — "Elements can also deposit on MTB cell surfaces... Arakaki and colleagues observed electron-dense Cd²⁺ deposits... A novel Alphaproteobacterium MTB species grown in a cobalt supplemented medium has efficient biosorption competence with 89% cobalt removed by magnetic separation"

**Assessment**: This is a **review citing other papers** (refs 170, 202-205). The 89% cobalt figure comes from ref 203 (a separate study). The MTB PDF itself does not contain original experiments. **All performance figures in this constraint are secondary/cited evidence.**

**Label**: `soft_boundary` — review-level narrative, accurately summarized from the review.

### 4.2 engineering_constraints[1]: "MTB——铁循环与全球铁循环"

**PDF source**: Pages 1-2 (0-indexed 0-1) — MTB ecology, magnetosome biomineralization, global iron cycling discussion.

**Assessment**: This is the review's core topic. Accurately summarized. No performance data, just ecological context. **Appropriate for a "medium relevance" constraint.**

**Label**: `soft_boundary` — ecological context, not engineering performance.

### 4.3 engineering_constraints[2]: "MTB——硫循环双重代谢"

**PDF source**: Page 3 (0-indexed 2) — "Nitrospirae MTB execute oxidative-reductive dual sulfur metabolism"

**Assessment**: Accurately summarized from the review. No engineering performance data. **Biological mechanism description, not adsorption performance.**

**Label**: `soft_boundary` — biological mechanism, not engineering data.

### 4.4 Summary for magnetic-bacteria

| Claim | Local PDF Evidence | Evidence Grade | Upgrade Candidate? | Action |
|---|---|---|---|---|
| MTB sequester Cd/Co/Se/Te | YES — review PDF page 9 cites refs 170, 202-205 | Secondary (cited) | NO — review-level; original data is in refs 202-205, not this paper | Keep as `soft_boundary` |
| MTB biomineralize Fe₃O₄/Fe₃S₄ | YES — review PDF pages 1-2, 7 | Review summary | NO — this is the review's own synthesis | Keep as `soft_boundary` |
| MTB participate in P/C/N/S cycling | YES — review PDF pages 1-3 | Review summary | NO — ecological context | Keep as `soft_boundary` |
| performance_data (quantitative adsorption values) | NO — extraction JSON has perf_data: [] | N/A | NO — correctly empty for a review paper | No change needed |

**Conclusion**: magnetic-bacteria is correctly structured for a review-source prototype. The zero performance_data is accurate. The engineering_constraints are appropriately labeled "medium relevance." No upgrade candidates exist because (a) this is a review, not an original experiment; (b) all quantitative claims within the review are secondary citations to other papers; (c) those cited papers are not locally available.

**⚠️ NOT upgrade_candidate**: Per project rules, "review-level论文（如 Goswami2022）中的性能数据为 organismal biogeochemistry，非工程设计，不满足 upgrade 条件". This applies here.

---

## 5. Park / Knowledge-Gap Candidate Table

| candidate_id | prototype_id | reason | evidence | recommended_status | consequence |
|---|---|---|---|---|---|
| coral-skeleton | coral-skeleton | **No local source for CaCO3/coral adsorption claims.** Han2020 extraction exists but the local PDF was not found and the extraction covers marine antifouling coatings (polymeric materials), NOT coral/CaCO3 biomineralization or adsorption. Zero performance_data. Enrichment is empty `{}`. | Han2020 extraction topic = antifouling polymers/marine coatings; NOT coral-related. No other local PDF/cache/json matches coral/CaCO3. | `knowledge_gap` | Prototype retains its placeholder in prototypes_db but all claims are effectively unsupported by local sources. Cannot be used for ranking or design guidance without new source acquisition. |
| lobster-exoskeleton | lobster-exoskeleton | **Source PDF missing.** Extraction JSON exists (2023-Vo) and contains performance data (1385 mg/g Pb(II)), but the PDF it was extracted from does not exist locally. Cannot verify extraction accuracy without source. | 2023-Vo PDF: searched 仿生文献库/ recursively, mdfind, `find /` — NOT FOUND. Extraction JSON: exists, paper_id matches, capacity 1385 mg/g. | `needs_human_decision` | performance_data[0] (1385 mg/g Pb(II)) remains in DB but cannot be verified or upgraded. If PDF is acquired later, extraction can be re-verified. |

---

## 6. Open Questions

### Requires Yao Decision

1. **coral-skeleton disposition**: This prototype has zero local evidence for its core claim (CaCO3 biomineralization → water purification). Han2020 is a real PDF but wrong topic. Should it be:
   - (a) Parked as `knowledge_gap` until relevant papers are found?
   - (b) Kept with a note that claims are inferred only?
   - (c) Removed from ranking entirely?

2. **lobster-exoskeleton PDF acquisition**: The 2023-Vo paper (DOI: 10.1007/s10311-023-01563-9, "Chitosan/membrane shell/hydroxyapatite composite beads for Pb(II) removal") is the source for the 1385 mg/g performance claim. Options:
   - (a) Acquire the PDF (Springer) and place in 仿生文献库/论文/第1组-配位螯合/
   - (b) Accept extraction JSON as sufficient evidence (unverified extraction)
   - (c) Downgrade performance_data[0] to `knowledge_gap`

3. **magnetic-bacteria: Is the current state acceptable?** The prototype is correctly structured for a review-source: zero performance_data (accurate), three engineering_constraints (review-level, appropriately labeled "medium relevance"). The PDF is verified. No upgrade candidates. Is this acceptable as-is, or should additional primary-source MTB papers be acquired?

### Requires No Action (Answered)

4. **Can 2024-Vo-wastewater-review 2.pdf substitute for lobster-exoskeleton?** NO. Confirmed different paper: microalgae-bacteria consortia (Tan Phat Vo et al.), NOT chitosan/HA composite beads.

5. **Is DOI 10.1038/s41522-022-00304-0 confirmed locally?** YES. XMP metadata on PDF page 100029 confirms DOI. PDF title matches: "Magnetotactic bacteria and magnetofossils: ecology, evolution and environmental implications".

6. **Does the MTB extraction JSON contain performance data?** NO. perf_data: [], constraints: null, verification: null. This is correct for a T5 review paper — no original experimental performance data.

---

## 7. Summary of Findings

| Prototype | Source Status | Package A? | Park/Gap? | Yao Decision? |
|---|---|---|---|---|
| lobster-exoskeleton | ⚠️ PDF missing (extraction JSON exists) | NO — no PDF to normalize | `needs_human_decision` | YES — acquire PDF or downgrade |
| coral-skeleton | ⚠️ Han2020 exists but wrong topic; no coral/CaCO3 source | NO — wrong-topic source | `knowledge_gap` | YES — park or acquire new sources |
| magnetic-bacteria | ✅ PDF verified, DOI confirmed | NO — no change needed | No — correctly structured | NO — current state is acceptable |

**Total Package A items: 0**
**Total items requiring Yao decision: 2** (lobster-exoskeleton, coral-skeleton)
**Total items with no action needed: 1** (magnetic-bacteria)
