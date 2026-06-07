# 生物原型知识库 / Biological Prototype Knowledge Base

> 水处理仿生吸附材料开发智能体系统的核心知识组件。
>
> 当前工作分支：`feature/extraction-results`
> 数据快照：2026-06-07，commit `2656784`

## 项目定位

本知识库为 ADRMATS / 水处理仿生吸附材料开发智能体系统提供仿生检索上下文。用户输入目标污染物和水质条件后，系统可从本库检索候选生物原型、材料特征、条件窗口、机制解释和工程约束，再交给下游设计 Agent 进行组合推理。

重要边界：本库只做检索和上下文供给，不负责最终材料推理。当前数据仍处于 alpha / draft 状态，性能数据尚未通过独立核查，不能直接作为 ADRMATS 的事实排序依据。

## 当前数据盘点

### 原型层

| 层级/字段 | 数量 | 说明 |
|---|---:|---|
| `prototypes/` 原型目录 | 36 | 每个目录含一个 `prototype.md` |
| `prototypes_db/*.json` 结构化原型 | 36 | 当前主要机器可读数据源 |
| `feature-mapping.json#prototype_metadata` | 36 | 检索层 canonical ID |
| `status=active` | 30 | 当前保留为活跃原型 |
| `status=needs_literature` | 6 | 明确缺文献支撑，待补充 |
| `coverage=normal` | 22 | 已有性能数据或较完整条目 |
| `coverage=low` | 14 | 低覆盖，不应作为强证据使用 |

### 原型类别与仿生维度

| 维度 | 数量 |
|---|---:|
| 动物 | 13 |
| 植物 | 9 |
| 微生物 | 7 |
| 仿生材料 | 7 |

| 仿生维度 | 数量 |
|---|---:|
| 结构仿生 | 16 |
| 分子仿生 | 9 |
| 过程仿生 | 6 |
| 功能仿生 | 3 |
| 形态仿生 | 1 |
| 系统仿生 | 1 |

### 结构化知识层

| 信息层 | 数量 | 当前质量状态 |
|---|---:|---|
| `performance_data` 性能数据 | 774 | 全部 `unverified` |
| `mechanisms` 机制条目 | 1,326 | 大量缺 active features / functional groups |
| `engineering_constraints` 工程约束条目 | 301 | 来自原型 JSON 聚合 |
| 缺污染物字段的性能数据 | 238 | 不能进入污染物匹配排序 |
| 缺 `functional_groups` 的机制条目 | 1,297 | 结构仿生条目后续应改为 `active_features` |
| 已核实性能数据 | 0 | `verification=verified` 只能由独立核查产生 |

### 来源与文献提参

| 项目 | 数量 | 说明 |
|---|---:|---|
| 进入 `performance_data` 的去重 `source_file` | 118 | 当前聚合库中实际引用的来源文件数 |
| 去重 DOI | 104 | 仅统计性能数据中的 DOI |
| 去重专利号 | 13 | 仅统计性能数据中的专利来源 |
| 文献来源性能条目 | 667 | `source=literature` |
| 专利来源性能条目 | 107 | `source=patent` |

LitExtract 原始提参结果位于子模块 `tools/litextract`（仓库 `YaoPan-NJU/Literature-extracting.git`，分支 `feature/biomimetic-extraction`）。当前本仓库文档记录的原始提参规模为：

| 原始提参类型 | 已提取数量 | 说明 |
|---|---:|---|
| 论文 JSON | 275 | 来自 `outputs/extractions/论文/json/` |
| 专利 JSON | 33-37 | 33 个有效专利，另有重复/版本差异记录 |
| 标准 JSON | 3 | 6 个标准中已提取 3 个 |
| 合计 | 311-315 | 口径差异来自专利重复 JSON 是否计入 |

注意：`prototypes_db` 是对 LitExtract 原始 JSON 的聚合结果。原始 311-315 个 JSON 并不等于全部都已进入性能数据；当前性能数据层实际去重来源为 118 个 `source_file`。

## feature-mapping.json 盘点

| 层级 | 字段 | 数量 |
|---|---|---:|
| Layer 1 条件预筛 | `prototype_metadata` | 36 原型 |
| Layer 1 条件预筛 | `tested_conditions` | 33 原型 |
| Layer 2 污染物匹配 | `pollutant_prototype_map` | 83 个污染物/子污染物键，200 条原型引用，29 个唯一原型 |
| Layer 2 特征匹配 | `feature_prototype_map` | 26 个特征键，79 条原型引用，33 个唯一原型 |
| Layer 3 机制桥接 | `mechanism_feature_bridge` | 16 个机制键 |
| Layer 4 工程约束 | `constraint_prototype_map` | 5 类约束，258 条原型约束引用，25 个唯一原型 |

约束类别包括：

| 约束类别 | 条目数 | 覆盖原型数 |
|---|---:|---:|
| `regeneration` | 128 | 18 |
| `pH_sensitivity` | 63 | 14 |
| `stability` | 52 | 18 |
| `temperature_sensitivity` | 14 | 7 |
| `salinity_tolerance` | 1 | 1 |

## 当前主要风险

1. 所有性能数据仍为 `unverified`，不能直接作为 ADRMATS 事实排序依据。
2. 部分原型存在 chimera / 串库问题，即不同生物原型或综述材料被混入同一原型。
3. 机制条目中混有实例级性能描述，需要拆分为 `mechanisms` 与 `mechanism_instances`。
4. 结构仿生原型不应强行使用 `functional_groups`，后续应统一为更通用的 `active_features`。
5. `prototype.md` 是可读投影，`prototypes_db/*.json` 才是当前主要机器可读层。

## 推荐使用方式

### 面向 ADRMATS

当前只建议使用：

- `feature-mapping.json` 做候选原型召回；
- `prototypes_db/*.json` 做上下文读取；
- `status`、`coverage`、`verification` 控制可信度；
- 未 verified 的性能数据只作为线索，不参与硬排序。

不建议直接使用：

- 未核查的 qmax / removal rate 作为设计优先级依据；
- 低覆盖原型作为强推荐依据；
- 未清理的机制条目作为最终解释。

### 面向整改

优先顺序：

1. 增强 `tools/validate_consistency.py`，新增严格 provenance 与 chimera 检查。
2. 新建 `tools/check_chimera.py`，先清理 6 个已知 chimera 原型。
3. 将机制层拆成 `mechanisms` 与 `mechanism_instances`。
4. 先把 `mussel-foot-adhesion` 做成 verified 金标准原型。
5. 金标准流程跑通后，再处理 `metal-organic-framework`、`chitosan`、`lotus-leaf`、`alginate`。

## 目录结构

```text
Biomimetic-design-library/
├── README.md
├── feature-mapping.json              # 检索映射层
├── prototypes/                       # 面向人读的 prototype.md
├── prototypes_db/                    # 机器可读结构化原型库
├── taxonomy/                         # 分类体系定义
├── templates/                        # 原型模板
├── tools/                            # 构建、清理、校验脚本
│   └── litextract/                   # LitExtract 子模块（原始提参工具与 JSON）
└── docs/                             # 审查、质量与修复文档
```

## 关键文件

| 文件 | 用途 |
|---|---|
| `feature-mapping.json` | 污染物/特征/约束到原型的检索映射 |
| `prototypes_db/*.json` | 结构化原型、性能、机制、约束数据 |
| `prototypes/*/prototype.md` | 面向人读的原型摘要 |
| `tools/build_prototypes_db.py` | 从 LitExtract JSON 聚合构建结构化库 |
| `tools/verify_data.py` | 批量核查性能数据的初版脚本 |
| `tools/validate_consistency.py` | 一致性校验脚本 |
| `优化方案_v2综合_2026-06-07.md` | 当前整改方案 |

## 相关仓库

| 仓库 | 关系 |
|---|---|
| `YaoPan-NJU/Biomimetic-design-library` | 本知识库 |
| `YaoPan-NJU/Literature-extracting` | LitExtract 提参工具与原始 JSON 来源 |

