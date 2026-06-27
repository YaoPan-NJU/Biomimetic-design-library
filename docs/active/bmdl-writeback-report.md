# BMDL 回写报告

日期: 2026-06-27

## Task 5.1: performance_data.pollutant 填充

- 总 performance_data: 502
- 修复前空 pollutant: 101
- 修复后空 pollutant: 30
- 已修复: 71
- 修复率: 70%

### 修复方法分布

| 方法 | 数量 | 说明 |
|------|------|------|
| mechanism context | 45 | 从同索引机制名称提取污染物 |
| value field | 13 | 从性能值文本提取污染物名 |
| matching matrix | 8 | 用匹配矩阵的最高权重污染物 |
| manual context | 5 | 从相邻机制上下文人工判断 |
| **总计** | **71** | |

### 剩余 30 条空 pollutant 分布

这些条目不属于特定污染物吸附性能，不需要填充 pollutant 字段：

| 原型 | 条数 | 数据类型 |
|------|------|----------|
| superhydrophobic-artificial | 8 | 油吸收容量 (g/g) |
| mussel-foot-adhesion | 7 | 响应润湿性/聚合物刷性能 |
| lotus-leaf | 4 | 油水分离/微塑料去除 |
| polydopamine-coating | 4 | 超疏水抗菌/吸附通用数据 |
| iron-oxidizing-bacteria | 2 | 元素组成 (Fe:S:K:Se) |
| mangrove-root | 2 | 系统级生态数据 |
| 其他 | 3 | 通用描述/CTAB效应 |

## Task 5.2: feature_matching_rules.json 扩充

待 Task 4 rule_gaps.md 审核后执行（需 Yao 确认新规则）。
