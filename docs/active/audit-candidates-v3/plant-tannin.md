# Audit: plant-tannin

## Summary
- Total mechanisms: 12
- Total performance_data: 15
- Total design_translation: 1
- Issues found: 3

## Findings

### [F1] Fluoropolymer membrane contamination in mechanisms[0-5]
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[0-5] (indices 0 through 5)
- **Evidence**: All six mechanisms cite DOI 10.3390/polym14245439 ("Fluoropolymer Membranes for Membrane Distillation and Membrane Crystallization"). These describe PVDF VMD performance, hydrophobic modification methods, PVDF-co-HFP/POTS membrane, F-POSS omniphobic membrane, Cassie-Baxter equation for membranes, and P(VDF-co-CTFE) FOMA membrane. None relate to plant-tannin adsorption.
- **Cross-ref**: Refuted-log lines 146-151 (wrong_source); Decision-queue B01-PLT-001 (guard_rule, applied 2026-06-17); B04-SHART-004 (keep_soft, applied 2026-06-17)
- **Recommended disposition**: Remove mechanisms[0-5] entirely. Guard rule B01-PLT-001 already applies but data appears not yet removed from JSON.

### [F2] Corrosion inhibitor mechanism outside adsorption scope
- **Type**: translation-scope
- **Severity**: medium
- **Location**: mechanisms[11] (index 11)
- **Evidence**: Mechanism describes DOLE corrosion inhibition on X70 steel in 0.5M H2SO4 (DOI 10.1016/j.indcrop.2022.116106). This is acid corrosion protection, not water-treatment adsorption. The verification_quote confirms: "DOLE contains a large number of hydroxyl groups...coordinate with the empty d orbital of Fe, which leads to the formation of chemical adsorption of DOLE at X70 steel."
- **Cross-ref**: Decision-queue B01-PLT-002 (soft_boundary, applied 2026-06-17)
- **Recommended disposition**: Add scope_caveat "corrosion inhibitor, not water-treatment adsorption" or remove if strict adsorption scope is enforced.

### [F3] Fluoropolymer membrane contamination in engineering_constraints and narrative
- **Type**: wrong-source
- **Severity**: high
- **Location**: engineering_constraints[0]; narrative.entries[0]
- **Evidence**: engineering_constraints[0] ("P(VDF-co-HFP) VMD stability") cites DOI 10.3390/polym14245439 (fluoropolymer membrane review). narrative.entries[0] is sourced from the same Li2022 fluoropolymer membrane review extraction JSON and describes membrane distillation concepts, not plant-tannin adsorption.
- **Cross-ref**: Refuted-log line 155 (wrong_source for engineering_constraints); Decision-queue B01-PLT-001 (guard_rule)
- **Recommended disposition**: Remove engineering_constraints[0] and narrative.entries[0] (or reassign to a membrane-separation prototype if applicable).

## Clean areas
- performance_data[0-14]: All 15 performance rows cite legitimate tannin-related sources (Yao2021, Zhu2022, Mao2024, Yuan2024) with proper verification quotes and locators. No refuted DOIs found.
- mechanisms[6-10]: Legitimate plant-tannin adsorption mechanisms (catechol-metal chelation, Cr(VI) reduction, BPA hydrogen bonding, Cu(II) chelation, CR Schiff base). All cite appropriate sources with verification quotes.
- design_translation: Source tier is llm_inference, which is acceptable. Content aligns with tannin catechol group chemistry.
