# Audit: silk-fibroin

## Summary
- Total mechanisms: 20
- Total performance_data: 22
- Total design_translation: 1
- Issues found: 3

## Findings

### [F1] Duplicated performance_data block
- **Type**: ledger-inaccuracy
- **Severity**: medium
- **Location**: performance_data[16-21] (indices 16 through 21)
- **Evidence**: performance_data[16-21] are exact duplicates of performance_data[11-15]. Both sets cite the same DOIs (Martis2022 10.1039/d1va00047k, Prasad2022 10.1016/j.eti.2022.102741) with the same values, locators, and quotes. This inflates provenance_summary.n_verified from 25 to what should be ~19 unique verified rows.
- **Cross-ref**: No specific decision-queue item, but inflates provenance counts.
- **Recommended disposition**: Remove performance_data[16-21] as duplicates. Update provenance_summary accordingly.

### [F2] verification_quote is paper title fragment, not text excerpt
- **Type**: label-contradiction
- **Severity**: low
- **Location**: mechanisms[10].verification_quote; mechanisms[12].verification_quote
- **Evidence**: mechanisms[10] (adsorption mechanism) has verification_quote: "Biosilica/Silk Fibroin/Polyurethane biocomposite for Cu2+ and Cr6+ removal" -- this is a paper title, not a text excerpt describing the mechanism. mechanisms[12] has the same title as its verification_quote.
- **Cross-ref**: No decision-queue item.
- **Recommended disposition**: Replace verification_quote with actual text excerpt from Prasad2022 describing the mechanism, or downgrade verification from "needs_review" to remove the misleading quote.

### [F3] MOF review data in silk-fibroin
- **Type**: translation-scope
- **Severity**: medium
- **Location**: performance_data[4-9]; mechanisms[2-5]
- **Evidence**: performance_data[4-9] cite Adil2022 (10.1039/d1ra07034g), a MOF separation/review paper. These report ZIF-8-PAN, MOF-808-PAN, ZIF-67@Fe3O4, etc. -- MOF composites, not silk-fibroin materials. mechanisms[2-5] describe MOF adsorption mechanisms (ZIF-8 Cu coordination, ZIF-67 Cr(VI) removal) that are not silk-fibroin-specific.
- **Cross-ref**: No specific decision-queue item, but boundary rule B01-SILK-001 acknowledges tested pH range is limited.
- **Recommended disposition**: Add scope_caveat "MOF composite review data, not silk-fibroin-specific" or relocate to metal-organic-framework material reference. These rows can remain as cross-domain background with caveats.

## Clean areas
- performance_data[0-3]: Legitimate silk-fibroin aerogel adsorption data from Bruder2021 with proper quotes.
- performance_data[10-15]: Legitimate Martis2022 and Prasad2022 data with verification quotes.
- performance_data[22]: Xing2025 FK/SF aerogel data with proper quote.
- mechanisms[0-1, 6-9, 13-20]: Legitimate silk-fibroin mechanisms (MO adsorption, Cu adsorption, beta-sheet structure, polar groups, superhydrophobic degumming, electrostatic MB, CV adsorption, electrospinning, lignin hydrophobicity, pH 2-4 mechanism).
- design_translation: Source tier is llm_inference (acceptable). Content aligns with silk beta-sheet functional groups.
