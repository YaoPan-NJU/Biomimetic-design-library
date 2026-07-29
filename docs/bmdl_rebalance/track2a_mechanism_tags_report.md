# Track 2A — mechanism_tags 派生与机制层激活报告

**日期：** 2026-07-29 ｜ **分支：** `massive`

## 覆盖
- **89/89 原型**获得 `mechanism_tags`（无空）。派生来源=各原型既有 `mechanisms[]`（name/causal_chain.interaction/functional_groups/key_structures/transferable_principle）+ 顶层 features，按 `track2a_vocab.md` 关键词规则映射到 canonical 机制。
- 机制分布：氢键 57 · 配位螯合 56 · 几何识别 52 · 孔道限域分子筛分 46 · 疏水分配 41 · 静电吸附 40 · 还原催化降解 27 · π-π堆积 21 · 离子交换 17 · 沉淀共沉淀 16 · 超浸润分离 14 · 生物矿化 8。
- 精度调优：`配位螯合` 由裸词"配位"（命中否定/顺带语境）过宽 63→收紧为 56（改用 螯合/金属配位/巯基/氨基/羧基 等具体词），moda 正确去掉 配位螯合。
- 样例：moda=[静电吸附,氢键,孔道限域分子筛分,几何识别]；scallop=[配位螯合,离子交换,氢键,沉淀共沉淀,生物矿化]；fabp4=[配位螯合,氢键,疏水分配,孔道限域分子筛分,几何识别]；lotus=[…,疏水分配,超浸润分离,…]。

## 改动
- 89 个 `prototypes_db/*.json` 新增 `mechanism_tags`（受控增量字段，未改既有 mechanism 内容/证据标签）；86/89 为纯增量单字段，3 个（hl-fabp/oat4/serine-protease）附带 compact-line 归一（cosmetic，共 5 行删除）。
- `feature_matching_rules.json` 新增 `canonical_mechanisms` / `interaction_to_mechanism` / `molecular_feature_to_mechanism`。
- `tools/biomimetic_context.py`：新增 `find_mechanism_based()`（pollutant 特征/相互作用→canonical 机制→原型经 mechanism_tags 倒排 + feature_prototype_map 次级），并入 `query()` 候选（direct→机制→feature）；`pollutant_prototype_map` 降级——`direct_evidence` 仅当原型对该污染物有真实 performance_data。match_basis 用既有白名单值 `mechanism_feature_bridge`。

## 验证
- **机制层生效**：SMX 候选 3→9；PO43- 机制候选 7；8 个查询覆盖 47 个不同原型。
- **不被污染物清单锁死**：构造一个库外新四面体氧阴离子污染物（仅给 molecular_features/interactions，无 profile/无 pollutant_prototype_map 条目）→ 命中 15 个原型，含 `moda-oxyanion-geometric-recognition`。
- **诚实度改善**：PFOA/BPA 导出候选现为 exploratory（此前经 pollutant key-match 误标 fact/lead）；导出 130→**422 行**、覆盖 29→**44** 污染物。
- **接口回归**：`test_biomimetic_context.py` PASS、`test_interface_honesty.py` PASS；`verify_adrmats_delivery.py` 回到预存基线（SMX/Pb(II) PASS；仅 PFOA/BPA/chimera 预存 FAIL，非本阶段引入）。
- **validator**：validate_consistency 0 error、from_source_integrity 全 compliant、causal_chain 全合格、source_authenticity 无硬错误。

## 预存问题（承接 Track1，非本阶段引入）
- verify_adrmats_delivery 的 PFOA/BPA "organic 不允许 direct_evidence/direct_pollutant_evidence" + check_chimera(10)：均为 expand 分支预存；本阶段基线对照已确认非新引入。plant-lignocellulosic 生物炭对 BPA 有真实容量数据与该测试"organic 一律无直接证据"口径冲突，留待 Track2B/口径评审。
