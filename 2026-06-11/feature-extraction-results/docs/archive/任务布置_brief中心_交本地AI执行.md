# 任务布置（交本地 AI 执行 · brief 中心版 · v1.1）

> 适用项目：Biomimetic-design-library
> 配合规格：《分层核查标准_交本地AI执行》《金标准闭环_启发质量评分卡》
> 执行者：能读取本地原始文献（PDF）的 agent（OpenClaw / Claude Code）
> 编制日期：2026-06-08

---

## 0. 库的定位（北极星，先写进 design.md，再动手）

本库是**仿生设计智能体的检索基座**，不是材料设计器、不是事实库，也不是按污染物名称硬查的简单映射表。

链路：`水质约束智能体 → 仿生设计智能体（推理 + 调库）→ 仿生设计 brief → 对抗设计模块（真正设计材料）`。

仿生设计智能体的产物是 **brief**，不是材料。库的唯一职责：让每个原型都能干净、可溯源、标注诚实地供出 brief 的三件套。

**新污染物匹配原则**：`pollutant_prototype_map` 只作为 direct evidence 层，不能作为唯一入口。对 PFOA、SMX、BPA 等痕量有机污染物，必须先做污染物分子特征画像（长链/芳香环/羧基/磺酰胺/酚羟基/电荷/pH 形态等），再由分子特征推可能吸附相互作用，最后匹配仿生机制/结构/特征和候选原型。

**brief 结构（库必须能逐字段填出 candidates 里的内容）：**

```
brief:
  context:                         # 来自上游水质约束智能体
    water_quality: {pH, 温度, 盐度, 共存离子, ...}
    removal_target: {污染物, 目标形态/去除率}
    pollutant_profile:              # 来自标准化 + 分子特征画像，不等同于文献证据
      canonical_name
      pollutant_class
      molecular_features: [...]      # 如 long_fluorinated_chain / aromatic_ring / sulfonamide / carboxylate
      likely_interactions: [...]     # 如 hydrophobic_partitioning / pi_pi / hydrogen_bond / electrostatic / pore_confinement
      profile_basis                  # database | rule | chemical_knowledge_inference | llm_inference
    engineering_constraints: [...]
  candidates:                      # 来自本库匹配 + 组装
    - prototype_id, organism
      match: {reason, weight, applicability_fit, match_basis, direct_evidence}  # (a) 借鉴哪些原型
      mechanism:                                         # (b) 靠什么机制/结构/特征
        name(原理)
        基本原理            # 为什么有效，一句接地的因果陈述（必填、必接地）
        key_structures / functional_groups
        molecular_feature_links       # 该机制响应了污染物画像中的哪些特征
        attribution: {source, ref, verification_tier}
      design_translation:                                # (c) 转译成什么材料设计思路
        idea               # 原型特异、可操作，非套话
        material_realization_examples   # 文献里现成的"生物→材料"转译（若有）
        source_tier: literature | llm_inference          # 接地 or 推断，必标
      evidence_context:                                  # 非 payload，仅佐证相关性
        performance_leads: [{pollutant, value, ..., verification_tier}]
  honesty_ledger:                  # 全 brief 的事实/线索/推断清单；必须区分 direct evidence 与 feature-based inspiration
    facts: [...]      # verified + corroborated
    leads: [...]      # single_source + unverified
    inferences: [...] # llm_inference
```

**交付单元 = 能供出干净 brief 三件套的原型。** 一个原型"做完"的定义不是"数据干净"，而是：能正确被匹配 (a)、有单一身份且接地的机制含基本原理 (b)、有可操作且诚实标注的设计转译 (c)。**性能核查等级不参与"做完"判定**（见规格的 active 公式）。

---

## 1. 执行阶段（P0→P3，前序未过验收不做下一步）

### Phase 0 — 定位与状态对齐（动手前必做）

1. 把第 0 节定位 + brief 结构写进 `docs/design.md` 顶部，作为全项目北极星；同步新建/更新 `docs/ADRMATS_INTEGRATION.md`，README / HANDOFF 同步加一行指向它。
2. **冻结 schema**（仅允许本布置第 2 节的小幅增补），**停止扩到 100 的一切工作**。
3. 用 `prototypes_db` 实测 + `validate_consistency.py` 输出，重写所有状态文档为**单一真相源**。删除/改正一切与实测不符的乐观表述（例如任何"已 verified / 验证完成"而实测为 0 的字样）。
- **验收**：design.md 含定位与 brief 结构；ADRMATS_INTEGRATION.md 含分层检索策略；全部状态文档与实测一致；无"完成/已核实"与数据矛盾处。

### Phase 1 — brief 三件套就绪（核心，按《分层核查标准》执行）

> 目标：让每个候选 active 原型都能干净供出 (a)(b)(c)。

- **1a 身份纯净（Path C，硬门）**：`check_chimera.py` 跑到 0，清完 HANDOFF 列的 5 个残留 chimera。清洗后内容不足的原型标 `needs_literature` / `low_coverage`，**移出 active**，不借他原型内容补。
- **1b 机制接地 + 基本原理（Path A + 新增）**：
  - 完成机制建模重构的**全部批次**（不止第一批），把"原理级机制"与"实例级性能"彻底分开，机制里不再混实例（消化 511 条 R14 警告）。
  - 每个 active 原型的核心机制**归属接地**（≥single_source 且在身份内）。
  - 每条机制补一句 **`基本原理`**：说清为什么有效（因果/物理化学机制），能从原文读到的接地填，读不到的标 `needs_review`、不编造。
- **1c 设计转译（Path D + material_realization）**：
  - 每个 active 原型至少 1 条**原型特异、可操作**的 `design_translation.idea`；删除/重写无信息量的套话（D5）。
  - 文献里有现成"生物→材料"转译的，建 `material_realization` / `inspired_by` 链并接地（source=literature）。
  - LLM 外推的转译标 `source_tier=llm_inference`，不挂文献引用。
- **1d 污染物画像与匹配依据（Path E，brief 硬门）**：
  - 对每个测试查询生成 `pollutant_profile`，至少包含 canonical_name、pollutant_class、molecular_features、likely_interactions、profile_basis。
  - 每个候选原型必须写明 `match_basis`：direct_pollutant_evidence / pollutant_class_evidence / molecular_feature_inference / mechanism_feature_bridge / llm_suggested_low_confidence。
  - 直接证据与特征推断必须分开；feature-based inspiration 可以下传，但不能伪装成文献直接证据。
- **验收**：每个 active 原型能填出非空且干净的 (a)(b)(c)；brief 含 pollutant_profile 与 match_basis；`check_chimera.py`=0；`validate_consistency.py` 0 错误；机制条目无实例级污染。

### Phase 2 — 诚实标注 + 接口契约（按《分层核查标准》第 1、3 节）

- **2a 性能分级（Path B）**：全库性能数据按五级打标签，**无未标条目**；粗大异常值闸生效（qmax>2000 等先标 needs_review 且不进权重）。缺 pollutant 的标 needs_review、不进匹配。
- **2b 分层匹配层补齐**：保留并修正 `pollutant_prototype_map` 作为 direct evidence 层；把 12 个有数据却未进 direct index 的原型补进去；污染物名归一（MB/亚甲基蓝等）；新增/整理污染物分子特征画像与 feature-based retrieval 入口，避免 PFOA/SMX/BPA 等新污染物只能靠名称硬匹配；剩余 3 个原型补 Layer 1 applicability。
- **2c 接口契约**：实现 `BiomimeticContext`，逐条暴露 verification_tier + source_tier，并按规格第 3 节表硬门控（强排序只吃 verified/corroborated；其余作线索；needs_review 排除）。brief 必须带 `honesty_ledger`。
- **验收**：接口能输出带 honesty_ledger 的 brief；下游拿到的每条定量值都带等级；validate 的接口契约规则通过。

### Phase 3 — 金标准 brief 闭环（按《评分卡》执行）

- 选 **3–5 个高价值吸附原型**作金标准（有真实数据、覆盖重金属/结构/多孔；mussel 因无数据不作金标准，MOF/chitosan/alginate/cellulose-nanocrystal/starch-granule 优先）。
- 对每个金标准设计 3–5 个查询（含**直接污染物命中、特征画像召回、负例**，验证不乱推），跑真实匹配链路出 brief，由**独立评审**按评分卡 D1–D8 打分。
- 评的是 brief 的启发质量，**不评数值准确性**。
- **关口（硬）**：5 个金标准的 brief 全部通过、负例未被错配，才进 Phase 4。第一个金标准通过先回报。

### Phase 4 — 扩库（仅在 Phase 3 关口通过后）

- 只把"能供出干净 brief 三件套"的原型纳入 active；空壳/分离簇保持 parked。
- 扩展时每个新原型走 Phase 1 三件套验收，不降标。

---

## 2. 允许的 schema 小幅增补（不构成 schema 重构）

仅以下增补，其余冻结：

- `mechanisms[].基本原理`（字符串，必填于 active 原型，需接地或标 needs_review）。
- `narrative.design_translation[]`：`{idea, material_realization_examples, source_tier}`。
- `material_realization` / `inspired_by` 互链字段（原型间）。
- 每条性能/机制：`verification_tier`（五级）；每条转译：`source_tier`（literature/llm_inference）。

---

## 3. 全程铁律（七条准则 + 本布置补充）

1. 质量与交付标准高于进度与数量。宁可 v1 只有 15 个能出 brief 的真原型。
2. brief 三件套必须可溯源、不串库、诚实标注。机制可定性、不要求可计算，但**必须可归属**（"不可计算"≠"无据"）。
3. 性能数据永远是 evidence_context、带等级的线索，**绝不进 brief 结论**。
4. 设计转译宁可少而接地，外推必标 llm_inference。
5. 空白优于错配；有引用不等于可信；综述数据不直接归属。
6. **先冻结 schema 再投核查**，不重演"核完即重建"。
7. 拿不准就停下问人（触发条件见规格第 5 节）。

---

## 4. 给本地 AI 的第一步（按顺序，做完一起回报）

1. 执行 Phase 0 全部（定位写入 + 冻结 + 状态对齐），回报对齐后的真实状态表。
2. 跑 `check_chimera.py` + `validate_consistency.py`，出当前违规清单（chimera / 机制污染 / 未标 / 断链），回报。
3. 选 **MOF** 作第一个金标准，按 Phase 1 把它的 (a)(b)(c) 做到能干净出 brief（含污染物画像、match_basis、基本原理 + 至少 1 条接地转译），至少跑一个 direct evidence 查询和一个 feature-based inspiration 查询，跑《评分卡》出一次闭环评分，回报。
4. 确认方法可行（评分通过）后，再推第二个金标准；5 个全过前不扩库、不重建 pollutant_map、不把 design-rules 投入匹配层。

---

*本布置以 brief 为交付单元，把《分层核查标准》《评分卡》嵌入 Phase 1–3。定位为"启发基座"，刻意不要求库产出可计算设计结论。*
