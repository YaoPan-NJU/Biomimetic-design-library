---
date: 2026-06-18
type: decision_request
from: qoderwork
to: yao
---

# Performance Data — 剩余未验证行汇总

## 概述

本轮 Batch 3-4 完成后，performance_data 验证状态如下：

| 状态 | 行数 | 占比 |
|------|------|------|
| partial（PDF已验证） | ~175 | 43% |
| verified（待 Yao 审批） | 130 | 32% |
| needs_review（PDF缺失） | 105 | 26% |
| missing_pdf（PDF缺失，已标记） | 8 | 2% |

**关键问题：113 行因为源 PDF 不在本地而无法验证。**

## 按原型分类

### chitosan — 70 rows（最大缺口）

22 个源 PDF 全部缺失，涵盖：
- 14 篇综述论文 (Aramesh2021, Ayub2021, Alves2021, Catenza2020, Eltaweil2021, Hsu2024, Keshvardoostchokami2021, Mallik2022, Sheth2020×2, Syeda2021, Upadhyay2020, Yang2021, Vo2023)
- 3 篇中文论文 (张2019, 冯2021, 赵2021, 胡2023, 张2022)
- 2 项专利 (CN109351339A, CN114873705A)

### cell-membrane-ion-channel — 14 rows

3 篇综述论文全部缺失 (Pachaiappan2022, Shaeli2022, Foorginezhad2025)

### mussel-foot-adhesion — 10 rows

3 项专利缺失 (CN105413659B, CN113042006A, CN114849661A)

### mycelium — 5 rows

1 篇综述缺失 (Zhang2022-adsorption-adsorbent-removal-review)

### polydopamine-coating — 4 rows

1 项专利缺失 (CN114887602A)

### diatom-frustule — 7 rows (missing_pdf)

杜2021 硅藻 paper (PDF exists as "2021-杜-硅藻-硅藻土-吸附-重金属 2.pdf" variant, but worker followed task instructions)

### oyster-shell — 1 row (missing_pdf)

Qiu2021 oyster-shell paper

### pitcher-plant — 1 row

Zeng2021 antifouling review

### lobster-exoskeleton — 1 row

Vo2023 chitosan membrane review (shared with chitosan)

## 需要 Yao 决策的事项

1. **chitosan 70 行**: 这是最大的缺口。22 篇文献全部不在本地。选项：
   - (a) 从学术数据库下载这些 PDF，放入仿生文献库
   - (b) 将无 PDF 支撑的行标记为 `unverified` 并在 provenance_summary 注明
   - (c) 如果是综述论文引用的二手数据，可以考虑从综述原文中交叉验证

2. **cell-membrane-ion-channel 14 行**: 该原型是分离/脱盐应用而非吸附，已在 scope_notes 中标注。选项：
   - (a) 下载 3 篇 PDF 进行验证
   - (b) 考虑将原型移至 parked（非吸附核心）

3. **mussel 10 行 + PDA 4 行**: 4 项专利缺失。选项：
   - (a) 从 Google Patents / CNIPA 下载
   - (b) 标记为 missing_pdf

4. **diatom-frustule 7 行**: 杜2021 PDF 有 "2.pdf" 变体存在于本地。可以直接用该变体验证。

5. **130 verified 行**: 仍等待 Yao 逐条审批升级为 verified。
