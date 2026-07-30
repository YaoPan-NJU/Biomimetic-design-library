# 生物原型知识库/匹配清单 — 设计文档

> 日期：2026-05-27（2026-06-08 更新定位）

---

## 0. 库的定位（北极星）

本库是**仿生设计智能体的检索基座**，不是材料设计器、不是事实库。

**链路**：`水质约束智能体 → 仿生设计智能体（推理 + 调库）→ 仿生设计 brief → 对抗设计模块（真正设计材料）`

仿生设计智能体的产物是 **brief**，不是材料。库的唯一职责：让每个原型都能干净、可溯源、标注诚实地供出 brief 的三件套。

**新污染物匹配原则**：`pollutant_prototype_map` 只作为 direct evidence 层，不能作为唯一入口。对 PFOA、SMX、BPA 等痕量有机污染物，必须先做污染物分子特征画像（长链/芳香环/羧基/磺酰胺/酚羟基/电荷/pH 形态等），再由分子特征推可能吸附相互作用，最后匹配仿生机制/结构/特征和候选原型。

### brief 结构（库必须能逐字段填出 candidates 里的内容）

```yaml
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

**交付单元 = 能供出干净 brief 三件套的原型。** 一个原型"做完"的定义不是"数据干净"，而是：能正确被匹配 (a)、有单一身份且接地的机制含基本原理 (b)、有可操作且诚实标注的设计转译 (c)。**性能核查等级不参与"做完"判定**。

---

## 0.1 Schema 冻结（2026-06-08 生效）

**当前 schema 已冻结**，仅允许以下小幅增补（不构成 schema 重构）：

| 增补字段 | 类型 | 说明 |
|----------|------|------|
| `mechanisms[].基本原理` | 字符串 | 必填于 active 原型，需接地或标 needs_review |
| `narrative.design_translation[]` | 数组 | `{idea, material_realization_examples, source_tier}` |
| `material_realization` / `inspired_by` | 互链 | 原型间互链字段 |
| `verification_tier` | 枚举 | 每条性能/机制：verified/corroborated/single_source/unverified/needs_review |
| `source_tier` | 枚举 | 每条转译：literature/llm_inference |

**冻结目的**：先冻结 schema 再投核查，避免重演"核完即重建"导致核查成果作废。

**禁止事项**：
- 停止扩到 100 的一切工作
- 不重建 pollutant_prototype_map
- 不把 design-rules 投入匹配层

---

## 1. 背景与目标

### 1.1 系统中的角色

"生物原型知识库/匹配清单"是智能体系统的核心组件之一。当用户输入目标污染物和水质条件后，**需求解析Agent** 从该知识库中检索匹配的生物原型，获取其吸附机制和结构特征信息，然后将匹配结果传递给下游的文献调研Agent做深度调研。该知识库是整个智能体流水线的**第一道检索关卡**——其覆盖面和结构化程度直接决定了下游Agent能否找到有意义的仿生设计方向。

### 1.2 双重目标

1. **系统支撑**：为设计流水线提供覆盖充分、结构清晰且可追溯的检索数据
2. **实际研究工具**：可作为团队日常开发仿生吸附材料的检索和匹配工具

### 1.3 设计原则

- **LLM友好**：核心数据以Markdown纯文本存储，大模型直接读取效率最高
- **分层架构**：原始证据层（图片、3D文件、文献PDF）与抽象映射层（结构化描述、特征映射）分离
- **增量建设**：一篇文献可建一个原型条目，逐步积累
- **可扩展**：后续可在文件系统之上加向量索引做语义检索
- **库只做匹配响应**：约束识别归前置推理模块，组合推理归下游模块

### 1.4 ID 命名规范

所有原型 ID 统一使用**英文小写 + 连字符**，如 `lotus-leaf`、`mussel-foot-adhesion`、`sulfate-reducing-bacteria`。

## 2. 知识库架构

### 2.1 整体方案

采用**结构化文件系统**方案。每个生物原型一个目录（含 `prototype.md`），配套一个特征-原型映射表（JSON）。LLM直接读取文件完成匹配。

### 2.2 目录结构

```
Biomimetic-design-library/
├── README.md
├── feature-mapping.json
├── prototypes/
│   ├── lotus-leaf/
│   │   └── prototype.md
│   ├── mussel-foot-adhesion/
│   │   └── prototype.md
│   └── ...
├── taxonomy/
│   ├── organisms.md
│   ├── mechanisms.md
│   └── pollutants.md
└── templates/
    └── prototype-template.md
```

每个原型目录初期只放 `prototype.md`，后续按需扩展：
- `evidence/`：图片、3D文件等原始证据
- `references.bib`：参考文献

## 3. 原型文件 Schema

见 `templates/prototype-template.md` 获取完整模板。

核心章节：吸附机制详解（现象→分子基础→关键官能团→仿生设计启示）、结构特征与结构-功能关系（多尺度描述）、已报道性能数据（可选）。

## 4. 匹配机制

### 4.1 三层匹配

1. **条件预筛**：根据 pH、温度、浓度等工况约束排除不适用的原型
2. **加权特征匹配**：按 weight×匹配强度计算综合得分
3. **组合推理**：LLM 读取 top 原型详情，提出跨原型的组合方案

### 4.2 feature-mapping.json 结构

四层结构，支持三层匹配：

| 层级 | 字段 | 作用 |
|------|------|------|
| Layer 1 条件预筛 | `prototype_metadata[id].applicability` | 按 pH、温度、盐度过滤 |
| Layer 2 污染物匹配 | `pollutant_prototype_map[污染物]` | 按污染物检索 + weight 排序 |
| Layer 2 特征匹配 | `feature_prototype_map[特征]` | 按特征检索（无明确污染物时） |
| Layer 3 机制解释 | `mechanism_feature_bridge` | 特征↔机理桥接 |

**weight 定义**：0-1 连续值，表示该原型对某个污染物/特征的匹配强度。

### 4.3 设计原则

- **库只做匹配响应**：不负责推理，约束识别归前置推理模块，组合推理归下游模块
- **推理指导可选**：如果前置模块已分析好需求，库直接做匹配；如果没有，库的机制摘要和设计提示可辅助理解

## 5. 仿生维度

分子仿生、结构仿生、形态仿生、过程仿生、功能仿生、系统仿生。

## 6. 分类体系

### 6.1 生物分类（taxonomy/organisms.md）
微生物、植物、动物、仿生材料

### 6.2 吸附机制分类（taxonomy/mechanisms.md）
化学吸附、物理吸附、结构驱动、生物过程

### 6.3 污染物分类（taxonomy/pollutants.md）
重金属、有机污染物、无机非金属污染物、油类、放射性元素

### 6.4 机理与材料性质的对应关系

机理分类（科学视角）和材料性质分类（设计视角）是不同维度，通过 `mechanism_feature_bridge` 关联。详见 `taxonomy/mechanisms.md` 末尾的对应表。

## 7. 分阶段实施

1. **初始交付**（20个原型）
2. **研究工具**（50+原型）
3. **演示与可视化**
4. **社区共建**（100+原型）
