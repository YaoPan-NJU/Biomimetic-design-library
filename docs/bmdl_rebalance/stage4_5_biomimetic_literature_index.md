# Stage 4.5 仿生文献库候选索引

**日期：** 2026-07-05
**扫描范围：** `/Users/panyao/Desktop/Biomimetic-design-library/仿生文献库`（643 篇 PDF）
**方法：** pdftotext 前 3 页关键词匹配

---

## 索引统计

| 指标 | 数值 |
|------|------|
| 总 PDF | 643 |
| 候选（含 bio_mat + qmax + pollutant） | 188 |
| 非综述 | 125 |
| BPA/PFOA/有机污染物 | 12 |
| 染料/重金属 | 113 |

## 按疑似 prototype 分布

| prototype | 候选数 |
|-----------|--------|
| chitosan | 78 |
| bacterial-cellulose | 27 |
| oyster-shell | 24 |
| bone-structure | 17 |
| chlorella-cell-wall | 11 |
| alginate | 9 |
| starch-granule | 5 |
| plant-lignocellulosic-architecture | 4 |
| diatom-frustule | 4 |
| plant-tannin | 2 |
| unknown | 7 |

## PDF 原文核查结果

对 8 个强候选做了 pdftotext 全文 + 多模态提取：

| 文件 | 疑似 proto | pollutant | 结果 | 原因 |
|------|-----------|-----------|------|------|
| 2021-Mo-wood-nanocellulose-aerogel | bacterial-cellulose | BPA | partial | qmax 在引用中非本文实验 |
| 2026-Shekh-adsorbent-modified | chitosan | PFOA | partial | qmax+material 不同页 |
| 2022-Liao-tetracycline-adsorption | chitosan | tetracycline | 0 entries | 多模态提取 4 data page 但 0 条结果 |
| 2022-Guo-diatomite-tetracycline | diatom-frustule | tetracycline | partial | 中文论文，qmax 在表格中 |
| 2023-Anuar-antibiotics-water | oyster-shell | tetracycline | rejected | 综述 |
| 2021-Zhang-shell-biochar-tetracycline | oyster-shell | tetracycline | partial | qmax 在表格图片中 |
| 2024-Qiu-biomassderived-carbon | chitosan | tetracycline | partial | qmax+material 不同页 |
| 2021-Mo-cellulose-nanocellulose-wood | bacterial-cellulose | BPA | partial | 同 Mo 2021（重复PDF） |

## 耗尽原因

仿生文献库的 qmax 数据主要在表格图片中，pdftotext 无法提取表格数值。多模态视觉精读（DashScope qwen3.7-Plus）对 Liao 2022 读取 4 个 data page 但提取 0 条——可能因为表格结构复杂或图片质量不足。
