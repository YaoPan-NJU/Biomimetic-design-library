# Phase 8 Report — 失效边界与 DO-NOT 输出

## 执行时间
2026-06-15

## 1. Phase 7.5 前置修复

### 问题
`query()` 取 `mechanisms[0]` 时，很多原型首条 mechanism 是 needs_review，导致强排序候选展示未核实机制。

### 修复
- `biomimetic_context.py`：机制选择按 verification 优先级排序（verified > corroborated > needs_review），添加 `confidence` 标记
- `verify_adrmats_delivery.py`：needs_review + `confidence != 'low'` 才报错；python3→python
- `pitcher-plant-slippery-surface.json`：添加 `function: anti_fouling`

### 验收：6/6 PASS ✅

---

## 2. Phase 8.1 — 审计修复现有 boundary_conditions

### 发现的问题
- **17 条数值护栏违规**：`basis=llm_inferred` 但 text 含具体 pH/浓度数字
- **1 条 gate_level 不一致**：sulfate-reducing-bacteria gate 为空

### 修复
将 17 条含数字的 B 档边界改写为定性描述（如 "pH < 3时壳聚糖溶解" → "强酸性条件下壳聚糖溶解"），同时将 `condition.operator` 从 `threshold_gt/threshold_lt` 改为 `qualitative`。修复 sulfate-reducing-bacteria 的 gate_level 为 `soft`。

### 验收：0 违规 ✅

---

## 3. Phase 8.2 — B 档资产补全 boundary_conditions

### 方法
从 `docs/imported/library-enhancement/design-rules.json` 的 22 条 CM 规则中，按 `affected_prototypes` 映射到 active 原型，为每个 qualified 机制添加 1-3 条定性边界。

### 结果
- 新增 23 条边界，涉及 17 个原型
- 最终：28 个 qualified 机制全部有 BC，共 62 条
- 平均每个 qualified 机制 2.2 条 BC

### 各原型边界数
| 原型 | BC 数 | 原型 | BC 数 |
|------|-------|------|-------|
| mussel-foot-adhesion | 11 | chitosan | 8 |
| plant-tannin | 3 | pitcher-plant | 3 |
| sulfate-reducing-bacteria | 3 | bone-structure | 2 |
| cell-membrane-ion-channel | 2 | chlorella-cell-wall | 2 |
| coral-skeleton | 2 | diatom-frustule | 2 |
| dna-aptamer | 2 | iron-oxidizing-bacteria | 2 |
| lobster-exoskeleton | 2 | magnetic-bacteria | 2 |
| mycelium | 2 | oyster-shell | 2 |
| polydopamine-coating | 2 | silk-fibroin | 2 |
| spider-silk | 2 | biomineralization-template | 2 |
| fish-scale-hydroxyapatite | 1 | mangrove-root | 1 |
| scallop-shell | 1 | wood-xylem | 1 |

---

## 4. Phase 8.3 — C 档文献检索请求

### 更新 `docs/optimization-v1/literature-requests.md`
追加 1 条：dna-aptamer 在不同 pH/温度/离子强度下的结合稳定性。

现有 8 条检索请求覆盖：
- coral-skeleton: 2 条
- magnetic-bacteria: 2 条
- pitcher-plant: 1 条
- lobster-exoskeleton: 1 条
- spider-silk: 1 条
- dna-aptamer: 1 条（新增）

---

## 5. Phase 8.4 — 校验与导出脚本

### `tools/check_boundary_guardrail.py`（新建）
检查项：
1. 每个 active 原型 ≥1 条 boundary ✅
2. 数值阈值护栏违规=0 ✅
3. gate_level 一致性=0 ✅
4. verified BC 有 locator ✅

### `tools/export_do_not.py`（新建）
输出 `exports/adrmats_do_not.json`：62 条边界，0 hard DO-NOT，62 soft cautions。

---

## 6. Phase 8.5 — 接口更新

### `tools/biomimetic_context.py`
- 新增 `_collect_rule_based_cautions()` 方法
- `query()` 返回的 brief 新增 `rule_based_cautions: {do_not: [...], cautions: [...]}`
- 按当前查询工况（pH/温度/盐度）匹配候选原型的 boundary_conditions
- hard 进 DO-NOT，soft 进 caution

### `tools/verify_adrmats_delivery.py`
- `validate_brief_structure()` 新增 `rule_based_cautions` 字段检查
- 验证 hard cautions 的 verification 必须是 verified/corroborated

---

## 7. 验收结果（全部为绿）

| 验收命令 | 结果 |
|----------|------|
| `check_boundary_guardrail.py` | ✅ 数值护栏违规=0, gate_level 一致=0, 每原型≥1 BC |
| `export_do_not.py` | ✅ 生成 exports/adrmats_do_not.json |
| 导出 JSON 断言 | ✅ 62 条, 硬DO-NOT=0, gate_level+basis 齐全 |
| `verify_adrmats_delivery.py` | ✅ 6/6 PASS |
| `test_interface_honesty.py` | ✅ 3/3 PASS |
| `check_translation_specificity.py` | ✅ 25/25 合格 |
| `check_chimera.py --strict` | ✅ 0 违规 |
| `validate_consistency.py` | ✅ 0 错误 |

---

## 7.5 Review 后修补（放行前修复）

Phase 8 初版提交后经 review 发现以下问题，已全部修复：

### 已修复：3 条隐藏数值阈值

这些 BC 的 `text` 已在 Phase 8.1 改为定性描述，但 `condition.value` 仍保留数值，违反"B 档 / llm_inferred 不得携带数字阈值"规则。

| 原型 | 修复前 condition | 修复后 |
|------|-----------------|--------|
| plant-tannin | `{"operator":"threshold_gt","value":[10]}` | `{"operator":"qualitative","value":null}` |
| silk-fibroin (×2) | `{"operator":"range","value":[2,11]}` | `{"operator":"qualitative","value":null}` |

### 已修复：SRB boundary from_source/verification 不一致

`sulfate-reducing-bacteria` 的 "SRB是严格厌氧菌" BC 原标记 `basis=from_source` + `locator="biology knowledge"`，但 "biology knowledge" 不算真实 locator，不构成 from_source 证据。

修复：`basis → llm_inferred`，`verification → needs_review`，`locator → null`。

### 已升级：check_boundary_guardrail.py

新增 5 项检查：
- BC 必填字段完整性（text/parameter/condition/basis/gate_level/verification）
- basis 合法值（仅 from_source | llm_inferred）
- `basis≠from_source` 时 `condition.value` 必须为 null
- `locator="biology knowledge"` 不算真实 locator
- `basis=from_source` 时 `verification` 必须为 verified/corroborated

### 已记录：silk-fibroin 重复机制

silk-fibroin 存在两个同名 "吸附机制" mechanism 且带重复 BC，属于 pre-existing 数据质量风险。不在本次小修中合并机制，留待后续清理。

### 当前状态

- 0 硬 DO-NOT / 62 软 caution（未夸大为硬约束）
- check_boundary_guardrail.py: 8 项检查全绿

---

## 8. 残留风险

1. **0 条硬 DO-NOT**：所有边界均为 B 档（llm_inferred + needs_review），因为 Phase 6 核验的 PDF 主要覆盖正向机制，边界条件未被逐条从 PDF 中提取。如需硬 DO-NOT，需从 PDF 中逐条摘取边界并核验。

2. **4 个原型的边界标记为 "待文献支撑"**：biomineralization-template、coral-skeleton、dna-aptamer、magnetic-bacteria 的 BC 为 placeholder。需学生下载对应文献后按 A 档核验。

3. **verify_adrmats_delivery.py 的 needs_review 排名**：已通过 Phase 7.5 修复，但若原型所有机制都是 needs_review，该原型仍会出现在候选中（标记 confidence: low）。

4. **silk-fibroin 重复机制**：存在两个同名 "吸附机制" mechanism 及重复 BC，pre-existing 数据质量问题，留待后续清理。

---

## 9. 关键文件

| 文件 | 修改类型 |
|------|----------|
| `tools/biomimetic_context.py` | Phase 7.5 排序修复 + Phase 8.5 cautions |
| `tools/verify_adrmats_delivery.py` | Phase 7.5 适配 + Phase 8.5 cautions 检查 |
| `tools/check_boundary_guardrail.py` | 新建 |
| `tools/export_do_not.py` | 新建 |
| `exports/adrmats_do_not.json` | 生成 |
| `prototypes_db/*.json` | 13 个文件修复数值护栏 + 17 个文件补全 BC |
| `docs/optimization-v1/literature-requests.md` | 追加 dna-aptamer 请求 |
| `docs/optimization-v1/phase7.5-report.md` | Phase 7.5 报告 |
| `docs/optimization-v1/phase8-report.md` | 本报告 |

---
*Phase 8 完成，待复核*
