# HANDOFF — 换设备续工作入口

> **唯一执行入口：[ADRMATS_DELIVERY_PLAN.md](ADRMATS_DELIVERY_PLAN.md)**

---

## 当前状态（2026-06-08 13:30）

| 指标 | 数值 |
|------|------|
| 分支 | `feature/extraction-results` |
| 最新 commit | `f47a3af` |
| prototypes_db/*.json | 31 |
| 性能数据总数 | 752 |
| verified | 0 |
| single_source | 236 |
| unverified | 500 |
| needs_review | 16 |
| 校验错误 | 0 |
| chimera 违规 | 0 |

## 怎么续上

1. 读 [ADRMATS_DELIVERY_PLAN.md](ADRMATS_DELIVERY_PLAN.md)
2. 按 Milestone 0-4 顺序执行
3. 每个 milestone 完成后 commit + push

## 关键文件

| 文件 | 用途 |
|------|------|
| `docs/ADRMATS_DELIVERY_PLAN.md` | 唯一执行入口 |
| `tools/biomimetic_context.py` | ADRMATS 接口 |
| `tools/verify_adrmats_delivery.py` | 验收脚本（待创建） |
| `tools/validate_consistency.py` | 校验脚本 |
| `tools/check_chimera.py` | chimera 检测 |
| `feature-mapping.json` | 污染物-原型映射 |
| `feature_matching_rules.json` | 匹配规则数据化 |
| `prototypes_db/` | 正典数据 |

---

*本文档只指向 ADRMATS_DELIVERY_PLAN.md，不维护独立状态。*
