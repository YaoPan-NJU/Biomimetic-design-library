# Audit: mycelium

## Summary
- Total mechanisms: 4
- Total performance_data: 6
- Total design_translation: 1
- Total engineering_constraints: 1
- Total narrative entries: 2
- Issues found: 3

## Findings

### [F1] Refuted DOI in performance_data[1-5]
- **Type**: wrong-source
- **Severity**: high
- **Location**: performance_data[1] (line 49-58), [2] (line 66-77), [3] (line 83-97), [4] (line 99-116), [5] (line 117-135)
- **Evidence**: All five entries cite ref_doi = "10.1016/j.tibtech.2022.09.011". This DOI is in the refuted source list. The source is a biomass/nanocellulose review (Zhang2022), not mycelium-specific evidence. Entries cover: spinifex nanocellulose Cd2+ removal, CNF/PVA dye removal, TOCNFs Cu2+ capacity, TOCNFs MB capacity, Ganoderma-corn cob anthracene removal.
- **Cross-ref**: Refuted-log confirms 10.1016/j.tibtech.2022.09.011 is wrong_source for mycelium. B03-MYC-001 (guard_rule applied).
- **Recommended disposition**: Remove all 5 rows (guard_rule already applied in decision queue)

### [F2] Refuted DOI in mechanisms[0-2]
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[0] (line 139-145), [1] (line 147-153), [2] (line 155-161)
- **Evidence**: All three mechanisms cite ref_doi = "10.1016/j.tibtech.2022.09.011". These are: "aminated CELF lignin powder for azo dye", "PEI-modified cellulose for PFAS", "nanocellulose foam for oil". None are mycelium-related. The refuted-log confirms these are cellulose/nanocellulose mechanisms wrongly placed in mycelium.
- **Cross-ref**: Refuted-log confirms wrong_source. B03-MYC-001 (guard_rule applied).
- **Recommended disposition**: Remove all 3 rows (guard_rule already applied in decision queue)

### [F3] Mechanism[3] verification_quote is paper title, not text excerpt
- **Type**: label-contradiction
- **Severity**: low
- **Location**: mechanisms[3].verification_quote (line 171)
- **Evidence**: verification_quote = "丝状真菌菌丝体细胞壁含80%-90%多糖(几丁质和纤维素),对重金属有吸附能力". This reads like a summary statement from the paper abstract rather than a direct text excerpt with locator context. The mechanism is verified but the quote quality is weak.
- **Cross-ref**: None specific
- **Recommended disposition**: Upgrade verification_quote to a more specific text excerpt from Liu2021 with page/section locator

## Clean areas
- mechanisms[3]: Legitimate Liu2021 source on fungal biosorption (chitosan/cellulose mechanism)
- performance_data[0]: Legitimate Liu2021 source (Table 1 comparison)
- narrative.entries[0-1]: Legitimate Liu2021 and Zhang2022 sources
- engineering_constraints[0]: Legitimate Liu2021 pH constraint
- design_translation: LLM-inference (correctly labeled)
- No label contradictions (no llm_inference + verified combos found)
