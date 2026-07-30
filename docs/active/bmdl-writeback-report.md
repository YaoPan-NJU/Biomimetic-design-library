# BMDL 回写报告

日期: 2026-06-27 | 更新: 2026-06-27（回退记录）

## Task 5.1: performance_data.pollutant 填充（已回退）

### 原始回写操作

- 总 performance_data: 502
- 修复前空 pollutant: 101
- 回写后空 pollutant: 30
- 回写填充: 71
- 回写率: 70%

### 回写方法分布

| 方法 | 数量 | 说明 |
|------|------|------|
| mechanism context | 45 | 从同索引机制名称提取污染物 |
| value field | 13 | 从性能值文本提取污染物名 |
| matching matrix | 8 | 用匹配矩阵的最高权重污染物 |
| manual context | 5 | 从相邻机制上下文人工判断 |
| **总计** | **71** | |

### 回退记录（2026-06-27）

**决定**: 全部回退 71 条回写，从 `prototypes_db.bak/` 恢复 9 个受影响文件。

**回退原因**: 回写操作混合了两个不同材料体系的数据。

BMDL 的 `performance_data` 来源于仿生吸附文献（重金属吸附、噬菌体去除、油吸收等），
而 2879 篇论文的匹配矩阵/机理上下文来源于有机污染物吸附文献。用后者的数据去填
前者的 `pollutant` 空字段，导致系统性误分类。

**典型错误示例**:
- `chitosan.json` 中 40 条重金属(Cu/Pb/Cd/Cr/As/Hg)吸附数据被标记为"壬基酚"
- `cell-membrane-ion-channel.json` 中膜分离重金属数据被标记为"壬基酚"
- `polydopamine-coating.json` 中 F-/Cr(VI)/Cu(II) 去除数据被标记为有机污染物
- `diatom-frustule.json` 中 matrix 方法数据被标记为"十溴二苯醚"

**受影响文件（9 个）**:

| 文件 | 回写条数 |
|------|----------|
| chitosan.json | 40 |
| cell-membrane-ion-channel.json | 11 |
| polydopamine-coating.json | 6 |
| diatom-frustule.json | 4 |
| fish-scale-hydroxyapatite.json | 2 |
| iron-oxidizing-bacteria.json | 2 |
| mussel-foot-adhesion.json | 2 |
| oyster-shell.json | 2 |
| scallop-shell.json | 2 |

**回退验证**: 恢复后空 pollutant 字段 = 101（与回写前一致）。

### 教训

1. **知识隔离原则不可违反**: 2879 篇有机污染物论文的提参结果独立存储在
   `pollutant_knowledge_base/` 下，不应用于回填 BMDL 自有的 `performance_data`。
   BMDL 的 `performance_data` 是来自仿生吸附文献的重要证据，两者属于不同材料体系。

2. **正确的增益方向**: 2879 篇论文给 BMDL 的增益仅限于：
   - 污染物基本性质（物化性质摘要）
   - 文献报道的去除机理（什么作用力、贡献比例）
   不包括性能数据（qmax 等），不应混入 BMDL 自有数据。

3. **匹配矩阵的正确用途**: `matching_matrix.md` 作为设计辅助参考，帮助 BMDL 根据
   用户输入的污染物性质推荐仿生原型，不用于回填 `performance_data.pollutant`。

### 剩余 101 条空 pollutant 字段（维持原状）

这些条目的 pollutant 字段保持为空。它们不属于特定有机污染物吸附性能，
而是其他类型的性能数据：

| 原型 | 条数 | 数据类型 |
|------|------|----------|
| chitosan | 40 | 重金属/染料/抗生素吸附 |
| cell-membrane-ion-channel | 11 | 膜分离重金属/油水分离 |
| mussel-foot-adhesion | 9 | 响应润湿性/聚合物刷性能 |
| polydopamine-coating | 9 | 超疏水抗菌/F-/Cr(VI)去除 |
| superhydrophobic-artificial | 8 | 油吸收容量 (g/g) |
| diatom-frustule | 4 | matrix 方法/硅藻 frustule |
| lotus-leaf | 4 | 油水分离/微塑料去除 |
| iron-oxidizing-bacteria | 4 | 元素组成 (Fe:S:K:Se) |
| fish-scale-hydroxyapatite | 3 | Cd(II)/Pb(II) 吸附 |
| mangrove-root | 2 | 系统级生态数据 |
| oyster-shell | 2 | Pb(II)/Cu(II) 吸附 |
| scallop-shell | 2 | Pb(II)/Cu(II) 吸附 |
| silk-fibroin | 1 | 通用描述 |
| mycelium | 1 | 通用描述 |
| pitcher-plant-slippery-surface | 1 | 通用描述 |
| **合计** | **101** | |

这些空字段是 BMDL 自有数据的问题，应由 BMDL 自身的文献溯源来解决，
而非用 2879 篇有机污染物论文的数据回填。

## Task 5.2: feature_matching_rules.json 扩充

待 Yao 确认 rule_gaps.md 中的 7 条新规则后执行。
注意：新增规则是基于 2879 篇论文的分子特征→原型关联，属于特征匹配规则扩充，
不涉及 performance_data 回填，不违反知识隔离原则。
