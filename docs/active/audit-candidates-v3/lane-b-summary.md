# Lane B Audit Summary — 8 Prototypes

Date: 2026-06-19
Auditor: Claude Code (audit agent)

## Findings by Type

| Type | Count | Prototypes affected |
|------|-------|-------------------|
| wrong-source | 5 | diatom-frustule (3), mycelium (1 combined), sulfate-reducing-bacteria (1 combined) |
| label-contradiction | 4 | diatom-frustule (3 duplicate-related), mycelium (1), iron-oxidizing-bacteria (1), mangrove-root (1) |
| ledger-inaccuracy | 0 | — |
| translation-scope | 1 | coral-skeleton (1) |
| **Total** | **10** | |

## Findings by Prototype

| Prototype | Issues | Severity breakdown |
|-----------|--------|-------------------|
| diatom-frustule | 7 | 3 high (refuted DOIs), 2 medium (duplicate perf/mech), 2 low (duplicate constraints/narrative) |
| mycelium | 3 | 2 high (refuted DOI in perf+mech), 1 low (quote quality) |
| sulfate-reducing-bacteria | 1 | 1 high (wrong-source constraints) |
| iron-oxidizing-bacteria | 1 | 1 medium (OCR verification gap) |
| coral-skeleton | 1 | 1 medium (wrong-topic narrative) |
| mangrove-root | 2 | 2 low (null values, quote quality) |
| biomineralization-template | 0 | Clean |
| dna-aptamer | 0 | Clean |

## Detailed Finding Inventory

### High severity (5 findings)
1. **diatom-frustule [F1]**: Refuted DOI 10.1016/j.jcis.2020.08.119 in performance_data[17]
2. **diatom-frustule [F2]**: Refuted DOI 10.1016/j.jcis.2020.08.119 in mechanisms[14]
3. **diatom-frustule [F3]**: Refuted DOI 10.1016/j.jcis.2020.08.119 in engineering_constraints
4. **mycelium [F1+F2]**: Refuted DOI 10.1016/j.tibtech.2022.09.011 in 5 performance_data rows + 3 mechanism rows (guard_rule already applied)
5. **sulfate-reducing-bacteria [F1]**: Wrong-source DOI 10.7524/j.issn.0254-6108.2020050901 in 3 engineering_constraints (guard_rule already applied)

### Medium severity (3 findings)
6. **diatom-frustule [F4+F5]**: ~8 duplicate performance_data rows + 2 duplicate mechanism rows inflate provenance counts
7. **iron-oxidizing-bacteria [F1]**: CN113275374A scanned patent rows need OCR verification; scope is mixed-bacteria MICP not IOB-specific
8. **coral-skeleton [F1]**: Han2020 narrative is antifouling review, not coral/CaCO3 adsorption

### Low severity (3 findings)
9. **diatom-frustule [F6+F7]**: Duplicate engineering_constraints (4 pairs) and narrative entries (4 pairs)
10. **mycelium [F3]**: Mechanism[3] verification_quote is title/summary, not text excerpt
11. **mangrove-root [F1+F2]**: Verification_quote is title fragment; 4 performance_data rows have null values

## Cross-Prototype Observations

1. **Refuted DOI persistence**: Three refuted DOIs still appear in Lane B prototypes:
   - `10.1016/j.jcis.2020.08.119` in diatom-frustule (3 locations) -- NOT in refuted-log as a guard_rule; needs action
   - `10.1016/j.tibtech.2022.09.011` in mycelium (8 locations) -- guard_rule applied but data NOT yet removed
   - `10.7524/j.issn.0254-6108.2020050901` in sulfate-reducing-bacteria (3 locations) -- guard_rule applied but data NOT yet removed

2. **Duplicate inflation**: diatom-frustule has ~8 duplicate performance_data rows, 2 duplicate mechanisms, 4 duplicate constraints, and 4 duplicate narrative pairs. This inflates provenance_summary.n_verified from the true ~25 unique rows to 42 counted rows.

3. **Empty prototypes**: biomineralization-template, dna-aptamer, and coral-skeleton have zero performance_data. coral-skeleton's single narrative is wrong-topic. These three are effectively placeholder prototypes.

4. **Verification quality gap**: mangrove-root mechanism[0] and mycelium mechanism[3] have verification quotes that are title fragments or summaries rather than verbatim text excerpts. Both are marked "verified" but the evidence quality is weak.

## Candidate Dispositions (DO NOT apply)

| Prototype | Field | Action | Priority |
|-----------|-------|--------|----------|
| diatom-frustule | performance_data[17], mechanisms[14], engineering_constraints[regen] | Remove or re-verify 10.1016/j.jcis.2020.08.119 rows | High |
| diatom-frustule | performance_data, mechanisms, constraints, narrative | Deduplicate all exact-copy rows | Medium |
| mycelium | performance_data[1-5], mechanisms[0-2] | Remove refuted tibtech rows (guard_rule pending execution) | High |
| sulfate-reducing-bacteria | engineering_constraints[1-3] | Remove iron-cycle rows (guard_rule pending execution) | High |
| iron-oxidizing-bacteria | performance_data[0-3] | Add scope caveat "mixed-bacteria MICP, not IOB-specific" | Medium |
| coral-skeleton | narrative.entries[0] | Remove or replace Han2020 antifouling entry | Medium |
| mangrove-root | performance_data[2-5] | Populate null values or mark qualitative-only | Low |
| mangrove-root | mechanisms[0].verification_quote | Upgrade to verbatim text excerpt | Low |
| mycelium | mechanisms[3].verification_quote | Upgrade to verbatim text excerpt | Low |
