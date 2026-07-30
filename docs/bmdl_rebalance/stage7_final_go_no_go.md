# Stage 7 Final Go/No-Go

**日期：** 2026-07-05
**状态：** CONDITIONAL GO — 待潘老师审计 + ADRMATS E2E smoke test 后执行 production cutover

---

## GO 条件

| 条件 | 状态 |
|------|------|
| ADRMATS BMDL_SCHEMA 环境变量补丁 | ✅ commit `5cb5902` |
| BMDL release candidate 导出 | ✅ commit `4f420f5` (132 rows, all checks pass) |
| Staging import 验证 | ✅ commit `63cbcbe` (48 protos, 132 mw, 1020 pd) |
| Query regression 8 pollutants | ✅ all assertions pass |
| Validator 0 errors | ✅ |
| BPA/PFOA direct evidence #1 | ✅ plant-lignocellulosic-architecture |
| MOF/quarantined 排除 | ✅ |
| bone/oyster 降权 | ✅ |
| PDA/mussel 去重 | ✅ |
| Top-5 concentration 下降 | ✅ 70%→61.8% |
| Production 未被触碰 | ✅ |
| Ad-hoc BMDL_SCHEMA 验证 | ✅ 5/5 passed |

## 上线前必跑项（BMDL regression 未覆盖）

| 必跑项 | 责任层 | 说明 |
|--------|--------|------|
| **医院废水 fallback E2E** | ADRMATS task 层 | `_get_relevant_water_data()` 三种场景：① 市政 WWTP → 查库 ② 无水类型 → 实验室环境 ③ 其他废水 → LLM 推理。BMDL 层不负责此 fallback，production cutover 前必须由 ADRMATS E2E 验收。 |
| ADRMATS 完整设计流程 | ADRMATS orchestrator | BPA/PFOA 设计流程 end-to-end |
| 水质约束注入 | ADRMATS adaptive_constraining_task | 确认不再无条件注入二沉池数据 |

## 已知风险

| 风险 | 严重性 | 说明 |
|------|--------|------|
| PFOS 无 direct evidence | 低 | 严格分桶 PFOS≠PFOA，正确行为。Stage 7 后可补充 |
| AC+BC 7.2% 未达 15% | 中 | 高质量证据已耗尽，接受为 Stage 4 最终值 |
| chitosan share 21.8% | 中 | evidence-based (direct + 102 pd)，可接受 |

## 建议

**CONDITIONAL GO**：

1. 潘老师审计 release candidate match_weights
2. Codex 审计代码改动
3. 执行 ADRMATS E2E smoke test（含医院废水 fallback）
4. 执行逻辑备份
5. 通过环境变量切换 `BMDL_SCHEMA=bmdl_staging`（推荐方案，零 drop production）
6. 重启 ADRMATS + 验证

**不建议在潘老师不在场时执行 production cutover。**
