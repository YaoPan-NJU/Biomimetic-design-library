# Massive 新增原型准入审计（2026-08-03）

## 结论

以 `main` 的正典、证据分层和 ADRMATS 查询契约为基线，对 `massive` 新增的 5 个根原型逐项复核。结果为：

- 修复后准入 2 个：`ssua-alkylsulfonate-binding-protein`、`bug-family-carboxylate-pincer`。
- 修复后仍不满足准入标准，舍弃 3 个：LIVBP、OxlT、LinA/LinB。
- 没有直接合并 `massive` 的原 JSON 和整份映射；准入项均在 `main` 上按原始论文重建，污染物映射保持 `exploratory`，`performance_data` 为空。

本轮 `main` 净增加 2 个根原型和 2 条合格机制卡：100 → 102 个根原型，630 → 632 条机制卡。

## 准入门

每个候选同时通过以下门槛才准入：

1. **生物身份单一**：不得把不同蛋白家族或不同物种的机制拼成一个原型。
2. **机制可定位**：每个 `from_source` 因果要素必须有 DOI、具体页码、短引文和范围匹配。
3. **转译不改写事实**：天然机制、污染物类比和材料实现分层保存；类比不能升级为直接证据。
4. **有可证伪边界**：明确什么情况下不再属于该仿生机制，以及下一步用什么对照判决。
5. **下游语义安全**：查询结果不得把蛋白结合、转运或催化事实显示为材料去除性能。
6. **召回范围受控**：通用的“氢键/疏水/几何”词不得把原型扩散到未审查污染物；必要时以机制级 `query_pollutant_allowlist` 限定发现范围。

## 逐项裁决

| Massive 候选 | 裁决 | 主要问题 | 处理结果 |
|---|---|---|---|
| SsuA 烷基磺酸盐结合蛋白 | 修复后准入 | 混写两个物种；引用了错误的 SsuA DOI；把 TauA 脱溶剂化机制并入 SsuA；含未接地的竞争倍数和相互作用能 | 统一为 *Xanthomonas citri* SsuA；只用配体结合主文 DOI `10.1371/journal.pone.0080083`；删除 TauA 串并和未接地数值；PFBS 保持 exploratory |
| Bug/TRAP 羧酸夹钳 | 重构、改名后准入 | 把 Bug/TTT 与 TRAP/IseP 混为一体；把 Bug27 泛化为 C4 二羧酸/酮酸受体；GenX 的 Y 形腔结论无来源 | 改为 `bug-family-carboxylate-pincer`；仅保留 DOI `10.1016/j.jmb.2007.08.006` 支持的羧酸夹钳和第二结构域生产性占位；GenX 设低权重 exploratory |
| LIVBP 支链氨基酸结合蛋白 | 舍弃 | 原始结构支持氨基酸头基氢键和非极性侧链凹槽，但不支持条目声称的 Y 形腔、纯拓扑支链判别；GenX 缺少氨基锚且全氟醚支链化学/尺寸不匹配 | 若删除不实机制，剩余内容不能支撑 GenX 专项材料映射；不入 `main` |
| OxlT 草酸/甲酸反向转运体 | 舍弃 | 天然机制本身可靠，但其判别对象是紧密匹配的 C2 二羧酸；GenX 是单羧酸支化全氟醚，电荷数、尺寸和骨架均违反核心口袋约束 | 修复后只能得到通用阳离子阴离子交换，不再是 OxlT 仿生；不入 `main` |
| LinA/LinB HCH 异构体酶 | 舍弃 | LinA 与 Geueke 文献 DOI 写错；天然催化选择性被改写为材料卤键识别；将碘代芳烃列作卤键受体且多个能量/尺寸数值无来源 | 删除错误转译后只剩酶催化事实，无法支持拟议吸附材料机制；不入 `main` |

## 准入项的证据边界

### SsuA

原始研究直接支持：双结构域裂隙、磺酸氧的多点极性相互作用、宽疏水口袋及水介导的尾部适配，并显示 SsuA 对所测烷基磺酸盐而非硫酸根等对照产生特异响应。来源：[PLoS ONE 主文](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0080083)。

原始研究不支持：PFBS/PFHxS 直接结合、材料吸附容量、真实水体选择性或再生。因此 PFBS 映射只表示“值得做有判决对照的设计假设”。

### Bug 家族羧酸夹钳

原始研究直接支持：Bug 家族双域 Venus flytrap 折叠、两半羧酸夹钳的直接/水介导氢键、第一结构域初始锚定以及第二结构域对生产性结合的判别。来源：[PubMed/原始论文摘要](https://pubmed.ncbi.nlm.nih.gov/17870093/)、PDB 2QPQ。

原始研究不支持：Bug27 直接识别 GenX 或支化全氟醚骨架。GenX 映射的唯一保留价值是检验“羧酸头基位点 + 第二占位位点”是否比头基单点受体增加选择性；若无增量，该路线应淘汰。

## 回归要求

- PFBS 查询必须能召回 SsuA，但 lane 必须为 `exploratory`、`direct_evidence=false`。
- GenX/HFPO-DA 查询必须能召回 Bug 家族原型，但 lane 必须为 `exploratory`、`direct_evidence=false`。
- DDT、PFOA 等未审查目标不得因通用机制词误召回这两个原型。
- 两个准入项的 `performance_data` 必须保持为空，除非以后获得带来源定位的材料去除实测数据。
- 被舍弃的 3 个 massive ID 不得出现在 `main` 的根正典或污染物映射中。
