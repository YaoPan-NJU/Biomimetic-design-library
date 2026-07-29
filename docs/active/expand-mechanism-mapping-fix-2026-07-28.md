# expand 分支机制与映射修复记录

日期：2026-07-28  
基线：`expand` / `b5288c0`  
工作分支：`codex/fix-expand-mechanism-mapping`

## 结论

本轮修复了会把“文字命中”误报为“直接证据”的检索根因，重写了 6 个证据边界失真的新增原型，纠正 β-环糊精来源归因，补齐新增原型映射，并清理了严格 chimera 与 boundary gate 的阻断项。修复后，直接证据只来自同污染物的可核验 `performance_data`，探索性生物启发仍可被查询，但统一标为非直接证据。

## 主要修复

1. **直接证据合同**
   - `find_direct_evidence()` 不再因污染物名称出现在映射摘要中就升级候选。
   - 必须同时满足：污染物匹配、`verified/corroborated`、来源标识、locator、verification quote，且 quote 不是 PDF 缺失占位符。
   - 新增回归测试覆盖 PFOA、BPA 与 Pb(II)。

2. **高风险原型纠偏**
   - `laccase-t1-cu-phenol-coordination`：由“酚氧直接配位 T1 Cu”改为邻近口袋预定位与外球电子转移。
   - `rw1-bay-region-dioxygenase`：保留 RW1 角位双加氧；MIP 吸附降为独立工程假设。
   - `ipso-hydroxylation-pathway`：删除无结构证据的形状互补酶口袋主张。
   - `alkb-alkane-hydroxylase-chain-length`：把“固定通道深度”改为有实验底物范围支持、但结构解释待验证的链长门控。
   - `gaba-rdl-rigid-hydrophobic-cavity`：只保留 A302S 抗性所支持的孔区敏感性调制，删除精确腔体尺寸和氢键能外推。
   - `bacterial-photosynthetic-reaction-center`：明确特殊对为初级供体、细菌脱镁叶绿素位于受体侧；水相 CT 吸附降为工程假设。

3. **来源与映射**
   - β-环糊精条目不再用 `10.1039/d0cc04784h` 支撑未追溯的 β-CD:BPA NMR 结合常数。
   - 6 个新增原型补入 `prototype_metadata` 与特征/类别映射；BPA、Nonylphenol、Octocrylene、TCDD、Dieldrin 查询均可命中对应探索原型，`direct_evidence=false`。
   - 油水分离改为显式 use-case 映射；表面物理机制只在该 use case 下恢复可见，不泄漏到普通吸附查询。

4. **治理门禁**
   - 10 个混合 organism 字段改成单一系统或明确的多物种比较原型范围。
   - 198 条缺少合格来源定位或使用旧枚举的 boundary 保守降级为 `llm_inferred + needs_review + soft`；未伪造 locator，也未升级为硬事实。

## 验收结果

| 检查 | 结果 |
|---|---:|
| `validate_consistency.py --strict` | 0 error；96 个 JSON 与 metadata 一致 |
| `check_causal_chain.py` | 625/625 合格 |
| `check_translation_specificity.py` | 97/97 合格 |
| `check_source_authenticity.py` | 0 error；18 个历史 warning |
| `check_from_source_integrity.py` | 1618/1618 合格 |
| `check_chimera.py --strict` | 0 违规 |
| `check_boundary_guardrail.py` | 0 违规 |
| ADRMATS brief usefulness / binding / gold set | 7/7 通过 |
| `test_biomimetic_context.py` | 全部通过 |
| `test_repo_hygiene.py` | 通过 |
| `verify_adrmats_delivery.py` | 6/6 通过 |

## 尚未清除的非阻断项

- 一致性检查仍有 224 个 warning，主要是旧 `prototype.md` 占位符、实例级数字和 5 个历史目录孤儿；不影响本轮严格错误门禁。
- 来源真实性检查仍有 18 个历史 quote 质量 warning；没有 DOI 缺失或 `from_source` 标签膨胀硬错误。
- 本轮纠偏原型多数仍为 `pending_extraction` / `exploratory`，不能表述为已完成全文证据审计或已验证材料性能。
