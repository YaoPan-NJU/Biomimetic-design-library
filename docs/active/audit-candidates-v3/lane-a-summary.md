# Lane A Audit Summary — 8 Prototypes

**Audit date**: 2026-06-19
**Scope**: ADRMATS-visible fields only (mechanisms, performance_data, design_translation, engineering_constraints, narrative, provenance_summary)

---

## Per-Prototype Overview

| Prototype | Mechanisms | Perf Data | DT | EC | Narrative | Total Fields | Findings | Contaminated Entries |
|-----------|-----------|-----------|-----|-----|-----------|-------------|----------|---------------------|
| chitosan | 132 | 117 | 1 | 60 | 44 | 354 | 10 | 40 (wrong-source) + 177 (ledger) |
| polydopamine-coating | 65 | 44 | 1 | 21 | 10 | 141 | 9 | 53 (wrong-source) + 3 (scope) |
| mussel-foot-adhesion | 88 | 43 | 2 | 29 | 11 | 173 | 11 | 34 (wrong-source) |
| fish-scale-hydroxyapatite | 89 | 29 | 1 | 12 | 10 | 141 | 3 | 104 (wrong-source) |
| bone-structure | 5 | 3 | 1 | 1 | 3 | 13 | 2 | 2 (wrong-source) |
| oyster-shell | 3 | 13 | 1 | 0 | 4 | 21 | 2 | 8 (wrong-source) |
| scallop-shell | 3 | 7 | 1 | 0 | 1 | 12 | 1 | 2 (wrong-source) |
| wood-xylem | 4 | 3 | 1 | 3 | 2 | 13 | 0 | 0 |
| **TOTAL** | **389** | **219** | **9** | **125** | **75** | **817** | **38** | **~371** |

---

## Findings by Type

| Finding Type | Count | Severity Breakdown |
|-------------|-------|-------------------|
| wrong-source | 24 | 18 high, 6 medium |
| ledger-inaccuracy | 8 | 0 high, 0 medium, 8 low |
| label-contradiction | 3 | 0 high, 0 medium, 3 low |
| translation-scope | 1 | 1 high |
| data-quality | 1 | 0 high, 0 medium, 1 low |
| **TOTAL** | **37** | **19 high, 6 medium, 12 low** |

---

## Worst-Contaminated Prototypes

### 1. fish-scale-hydroxyapatite (104 contaminated entries, 74% of total fields)
- **Root cause**: Massive wrong-source injection from 7+ superhydrophobic/membrane/separation reviews
- 86 mechanisms from refuted DOIs (membrane classification, oil-water separation, femtosecond laser, SLIPS, etc.)
- 11 engineering_constraints from refuted DOIs
- 7 performance_data from abalone shell + general shell reviews
- Refuted-log already identifies these but they have NOT been removed

### 2. polydopamine-coating (56 contaminated entries, 40% of total fields)
- **Root cause**: Wrong-source injection from 5 different reviews
- 12 mechanisms from superhydrophobic review (acsami.0c18794)
- 16 mechanisms from superhydrophobic antibacterial review (jxhg.20201035)
- 6 mechanisms from PVDF fluoropolymer membrane review (polym14245439)
- 10 mechanisms from superwetting membrane review (cnki.issn.1001-3660)
- 2 mechanisms + 2 perf + 2 ec from PDA/MGO composite (borderline)
- 3 narrative entries from non-PDA reviews
- All 19 mechanism_instances reference refuted DOIs

### 3. chitosan (40 wrong-source entries, 11% of total fields)
- 14 performance_data from dye-removal review (ijbiomac.2021.04.158) — borderline (chitosan-relevant but review-sourced)
- 10 mechanisms from superhydrophobic membrane review (cnki.issn.1001-3660)
- 10 mechanisms from BPA/membrane review (cej.2024.149414)
- 4 performance_data + 2 engineering_constraints from same BPA review
- Plus 177 ledger-inaccuracy entries (verified without quote, missing source_file, stale provenance)

### 4. mussel-foot-adhesion (34 contaminated entries, 20% of total fields)
- 23 mechanisms from superhydrophobic review (acsami.0c18794)
- 4 engineering_constraints from same review
- 1 narrative entry from same review
- 2 mechanisms + 2 performance_data + 2 engineering_constraints from PDA/MGO composite (borderline)

---

## Clean Prototypes

### wood-xylem
- 0 findings, 0 contaminated entries
- All 4 mechanisms, 3 performance_data, 1 design_translation are from legitimate wood/biochar sources (Kumar2021, Mo2021)
- No refuted DOIs, no label contradictions, no ledger issues

---

## Cross-Prototype Contamination Patterns

### Pattern 1: Superhydrophobic/membrane reviews injected into non-membrane prototypes
- **10.1021/acsami.0c18794** (Zheng2020 oily wastewater review): Present in fish-scale (23 mech), mussel-foot (23 mech), polydopamine (12 mech)
- **10.1007/s11783-021-1515-2** (Halim2022 cellulose superhydrophobic review): Present in fish-scale (15 mech, 4 ec)
- **10.34133/2022/9895418** (Yong2022 femtosecond laser review): Present in fish-scale (12 mech)
- **10.1007/s10853-022-07945-8** (Mao2022 superhydrophobic membrane review): Present in fish-scale (9 mech, 2 ec)
- **10.3390/membranes13080727** (Tan2023 MD membrane review): Present in fish-scale (8 mech, 1 ec)
- **10.16490/j.cnki.issn.1001-3660.2023.02.015** (Jing2023 superwetting review): Present in fish-scale (10 mech), chitosan (10 mech), polydopamine (10 mech)
- **10.3390/polym14245439** (Li2023 PVDF membrane review): Present in polydopamine (6 mech, 1 ec)
- **10.1002/smll.202204624** (Yang2022 superwetting review): Present in fish-scale (10 mech)

### Pattern 2: Shell review data cross-contaminating shell prototypes
- **10.1016/j.matlet.2021.130573** (Wang2021 abalone shell): In oyster-shell (2 perf) and fish-scale (2 perf + 1 mech)
- **10.3969/j.issn.1672-7304.2024.02.0011** (Zhang2024 general shell review): In oyster-shell (5 perf + 1 mech), scallop-shell (5 perf + 1 mech), fish-scale (5 perf + 1 mech)

### Pattern 3: PDA/MGO composite appearing in multiple prototypes
- **10.1016/j.apsusc.2022.154338** (Yan2022 PDA/MGO/CA-CD): In mussel-foot (2 mech + 2 perf + 2 ec), polydopamine (2 mech + 2 perf + 2 ec) — borderline scope

---

## Recommended Priority Actions

1. **Immediate removal** (high severity, already in refuted-log):
   - fish-scale-hydroxyapatite: Remove 87 contaminated entries (mechanisms[0-77] refuted, ec[0-10], perf[22-28])
   - polydopamine-coating: Remove 53+ contaminated entries (mechanisms from 4 refuted reviews, all 19 instances)
   - mussel-foot-adhesion: Remove 28 contaminated entries (mechanisms[0-22], ec[0-3], narrative[0])
   - chitosan: Remove 24 contaminated entries (mechanisms[76-85,90-99], perf[76-79], ec[35-36])

2. **Scope assessment needed** (medium severity):
   - oyster-shell: Assess whether Zhang2024 shell review data is oyster-specific or general
   - scallop-shell: Assess whether Zhang2024 data is scallop-specific
   - chitosan: Assess whether Aramesh2021 dye review perf_data should be kept (chitosan-relevant but review-sourced)
   - All 3 prototypes with PDA/MGO data: Decide if Yan2022 belongs in mussel-foot or polydopamine

3. **Ledger cleanup** (low severity):
   - chitosan: Downgrade 24 "verified" perf_data to "needs_review" (no verification_quote)
   - All prototypes: Recompute provenance_summary to match actual field states
   - Add source_file to 130 chitosan mechanisms
