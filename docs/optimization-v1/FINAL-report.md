# FINAL Report — 仿生库整改总验收

> 分支：`opt/curation-grounding-v1`
> 当前 HEAD：`096c281`（Phase 9 基线）
> Phase 8 patch：`333b092`
> 日期：2026-06-15

---

## 1. Phase 0–9 总结

| Phase | 内容 | Commit | 状态 |
|-------|------|--------|------|
| 0 | 基线冻结 | `9633aeb` | ✅ |
| 1 | 接口诚实度 P0 bug | `9633aeb` | ✅ |
| 2 | 策展落地 | `9633aeb` | ✅ |
| 3 | chimera 全字段清理 | `48e2cf4` | ✅ |
| 4 | 字段语义+诚实标注 | `48e2cf4` | ✅ |
| 5 | 因果链补全 | `0b49533` | ✅ |
| 6 | PDF 逐条核验 | `c7bee7f` | ✅ |
| 7 | 设计转译重做 | `e78ea8c` + `6a7a9fa` | ✅ |
| 7.5 | 接口候选排序诚实度 | `437eb9f` | ✅ |
| 8 | 失效边界+DO-NOT | `53dff3c` | ✅ |
| 8 patch | schema/护栏修复 | `333b092` | ✅ |
| 9 | 打包与总验收 | 本报告 | ✅ |

---

## 2. Phase 7.5 修复摘要

**问题**：`query()` 取 `mechanisms[0]`，很多原型首条 mechanism 是 `needs_review`，导致强排序展示未核实机制。

**修复**：
- 机制选择按 verification 优先级排序（verified > corroborated > needs_review）
- 添加 `confidence: low` 标记
- `verify_adrmats_delivery.py` 适配 + python3→python
- pitcher-plant 添加 `function: anti_fouling`

---

## 3. Phase 8 + Patch 摘要

**Phase 8 初版**：
- 修复 17 条数值护栏违规（B 档 text 含数字 → 定性化）
- 从 design-rules.json CM 规则补全 23 条 B 档边界
- 新建 `check_boundary_guardrail.py` + `export_do_not.py`
- `biomimetic_context.py` 添加 `rule_based_cautions`
- `literature-requests.md` 追加 dna-aptamer 请求

**Phase 8 patch**：
- 修复 3 条隐藏数值阈值（plant-tannin `condition.value=[10]`，silk-fibroin `condition.value=[2,11]` ×2）
- 修复 SRB boundary `from_source`/`verification` 不一致
- 升级 `check_boundary_guardrail.py` 至 8 项检查

---

## 4. 最终统计

| 指标 | 数值 |
|------|------|
| active 原型 | 24 |
| materials_reference | 4 |
| parked | 1 |
| 机制总数 | 534 |
| 因果链卡（合格）| 28 张（覆盖 24/24）|
| PDF 已核验 verified | 23 张 |
| boundary_conditions | 62 条 |
| **硬 DO-NOT** | **0 条** |
| **软 caution** | **62 条** |
| design_translation | 25 条（2 literature / 23 llm_inference）|
| 校验错误 | 0 |
| chimera 违规 | 0 |

---

## 5. 验收命令与实际结果

### check_boundary_guardrail.py
```
active 原型数: 24, 总 BC 条数: 62, 硬 DO-NOT: 0, 软 caution: 62
✅ 缺少 BC 的原型=0
✅ BC 缺必填字段=0
✅ basis 非法值=0
✅ 隐藏数值阈值=0
✅ text 含数字=0
✅ gate_level 不一致=0
✅ from_source 但 locator 缺失/无效=0
✅ verified 但 locator 缺失/无效=0
✅ 验收通过
```

### export_do_not.py
```
导出完成: exports/adrmats_do_not.json
总边界条数: 62, 硬 DO-NOT: 0, 软 caution: 62, 涉及原型: 24
```

### verify_adrmats_delivery.py
```
[PASS] PFOA 痕量吸附去除
[PASS] SMX 抗生素吸附去除
[PASS] BPA 内分泌干扰物去除
[PASS] Pb(II) 重金属离子去除
[PASS] validate_consistency.py: 0 error
[PASS] check_chimera.py: 0 violation
总计: 6 通过, 0 失败
[PASS] 验收通过
```

### test_interface_honesty.py
```
PASS: 空 pollutant 不匹配
PASS: verification_tier 读取机制真实值
PASS: main() 正常运行
All 3 tests PASSED
```

### check_translation_specificity.py
```
总条数: 25, 合格: 25, 不合格: 0
✅ 验证通过
```

### check_chimera.py --strict
```
违规原型: 0, 总违规数: 0
✅ 严格模式：无违规
```

### validate_consistency.py
```
错误: 0, 警告: 193（预存在的非关键警告）
✅ 报告模式：无错误
```

---

## 6. 残留风险

1. **0 条硬 DO-NOT**：所有边界均为 B 档（llm_inferred + needs_review），未从 PDF 逐条核验。如需硬约束，需学生下载文献后按 A 档核验。

2. **5 个原型无对口 PDF**：coral-skeleton、magnetic-bacteria、pitcher-plant、lobster-exoskeleton、spider-silk 的边界为 placeholder。`literature-requests.md` 已写 8 条检索请求。

3. **silk-fibroin 重复机制**：存在两个同名"吸附机制" mechanism 及重复 BC，pre-existing 数据质量问题，留待后续清理。

4. **needs_review 可进入候选**：低置信候选仍会出现（标记 `confidence: low`），但高置信候选展示 verified 机制。

---

## 7. 是否建议入库

**待 final acceptance review**。

当前状态：Phase 9 打包完成，全套验收脚本全绿。但以下事项需 final review 确认：

- 0 硬 DO-NOT 是否可接受（当前全部是 soft caution）
- 5 个无对口 PDF 的原型边界是否足够
- 是否需要抽查 PDF 证据链
- README / SUPPORT 文档是否与真实统计一致

---

## 8. 关键承诺

- **0 hard DO-NOT / 62 soft caution**：未夸大为硬约束
- 所有 brief 由 `BiomimeticContext.query()` 真实生成
- 未运行 `build_prototypes_db.py`
- 未将 `llm_inferred` 升级为 `verified`
- 未为通过验收删除 unresolved 风险

---

*Phase 9 完成，待 final acceptance review。*
