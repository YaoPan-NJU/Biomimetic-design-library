# Massive Stage — Track 1 接线补全试点 完成报告

**日期：** 2026-07-29 ｜ **分支：** `massive`（基于 `expand`）

## 做了什么
把"已完整但从未生成映射包"的原型接线补全，让它们对下游可达，并跨通到导出层。全程遵守知识隔离红线（未从姊妹项目搬运任何性能数值），所有目标接线经真源接地对抗验证（见 `massive_stage3_adversarial_ledger.jsonl`）。

## 改动文件（surgical）
- `feature-mapping.json`：`pollutant_prototype_map` 新增 28 条原型接线（保留原有 PO43-/chitosan 条目）；新建 3 个污染物键（Nonylphenol/Cr(VI)/PFOS）。
- `feature_matching_rules.json`：修正 `氟碳链` 误指（超疏水表面 → PFAS 分子识别蛋白 FABP4/HSA/NTCP/hL-FABP）；`离子交换`+3、`沉淀`+scallop-shell；4 个 use_case 补入背景表面原型。
- `adrmats_export/`：重新生成 `match_export.json` / `match_weights.csv` / `_stats.json` / `README.md`。
- `tools/generate_prototype_md.py`：修复渲染工具对旧 schema 变体的健壮性（`tested_conditions`/`provenance_summary`/`narrative` 类型守卫 + 非规范 `organism.category` → 规范四类映射）。
- `prototypes/<12 接线原型>/prototype.md`：全部重渲染，保持 canon↔render 同步。
- `docs/bmdl_rebalance/`：本报告 + triage + 对抗账本。
- **未改任何 `prototypes_db/*.json`**（canon 未动；.md 为渲染产物非 canon）。

## 验收指标（before → after）
| 指标 | before | after |
|------|--------|-------|
| 可达 root 原型 | 70/89（19 不可达） | **86/89（3 不可达）** |
| 剩余不可达 | 19 个 | 3 个（全为 placeholder：biomineralization-template / coral-skeleton / dna-aptamer，query 本就过滤，留 Track 2） |
| 导出 `match_weights` distinct 原型 | 16 | 显著提升 |
| 导出行数 | 130 | **267** |
| 导出覆盖污染物 | 29 | **37** |
| query 抽查 | 有机物只收敛到 chitosan/PDA/单宁/硅藻 | Pb/Cd/Cu/Cr/Hg/PO₄/PFOS/PFBS/BPA/壬基酚 均新增诚实分层候选，未挤掉既有强证据原型 |

## 校验结果
| 脚本 | 结果 |
|------|------|
| validate_consistency.py | 0 errors, 231 warnings（无错误，通过）|
| check_from_source_integrity.py | 1617/1617 compliant ✅ |
| check_causal_chain.py | 616/616 qualified ✅ |
| check_source_authenticity.py | 无 from_source 膨胀/DOI 缺失类硬错误 ✅ |
| check_chimera.py --strict | **exit 1（10 个预存违规，均为 organism 多物种/家族级，非本批引入；本批 12 个接线原型无一违规）** |
| check_boundary_guardrail.py | **exit 1（预存失败，非本批引入）** |

## 预存问题（记录，不在本批修复）
1. **check_boundary_guardrail 失败**：`superhydrophobic-artificial.json`（分离/背景原型，本批未改动）有 from_source 机制标 verification=needs_review。该脚本只读 `prototypes_db/*.json`，为 expand 分支预存失败，属 canon 证据卫生，留待专门修复（本批坚持 canon-freeze，不牵连修改无关原型）。
1b. **check_chimera --strict 10 违规**：均为 organism 字段列多物种（多为蛋白家族跨物种代表，属设计判断而非本批引入）；计划已将嵌合清理（如 spider-silk）列入 Track 2。本批 12 个接线原型经核验无一在违规名单。
2. **prototype.md 渲染（已解决）**：`tools/generate_prototype_md.py` 原对旧 schema 变体（`tested_conditions`/`provenance_summary`/`narrative` 为 list/str、`organism.category` 非规范如真菌/节肢动物）抛 `AttributeError` 或产生非法 category。已修复（类型守卫 + category 映射），12 个接线原型 prototype.md 全部成功重渲染，validate_consistency 回到 0 errors。.md 为渲染产物，不被 query/export 消费。
3. **PFOA 导出全 lane=lead/fact（exploratory=0）**：为 expand 分支 query() 对 PFAS 蛋白原型经 pollutant key-match 置 direct_evidence=True 的预存诚实度口径问题，非本批引入。建议 Track 2 评估 query() 有机域 honesty 计算。

## Track 2 指针
- 修渲染工具 + prototype.md 全量重渲染。
- 源项目 Qwen/Ultimate/kimi-k3/main 的失败但有价值方案挖掘 → 同一对抗验证协议补全为完整原型 + 映射包。
- 3 个 placeholder 原型（biomineralization-template/coral-skeleton/dna-aptamer）补全接地后接线。
- spider-silk 嵌合清理（超疏水/油水/集雾机制与重金属吸附机制分离）。
