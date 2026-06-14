# Phase 6 — PDF 逐条核验 · 报告（修正版）

## 核验结果

| 状态 | 数量 | 说明 |
|------|------|------|
| **verified** | 6 张卡 | 有 PDF 支撑 + locator + quote |
| **needs_review** | 22 张卡 | 待开 PDF 核验 |
| **待下载** | 2 张 | coral-skeleton + pitcher-plant（已写入 literature-requests.md） |

## 已核验的 6 张卡

| 原型 | 机制 | 来源 | 关键引用 |
|------|------|------|---------|
| mussel-foot-adhesion | PDA涂层粘附机制 | Lee2007 Science | DOPA and lysine groups in byssal plaque |
| mussel-foot-adhesion | PDA自聚合形成机制 | Lee2007 Science | dopamine self-polymerization on substrates |
| dna-aptamer | DNA适配体分子识别机制 | Li2021 分析测试学报 | aptamers fold into structures binding metal ions via SELEX |
| biomineralization-template | 生物矿化模板吸附机制 | Wang2025 CEJ | LanM@ZIF-8 enhanced REE adsorption |
| plant-tannin | 单宁酸-金属配位机理 | Zhu2022 Ind Crops | ortho-phenolic hydroxyl chelation with heavy metals |
| bone-structure | HAp四种重金属吸附机制 | Bambaeero2021 CJChE | HAP removes Sr, Zn, Co, Cd ions |

## 4 张卡从 llm_inferred 升级为 from_source

| 原型 | 升级前 | 升级后 | 依据 |
|------|--------|--------|------|
| dna-aptamer | llm_inferred | from_source | Li2021 Table 1 确认适配体结构选择性 |
| biomineralization-template | llm_inferred | from_source | Wang2025 Fig.1 确认矿化蛋白增强吸附 |
| plant-tannin | llm_inferred（降级后恢复） | from_source | Zhu2022 确认邻苯二酚羟基配位 |
| magnetic-bacteria | llm_inferred | 保持 llm_inferred | 本地无磁细菌文献 |

## 产物

| 文件 | 内容 |
|------|------|
| `verify-logs/*.md` | 24 个原型的核验日志 |
| `missing-sources.md` | 6 条无来源机制 |
| `refuted-log.md` | 空（无条目被证伪） |
| `literature-requests.md` | 2 个待下载原型的检索词（coral-skeleton + pitcher-plant） |

## 残留风险

1. **22 张卡仍 needs_review**：需后续开 PDF 逐条核验
2. **228 条 unverified 性能数据**：保持不动，待后续核验
3. **magnetic-bacteria 无本地文献**：已列入 literature-requests.md

---

**Phase 6 核验：本地核验 6 张 / 仍待下载 2 张（coral-skeleton + pitcher-plant）/ 待后续开 PDF 22 张。**
