# BMDL 决策与工作记录（集中审阅）

> 分支：`massive`｜时间跨度：Track 2A → Track 2B → 检索排序修复｜用途：供集中审阅本轮所有决策与改动。
> 逐批次细节另见：`track2a_*.md`、`track2b_extraction_log.md`；本文件是**总纲 + 决策依据 + 遗留清单**。
>
> **状态更正（2026-07-29）：** 本文件保留历史决策，但其“全部分支已扫描/机制均已联网接地”的概括未形成逐文件审计链，不能作为完备性证明。β-CD 重复项、5 个 Track 2B 原型的证据等级和查询诚实门已按 `docs/active/massive-remediation-2026-07-29.md` 修正。

---

## 0. 一句话总览

把匹配从"污染物查表"升级为"原型-机制"映射（Track 2A），跨源项目 4 分支抽取 5 个库中缺失的生物原型（Track 2B，库 89→94），并修复检索排序使新原型能真正被检索到（cap 10→15 + 权重排序 + 有机域诚实降级）。全程知识隔离（不搬运姊妹项目性能数值），机制经联网核验的原始文献接地。

---

## 1. 关键决策（含依据）

| # | 决策 | 依据 / 权衡 |
|---|------|------------|
| D1 | 匹配架构转向"原型-机制"优先（机制层），非污染物中心 | 用户要求；避免创意被固定污染物清单锁死；新原型只声明 `mechanism_tags` 即自动可达 |
| D2 | 显式 `mechanism_tags` 字段（canonical 12 类机制），而非隐式推断 | 用户选定；可审计、可倒排检索 |
| D3 | `pollutant_prototype_map` 命中降级：仅有真实 `performance_data` 才算 `direct_evidence` | 诚实优先；ppm 多为策展关联而非实测数据 |
| D4 | Track 2B 口径：跨全部分支、**只看原型、不论方案成败**；好的入库、不完整补全+对抗 | 用户明确纠正（此前误退回"跟现有库比对、大多已吸收、只挑一两个"的窄做法）|
| D5 | 知识隔离红线：新原型 `performance_data` 一律留空，机制独立从原始文献接地 | 两项目知识边界；不搬运姊妹项目容量数值 |
| D6 | 证据分层诚实：仅可页码接地的标 `from_source`，仅题录级的标 `literature_backed`，转译标 lead/inspiration | 不虚标；`from_source` 铁律要求精确页码定位器 |
| D7 | 不硬造原型：PFHxS "PFH-1"（源项目自述为工程离子交换珠）不入库；已在库的（FcRn/NrtA/PstS/FABP/HSA/ERRγ/核糖体/TTR）不重复 | 生物身份门槛 + 去重 |
| D8 | 检索排序修复采用"权重排序 + cap 10→15 + 有机域 match_basis 降级"，而非重写 lane 体系 | 最小改动达成"新原型可检索"，保留 lane 语义与回归安全 |
| D9 | bare-list 遗留只**定点修 As(III)**（转 dict-form），不做 47 键全量转换 | 全量转换高回归风险；定点修复即可让 ArsR 可见，其余留统一治理 |

---

## 2. 工作日志（按阶段）

### 2A. 机制层匹配激活（提交 3034aee + 9ebcc11）
- 89 个原型加 `mechanism_tags`；`feature_matching_rules.json` 新增 `canonical_mechanisms` / `interaction_to_mechanism` / `molecular_feature_to_mechanism` / `mechanism_to_bridge`。
- `biomimetic_context.py` 新增 `find_mechanism_based()`（mechanism_tags 倒排为主 + 激活闲置的 `feature_prototype_map` 与 `mechanism_feature_bridge` 为次级）；`query()` 合并顺序 direct → mechanism → feature。
- `pollutant_prototype_map` 命中降级（`_has_perf_for` 门控 direct_evidence）。

### 2B. 源项目原型抽取扩库（提交 c0f736e + f162e06 + 908f613）
逐设计扫描 `biomimetic-adsorbent-design` 四分支（Ultimate portfolio 十套方案 + main 的 ROX/PFHxS 深研 + `research/bmdl/paired` 的 model_only/bmdl_assisted 设计批次 + Qwen `rounds/` + kimi-k3）。

| 新原型 id | 中文 | 来源 | 目标污染物 | 接地层级 |
|---|---|---|---|---|
| `beta-cyclodextrin-hostguest-inclusion` | β-环糊精天然环腔主客体包合 | Ultimate S2 | PFOA/PFOS/PFBS/BPA/壬基酚/MB | 去重保留；正确 DOI `10.1038/nature16185`；专项映射为 inspiration |
| `sert-serotonin-transporter-aromatic-amine-recognition` | SERT 芳香胺中央位点识别 | model_only A5 | ODV/文拉法辛（芳香胺药物）| exploratory / needs_review |
| `wastewater-biofilm-macrolide-class-enrichment` | 成熟污水生物膜大环内酯类别富集（系统仿生）| main ROX | 罗红霉素/克拉霉素/红霉素 | exploratory；界面材料化为 llm_inferred |
| `dhps-dihydropteroate-synthase-paba-recognition` | DHPS 条件性 PABA/磺胺识别 | batch_b | SMX | exploratory；3H26 非 SMX/pABA 直接结构 |
| `arsr-arsenic-trithiol-disorder-to-order` | ArsR 砷三硫醇 AsS3 捕获 | batch_b | As(III) | exploratory / needs_review |

未入库判定：PFHxS "PFH-1"（工程离子交换珠，非仿生原型）；ER/GPER 烷基酚（证据弱）、BSA（与 HSA 近重复）暂缓。

### 2C. 检索排序修复（本轮，待提交）
问题：`query()` 合并后按 lane 顺序取 `[:10]`，`find_direct_evidence` 按 ppm 遍历顺序返回（非权重），导致后接线的新原型被截断而不浮现；且 `As(III)` 为 bare-list，ArsR 完全不可见。

改动（`tools/biomimetic_context.py` + `feature-mapping.json`）：
1. `find_direct_evidence` 返回前按 `(direct_evidence, weight)` 降序排序。
2. brief 候选上限 `[:10]` → `[:15]`。
3. 有机诚实域（PFOA/SMX/BPA）：无真实 `performance_data` 的 ppm 命中 `match_basis` 由 `direct_pollutant_evidence` 降级为 `mechanism_feature_bridge`（与 `direct_evidence` 门控一致，避免违反有机域诚实门）。
4. `ppm['As(III)']` 由 bare-list 转 `{"prototypes":[...]}`，使 ArsR 被扫描。

效果（修复后浮现排名）：SMX→DHPS **1/12**；As(III)→ArsR **4/15**；PFOA→β-CD **12/15**；BPA→β-CD **7/14**；Roxithromycin→biofilm **4/12**。

---

## 3. 验证状态（本轮结束时）

| 检查 | 结果 |
|---|---|
| pytest（biomimetic_context/interface_honesty/canon_safety/invariant_guard）| **21 passed** |
| validate_consistency | 0 error |
| check_from_source_integrity | 0 non-compliant |
| check_chimera --strict | 10 违规（**预存**，5 个新原型均单物种/单群落未新增）|
| verify_adrmats_delivery | SMX **PASS**（已回升）· Pb(II) PASS · PFOA/BPA/chimera **FAIL（预存基线）** |
| ADRMATS 导出 | 586 行 / 44 污染物，含全部 5 个新原型 |

---

## 4. 遗留问题 / 后续建议（待你决策）

| 优先级 | 问题 | 建议 |
|---|---|---|
| 中 | `pollutant_prototype_map` 47/69 键为 bare-list，`find_direct_evidence` 主要靠 `mechanism_summary` 扫描，bare-list 条目不被键路由扫描（大量映射实际"死"）| 统一治理：要么把 bare-list 全转 dict-form，要么修 `find_direct_evidence` 的键匹配分支同时处理两种形态（需跑全回归，防止 47 键复活冲击 gold-set）|
| 中 | `verify_adrmats_delivery` 有机域口径：PFOA/BPA 的 plant-lignocellulosic/fabp4 有真实容量数据，与"有机域一律无直接证据"门冲突 | 口径评审：要么承认这些有机域真实数据、放宽门；要么把这些候选也降级 |
| 低 | `check_chimera` 10 个多物种 organism（蛋白家族跨物种）| 逐个核定是否拆分/改写 organism 字段 |
| 低 | β-CD 对 PFOA 排名 12/15（旗舰污染物 top 区被 16 个预存直接候选占据）| 若要 β-CD 更靠前，需评审 PFOA 既有候选权重校准（非本轮范围）|

---

## 5. 提交记录（massive 分支）

| 提交 | 主题 |
|---|---|
| 3034aee | Track2A 机制层主体 |
| 9ebcc11 | Track2A 激活 mechanism_feature_bridge（补全 Step 3）|
| c0f736e | Track2B 抽取 β-环糊精（89→90）|
| f162e06 | Track2B 抽取 SERT + 污水生物膜（90→92）|
| 908f613 | Track2B 抽取 DHPS + ArsR；源挖矿完成（92→94）|
| （本轮）| 检索排序修复 + README + 本文档 |
