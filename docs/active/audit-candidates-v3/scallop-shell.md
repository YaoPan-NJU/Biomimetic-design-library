# Audit: scallop-shell

## Summary
- Total mechanisms: 3
- Total performance_data: 7
- Total design_translation: 1
- Issues found: 1

## Findings

### [F1] Oyster shell data in scallop-shell prototype
- **Type**: wrong-source
- **Severity**: high
- **Location**: performance_data[0], performance_data[1]
- **Evidence**: parameter="煅烧牡蛎壳(800℃)最大吸附容量" and "煅烧双色牡蛎壳去除率(Cu/Co/Pb)", ref_doi="10.13254/j.jare.2020.0504". The parameter text explicitly says "牡蛎壳" (oyster shell), not scallop shell.
- **Cross-ref**: refuted-log fish-scale-hydroxyapatite performance_data[22-28] lists related shell review data. The Zhang2021 paper (2021-Zhang-shellfish-heavy-metal-passivation-review.pdf) is a general shellfish review. While it covers multiple shell species, the specific data rows here are labeled as oyster shell (牡蛎壳), not scallop.
- **Recommended disposition**: Remove performance_data[0-1]. These are oyster shell data entries incorrectly placed in scallop-shell. The same data already exists in oyster-shell.json performance_data[6-7]. Retain performance_data[2-6] which are from Zhang2024 (general shell review applicable to scallop).

## Clean areas
- mechanisms[0]: 钝化机理 — general shell mechanism (lime effect, precipitation, adsorption)
- mechanisms[1]: 吸附机理增强因素 — hydrogen bonding with Congo red, from Wang2024 scallop-specific paper
- mechanisms[2]: 吸附机理三步骤 — from Zhang2024 general shell review, applicable to scallop
- performance_data[2-6]: Zhang2024 general shell review data — legitimate for scallop
- design_translation[1]: CaCO3 pollutant fixation — legitimate
- No label contradictions found
- No honesty_ledger present
- Narrative: 1 legitimate shell-related narrative
