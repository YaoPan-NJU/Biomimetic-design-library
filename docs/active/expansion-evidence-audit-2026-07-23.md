# `expand` 分支新增原型证据质控（2026-07-23）

## 技术结论

`expand` 相对扩张前节点 `52fc739` 净增 47 个根级原型，原型总数由 42 增至 89。新增部分不是“没有来源”，而是“来源存在但证据等级标得过高”：47 条共引用 132 个唯一 DOI，Crossref 首轮成功解析 126 个；其余 6 个为 429 或 TLS 临时错误，不能据此判无效。题名级核验显示，大多数 DOI 与原型主题一致，但 DOI 存在只证明文献存在，不证明文献逐句支持词条中的所有机制、边界和设计转译。

当前新增 47 条全部为 `library_tier=extended`、`coverage=partial`，共有 96 个机制。43 条明确记录“未完成全文 PDF 审计”或同等缺口。按仓库定义，未打开全文 PDF、没有页码/图表定位的来源不能算 `verified`；因此新增条目的主要质控任务是证据重分级，而不是继续扩数量。`performance_data` 是否存在不作为固定评价维度：本库的核心用途是启发设计，重点评价天然机制是否真实、设计对应是否讲得通、推理边界是否诚实、来源是否可追溯；性能数据仅在恰好存在且与主张相关时作为补强。

## 已确认并落库的修订

1. `serine-protease-oxyanion-hole`：补入 Bobofchak et al. 2005 的直接结构—动力学研究，DOI `10.1074/jbc.M503499200`。该研究直接说明 Gly193/Ser195 骨架氮构成丝氨酸蛋白酶氧阴离子穴，并通过 G193A/G193P 突变和晶体结构估算氢键稳定贡献。原有两篇 2026 年文献保留为窄实例，不再单独承担通用机制的主证据。
2. `hsa-fatty-acid-pfas-binding`：补入 Maso et al. 2021，DOI `10.1002/pro.4036`。全文 PDF 报告 2.10 Å HSA–PFOA 复合物、4 个 PFOA 位点、4:1 化学计量，以及羧酸头基极性锚和氟化尾链疏水接触。该来源支持 HSA–PFOA 结合模式；从该机制进一步推导 PFAS 特异材料仍须单独标作设计推理，但不因缺少材料性能数据而降低原型本身的启发价值。
3. `oat4-organic-anion-transporter`：补入 Louisse et al. 2023，DOI `10.1007/s00204-022-03428-6`。OAT4 转染细胞直接测定 7 种 PFAS，除 PFBS 外其余 6 种显示清晰摄取。该来源标为污染物—转运体直接证据，不升级为吸附材料 direct evidence。
4. `hl-fabp-liver-fatty-acid-pfas-binding`：纠正一条错误归属。原词条把 HSA–PFOA 论文 DOI `10.1002/pro.4036` 署名为 Cheng & Ng 2021，并据此排除定向 C–F 贡献；该 DOI 与断言不匹配。真实的 Cheng & Ng 研究是 2018 年 ES&T 论文 DOI `10.1021/acs.est.8b01268`，研究 15 种 PFAS 对人/鼠 L-FABP 的相对亲和力模拟。已补入正确 DOI，并把“排除定向 C–F”降回 `llm_inferred/needs_review`。

同时，`hl-fabp` 原有 2 个机制的 7 个因果链要素全部只有题名/摘要/PDB 层支持，不符合仓库 `verified` 定义。本轮将 `n_verified` 从 3 降为 0、`n_unverified` 调整为 5，并把这些要素统一降为 `source_lead_abstract`/`llm_inferred`；来源线索仍保留，待学生取得全文后再逐项升级。

HSA 来源还暴露出一个需保留的资料冲突：Maso 论文 PDF 正文把 PFOA 复合物写作 7AAE、肉豆蔻酸复合物写作 7AAI；当前 RCSB 条目标题、配体和分辨率则是 7AAI=PFOA 2.10 Å、7AAE=肉豆蔻酸 2.27 Å。词条已避免把争议 PDB 编号作为唯一证据键，并保留冲突说明。

## 47 条全量初筛

这里的 A/B 是“下一步审计路线”，不是最终质量等级。

### A 组：已有污染物直接实验或原型本体的强匹配来源（24 条）

这些条目的 DOI 题名与原型本体、目标污染物或直接结构高度匹配；下一步重点是打开 PDF、补 locator/quote，并核对数值与适用边界。

| 原型 ID | 首轮判断 | 下一步 |
|---|---|---|
| acidimicrobium-reductive-defluorination | 有 PFOA/PFOS 生物脱氟直接论文 | 核对脱氟比例、产物和争议复现性 |
| anaerobic-sequential-dechlorination-cascade | 有 B12/DDT/DDE 还原脱氯直接论文 | 区分纯化辅酶、微宇宙和完整级联 |
| asbt-bile-acid-elevator-transporter | 有 ASBT 结构及 PFAS disposition 论文 | 核对具体 PFAS、物种和转运方向 |
| chlorophenol-hydroxylase-regioselective | 有 TCP 单加氧酶结构/催化论文 | 核对底物范围与位点归属 |
| ddt-dehydrochlorinase-gst | 有 DDT 脱氯酶及 GSTe2 抗性论文 | 核对单突变因果强度 |
| dmpr-phenol-effector-binding-domain | 有 phenol-bound DmpR 全文结构论文 | 已接近首批质量，补 PDF 版式定位 |
| errg-bpa-endocrine-receptor | 有 BPA–ERRγ 结合与晶体结构 | 已接近首批质量，补 PDF 页码 |
| fluc-fluoride-export-channel | 有 Fluc 通道晶体结构和选择性研究 | 补残基与渗透路径页码 |
| fluoride-riboswitch-f-sensing-switch | 有氟离子核糖开关结构和遗传学证据 | 区分 sensing 与 engineering translation |
| fluoroacetate-dehalogenase | 有酶促脱氟反应坐标和复合物结构 | 核对突变体与野生型边界 |
| gpr43-ffar2-short-chain-fatty-acid-receptor | 有 FFA2 链长选择性结构 | 补链长窗口的数值依据 |
| hl-fabp-liver-fatty-acid-pfas-binding | 有 PFAS–L-FABP 直接作用及敲除研究 | 全文核对不同 PFAS 与体内外结论 |
| hrp-laccase-phenol-radical-coupling | 有酚去除、交联酶聚集体及酶结构 | 分离去除性能与自由基机理来源 |
| hsa-fatty-acid-pfas-binding | 有 PFOS/PFOA–HSA 直接晶体结构 | 已补 PFOA 全文来源；保留非特异性边界 |
| lanmodulin-lanthanide-coordination | 有结构、选择性与分离直接研究 | 核对金属序列和条件依赖 |
| lignin-peroxidase-white-rot | 有 W171 自由基、结构与底物自由基研究 | 补酸性稳定和底物范围的来源分层 |
| nrta-nitrate-binding-protein | 有硝酸盐结合蛋白原子结构 | 补硝酸盐/亚硝酸盐选择性数据 |
| ntcp-bile-acid-pfas-transporter | 有人 NTCP 结构和 PFAS disposition 线索 | 核对 PFAS 是否为底物、抑制剂或间接关联 |
| oatp-intestinal-hepatic-uptake | 有 OATP1B1/1B3 结构和 PFAA disposition | 核对物种与转运方向 |
| p450bisd-bisphenol-monooxygenase | 有 AO1 P450bisd–BPA 降解直接论文 | P450cam 结构只能作家族机理替代，不得写成 P450bisd 结构 |
| psts-phosphate-binding-protein | 有高特异磷酸盐结合结构与突变 | 核对砷酸盐等竞争物边界 |
| reductive-dehalogenase-b12-dechlorination | 有 B12 脱氯酶结构及 DDT 脱氯直接论文 | 分离酶、游离 B12 与细胞体系 |
| ttr-halophenol-thyroxine-channel | 有 OH-PCB–TTR 共晶与竞争结合 | 已接近首批质量，补全文页码 |
| ugt-glucuronidation-glycosylation-regioselective | 有 BPA 葡萄糖醛酸化及糖基转移酶结构 | 区分人 UGT 与植物 UGT 的同源外推 |

### B 组：天然机制有来源，但工程/污染物映射主要是推理（23 条）

这些条目不是“假”，但目前最容易稀释库：来源通常证明天然系统，不直接证明拟议材料、污染物去除或选择性。应保留为 `inspiration`/`llm_inferred`，除非找到直接论文或专利。

| 原型 ID | 已有接地 | 主要缺口 |
|---|---|---|
| bile-salt-mixed-micelle-solubilization | 胆盐胶束与胆固醇溶解 | 到污染物捕获/再生的直接证据 |
| decarboxylase-carbanion-activation | OMP decarboxylase 结构与电静力催化 | 到吸附/转化材料的可实现映射 |
| ecdysis-renewable-interface | 蜕皮激素与几丁质结合 | “可更新界面”工程证据 |
| fcrn-ph-dependent-fc-recycling | FcRn–Fc 结构和 pH 依赖 | 到吸附再生的直接材料证据 |
| hemoglobin-bohr-ph-allostery | Bohr 效应和 His146 因果 | 到 pH 开关吸附的直接证据 |
| kcsa-potassium-channel-selectivity-filter | KcsA 选择性滤器结构 | 到离子筛材料的定量映射 |
| lectin-glycan-hydroxyl-recognition | ConA–糖复合物结构 | 对目标污染物的直接识别 |
| lipocalin-hydrophobic-calyx | MUP/脂质配体疏水 calyx | 未找到 lipocalin–DDT 直接来源 |
| lysosome-acid-ion-trapping-ph-switch | 溶酶体酸化和弱碱捕获 | 工程吸附与可逆释放证据 |
| mammalian-lung-murray-law-branching | Murray 定律与肺分支形态 | 到传质/分离器件的实验验证 |
| mscl-mechanosensitive-channel | MscL 结构与门控能量 | 到压力响应分离材料的直接证据 |
| natural-dna-imotif-gquadruplex-switch | i-motif/G4 结构 | 到目标污染物捕获的直接证据 |
| natural-riboswitch-metabolite-sensing | 天然核糖开关结构 | 到材料化、再生和耐水性的证据 |
| nephron-capture-then-separate | 肾小球屏障及 megalin/cubilin | “先捕获后分离”器件证据 |
| oat4-organic-anion-transporter | OAT4 结构、交换和 PFAS 直接转运 | 到 PFAS 吸附材料和链长窗口的证据 |
| pulmonary-surfactant-phospholipid-interface | 肺表面活性膜与 PFOA 膜作用 | 到选择性吸附界面的证据 |
| pxr-xenobiotic-receptor-promiscuity | PXR 定向多特异结构 | 到污染物识别材料的直接证据 |
| ribosome-npet-macrolide-recognition | 核糖体–大环内酯结构 | 到合成孔道识别的直接证据 |
| sbp-sulfate-oxyanion-geometric-recognition | 硫酸根结合蛋白结构 | 到目标阴离子材料的湿态选择性 |
| serine-protease-oxyanion-hole | 氧阴离子穴结构—动力学证据 | 到羧酸根/酚氧吸附的直接证据 |
| siderophore-capture-recovery-architecture | 铁载体配位和平衡 | 到污染物捕获—回收架构的直接证据 |
| sortase-a-lpxtg-covalent-immobilization | Sortase A–底物复合物 | 固载材料寿命和规模化证据 |
| viral-capsid-slayer-multivalent-self-assembly | 病毒衣壳和 S-layer 结构 | 两类体系被合并后的统一工程证据 |

## 方法与判定口径

- 批次：`git diff 52fc739..expand -- prototypes_db/*.json` 得到 47 个新增根级 JSON。
- DOI 存在性：对 132 个唯一 DOI 做 Crossref 元数据解析。126 个成功；6 个网络限流/握手失败，未判无效。
- 题名匹配：比较原型 ID、机制名称与 Crossref 题名，只作为错误发现筛查。
- 深审：优先打开出版社/PMC/PubMed/RCSB 等一手来源，核对对象、配体、结构、实验系统、页码/图表和结论边界。
- `verified`：按本仓库定义，必须打开全文 PDF，并记录精确 locator 与 quote；仅摘要、题录、PDB 标题或同源结构不足以达到该等级。
- 污染物直接相互作用、天然机制、工程转译和材料性能是不同主张，不能互相替代；前三者是本库的主要评价对象，材料性能是可选补强项，不作为统一准入条件。

## 局限与稳健性

本轮完成了全量 DOI 元数据初筛和 7 个高价值条目的深查（ERRγ、DmpR、HSA、hL-FABP、TTR、OAT4、氧阴离子穴），尚未逐篇打开 47 条的全部全文 PDF。因而 A/B 分组是审计优先级，不是最终认证。新增条目仍应保持 `coverage=partial`；在逐篇 PDF 审计完成前，不应批量升级 `verification`。

## 下一步

1. 按 A 组先完成“论文全文—机制断言—locator/quote”逐项闭环，优先直接污染物证据。
2. 对 B 组先检索是否存在目标污染物/工程实现的直接论文或专利；没有则明确维持 `inspiration`。
3. 将 `verified` 全量重算，撤销仅由摘要/PDB 标题支撑的虚高标记。
4. 修复消费者层把 `pollutant_prototype_map` 中任意候选自动标成 `direct_pollutant_evidence` 的逻辑；否则库内诚实标注会在查询时被覆盖。
5. 每批修订后运行 JSON、因果链、边界、chimera 和 ADRMATS delivery 验证，并单列既有警告与本批新增回归。

## 待回答的进一步问题

- 是否将“天然机制已证实但工程映射未证实”的 23 条统一降为 `exploratory`，还是保留 `extended + partial`？
- 专利能否作为工程可实现性的补强来源，但不参与生物机制的 `verified` 计数？
- 对论文正文与 PDB 当前条目冲突时，是否增加结构化 `source_conflict` 字段，而不是只写在 note 中？
