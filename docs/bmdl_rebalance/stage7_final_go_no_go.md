# Stage 7 Final Go/No-Go

**日期：** 2026-07-05
**状态：** GO — 待潘老师回来后执行 production cutover

---

## GO 条件

| 条件 | 状态 |
|------|------|
| ADRMATS BMDL_SCHEMA 环境变量补丁 | ✅ commit `5cb5902` |
| BMDL release candidate 导出 | ✅ 132 rows, all checks pass |
| Staging import 验证 | ✅ 48 protos, 132 mw, 1020 pd |
| Query regression 8 pollutants | ✅ all assertions pass |
| Validator 0 errors | ✅ |
| BPA/PFOA direct evidence #1 | ✅ plant-lignocellulosic |
| MOF/quarantined 排除 | ✅ |
| bone/oyster 降权 | ✅ |
| PDA/mussel 去重 | ✅ |
| Top-5 concentration 下降 | ✅ 70%→61.8% |
| Production 未被触碰 | ✅ |

## 已知风险

| 风险 | 严重性 | 说明 |
|------|--------|------|
| PFOS 无 direct evidence | 低 | 严格分桶 PFOS≠PFOA，正确行为。Stage 7 后可补充 |
| AC+BC 7.2% 未达 15% | 中 | 高质量证据已耗尽，接受为 Stage 4 最终值 |
| chitosan share 21.8% | 中 | evidence-based (direct + 102 pd)，可接受 |
| bmdl_repository SCHEMA 硬编码已修复 | 已解决 | 改为 `os.environ.get("BMDL_SCHEMA", "bmdl")` |

## 建议

**建议潘老师回来后和 Codex 一起审计，然后执行 production cutover**：

1. 审计 release candidate match_weights
2. 执行逻辑备份
3. 执行 schema rename 或 final import
4. 跑 ADRMATS E2E 回归测试
5. 确认 production 查询正常

**不建议在潘老师不在场时执行 production cutover。**
