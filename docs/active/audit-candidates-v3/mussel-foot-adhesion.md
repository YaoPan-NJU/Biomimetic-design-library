# Mussel-Foot-Adhesion Audit Report

**File**: `prototypes_db/mussel-foot-adhesion.json` (2602 lines)
**Audit date**: 2026-06-19
**Auditor**: Claude Code (automated)

---

## Data Counts

| Field | Count |
|-------|-------|
| performance_data | 46 |
| mechanisms | 88 |
| design_translation | 2 |
| engineering_constraints | 29 |
| narrative entries | 11 |
| **Total verifiable entries** | **176** |

---

## Findings

### [F1] Refuted DOI 10.1021/acsami.0c18794 — 23 mechanisms are oil-water separation content, not mussel adhesion
- **Type**: wrong-source / scope contamination
- **Severity**: high
- **Location**: `mechanisms[0]` through `mechanisms[22]`
- **Evidence**: All 23 mechanisms cite `ref_doi: "10.1021/acsami.0c18794"` (Zheng2020, "Advanced Materials with Special Wettability toward Intelligent Oily Wastewater Separation", ACS AMI). Content includes: lotus leaf effect, gecko foot adhesion, rose petal superhydrophobicity, TiO2 photocatalysis, CeO2 nanoparticles, PDMS-bP4VP electrospun membranes, UV+pH switchable wettability, 6 natural superwetting materials, oil-water separation classification, ZnO nanorod cotton, CVD graphene aerogel, PANI/TiO2 mesh, Co-coordination self-healing fabric, sol-gel PDMS@SiO2 durability. NONE of these relate to mussel-foot-adhesion (DOPA/catechol/PDA adhesion chemistry).
- **Cross-ref**: refuted-log item for 10.1021/acsami.0c18794
- **Recommended disposition**: Remove all 23 mechanisms. They belong in a superhydrophobic/special-wettability prototype, not mussel-foot-adhesion. **DO NOT apply.**

### [F2] Refuted DOI 10.1021/acsami.0c18794 — 4 engineering constraints are oil-water separation content
- **Type**: wrong-source / scope contamination
- **Severity**: high
- **Location**: `engineering_constraints[0]` through `engineering_constraints[3]`
- **Evidence**: All 4 constraints cite `ref_doi: "10.1021/acsami.0c18794"`. Content: Fe3+-PA/OTMS/PI electrospun membrane flux (8424 L/m2h), PTFE stainless steel felt WCA, PANI/TiO2 mesh oil flux (170 kL/m2h), UV+pH responsive membrane switching. These are oil-water separation membrane performance metrics, not mussel adhesion constraints.
- **Cross-ref**: refuted-log item for 10.1021/acsami.0c18794
- **Recommended disposition**: Remove all 4 constraints. **DO NOT apply.**

### [F3] Refuted DOI 10.1016/j.apsusc.2022.154338 — 2 mechanisms from Yan2022 PDA/MGO dye study
- **Type**: wrong-source
- **Severity**: medium
- **Location**: `mechanisms[85]` (pHpzc和pH影响), `mechanisms[86]` (吸附机理六重协同)
- **Evidence**: Both cite `ref_doi: "10.1016/j.apsusc.2022.154338"` (Yan2022, PDA/MGO/CA-CD cationic dye adsorption). Content describes pHpzc=4.32 and six-fold synergistic adsorption mechanism (electrostatic, hydrogen bonding, Yoshida H-pi, pi-pi conjugation, n-pi, beta-CD host-guest). While PDA is mussel-inspired, this paper is primarily about dye adsorption performance on a PDA/MGO/CA-CD composite, and the DOI is on the refuted list.
- **Cross-ref**: refuted-log item for 10.1016/j.apsusc.2022.154338
- **Recommended disposition**: Remove or re-evaluate. If PDA/MGO/CA-CD is considered a legitimate PDA derivative, the mechanisms could be retained with a scope caveat. **DO NOT apply.**

### [F4] Refuted DOI 10.1016/j.apsusc.2022.154338 — 2 performance_data entries from Yan2022
- **Type**: wrong-source
- **Severity**: medium
- **Location**: `performance_data[37]` (MB最大吸附容量 1372.32 mg/g), `performance_data[38]` (MG 822.39 mg/g, CV 570.79 mg/g)
- **Evidence**: Both cite `ref_doi: "10.1016/j.apsusc.2022.154338"`. These are PDA/MGO/CA-CD dye adsorption capacities. The DOI is on the refuted list.
- **Cross-ref**: refuted-log item for 10.1016/j.apsusc.2022.154338
- **Recommended disposition**: Remove or re-evaluate with scope caveat. **DO NOT apply.**

### [F5] Refuted DOI 10.1016/j.apsusc.2022.154338 — 2 engineering_constraints from Yan2022
- **Type**: wrong-source
- **Severity**: medium
- **Location**: `engineering_constraints[23]` (循环再生性能 8次循环), `engineering_constraints[24]` (TGA热稳定性)
- **Evidence**: Both cite `ref_doi: "10.1016/j.apsusc.2022.154338"`. These describe cycling stability and thermal stability of PDA/MGO/CA-CD composite.
- **Cross-ref**: refuted-log item for 10.1016/j.apsusc.2022.154338
- **Recommended disposition**: Remove or re-evaluate. **DO NOT apply.**

### [F6] Refuted DOI 10.1021/acsami.0c18794 — narrative entry from Zheng2020 extraction
- **Type**: wrong-source / scope contamination
- **Severity**: medium
- **Location**: `narrative.entries[0]` (paper_id: "2020-Zheng-special-wettability-oily-wastewater-review")
- **Evidence**: The source_file points to `2020-Zheng-self-cleaning-separation-wastewater-water-treatment-review.json` which corresponds to the same Zheng2020 review cited as 10.1021/acsami.0c18794. The narrative content discusses oil-water separation (lotus leaf, fish scale, mussel PDA as one of many topics), not specifically mussel-foot-adhesion.
- **Cross-ref**: refuted-log item for 10.1021/acsami.0c18794
- **Recommended disposition**: Remove this narrative entry. **DO NOT apply.**

### [F7] Provenance summary counts do not match actual field states
- **Type**: ledger-inaccuracy
- **Severity**: low
- **Location**: `provenance_summary` (n_papers: 27, n_verified: 33, n_unverified: 115)
- **Evidence**: Actual counts: performance_data has 23 verified + 7 partial + 16 unverified = 46; mechanisms has 2 verified + 86 needs_review = 88. Total verified across perf+mechanisms = 25 (not 33). The discrepancy of 8 suggests the provenance_summary may count engineering_constraints or causal_chain sub-fields, but this is not documented and the numbers are misleading.
- **Cross-ref**: N/A
- **Recommended disposition**: Recount and update provenance_summary to accurately reflect field-level verification states. **DO NOT apply.**

### [F8] Two mechanisms have null descriptions
- **Type**: data-quality
- **Severity**: low
- **Location**: `mechanisms[76]` (PDA吸附机制-姜黄素), `mechanisms[77]` (PDA吸附机制-番茄红素)
- **Evidence**: Both have `"description": null`. These are patent-derived mechanisms (CN115040496A) about PDA hollow mesoporous nanoparticles for fat-soluble pigment delivery. The null descriptions mean the mechanism content is missing.
- **Cross-ref**: N/A
- **Recommended disposition**: Fill in descriptions from the patent extraction or mark as knowledge_gap. **DO NOT apply.**

### [F9] Mechanism verification_quote is title/abstract snippet, not specific text excerpt
- **Type**: ledger-inaccuracy
- **Severity**: low
- **Location**: `mechanisms[25]` (PDA自聚合形成机制), verification: "verified"
- **Evidence**: The verification_quote is "dopamine self-polymerization into thin, surface-adherent polydopamine films onto a wide range of inorganic and organic materials" — this is a general description of the paper's topic, not a specific text excerpt that verifies the mechanism description (which describes the detailed polymerization pathway through dopamine quinone, leukodopaminechrome, 5,6-DHI, etc.). The quote confirms the general concept but not the specific mechanistic details.
- **Cross-ref**: N/A
- **Recommended disposition**: Downgrade to "partial" or obtain a more specific quote from the Lee2007 PDF. **DO NOT apply.**

### [F10] design_translation[1] is ungrounded LLM inference
- **Type**: label-contradiction
- **Severity**: low
- **Location**: `design_translation[1]` (amidoxime groups for uranium adsorption)
- **Evidence**: `source_tier: "llm_inference"` with `examples: []` (empty). The concept is valid (amidoxime chemistry for uranium capture is well-established), but it has no supporting DOI or example references. This makes it an ungrounded claim in the design_translation section.
- **Cross-ref**: N/A
- **Recommended disposition**: Add a supporting reference (e.g., the Liu2024 review 10.1016/j.ccr.2023.215234 that is already cited in mechanisms) or mark as needs_source. **DO NOT apply.**

### [F11] Massive scope contamination — 34 of 176 entries (19.3%) from refuted sources
- **Type**: wrong-source / scope contamination
- **Severity**: high
- **Location**: Aggregate across file
- **Evidence**: The prototype conflates "mussel-foot-adhesion" (DOPA/catechol/PDA adhesion chemistry) with "polydopamine coating derivatives" and "oil-water separation superhydrophobic materials". Of 176 total entries, 34 (19.3%) reference refuted DOIs:
  - 23 mechanisms from oil-water separation review (10.1021/acsami.0c18794)
  - 4 engineering constraints from same review
  - 1 narrative entry from same review
  - 2 mechanisms from PDA/MGO dye study (10.1016/j.apsusc.2022.154338)
  - 2 performance_data entries from same study
  - 2 engineering constraints from same study
- **Cross-ref**: refuted-log items for both DOIs
- **Recommended disposition**: Perform scope split. The legitimate mussel-foot-adhesion content should be separated from oil-water separation content. **DO NOT apply.**

---

## Scope Contamination Summary

The prototype has three distinct content domains that have been incorrectly merged:

### Domain A: Legitimate Mussel-Foot-Adhesion (should remain)
- PDA self-polymerization mechanism (Lee2007, mechanisms[25])
- PDA coating adhesion mechanism (Lee2007, mechanisms[50])
- PDA vs traditional coating comparison (mechanisms[26])
- Dopamine-assisted co-deposition (mechanisms[27])
- Zwitterion hydration (mechanisms[23-24])
- Patent-derived PDA mechanisms (mechanisms[70-77])
- All PDA-based performance_data entries (patents CN105413659B, CN113042006A, CN114849661A, CN115055171A, CN114570339A, CN115040496A)
- PDA-composite performance_data (Foroutan2021, Shi2021, Xiao2021, Zhang2021, Yan2022, Jin2023, Xiang2023)
- design_translation[0] (DOPA catechol surface functionalization)

### Domain B: Oil-Water Separation (should be removed or moved)
- mechanisms[0-22] from 10.1021/acsami.0c18794 (23 mechanisms)
- engineering_constraints[0-3] from same source (4 constraints)
- narrative.entries[0] from same extraction
- mechanisms[30-32] from 10.1016/j.carbpol.2022.120242 (hydrophobic modification review)
- mechanisms[33-40] from 10.1002/smll.202204624 (superwetting review, 8 mechanisms)
- mechanisms[56-62] from 10.1021/acsnano.5c01252 (smart membranes, 7 mechanisms)
- mechanisms[63-69] from 10.1021/acsnano.4c18335 (polymer brushes, 7 mechanisms)
- engineering_constraints[4-6] from various oil-water separation sources

### Domain C: Uranium Adsorption (borderline, needs scope caveats)
- mechanisms[41-47] from 10.1016/j.ccr.2023.215234 (uranium adsorption review, 7 mechanisms)
- design_translation[1] (amidoxime chemistry, llm_inference)

---

## Clean Areas

The following entries are clean (no refuted DOIs, proper labels):

- **PDA core mechanisms**: mechanisms[25] (verified, Lee2007), mechanisms[50] (verified, Lee2007)
- **PDA coating review**: mechanisms[26-27] (10.1039/d1cs00658d, needs_review)
- **PDA superhydrophobic review**: mechanisms[51-55] (10.1039/d5su00041f, needs_review)
- **Adsorption force mechanisms**: mechanisms[28-29] (10.1016/j.cej.2021.129237, needs_review)
- **MI-PDA mechanisms**: mechanisms[48-49] (10.1016/j.apcatb.2023.122852, needs_review)
- **Patent-derived PDA mechanisms**: mechanisms[70-77] (patents, needs_review)
- **Verified performance_data**: perf[0] (SMX removal), perf[12] (CN115055171A cycling), perf[13-18] (HAp/Fe3O4/PDA metals), perf[19-21] (MnO2/PDA/Fe3O4 Pb), perf[22-28] (COF@PDA metals), perf[29] (Gd aerogel), perf[39] (PDA/DCS carmine), perf[40] (Ge adsorption)
- **Partial performance_data**: perf[30-36] (CN114570339A uranium)
- **design_translation[0]**: DOPA catechol functionalization (Lee2007)
- **All narrative entries except [0]**: PDA-specific narratives from legitimate extractions

---

## Summary Statistics

| Category | Total | Refuted | Clean |
|----------|-------|---------|-------|
| mechanisms | 88 | 25 (28.4%) | 63 |
| performance_data | 46 | 2 (4.3%) | 44 |
| engineering_constraints | 29 | 6 (20.7%) | 23 |
| design_translation | 2 | 0 (0%) | 2 |
| narrative entries | 11 | 1 (9.1%) | 10 |
| **Total** | **176** | **34 (19.3%)** | **142** |

**Top refuted source**: 10.1021/acsami.0c18794 — 28 entries (23 mechanisms + 4 constraints + 1 narrative)
**Second refuted source**: 10.1016/j.apsusc.2022.154338 — 6 entries (2 mechanisms + 2 perf_data + 2 constraints)
