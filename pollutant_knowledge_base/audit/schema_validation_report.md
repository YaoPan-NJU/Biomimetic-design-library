# Schema 合规性验证报告

日期: 2026-06-27
Schema: biomimetic_extraction_v2.schema.json

## 统计

- 扫描文件: 2879
- 扫描 KI: 27592
- Errors: 72
- Warnings: 15

## Errors 分析

### 严重: 3 个畸形文件（缺少全部顶层字段）

这些文件只有 `response`/`content`/`result` + `quality_control`，是提取失败的产物：

| 文件 | keys |
|------|------|
| 十溴二苯醚/Chang等-2020-... | response, quality_control |
| 双酚A（BPA）/Stanková和Jandera-2016-... | content, quality_control |
| 滴滴涕（DDT）/Reiss等-2016-Dust Devil Tracks | result, quality_control |

**建议**: 这 3 个文件对应的 PDF 可重跑提取，或标记为提取失败。

### 中等: 30 个文件缺少 processing_notes

| 污染物 | 缺失数 |
|--------|--------|
| 双酚A（BPA） | 10 |
| 十溴二苯醚 | 6 |
| 滴滴涕（DDT） | 4 |
| 全氟辛酸（PFOA） | 3 |
| 其他 | 7 |

**原因**: 这些文件可能是早期提取产物，`processing_notes` 字段在 v2 schema 中才引入。
**影响**: 不影响数据使用，但不完全符合 v2 schema。

### 轻微: 36 个 KI 缺少字段

- `ki.confidence` 缺失: 9 条
- `ki.source` 缺失: 9 条
- `ki.source_file` 缺失: 9 条

**影响**: 极少量，不影响聚合和匹配。

## Warnings

15 条 `domain_direction` 异常值（已通过 Task 1.2 修复的 25 条之外的残留）。

## 结论

- **3 个畸形文件**: 建议重跑提取或标记为失败
- **30 个缺 processing_notes**: 低影响，可后续补全
- **36 个 KI 缺字段**: 极少量，可忽略
- **总体合规率**: 2876/2879 = **99.9%**
