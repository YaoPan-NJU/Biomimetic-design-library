# Track 2A — Canonical 机制/特征词表与派生规则

**日期：** 2026-07-29 ｜ **分支：** `massive`

机制层匹配的词表与映射。机器可读映射已写入 `feature_matching_rules.json`（`canonical_mechanisms` / `interaction_to_mechanism` / `molecular_feature_to_mechanism`）；每个原型的 `mechanism_tags` 字段用同一 canonical 机制词表。

## Canonical 机制词表（12）
配位螯合 · 静电吸附 · 离子交换 · 氢键 · π-π堆积 · 疏水分配 · 孔道限域分子筛分 · 沉淀共沉淀 · 还原催化降解 · 生物矿化 · 几何识别 · 超浸润分离

## pollutant.likely_interactions → 机制（归一化 23→12）
- 配位/络合 → 配位螯合
- 静电吸引/静电/静电(阴离子)/静电(质子化胺) → 静电吸附
- 氢键/氢键(环氧)/卤键 → 氢键
- π-π堆积/π-π/电子供受体(EDA) → π-π堆积
- 疏水/疏水分配/强疏水/范德华/弱范德华/界面CMC → 疏水分配
- 离子交换 → 离子交换 ｜ 沉淀/还原沉淀 → 沉淀共沉淀
- 还原/氧化 → 还原催化降解 ｜ 孔道限域 → 孔道限域分子筛分

## pollutant.molecular_features → 机制（主要项）
- 二价阳离子→配位螯合+静电吸附；软酸/交界酸/可配位/各类"可与…配位"/铀酰离子→配位螯合；高电荷密度→静电吸附
- 芳香环/平面结构/大平面结构/两芳环→π-π堆积
- 疏水性/氟碳链/长链全氟烷基/C-F键/弱极性/挥发性→疏水分配；两亲性/全氟醚羧酸尾→疏水分配+静电吸附
- 酚羟基→氢键+配位螯合；羧酸基团/羧酸头基→配位螯合+静电吸附；多羟基→氢键
- 可电离/弱酸性/弱碱性/正电荷/负电荷/两性离子→静电吸附
- 含氧阴离子/四面体结构/磺酸头基/磺酸基团→几何识别+静电吸附
- 大分子/大环内酯→孔道限域分子筛分；氯代→疏水分配+氢键；内分泌干扰/特异性识别/小半径→几何识别

## 原型 mechanism_tags 派生关键词规则（来源=mechanisms[]）
从每个原型 `mechanisms[]` 的 name + causal_chain.interaction.text + functional_groups + key_structures + transferable_principle + 顶层 features 匹配以下关键词并集：
- 螯合/chelat/coordinat/软酸/金属配位/双齿/络合 → 配位螯合
- 巯基/-SH/硫醇/thiol/-S-/亲硫；氨基/-NH/amine/壳聚糖/胺基；羧基/-COO/羧酸；邻苯二酚/DOPA/多巴胺/PDA/单宁/儿茶酚 → 配位螯合
- 静电/正电/负电/electrostat/库仑/质子化 → 静电吸附
- 离子交换/ion exchange → 离子交换
- 氢键/hydrogen bond/-OH/羟基/硅醇/silanol → 氢键
- π/pi-pi/芳香/aromatic/石墨烯/graphene/GO/π电子 → π-π堆积
- 疏水/hydrophobic/氟碳/PDMS/PTFE/PVDF/低表面能/范德华 → 疏水分配
- 超疏水/超浸润/超润湿/油水/Janus/超亲/乳突/集雾/集水/fog → 超浸润分离
- 孔/pore/限域/筛分/siev/微孔/介孔/大孔/截留 → 孔道限域分子筛分
- 沉淀/precipit/碳酸盐/CaCO/文石/方解石/羟基磷灰石/HAp → 沉淀共沉淀
- 矿化/mineraliz/模板 → 生物矿化
- 还原/reduct/催化/cataly/活性氧/降解/degrad/漆酶/过氧化物酶/脱卤/脱氯 → 还原催化降解
- 识别/口袋/头基锚/识别结构/几何/氧阴离子/四面体/受体/结合腔/selectiv/recognition/印迹/imprint/适配体/aptamer/通道/channel/转运 → 几何识别

## 说明
- `mechanism_tags` 为**显式 canon 字段**（用户选定），可直接手工编辑维护；上表规则仅为首次批量派生依据，非运行时依赖。
- 匹配主路径 = pollutant 特征/相互作用 → canonical 机制 → 原型（经 `mechanism_tags` 倒排，主）；并经 `mechanism_to_bridge` 将 canonical 机制映射到 `mechanism_feature_bridge` 键 → bridge 特征 → `feature_prototype_map` 原型（次级，**已激活**）。bridge 的 feature vocab 已对齐 fpm 键（修 `离子交换能力→离子交换`）；`mechanism_to_bridge` 位于 `feature_matching_rules.json`。
