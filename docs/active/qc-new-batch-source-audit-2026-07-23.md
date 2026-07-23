# 新批次原型来源质控审计（expand 分支）

- 日期：2026-07-23
- 分支：`expand`
- 范围：V1-B 生物/仿生扩展批次的来源真实性与范围匹配审计
- 方法：`prototypes_db/*.json` 结构盘点 + Crossref DOI 核实 + 联网检索原型专属一手文献
- 结论摘要：新批次 DOI **无一伪造**（全部能在 Crossref 解析），但存在**证据标签膨胀**——多个原型用宽泛综述冒充 `from_source`，与自身 `honesty_ledger` 自相矛盾。已为 5 个问题原型中的 4 个找到并核实原型专属一手源。

---

## 1. 入库盘点

`prototypes_db/*.json` 根目录共 **42 个 active 原型**（基线 36，本轮净扩）。按来源批次：

| 归属 | 数量 | 特征标记 |
|---|---|---|
| 第一批 · core（文献提取） | 24 | `tier=core`，`generated_by=P1c-auto/P1d`，2026-06-07 |
| 第一批 · extended（提取流水线） | 8 | `generated_by=P5-B-preflight/P3/P1c`，2026-06-07（分离/超疏水/材料类） |
| **★ 新批次（设计方案捞出）** | **8** | `tier=extended`，**无 `generated_by`**，2026-06-22 提交 `4462c63` |
| 新批次 · 手工精修 | 2 | 2026-07-21 `manual-curation`：FABP4、ModA |

另有 4 个二次浪潮原型已隔离于 `prototypes_db/quarantined/`（algae-polysaccharide、bacterial-surfactant、microbial-biomineralization、plant-gum），提交说明即 "lacking PDF grounding"。

**本次审计对象 = 2026-06-22 的 8 个新原型。**

## 2. 质控体系覆盖缺口

现有自动校验为**结构性绿灯**：
- `validate_consistency.py`：0 error / 171 warning（皆为分离类原型 R14 风格告警，预存）
- `check_causal_chain.py`：520/520 因果链字段已填

但这些脚本**只校验字段是否填满与内部一致，不校验来源是否真实、是否支撑论断**。来源真实性质控此前从未执行——新批次正落在此盲区。

## 3. 判定分档（基于 honesty_ledger 自报 + 本地 PDF + DOI 范围匹配）

| 原型 | 本地PDF | ledger from_source | 现引 DOI 判定 | 分档 |
|---|---|---|---|---|
| bacterial-cellulose | ✅ Hu 2021 | 2 | 真且专属 | **A 达标** |
| plant-lignocellulosic-architecture | ✅ ×10 | 2 | 真且相关 | **A 达标** |
| rice-husk-phytolith | ⚠️ 复用 Cai 2021 | 1 | 真但非稻壳专属 | B 偏 |
| bird-feather-keratin | ❌ | 0 | 真但错源（膜综述） | **C 膨胀** |
| fungal-biosorption | ❌ | 0 | 真但错源（细菌综述） | **C 膨胀** |
| insect-chitin | ❌ | 0 | 真但泛综述 | **C 膨胀** |
| microbial-exopolysaccharide | ❌ | 0 | 真但错源（细菌综述，复用） | **C 膨胀** |
| plant-wax-cuticle | ❌ | 0 | 真但错源（通用材料综述） | **C 膨胀** |

**核心问题（证据标签膨胀）**：C 档 5 个原型的 `honesty_ledger` 诚实写明 `from_source_mechanisms: 0`，但其 `causal_chain` 各要素却标 `basis/evidence_label: "from_source"` + 一篇宽泛综述 DOI + 形如 `p.12` 的定位 + `"Ligand groups such as amines, thiols"` 这类泛句。这违反 `CLAUDE.md` 明令禁止的"证据标签膨胀"。第一批（core）与 FABP4/ModA 均无此问题。

## 4. 现有 DOI 核实结果（Crossref 逐一确认，均真实存在）

| 原型 | 现引 DOI | 真实论文（Crossref 确认） | 匹配 |
|---|---|---|---|
| bacterial-cellulose | `10.1016/j.memsci.2020.118982` | Hu 2021, *Bio-inspired…UF membranes based on bacterial cellulose…dyes and oils*, J Membr Sci | ✅ 专属 |
| plant-lignocellulosic | `10.1016/j.jclepro.2020.125390` | 2021, *Silicate-modified oiltea camellia shell biochar…Cd removal*, J Clean Prod | ✅ 相关 |
| rice-husk-phytolith | `10.1016/j.jclepro.2020.125390` | 同上（复用油茶壳 biochar 论文） | ⚠️ 复用 |
| bird-feather-keratin | `10.1007/s10853-026-12899-2` | 2026, *Adsorbent-modified membranes for selective contaminant removal*, J Mater Sci | ❌ 错源 |
| fungal-biosorption | `10.1016/j.jwpe.2022.102884` | Sreedevi 2022, *Bacterial bioremediation of heavy metals…review*, JWPE | ❌ 错源 |
| microbial-exopolysaccharide | `10.1016/j.jwpe.2022.102884` | 同上（复用细菌综述） | ⚠️ 复用 |
| insect-chitin | `10.1007/s10924-021-02312-1` | 2021, *Natural Polymer…Electrospun Nanofibrous Membranes…review*, J Polym Environ | ⚠️ 泛综述 |
| plant-wax-cuticle | `10.3390/jmse10040534` | 2022, *Recent Advances in Functional Materials for Wastewater Treatment*, J Mar Sci Eng | ❌ 错源 |

## 5. 已核实的原型专属一手替代源（Crossref 确认，可直接采信标题/期刊/年份）

> 说明：以下 DOI 与刊物已经 Crossref 核实为真且主题匹配。**尚未做全文逐字引文提取**，故只能作为"候选一手源"记入，待补 quote+精确页码后方可升为 `from_source`（对齐第一批标准）。

| 目标原型 | 推荐一手源 DOI | 论文 | 支撑点 |
|---|---|---|---|
| **bird-feather-keratin** | `10.1177/0040517518764008` | Zhang 2018, *Valorization of keratin biofibers for removing heavy metals from aqueous solutions*, Textile Research Journal | 鸡毛/羊毛角蛋白生物吸附重金属，一手实验 |
| **fungal-biosorption** | `10.1016/S0960-8524(01)00148-1` | Baik 2002, *Biosorption of heavy metals using whole mold mycelia and parts thereof*, Bioresource Technology | A. niger/Rhizopus/Mucor 细胞壁生物吸附，一手 |
| fungal-biosorption（第二源） | `10.1016/S0960-8524(98)00192-8` | Kapoor 1999, *Removal of heavy metals using the fungus Aspergillus niger*, Bioresource Technology | A. niger 专属，一手 |
| **plant-wax-cuticle** | `10.1098/rsta.2009.0022` | Koch & Barthlott 2009, *Superhydrophobic and superhydrophilic plant surfaces: an inspiration for biomimetic materials*, Phil Trans R Soc A | 植物表皮蜡质微纳结构→超疏水权威一手源 |
| **microbial-exopolysaccharide** | `10.1038/s41598-025-94372-9` | Ciempiel 2025, *Lead biosorption and chemical composition of EPS…microalgal cultures*, Sci Rep | EPS 羧基/羟基吸附 Pb(II)，一手 |
| microbial-exopolysaccharide（候选，DOI 待核实） | Qu 2022, Environ Pollut, PII S0269749121022338 | *Functional group diversity for the adsorption of lead to bacterial EPS* | EPS 官能团多样性对 Pb 吸附，一手（**DOI 待核实**） |

## 6. 未找到专属源 → 交学生检索的关键词

**insect-chitin（真缺口）**：几丁质吸附文献绝大多数用虾/蟹壳（与既有 chitosan、lobster-exoskeleton 原型重叠），昆虫外骨骼专属吸附一手研究稀少。需确认该原型是否与虾蟹几丁质原型冗余；若保留，检索：
- `black soldier fly larvae chitin heavy metal adsorption`
- `insect cuticle chitin biosorption Pb Cd FTIR`
- `Bombyx / cicada slough chitin adsorbent`

**rice-husk-phytolith（补稻壳专属源，替换复用的油茶壳论文）**：
- `rice husk biogenic silica silanol heavy metal adsorption`
- `rice husk phytolith opal silica Pb Cd ion exchange`
- 候选：Yefremova 2023, *Rice Husk-Based Adsorbents for Removal of Metals*（综述，PMC10706995）；Hossain 2024, J Clean Prod（rice husk solvochar，一手）

## 7. FABP4 / ModA 抽查（2026-07-21 手工精修）

质量达到甚至超过第一批标准，无需处理：
- **FABP4**：`10.1021/jacsau.5c00504`（JACS Au 2025）+ PDB `9MIW`/`9OB7`，逐字 quote、honesty_ledger、boundary_notes 齐全，并诚实标注"正文 PDF 被墙、精确页码未核验"。
- **ModA**：`10.1038/nsb0997-703`（Nat Struct Biol 1997，ModA 钼酸根结合蛋白结构）+ `10.1038/314257a0`（Nature 1985，硫酸根结合蛋白）——领域经典，标注 verified/corroborated。

## 8. 建议动作

- **A 档（bacterial-cellulose、plant-lignocellulosic）**：已达标，无需改动。
- **C 档 5 个**：先做**去膨胀**（`causal_chain` 的 `from_source` → `llm_inferred`，对齐诚实 ledger），并把本报告 §5 已核实候选源写入各文件 `honesty_ledger`，待全文补 quote+页码后升 `from_source`。
- **B 档（rice-husk-phytolith）**：补稻壳专属源，将复用的油茶壳论文降为 background。
- **insect-chitin**：先按关键词检索；确认是否与虾蟹几丁质原型冗余。
- **质控体系**：建议新增 `check_source_authenticity`，自动标记 `causal_chain` 的 `from_source` 标签与 `honesty_ledger` 不一致、DOI 缺失、疑似泛引的条目。

## 9. 变更记录（本次直接执行）

对 C 档 5 文件做去膨胀：`causal_chain` 各要素 `basis`/`evidence_label` 由 `from_source` 改为 `llm_inferred`（对齐其 `honesty_ledger` 自报的 `from_source_mechanisms: 0`）；plant-wax-cuticle 另将 1 条 `corroborated` 边界降为 `llm_inferred/needs_review`；各文件 `honesty_ledger.knowledge_gaps[0]` 写入 §5 已 Crossref 核实的候选一手源与"现引为 background"说明。

- 已改：bird-feather-keratin、fungal-biosorption、microbial-exopolysaccharide、insect-chitin、plant-wax-cuticle
- 未改（待人工/学生检索）：rice-husk-phytolith（B 档补稻壳源）、insect-chitin 的冗余判定
- 未改（已达标）：bacterial-cellulose、plant-lignocellulosic-architecture
- 校验：`validate_consistency` 0 error / 171 warning（与改前一致）；`check_causal_chain` 520/520 qualified；5 文件 JSON 合法
- 说明：这些 causal_chain 的 `source`/`quote`/`locator` 仍指向原综述，现已标 `llm_inferred`（不再冒充 from_source）；下一步需用 §5 一手源提取逐字 quote+精确页码后方可升 `from_source`。尚未 commit。
