# Audit: spider-silk

## Summary
- Total mechanisms: 26
- Total performance_data: 4
- Total design_translation: 1
- Issues found: 3

## Findings

### [F1] Femtosecond-laser/superhydrophobic mechanisms spillover
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[15-21] (indices 15 through 21)
- **Evidence**: Seven mechanisms cite DOI 10.34133/2022/9895418 (femtosecond laser superwettability review). These describe: (15) wetting theory (Young/Wenzel/Cassie), (16) femtosecond-laser silicon superhydrophobic, (17) PDMS femtosecond-laser superhydrophobic, (18) PTFE femtosecond-laser durability, (19) PDMS multi-state wetting switching, (20) SLIPS NiTi blood compatibility, (21) femtosecond-laser universal wetting rules. None are spider-silk-specific; they describe laser-processed inorganic surfaces.
- **Cross-ref**: Decision-queue B14-SPIDER-001 (scope_mismatch, applied 2026-06-17): "Broad superhydrophobic, femtosecond-laser, uranium-coordination, and general wetting-review mechanisms should not be treated as spider-silk-specific."
- **Recommended disposition**: Remove mechanisms[15-21] or relocate to a general-superhydrophobic prototype. Guard rule B14-SPIDER-001 already flags this.

### [F2] Uranium coordination chemistry mechanisms not spider-silk
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[22-25] (indices 22 through 25)
- **Evidence**: Four mechanisms cite DOI 10.1016/j.ccr.2023.215234 (uranium coordination chemistry review). These describe: (22) uranyl ion coordination chemistry, (23) amidoxime coordination modes, (24) ligand optimization strategies, (25) dual-function synergy strategies. These are uranium extraction chemistry, not spider-silk biology.
- **Cross-ref**: B14-SPIDER-001 scope_mismatch rule covers this.
- **Recommended disposition**: Remove mechanisms[22-25]. These belong to a uranium-extraction or general-adsorption-chemistry prototype.

### [F3] Desert beetle fog-harvesting mechanism not spider-silk
- **Type**: wrong-source
- **Severity**: medium
- **Location**: mechanisms[14] (index 14)
- **Evidence**: Mechanism cites DOI 10.1002/adfm.202200359 and describes "Namib desert beetle fog water collection mechanism" -- hydrophilic bumps capture fog droplets, hydrophobic channels direct transport. This is about Namib beetle, not spider silk.
- **Cross-ref**: B14-SPIDER-001 scope_mismatch.
- **Recommended disposition**: Remove mechanism[14]. This belongs to a Namib-beetle or fog-harvesting prototype.

## Clean areas
- performance_data[0-3]: Legitimate spider-silk-inspired CNF/PEI@GOA fiber adsorption data from Zhou2021 with verified status and proper figures.
- mechanisms[0-1]: Legitimate spider-silk mechanisms (metal doping/CNT composites, electrospinning fiber morphology).
- mechanisms[2-13]: Mixed. mechanisms[2-5] are electrospinning/Janus fabric mechanisms from Li2021 (10.1007/s40242-021-0010-4) -- these are electrospinning review content, borderline for spider-silk. mechanisms[8-13] are legitimate spider-silk or CNF/PEI@GOA fiber mechanisms (antifouling, Cr XPS, Cd XPS, fiber formation, specialization-cooperation, spider silk biomimetic inspiration).
- design_translation: Source tier is llm_inference (acceptable). Content about spidroin amide/carboxyl groups aligns with spider-silk biology.
