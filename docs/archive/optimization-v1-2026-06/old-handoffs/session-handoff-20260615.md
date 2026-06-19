# Session Handoff — 2026-06-15（Post-Phase 9）

## 当前状态

- **主分支**：`adsorption/dev`
- **源工作分支**：`opt/curation-grounding-v1`
- **已接受 commit**：`bac696a`（Phase 9 acceptance patch）
- **Phase 进度**：Phase 0-9 已完成，final acceptance review 已通过
- **下一步**：回家后同步 `adsorption/dev`，复跑 post-merge 验收，然后开始证据增强 review

不要再按旧流程启动 Phase 8 或 Phase 9。

## 最新 commit 链

| Commit | 内容 | 状态 |
|---|---|---|
| `437eb9f` | Phase 7.5：接口候选排序诚实度 + pitcher-plant function 字段 | 通过 |
| `53dff3c` | Phase 8：失效边界补全 + DO-NOT 导出 | 通过 |
| `333b092` | Phase 8 patch：修复 schema/护栏问题 | 通过 |
| `ccded69` | Phase 9：打包与总验收 | 通过 |
| `bac696a` | Phase 9 acceptance patch：最终文档和 examples 对齐 | 通过 |

## 当前硬指标

- active 原型：24
- materials_reference：4
- parked：1
- 机制总数：534
- 合格因果链卡：28，覆盖 24/24 active 原型
- PDF 已核验 verified：23
- boundary_conditions：62
- hard DO-NOT：0
- soft caution：62
- official examples：4 个新版 `brief_*.json`
- chimera 违规：0
- validation error：0

## 已通过的最终验收

- `verify_adrmats_delivery.py`：6/6 PASS
- `check_boundary_guardrail.py`：8 项全绿
- `export_do_not.py`：62 条，0 hard，62 soft
- `test_interface_honesty.py`：3/3 PASS
- `check_translation_specificity.py`：25/25 合格
- `check_chimera.py --strict`：0 违规
- `validate_consistency.py`：0 error
- `check_repo_hygiene.py`：PASS

## 回家后先读

1. `docs/optimization-v1/CROSS_DEVICE_HANDOFF_20260615.md`
2. `docs/optimization-v1/HOME_PHASE9_WORK_PLAN_20260615.md`
3. `docs/optimization-v1/FINAL-report.md`
4. `docs/SUPPORT_SCOPE_AND_RISKS.md`
5. `docs/optimization-v1/DEFINITIONS.md`
6. `docs/optimization-v1/literature-requests.md`

## 关键铁律

- 严禁运行 `tools/build_prototypes_db.py`
- canon 唯一真源是 `prototypes_db/*.json`
- 不把 `needs_review` 自动升级为 `verified`
- 不把 `llm_inferred` 自动升级为 `from_source`
- 不把 soft caution 自动升级为 hard DO-NOT
- 具体数值阈值只能来自 PDF 原文 quote
- 证据等级、hard/soft、删除/合并机制都必须进入 decision queue，由 Yao/Codex 决策

## 后续主线

后续不是 Phase 10，而是“证据增强 review”：

1. 同步 `adsorption/dev`
2. 复跑 post-merge 验收
3. 用家里电脑上的原始 PDF 做证据核查
4. 先输出候选表，不直接改数据
5. Yao/Codex 决策后，再修改 `prototypes_db/*.json`
6. 修改后复跑验收

优先级：

1. 5 个待文献原型：coral-skeleton、magnetic-bacteria、pitcher-plant、lobster-exoskeleton、spider-silk
2. 62 条 soft caution 中可被 PDF 明确支持的边界
3. 高频 ADRMATS brief 候选机制
4. silk-fibroin 重复机制清理

## 入口文件

详细执行步骤见：

- `docs/optimization-v1/CROSS_DEVICE_HANDOFF_20260615.md`
- `docs/optimization-v1/HOME_PHASE9_WORK_PLAN_20260615.md`
