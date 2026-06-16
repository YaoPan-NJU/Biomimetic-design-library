---
status: ready_for_codex_acceptance
worker: OpenClaw/mimo-v2.5
completed_at: 2026-06-16T15:30:00+08:00
target_file: prototypes_db/materials_reference/metal-organic-framework.json
scope: verification semantics audit — Sub-Batch C
total_rows: 254
verification_distribution:
  single_source: 236
  needs_review: 16
  unverified: 2
---

# MOF Verification Semantics Audit

## Executive Summary

This audit examines the `verification` field semantics across all 254 `performance_data` rows in `metal-organic-framework.json`. The core finding: **`single_source` is being used as a blanket "one review paper says so" label, which conflates three distinct epistemic states** (direct primary data, review-summary second-hand data, and cross-domain contamination). The `provenance_summary.n_verified = 252` claim is **not** equivalent to quote+locator verified — it inflates confidence by counting all non-needs_review rows as "verified."

---

## 1. Verification Semantics Table

| Current label | Count | Actual meaning | Proposed rename/semantic |
|---|---|---|---|
| `single_source` | 236 | Data comes from exactly one source_file (usually a review paper). Does NOT mean the extractor found a direct quote/locator in the PDF. Most are "the review paper's table X says Y." | **Split into:** `review_summary` (data from a review's summary table, no primary-source cross-check), `single_primary` (data from a primary research paper with locator), `needs_human_decision` (ambiguous provenance) |
| `needs_review` | 16 | Data that the extractor flagged as needing human review — typically summary tables, mechanism descriptions, or patent examples. | **Keep as-is** — these are correctly flagged. |
| `unverified` | 2 | Rows where no verification could be performed (last 2 rows from Yan2022 polydopamine source). | **Keep as-is** — correct label for unverified data. |

### Why `n_verified = 252` is wrong

The `provenance_summary.n_verified = 252` appears to be computed as: `total_rows (254) - unverified (2) = 252`. This is **not** the same as "quote+locator verified." It simply means "not flagged as unverified." The field should be renamed to `n_not_unverified` or `n_present`, and a new field `n_quote_located` should track rows where the extractor actually found the data at a specific page/table/figure locator.

**Recommended:** Rename `n_verified` → `n_present_with_source` and add `n_quote_located` = count of rows with non-null `locator` AND `source_file`.

---

## 2. Suspicious Row Table — Codex-Flagged Clusters

### 2a. performance_data[24-37]: Aramesh2021 Chitosan Dye-Removal Review → MOF Contamination

**Finding: CONFIRMED CONTAMINATION**

14 rows (indices 23–36, 1-indexed 24–37) come from `2021-Aramesh-chitosan-adsorbent-dye-removal-review.pdf` — a **chitosan** review paper, not a MOF paper. Of these:

- **12 rows are pure chitosan materials** (no MOF component): CTS-Cu@SiO₂@Fe₃O₄, 磁性黄原酸盐改性壳聚糖, 二铵酒石酸盐改性壳聚糖凝胶珠, 壳聚糖/膨润土混合复合物, 壳聚糖/聚丙烯酸/GO复合水凝胶, 阳离子聚合物改性磁性壳聚糖珠, Fe₃O₄-CS复合物, 聚丙烯酰胺/壳聚糖/Fe3O4水凝胶, 二铵酒石酸盐改性壳聚糖, 半互穿网络壳聚糖-淀粉水凝胶, 锆(IV)负载壳聚糖/Fe3O4/GO, 壳聚糖/膨润土混合复合物
- **2 rows have MOF component** (ZIF-8@壳聚糖/PVA, MIL-101(Fe)@壳聚糖) — these are chitosan-MOF composites and could be legitimate but the source is still a chitosan review, not a MOF primary study

**Recommended action for pure chitosan rows (12 rows):** `wrong_source` — these are chitosan data, not MOF data. They belong in `chitosan.json`, not `metal-organic-framework.json`.

**Recommended action for chitosan-MOF composite rows (2 rows):** `needs_human_decision` — these are hybrid materials. The source is a chitosan review, so the MOF-specific performance claims may be second-hand summaries without primary-source verification.

| Index | material | pollutant | source_file | recommendation |
|---|---|---|---|---|
| 24 | CTS-Cu@SiO₂@Fe₃O₄ | RBR | Aramesh2021 chitosan review | wrong_source |
| 25 | 磁性黄原酸盐改性壳聚糖 | cationic azo dyes | Aramesh2021 | wrong_source |
| 26 | 二铵酒石酸盐改性壳聚糖凝胶珠 | CR, DY | Aramesh2021 | wrong_source |
| 27 | 壳聚糖/膨润土混合复合物 | dyes | Aramesh2021 | wrong_source |
| 28 | 壳聚糖/聚丙烯酸/GO复合水凝胶 | dyes | Aramesh2021 | wrong_source |
| 29 | 阳离子聚合物改性磁性壳聚糖珠 | SY dye | Aramesh2021 | wrong_source |
| 30 | Fe₃O₄-CS复合物 | MB, MO | Aramesh2021 | wrong_source |
| 31 | 聚丙烯酰胺/壳聚糖/Fe3O4水凝胶 | MB | Aramesh2021 | wrong_source |
| 32 | ZIF-8@壳聚糖/PVA纳米纤维 | MG | Aramesh2021 | needs_human_decision |
| 33 | 纳米MIL-101(Fe)@壳聚糖海绵 | Acid Red 94 | Aramesh2021 | needs_human_decision |
| 34 | 二铵酒石酸盐改性壳聚糖 | CR | Aramesh2021 | wrong_source |
| 35 | 半互穿网络壳聚糖-淀粉水凝胶 | DR80 | Aramesh2021 | wrong_source |
| 36 | 锆(IV)负载壳聚糖/Fe3O4/GO | AR | Aramesh2021 | wrong_source |
| 37 | 壳聚糖/膨润土混合复合物 | MG, AR | Aramesh2021 | wrong_source |

### 2b. performance_data[78-81]: Cheng2024 Membrane/Catalytic BPA Rows → MOF Contamination

**Finding: CONFIRMED CONTAMINATION**

4 rows (indices 77–80, 1-indexed 78–81) come from `2024-Cheng-chitosan-cellulose-separation-membrane-review.pdf` — a **membrane separation** review, not a MOF paper. None of these rows contain MOF materials:

| Index | parameter | material | pollutant | source_file | recommendation |
|---|---|---|---|---|---|
| 78 | 活性炭对BPA的吸附容量 | (empty) | BPA | Cheng2024 membrane review | wrong_source |
| 79 | NF膜去除BPA的机制 | (empty) | BPA | Cheng2024 membrane review | wrong_source |
| 80 | MF膜去除BPA的机制 | (empty) | BPA | Cheng2024 membrane review | wrong_source |
| 81 | UF膜与AOP联用去除BPA | (empty) | BPA | Cheng2024 membrane review | wrong_source |

These describe activated carbon, NF membranes, MF membranes, and UF-AOP coupling — none are MOF-related. The `material` field is empty for all of them, which is itself a red flag.

**Recommended action:** All 4 → `wrong_source`. Remove from MOF file.

### 2c. performance_data[89]: H2 Storage wt% — Context Mismatch

**Finding: NOT wrong_source, but context-mismatched**

Row 89: `MOF-5 氢气吸附容量 = 4.5 wt% at 78 K` from `2021-霍-膜-多孔-金属有机框架-吸附-综述.pdf`.

This is **not contamination** — MOF-5 is genuinely a MOF, and H₂ storage is a legitimate MOF application. However, it is a **context mismatch** for a water-treatment adsorption database. The MOF file's primary purpose is water treatment (pollutants, adsorption capacities for contaminants). H₂ storage at cryogenic temperature (78 K) is a completely different application domain.

**Recommended action:** `needs_human_decision` — either keep with a note that it's non-water-treatment, or move to a separate "MOF-gas-storage" category. Do NOT delete — it's a valid MOF data point, just misplaced.

---

## 3. Additional Wrong-Source Candidates

### 3a. performance_data[253-254]: Yan2022 Polydopamine → MOF Contamination

**Finding: CONFIRMED CONTAMINATION**

2 rows from `2022-Yan-polydopamine-magnetic-dye-adsorption-water-treatment.pdf` — a **polydopamine** review, not MOF. Material is `PDA/MGO/CA-CD` (polydopamine/graphene oxide composite), verification = `unverified`.

| Index | parameter | material | verification | recommendation |
|---|---|---|---|---|
| 253 | MB最大吸附容量 | PDA/MGO/CA-CD | unverified | wrong_source |
| 254 | MG和CV最大吸附容量 | PDA/MGO/CA-CD | unverified | wrong_source |

### 3b. performance_data[242-252]: CN121130847A Patent Rows — Acceptable but Special

**Finding: NOT wrong_source, but needs `patent_scan` flag**

11 rows from a Chinese patent (CN121130847A) for chitosan-cellulose-MOF composite foams. All materials contain ZIF-8 or ZIF-67, so they are legitimately MOF-related. However:

- Source is a patent, not a peer-reviewed paper
- `verification = needs_review` (correctly flagged)
- Patent PDF is not locally available for quote verification
- Patent data may not meet the same evidentiary standards as peer-reviewed literature

**Recommended action:** Keep as `needs_review` with additional flag `source_type: patent`. Do not upgrade to `single_source`. These are acceptable in the database but should be clearly distinguished from peer-reviewed data.

### 3c. performance_data[106, 118, 121, 165, 190]: Other needs_review Rows

These 5 rows are already correctly flagged as `needs_review`. They come from legitimate MOF review papers but involve summary tables or mechanism descriptions where the extractor couldn't pinpoint exact data. **Keep as-is.**

---

## 4. n_verified Reconciliation

| Metric | Current value | Correct value | Action |
|---|---|---|---|
| `provenance_summary.n_verified` | 252 | **Should not exist as-is** | Rename to `n_present_with_source` (252 = total - 2 unverified) |
| `provenance_summary.n_unverified` | 133 | Unknown meaning | Investigate: this seems too high for "unverified" when only 2 rows are labeled `unverified` |
| Actual `single_source` count | 236 | Should be split | ~224 after removing 14 Aramesh + 4 Cheng + 2 Yan = 220, plus 12 patent rows reclassified |
| Actual quote-located rows | Unknown | ~0 (none have extractor-verified quote+locator) | All locators are "Section X" or "表X" — these are the extractor's claims, not independently verified |

**Key insight:** The `n_verified = 252` number is a **false positive**. It counts every row that has a `source_file` as "verified," but none of these have been independently cross-checked against the actual PDF text. The `single_source` label means "one source says so," not "we verified this against the PDF."

**Recommended provenance_summary revision:**
```json
{
  "n_papers": 43,
  "n_total_rows": 254,
  "n_present_with_source": 252,
  "n_quote_located": 0,
  "n_wrong_source_suspected": 18,
  "n_needs_human_decision": 15,
  "n_patent_source": 11,
  "n_unverified": 2
}
```

---

## 5. Recommended Queue Items

### Immediate Actions (wrong_source — should be moved/removed)

| Row(s) | source_file | reason | target |
|---|---|---|---|
| 24-31, 34-37 (12 rows) | Aramesh2021 chitosan review | Pure chitosan materials, no MOF component | Move to `chitosan.json` or delete from MOF |
| 32-33 (2 rows) | Aramesh2021 chitosan review | Chitosan-MOF composites from chitosan review | needs_human_decision — verify if MOF data is primary |
| 78-81 (4 rows) | Cheng2024 membrane review | Activated carbon, NF/MF/UF membranes, no MOF | Delete from MOF |
| 253-254 (2 rows) | Yan2022 polydopamine review | PDA/MGO composite, not MOF | Delete from MOF |

**Total wrong_source candidates: 18 rows**

### Needs Human Decision

| Row(s) | reason | question |
|---|---|---|
| 32-33 | Chitosan-MOF composites from chitosan review | Should these be in MOF or chitosan? |
| 89 | H₂ storage wt% (not water treatment) | Should gas storage be in this file? |
| 242-252 | Patent data, not peer-reviewed | Accept patent data as equivalent to literature? |

### Semantic Rename Queue

| Current | Proposed | Reason |
|---|---|---|
| `verification: single_source` | `verification: review_summary` | More accurate — most are review paper summaries |
| `provenance_summary.n_verified` | `provenance_summary.n_present_with_source` | Avoids false "verified" claim |
| Add `source_type` field | `literature` / `patent` / `primary` | Distinguish source quality |

### Keep As-Is

- All `needs_review` rows (16): correctly flagged
- All `unverified` rows (2): correctly flagged
- All legitimate MOF literature rows (~220): valid data, just need semantic rename

---

## 6. Summary Statistics After Proposed Cleanup

| Category | Before | After |
|---|---|---|
| Total rows | 254 | 254 (no deletion, only reclassification) |
| wrong_source (move/remove) | 0 | 18 |
| needs_human_decision | 0 | 15 |
| review_summary (renamed from single_source) | 236 | 220 |
| needs_review | 16 | 16 |
| unverified | 2 | 2 |
| patent_source (new flag) | 0 | 11 |
