# Audit: diatom-frustule

## Summary
- Total mechanisms: 15
- Total performance_data: 43 (but ~8 are exact duplicates, ~30 unique)
- Total design_translation: 0
- Total engineering_constraints: 17 (but ~4 are exact duplicates)
- Total narrative entries: 7 (but 2 are exact duplicates)
- Issues found: 7

## Findings

### [F1] Refuted DOI still present in performance_data[17]
- **Type**: wrong-source
- **Severity**: high
- **Location**: performance_data[17] (line 391)
- **Evidence**: ref_doi = "10.1016/j.jcis.2020.08.119" is in the refuted source list. Entry describes Ni(II) adsorption by DECFASEs with qmax 19.22 mg/g, source_file = "2021-Wu-diatomite-diatom-magnetic-nickel-adsorption.pdf". The DOI was refuted for wrong-source contamination.
- **Cross-ref**: Refuted source list includes 10.1016/j.jcis.2020.08.119
- **Recommended disposition**: Remove performance_data[17] or re-verify with correct source DOI

### [F2] Refuted DOI still present in mechanisms[14]
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[14] (line 1052-1059)
- **Evidence**: ref_doi = "10.1016/j.jcis.2020.08.119" is in the refuted source list. Mechanism is "XPS analysis confirming Si-OH bonding to Ni(II)". The DOI was refuted.
- **Cross-ref**: Refuted source list includes 10.1016/j.jcis.2020.08.119
- **Recommended disposition**: Remove or re-verify with correct source

### [F3] Refuted DOI still present in engineering_constraints
- **Type**: wrong-source
- **Severity**: high
- **Location**: engineering_constraints (line 1282-1289)
- **Evidence**: "循环再生性能" constraint cites ref_doi = "10.1016/j.jcis.2020.08.119" with value "4次循环后吸附容量从9.11降至8.25 mg/g". This DOI is in the refuted list.
- **Cross-ref**: Refuted source list includes 10.1016/j.jcis.2020.08.119
- **Recommended disposition**: Remove or re-verify with correct source

### [F4] Duplicate performance_data rows
- **Type**: label-contradiction (inflates provenance)
- **Severity**: medium
- **Location**: performance_data[7-8], [9-10], [11-12], [13-14], [15-16], [27-34] vs [35-42]
- **Evidence**: Exact duplicate rows exist for: DE removal ~93% (perf[7]=perf[8]), CD300 TC qmax (perf[9]=perf[10]), DE-SO3 Pb (perf[11]=perf[12]), DE-SO3 MB (perf[13]=perf[14]), DE-SO3 mixed (perf[15]=perf[16]), Sriram MO rows (perf[27-34] = perf[35-42]).
- **Cross-ref**: B09-DIAT-002 (boundary rule already applied)
- **Recommended disposition**: Deduplicate; do not count duplicates as independent evidence

### [F5] Duplicate mechanisms
- **Type**: label-contradiction (inflates provenance)
- **Severity**: medium
- **Location**: mechanisms[10]=mechanisms[11], mechanisms[12]=mechanisms[13]
- **Evidence**: "吸附机制（物理吸附为主）" appears twice (indices 10, 11). "离子强度影响" appears twice (indices 12, 13). Both are exact duplicates.
- **Cross-ref**: B09-DIAT-002
- **Recommended disposition**: Deduplicate

### [F6] Duplicate engineering_constraints
- **Type**: label-contradiction (inflates provenance)
- **Severity**: low
- **Location**: engineering_constraints[5]=engineering_constraints[6], [7]=engineering_constraints[8], [13]=engineering_constraints[14], [15]=engineering_constraints[16]
- **Evidence**: "再生性能" (Guo2022) duplicated at indices 5,6. "再生循环性能" (Abou-Elanwar) duplicated at indices 7,8. "NFD和NFB循环再生性能" (Sriram) duplicated at indices 13,14 and 15,16.
- **Cross-ref**: B09-DIAT-002
- **Recommended disposition**: Deduplicate

### [F7] Duplicate narrative entries
- **Type**: label-contradiction (inflates provenance)
- **Severity**: low
- **Location**: narrative.entries[6]=narrative.entries[7] (Qin2024), narrative.entries[8]=narrative.entries[9] (Guo2022), narrative.entries[10]=narrative.entries[11] (Abou-Elanwar), narrative.entries[12]=narrative.entries[13] (Arachnoidiscus)
- **Evidence**: Four pairs of exact duplicate narrative entries exist.
- **Cross-ref**: B09-DIAT-002
- **Recommended disposition**: Deduplicate

## Clean areas
- mechanisms[0-9]: Du2021, Qin2024, Guo2022 sources are legitimate (not refuted)
- performance_data[0-16]: Du2021, Qin2024, Guo2022, Abou-Elanwar sources are legitimate
- performance_data[18-26]: legitimate sources (Abou-Elanwar, Radjai, Sriram)
- design_translation: absent (no cross-domain contamination possible)
- R1-D corrective downgrades on mechanisms[5-13] are properly documented
