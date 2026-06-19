# Audit: sulfate-reducing-bacteria

## Summary
- Total mechanisms: 1
- Total performance_data: 0
- Total design_translation: 1
- Total engineering_constraints: 4
- Total narrative entries: 8
- Issues found: 1

## Findings

### [F1] Wrong-source engineering_constraints[1-3]
- **Type**: wrong-source
- **Severity**: high
- **Location**: engineering_constraints[1] (line 235-243), [2] (line 244-252), [3] (line 253-261)
- **Evidence**: All three constraints cite ref_doi = "10.7524/j.issn.0254-6108.2020050901". This DOI is from an iron-cycling microorganisms review (Qian2021), not an SRB-specific source. The constraints describe: (1) iron-cycle As remediation factors, (2) specific Cr(VI) reduction by Acidiphilium/Acidocella, (3) iron-oxidizing bacteria removing Cr/Cu/Zn/Ni/Pb from sludge. These are iron-oxidizing/reducing bacteria mechanisms, not sulfate-reducing bacteria.
- **Cross-ref**: Refuted-log confirms 10.7524/j.issn.0254-6108.2020050901 is wrong_source for SRB. B03-SRB-002 (guard_rule applied).
- **Recommended disposition**: Remove all 3 rows (guard_rule already applied in decision queue)

## Clean areas
- mechanisms[0]: Legitimate Kumar2021 source on SRB sulfate reduction mechanism (verified)
- engineering_constraints[0]: Legitimate PSEP2024 source on SRB sulfur cycling
- narrative.entries[0-7]: All 8 entries cite legitimate SRB-related sources (Kumar2021, Zhu2021, Miao2021, Li2022, Zhang2022, Wang2022, Zhao2022, Wen2022, Diao2023, Li2023, Novair2024)
- design_translation: LLM-inference (correctly labeled)
- No label contradictions found
- No performance_data exists (status = needs_literature for performance)
