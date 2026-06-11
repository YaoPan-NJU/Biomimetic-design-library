# 项目下一步执行计划 v2（交本地 AI 执行 · 可直接处理原始文献）

> 适用项目：Biomimetic-design-library（生物原型知识库，ADRMATS 系统的仿生检索模块）
> 适用执行者：能直接读取本地原始文献（PDF）的 AI agent（OpenClaw）
> 配套文档：仓库内 `docs/HANDOFF.md`（项目背景与状态总览）。本文件与其冲突时，以本文件为准。
> 工作分支：`feature/library-enhancement`（唯一，勿在 main / biomimetic-story-v2 / project/tracking 上开发）
> 编制日期：2026-06-05

---

## 本版更新（v2，必读）

抽样验证（任务 1，mussel-foot-adhesion）已完成，结论比预期严重：

- 7 条性能数据引用全部为 LLM 编造（材料体系、精确到小数点的 qmax、作者-年份-期刊俱全，但论文组合不存在）。
- 5 条基础文献引用中 2 条编造（Waite 2011 Nature 标题/期刊/年份全错，真实为 Holten-Andersen 2007 Nature Materials；Ryu 2018 Adv Funct Mater 的 DOI 返回 404）；3 条真实（Lee 2007 Science、Holten-Andersen 2011 PNAS、Dreyer 2012 Langmuir）。
- 库中 3 篇 PDA 论文无一包含原型声称的 7 个数值。原型里"Fu et al. 2015"虽是真论文，却是 PDA 微球吸附染料（Chem Eng J），被错安到"PDA@Fe3O4 吸附 Pb²⁺"（J Mater Chem A）上。

由此带来的变更：

1. **5 个手工标杆全部判定不可信**，不是只有 mussel。它们同一流程产出，需先清理（任务 1），不是深化。
2. **手工/LLM 直接撰写内容的路线作废**。此后所有内容只能来自对真实 PDF 的 grounded 提取。
3. **校验改为双层**。原静态不变量"literature 必须有 ref"不够，因为编造条目恰恰有 ref（只是假的），静态校验会放行。必须叠加 agentic 核查（解析 ref + 核对数值），见第 4 节。`verification=verified` 永不许自报。
4. **任务重排**：清理隔离 → 建体系与双层校验 → ID 对齐 → 用真实 PDF 重建标杆 → 批量 → 核查规则 → 扩到 100。
5. 25 个空壳现在比 5 个"填好的"标杆状态更好：空壳是诚实的待补充、可恢复；编造带毒、会污染下游。

---

## 0. 给本地 AI 的第一步：自检，别信文档里的进度数字

Windows 用 `python`，`grep` 换 `findstr` 或用 Git Bash。

```bash
git checkout feature/library-enhancement && git pull
python - <<'PY'
import json, os
meta = set(json.load(open('feature-mapping.json'))['prototype_metadata'].keys())
have = {n for n in os.listdir('prototypes') if os.path.exists(f'prototypes/{n}/prototype.md')}
print('canonical IDs:', len(meta), '| 有内容的目录:', len(have))
print('断链(索引->空目录):', sorted(meta - have))
print('孤儿(有内容->索引不到):', sorted(have - meta))
PY
```

确认本地文献库可访问，记录路径与结构（预期：`C:\Users\15995\Desktop\仿生文献库`，约 302 论文 + 33 专利 + 6 标准，分 8 组 + 全局综述）。把自检结果回报项目负责人确认后再动手。

---

## 1. 项目目标与边界

最终形态是约 100 个达到质量基线的生物原型，外加经验证的设计规则，作为 ADRMATS 多智能体系统的仿生检索模块。库只做匹配检索，不做推理与组合（约束识别归 ADRMATS 的 AdaptiveConstrainingAgent，组合推理归对抗设计引擎）。库的价值在于提供有证据、可溯源的仿生上下文。

---

## 2. 当前真实状态（已核实）

内容层：5 个手工标杆已确认为编造（chitosan、lotus-leaf、metal-organic-framework、mussel-foot-adhesion、sulfate-reducing-bacteria），其性能数据与部分引用不可信；其余约 25 个为诚实空壳（06-04 仅扫摘要的旧产出）。

提取引擎：OpenClaw agent 直接读 PDF。仓库内 Python 流水线（`extraction/`）目前产不出仿生叙事，深度提取以 agent 读全文为准；`writer.py`/routing 可作 frontmatter 骨架与粗路由的辅助。

工具与配置：`writer.py` 已修六项 bug，测试 66 个全过。`prototype_routing.json` 33 个原型均带 `category` 与 `biomimetic_dimension`。ID 对齐约 23/33，剩 10 断链、7 孤儿。

已知小问题：`validators.py` 期望 qmax 标量但 Phase 4 返回 dict；`qmax_range` 残留单位未剥净；标杆章节编号有 bug（两个 "## 10."）；frontmatter `category` 仍是 "biomimetic_adsorbent"，未用 taxonomy 分类。

design-rules.json 的 40 条规则为 LLM 草稿、引用标 require verification，按 mussel 结果推断其引用很可能也是编造，任务 6 前默认全部存疑。

---

## 3. 最高优先的铁律：证据完整性

整个项目的成败系于一条规则：

**AI 可以推理与综合（标注清楚即可），但绝不能给一个它没有从原文读到的数值挂上引用。**

危险的不是推理本身，是推理穿着引用的外衣。一个标"低置信"的定性机制描述可以接受；一个编造的 qmax 配一个假引用就是错误信息，会直接污染下游 ADRMATS。

这次的教训补充一点：有引用不等于可信。编造条目也带格式完整的引用，所以仅靠"有没有 ref"的静态检查挡不住。真伪只能靠解析 ref、核对数值这一步（第 4 节）。`verification=verified` 永远不许由生成方自报，只能由核查产生。

---

## 4. provenance 标注体系 + 双层校验

来源是每条 claim 的属性，不是整篇文件的属性。沿用 `design-rules.json` 已有的 `generation_method` 思路，全仓库统一。

**两个正交维度：**
- `source`：`literature` | `patent` | `standard` | `llm_inference`
- `verification`：`verified` | `unverified` | `conflict`
- `confidence`（0 到 1）是上述两者加证据强度的函数。

**性能数据用结构化字段承载（写入 frontmatter，供机器解析），prose 表格由它渲染：**

```yaml
performance_data:
  - pollutant: "Pb(II)"
    material: "PDA@Fe3O4"
    qmax: 185.2
    qmax_unit: "mg/g"
    removal_rate: ">95%"
    ph: 5.0
    temperature: 25
    isotherm: "Langmuir"
    kinetics: "pseudo-second-order"
    source: "literature"        # literature/patent/standard 必须配可解析 ref；llm_inference 必须 ref=null
    ref_doi: "10.1039/xxxxxx"   # DOI 优先；无法解析就不能标 literature
    source_file: "组3/Zhang2016_PDA_SiO2.pdf"   # 指向本地库的文件，便于复核
    verification: "verified"    # 只能由第 4 节核查流程产生，禁止自报
    confidence: 0.9
```

机制与叙事段落用 prose 行内标注。机制块、叙事小节末尾加一行：

```
> 溯源：source=literature；ref_doi=10.xxxx/yyyy（Lee et al., 2007, Science）；verification=verified
```

设计推断（5.4 这类超出论文直接结论的推理）标为：

```
> 溯源：source=llm_inference；ref=null；基于上述机制的设计推断，非文献直接结论
```

**校验分两层，两层都要过：**

第一层，静态校验（脚本，确定性）。任务 2 的 `tools/validate_consistency.py` 检查结构：
1. `feature-mapping.json` 每个 ID 都有非空 `prototype.md`（无断链）；
2. 无孤儿内容目录；
3. `feature-mapping.json` 与 `prototype_routing.json` 的 ID 集合一致；
4. frontmatter 必填字段齐全，`category` ∈ {微生物, 植物, 动物, 仿生材料}；
5. `performance_data` 中 `source` 为 literature/patent/standard 必须有非空 `ref_doi`，`source=llm_inference` 必须 `ref=null`；
6. 凡标 `verification=verified` 的 literature 条目，必须带可解析格式的 `ref_doi` 或非空 `source_file`，否则视为违规（挡住"自称已核实"）。

第二层，agentic 核查（OpenClaw，查真伪）。对每条 literature 数据：
1. 解析 `ref_doi`（Crossref/web）。解析不到或指向另一篇 → FAIL（编造或错引）。
2. 打开被引论文或 `source_file` 的 PDF，确认该 qmax/数值确实出现在其中，且对应同一材料与污染物。引用真但数值无 → FAIL（错归属/错数值）。
3. 交叉核对本地库：来源应确实在文献库中（本项目的证据基座是这批 PDF）。
4. 三步全过才置 `verification=verified`。
5. 产出一份核查报告（沿用本次 mussel 的表格：类别 / 总数 / 真实 / 编造 / 无法核实），作为审计轨。

新内容经第 5 节 grounded 提取产生时，因 agent 是从 PDF 读出，`verification` 可直接置 verified，但必须同时记 `ref_doi` 与 `source_file` 以便复核。旧的可疑内容靠第二层核查暴露。

---

## 5. 文献接地提取协议（本地 AI 的核心工作方式）

你能直接读 PDF，必须用它把数据接地，而不是凭记忆生成。对每个原型：

1. **归集论文。** 用 `prototype_routing.json` 关键词 + 文献库 8 组结构，从 302 篇里挑出相关 PDF。
2. **逐篇读取，只记原文所述。** 每篇记录：材料/生物体、机制（连同支撑句）、性能（qmax/去除率/条件，记下确切数值与所在表格或页码）、结构特征。每个数据点绑定来源论文（`ref_doi` + `source_file`）。
3. **建 performance_data。** 一条对应一篇论文真实报道的一组（污染物，材料）；不许跨论文拼凑，不许取整或外推。
4. **机制。** 每条论断追到某篇某句，按第 4 节标注。
5. **叙事 5.1 到 5.5。** 复述已提取事实的句子标 literature 加 ref；属于设计推断、超出论文结论的句子标 llm_inference 加 ref=null。叙事里绝不放带引用的数值。
6. **缺源即留空。** 字段在可得论文里没来源就留空（基线检查会显示未达标），不许编造填补。

---

## 6. 任务清单（按顺序，前序未过验收不进下一步）

### 任务 1【立即 · 止损】清理 5 个手工标杆的编造内容

- mussel-foot-adhesion：删除 7 条编造性能数据与 2 条假基础引用（Waite 2011、Ryu 2018），保留 3 条真实引用（Lee 2007、Holten-Andersen 2011、Dreyer 2012）。
- 其余 4 个标杆（chitosan、lotus-leaf、MOF、SRB）：用第 4 节第二层核查各做一遍，凡解析不到或数值无法在被引论文中核到的，一律删除。
- 处理原则：性能表与未核实引用删除（git 历史已留底，必要时可在 `prototypes/<id>/_quarantine.md` 留存被删内容备查）；保留章节结构与已核实引用；定性机制/叙事 prose 若科学方向正确可保留，但重标为 `llm_inference`、剥掉其中任何具体数值与引用。顺手修章节编号 bug、把 `category` 改成 taxonomy 分类（贻贝→动物、荷叶→植物、MOF→仿生材料、SRB→微生物）。
- 验收：5 个标杆中不存在任何"数值 + 未核实引用"；状态重置为"待接地的空壳 + 已核实引用"。

### 任务 2【基础设施】provenance 模板 + 双层校验

- 按第 4 节更新 `templates/prototype-template.md`，加入 `performance_data` 结构与机制/叙事溯源标注。
- 新建 `tools/validate_consistency.py`，实现第 4 节第一层（静态）全部 6 项检查，接入 pre-commit 或 CI。
- 将第 4 节第二层（agentic 核查）固化为强制流程文档，明确 `verification=verified` 只能由核查产生。
- 验收：脚本能检出当前仓库的 10 断链、7 孤儿、category 问题与任意缺 ref 违规并返回非零。

### 任务 3【收尾对齐 + 清理】

- 按 `docs/prototype-id-mapping.md` 执行合并改名，消除 10 断链、7 孤儿。明显合并项：`chlorella`→`chlorella-cell-wall`；`hydroxyapatite-adsorbent` 与 `fish-scale-hydroxyapatite`、`diatom-microspheres` 与 `diatom-frustule`/`diatom-inspired-porous` 要么合并要么按 keep-both 都登进 `feature-mapping.json`。
- 修 `validators.py` 的 qmax schema、`qmax_range` 残留单位正则。
- 验收：`validate_consistency.py` 全过，断链与孤儿均为 0。

### 任务 4【用真实 PDF 重建 5 个标杆 · 生产能力关口】

按第 5 节协议，用文献库 PDF 从零重建 5 个标杆的性能数据、机制、叙事，全部带 `ref_doi` + `source_file` 并过第 4 节双层校验。
- 验收：5 个标杆达质量基线（见第 8 节），每条数据 verified。
- 这一任务是生产能力关口：上一轮抽样只证明了 OpenClaw 能"查出编造"，尚未证明它能"读 PDF 产出干净的接地内容"。若在此连一个干净标杆都产不出，立即停下回报，再决定批量是否可行。

### 任务 5【批量深化剩余原型】

按第 5 节协议处理剩余约 25 个空壳 + 5 个零覆盖原型（bone-structure、cactus-spine、cell-membrane-ion-channel、coral-skeleton、lobster-exoskeleton），顺序按 `feature-mapping.json` 引用频次从高到低。校验脚本在批处理循环中每个原型完成即跑，不要末尾统一跑。
- 验收：每个原型达基线且带完整 provenance，逐个过双层校验。

### 任务 6【核查设计规则】

对 design-rules.json 的 40 条规则做第 4 节第二层核查，解析每条引用、核对其结论。通过的标 `validated_against_exemplars: true` 并补真实 `ref_doi`；编造或无证据的降级或移除。
- 验收：超过 80% 规则有真实证据支撑；未验证规则不投入匹配层。

### 任务 7【扩到 100】

按 `docs/仿生设计方法论补充检索策略.md`（4 缺口领域、61 条检索词）补充文献，按 spec 第 5 节阶段二（34 到 60，补薄弱仿生维度：壁虎黏附、藤壶水泥、乌贼喙、鲍鱼壳珍珠层、生物膜、群体感应菌、嗜极古菌、竹维管束等）与阶段三（61 到 100）逐个新增。每新增一个走第 7 节标准动作。
- 验收：原型约 100，每个过基线与双层校验。

---

## 7. 每加一个原型的标准动作

1. `feature-mapping.json#prototype_metadata` 加 ID 与 applicability，并在相关 `pollutant_prototype_map`/`feature_prototype_map`/`constraint_prototype_map` 加权重条目。
2. `prototype_routing.json` 加同名 ID 的中英文关键词 + category + biomimetic_dimension。
3. 涉及新类别/污染物/机制，先在 `taxonomy/*.md` 登记。
4. 按第 5 节协议读 PDF 产出达基线、带 provenance 的 `prototype.md`。
5. 过 `validate_consistency.py`（静态）+ agentic 核查（真伪），通过方可提交。
ID 命名：英文小写加连字符，偏好更通用的短名，仅确为不同概念才并存。

---

## 8. 完成的定义

**单原型质量基线：** 仿生叙事 5.1 到 5.5 至少 3 节有实质内容；至少 3 种污染物有 qmax 或去除率；至少 2 个机制写全；四尺度至少描述 2 个；11 项工程约束至少评估 5 项。**且：** 所有定量数据与机制论断带 provenance，`source=literature` 的均 `verification=verified`（经第 4 节第二层核查），零"数值 + 未核实引用"。

**整体：** 原型约 100；规则经核查后 80 到 120 条 + 原则 30 到 50 条，平均置信度 > 0.8；100% 原型过双层校验；每标杆 ≥ 15 篇文献、其余 ≥ 5 篇；ADRMATS 端到端能消费 BiomimeticContext。

---

## 9. 不要做的事

- 不要给任何未从原文读到的数值挂引用（第 3 节铁律）。
- 不要让生成方自报 `verification=verified`；它只能由核查产生。
- 不要 LLM 直接撰写内容；所有内容来自对真实 PDF 的 grounded 提取。
- 不要跨论文拼凑或外推性能数值；不要取整美化。
- 不要在还有 `[待补充]`（尤其叙事 5.1 到 5.5）时声称原型完成。
- 不要只改一份配置就加原型（三份须同步，见第 7 节）。
- 不要把未验证的规则喂给匹配层。
- 不要混淆"流水线 Phase"与"spec Phase"（见 `docs/HANDOFF.md` 第 2 节）。
- 不要在 main / biomimetic-story-v2 / project/tracking 上开发。
- 不要相信旧文档或任何"已完成"自述的进度，以第 0 节自检与核查报告为准。

---

## 10. 给本地 AI 的开场提示词（可直接复制）

```
你将接手 Biomimetic-design-library 项目，你可以直接读取本地原始文献库（OpenClaw 读 PDF）。请先读仓库根目录的本执行计划 v2（下一步执行计划_本地AI.md），它是当前权威行动指南，与其他文档冲突时以它为准，背景见 docs/HANDOFF.md。

前情：抽样验证已确认 5 个手工标杆的性能数据与部分引用是 LLM 编造的。最高优先的铁律是第 3 节：你可以推理并标注清楚，但绝不能给一个你没从原文读到的数值挂引用；verification=verified 只能由核查产生，禁止自报。

开始前，按第 0 节自检真实状态、确认本地文献库路径，回报给我确认。

确认后从任务 1（清理 5 个标杆的编造内容，含对其余 4 个的核查）开始，再做任务 2（建 provenance 模板 + 双层校验脚本），逐步推进。每完成一步对照验收标准自检并回报，未过验收不进下一步。任务 4（用真实 PDF 重建标杆）若连一个干净标杆都产不出，立即停下回报。

唯一工作分支是 feature/library-enhancement。
```
