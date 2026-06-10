# 通用仿生水处理设计参考库 — 设计文档

> 日期：2026-06-09
> 状态：设计确认
> 关系：本项目为独立开发的新项目，后续将吸收现有"仿生吸附材料知识库"作为子集

## 1. 背景与目标

### 1.1 项目定位

从"仿生吸附材料设计"扩展为"面向整个水处理过程的通用仿生设计参考库"。覆盖仿生材料、微生物设计、反应器设计、元件设计、仿生智慧水处理装备及污水厂提标改造方案。

### 1.2 核心目标

- **设计支持**：指导材料和微生物的设计合成
- **系统级设计**：根据流场、生化反应、微生物功能、污染物迁移转化等规律设计仿生智慧水处理装备
- **改造优化**：为已有污水处理系统的提标改造、工艺优化、环节调优提供仿生灵感
- **运行调控**：为实时运行控制系统的调控决策提供仿生参考

### 1.3 设计原则

- **LLM 友好**：核心数据以 Markdown 纯文本存储，大模型直接读取
- **分层架构**：原型层（知识）与路由层（查询）分离，领域隔离可独立建设
- **多尺度覆盖**：每个原型描述材料→组件→反应器→系统四个尺度的设计启示
- **灵感 + 参数边界**：提供仿生灵感和可量化设计参数，但不包含仿真模型本身
- **增量建设**：领域独立建设，原型逐步积累

### 1.4 与现有项目的关系

现阶段独立开发。现有"仿生吸附材料知识库"后续将作为 `domains/adsorption/` 领域迁入，33 个吸附原型补充多尺度描述后纳入共享原型池。

## 2. 架构方案

### 2.1 选型：领域路由架构（方案 B）

在生物原型池之上增加领域路由层。每个领域拥有独立的分类视图和映射文件，共享同一个原型池。

**选型理由**：
- 12+ 个领域天然需要隔离建设，避免单文件膨胀
- LLM 友好（Markdown + JSON 双层结构）
- 现有吸附库可零改造成为第 13 个领域
- 支持 5 种用户入口的灵活路由
- 后期可渐进引入图架构（JSON-LD）元素

### 2.2 整体目录结构

```
water-biomimetic-library/
├── README.md
├── prototypes/                         # 共享原型池
│   ├── _index.json                     # 原型索引（元数据摘要）
│   ├── lotus-leaf/
│   │   └── prototype.md
│   └── ...（所有原型平铺在此）
├── domains/                            # 领域路由层
│   ├── _index.json                     # 领域列表与跨域关系
│   ├── fluid-mechanics/                # 流体力学
│   ├── biochemical-reactions/          # 生化反应
│   ├── separation-filtration/          # 分离/过滤
│   ├── microbial-community/            # 微生物群落
│   ├── biofilm/                        # 生物膜
│   ├── metabolic-pathways/             # 代谢路径
│   ├── mass-transfer/                  # 传质与流场
│   ├── solid-liquid-separation/        # 固液分离
│   ├── shock-resistance/               # 抗冲击与自恢复
│   ├── resource-recovery/              # 资源化
│   ├── energy-drive/                   # 能源/驱动
│   ├── system-community/               # 系统/群落
│   └── adsorption/                     # 吸附（从现有项目迁入）
├── shared/                             # 跨领域共享资源
│   ├── taxonomy/
│   │   ├── organisms.md                # 生物分类（全局）
│   │   ├── pollutants.md               # 污染物分类（全局）
│   │   ├── processes.md                # 水处理工艺分类
│   │   ├── scales.md                   # 尺度定义
│   │   └── design-problems.md          # 设计问题分类
│   └── cross-domain-links.json         # 跨域原型关系（协同/替代/互补）
├── entrypoints/                        # 多入口路由
│   ├── pollutant-router.json           # 污染物→领域→原型
│   ├── process-router.json             # 工艺→领域→原型
│   ├── problem-router.json             # 设计问题→领域→原型
│   ├── retrofit-router.json            # 改造场景→领域→原型
│   └── operation-router.json           # 运行调控→领域→原型
├── templates/
│   ├── prototype-template.md
│   ├── domain-profile-template.md
│   └── mapping-template.json
└── docs/
    ├── design.md                       # 本文件
    └── design-decisions.md
```

每个领域目录（如 `domains/mass-transfer/`）内部结构：

| 文件 | 作用 | 篇幅 |
|------|------|------|
| `domain-profile.md` | 领域概况：核心原理、典型问题、关联工程工具 | 500-800 字 |
| `taxonomy.md` | 领域专属分类：子类别体系 | 100-300 字 |
| `mapping.json` | 领域内原型映射 + 权重 + 尺度聚焦 + 设计启示摘要 | 200-400 行 |
| `design-patterns.md` | 领域内常见仿生设计策略 | 按需 |

## 3. 原型模板（prototype-template.md）

### 3.1 YAML 前置元数据

```yaml
---
# === 基础元数据 ===
id: [prototype-id]                      # 英文小写+连字符
name: [中文名称]
category: [微生物/植物/动物/仿生材料]
organism: [学名]
biomimetic_dimension: [分子/结构/形态/过程/功能/系统仿生]

# === 全局标签 ===
features: [特征标签列表]
pollutants: [适用污染物]
applicability:
  pH_range: [min, max]
  temp_range: [min, max]
  salinity: [low/moderate/high/low_to_moderate]
evidence_level: [high/medium/low]

# === 领域关联（指向 domains/ 下的领域 ID）===
domains:
  - id: [领域ID]
    relevance: [0-1]
    role: [该原型在该领域中的角色描述]

# === 工程约束 ===
engineering_constraints:
  - constraint: [工程约束名称]
    relevance: [high/medium/low]
    explanation: [说明]
---
```

### 3.2 正文章节结构

```markdown
# [中文名称]（[英文名称]）

## 1. 生物原型简介
[200-300字：来源、生物学背景、水处理应用价值]

## 2. 多尺度设计启示（必填）

### 2.1 材料尺度
[表面化学、微观结构、功能涂层等材料层面启示]
- **关键设计参数**：[可直接用于仿真的参数及取值范围]
- **关联工程工具**：[如适用，标注相关仿真/分析工具]

### 2.2 组件尺度
[填料几何、膜结构、曝气头等组件层面启示]
- **关键设计参数**：[参数及取值范围]
- **关联工程工具**：[工具]

### 2.3 反应器尺度
[流场布局、内构件、接触方式等反应器设计启示]
- **关键设计参数**：[参数及取值范围]
- **关联工程工具**：[如 CFD、COMSOL]

### 2.4 系统尺度
[多级串联、循环回路、冗余设计等系统架构启示]
- **关键设计参数**：[参数及取值范围]
- **关联工程工具**：[如 GPS-X、BioWin]

## 3. 机制详解

### 3.1 [机制名称]
**现象**：[描述]
**原理**：[科学原理]
**关键特征**：[支撑该机制的关键生物特征]
**仿生设计启示**：[从生物到工程的设计思路]

### 3.2 [机制名称2（如有）]

## 4. 改造与优化启示
- **适用改造场景**：[具体场景]
- **仿生改造思路**：[改造方向和参数建议]
- **预期效果**：[改造后可能的改善]

## 5. 已报道性能数据（可选）

## 6. 仿生设计叙事（Biomimetic Narrative）

### 6.1 问题定义（Problem）
### 6.2 生物解决方案（Biological Solution）
### 6.3 关键特征提取（Key Features）
### 6.4 设计思路映射（Design Mapping）
### 6.5 可解释性锚点（Explainability Anchors）

## 7. 适用场景
[最适合 / 不适用]

## 8. 相关原型
- [原型]：[关联说明 + 关系类型（协同/替代/互补）]

## 参考文献
```

**关键决定**：多尺度设计启示（2.1-2.4）为必填字段。即使某尺度暂无明确启示，写"暂无明确启示"以迫使建库者系统思考。

## 4. 领域列表与分类体系

### 4.1 十三个领域

| 领域 ID | 名称 | 覆盖范围 |
|---------|------|----------|
| `fluid-mechanics` | 流体力学 | 减阻、湍流控制、混合强化 |
| `biochemical-reactions` | 生化反应 | 代谢反应机制、酶催化、氧化还原 |
| `separation-filtration` | 分离/过滤 | 逆流交换、高效过滤、分子筛分 |
| `microbial-community` | 微生物群落 | 群落结构、功能分工、种间互作 |
| `biofilm` | 生物膜 | 生物膜形成、成熟、脱落、调控 |
| `metabolic-pathways` | 代谢路径 | 代谢链、协同降解、物质循环 |
| `mass-transfer` | 传质与流场 | 对流传质、扩散传质、流场优化 |
| `solid-liquid-separation` | 固液分离 | 絮凝、沉降、过滤、膜分离 |
| `shock-resistance` | 抗冲击与自恢复 | 韧性机制、休眠/复苏、缓冲 |
| `resource-recovery` | 资源化 | 碳源回收、磷回收、能源回收、再生水 |
| `energy-drive` | 能源/驱动 | 光合作用、化学能转化、ATP 驱动 |
| `system-community` | 系统/群落 | 多级净化、物质循环、生态系统 |
| `adsorption` | 吸附 | 化学吸附、物理吸附、结构驱动分离 |

### 4.2 水处理工艺分类（聚焦生化处理段）

```
## 二级处理（生化处理）—— 核心 80%+

### 活性污泥法
- A²/O 及其变体（改良A²/O、UCT、MUCT）
- SBR 及其变体（ICEAS、CASS、DAT-IAT）
- 氧化沟（Carrousel、Orbal、三沟式）
- MBR（膜生物反应器）
- A/O 脱氮、A/O 除磷

### 生物膜法
- 曝气生物滤池（BAF）
- 移动床生物膜反应器（MBBR）
- 生物滤池、生物转盘、生物流化床

### 厌氧处理
- UASB、IC、EGSB、AnMBR、ABR

### 组合工艺
- A²/O + MBR、厌氧+好氧、IFAS（生物膜+活性污泥复合）

## 深度处理（辅助）
- 混凝/絮凝、高级氧化、活性炭吸附

## 污泥处理
- 厌氧消化、好氧消化

## 资源化
- 碳源回收（VFAs）、磷回收（鸟粪石）、再生水、能源回收（沼气）
```

### 4.3 尺度定义

| 尺度 | 定义 | 典型尺寸 | 水处理对应 |
|------|------|----------|-----------|
| 材料 | 材料表面/内部结构 | nm-mm | 吸附剂、催化剂、膜材料、涂层 |
| 组件 | 功能单元/构件 | mm-m | 填料、曝气头、膜组件、内构件 |
| 反应器 | 反应容器/处理单元 | m 级 | 反应池、沉淀池、生物反应器 |
| 系统 | 全流程/多单元组合 | m-km 级 | 污水厂、处理工艺链 |

### 4.4 设计问题分类

- **传质类**：曝气效率低、混合不均匀、死区、短流
- **生物膜类**：生物膜过厚脱落、挂膜困难、填料堵塞
- **固液分离类**：污泥沉降性差、出水悬浮物高、膜污染
- **抗冲击类**：进水水质波动、有毒物质冲击、低温运行
- **能耗类**：曝气能耗高、整体能效优化
- **改造类**：池型优化、流场改造、填料更换、工艺升级

### 4.5 领域概况中的工程工具关联

每个领域的 `domain-profile.md` 需包含"关联工程工具"章节：

```markdown
## 关联工程工具
- **CFD 仿真**（Fluent/OpenFOAM）：用于验证仿生流场设计
  - 关键仿真参数：流速分布、湍流强度、RTD、死区比例
- **多物理场仿真**（COMSOL）：传质-反应耦合分析
- **活性污泥模型**（ASM1/2/3）：生化反应过程模拟
- **过程仿真**（GPS-X/BioWin）：全厂工艺模拟与优化
```

## 5. 多入口路由与匹配机制

### 5.1 五种用户入口

| 入口 | 典型问题 | 路由文件 |
|------|----------|----------|
| 污染物 | "去除 NH₄⁺-N 有什么仿生方案？" | `pollutant-router.json` |
| 工艺 | "我在做 MBR，有什么仿生优化思路？" | `process-router.json` |
| 设计问题 | "曝气效率低，怎么仿生改进？" | `problem-router.json` |
| 改造场景 | "现有 A²/O 池想优化流场" | `retrofit-router.json` |
| 运行调控 | "DO 偏低，怎么调曝气？" | `operation-router.json` |

### 5.2 两阶段路由机制

```
用户输入
    ↓
第一阶段：入口路由 → 识别涉及的 1-3 个领域
    ↓
第二阶段：领域内精确匹配 → 条件预筛 + weight 排序 → top N
    ↓
跨域发现：查询 cross-domain-links.json → 发现关联原型
    ↓
输出：候选原型池 + 多尺度设计启示 + 跨域协同建议
    ↓
LLM 读取原型详情 → 组合推理
```

### 5.3 路由文件结构

**pollutant-router.json**：污染物 → 领域 → 原型列表（含 weight）

**process-router.json**：以工艺类型为主键，包含关联领域、关键原型、改造机会

**problem-router.json**：以设计问题为主键，按尺度分组原型

**retrofit-router.json**：以现有设备/工艺类型为主键（如曝气池、二沉池），包含常见问题、关联领域、仿生改造策略

**operation-router.json**：以调控类型为主键（曝气调控、流道调控、加药调控、污泥调控），包含触发信号、调节目标、仿生调控策略、参考参数

### 5.4 运行调控路由的特殊设计

`operation-router.json` 面向实时运行控制场景：

```
多维传感器 → 数据采集 → 建模/分析（ASM/CFD/ML）
                                ↓
                  识别需要调控的操作点
                                ↓
      查询 operation-router.json（按调控类型匹配）
                                ↓
          获取仿生调控策略 + 参考参数
                                ↓
        操作人员决策 / 自动控制系统执行
```

库不参与实时控制回路（毫秒级），而是作为决策支持层提供仿生参考。

## 6. 跨域关系（cross-domain-links.json）

```json
{
  "synergy_pairs": [
    {
      "prototype_a": "...",
      "prototype_b": "...",
      "relationship": "complementary",
      "context": "...",
      "applicable_domains": ["...", "..."]
    }
  ],
  "substitution_pairs": [
    {
      "prototype_a": "...",
      "prototype_b": "...",
      "relationship": "alternative",
      "context": "...",
      "selection_guide": "..."
    }
  ]
}
```

## 7. 索引文件

### 7.1 原型索引（prototypes/_index.json）

为 LLM 提供快速概览，避免逐个读取所有 prototype.md：

```json
{
  "total": 80,
  "prototypes": [
    {
      "id": "...",
      "name": "...",
      "category": "...",
      "domains": ["..."],
      "scale_coverage": ["material", "component", "reactor", "system"],
      "key_features": ["..."],
      "evidence_level": "high"
    }
  ]
}
```

### 7.2 领域索引（domains/_index.json）

```json
{
  "domains": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "prototype_count": 12,
      "related_domains": ["...", "..."]
    }
  ]
}
```

## 8. 分阶段实施

### 第 1 阶段：搭建骨架
- 创建目录结构
- 设计并确认 prototype-template.md（含多尺度章节）
- 创建 adsorption 领域（从现有数据迁移）
- 创建 2-3 个高优先领域（如 mass-transfer, biofilm, microbial-community）
- 创建 5 个入口路由文件的骨架
- 创建 shared/taxonomy/ 全局分类

### 第 2 阶段：填充领域内容
- 逐步建设剩余领域
- 为吸附原型补充多尺度启示
- 建设 cross-domain-links.json
- 完善 retrofit-router.json 和 operation-router.json

### 第 3 阶段：按需演进
- 如原型超 150 个，可引入 JSON-LD 图架构
- 如需跨尺度路径查询，增加图查询能力
- 如有图数据库需求，可迁移至 Neo4j
