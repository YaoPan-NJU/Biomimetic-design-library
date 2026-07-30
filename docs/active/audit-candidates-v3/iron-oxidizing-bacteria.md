# Audit: iron-oxidizing-bacteria

## Summary
- Total mechanisms: 6
- Total performance_data: 26
- Total design_translation: 1
- Total engineering_constraints: 22
- Total narrative entries: 1
- Issues found: 1

## Findings

### [F1] CN113275374A performance rows need OCR verification
- **Type**: label-contradiction (verification vs. source quality)
- **Severity**: medium
- **Location**: performance_data[0-3] (lines 26-109)
- **Evidence**: Four performance rows cite patent_number = "CN113275374A" with verification = "partial" and confidence = 0.85. However, this is a scanned patent that cannot be text-verified locally. The B03-IOB-002 boundary rule acknowledges this as needs_human_decision. The verification_quote appears to be extracted from OCR but the patent is a MICP (microbially induced carbonate precipitation) patent involving mixed bacteria (not IOB-specific). The values may be legitimate but the source scope is questionable: it involves mixed carbonate-mineralizing bacteria with HAp additive, not pure IOB.
- **Cross-ref**: B03-IOB-002 (acknowledged_knowledge_gap_2026_06_17). Also relevant: B11-FISH-002 notes CN113275374A is "microbial carbonate biomineralization/MICP with mixed bacteria and HAp additive, not fish-scale extracted HAp adsorption."
- **Recommended disposition**: Keep as knowledge_gap with scope caveat "mixed-bacteria MICP, not IOB-specific"; do not use for IOB ranking until OCR and scope verification

## Clean areas
- mechanisms[0]: Legitimate CN113275374A patent source (MICP mechanism, needs_review)
- mechanisms[1]: Legitimate Luo2021 schwertmannite As(III) mechanism (verified with causal_chain)
- mechanisms[2-5]: Legitimate literature sources (10.13671/j.hjkxxb.2021.0204, 10.1016/j.clay.2021.106392, 10.3390/min15080868)
- performance_data[4-25]: All cite legitimate literature sources (Luo2021, Xu2022, Jhariya2024) -- all partially verified with quotes and locators
- engineering_constraints: All 22 rows cite legitimate literature sources (Luo2021, Xu2022, Jhariya2024, 10.7524/j.issn.0254-6108.2020050901 -- the last is iron-cycling but relevant to IOB)
- design_translation: LLM-inference (correctly labeled)
- No refuted DOI contamination found
- No label contradictions (no llm_inference + verified combos)
