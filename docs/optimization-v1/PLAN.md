# 仿生吸附设计库 · 策展与接地优化方案 v1

> 执行对象：本地 AI 工程代理
> 操作仓库：`Biomimetic-design-library`，分支基线 `adsorption/dev`
> 编制日期：2026-06-14
> 核心约束：核验预算无限（可对每条断言开 PDF 逐条确认），不考虑时间/token 成本；唯一要求是**严格按本方案的方法与验收标准执行**。

---

## 0. 写在最前（执行总则，必须逐条遵守）

> **配套必读**：本方案的判定标准（§1）、字段 schema（§2）、Phase 8 边界三档与数值护栏已抽成单页卡片 `DEFINITIONS.md`。本地 AI **全程挂载 `DEFINITIONS.md`**，遇歧义先查它；它与本方案冲突时以它为准并回报 Yao。

**北极星**：本库唯一的价值是**给下游提供大模型自己拿不到、且对吸附设计有用的因果链**。库的原子产出不是"性能数字"，而是一张**接地的、原型特异的、可迁移的因果链卡（含失效边界），并诚实标注其证据等级**。

**九条铁律（违反任意一条即判该阶段不通过）：**

1. **不许把推断当事实。** 任何由模型补全/推断的内容，`basis` 必须标 `llm_inferred`，永远不得升级为 `verified`，在 brief 中永远显示为"推断"。
2. **不许夸大证据。** 证据等级只能来自真实核验结果（见 §1），禁止任何硬编码默认值。
3. **先 dry-run 再写入。** 所有批量修改 JSON 的脚本，必须先输出"将要改什么"的 dry-run 报告（不落盘），人工/自检确认后再执行写入。
4. **每阶段产出一份阶段报告**，固定包含四块：①修改文件列表 ②执行的命令 ③验收命令的实际输出 ④残留风险。报告存到 `docs/optimization-v1/phaseN-report.md`。
5. **不许跳验收。** 每个 Phase 的"验收标准"全部为绿，才能进入下一个 Phase。
6. **surgical 改动。** 只改本方案要求改的内容；不顺手"优化"无关代码、注释、格式；不删除非本方案产生的死代码（发现了就在阶段报告里记一笔）。
7. **canon 唯一真源是 `prototypes_db/*.json`。** 所有 `prototypes/*/prototype.md`、`feature-mapping.json` 等都是派生物，改完 canon 后用既有工具重建，不手改派生物。⚠️ **严禁运行 `build_prototypes_db.py`**——它从 extraction 原始 JSON 重建 canon，会冲掉 Phase 2/3/4 的清理（chimera 复活、已删机制重入）。canon 已冻结，只在其上直接编辑；生成 prototype.md 用 `generate_prototype_md.py`（canon→md 方向）。
8. **不确定就停。** 任何一步遇到本方案没覆盖的歧义，停止该条目处理，把它记入该阶段报告的"待裁决清单"，继续处理其它条目，最后统一交回 Yao。
9. **全程 UTF-8。** Python 脚本统一 `python -X utf8`。

**总执行顺序（依赖关系已排好，不得乱序）：**
Phase 0 准备 → 1 修接口诚实度 → 2 策展落地 → 3 去污染 → 4 字段语义与诚实标注 → 5 因果链补全 → 6 PDF 核验 → 7 设计转译重做 → 8 失效边界与 DO-NOT → 9 总验收。

---

## 1. 统一名词与判定标准（消除歧义，所有 Phase 通用）

### 1.1 证据等级 `verification`（用于每条 mechanism 与每条 performance_data）

| 等级 | 精确定义（判定标准） |
|------|----------------------|
| `verified` | 已打开该条目标注的来源（`source_file` 或 `ref_doi`），在其中**定位到该断言本身**（机制描述或具体数值）。必须记录 `locator`（页码/章节）与 `quote`（原文引用 ≤300 字）。 |
| `corroborated` | 在 **≥2 个相互独立来源**（不同 DOI/不同作者团队）中都达到 `verified`。两条来源信息都要记录。 |
| `refuted` | 打开来源后**找不到**该断言，或来源内容与该断言**矛盾**。→ 该条目从 canon 中**删除**，并记入 `refuted` 日志（见 Phase 6）。 |
| `needs_review` | 来源文件缺失/无法获取，或条目字段本身残缺到无法核验。→ 暂留但**禁止进入 brief 排序**。 |

> 旧值 `unverified` / `single_source` **只能作为"未核验的初始态"**，不得作为任何 active 原型的终态。Phase 6 结束后，active 原型里不允许残留 `unverified`/`single_source`。

### 1.2 来源/推断标记 `basis`（用于因果链每个步骤、design_translation）

- `from_source`：该说法能在引用文献中直接定位（须给 locator）。
- `llm_inferred`：该说法是模型基于化学/物理常识的推断，文献中没有直接出处。**永不升级为 verified。**

### 1.3 "接地（grounded）"的判定

一条 mechanism 算"接地"，当且仅当它的 `causal_chain`（见 §2）**四个核心要素**（`pollutant_feature` / `bio_structure` / `interaction` / `why_it_works`）**全部非空、且都不是 `needs_review`**。否则视为"未接地"。

### 1.4 "因果链卡"的合格判定

见 §2 的 `causal_chain` 结构。一张卡合格 = 四要素齐全 + 每个 `from_source` 要素都有 locator + 至少 1 条 `boundary_conditions` + 1 条 `transferable_principle`。缺任一项 → 该机制 `verification=needs_review`。

### 1.5 "嵌合/污染（chimera）"的判定

一条 mechanism 或 performance_data 属于污染，当且仅当**它的主语主体（所述的生物体/材料/结构）与所在原型的身份不一致**。
- 判定规则：若该条目的 `name`/`description`/`基本原理` 的**主体**指向了与本原型 `organism.scientific` 不同的生物/材料，且不是作为"对比/参照"出现，而是作为本条目的主角 → 判污染。
- 处置：能对应到库内另一个正确原型 → 迁移过去；否则 → 删除。两种都记入污染处置日志。

### 1.6 "套话（boilerplate）"的判定（用于 design_translation）

一条设计转译属于套话（不合格），当且仅当满足以下任一：
- 命中禁用泛词清单（见 Phase 7）且没有原型特异内容；或
- **把原型名替换成任意其它原型后，这段话依然成立**（即不特异）；或
- 缺少 Phase 7 要求的三要素（具体官能团/结构、具体材料实现抓手、目标污染物相互作用）。

### 1.7 pollutant 字段回填判定

对 `performance_data[].pollutant` 为空的条目，按优先级尝试判定：
1. 从 `parameter` / `value` / `material` / `conditions` 文本中出现的污染物名（含化学式、别名）识别；
2. 用 `pollutant_aliases.json` 归一到 canonical 名；
3. 若文本中出现**多个**污染物且无法确定该条具体指哪个 → **不要猜**，置 `verification=needs_review`，并在 `note` 写"pollutant ambiguous"；
4. 若完全无法识别 → 保持空 + `verification=needs_review`，进入待裁决清单。
**绝对禁止**：用空字符串去参与任何匹配（这正是 Phase 1 要修的 bug）。

---

## 2. 数据 Schema 增补（精确字段，本地 AI 按此写 JSON）

在现有 mechanism 对象上**新增/规范**以下字段（不破坏既有字段）：

```json
{
  "name": "机制名（须与本原型身份一致）",
  "source": "literature | patent",
  "ref_doi": "10.xxxx/xxxx",
  "source_file": "xxx.pdf",
  "verification": "verified | corroborated | refuted | needs_review",
  "基本原理": "一句接地的因果陈述（= causal_chain.why_it_works 的自然语言版）",
  "causal_chain": {
    "pollutant_feature": {"text": "污染物的哪个特征触发吸附", "basis": "from_source|llm_inferred", "locator": "p.x / Sec.y 或 null"},
    "bio_structure":     {"text": "生物的哪个结构/官能团负责", "basis": "...", "locator": "..."},
    "interaction":       {"text": "二者之间的相互作用类型", "basis": "...", "locator": "..."},
    "why_it_works":      {"text": "为什么有效（因果）", "basis": "...", "locator": "..."},
    "boundary_conditions": [
      {"text": "在什么条件下该机制失效/减弱（pH/盐度/温度/竞争离子…）", "basis": "...", "locator": "..."}
    ],
    "transferable_principle": "脱离该物种后可迁移到任意材料设计的功能原理一句话",
    "verification_quote": "若 verified/corroborated：来源原文引用 ≤300 字；否则 null"
  }
}
```

performance_data 条目：保留原字段，确保 `pollutant` 已按 §1.7 处理，`verification` 按 §1.1 取值，并新增 `verification_quote`（verified 时必填）。

design_translation（每个 active 原型至少一条，写入 narrative，结构化）：

```json
{
  "idea": "原型特异、可操作的一段设计思路",
  "specific_functional_group": "具体官能团/结构，如 邻苯二酚(catechol)双齿位点",
  "material_handle": "具体材料实现抓手，如 弱碱性pH下多巴胺自聚成涂层并控厚度",
  "target_interaction": "对应的污染物相互作用，如 与软金属的双齿螯合",
  "source_tier": "literature | llm_inference",
  "examples": ["文献里现成的 生物→材料 转译（若有，附 DOI）"]
}
```

> 字段命名一律照抄上面，不得自创同义字段；中文键 `基本原理` 保留以兼容既有工具。

---

## 3. 原型处置总表（31 个，最终决定，已纳入 Yao 的反馈）

> 处置类型：**KEEP-DEEPEN**=保留并补全核验；**VERIFY-FIRST**=已接地，优先开 PDF 转 verified；**DEMOTE**=移入材料参考、退出仿生检索；**PARK**=移出（超范围，停放）；**DEDUP**=并入同源原型；**ANTIFOULING**=保留为抗污原型。

| 原型 | 处置 | 说明 |
|------|------|------|
| chitosan 壳聚糖 | VERIFY-FIRST | Yao 确认保留：壳聚糖=甲壳素脱乙酰，氨基/羟基配位是真仿生机制；已 132/120 接地，先做去重(132条机制必有碎片重复)再开 PDF 核验 |
| chlorella-cell-wall 小球藻细胞壁 | VERIFY-FIRST | 已接地100%，优先核验转 verified |
| diatom-frustule 硅藻壳 | VERIFY-FIRST | 已接地60%，优先核验 |
| mussel-foot-adhesion 贻贝足丝 | KEEP-DEEPEN | **必须先 Phase 3 去除纳米纤维素污染**，再补全核验 |
| polydopamine-coating 聚多巴胺涂层 | KEEP-DEEPEN | 通用儿茶酚/胺表面化学 |
| plant-tannin 植物单宁 | KEEP-DEEPEN | 多酚多齿螯合 |
| sulfate-reducing-bacteria 硫酸盐还原菌 | KEEP-DEEPEN | 生物硫化沉淀软金属 |
| iron-oxidizing-bacteria 铁氧化菌 | KEEP-DEEPEN | 生物铁氧化物除 As/P |
| cell-membrane-ion-channel 细胞膜离子通道 | KEEP-DEEPEN | 选择性离子识别 |
| magnetic-bacteria 趋磁细菌 | KEEP-DEEPEN | 空壳，从零建；磁小体→磁分离回收 |
| mangrove-root 红树林根 | KEEP-DEEPEN | 盐排斥/选择性输运 |
| biomineralization-template 生物矿化模板 | KEEP-DEEPEN | 空壳，从零建；模板化多级孔 |
| dna-aptamer DNA适配体 | KEEP-DEEPEN | 空壳，从零建；分子识别超选择性 |
| oyster-shell 牡蛎壳 | KEEP-DEEPEN | **保留为独立生物原型**（撤销合并），填实核验 |
| scallop-shell 扇贝壳 | KEEP-DEEPEN | 同上，独立保留 |
| coral-skeleton 珊瑚骨骼 | KEEP-DEEPEN | 同上，独立保留（空壳→从零建）|
| fish-scale-hydroxyapatite 鱼鳞羟基磷灰石 | KEEP-DEEPEN | **独立保留**（撤销并入骨结构），89条机制需去碎片 |
| bone-structure 骨结构 | KEEP-DEEPEN | 独立保留 |
| silk-fibroin 丝素蛋白 | KEEP-DEEPEN | 吸收 silkworm-silk |
| spider-silk 蜘蛛丝 | KEEP-DEEPEN | 保留（独立物种，低优先），补吸附相关因果链 |
| mycelium 菌丝体 | KEEP-DEEPEN | 几丁质/葡聚糖生物吸附网络 |
| wood-xylem 木质部 | KEEP-DEEPEN | 多级输运孔道 |
| lobster-exoskeleton 龙虾外骨骼 | KEEP-DEEPEN | 几丁质-矿物复合 |
| pitcher-plant-slippery-surface 猪笼草滑面 | ANTIFOULING | Yao 确认保留为**抗污原型**，function 标 `anti_fouling`，不参与吸附排序但可被抗污查询召回 |
| metal-organic-framework MOF | DEMOTE | 合成材料，非仿生 |
| cellulose-nanocrystal 纤维素纳米晶 | DEMOTE | 生物来源但信息增益低；可被 Yao 一句话拉回 |
| starch-granule 淀粉颗粒 | DEMOTE | 同上 |
| alginate 海藻酸盐 | DEMOTE | 同上 |
| silkworm-silk 蚕丝 | DEDUP | 并入 silk-fibroin（同为家蚕丝蛋白）|
| diatom-inspired-porous 仿硅藻多孔 | DEDUP | 并入 diatom-frustule（非独立生物体）|
| namib-beetle 纳米布甲虫 | PARK | 超出吸附范围（集水），移入 `prototypes_db/parked/` |

> active 仿生原型（KEEP-DEEPEN + VERIFY-FIRST + ANTIFOULING）共 **24 个**；DEMOTE 4 个；DEDUP 2 个；PARK 1 个。合计 31。

---

## 4. 分阶段执行

> 每个 Phase 固定格式：目的 / 前置 / 步骤 / 判定标准 / 验收（命令 + 期望输出）/ 产物。

### Phase 0 — 准备与基线冻结

**目的**：建立干净工作分支，记录整改前基线，建立报告目录。

**步骤**
1. 基于远端最新 `adsorption/dev` 新建分支 `opt/curation-grounding-v1`。
2. 新建目录 `docs/optimization-v1/`，把本方案复制为 `docs/optimization-v1/PLAN.md`。
3. 写脚本 `tools/snapshot_stats.py`：遍历 `prototypes_db/*.json`（含 `parked/`、`enrichment/` 单独统计），输出：原型数、机制总数、接地机制数（按 §1.3）、performance 总数、各 `verification` 计数、空 pollutant 数、空壳原型清单。结果存 `docs/optimization-v1/phase0-baseline.md`。

**判定标准**：脚本输出可复现（连跑两次结果一致）。

**验收**
```bash
python -X utf8 tools/snapshot_stats.py
# 期望：在 docs/optimization-v1/phase0-baseline.md 生成统计表，且与本方案 §3 的原型清单一致（31个）
git rev-parse --abbrev-ref HEAD   # 期望输出 opt/curation-grounding-v1
```

**产物**：分支、`PLAN.md`、`phase0-baseline.md`、`tools/snapshot_stats.py`、`phase0-report.md`。

---

### Phase 1 — 修接口诚实度 P0 bug

**目的**：堵住接口"夸大证据 + 空值乱配"两个会污染下游的硬 bug。

**前置**：Phase 0 完成。

**步骤**（改 `tools/biomimetic_context.py`，最小改动）
1. **去硬编码**：删除把 mechanism 的 `verification_tier` 写死成 `'single_source'` 的代码（约第 385 行）。改为读取该机制条目真实的 `verification` 值；若该字段缺失 → 填 `'needs_review'`。
2. **空 pollutant 不匹配**：修 `_get_performance_leads`（约第 455 行）。当前 `pol.lower() in pollutant.lower()` 会让空字符串匹配一切。改判定规则：`pol` 为空或 `None` → **跳过该条**，不进入 performance_leads。
3. 不改其它逻辑。

**判定标准**：见验收的单元行为。

**验收**
```bash
# 新增最小测试 tools/test_interface_honesty.py，包含两个断言：
# (a) 构造一个含空 pollutant 的 performance 条目，查询任意污染物，结果 performance_leads 不含该条；
# (b) 构造一个 verification=needs_review 的机制，brief 中该机制 attribution.verification_tier == 'needs_review'（不得是 single_source）。
python -X utf8 tools/test_interface_honesty.py   # 期望：全部 PASS
# 回归：Pb(II) 查询，确认 mussel 不再因 cellulose 空数据被异常抬到前排
python -X utf8 tools/biomimetic_context.py        # 期望：能正常输出，无报错（注意原 main() 有 brief['candidates'] 笔误，顺手改成 brief['brief']['candidates']）
python -X utf8 tools/verify_adrmats_delivery.py    # 期望：仍 6/6 PASS
```

**产物**：改后的 `biomimetic_context.py`、`tools/test_interface_honesty.py`、`phase1-report.md`。

---

### Phase 2 — 策展落地（按 §3 总表执行处置）

**目的**：让仓库里的原型集合与 §3 决定一致，且全程可追溯、零静默丢失。

**前置**：Phase 1 完成。

**步骤**
1. **PARK**：`mkdir prototypes_db/parked/`，把 `namib-beetle.json` 移入。它不参与任何吸附检索。
2. **DEMOTE**：`mkdir prototypes_db/materials_reference/`，把 `metal-organic-framework.json`、`cellulose-nanocrystal.json`、`starch-granule.json`、`alginate.json` 移入。在每个文件加字段 `"status": "material_reference"`。
3. **DEDUP**：
   - 把 `silkworm-silk.json` 的非空内容合并进 `silk-fibroin.json`（按 §1.5 先确认无污染再并），然后删除 `silkworm-silk.json`。
   - 把 `diatom-inspired-porous.json` 的非空内容合并进 `diatom-frustule.json`，然后删除 `diatom-inspired-porous.json`。
   - 合并时若两边有重复机制（同 DOI + 同主旨）→ 去重保留一条。
4. **ANTIFOULING**：在 `pitcher-plant-slippery-surface.json` 加 `"function": "anti_fouling"`；在 `feature-mapping.json` 里确保它**不进入吸附 pollutant 排序**，仅当查询意图含"抗污/防污"时召回（若现有 mapping 无此通道，记入待裁决，先打标不接线）。
5. 同步更新 `feature-mapping.json` / `feature_matching_rules.json`：移除指向 PARK/DEMOTE/已删除原型的引用。
6. 写一份 `docs/optimization-v1/phase2-moves.md`：逐条记录每个原型的"从→到/删除/合并目标"。

**判定标准**：active 原型恰为 §3 列出的 24 个；DEMOTE/PARK/DEDUP 结果与总表逐条一致。

**验收**
```bash
ls prototypes_db/*.json | wc -l            # 期望：24（active 顶层）
ls prototypes_db/materials_reference/*.json | wc -l   # 期望：4
ls prototypes_db/parked/*.json | wc -l     # 期望：1
test ! -f prototypes_db/silkworm-silk.json && echo OK-dedup1
test ! -f prototypes_db/diatom-inspired-porous.json && echo OK-dedup2
python -X utf8 tools/validate_consistency.py   # 期望：0 error
python -X utf8 tools/check_repo_hygiene.py     # 期望：通过
```

**产物**：移动后的目录、`phase2-moves.md`、`phase2-report.md`。

---

### Phase 3 — 去污染 + chimera 真清理

**目的**：清掉会误导下游的错机制，并让 `check_chimera.py` 真能抓到（现在是假绿）。

**前置**：Phase 2 完成。

**步骤**
1. 扩展 `tools/check_chimera.py`：
   - 加载一个污染对 blocklist（写在 `tools/chimera_blocklist.json`），格式 `{"prototype_id": ["禁用主体词", ...]}`。种子条目（至少包含）：
     - `mussel-foot-adhesion`: `["cellulose","nanocellulose","nanocrystal","纤维素"]`
     - `polydopamine-coating`: `["stenocara","desert beetle","namib","沙漠甲虫","纳米布甲虫"]`
     - `spider-silk`: `["lotus","荷叶","pitcher","猪笼草"]`
   - 通用规则（§1.5）：扫描每条 mechanism 的 `name`+`description`+`基本原理`，若其主体词命中本原型 blocklist，或出现与本原型 `organism` 明显不符且作为主语的生物/材料 → 标记为 violation，打印 `原型/条目/命中词/原文片段`。
2. 对每个 violation 按 §1.5 处置（迁移或删除），处置写入 `docs/optimization-v1/phase3-decontam.md`。
3. 把 blocklist 检查接入重建流程（`build_prototypes_db.py` 重建后自动跑一遍 chimera 检查，非 0 则报错），防止重跑后污染复发。

**判定标准**：修复前 `check_chimera.py` 必须能报出 mussel/cellulose 这一类（证明检查有效），修复后为 0。

**验收**
```bash
# 先在修复前跑一次，确认能抓到（留存输出到报告）
python -X utf8 tools/check_chimera.py   # 修复内容前：期望 > 0 violation 且包含 mussel-foot-adhesion×cellulose
# 完成处置后再跑
python -X utf8 tools/check_chimera.py   # 期望：0 violation
# 验证 mussel 不再含纤维素机制
python -X utf8 -c "import json;d=json.load(open('prototypes_db/mussel-foot-adhesion.json'));b=json.dumps(d,ensure_ascii=False).lower();print('cellulose' in b or 'nanocellulose' in b)"  # 期望：False
```

**产物**：扩展后的 `check_chimera.py`、`chimera_blocklist.json`、`phase3-decontam.md`、`phase3-report.md`。

---

### Phase 4 — 字段语义修复与诚实标注

**目的**：把 organism、pollutant、证据/推断标记修到"可被诚实消费"的最低线。

**前置**：Phase 3 完成。

**步骤**
1. **organism 复核**：跑一遍核对，确认每个 active 原型 `organism.scientific` 与其真实生物一致（Phase 已修过，这里只复核，发现错的修）。
2. **pollutant 回填**：对 active 原型所有 `performance_data[].pollutant` 为空的条目，按 §1.7 处理（可复用/改进 `tools/fill_pollutant_smart.py`，但必须先 dry-run）。不能判定的置 `needs_review`，不许猜。
3. **加诚实标注字段**：给每条 mechanism 补 `causal_chain` 骨架（此阶段先建空骨架 + `basis` 占位，内容在 Phase 5 填）；把所有 mechanism 现有 `verification` 统一为合法初始态（核验前一律 `needs_review`，禁止保留 `single_source`/`unverified` 作为终态——它们会在 Phase 6 被真实核验覆盖）。
4. 重建并导出 enrichment：`python tools/build_prototypes_db.py --export-enrichment`，确认 active 原型每个都有对应 enrichment 文件，且重建前后富化字段零丢失。

**判定标准**：active 原型空 pollutant（非 needs_review）数 = 0；organism 明显错误 = 0；每条 mechanism 都有 `causal_chain` 键。

**验收**
```bash
python -X utf8 -c "
import json,glob
bad=0
for f in glob.glob('prototypes_db/*.json'):
    d=json.load(open(f))
    for p in d.get('performance_data',[]):
        if not p.get('pollutant') and p.get('verification')!='needs_review': bad+=1
    for m in d.get('mechanisms',[]):
        if 'causal_chain' not in m: bad+=1
print('defects=',bad)"   # 期望：defects= 0
python -X utf8 tools/validate_consistency.py   # 期望：0 error
ls prototypes_db/enrichment/*.json | wc -l      # 期望：24（每个 active 一个）
```

**产物**：修后 canon、enrichment、`phase4-report.md`（含 pollutant 回填 dry-run 与最终差异、待裁决清单）。

---

### Phase 5 — 因果链补全引擎（LLM 补全，结构化 + 自标来源）

**目的**：给每个 active 原型产出**结构化、可证伪、诚实标注**的因果链卡，覆盖到位。

**前置**：Phase 4 完成。

**工作方式（对每个 active 原型逐个执行）**
1. 读该原型已抽取的机制/性能/源文献，为它产出 **1–N 张** `causal_chain` 卡（按 §2 结构），覆盖该原型主要的吸附/功能机制。
2. 每张卡的每个要素，明确判断它是 `from_source`（能在引用文献定位，给 locator）还是 `llm_inferred`（常识推断）。**把"文献说的"和"我推的"分开**，不许混。
3. 必填 `transferable_principle`（脱离物种的功能原理）与至少 1 条 `boundary_conditions`（先写出来，真伪在 Phase 6 核验）。
4. 输出禁止笼统：要素文本必须点名具体官能团/结构与具体相互作用类型（如"邻苯二酚双齿位点与软金属的螯合"，不能写"具有良好的吸附性能"）。
5. 把补全产物写进对应 mechanism 的 `causal_chain`；`基本原理` 同步为 `why_it_works.text`。

**判定标准（合格卡，按 §1.4）**：四要素齐全、`from_source` 要素都有 locator、有 boundary、有 transferable_principle。空壳原型（magnetic-bacteria、biomineralization-template、coral-skeleton、dna-aptamer）必须从其领域文献新建至少 1 张合格卡（找不到可靠文献则置 `needs_review` 并入待裁决，不许编）。

**验收**
```bash
# 新增 tools/check_causal_chain.py：对每个 active 原型，统计合格卡数、缺要素清单、未标 basis 的要素数
python -X utf8 tools/check_causal_chain.py
# 期望：每个 active 原型 ≥1 张合格卡；"未标 basis 的要素" = 0；输出明细表存 docs/optimization-v1/phase5-chains.md
```

**产物**：补全后的 canon、`tools/check_causal_chain.py`、`phase5-chains.md`、`phase5-report.md`。

---

### Phase 6 — PDF 逐条核验引擎（把"叙事"变"知识"）

**目的**：用无限核验预算，把 active 原型的每条 `from_source` 断言与每条 performance 数值，开 PDF 逐条确认，落实 `verified`/`corroborated`/`refuted`。

**前置**：Phase 5 完成。

**工作方式（对每个 active 原型逐个执行；每条待核验断言走同一流程）**
1. 取断言的来源（`source_file` / `ref_doi`），打开 PDF。
2. 在 PDF 内检索该断言（机制说法或数值）。按 §1.1 判定：
   - 定位到且一致 → `verification=verified`，记录 `locator`（页/章节）+ `verification_quote`（原文 ≤300 字）。
   - 在 ≥2 个独立来源都定位到 → `corroborated`（两条来源都记录）。
   - 找不到 / 矛盾 → `refuted`：**从 canon 删除该条目**，把 `{原型, 条目摘要, 来源, 删除原因}` 追加到 `docs/optimization-v1/refuted-log.md`。
   - 来源文件确实拿不到 → `needs_review`，把缺失文件列入 `docs/optimization-v1/missing-sources.md`。
3. `llm_inferred` 的因果链要素**不走文献核验**：保持 `llm_inferred`，但若被某条 verified 来源**证伪**，则改写或删除该要素。
4. 每个原型产出一份核验日志 `docs/optimization-v1/verify-logs/<id>.md`，逐条列：断言 / 来源 / 结论(tier) / 页码 / 引用。

**判定标准**：active 原型中**没有任何 mechanism/performance 停留在 `unverified`/`single_source`**；每条 `verified`/`corroborated` 都带 locator + quote；所有 `refuted` 都已删除并记日志。

**验收**
```bash
python -X utf8 -c "
import json,glob,collections
c=collections.Counter(); noq=0
for f in glob.glob('prototypes_db/*.json'):
    d=json.load(open(f))
    for m in d.get('mechanisms',[]):
        v=m.get('verification'); c[v]+=1
        if v in ('verified','corroborated') and not m.get('causal_chain',{}).get('verification_quote'): noq+=1
    for p in d.get('performance_data',[]):
        c['perf:'+str(p.get('verification'))]+=1
print(dict(c)); print('verified缺quote=',noq)"
# 期望：不出现 'unverified'/'single_source'（active）；verified 计数 > 0；verified缺quote = 0
ls docs/optimization-v1/verify-logs/ | wc -l   # 期望：= active 原型数（24）
```

**产物**：核验后 canon、`verify-logs/`、`refuted-log.md`、`missing-sources.md`、`phase6-report.md`。

---

### Phase 7 — 设计转译重做（原型特异、可证伪、诚实标 tier）

**目的**：把 design_translation 从套话改成"能指导设计、且诚实标注来源/推断"的内容。

**前置**：Phase 6 完成。

**步骤**
1. 为每个 active 原型按 §2 的 design_translation 结构写 ≥1 条，必须含三要素：`specific_functional_group` / `material_handle` / `target_interaction`，并标 `source_tier`（有文献现成"生物→材料"转译则 literature 并附 DOI，否则 llm_inference）。
2. 删除/改写所有命中套话判定（§1.6）的旧转译。
3. 禁用泛词清单（命中且无特异内容即判不合格，至少包含）：`良好的吸附性能、优异的、广泛的应用前景、具有潜力、提高效率、绿色环保、多种污染物、协同效应（无机理说明时）`。

**判定标准（§1.6）**：每个 active 原型至少 1 条合格转译；把原型名替换成别的原型后该段不再成立（特异性）；无命中禁用泛词的不合格条。

**验收**
```bash
# 新增 tools/check_translation_specificity.py：检测每个 active 原型的 design_translation 是否含三要素、是否命中禁用泛词
python -X utf8 tools/check_translation_specificity.py
# 期望：每个 active 原型 ≥1 条合格；不合格条 = 0；明细存 docs/optimization-v1/phase7-translation.md
```

**产物**：改后 canon、`tools/check_translation_specificity.py`、`phase7-translation.md`、`phase7-report.md`。

---

### Phase 8 — 失效边界与 DO-NOT 输出（对接 ADRMATS）

**目的**：把每个 active 机制的失效/适用边界沉淀成结构化条目，按证据强度分级，生成 ADRMATS 可消费的 DO-NOT（硬约束）与 caution（软提示），并优先复用库内已有的边界资产。

**前置**：Phase 7 完成。

> 北极星：边界知识是"知道机制在哪里失效"，它和正向机制同等重要。但边界最容易被模型编造**带假精度的数字阈值**——本阶段的护栏就是为了堵这个。

#### 8.1 边界的三档来源（按优先级，逐条边界都要标明属于哪一档）

| 档 | 来源 | 标注 | 能否带数值阈值 | 进 ADRMATS 的形态 |
|----|------|------|----------------|-------------------|
| **A 档（首选，零新增下载）** | 从 Phase 6 正在核验的**同一批 PDF** 里摘出边界（吸附文献普遍报告 pH 依赖、离子强度、共存离子干扰、再生衰减、湿稳定性） | `basis=from_source` + `verification=verified/corroborated` + locator + quote | **可以**（数字必须来自 PDF 原文） | **硬 DO-NOT**（可门控排序） |
| **B 档（推理 + 复用资产 + 人工校对）** | 由机制第一性原理推出，或**复用库内既有资产**（见 8.3） | `basis=llm_inferred` + `verification=needs_review`（永不升 verified） | **不可以**，只能定性（如"低 pH 下因质子化而被抑制"） | **软 caution**（只提示，不门控） |
| **C 档（例外，质量优先时允许）** | A、B 都支撑不了的**高风险**边界，需要新文献 | 由本地 AI**写检索请求**（见 8.5），学生下载，PDF 到位后按 A 档核验 | 到位核验后才可带数值 | 核验前 `needs_review`，核验后转 A 档（硬 DO-NOT） |

**判定"高风险"（决定是否值得动用 C 档）**：满足任一即高风险——①该边界若错会让 ADRMATS 选出在目标工况下会溶解/失效的材料；②涉及饮用水/痕量污染物等安全敏感场景；③该原型是 KEEP-DEEPEN 核心且当前完全无边界信息。非高风险且 A/B 无支撑 → 直接置 `needs_review`，不必走 C 档。

#### 8.2 数值阈值护栏（硬规则，违反即不通过）

- **任何具体数值阈值（pH 值、盐度浓度、温度、循环次数等）只允许出现在 A 档（verified）边界里**，且必须有 `locator` + `quote`。
- B 档与"C 档未到位"的边界**一律只能定性**，禁止出现数字。例：可写"高盐下 egg-box 交联因 Ca²⁺ 被竞争而减弱"，**不可**写"NaCl > 0.5 M 时失效"除非有 PDF 出处。
- 校验脚本须能抓出"basis≠from_source 却含数字阈值"的违规条目。

#### 8.3 复用库内既有边界资产（先用现成的，别从零推）

库里已有可直接利用的资产，本阶段须**先扫描、对齐、校对**它们，而不是重新发明：
- `docs/imported/library-enhancement/principles/mechanisms/*.md`：如 `catechol-low-ph-suppression.md`、`high-salinity-coordination-suppression.md`、`universal-proton-suppression.md`、`competitive-ion-saturation.md` 等——机制级失效原理。
- `docs/imported/library-enhancement/principles/trade-offs/*.md`：如 `acid-resistance-vs-carboxyl-coordination.md`、`wet-stability-vs-functional-activity.md` 等——权衡型边界。
- `docs/imported/library-enhancement/design-rules.json` 的 `condition_mechanism_rules`：已是"条件→机制行为"的结构化规则，且已被接口 `find_applicable_rules` 读取（当前为 `pending_validation`）。

对齐方法：把每条资产挂到它影响的 active 原型的 `boundary_conditions` 上。默认 `basis=llm_inferred / verification=needs_review`（因为这些资产本就是 pending_validation）；**只有当能在某篇 A 档 PDF 里核实该条边界时，才升为 verified 并允许带数值**。

#### 8.4 字段、导出与接口

`boundary_conditions` 每条目结构（扩展 §2 的卡内字段）：
```json
{
  "text": "定性描述（B/C未到位时禁含数字）",
  "parameter": "pH | salinity | temperature | competing_ion | wet_stability | regeneration | other",
  "condition": {"operator": "range|threshold_gt|threshold_lt|qualitative", "value": [低,高] 或 [阈值] 或 null},
  "basis": "from_source | llm_inferred",
  "verification": "verified | corroborated | needs_review",
  "gate_level": "hard | soft",
  "locator": "p.x / Sec.y 或 null",
  "quote": "verified 时原文 ≤300 字，否则 null",
  "source_asset": "若复用自 principles/ 或 design-rules.json，写来源文件名/rule_id，否则 null"
}
```
规则：`gate_level=hard` ⟺ `basis=from_source 且 verification∈{verified,corroborated}`；其余一律 `soft`。

写 `tools/export_do_not.py`：遍历 active 原型，汇总边界到 `exports/adrmats_do_not.json`，每条含 `{prototype_id, parameter, condition, text, gate_level, basis, verification, locator, source_asset}`。`condition` 用机器可读结构，便于接口按工况匹配。

改 `biomimetic_context.py`：brief 新增 `rule_based_cautions`，按当前查询工况匹配边界——`hard` 进 DO-NOT 段（可参与门控），`soft` 进 caution 段（只提示，不制造 direct evidence）。

#### 8.5 C 档检索请求清单（交学生下载用）

当判定需要 C 档时，本地 AI **不自行下载**，而是把需求写进 `docs/optimization-v1/literature-requests.md`，每条一行表格，字段：

| prototype_id | 待支撑的边界断言 | 为何高风险 | 检索词（中文） | 检索词（English，含布尔式） | 建议数据库 | 期望证据 |
|---|---|---|---|---|---|---|

英文检索词须给可直接粘贴的布尔式，例：`("polydopamine" OR "catechol") AND ("pH" ) AND ("adsorption" OR "chelation") AND ("desorption" OR "stability")`。学生下载后把 PDF 放入 `data/literature/` 并回填 `source_file`，本地 AI 再按 A 档核验。

#### 步骤小结
1. 复核每个 active 机制的 `boundary_conditions`，按 8.1 三档逐条定档、按 8.2 护栏处理数值。
2. 按 8.3 扫描并对齐 `principles/`、`trade-offs/`、`design-rules.json`，挂到对应原型。
3. 对高风险且 A/B 无支撑的边界，按 8.5 写检索请求；非高风险的置 `needs_review`。
4. 写 `tools/export_do_not.py` 与校验脚本 `tools/check_boundary_guardrail.py`（抓数值护栏违规、gate_level 一致性）。
5. 接口加 `rule_based_cautions`（hard/soft 分流）。

**判定标准**：每个 active 原型至少 1 条 boundary；无"非 from_source 却带数字阈值"的违规条；`gate_level` 与 basis/verification 一致；所有 C 档需求已写入 `literature-requests.md`。

**验收**
```bash
python -X utf8 tools/check_boundary_guardrail.py
# 期望：数值阈值护栏违规=0；gate_level 不一致=0；每个 active 原型 ≥1 条 boundary
python -X utf8 tools/export_do_not.py        # 期望：生成 exports/adrmats_do_not.json
python -X utf8 -c "import json;d=json.load(open('exports/adrmats_do_not.json'));print('边界条数=',len(d));print('硬DO-NOT=',sum(1 for x in d if x['gate_level']=='hard'));assert all('gate_level' in x and 'basis' in x for x in d)"
# 期望：边界条数>0；硬DO-NOT 来自 verified；无断言报错
# 低 pH 查询应返回 caution（如 catechol/carboxyl 低 pH 抑制，soft）
python -X utf8 tools/verify_adrmats_delivery.py   # 期望：仍全 PASS，且覆盖 cautions 输出
```

**产物**：`tools/export_do_not.py`、`tools/check_boundary_guardrail.py`、`exports/adrmats_do_not.json`、`docs/optimization-v1/literature-requests.md`、改后 `biomimetic_context.py`、`phase8-report.md`。

---

### Phase 9 — 总验收与交付

**目的**：形成一个可信、可调用、文档与真实状态一致的版本。

**前置**：Phase 0–8 全部通过。

**步骤**
1. 重建派生物：⚠️ **不运行 `build_prototypes_db.py`**（会冲掉清理）。改用 `generate_prototype_md.py` 从 canon 生成 prototype.md；enrichment 已在 Phase 4 导出。随后跑全套检查。
2. 重新生成 4 个金标准 brief 示例（Pb(II)、PFOA、SMX、BPA），存 `examples/adrmats_briefs/`，并人工抽查其 `honesty_ledger`：verified 进 facts、llm_inferred 进 inferences，无错配。
3. 更新 `README.md` 与 `docs/SUPPORT_SCOPE_AND_RISKS.md`，使统计与真实一致（verified 数、active 原型数、DEMOTE/PARK 说明）。
4. 写总验收报告 `docs/optimization-v1/FINAL-report.md`。

**总验收清单（全绿才算完成）**
```bash
python -X utf8 tools/validate_consistency.py        # 0 error
python -X utf8 tools/check_chimera.py               # 0 violation（且 blocklist 已覆盖 mussel/cellulose）
python -X utf8 tools/check_causal_chain.py          # 每个 active 原型 ≥1 合格卡；basis 全标
python -X utf8 tools/check_translation_specificity.py   # 无不合格转译
python -X utf8 tools/check_boundary_guardrail.py    # 数值阈值护栏违规=0；gate_level 一致
python -X utf8 tools/test_interface_honesty.py      # PASS
python -X utf8 tools/verify_adrmats_delivery.py     # 6/6 PASS
python -X utf8 tools/check_repo_hygiene.py          # PASS
```
- [ ] active 原型 = 24，DEMOTE=4，PARK=1，DEDUP 已删除 2
- [ ] active 原型无 `unverified`/`single_source` 残留；`verified` 计数 > 0
- [ ] 每条 verified/corroborated 有 locator + quote
- [ ] 每个 active 原型 ≥1 条 boundary；无"非 from_source 却带数字阈值"违规
- [ ] `refuted-log.md`、`missing-sources.md`、`verify-logs/`、`literature-requests.md` 齐全
- [ ] README/SUPPORT 文档与统计一致

**产物**：最终 canon、`examples/adrmats_briefs/`、`exports/adrmats_do_not.json`、`docs/optimization-v1/FINAL-report.md`。

---

## 5. 交回 Yao 复核时需提交的清单

1. `docs/optimization-v1/` 下全部阶段报告 + `FINAL-report.md`。
2. `phase0-baseline.md` 与最终统计的对照（改了什么、为什么）。
3. `refuted-log.md`（被核验删掉的条目）、`待裁决清单`（所有歧义条目汇总）。
4. 全套验收命令的实际输出截图/文本。
5. 4 个重生成的 brief 示例。
6. `literature-requests.md`（C 档新文献检索请求清单，交学生下载）+ `exports/adrmats_do_not.json`。

> 复核口径：Yao 会重点抽查 ①是否有把 llm_inferred 标成 verified 的；②refuted 删除是否合理；③因果链卡是否特异、有边界；④待裁决清单是否被擅自"猜测"处理。

---

## 6. 给本地 AI 的最后提醒

- 看不懂某条原型该归哪类、某条断言算不算 verified、某机制算不算污染——**回到 §1 的判定标准逐条对照**；仍不确定就进"待裁决"，不要自由发挥。
- 每个 Phase 结束**停下来**，产出阶段报告，再继续。
- 你交付的不是"看起来很全的库"，而是"窄但每条都接地、可溯源、诚实标注的库"。**宁可少而真，不可多而假。**
