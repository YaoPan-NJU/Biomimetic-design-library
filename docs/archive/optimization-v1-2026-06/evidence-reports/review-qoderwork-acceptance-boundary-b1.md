# QoderWork Acceptance: Boundary B1 Writes

status: accepted (6/8), needs_yao (2/8)
reviewer: QoderWork
date: 2026-06-17 23:50 CST

## Spot-Check Summary

| # | Rule | Applied | Spot-Check | Result |
|---|------|---------|------------|--------|
| 1 | B01-CHI-002 | chitosan eng_constraints[60] | PASS | soft_boundary 结构正确，gate_level=soft 匹配 basis=from_source+needs_review |
| 2 | B01-PDA-003 | enrichment PDA | INFO | 17 机制全是吸附相关，之前清除的 21 条已不在了。无需操作。 |
| 3 | B03-CHL-001 | chlorella | DEFERRED | mechanisms[0] 不是 Cheng2021 Pb2+（已被重编号或移除）。需 Yao 确认。 |
| 4 | B03-CMIC-001 | cell-membrane scope_note | PASS | "Separation/desalination prototype" 准确 |
| 5 | B04-SHART-003 | superhydrophobic-artificial | DEFERRED | CN114874407A 不在 performance_data 中。需 Yao 确认目标位置。 |
| 6 | B05-MATREF-001 | 4 materials_ref files | PASS | review_table_caveat 已写入全部 4 个文件 |
| 7 | B07-REG-002 | parked/namib-beetle | PASS | scope_note 正确标注 background only |
| 8 | B13-PDA-OCR-002 | PDA perf[34] | PASS | metric_type + ranking_exclusion + notes 结构正确 |

## 校验结果

- check_boundary_guardrail: PASS（61 BC, 5 hard, 56 soft, pitcher-plant 缺 BC 为既有问题）
- validate_consistency: PASS（0 error, 194 warnings 全为既有）

## 待 Yao 决策

1. **B03-CHL-001**: Cheng2021 Pb2+ 在 chlorella-cell-wall.json 中的位置已变化，mechanisms[0] 现在不是它了。是否还需要添加 scope_caveat？如果是，应该加到哪个 mechanism index？
2. **B04-SHART-003**: CN114874407A 在 superhydrophobic-artificial.json 的 performance_data 中不存在。ownership_note 应该加到机制还是其他位置？

## 后续动作

已写入的 6 项无需进一步操作。2 项待 Yao 回复后处理。
