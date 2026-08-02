# MASSIVE_INGESTION_REVIEW_REPORT

**日期：** 2026-08-02
**分支：** massive
**源数据：** biomimetic-adsorbent-design Ultimate 分支 `rounds/fresh_1000_R4/`（20 污染物 × 50 方案，~90 独立原型）

---

## 审阅统计

| 指标 | 数量 |
|---|---|
| 源原型总数（去重后独立原型） | ~90 |
| 去重跳过（已在 BMDL） | 27 |
| 过于泛化/非特异（不入库） | 51 |
| 联网验证后不达标（❌） | 5 |
| 达标并入库（✅） | **5** |
| 优化后达标（⚠️→✅） | 0 |
| 建议补充已有原型 tested_conditions | 3 |

---

## 去重跳过清单（27 个，已在 BMDL）

| 原型 | BMDL 对应文件 |
|---|---|
| DmpR/PoxR 酚感应 | dmpr-phenol-effector-binding-domain.json |
| OAT4 链长阈值 | oat4-organic-anion-transporter.json |
| SBP 四面体纯氢键 | sbp-sulfate-oxyanion-geometric-recognition.json |
| NTCP 胆汁酸转运 | ntcp-bile-acid-pfas-transporter.json |
| ASBT 胆汁酸转运 | asbt-bile-acid-elevator-transporter.json |
| 23S rRNA NPET | ribosome-npet-macrolide-recognition.json |
| FcRn pH 开关 | fcrn-ph-dependent-fc-recycling.json |
| 脱氯化氢酶 GST | ddt-dehydrochlorinase-gst.json |
| 氟核糖开关 | fluoride-riboswitch-f-sensing-switch.json |
| FABP4 三模式 | fabp4-fatty-acid-pfas-binding.json |
| hL-FABP | hl-fabp-liver-fatty-acid-pfas-binding.json |
| HSA | hsa-fatty-acid-pfas-binding.json |
| TTR 卤代酚通道 | ttr-halophenol-thyroxine-channel.json |
| Bayram ipso 途径 | ipso-hydroxylation-pathway.json |
| GABA/Rdl 刚性疏水腔 | gaba-rdl-rigid-hydrophobic-cavity.json |
| ERRγ | errg-bpa-endocrine-receptor.json |
| PXR 定向混杂 | pxr-xenobiotic-receptor-promiscuity.json |
| 漆酶/HRP | hrp-laccase-phenol-radical-coupling.json |
| 漆酶 T1 Cu | laccase-t1-cu-phenol-coordination.json |
| β-CD 包结 | beta-cyclodextrin-hostguest-inclusion.json |
| ModA 四面体 | moda-oxyanion-geometric-recognition.json |
| EPS/微生物胞外多糖 | microbial-exopolysaccharide.json |
| 白腐真菌 LiP | lignin-peroxidase-white-rot.json |
| 还原脱氯酶 B12 | reductive-dehalogenase-b12-dechlorination.json |
| Lipocalin/SCP-2 | lipocalin-hydrophobic-calyx.json |
| 溶酶体 pH 离子阱 | lysosome-acid-ion-trapping-ph-switch.json |
| 光合反应中心 | bacterial-photosynthetic-reaction-center.json |

---

## 不达标清单（❌，5 个）

| 原型 | 原因 | 联网搜索证据 |
|---|---|---|
| DMSP 裂解酶 DddP | **化学错误**：概念卡声称 PFBS 与 DMSP "共享磺酸/锍基团"，但 PFBS 是磺酸根 R-SO3⁻（S 氧化态 +5），DMSP 是锍 (CH3)2S+-CH2CH2COO-（S 氧化态 -2），化学本质完全不同 | 搜索 PDB 4S01 确认 DddP 是 M24 金属肽酶折叠，识别锍中心（非磺酸根）；Wang 2015 被引 52 确认 C-S 键裂解机制 |
| 环氧化物水解酶 | **转译原则不可操作**："环氧氧 H 键供体识别"过于泛化（任何醚氧都可做 H 键受体）；且无直接证据 EH 处理狄氏剂笼状环氧 | 搜索确认 EH 机制（Asp 亲核攻击 + Tyr H 键），但 Pang 2022 综述中狄氏剂降解未提及 EH 途径 |
| CYP3A4 大环内酯代谢 | **无独立识别价值**：CYP3A4 是广谱药物代谢酶，N-脱甲基是催化功能；无法提供 ROX vs 红霉素类内选择性 | 搜索确认 CYP3A4 代谢 ROX 但无选择性（类级） |
| 甲状腺激素脱碘酶 | **与 TTR 重叠**：脱碘酶是催化酶（催化功能），识别价值已被 TTR 卤代酚通道覆盖 | 搜索确认脱碘酶功能为催化脱碘，非独立识别 |
| PcpB 五氯酚羟化酶 | **与已有原型重叠**：BMDL 已有 chlorophenol-hydroxylase-regioselective.json 覆盖氯酚羟化识别 | 搜索确认 PcpB 是氯酚羟化酶，与已有原型机制同类 |

---

## 达标入库清单（✅，5 个）

| # | 原型 ID | 名称 | 证据层级 | 适用污染物 | 联网搜索验证摘要 |
|---|---|---|---|---|---|
| 1 | ssua-alkylsulfonate-binding-protein | SsuA 烷基磺酸盐结合蛋白 | 结构级(PDB 3UIF/3E4R) + 机制级 | PFBS, PFHxS, PFOA | Beale 2010 (PubMed 20383006, 被引 18) 确认两球域裂缝结构；Qu 2019 (Biochem J, 被引 25+) 确认脱溶剂化门控 |
| 2 | bug-trap-carboxylate-clamp | Bug/TRAP 羧酸夹钳 | 结构级(PDB 2QPQ/8TQN) | GenX | PDB 2QPQ 确认 Bug27 "carboxylated solutes characteristic binding mode"；PDB 8TQN (2025) 扩展底物谱 |
| 3 | livbp-branched-chain-amino-acid-binding | LIVBP 支链氨基酸结合蛋白 | 结构级(PDB 2LIV/1Z15) | GenX | PDB 2LIV 经典结构确认 Y 形腔；PDB 1Z15/7JFN/9JTI 确认家族广泛存在 |
| 4 | oxlt-short-chain-dicarboxylate-transporter | OxlT 草酸转运体 | 结构级(PDB 8HPJ) | GenX | Jaunet-Lahary 2023 (Nature Comms, PMC10070484, 被引 24) 确认双碱性残基盐桥 + 严格底物区分 |
| 5 | lina-linb-hch-isomer-dehydrochlorinase | LinA/LinB HCH 异构体酶 | 机制级 + 结构级(PDB 4H77/1D07) | β-HCH | Okai 2010 (被引 55) 确认 LinA γ-HCH 结构；Okai 2013 (PMC3676048, 被引 36) 确认 LinB β-HCH 水解；ES&T 2022 QM/MM 确认能垒差异 |

---

## 过于泛化/非特异不入库（51 个，部分列举）

以下原型因过于泛化、非特异、或与已有原型机制同类而不入库：

- EPS/生物膜分配（各污染物重复出现，非特异疏水分配）
- HSA/FABP 广谱结合（各污染物重复，无选择性）
- 膜分配/脂质双层（物化原理，太泛）
- Hofmeister 趋液性（物化原理，太泛）
- 卤键 σ-空穴（物化原理，无进化优化）
- 偶极矩差异（物化原理，太泛）
- P450 泛化代谢（各污染物重复，无独立识别价值）
- β-CD 包结（已有，先例饱和）
- 分子印迹（材料化学方法，非生物原型）
- AhR（毒性靶标，与 PXR 重叠）
- AGP（广谱碱性药物结合，无选择性）
- MefA/MsrA 外排泵（外排非识别）
- Erm 甲基转移酶（间接证据）
- PKS DEBS（合成酶，非识别功能）
- 各污染物 P450 变体（与已有 P450BisD 同类）
- 白腐真菌（各污染物重复，已有）
- 还原脱氯酶（各污染物重复，已有）

---

## 建议补充已有原型 tested_conditions（本次不修改，仅标注）

| 已有原型 | 建议补充 |
|---|---|
| ipso-hydroxylation-pathway | 当前 status=pending_extraction，建议补充 Bayram/TTNP3 异构体选择性数据（Lu 2015 Water Res） |
| gaba-rdl-rigid-hydrophobic-cavity | 当前 status=pending_extraction，建议补充 Casida 2015 综述的立体化学证据 |
| oat4-organic-anion-transporter | 建议补充 PFHxS 适用场景（Louisse 2023 确认 PFHxS 被 OAT4 转运） |

---

## 与已有 BMDL 原型的关联说明

| 新原型 | 关联已有原型 | 区分说明 |
|---|---|---|
| SsuA | SBP (sbp-sulfate-oxyanion-geometric-recognition) | SBP 识别硫酸根（二价四面体），SsuA 识别烷基磺酸盐（单价四面体 + 烷基尾）；SsuA 有尾部口袋和脱溶剂化门控，SBP 无 |
| SsuA | ModA (moda-oxyanion-geometric-recognition) | ModA 识别钼酸根/钨酸根，SsuA 识别烷基磺酸盐；头基化学不同 |
| Bug/TRAP | 无直接对应 | 首个羧酸夹钳型识别原型，与 SBP/ModA（氧阴离子）和 SsuA（磺酸盐）均不同 |
| LIVBP | 无直接对应 | 首个纯拓扑/形状识别原型（支链 vs 线性），不依赖头基化学 |
| OxlT | 无直接对应 | 首个"不依赖疏水链"的短链羧酸识别原型 |
| LinA/LinB | ddt-dehydrochlorinase-gst | DDT-脱氯化氢酶识别 DDT 桥 H + CCl3；LinA/LinB 识别 HCH 轴向/平伏氯取向；底物和判据完全不同 |

---

## 质量门控脚本结果

```
validate_consistency.py --strict: 错误 0, 警告 232 (均为已有原型的预存警告)
check_source_authenticity.py: 错误 0 ✅
check_causal_chain.py: 637/637 合格 ✅
check_repo_hygiene.py: PASS ✅
```

---

## 入库文件清单

```
prototypes_db/ssua-alkylsulfonate-binding-protein.json (287 行)
prototypes_db/bug-trap-carboxylate-clamp.json (210 行)
prototypes_db/livbp-branched-chain-amino-acid-binding.json (201 行)
prototypes_db/oxlt-short-chain-dicarboxylate-transporter.json (209 行)
prototypes_db/lina-linb-hch-isomer-dehydrochlorinase.json (283 行)
prototypes/ssua-alkylsulfonate-binding-protein/prototype.md
prototypes/bug-trap-carboxylate-clamp/prototype.md
prototypes/livbp-branched-chain-amino-acid-binding/prototype.md
prototypes/oxlt-short-chain-dicarboxylate-transporter/prototype.md
prototypes/lina-linb-hch-isomer-dehydrochlorinase/prototype.md
feature-mapping.json (更新: +5 prototype_metadata + PFBS/GenX/β-HCH 映射)
```
