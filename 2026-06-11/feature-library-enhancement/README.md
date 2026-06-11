# 仿生设计知识库 / Biomimetic Design Knowledge Base

> 水处理仿生吸附材料设计 AI Agent 系统的核心知识组件

---

## 项目简介

本知识库是"水处理仿生吸附材料开发智能体系统"的核心数据支撑，为仿生吸附材料的设计与筛选提供结构化的生物原型数据、条件-机制规则和设计原则。当用户输入目标污染物和水质条件后，系统从本知识库中检索匹配的生物原型，获取其吸附机制和结构特征信息，并将结构化的仿生上下文（BiomimeticContext）传递给下游设计引擎。

知识库目前包含约 100 个生物原型条目（含 33 个核心原型及扩展条目）、40+ 条设计规则（22 条条件-机制规则 + 18 条设计原则）、以及结构化的特征-原型四层映射表（156 条权重条目）。每个原型条目涵盖仿生叙事、定量性能数据、机制分析、多尺度结构特征和工程约束评估。

本库作为 ADRMATS（Adversarial Design of Reactive Materials Through Autonomous Testing and Simulation）多智能体系统中的仿生检索模块（BiomimeticRetrievalModule），位于约束生成 Agent 与对抗式设计引擎之间，负责将工程约束转化为仿生设计灵感。

---

## 项目结构

```
Biomimetic-design-library/
├── README.md
├── feature-mapping.json         # 特征-原型四层映射表（33原型，156权重条目）
├── design-rules.json            # 设计规则索引（40条：22 CM + 18 DP）
├── prototypes/                  # 生物原型条目（~40个目录）
│   ├── mussel-foot-adhesion/
│   │   └── prototype.md
│   └── ...
├── principles/                  # 设计规则详解
│   ├── mechanisms/              # 条件-机制规则（22篇）
│   ├── design-strategies/       # 设计策略（10篇）
│   └── trade-offs/              # 设计权衡（8篇）
├── taxonomy/                    # 分类体系
│   ├── organisms.md             # 生物分类
│   ├── mechanisms.md            # 吸附机制分类
│   └── pollutants.md            # 污染物分类
├── extraction/                  # 仿生知识提取工具
│   ├── schema/                  # JSON Schema (biomimetic-v1)
│   ├── prompts/                 # LLM 提取提示词
│   ├── config/                  # 术语映射 + 原型路由
│   ├── scripts/                 # 后处理脚本
│   ├── pipeline/                # 四阶段提取管道
│   └── tests/                   # 测试用例
└── docs/
    ├── design.md                # 原始设计文档
    ├── prototype-id-mapping.md  # 原型ID对照表
    ├── adrmats-integration.md   # ADRMATS 集成方案
    └── superpowers/specs/       # 设计规范
```

---

## feature-mapping.json 结构

v2.0 四层结构，支持三层匹配机制 + 工程约束映射：

| 层级 | 字段 | 作用 |
|------|------|------|
| Layer 1 条件预筛 | `prototype_metadata[id].applicability` | 按 pH、温度、盐度过滤不适用的原型 |
| Layer 2 污染物匹配 | `pollutant_prototype_map[污染物]` | 按污染物检索原型 + weight 排序 |
| Layer 2 特征匹配 | `feature_prototype_map[特征]` | 按功能特征检索（无明确污染物时使用） |
| Layer 3 机制解释 | `mechanism_feature_bridge` | 特征 ↔ 机理桥接，为匹配结果提供机制解释 |
| Layer 4 约束映射 | `constraint_prototype_map` | 工程约束（成本、可扩展性等）→ 原型映射 |

**设计原则**：库只做匹配响应，不负责推理。约束识别归前置推理模块（AdaptiveConstrainingAgent），组合推理归下游模块（AdversarialDesignFlow）。

**weight 定义**：0-1 连续值，表示该原型对某个污染物/特征的匹配强度。

---

## design-rules.json 结构

设计规则采用双层存储架构：JSON 索引层 + Markdown 详解层。

### 规则类型

**CM 规则（Condition-Mechanism，条件-机制规则）**：描述特定环境条件下官能团的行为规律。

- 覆盖 pH / 温度 / 盐度 / 离子强度等条件下的官能团行为
- 示例：CM-001 "Catechol pH-dependent bidentate coordination" — 描述邻苯二酚在不同 pH 下与金属离子的配位行为
- 每条规则包含：条件参数、行为描述（中英双语）、受影响原型列表、适用范围、置信度
- 当前共 22 条，详解文档位于 `principles/mechanisms/`

**DP 规则（Design Principle，设计原则）**：总结仿生材料设计中的策略和权衡。

- 设计策略（`principles/design-strategies/`，10 篇）：如多价协同效应、层级结构优势、动态响应设计等
- 设计权衡（`principles/trade-offs/`，8 篇）：如耐酸性 vs 羧基配位能力、高容量 vs 快动力学、选择性 vs 广谱性等
- 每条规则包含：上下文、核心主张（中英双语）、设计启示、受影响原型列表
- 当前共 18 条

每条规则在 `design-rules.json` 中有 JSON 索引条目（便于程序化检索），同时在 `principles/` 目录下有对应的 Markdown 详解文档（便于 Agent 深度阅读和 Prompt 注入）。

---

## 三层匹配机制

1. **条件预筛**：根据 pH、温度、浓度、盐度等工况约束，从 `prototype_metadata.applicability` 排除不适用的原型
2. **加权特征匹配**：按 `pollutant_prototype_map` 或 `feature_prototype_map` 检索候选原型，以 weight × 匹配强度计算综合得分，取 Top-K
3. **机制解释与组合推理**：通过 `mechanism_feature_bridge` 为匹配结果提供机制解释；下游 LLM 读取 Top 原型详情，提出跨原型的组合设计方案

---

## 提取工具

`extraction/` 目录包含一套完整的仿生知识提取工具链，用于从学术文献中自动提取结构化仿生数据并更新知识库。

### 工具链组成

| 组件 | 路径 | 说明 |
|------|------|------|
| JSON Schema | `extraction/schema/` | biomimetic-v1 格式定义，规范提取输出的数据结构 |
| LLM 提示词 | `extraction/prompts/` | 包含粗提取、深度性能、仿生叙事、权重分配等模板（Jinja2 格式） |
| 术语映射 | `extraction/config/vocabulary_mapping.json` | 同义词归一化，将文献中的不同表述映射到标准术语 |
| 原型路由 | `extraction/config/prototype_routing.json` | 将提取结果路由到对应的原型目录 |
| 提取管道 | `extraction/pipeline/` | 四阶段自动化管道（Phase 1-4） |
| 测试 | `extraction/tests/` | 各组件的单元测试和集成测试 |

### 四阶段提取管道

```
Phase 1: Coarse Scan         粗扫描 — 快速提取文献中的核心仿生数据
    ↓
Phase 2: Gap Analysis         差距分析 — 识别原型条目中的缺失字段
    ↓
Phase 3: Supplement Plan      补充规划 — 制定针对性的补充提取策略
    ↓
Phase 4: Deep Extraction      深度提取 — 精细化提取性能数据和机制分析
```

### 完整工作流

```
学术文献 (PDF)
  → Schema 校验
  → Prompt 模板填充
  → LLM 结构化提取
  → 术语归一化 (vocabulary_mapping)
  → 原型匹配 (prototype_routing)
  → prototype.md 生成
  → feature-mapping.json 更新
```

运行方式：

```bash
cd extraction
python run_pipeline.py phase1   # 粗扫描
python run_pipeline.py phase2   # 差距分析
python run_pipeline.py phase3   # 补充规划
python run_pipeline.py phase4   # 深度提取
python run_pipeline.py all      # 完整管道
```

---

## 与 ADRMATS 的集成

本库作为 ADRMATS 多智能体系统中 **BiomimeticRetrievalModule** 的数据源，在系统管道中的位置如下：

```
User Input
    ↓
AdaptiveConstrainingAgent    ← 识别工程约束
    ↓ (ConstraintPreprocessOutput)
BiomimeticRetrievalTool      ← 本库数据
    ↓ (BiomimeticContext)
AdversarialDesignFlow        ← 消费仿生上下文，提出材料设计方案
    ↓
Proposer A/B, Design Explaining Agent, ...
```

### 输入

`ConstraintPreprocessOutput`（由 AdaptiveConstrainingAgent 生成）：目标污染物、pH 范围、温度范围、盐度、设计指导方针。

### 输出

`BiomimeticContext`（Pydantic 模型），包含：

- `candidate_prototypes`：Top 5 匹配原型（含匹配权重、关键特征、关键机制）
- `applicable_rules`：当前水质条件下适用的 CM 规则
- `design_principles`：相关 DP 设计原则
- `biomimetic_suggestions`：自由格式的仿生设计建议

**本库不包含 ADRMATS 代码。** 仅提供知识库数据和集成接口定义。`BiomimeticRetrievalTool` 的实际实现位于 ADRMATS 代码库中。

详见 [`docs/adrmats-integration.md`](docs/adrmats-integration.md)。

---

## ID 命名规范

所有原型 ID 统一使用**英文小写 + 连字符**格式。以下为 `feature-mapping.json#prototype_metadata` 中的 33 个核心原型 ID：

| ID | 原型 | 仿生维度 |
|----|------|----------|
| `lotus-leaf` | 荷叶表面 | 结构仿生 |
| `superhydrophobic-artificial` | 人工超疏水表面 | 功能仿生 |
| `namib-beetle` | 纳米布沙漠甲虫 | 形态仿生 |
| `pitcher-plant-slippery-surface` | 猪笼草滑移表面 | 结构仿生 |
| `shark-skin` | 鲨鱼皮 | 形态仿生 |
| `mussel-foot-adhesion` | 贻贝足丝粘附 | 分子仿生 |
| `polydopamine-coating` | 聚多巴胺涂层 | 分子仿生 |
| `plant-tannin` | 植物单宁 | 分子仿生 |
| `spider-silk` | 蜘蛛丝 | 结构仿生 |
| `silk-fibroin` | 丝素蛋白 | 分子仿生 |
| `mycelium` | 菌丝体 | 形态仿生 |
| `sulfate-reducing-bacteria` | 硫酸盐还原菌 | 过程仿生 |
| `iron-oxidizing-bacteria` | 铁氧化菌 | 过程仿生 |
| `magnetic-bacteria` | 趋磁细菌 | 功能仿生 |
| `chlorella-cell-wall` | 小球藻细胞壁 | 结构仿生 |
| `diatom-frustule` | 硅藻壳 | 结构仿生 |
| `diatom-inspired-porous` | 硅藻启发多孔结构 | 结构仿生 |
| `oyster-shell` | 牡蛎壳 | 结构仿生 |
| `scallop-shell` | 扇贝壳 | 结构仿生 |
| `coral-skeleton` | 珊瑚骨架 | 结构仿生 |
| `bone-structure` | 骨骼结构 | 结构仿生 |
| `fish-scale-hydroxyapatite` | 鱼鳞羟基磷灰石 | 分子仿生 |
| `chitosan` | 壳聚糖 | 分子仿生 |
| `alginate` | 海藻酸盐 | 分子仿生 |
| `cellulose-nanocrystal` | 纤维素纳米晶 | 结构仿生 |
| `starch-granule` | 淀粉颗粒 | 结构仿生 |
| `metal-organic-framework` | 金属有机框架 | 系统仿生 |
| `mangrove-root` | 红树根 | 形态仿生 |
| `wood-xylem` | 木质部 | 结构仿生 |
| `water-strider-leg` | 水黾腿 | 形态仿生 |
| `cactus-spine` | 仙人掌刺 | 形态仿生 |
| `lobster-exoskeleton` | 龙虾外骨骼 | 结构仿生 |
| `cell-membrane-ion-channel` | 细胞膜离子通道 | 分子仿生 |

扩展原型（由提取管道生成，正在合并中）包括：`biochar-adsorbent`、`biomineralization-template`、`dna-aptamer`、`molecularly-imprinted-polymer`、`diatom-microspheres`、`hydroxyapatite-adsorbent` 等。

完整 ID 对照表及合并状态见 [`docs/prototype-id-mapping.md`](docs/prototype-id-mapping.md)。

---

## 覆盖范围

| 维度 | 内容 |
|------|------|
| **生物类别** | 微生物（细菌、藻类）、植物（红树、仙人掌、猪笼草）、动物（贻贝、蜘蛛、鲨鱼）、仿生合成材料（MOF、PDA、MIP） |
| **仿生维度** | 分子仿生、结构仿生、形态仿生、过程仿生、功能仿生、系统仿生 |
| **吸附机制** | 配位螯合、超疏水分离、多孔吸附、生物矿化、纤维结构、静电吸附、氢键作用、π-π 堆积、分子筛分 |
| **目标污染物** | 重金属（Hg²⁺、Pb²⁺、Cd²⁺、Cr⁶⁺、As 等）、有机污染物（染料、药物、芳香族化合物）、油污、营养盐（磷酸盐、氟化物） |
| **设计规则** | 22 条 CM 规则（pH/温度/盐度/离子强度/氧化还原条件）+ 18 条 DP 规则（10 策略 + 8 权衡） |

### 统计概览

- 核心原型：33 个（`feature-mapping.json#prototype_metadata`）
- 原型目录：~50 个（含扩展和待合并条目）
- 映射条目：156 条权重记录
- 设计规则：40 条（22 CM + 18 DP）
- 详解文档：40 篇（`principles/` 目录）

---

## 如何使用

### 新 AI / 新会话上手流程

1. 读取本 README 了解项目全貌
2. 读取 [`docs/design.md`](docs/design.md) 了解原始设计
3. 读取 [`docs/adrmats-integration.md`](docs/adrmats-integration.md) 了解集成接口
4. 查看 `feature-mapping.json` 了解当前映射状态
5. 查看 `design-rules.json` 了解规则覆盖情况
6. 查看 `prototypes/[id]/prototype.md` 了解具体原型条目格式

### 建库工作流

1. 按检索方案在 Web of Science / Google Scholar 下载目标文献（PDF）
2. 使用 `extraction/` 工具链运行四阶段提取管道（见上方"提取工具"章节）
3. 审核提取结果，必要时手动补充和修正 `prototypes/[id]/prototype.md`
4. 同步更新 `feature-mapping.json` 中的映射表和 `design-rules.json` 中的规则
5. 每完成一批原型即 commit + push

### 手动添加原型

1. 在 `prototypes/` 下创建以 ID 命名的目录（如 `prototypes/new-prototype-id/`）
2. 按模板编写 `prototype.md`（包含仿生叙事、性能数据、机制分析、结构特征、工程约束）
3. 在 `feature-mapping.json` 的 `prototype_metadata`、`pollutant_prototype_map`、`feature_prototype_map` 中添加对应条目
4. 检查 `design-rules.json` 中是否有需要更新 `affected_prototypes` 的规则

---

## 相关项目和专利

- **ADRMATS**：对抗式活性材料设计自主测试与仿真系统，本库作为其仿生检索模块
- **Literature-extracting**（biomimetic-extraction 分支）：文献提取工具，与本库的 `extraction/` 工具链协同工作
- 隶属于《一种水处理仿生吸附材料开发智能体系统》相关专利
