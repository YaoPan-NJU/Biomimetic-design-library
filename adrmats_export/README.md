# ADRMATS Match Export

由 `tools/export_adrmats_snapshot.py` 在 `2026-08-03T12:43Z` 从 `BiomimeticContext.query()` 生成。这是下游集成的权威匹配快照；不要从规则文件重新推导。

## 文件

| 文件 | 用途 |
|---|---|
| `match_export.json` | 完整契约，含证据分级和绑定机制 |
| `match_weights.csv` | 仅用于兼容旧的五列表结构 |
| `_stats.json` | 行数、lane 分布和抽查统计 |

完整 JSON 的关键字段为 `lane`、`direct_evidence`、`performance_evidence_tier`、`candidate_honesty`、`bound_mechanism_id`、`bound_mechanism`。

## 证据语义

| lane | 含义 |
|---|---|
| `fact` | 污染物特异材料去除性能严格核验，且所展示机制已核验 |
| `lead` | 实测去除性能有来源、定位和原文引文，但仍为 partial；或性能严格而机制待核验 |
| `exploratory` | 生物结合、传感、规则映射或机制类比，仅作设计启发 |

`direct_evidence=true` 只用于严格性能事实。`weight` 是同一 lane 内的相关性排序信号，不是置信度，不应跨 lane 直接比较。

## 导出统计

- 污染物：45
- 候选行：638
- fact / lead / exploratory：0 / 81 / 557
- Pb(II)：fact 0，lead 13
- PFOA：lead 2，exploratory 13
- BPA：lead 2，exploratory 13

查询条件固定为 `pH=7.0, temperature=25°C, salinity=low`，每个污染物最多返回 15 个候选。
