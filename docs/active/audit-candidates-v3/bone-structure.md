# Audit: bone-structure

## Summary
- Total mechanisms: 5
- Total performance_data: 3
- Total design_translation: 1
- Issues found: 2

## Findings

### [F1] MOF photocatalysis mechanism in bone-structure prototype
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[0]
- **Evidence**: mechanism name="MOFs光催化降解染料的机理", description="VB电子→CB→·OH和O₂⁻·自由基降解", source="literature", verification="unverified"
- **Cross-ref**: refuted-log line 167: bone-structure.json mechanisms[4] MOFs光催化降解染料的机理 | N/A | reason: wrong_source
- **Recommended disposition**: Remove mechanisms[0]. MOF photocatalytic dye degradation has no connection to bone structure adsorption. This is a clear scope contamination from a MOF review paper.

### [F2] MOF Cr(VI) performance data in bone-structure prototype
- **Type**: wrong-source
- **Severity**: high
- **Location**: performance_data[2]
- **Evidence**: parameter="HPU-13@Fe₃O₄对Cr(VI)的吸附容量", material="HPU-13@Fe₃O₄磁性杂化MOF", source_file="2021-陈-多孔-MOF-重金属-铬-综述.pdf"
- **Cross-ref**: refuted-log line 163: bone-structure.json performance_data[2] HPU-13@Fe₃O₄对Cr(VI)的吸附容量 | N/A | reason: wrong_source
- **Recommended disposition**: Remove performance_data[2]. MOF hybrid material for Cr(VI) is not related to bone structure. The source is a MOF heavy metal review, not bone/HAp literature.

## Clean areas
- mechanisms[1-4]: HAp-related mechanisms (HAp膜重金属去除性能, HAp四种重金属吸附机制, HAp膜制备方法, HAp膜类型与制备技术) — legitimate bone/HAp scope
- performance_data[0-1]: Bambaeero2020 data on chitosan-bone-shell-HAp composite — legitimate bone scope
- design_translation[1]: HAp Ca²⁺/PO₄³⁻ adsorption — legitimate bone scope
- No label contradictions found
- No honesty_ledger present
- No refuted DOIs found in remaining fields
