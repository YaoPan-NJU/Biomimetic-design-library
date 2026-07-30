# Audit: shark-skin

## Summary
- Total mechanisms: 31
- Total performance_data: 0
- Total design_translation: 0
- Issues found: 3

## Findings

### [F1] Non-shark-skin mechanisms (gecko, rose-petal, lotus)
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[5,6] (indices 5 and 6)
- **Evidence**: mechanism[5] ("壁虎脚仿生特性") describes gecko-foot adhesion via aligned setae and van der Waals forces. mechanism[6] ("玫瑰花瓣高黏附超疏水") describes rose-petal micro-papillae array producing high-adhesion superhydrophobicity. Neither relates to shark-skin antifouling or microstructure.
- **Cross-ref**: No specific decision-queue item, but B04-SHART-003 establishes that non-shark/non-lotus biological examples should not be mixed.
- **Recommended disposition**: Remove mechanisms[5,6] as off-topic for shark-skin. These belong to gecko or rose-petal prototypes.

### [F2] Wrong-source mechanisms from refuted superhydrophobic reviews
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[2,3,4,7,8,9,10,11,12,13] (10 mechanisms)
- **Evidence**: mechanisms[2-4] cite DOI 10.1021/acsami.0c18794 (refuted for fish-scale-hydropyapate). These describe: special wettability classification, lotus effect principle, lotus upper/lower surface wetting differences -- all about lotus leaf and general superhydrophobicity, not shark-skin. mechanisms[7-13] also cite the same DOI and describe: THF/water dip-coating, sol-gel textile durability, material preparation summary table, TiO2 photocatalysis, CeO2 nanoparticle film, pH-responsive PDMS-bP4VP electrospinning, UV+pH stimuli-responsive switching -- all general superhydrophobic surface fabrication, not shark-skin antifouling.
- **Cross-ref**: Refuted-log entries for fish-scale-hydroxyapatite (DOI 10.1021/acsami.0c18794 is wrong_source there); B04-SHARK-001 knowledge_gap rule.
- **Recommended disposition**: Remove mechanisms[2-4,7-13]. These are general superhydrophobic surface reviews, not shark-skin-specific evidence.

### [F3] General superhydrophobic theory without shark-skin specificity
- **Type**: translation-scope
- **Severity**: medium
- **Location**: mechanisms[14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30]
- **Evidence**: Multiple mechanisms describe general superhydrophobic concepts (wetting thresholds, PDMS adhesion, ice formation, self-cleaning, anti-corrosion, etc.) from DOIs 10.33263/BRIAC132.185, 10.3390/polym15030543, etc. While some mention shark-skin tangentially (mechanisms[17,18] mention shark antifouling), most are general superhydrophobic material science. mechanism[29] ("自然界九种超疏水生物原型") lists 9 organisms including shark-skin but is a general overview.
- **Cross-ref**: B04-SHARK-001: "Zero performance rows and mostly generic antifouling/superhydrophobic mechanisms."
- **Recommended disposition**: Keep only mechanisms that specifically discuss shark-skin microstructure (Sharklet, dermal denticle riblets). Remove or relocate general superhydrophobic theory mechanisms.

## Clean areas
- mechanisms[0-1]: Legitimate shark-skin-adjacent antifouling content (surface wettability effect on bacterial adhesion, long/short-range interaction thresholds).
- mechanisms[17-18]: Mention shark-skin antifouling specifically (natural antifouling organisms including shark dermal denticles, antifouling short-lived nature).
- provenance_summary: Correctly shows n_verified: 0, status: parked_separation, with note "scope: background-only, no direct shark-skin adsorption performance."
