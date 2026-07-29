# massive 分支第三方复核修复记录

日期：2026-07-29

工作分支：`codex/fix-massive-audit`

基线：`massive@fdf6105`

expand 修复合并：`96d1375`（包含 `6be0a82`）

## 结论

`expand` 的机制卡、边界条件、诚实分层和门禁修复可复用，已按保留双边历史的方式并入 `massive`。本轮没有把低质量条目删除，而是修正重复身份、错误 DOI、来源范围错配和证据等级，让它们以真实质量继续留库。

## 原型处置

| 原型 | 处置 | 当前可接受边界 |
|---|---|---|
| `beta-cyclodextrin-hostguest-inclusion` | 保留 expand canonical；删除 massive 重复项 | DOI 为 `10.1038/nature16185`；污染物专项关联不是直接吸附证据 |
| `arsr-arsenic-trithiol-disorder-to-order` | 降为 exploratory | 三硫醇配位是有价值线索；逐字引文/定位器未闭环，不得标 verified |
| `sert-serotonin-transporter-aromatic-amine-recognition` | 降为 exploratory | SERT 结构方向可作启发；ODV/文拉法辛及材料转译未获直接来源支持 |
| `wastewater-biofilm-macrolide-class-enrichment` | 降为 exploratory | 类别富集方向可保留；浅层阴离子、低极性界面是材料假说 |
| `dhps-dihydropteroate-synthase-paba-recognition` | 降为 exploratory 并重写机制边界 | 3H26 是蝶呤抑制剂结构；仅保留 DHPP 先行结合后的条件性识别假说 |

## 共享逻辑修复

- `direct_evidence` 现在必须同时具备已核验来源、定位器、逐字引文和去除/吸附性能指标；蛋白结合 Kd、传感器响应或检测限不再冒充材料去除证据。
- `pollutant_prototype_map` 永远输出 inspiration；只有同一机制卡的 `pollutant_feature` 具备完整来源四件套时才获得来源加权。
- 每个 brief 最多取 8 个污染物专项映射和 4 个策展特征映射，给独立的机制检索保留位置；机制命中绑定到实际 `mechanism_id`。
- 修正污染物别名递归扫描中过短 JSON 键误命中的问题，并隔离 `oil-water` 用例路由。
- `check_causal_chain.py` 现在会在零合格原型或空 basis 时返回非零状态，避免假绿。
- 18 条来源卫生 warning 已清零：参考文献残片和非法 DOI 不再作为 `from_source`；有完整逐字句的 XPS 条目改用已有完整引文，未新增或猜测来源。
- 补齐 5 个旧 canonical 原型缺失的 `organism.category`，并把该字段加入一致性硬检查，避免 Markdown 渲染器到运行期才崩溃。

## 完备性边界

当前记录能证明本轮列出的迁移条目已经处置，不能证明源项目所有历史与后续分支都已逐文件审计。尤其 `fresh_1000` 集合和 EreA/EreB 线索仍需从 `biomimetic-adsorbent-design` 建立“分支/设计文件/方案结果/原型/处置”清单后再决定是否入库。这个缺口不影响本轮已修改条目的真实性，但阻止发布“迁移已完整”的结论。

## 当前规模

- root canonical 原型：100
- 机制卡：630
- 层级：24 core / 65 extended / 11 exploratory
- 生命周期：93 active / 5 pending_extraction / 2 parked

最终门禁结果以本分支提交前的验证输出为准。
