# Stage 5 Source of Truth

**日期：** 2026-07-05

---

## 被正式修改的文件

| 文件 | 操作 | 说明 |
|------|------|------|
| `adrmats_export/match_export_stage5.json` | **新建** | Stage 5 正式候选 match_weights，不覆盖原 match_export.json |
| `adrmats_export/match_weights.csv` | **不修改** | 原 CSV 保持不变，Stage 7 切换时才更新 |
| `adrmats_export/match_export.json` | **不修改** | 原导出文件保持不变，作为 before baseline |
| `pollutant_knowledge_base/biomimetic_matching/matching_matrix.json` | **不修改** | 匹配矩阵源文件，Stage 7 才更新 |

## 审计文档（不直接影响数据）

| 文件 | 说明 |
|------|------|
| `docs/bmdl_rebalance/stage5_dry_run_rules.md` | Dry-run 规则定义 |
| `docs/bmdl_rebalance/stage5_match_weight_delta_preview.json` | Dry-run delta |
| `docs/bmdl_rebalance/stage5_risk_review.md` | Dry-run 风险审查 |
| `docs/bmdl_rebalance/stage5_formal_rules.md` | 正式规则定义 |
| `docs/bmdl_rebalance/stage5_formal_delta_report.md` | 正式 delta 报告 |
| `docs/bmdl_rebalance/stage5_risk_resolution_report.md` | 4 个风险项处理结果 |

## 回滚方案

- 原文件 `match_export.json` 未被修改，可随时回滚
- `match_export_stage5.json` 是独立新文件
- Stage 7 导入时才覆盖 RDS 和正式导出文件
