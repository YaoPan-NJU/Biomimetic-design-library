# Audit: lotus-leaf

## Summary
- Total mechanisms: 49
- Total performance_data: 4
- Total design_translation: 0
- Issues found: 5

## Findings

### [F1] Refuted DOIs still present after scope split
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[14,15,19,20,21,22,25,26,27,28,29,30]; engineering_constraints[0,1]
- **Evidence**: Multiple mechanisms cite DOIs that were refuted in the fish-scale-hydroxyapatite cleanup (refuted-log):
  - mechanisms[14,15,25,26]: DOI 10.1007/s11783-021-1515-2 (membrane review, refuted for fish-scale)
  - mechanisms[19,20,21,22]: DOI 10.34133/2022/9895418 (femtosecond-laser review, refuted for fish-scale)
  - mechanisms[27,28,29,30]: DOI 10.1021/acsami.0c18794 (superhydrophobic review, refuted for fish-scale)
  - engineering_constraints[0]: DOI 10.1007/s10853-022-07945-8 (membrane/superhydrophobic review, refuted for fish-scale)
  - engineering_constraints[1]: DOI 10.1021/acsami.0c18794 (refuted for fish-scale)
  These DOIs were wrong-source for fish-scale-HAp but may represent legitimate superhydrophobic/wetting theory content. However, they describe general membrane/superhydrophobic materials, not lotus-leaf-specific mechanisms.
- **Cross-ref**: Refuted-log entries for fish-scale-hydroxyapatite; B04-LOTUS-003 guard rule.
- **Recommended disposition**: These mechanisms are from general superhydrophobic/wetting reviews. They may be acceptable as wetting-theory background if properly scoped, but the refuted-DOI association is a red flag. Recommend scope_caveat: "general wetting theory, not lotus-specific."

### [F2] Non-lotus biological sources still present
- **Type**: wrong-source
- **Severity**: high
- **Location**: mechanisms[16,17,18,23,24,31,32,33]
- **Evidence**: Several mechanisms describe non-lotus organisms:
  - mechanisms[16,17]: "荷叶超疏水仿生机制" from DOI 10.1007/s11783-021-1515-2 -- describes lotus but the source is a membrane review
  - mechanisms[18]: "六种自然超浸润材料" from DOI 10.1021/acsami.0c18794 -- describes gecko, butterfly, rose-petal, fish-scale (not lotus-specific)
  - mechanisms[23]: "仿荷叶PS纳米纤维/微球复合" -- this is artificial PS material, not biological lotus
  - mechanisms[24]: "荷叶效应仿生原理" -- acceptable as lotus
  - mechanisms[31]: "自然界仿生原型：植物/动物超浸润表面" from DOI 10.1007/s10853-022-07945-8 -- describes butterfly, cicada, dragonfly (non-lotus)
  - mechanisms[32]: "仿生单宁酸金属配合物" from DOI 10.1007/s10853-022-07945-8 -- tannic acid metal complexes, not lotus
  - mechanisms[33]: "自然界九种超疏水生物原型" from DOI 10.3390/polym15030543 -- lists lotus alongside 8 other organisms
- **Cross-ref**: Decision-queue B04-LOTUS-003 (hard_do_not, applied 2026-06-17): "Non-lotus examples must not be reported as lotus-leaf-specific evidence."
- **Recommended disposition**: Remove mechanisms[18,31,32] (non-lotus organisms/materials). Keep mechanisms[16,17,24] if they are genuinely lotus-specific despite the membrane-review source. Add scope_caveat to mechanism[33].

### [F3] Engineering constraints cite refuted membrane DOIs
- **Type**: wrong-source
- **Severity**: high
- **Location**: engineering_constraints[0,1]
- **Evidence**: engineering_constraints[0] ("智能响应膜：光/pH/温度/等离子体可切换润湿性") cites DOI 10.1007/s10853-022-07945-8 (membrane review). engineering_constraints[1] ("双刺激响应膜UV+pH") cites DOI 10.1021/acsami.0c18794. Both describe smart-responsive membranes, not lotus-leaf-specific constraints.
- **Cross-ref**: Refuted-log for fish-scale-hydroxyapatite; B04-LOTUS-003 guard rule.
- **Recommended disposition**: Remove both engineering_constraints as wrong-source for lotus-leaf. They describe membrane technologies, not lotus-leaf design constraints.

### [F4] Performance data scope_mismatch and knowledge_gap
- **Type**: wrong-source / knowledge-gap
- **Severity**: medium
- **Location**: performance_data[0,1,2,3]
- **Evidence**: performance_data[0] (PDMS/Al2O3 sponge, verification: knowledge_gap), [1] (3D graphene foam, verification: knowledge_gap), [2] (sol-gel calcination, verification: knowledge_gap) all have "PDF missing, cannot verify" notes. performance_data[3] (modified GO/sponge 53000x capacity) has verification: "scope_mismatch" with note "Li2023 oil-water separation review, not lotus-specific".
- **Cross-ref**: Decision-queue B04-LOTUS-002 (knowledge_gap, missing PDFs); B04-LOTUS-003 (wrong-source for performance_data[3]).
- **Recommended disposition**: Keep performance_data[0-2] as knowledge_gap (pending PDF acquisition). Remove performance_data[3] as scope_mismatch (not lotus-specific).

### [F5] Zero verified provenance
- **Type**: ledger-inaccuracy
- **Severity**: medium
- **Location**: provenance_summary
- **Evidence**: provenance_summary shows n_verified: 0, n_unverified: 359. This means zero mechanisms or performance rows have been verified with quotes and locators. The scope split note says "Kept 49 mechanisms (lotus-specific + wetting-theory)" but verification has not been upgraded for any retained row.
- **Cross-ref**: Decision-queue B04-LOTUS-001 (knowledge_gap, acknowledged).
- **Recommended disposition**: After scope cleanup, add verification quotes and locators to the retained lotus-specific mechanisms to upgrade from unverified.

## Clean areas
- mechanisms[0-9,10-13]: Core lotus-leaf mechanisms (superhydrophobic definition, lotus effect, natural wax coatings, green materials comparison, oil-water separation mechanism, surface energy change, lotus design principles, lotus effect microstructures, natural superhydrophobic sources, superhydrophobic threshold, Cassie-Baxter state, lotus effect mechanism, lotus biomimetic design). These are legitimate lotus-leaf content.
- mechanisms[11,12,13]: Green coating materials and MD membrane application (borderline -- these are about artificial materials inspired by lotus, acceptable as design translation context).
