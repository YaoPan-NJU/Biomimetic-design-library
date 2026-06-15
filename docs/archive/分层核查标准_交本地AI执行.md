# 分层核查标准（交本地 AI 执行 · v1.1）

> 适用项目：Biomimetic-design-library（ADRMATS 的仿生**启发**检索模块）
> 适用执行者：能读取本地原始文献（PDF）的 agent（OpenClaw / Claude Code）
> 配合阅读：`docs/design.md`、`SESSION-CONTEXT.md` 七条准则
> 编制日期：2026-06-08

---

## 0. 定位前提（决定下面所有判据，先读）

本库是**启发/路由层**，不是事实库。它的职责是：按污染物 + 水质 + 工程约束，匹配出**对题、不跑偏、不串库**的生物原型、机制线索和设计思路。真正的材料构型生成、方案组合、冲突权衡，归下游对抗设计模块。

由此推出本规格的核心原则，与"全量核查"不同：

> **核查标准按 claim 类型分层。定性归属必须接地；定量性能只需诚实分级。**
>
> - **定性的机制/结构/特征归属**（库的核心载荷）→ 必须可溯源到真实来源（Path A），否则原型不可用作启发。
> - **定量的性能数值**（qmax、去除率等）→ 只需如实打分级标签（Path B），全量开 PDF 可延后/抽样，**不阻塞原型上线**。
> - **生物身份**必须单一、叙事/机制主题与原型 ID 一致（Path C，硬门）。
> - **LLM 外推的设计提示**必须标 `llm_inference`，不挂文献引用（Path D）。
> - **污染物画像与匹配依据**必须显式标注（Path E）。新污染物不能只靠 `pollutant_prototype_map` 硬查，必须区分 direct evidence 与 feature-based inspiration。

**原型可标 `active`（可用作启发）的充要条件**：

```
active  ⟺  (Path C 通过：身份单一、无串库)
        且 (Path A 通过：核心机制/结构归属至少 single_source 且在身份内)
        且 (Path D 通过：设计提示已分级标注)
        且 (Path E 通过：brief 查询能给出污染物画像与 match_basis)
        且 (Path B 已执行：每条性能数据有 verification 等级，无未标的)
```

注意：**性能数据的核查等级不参与 active 判定**。一个原型可以全部性能数据是 `unverified`，只要它们被诚实标注、且机制归属接地、身份干净，它就能作启发用。这是定位带来的直接红利，不要再用"全量 verified"卡上线。

---

## 1. verification 五级定义（机械套用，不靠判断）

每条性能数据（及可核查的机制条目）必须落在且仅落在以下五级之一：

| 等级 | 充要条件 | 是否需要开 PDF |
|------|----------|----------------|
| `verified` | source∈{literature,patent,standard} **且** ref 可解析（DOI 解析到 / 专利号或标准号确切）**且** 数值确实出现在该来源指定页/表，材料与污染物一致。三者缺一不可。 | 是 |
| `corroborated` | 同一定量 claim（**同污染物 + 同材料类 + 工况可比**，数值在 ±20% 或同数量级内）独立出现在 **≥2 个互非拷贝的来源**（非同一综述被重复引、非同一数据表被转引）。需核对跨源一致性，但不要求逐篇开 PDF 确认原始页码。 | 否（核对跨源一致性即可） |
| `single_source` | 可溯源到**恰好一个**来源、ref 字段在场，但尚未开 PDF 确认、也未被印证。这是"有据未核"的诚实默认态。 | 否 |
| `unverified` | 有来源引用但接地未建立，或提取阶段默认值。仅作线索。 | 否 |
| `needs_review` | 存在缺陷：缺页码 / 引用过短 / 数值精度不一致 / source=patent 无号 / 来自综述未追到原始实验论文 / 缺 pollutant / 同名异译未归一。**隔离，不可用作任何用途**直到解决。 | 视缺陷而定 |

**`corroborated` 判定细则（防止把综述拷贝洗成印证）**：

- 两来源的 DOI / 专利号 / 标准号必须不同。
- 若两条数据的 `source_file` 指向同一文献的不同副本（如 " 2.pdf" 后缀），算**一个**来源，不构成印证。
- 若 A 是综述、B 是综述引用的原始论文，**只算 B（原始论文）一个来源**；综述不计入印证票数。
- 数值容差：默认 ±20%；qmax 类可放宽到同数量级；去除率类必须同一区间（如均 >90%）。超出容差 → 不构成印证，二者各自按 `single_source` 处理，并标注分歧。

---

## 2. 四条核查路径（按 claim 类型分流）

每条进库内容先判断属于哪类 claim，再走对应路径。

### Path A — 归属接地核查（定性机制/结构/特征 · 必须做）

- **适用字段**：`mechanisms[].name`（原理）、`mechanisms[].description`、`mechanisms[].functional_groups`、`features[]`、`narrative.biological_solution`、`narrative.key_features`。
- **判据（通过）**：该机制/结构/特征**确实在某真实来源中被归因于该原型对应的生物**（看 JSON 的 `routing.prototype_targets` + 原文确认，不是仅关键词命中）。归属来源至少达到 `single_source`。
- **降级条件**：归属来源缺 ref / 来自综述未追到原始论文 → 标 `needs_review`，该机制条目不计入 active 判定。
- **删除条件**：原文中查无此归属，或归属的是**别的生物** → 删除该条（属串库，转 Path C 处理原型）。
- **边界**：`functional_groups` 能从原文读到的填；读不到的**留空**，不编造。留空不影响 active（启发不要求官能团齐全），但若整条机制连原理都无来源，则整条降级。

### Path B — 性能分级标注（定量数值 · 只需诚实分级，可延后核查）

- **适用字段**：`performance_data[]` 全部定量字段（qmax、removal_rate、动力学、循环等）。
- **判据**：按第 1 节五级定义打标签。**默认不开 PDF**，按现有 ref/source_file 在场情况落在 `single_source` 或 `unverified`；有缺陷的落 `needs_review`。
- **升级到 `verified` / `corroborated`**：仅在排期的核查阶段或抽审中做（见第 4 节），不在常规清洗中强求。
- **粗大异常值闸**：qmax > 2000 mg/g、removal_rate > 100%、或明显违背量级常识的 → 不论来源,先标 `needs_review`，且**不进 feature-mapping 权重计算**（防止未核实离群值抬高排序、误导"该看哪个原型"）。
- **删除条件**：来源查无此文，或开 PDF 后数值在来源中找不到 → 删除。
- **缺 pollutant**：标 `needs_review`，且不进 Layer 2 污染物匹配（无法匹配的线索不入路由）。

### Path C — 身份核查 / chimera（硬门 · 跑到 0 才能往下）

- **适用对象**：每个原型整体。
- **判据（通过）**：`organism.scientific` 为单一物种**或同类合理多源**（如各种 SRB 属、确为多源合成的超疏水体）；叙事与机制主题与原型 ID 领域一致。
- **判为 chimera（需清理）**：organism 含 ≥2 个**不同类**生物 **且** 机制/叙事主题与原型 ID 领域不符。
- **改法**：只保留 `prototype_targets` 确实指向该原型、且 `organism_scientific` 与之一致的来源的内容；其余删除或转移到正确原型。叙事/机制只能来自主题为该原型的来源，**绝不 `dict.update()` 跨生物合并**。
- **清洗后内容不足**：标 `status=needs_literature` 或 `coverage=low`，**不借别的原型内容补齐**。
- **验收**：`tools/check_chimera.py` 返回 0；当前 HANDOFF 列的 5 个残留 chimera 全部清完。

### Path D — 设计提示分级（防止外推当事实 · 必须标注）

- **适用字段**：`narrative.design_mapping`、任何"可迁移设计提示 / 仿生设计启示"类字段。
- **判据**：
  - 提示是对源文机制的**直接复述/合理直推** → `source=literature/patent`（接地）。
  - 提示是 LLM 跨域**外推**（源文未明说的迁移建议）→ 标 `source=llm_inference`，`ref_doi=null`，**不得标 verified/corroborated**。
- **删除条件**：提示与该原型机制矛盾，或明显是泛泛套话且无信息量（如"增大比表面积以提升吸附"无任何原型特异性）→ 删除或重写。
- **边界**：`llm_inference` 的提示**允许保留**并下传（它仍是合法启发），但接口上必须可见其为推断，由下游对抗模块自行决定是否采纳。

### Path E — 污染物画像 / 匹配依据核查（新污染物召回 · brief 硬门）

- **适用字段**：`brief.context.pollutant_profile`、`candidates[].match.match_basis`、`candidates[].match.direct_evidence`、`mechanism.molecular_feature_links`。
- **判据（通过）**：
  - 每个查询必须有 canonical pollutant name、pollutant class、molecular_features、likely_interactions、profile_basis。
  - 每个候选原型必须说明它是因何被召回：direct_pollutant_evidence / pollutant_class_evidence / molecular_feature_inference / mechanism_feature_bridge / llm_suggested_low_confidence。
  - 若直接命中 `pollutant_prototype_map`，可标 `direct_evidence=true`，但仍需带 verification_tier。
  - 若靠分子特征召回，必须标 `direct_evidence=false`，并说明哪些分子特征连接到哪些机制/结构/特征。
- **删除/降级条件**：
  - 只有污染物名称相似、没有特征或机制连接 → 降级为 `llm_suggested_low_confidence` 或删除。
  - 把 feature-based inspiration 写成 direct evidence → D6 风险，必须改。
  - 对 PFOA/SMX/BPA 等新污染物只查污染物名、没有画像 → 本次 brief 不通过。
- **边界**：LLM 可以辅助生成污染物画像，但 `profile_basis` 必须写明 `chemical_knowledge_inference` 或 `llm_inference`；不得把画像当作文献事实。

---

## 3. 接口契约（ADRMATS 对抗设计模块如何消费 · P0，不是以后再说）

`BiomimeticContext` 接口必须逐条暴露 verification 等级、source 类型、pollutant_profile 与 match_basis。下游消费按下表硬门控：

| 用途 | 可消费等级 |
|------|-----------|
| 强排序 / 候选打分 / 事实性解释 | 仅 `verified` + `corroborated` |
| 假设播种 / 设计灵感 / 探索方向 | `verified` + `corroborated` + `single_source` + `unverified`（均作**线索**，不得断言为事实） |
| 完全排除 | `needs_review`（直到缺陷解决） |
| 设计提示采纳 | `llm_inference` 提示可下传，但需在产出中保留"推断"标记 |
| 新污染物召回 | direct evidence 优先；无直接证据时允许 feature-based inspiration，但必须保留 `direct_evidence=false` 与 `match_basis` |

**强制方式**：契约写进接口 schema，不是写进文档共识。下游做任何定量排序时，若上游某条无 verification 等级或为 `needs_review`，接口直接拒绝该字段进入排序输入。

---

## 4. 全量核查的信任模型（必须排期，不要无限拖延）

性能数据逐条开 PDF 是大工程，扩到 100 原型会到数千条。采用**分级信任 + 排期核查**，并明确写进计划：

1. **优先级**：被 feature-mapping 高频引用的原型 → 金标准原型 → 其余。高频先做到 `verified`，其余明确停在 `single_source`/`unverified`。
2. **印证优先于逐条**：能用第 1 节 `corroborated` 规则低成本升级的，先做跨源印证，省去逐篇开 PDF。
3. **抽审**：每个原型随机抽 N 条（建议 ≥20% 或 ≥5 条）开 PDF 核对，作为该原型整体可信度的估计；抽审通过率写进 `provenance_summary`。
4. **冻结后再核**：先冻结 schema 与聚合逻辑，再投核查工，**避免重演"核完即重建"导致核查成果作废**（94.9% 旧库的教训）。

全量核查完成前，未核实数据必须显式带等级标志，让下游知情。

---

## 5. 何时必须停下来问人（不要自行决定）

- 某原型清洗后内容过少，不确定标 `needs_literature` 还是补文献。
- 某条数值在来源里找不到，但删了会让原型不达标 → **一律删/降级，绝不为达标保留**；若为难，问，不要自行放宽。
- `corroborated` 的容差/同材料判定拿不准。
- 六对重复 / chimera 的 canonical ID 与 feature-mapping 不一致或无法确定。
- 出现"为让原型达标想放宽核查标准或保留可疑数据"的念头 → 立即停，问。

---

## 6. 执行起点（按顺序，前序未过验收不做下一步）

1. 先跑 Path C（`check_chimera.py`）到 0，合并机制归属接地（Path A）为同一道 P0 闸。回报前后对比。
2. 对全库性能数据跑 Path B 分级标注，确保**无未标 verification 的条目**；粗大异常值闸生效。回报五级分布。
3. 对设计提示跑 Path D 分级。回报 `llm_inference` 条目清单。
4. 实现第 3 节接口契约的 schema 字段（每条带 verification + source 类型 + pollutant_profile + match_basis）。
5. 进入第 4 节排期核查：先挑一个金标准原型做抽审 + 印证升级，出"真实/编造/无法核实"分布，回报。达标再下一个。

全程对照七条准则；真实压过达标。每步对照本节验收自检并回报。

---

*配合《金标准闭环_启发质量评分卡》使用。本规格定位为"启发层"标准，刻意不要求把机制做成可计算规则。*
