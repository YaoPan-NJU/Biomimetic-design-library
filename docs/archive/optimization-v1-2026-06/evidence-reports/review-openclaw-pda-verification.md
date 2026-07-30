---
status: ready_for_qoderwork_acceptance
task: PDA-coating performance_data PDF verification upgrade
date: 2026-06-17
model: mimo-v2.5-pro
rows_processed: 44
---

# PDA-coating Performance Data — PDF Verification Report

## Summary

对 `prototypes_db/polydopamine-coating.json` 的 44 条 `performance_data` 行完成 PDF 引文验证升级。

### Verification Status Distribution

| Status | Count | Description |
|--------|-------|-------------|
| `partial` | 30 | 单源 PDF 文本确认，待 Yao 审批升级 `verified` |
| `needs_review` | 10 | 引文质量不足或 OCR/估读值 |
| `missing_pdf` | 4 | CN114887602A 本地无 PDF |
| **Total** | **44** | |

### Changes Per Row

每条 `performance_data` 新增字段：
- `verification_quote`: PDF 中提取的真实文本摘录
- `source_locator`: 页码/段落/表格定位
- `verification`: 从 `unverified` → `partial` / `needs_review` / `missing_pdf`

## Group-by-Group Details

### Group 1: Foroutan (9 rows, indices 8–16) — `partial`
- **Source**: `2021-Foroutan-polydopamine-magnetic-iron-oxide-nickel-mercury.pdf`
- **Quote (qmax)**: "The highest elimination capacity (qm) for Hg(II), Co(II), and Ni(II) was set at 51.73 mg/g, 49.32 mg/g, and 48.09 mg/g, respectively" (p.1 Abstract / p.8 Section 3.3)
- **Quote (removal%)**: "As our findings show, with increasing water temperature from 25 °C to 50 °C, the elimination of Hg(II), Co(II), and Ni(II) are diminished from 94.36%, 93.66%, and 92.36% to 90.14%, 88.84%, and 87.46%, respectively" (p.7 Section 3.4)

### Group 2: Xiao COF (7 rows, indices 20–26) — `partial`
- **Source**: `2021-Xiao-cof-adsorption-water-treatment-regeneration.pdf`
- **Quote (COF@PDA qmax)**: "According to the Langmuir fitting, the calculated capture capacities of COF@PDA for Fe2+, Co2+ and Ni2+ equal 204.9, 194.2, and 207.5 mg/g, respectively" (p.1 Abstract / p.8 Section 3.2.3)
- **Quote (cycling)**: "The adsorption capacities of COF@PDA were still well-maintained with only a 2% decrease for Fe2+, a 2.9% decrease for Co2+ and a 2.7% decrease for Ni2+" (p.8 Section 3.2.5)
- **Quote (COF bare)**: "The maximum adsorption capacities of COF towards Fe2+, Co2+ and Ni2+ are only 55.4, 31.4 and 56.5 mg g−1, respectively" (p.7 Section 3.2.3)

### Group 3: CN114570339A Uranium (7 rows, indices 28–34) — `partial` / `needs_review`
- **Source**: `2022-CN114570339A-polydopamine-uranium-adsorbent.pdf` (scanned patent, visual_cache OCR)
- **Quote (96.5, abstract)**: "H-PDA-SO制备仅需130min，将其应用于水溶液中的U（VI）溶液吸附，40-50min内可达到平衡，室温下最大吸附容量96.5mg•g-1" (p.1 摘要)
- **Quote (103, 实施例)**: "25℃室温条件下其最大吸附容量可达103mg g⁻¹" (p.4 说明书[0023])
- **Quote (temp series)**: "其在288K时最大吸附容量为81.25mg g⁻¹，298K时最大吸附容量为96.5mg g⁻¹，308K时最大吸附容量为132.25mg g⁻¹" (p.7 实施例10 图6)
- **needs_review rows**: pH ~38/~36 (图4a/b 估读), ~8.2 (图7 selectivity figure 估读)

### Group 4: Shi Pb(II) (3 rows, indices 17–19) — `partial`
- **Source**: `2021-Shi-polydopamine-magnetic-iron-oxide-lead-adsorption.pdf`
- **Quote**: "The maximum Pb(II) adsorption capacity at 300 K, 308 K and 318 K calculated by Langmuir model could reach 196.67, 200.45 and 205.07 mg/g, respectively" (p.1 Abstract / p.4 Section 3.3.3 / Table 2 p.7)

### Group 5: Yuan Cr/Cu/CR (3 rows, indices 41–43) — `partial` / `needs_review`
- **Source**: `2024-Yuan-tannic-acid-cellulose-aerogel-heavy-metal-chromium.pdf`
- **Quote**: "CNF-TA-PMMT-PEI has a honeycomb-like pore structure, high porosity (98.29 %)... showed rapid and excellent adsorption performance for Cr(VI), Cu(II), and Congo red (CR), with the Qm of 456.62, 289.86, and 3429.23 mg/g, respectively" (p.1 Abstract / p.10 Section 3.4.3)
- **needs_review**: CR 3429.23 mg/g (extreme value — added caveat about multilayer/dye-aggregate adsorption)

### Group 6: Yan MB/MG/CV (2 rows, indices 37–38) — `partial`
- **Source**: `2022-Yan-polydopamine-magnetic-dye-adsorption-water-treatment.pdf`
- **Quote**: "Under optimal conditions, the maximum adsorption capacities of PDA/MGO/CA-CD towards MB, MG, and CV were 1372.32, 822.39, and 570.79 mg/g, respectively" (p.1 Abstract / p.11 / p.17)

### Group 7: Jin Carmine (1 row, index 39) — `partial`
- **Source**: `2023-Jin-polydopamine-chitosan-carmine-adsorption.pdf`
- **Quote**: "当染料初始质量浓度为700 mg/L 时，PDA/DCS 最大单分子层吸附量可达到1194.4 mg/g" (p.1 摘要 / p.7 正文)

### Other Rows
- **CN115055171A** (index 4): `partial` — "Fe3O4@PDA@CSH复合磁性吸附材料对上述重金属去除率仍能保持在72％以上" (p.8 [0036])
- **CN113244898A** (indices 5–7): `partial` — 96.31% 摘要, C0 4~70 mg/L 实施例3, 5mg/95.68% 实施例4
- **Zhang Gd** (index 27): `partial` — "At pH 7.0, the maximum adsorption capacity of aerogel for Gd(III) reached 150.86 mg g−1" (p.1 Abstract / p.6 / Table 5)
- **Godiya Cu** (indices 35–36): `partial` — "~434.8, ~277.7, and ~261.8 mg/g" (p.1 Abstract / p.5)
- **Xiang Ge** (index 40): `needs_review` — Langmuir qm = 0.349 mmol/g (p.8 Table), ~0.33 mmol/g 是估算值

### Missing PDF (4 rows, indices 0–3)
- **CN114887602A** (BC/PDA/La(OH)3 除磷): 本地仅有 `_visual_cache.json`，无 PDF 文件。已标记 `missing_pdf`。

## Validation Results

```
tools/validate_consistency.py: 1 error (pre-existing bone-structure), 0 new errors
tools/verify_data.py: polydopamine-coating 44 items — 30 partial, 10 needs_review, 4 missing_pdf
```

## Git Diff Summary

```
prototypes_db/polydopamine-coating.json | 273 +++++++++++++++++++-----------
1 file changed, 182 insertions(+), 91 deletions(-)
```

## Rules Compliance

- [x] `verification_quote` 均为 PDF 真实文本（非标题/DOI）
- [x] 无行标记为 `verified`（需 Yao 审批）
- [x] CN114887602A 的 4 行标记 `missing_pdf`
- [x] 未修改 `build_prototypes_db.py`
- [x] 未 commit/push
- [x] 校验脚本无新增 error

## Cleanup

可删除临时脚本：
- `scripts/apply_verification.py`
- `scripts/verify_pda_performance.py`
