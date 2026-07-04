# Duplicate knowledge_items Audit Report

**Date**: 2026-06-26
**Scope**: All JSON files under `pollutant_knowledge_base/by_pollutant/*/`
**Method**: Three-pass analysis with evidence_text discrimination

## Summary

| Metric | Count |
|--------|-------|
| Pollutant directories scanned | 20 |
| JSON files with knowledge_items | 2,519 |
| Total knowledge_items | 27,592 |
| Exact `record_id` duplicates within same file | **0** |
| True duplicates (same param+value+evidence_text, same paper) | **4 cases / 8 items** |
| Cross-file true duplicates (same param+value+ref_doi, different filenames) | **1 case / 2 items** |
| Same param+value, different context pollutant (NOT duplicates) | 27 cases / 72 items |

## Detection Method

Three-pass analysis was used to minimize false positives:

1. **Pass 1 - record_id**: Exact `record_id` match within same file. Result: 0 duplicates.
2. **Pass 2 - param+value+context**: Same `parameter` + `value` + `context.pollutant` within same file. Found 24 cases, but many are false positives (different compounds in same table sharing a sentence-level evidence text).
3. **Pass 3 - param+value+evidence_text**: Same `parameter` + `value` + identical `evidence_text` within same file. This is the strongest signal of a true extraction duplicate. Found 13 cases.
4. **Manual verification** of all 13 strong-dup cases against context pollutant, evidence text, and notes. 9 were false positives (different compounds sharing the same evidence sentence). 4 confirmed true duplicates.

## Confirmed True Duplicates

### Case 1: PFOA - Zhuang2020 qmax 540.18

**File**: `全氟辛酸（PFOA）/Zhuang 等 - 2020 - Mechanism study on organic pollutant accumulation by iron-base.json`
**record_ids**: `ki_002`, `ki_003`
**Parameter**: Maximum adsorption capacity qmax
**Value**: 540.18 mg/g
**Context pollutant**: tetracycline (both)
**Evidence**: Identical - "The FeOOH-TCA and FeOOH-PFOA nanoparticles exhibit adsorption capacities more than 35% greater..."
**Notes**: Identical - "specific value 400.13 * 1.35 = 540.18"
**Verdict**: TRUE DUPLICATE. Exact same extraction appears twice. One should be removed.

### Case 2: BPA - Egbedina2023 crystallite size 8.1

**File**: `双酚A（BPA）/Egbedina 等 - 2023 - A porous bentonite-coconut husk composite for.json`
**record_ids**: `ki_022`, `ki_023`
**Parameter**: Crystallite size
**Value**: 8.1 nm
**Context pollutant**: (empty for both)
**Evidence**: Identical - "The crystallite sizes for BECH, BECH-H, and BECH-K were found to be 8.1, 8.1, and 6.9 nm"
**Verdict**: TRUE DUPLICATE. Both refer to the same 8.1 nm value. The evidence mentions BECH and BECH-H both at 8.1 nm, but both items have no distinguishing context. One should be removed or they should be differentiated by material type (BECH vs BECH-H).

### Case 3: BPA - Pilsniak2023 ion-exchange mechanism

**File**: `双酚A（BPA）/Pilsniak-Rabiega和Wolska - 2023 - Removal of silver from chlo.json`
**record_ids**: `ki_015`, `ki_016`
**Parameter**: Dominant sorption mechanism (based on E value)
**Value**: Ion-exchange
**Context pollutant**: Ag(I) (both)
**Evidence**: Identical - "For Resins I and II, the E parameter was 10.2 and 9.60 kJ/mol, respectively..."
**Notes**: Identical
**Verdict**: TRUE DUPLICATE. Both items describe the same mechanism for the same pollutant. One should be removed.

### Case 4: BPA - Yang2023 removal efficiency >98% (triple)

**File**: `双酚A（BPA）/Yang和Ji - 2023 - Facile Synthesis of Quinolinecarboxylic Acid-Linked C.json`
**record_ids**: `ki_005`, `ki_006`, `ki_007`
**Parameter**: Removal efficiency
**Value**: >98%
**Context pollutant**: 2,4-D, RhB, MB, Gentamycin (all three)
**Evidence**: Identical - "all four organic pollutants can be removed >98% within 5 min, 9 min, and 15 min..."
**Verdict**: TRUE DUPLICATE (triple). All three items are identical. Two should be removed.

## Cross-File Duplicate

### Case 5: PFOA - Liu2022 pore size 22.8 across two filenames

**Pollutant**: PFOA
**ref_doi**: 10.1038/s41467-022-29816-1
**Parameter**: Pore size
**Value**: 22.8
**Files**:
- `Installation of synergistic binding sites onto porous organi...` -> ki_011
- `Liu 等 - 2022 - Installation of synergistic binding sites ont...` -> ki_008
**Verdict**: TRUE DUPLICATE across two different filenames for the same paper. One file should be consolidated or the duplicate item removed.

## False Positives Investigated and Excluded

The following 9 cases were initially flagged as "strong duplicates" (same param+value+evidence_text) but confirmed as **legitimate** upon manual review. They represent different compounds or materials from the same table/sentence in the source paper.

| File | record_ids | Reason excluded |
|------|-----------|-----------------|
| Jun 2019 (BPA) | ki_014, ki_016 | Different compounds: BPA vs PFOA, both at pH 7 |
| Jun 2019 (BPA) | ki_021, ki_022 | Different compounds: BPA vs EE2 |
| Pharmaceutical (BPA) | ki_002, ki_009 | Different compounds: Aspirin vs Ibuprofen, both >90% |
| Pharmaceutical (BPA) | ki_005, ki_012 | Different compounds: Crotamiton vs Carbamazepine, both <45% |
| Sinha 2013 (BPA) | ki_003, ki_004 | Different compounds: atrazine vs dibutyl phthalate, both 200 mg/g |
| Dickenson 2010 (NP) | ki_023, ki_025, ki_027 | Different compounds: carbamazepine, naproxen, ibuprofen, all ~98% |
| Dickenson 2010 (NP) | ki_028, ki_030 | Different compounds: ibuprofen vs diclofenac, both ~60% |
| Hazratian 2025 (NP) | ki_011, ki_012 | Different compounds: BPA vs NP, both R2 > 0.9995 |
| Pacholak 2018 (BDE) | ki_003, ki_004 | Different compounds: BDE vs CDE, both 70% removal |

These are NOT duplicates. They are legitimate entries for different compounds that happen to share the same value, extracted from the same sentence in the source paper.

## Same Value, Different Context Pollutant (Not Duplicates)

27 cases were found where the same `parameter` + `value` appears in the same file but with different `context.pollutant`. These are entirely legitimate -- they represent multi-compound studies (e.g., a paper testing 5 pesticides reports the same removal rate for each).

Top pollutant directories with such entries:
- BPA: 8 cases
- DDT: 6 cases
- PFOA: 3 cases

## Recommendations

1. **Remove 4 confirmed true-duplicate pairs** (8 items total):
   - PFOA Zhuang2020: remove ki_003 (keep ki_002)
   - BPA Egbedina2023: remove ki_023 (keep ki_022) or differentiate by material
   - BPA Pilsniak2023: remove ki_016 (keep ki_015)
   - BPA Yang2023: remove ki_006 and ki_007 (keep ki_005)

2. **Consolidate cross-file duplicate**: The PFOA Liu2022 paper appears under two different filenames. Merge into one file or remove the duplicate item.

3. **No systemic pattern**: The duplicates appear to be isolated extraction errors, not a systematic issue. The overall deduplication quality is high (4 true duplicates out of 27,592 items = 0.015%).

## Appendix: Detection Statistics

- Files scanned: 2,519
- Items scanned: 27,592
- Pass 1 (record_id match): 0 hits
- Pass 2 (param+value+context match): 24 cases (includes false positives)
- Pass 3 (param+value+evidence_text match): 13 cases
- After manual verification: **4 confirmed true-duplicate cases, 8 affected items**
- Cross-file duplicates: **1 case, 2 affected items**
- **Total actionable duplicates: 5 cases, 10 items**
