# 生物原型知识库 / Biological Prototype Knowledge Base

水处理仿生吸附材料开发智能体系统的核心组件。

> **👉 库的定位与 brief 结构：[docs/design.md](docs/design.md#0-库的定位北极星)**
> **👉 ADRMATS 集成与分层检索策略：[docs/ADRMATS_INTEGRATION.md](docs/ADRMATS_INTEGRATION.md)**
> **👉 换设备续工作？先读 [docs/HANDOFF.md](docs/HANDOFF.md)**

---

## 当前状态

> 数据快照：2026-06-08 08:15 | 分支：`feature/extraction-results` | commit: `9495f3a`

### 原型层

| 指标 | 数值 |
|------|------|
| prototypes_db/*.json (吸附) | 31 |
| prototypes_db/separation/*.json (分离) | 5 |
| 有性能数据的原型 | 19 |
| 状态：active | 19 |
| 状态：needs_literature | 8 |
| 状态：parked_separation | 5 |

### 结构化知识（吸附原型）

| 指标 | 数值 |
|------|------|
| performance_data 总数 | 752 |
| mechanisms 总数 | 723 |
| engineering_constraints 总数 | 270 |
| 缺 pollutant 的性能数据 | 191 (25%) |
| 缺 active_features 的机制 | 581 (80%) |
| verified | 0 |
| pending_manual_check | 236 |
| needs_review | 16 |
| unverified | 500 |

### feature-mapping.json

| 层级 | 数量 |
|------|------|
| prototype_metadata | 36 |
| pollutant_prototype_map | 83 污染物类别 |
| feature_prototype_map | 26 features |
| mechanism_feature_bridge | 16 mechanisms |
| tested_conditions | 33 |
| constraint_prototype_map | 5 |

---

## 简介

本知识库为"水处理仿生吸附材料开发智能体系统"提供生物原型的结构化数据支撑。当用户输入目标污染物和水质条件后，需求解析Agent从本知识库检索匹配的生物原型，获取其吸附机制和结构特征信息。

## 架构

```
Biomimetic-design-library/
├── README.md                    # 本文件
├── feature-mapping.json         # 特征-原型映射表（四层结构）
├── prototypes_db/               # 正典数据（36个JSON）
├── prototypes/                  # 渲染产物（36个prototype.md）
├── taxonomy/                    # 分类体系
│   ├── organisms.md             # 生物分类
│   ├── mechanisms.md            # 吸附机制分类
│   └── pollutants.md            # 污染物分类
├── templates/
│   └── prototype-template.md    # 原型条目模板
└── docs/
    ├── design.md                # 设计文档
    └── HANDOFF.md               # 换设备续工作入口
```

## feature-mapping.json 结构

四层结构，支持三层匹配机制：

| 层级 | 字段 | 作用 |
|------|------|------|
| Layer 1 条件预筛 | `prototype_metadata[id].applicability` | 按 pH、温度、盐度过滤 |
| Layer 2 污染物匹配 | `pollutant_prototype_map[污染物]` | 按污染物检索 + weight 排序 |
| Layer 2 特征匹配 | `feature_prototype_map[特征]` | 按特征检索（无明确污染物时） |
| Layer 3 机制解释 | `mechanism_feature_bridge` | 特征↔机理桥接 |

**设计原则**：库只做匹配响应，不负责推理。约束识别归前置推理模块，组合推理归下游模块。

## 当前主要风险和使用边界

- ⚠️ **0 条 verified**，236 条 pending_manual_check（MOF 金标准），500 条 unverified
- ⚠️ 191 条性能数据缺 pollutant 字段，无法按污染物匹配
- ⚠️ 581 条机制缺 active_features，无法精细桥接
- ⚠️ 5 个分离簇原型已停放（shark-skin, lotus-leaf, water-strider-leg, cactus-spine, superhydrophobic-artificial）
- ⚠️ 8 个原型 needs_literature（无数据）
- ⚠️ MOF 金标准的 236 条数据需人工开 PDF 确认数值

## 如何使用

本知识库通过 `feature-mapping.json` 提供检索接口：

1. **按污染物检索**：查询 `pollutant_prototype_map[污染物名]` 获取匹配原型及权重
2. **按特征检索**：查询 `feature_prototype_map[特征名]` 获取匹配原型
3. **条件预筛**：根据工况条件（pH、温度等）过滤不适用的原型
4. **机制桥接**：通过 `mechanism_feature_bridge` 理解特征与机理的对应关系

详细设计见 `docs/design.md`。

## 相关专利

隶属于《一种水处理仿生吸附材料开发智能体系统》
