# Audit: fish-scale-hydroxyapatite

## Summary
- Total mechanisms: 89
- Total performance_data: 29
- Total design_translation: 1
- Total engineering_constraints: 12
- Total narrative entries: 10
- Issues found: 3 (categories), affecting 104 of 141 total fields (74%)
- Contaminated entries: 86 mechanisms + 7 performance_data + 11 engineering_constraints = 104

## Findings

### [F1] Massive wrong-source contamination from membrane/superhydrophobic reviews in mechanisms
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[0-15] (10.1007/s11783-021-1515-2, 10.1021/acsami.0c18794), mechanisms[16-33] (10.1021/acsami.0c18794), mechanisms[34-45] (10.34133/2022/9895418), mechanisms[46-55] (10.1002/smll.202204624), mechanisms[56-68] (10.1007/s10853-022-07945-8, 10.3390/membranes13080727, 10.16490/j.cnki.issn.1001-3660.2023.02.015), mechanisms[69-77] (10.16490/j.cnki.issn.1001-3660.2023.02.015), mechanisms[78-85] (additional refuted DOIs)
- **Evidence**: 86 of 89 mechanisms cite refuted DOIs from superhydrophobic/membrane/separation reviews. These cover topics entirely unrelated to fish-scale HAp adsorption:
  - Membrane classification, Janus membranes, oil-water separation (10.1007/s11783-021-1515-2)
  - Superhydrophobic surface fabrication, WCA measurements, PVDF/PDMS coatings (10.1021/acsami.0c18794)
  - Femtosecond laser surface texturing (10.34133/2022/9895418)
  - Superwetting theory, re-entrant geometry, SLIPS (10.1002/smll.202204624)
  - Superwetting membrane nanofiber reviews (10.1007/s10853-022-07945-8)
  - MD membrane performance (10.3390/membranes13080727)
  - Superwetting oil-water separation Chinese review (10.16490/j.cnki.issn.1001-3660.2023.02.015)
- **Cross-ref**: refuted-log lines 9-97: fish-scale-hydroxyapatite.json mechanisms[0-88] — all listed as wrong_source
- **Recommended disposition**: Remove 86 mechanisms with refuted DOIs. Retain only 3 clean mechanisms (from 10.1016/j.chemosphere.2021.131962 and CN113275374A). Note: mechanisms citing 10.1016/j.matlet.2021.130573 and 10.3969/j.issn.1672-7304.2024.02.0011 are also flagged as wrong-source for fish-scale (see F3).

### [F2] Wrong-source engineering_constraints from membrane/superhydrophobic reviews
- **Type**: wrong-source
- **Severity**: high
- **Location**: engineering_constraints[0-10] (all 11 entries)
- **Evidence**: All engineering_constraints cite refuted DOIs:
  - [0-1]: 10.1007/s10853-022-07945-8 (superhydrophobic membrane review)
  - [2]: 10.3390/membranes13080727 (MD membrane review)
  - [3-6]: 10.1007/s11783-021-1515-2 (cellulose superhydrophobic review)
  - [7-10]: 10.1021/acsami.0c18794 (superhydrophobic/oily wastewater review)
  - None of these relate to fish-scale HAp.
- **Cross-ref**: refuted-log lines 99-111: fish-scale-hydroxyapatite.json engineering_constraints[0-10]
- **Recommended disposition**: Remove all 11 engineering_constraints. They are all from wrong-source reviews. Only constraint[11] (regeneration performance from 10.1016/j.chemosphere.2021.131962) should be retained if present.

### [F3] Wrong-source performance_data entries (abalone shell + shell reviews)
- **Type**: wrong-source
- **Severity**: high
- **Location**: performance_data[22-28]
- **Evidence**:
  - [22-23]: Wang2021 abalone shell HA microspheres (10.1016/j.matlet.2021.130573) — abalone is not fish-scale
  - [24]: Zhang2024 calcined shell Pb adsorption (10.3969/j.issn.1672-7304.2024.02.0011) — general shell review
  - [25-26]: Zhang2024 shell-based HAp capacity/removal (same DOI) — general shell data
  - [27]: Zhang2024 Cd removal by shell powder (same DOI) — general shell data
  - [28]: Zhang2024 modified mussel shell Pb capacity (same DOI) — mussel shell, not fish-scale
- **Cross-ref**: refuted-log lines 113-121: fish-scale-hydroxyapatite.json performance_data[22-28]
- **Recommended disposition**: Remove performance_data[22-28]. These are abalone/shell data, not fish-scale HAp. The legitimate performance_data entries are [0-21] which cite fish-scale-specific sources (Dou2021, Wu2022, CN114849640A, CN113275374A).

## Clean areas
- mechanisms (3 clean): 八重协同吸附机制 (10.1016/j.chemosphere.2021.131962), 疏水相互作用证据 (same), MICP化学反应机理 (CN113275374A) — legitimate fish-scale/HAp sources
- performance_data[0-21]: Legitimate fish-scale/HAp data:
  - [0-1]: Dou2021 DPBC fish-scale biochar CIP adsorption
  - [2-6]: Wu2022 HA-3HPB fish-scale HAp biochar heavy metals
  - [7-17]: CN114849640A fish-scale HAp dye adsorption patent
  - [18-21]: CN113275374A biomineralization heavy metal patent
- design_translation[1]: HAp Ca²⁺/PO₄³⁻ adsorption — legitimate
- Narrative: 10 legitimate fish-scale/HAp narratives (Halim2022, Zheng2020, Dou2021, Yong2022, Mao2022, Yang2022, Tan2023, Jing2023 x2, CN114849640A)
- No label contradictions found
- No honesty_ledger present
