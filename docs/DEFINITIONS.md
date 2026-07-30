# DEFINITIONS · 判定标准与字段卡（始终挂载）

> 本卡是《优化方案_仿生库策展与接地_v1.md》的判定标准与字段定义的**单页权威摘录**，供上下文短的本地 AI 全程挂载。任何歧义先查本卡；本卡与正文冲突时，以本卡为准并回报 Yao。

---

## 0. 九条铁律（违反任意一条 = 该阶段不通过）

1. 不许把推断当事实：模型补全/推断的内容 `basis=llm_inferred`，永不升 `verified`，brief 中永远显示"推断"。
2. 不许夸大证据：证据等级只能来自真实核验，禁止任何硬编码默认值。
3. 先 dry-run 再写入：批量改 JSON 前先输出"将改什么"的 dry-run，确认后再落盘。
4. 每阶段产一份报告：①改了哪些文件 ②执行的命令 ③验收实际输出 ④残留风险。存 `docs/optimization-v1/phaseN-report.md`。
5. 不许跳验收：本阶段验收全绿才进下一阶段。
6. surgical 改动：只改方案要求的；不顺手优化无关代码/注释/格式；发现既有死代码只记录不删。
7. canon 唯一真源 = `prototypes_db/*.json`；派生物（`prototype.md`、`feature-mapping.json`）用工具重建，不手改。
8. 不确定就停：歧义条目进"待裁决清单"，继续处理其它，最后交回 Yao；**绝不自由发挥/猜测**。
9. 全程 `python -X utf8`。

**一句话总纲：宁可少而真，不可多而假。**

---

## 1. 证据等级 `verification`（每条 mechanism / performance_data）

| 等级 | 判定标准 |
|------|----------|
| `verified` | 已开来源 PDF，**定位到该断言本身**；必须记 `locator`(页/章节) + `quote`(原文 ≤300 字)。 |
| `corroborated` | 在 **≥2 个独立来源**（不同 DOI/团队）均 verified；两条来源都记录。 |
| `refuted` | 开 PDF 后**找不到**或**矛盾** → **删除该条目** + 记入 `refuted-log.md`。 |
| `needs_review` | 来源缺失/无法获取，或字段残缺无法核验 → 暂留，**禁止进 brief 排序**。 |

> `unverified`/`single_source` 只能是"核验前初始态"，Phase 6 后 active 原型不得残留。

## 2. 来源/推断标记 `basis`（因果链每要素、design_translation、boundary）

- `from_source`：能在引用文献定位（须给 `locator`）。
- `llm_inferred`：常识/机理推断，文献无直接出处。**永不升 verified。**

## 3. "接地 grounded"

mechanism 算接地 ⟺ 其 `causal_chain` 的四要素 `pollutant_feature / bio_structure / interaction / why_it_works` **全非空且都非 needs_review**。

## 4. "因果链卡"合格

四要素齐全 + 每个 `from_source` 要素有 locator + ≥1 条 `boundary_conditions` + 有 `transferable_principle`。缺任一 → 该机制 `verification=needs_review`。

## 5. "嵌合/污染 chimera"

某条目的**主语主体**（所述生物体/材料/结构）与所在原型 `organism.scientific` 不一致、且作为主角而非对比 → 判污染。处置：能对应到库内正确原型则迁移，否则删除；均记日志。
种子污染对（写入 `tools/chimera_blocklist.json`）：
- `mussel-foot-adhesion` ✗ `cellulose / nanocellulose / nanocrystal / 纤维素`
- `polydopamine-coating` ✗ `stenocara / desert beetle / namib / 沙漠甲虫 / 纳米布甲虫`
- `spider-silk` ✗ `lotus / 荷叶 / pitcher / 猪笼草`

## 6. "套话 boilerplate"（design_translation 不合格）

命中任一即不合格：① 命中禁用泛词且无原型特异内容；② 把原型名替换成别的原型后该段仍成立（不特异）；③ 缺三要素之一。
禁用泛词（至少）：`良好的吸附性能、优异的、广泛的应用前景、具有潜力、提高效率、绿色环保、多种污染物、协同效应（无机理说明时）`。

## 7. pollutant 回填

优先级：①从 `parameter/value/material/conditions` 文本识别污染物名 → ②`pollutant_aliases.json` 归一 → ③多个污染物无法确定该条指哪个：置 `needs_review` + note "pollutant ambiguous" → ④完全无法识别：留空 + `needs_review` + 入待裁决。**绝不用空字符串参与匹配。**

---

## 8. 失效边界三档来源 + 数值护栏（Phase 8 专用）

| 档 | 来源 | 标注 | 数值阈值 | 进 ADRMATS |
|----|------|------|----------|-----------|
| **A** | 同批 PDF 摘边界（首选，零下载） | `from_source` + `verified/corroborated` + locator + quote | **可带**（须 PDF 原文） | **硬 DO-NOT** |
| **B** | 机理推理 / 复用 `principles/`、`trade-offs/`、`design-rules.json` | `llm_inferred` + `needs_review` | **禁止带数字**，只定性 | **软 caution** |
| **C** | 高风险且 A/B 无支撑 → 写检索请求交学生下载 | 到位后按 A 档核验 | 核验后才可带数字 | 核验前 needs_review |

**数值护栏（硬规则）**：具体数字阈值（pH/盐度/温度/循环数）**只允许出现在 A 档 verified 条目**。B 档与 C 档未到位的边界**一律只能定性，禁止出现数字**。

**高风险判定（是否值得动 C 档）**：① 边界若错会导致选出在目标工况下溶解/失效的材料；② 饮用水/痕量等安全敏感；③ 该原型是 KEEP-DEEPEN 核心且当前完全无边界。非高风险且无支撑 → 直接 `needs_review`，不走 C 档。

**`gate_level` 规则**：`hard` ⟺ `basis=from_source 且 verification∈{verified,corroborated}`；其余一律 `soft`。

---

## 9. 字段 Schema（照抄字段名，不得自创同义字段）

### mechanism（新增/规范 `causal_chain`）
```json
{
  "name": "机制名（须与本原型身份一致）",
  "source": "literature | patent",
  "ref_doi": "10.xxxx/xxxx",
  "source_file": "xxx.pdf",
  "verification": "verified | corroborated | refuted | needs_review",
  "基本原理": "= causal_chain.why_it_works.text 的自然语言版",
  "causal_chain": {
    "pollutant_feature": {"text": "", "basis": "from_source|llm_inferred", "locator": "p.x/Sec.y 或 null"},
    "bio_structure":     {"text": "", "basis": "", "locator": ""},
    "interaction":       {"text": "", "basis": "", "locator": ""},
    "why_it_works":      {"text": "", "basis": "", "locator": ""},
    "boundary_conditions": [
      {
        "text": "定性描述（B/C未到位禁含数字）",
        "parameter": "pH|salinity|temperature|competing_ion|wet_stability|regeneration|other",
        "condition": {"operator": "range|threshold_gt|threshold_lt|qualitative", "value": "[低,高]|[阈值]|null"},
        "basis": "from_source|llm_inferred",
        "verification": "verified|corroborated|needs_review",
        "gate_level": "hard|soft",
        "locator": "p.x/Sec.y 或 null",
        "quote": "verified 时 ≤300 字，否则 null",
        "source_asset": "复用自 principles/ 或 design-rules.json 时写来源/rule_id，否则 null"
      }
    ],
    "transferable_principle": "脱离物种、可迁移到任意材料设计的功能原理一句话",
    "verification_quote": "verified/corroborated 时来源原文 ≤300 字，否则 null"
  }
}
```

### performance_data
保留原字段；`pollutant` 按 §7 处理；`verification` 按 §1；`verification_quote`（verified 时必填）。

### design_translation（每个 active 原型 ≥1 条）
```json
{
  "idea": "原型特异、可操作的设计思路",
  "specific_functional_group": "具体官能团/结构",
  "material_handle": "具体材料实现抓手（合成/改性路线）",
  "target_interaction": "对应的污染物相互作用",
  "source_tier": "literature | llm_inference",
  "examples": ["文献现成的 生物→材料 转译（附 DOI，若有）"]
}
```

---

## 10. C 档检索请求清单格式（`docs/optimization-v1/literature-requests.md`）

本地 AI **不自行下载**，按下表逐行写需求交学生：

| prototype_id | 待支撑的边界断言 | 为何高风险 | 检索词（中文） | 检索词（English 布尔式） | 建议数据库 | 期望证据 |
|---|---|---|---|---|---|---|

英文须给可直接粘贴的布尔式，例：`("polydopamine" OR "catechol") AND "pH" AND ("adsorption" OR "chelation") AND ("desorption" OR "stability")`。
