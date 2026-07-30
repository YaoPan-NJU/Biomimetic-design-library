# Audit: oyster-shell

## Summary
- Total mechanisms: 3
- Total performance_data: 13
- Total design_translation: 1
- Issues found: 2

## Findings

### [F1] Abalone shell data in oyster-shell prototype (Wang2021)
- **Type**: wrong-source
- **Severity**: high
- **Location**: performance_data[4], performance_data[5]
- **Evidence**: material="鲍鱼壳HA微球（abalone HA）", parameter="最大吸附容量 qmax (CR)" and "不同温度下的吸附容量", ref_doi="10.1016/j.matlet.2021.130573"
- **Cross-ref**: refuted-log fish-scale-hydroxyapatite performance_data[22-23] lists same DOI as wrong_source. The Wang2021 paper is about abalone shell (鲍鱼壳), not oyster shell (牡蛎壳).
- **Recommended disposition**: Remove performance_data[4-5]. Abalone shell HA microspheres are a different biological species from oyster. This data belongs in a shell-HAp category prototype, not specifically oyster-shell. Alternatively, move to fish-scale-hydroxyapatite if abalone is considered within that scope.

### [F2] General shell review data attributed to oyster-shell (Zhang2024)
- **Type**: wrong-source (scope contamination)
- **Severity**: medium
- **Location**: performance_data[8-12], mechanisms[2]
- **Evidence**: ref_doi="10.3969/j.issn.1672-7304.2024.02.0011" (Zhang2024 shell powder review). Entries include "煅烧改性对Pb吸附容量", "贝壳基羟基磷灰石吸附容量", "贝壳基羟基磷灰石去除率", "吸附剂用量对Cd去除率", "改性贻贝壳粉Pb吸附容量". Also mechanism[2] "吸附机理三步骤" from same DOI.
- **Cross-ref**: This DOI is a general shell review (2024-Zhang-shell-powder-heavy-metal-review.pdf) covering oyster, scallop, mussel, and abalone shells. While some data may be oyster-specific, entries like "改性贻贝壳粉" (modified mussel shell powder) are not oyster-specific.
- **Recommended disposition**: Retain with scope_caveat "general shell review, mixed species data". Verify which entries are specifically oyster-derived vs. general shell data. The "改性贻贝壳粉" entry (performance_data[12]) should be removed or reclassified since it is mussel shell, not oyster shell.

## Clean areas
- mechanisms[0]: 牡蛎壳改性吸附机制 — oyster-specific (CaCO3→CaO phosphorus removal)
- mechanisms[1]: 钝化机理 — general shell mechanism, legitimate for oyster
- performance_data[0-3]: Oyster shell modified biochar (Li2017, Qiu2021, Xu2022) — oyster-specific
- performance_data[6-7]: Calcined oyster shell (Zhang2021) — oyster-specific
- design_translation[1]: CaCO3 heavy metal fixation — legitimate
- No label contradictions found
- No honesty_ledger present
- Narrative entries: 4 legitimate oyster/shell-related narratives
