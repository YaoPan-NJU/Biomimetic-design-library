# Audit: superhydrophobic-artificial

## Summary
- Total mechanisms: 76
- Total performance_data: 8
- Total design_translation: 0
- Issues found: 2

## Findings

### [F1] Fluoropolymer membrane mechanisms (polym14245439) not superhydrophobic-adsorption
- **Type**: wrong-source / translation-scope
- **Severity**: medium
- **Location**: mechanisms[19-24] (indices 19 through 24); engineering_constraints[0]
- **Evidence**: mechanisms[19-24] cite DOI 10.3390/polym14245439 ("Fluoropolymer Membranes for Membrane Distillation and Membrane Crystallization"). These describe: (19) Teflon AF 2400 PVDF VMD performance, (20) hydrophobic modification methods, (21) PVDF-co-HFP/POTS membrane, (22) PVDF-co-HFP/F-POSS omniphobic membrane, (23) Cassie-Baxter equation for membranes, (24) P(VDF-co-CTFE) FOMA membrane. These are membrane distillation technologies, not superhydrophobic adsorption foam. engineering_constraints[0] ("P(VDF-co-HFP) VMD stability") also cites this DOI.
- **Cross-ref**: Decision-queue B04-SHART-004 (keep_soft, applied 2026-06-17): "DOI 10.3390/polym14245439 is membrane-distillation evidence, not adsorption-foam capacity evidence."
- **Recommended disposition**: Add scope_caveat "membrane distillation, not adsorption foam" to mechanisms[19-24] and engineering_constraints[0], or remove them from this prototype. B04-SHART-004 already flags this as keep_soft.

### [F2] General superhydrophobic review mechanisms from refuted DOIs
- **Type**: wrong-source
- **Severity**: low
- **Location**: mechanisms[25-32] (indices 25 through 32)
- **Evidence**: mechanisms[25-32] cite DOI 10.1021/acsami.0c18794 (refuted for fish-scale-hydroxyapatite). These describe: special wettability classification, lotus effect principle, lotus upper/lower surface differences, gecko foot adhesion, rose petal high adhesion, THF/water dip-coating, sol-gel textile durability, material preparation summary. While these were refuted as wrong-source for fish-scale-HAp, they are arguably relevant to superhydrophobic-artificial as general superhydrophobic background. However, some (gecko, rose-petal) are off-topic for artificial superhydrophobic materials.
- **Cross-ref**: Refuted-log for fish-scale-hydroxyapatite (these DOIs were wrong-source there).
- **Recommended disposition**: Keep mechanisms[25-26,28-32] as general superhydrophobic theory (relevant to this prototype). Remove mechanisms[27] (gecko foot) and consider mechanism for rose petal as off-topic. Add scope_caveat: "general superhydrophobic review, not superhydrophobic-adsorption-specific."

## Clean areas
- performance_data[0-7]: All 8 performance rows cite legitimate superhydrophobic adsorption patents (CN121130847A, CN113244892B) with proper locators. No refuted DOIs found. Boundary rules B04-SHART-001 and B04-SHART-002 are appropriate.
- mechanisms[0-18]: Legitimate superhydrophobic artificial surface mechanisms from 10.16865/j.cnki.1000-7555.2020.0282 (superhydrophobic preparation review) and CN113244892B/CN121130847A patents. These describe PTFE coating, TiO2 fabric, SAS/silica sol-gel, HBCSM aerogel, metal rubber, femtosecond-laser PTFE, porous SiO2 nanofiber, PI/CA/F-PB/SNP fiber, Cu(OH)2 coating, all-water-based spray, diatomite mesh, candle-soot/SiO2 mesh, HAPNWs paper, PDA/FA foam, PDA cotton, PDMS rain-impact -- all relevant to superhydrophobic artificial materials.
- mechanisms[33-76]: Mixed general superhydrophobic content (separation mechanisms, antibacterial surfaces, copper-based antimicrobial, etc.). Most are relevant to superhydrophobic artificial materials. No refuted DOIs found.
- engineering_constraints[1-7]: Legitimate patent-derived constraints (diazotized MOF foam cycling, biochar foam preparation, pH stability, recyclability, ionic strength stability).
