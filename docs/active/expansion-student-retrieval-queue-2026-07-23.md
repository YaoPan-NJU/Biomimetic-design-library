# `expand` 新增原型学生检索队列（2026-07-23）

## 使用规则

每项至少交付：题录、DOI/专利号、可访问全文、精确页码/图表、逐字原文、实验对象与条件、能支持和不能支持的断言。只找到综述时继续追原始研究；专利必须记录申请人、优先权日、权利要求号和实施例。没有结果也要保存检索式与数据库。

| 优先级 | prototype_id | 待证断言与风险 | 中文关键词 | English Boolean query | 数据库 | 期望证据 |
|---|---|---|---|---|---|---|
| P0 | lipocalin-hydrophobic-calyx | 是否存在 DDT/DDD/DDE 与 lipocalin/MUP 的直接结合；当前只有疏水 calyx 类比 | 脂质运载蛋白 小鼠尿蛋白 DDT DDE 结合 晶体 | `(lipocalin OR "major urinary protein" OR MUP) AND (DDT OR DDE OR DDD) AND (binding OR crystal OR affinity)` | Web of Science, Scopus, PubMed, Google Patents, Espacenet | 直接结合、Kd/IC50、共晶或明确阴性结果 |
| P0 | p450bisd-bisphenol-monooxygenase | P450bisd 的底物位点/残基与结构；P450cam 只能作家族替代 | P450bisd 双酚A 单加氧酶 Sphingomonas AO1 结构 残基 | `(P450bisd OR "bisphenol monooxygenase") AND (bisphenol A OR BPA) AND (structure OR residue OR mutation OR substrate specificity)` | PubMed, Crossref, Web of Science, Google Patents, Espacenet | P450bisd 本体结构、突变、产物和动力学；若无结构需明确“未见” |
| P0 | oat4-organic-anion-transporter | PFAS 的 OAT4 链长选择性、动力学与结构位点；已知转运不等于吸附 | OAT4 SLC22A11 PFAS PFOA PFOS PFBS 转运动力学 链长 | `(OAT4 OR SLC22A11) AND (PFAS OR PFOA OR PFOS OR PFBS) AND (transport kinetics OR uptake OR chain length OR structure)` | PubMed, Web of Science, Scopus | Km/Vmax、物种/细胞系、抑制或底物判定、链长序列 |
| P0 | hsa-fatty-acid-pfas-binding | “FABP/HSA 敲除不改变 PFOS 分布”中的 HSA 部分尚无原始来源 | 白蛋白 敲除 PFOS 组织分布 FABP 小鼠 | `(albumin OR HSA OR ALB OR FABP) AND knockout AND (PFOS OR PFOA OR PFAS) AND (distribution OR toxicokinetics)` | PubMed, Web of Science, Scopus | 基因型、剂量、组织分布、统计结果；区分 HSA 与 L/I-FABP |
| P0 | hl-fabp-liver-fatty-acid-pfas-binding | 区分链长/体积/疏水色散与定向 C–F 对 L-FABP–PFAS 亲和力的贡献；当前不能排除后者 | 肝脂肪酸结合蛋白 PFAS 氟特异 C-F 疏水 体积 自由能 | `(L-FABP OR FABP1) AND PFAS AND (fluorine-specific OR C-F interaction OR hydrophobic OR volume OR free energy decomposition)` | Web of Science, Scopus, PubMed, SciFinder | 全文原文、自由能分解/突变/匹配碳链对照；允许得到“无法区分”的阴性结论 |
| P0 | serine-protease-oxyanion-hole | 预组织双氢键供体能否在水相材料中选择性捕获羧酸根/酚氧；当前为机制外推 | 氧阴离子穴 仿生 双氢键供体 羧酸根 水相 吸附 | `("oxyanion hole" OR "preorganized hydrogen-bond donor") AND (carboxylate OR phenoxide) AND (receptor OR adsorbent OR polymer OR porous) AND water` | Web of Science, SciFinder, Reaxys, Google Patents, Espacenet | 合成受体/材料、含水条件、选择性、结合常数、再生 |
| P1 | ecdysis-renewable-interface | 蜕皮是否有可工程化“污染后整体脱落更新界面”的直接先例 | 蜕皮 仿生 可更新 表面 自清洁 脱落 涂层 | `(ecdysis OR molting OR sloughing) AND (bioinspired OR biomimetic) AND (renewable surface OR self-cleaning OR fouling release)` | Web of Science, Scopus, Google Patents, Espacenet | 机制对应与器件/涂层实施例；循环或性能数据如有则附 |
| P1 | nephron-capture-then-separate | 肾单位“先捕获后分流”是否有明确分离器件先例 | 肾单位 仿生 先捕获 后分离 过滤 回收 | `(nephron OR glomerular OR megalin OR cubilin) AND biomimetic AND (separation OR filtration OR capture OR recovery)` | Web of Science, Scopus, Google Patents | 结构映射、实验装置、通量与选择性 |
| P1 | mammalian-lung-murray-law-branching | Murray 分支是否在吸附/膜分离中改善传质且有实验对照 | Murray 定律 分支流道 吸附 膜分离 传质 | `("Murray's law" OR Murray law) AND (adsorption OR membrane separation OR mass transfer OR microfluidic) AND experiment` | Web of Science, Scopus, IEEE Xplore, Google Patents | 与非分支对照、压降、通量、传质系数 |
| P1 | viral-capsid-slayer-multivalent-self-assembly | 病毒衣壳与 S-layer 被合并为一个原型是否有共同的污染物捕获证据 | 病毒衣壳 S层 多价 自组装 污染物 捕获 | `((viral capsid) OR (S-layer)) AND multivalent AND (pollutant capture OR adsorption OR separation)` | Web of Science, Scopus, PubMed, Google Patents | 分开报告两类体系；重点核对结构与多价机制对应，性能数据如有则附 |
| P1 | pulmonary-surfactant-phospholipid-interface | PFOA 改变膜刚度不等于膜可选择性捕获 PFOA | 肺表面活性剂 PFOA 磷脂膜 结合 分配 选择性 | `(pulmonary surfactant OR phospholipid membrane) AND PFOA AND (binding OR partition OR adsorption OR selectivity)` | PubMed, Web of Science, Scopus | 分配系数、膜组成依赖、竞争体系、可逆性 |
| P1 | bile-salt-mixed-micelle-solubilization | 胆盐混合胶束是否有环境污染物选择性捕获/可再生分离直接证据 | 胆盐 混合胶束 环境污染物 增溶 分离 再生 | `(bile salt mixed micelle) AND (environmental pollutant OR endocrine disruptor) AND (solubilization OR separation OR recovery)` | Web of Science, Scopus, SciFinder, Google Patents | 污染物谱、增溶系数、竞争、回收/再生 |
| P2 | siderophore-capture-recovery-architecture | 铁载体的捕获—回收架构能否迁移到非金属污染物；避免概念拼接 | 铁载体 捕获 回收 仿生 分离 污染物 | `(siderophore OR enterobactin) AND (capture AND recovery) AND (separation OR adsorbent OR sensor)` | Web of Science, Scopus, Google Patents | 有循环回收的实施例、目标物、配位选择性 |

## 专利统一检索补充

对每个 P0/P1 项，再用以下分类与同义词组合检索：`adsorbent`, `molecular receptor`, `selective capture`, `regeneration`, `porous polymer`, `membrane`, `biosensor`, `water treatment`；优先查看 CPC `B01J20`、`B01D`、`C02F`、`G01N33` 下的权利要求和实施例。专利题名或摘要命中不能直接入库，至少要核对独立权利要求和一个可工作的实施例。
