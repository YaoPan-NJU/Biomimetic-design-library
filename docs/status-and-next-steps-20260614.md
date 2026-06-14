## 仿生库整改状态盘点 & 下一步协作方案

---

### 一、两份文档的关系

你同事给了你两套文档：

1. **主整改方案**（`2026-06-10-biomimetic-library-remediation.md`）：8 个 Phase（0-7），覆盖安全、入库闭环、chimera 清理、字段修复、enrichment 分离、library-enhancement 导入、design-rules 接入、最终验收。范围大而全。

2. **Canon 稳定化子计划**（`canon-stabilization-plan-20260610.zip`，6 个 Phase）：是主方案的聚焦版，只做接口信任修复 + enrichment 分离 + 重建验证 + mapping 同步 + 交接报告。明确禁止 PG 工作，Phase 3 完成后是交接给 PG 同事的最低节点。

你选择性执行后，当前 `adsorption/dev` 分支的状态是**大部分完成了，但有几个关键缺口**。

---

### 二、逐项对照：做了什么、还差什么

| 主方案 Phase | 内容 | 状态 | 缺口 |
|-------------|------|------|------|
| P0 安全 + 基线 | 创建整改分支、token 处理、基线统计 | ✅ 分支已建、基线已记 | ⚠️ token 轮换状态不明（子模块显示 modified） |
| P1 入库闭环 | 第三波数据入库、批次追溯 | ✅ 第三波 63 JSON 已入库（性能数据 764→963） | ⚠️ 条目级批次追溯未实现 |
| P2 Chimera 清理 | PDA/甲虫、spider/荷叶、mussel/纤维素 | ⚠️ PDA 和 spider 已修，**mussel/cellulose 未修干净** | ❌ mussel-foot-adhesion 仍有 1 条机制 + 11 条性能含 cellulose 数据；`check_chimera.py` 未覆盖此污染对 |
| P3 字段修复 | organism 修正、pollutant 回填、verification 语义 | ⚠️ organism 已修（MOF/cellulose/namib-beetle） | ❌ pollutant 空字段从 226 **涨到 308**（新数据入库时未填）；❌ verification_status 全部缺失（963 条都没有） |
| P4 Enrichment 分离 | `--export-enrichment`、enrichment 目录、merge 改读 enrichment | ✅ 已实现 | ⚠️ enrichment 只有 21 个文件（不是 31 个）；`CHIMERA_BLOCKLIST` 没写进 build 脚本 |
| P5 Library-enhancement 导入 | design-rules.json + principles/ | ✅ 40 条规则 + 39 篇 markdown 已导入 | ⚠️ 全部缺 `validation_status` 标签（应为 `pending_validation`，实际字段不存在） |
| P6 Design-rules 接入 | `find_applicable_rules`、brief 输出 applicable_rules | ✅ 已实现并集成到 query() | ⚠️ 未验证的规则直接参与检索，可能导致误导 |
| P7 最终验收 | 四个脚本通过、README 更新 | ⚠️ 三个核心脚本通过 | ❌ README 仍是 v1.1 旧数据（752 条性能 vs 实际 963）；`check_repo_hygiene.py` 不存在 |

---

### 三、当前最危险的 4 个缺口

**缺口 1：mussel-foot-adhesion 的 cellulose 污染（P2 残留）**

`mussel-foot-adhesion.json` 中仍有 1 条机制叫 "Mechanisms of Heavy Metal Removal by Nanocellulose"（来自 DOI: 10.3390/nano11113008，一篇纳米纤维素论文），还有 11 条性能数据含 "Bacterial Nanocellulose"、"CNF"、"CNCs"、"cellulose/graphene aerogel" 等材料。`check_chimera.py` 检测不到，因为 `UNRELATED_ORGANISMS` 字典里没有 `mussel-foot-adhesion` 这个 key。ADRMATS 查询如果命中 mussel 原型，会把纤维素吸附机制当成贻贝仿生的设计灵感返回。

**缺口 2：308 条空 pollutant（P3 恶化）**

你同事方案的目标是降到 50 以下，实际从 226 涨到了 308——因为第三波数据入库时新数据也带着空 pollutant。`biomimetic_context.py` 的 `_get_performance_leads` 是否已经跳过空 pollutant 需要确认（同事的 Phase 1 要求改这个，但不确定是否执行了）。

**缺口 3：verification_status 全部缺失（P3 核心）**

963 条性能数据的 `verification` 字段全部是默认值或不存在。你同事方案里要求实现 5 档 evidence tier（verified / corroborated / single_source / needs_review / unverified），但目前这个系统没有在数据层面落地。`honesty_ledger` 的分桶逻辑（facts/leads/inferences）依赖这个字段，如果没有数据支撑，ledger 就是空的或全归 inference。

**缺口 4：design-rules 未标记验证状态就参与检索（P5/P6 风险）**

40 条规则全部是 `generation_method: "LLM_draft"`、`validated_against_exemplars: false`，但没有 `validation_status` 字段。`find_applicable_rules` 把它们当正常数据返回给 ADRMATS，下游 Agent 可能把这些未验证的 LLM 草稿当成可靠规则来用。

---

### 四、下一步该做什么

按优先级排序：

#### 立即做（本周）

1. **修 mussel/cellulose chimera**：编辑 `prototypes_db/mussel-foot-adhesion.json`，移除 cellulose/nanocellulose 相关的 1 条机制和 11 条性能数据。同时在 `check_chimera.py` 的 `UNRELATED_ORGANISMS` 中加入 `mussel-foot-adhesion: ['cellulose', 'nanocellulose', 'CNF', 'CNC', 'CMC', 'MCC', 'bacterial cellulose']`。

2. **确认 `_get_performance_leads` 是否跳过空 pollutant**：如果没有，改掉。这是同事 Phase 1 的核心修复点。

3. **给 design-rules 加 `validation_status: "pending_validation"`**：在 `design-rules.json` 中给每条规则加上这个字段。在 `find_applicable_rules` 的输出中标注 `"caution": "LLM-generated, not literature-validated"`。

#### 短期做（下周）

4. **补 pollutant 字段**：从 parameter、value、material、source_file 中智能推断 pollutant（之前同事给的 `fill_pollutant_smart.py` 可能已有这个功能，检查一下能不能再跑一轮）。目标从 308 降到 100 以下。

5. **实现 verification_status 落地**：参考同事方案 P3 中的 5 档定义，给已有 `ref_doi` 的条目标 `single_source`，有 `needs_review` 标记的保持，其余为 `unverified`。

6. **把 `CHIMERA_BLOCKLIST` 写进 `build_prototypes_db.py`**：目前只在文档里有，实际代码没有。确保重跑重建时 chimera 不会复发。

7. **更新 README**：把 v1.1 的旧数据换成当前实际统计。

#### 交接前做

8. **生成交接报告**：按同事 Phase 5 的格式，写一份 `canon-stabilization-report`，包含当前 HEAD、关键统计、验收结果、残留风险。这份报告是给同事的 PG 迁移工作的起点。

---

### 五、如何和同事协作

你们之间的分工边界已经很清楚了：

**你的地盘（仿生库）**：数据质量（chimera、pollutant、verification）、enrichment 架构、design-rules 验证、README 准确性、`BiomimeticContext.query()` 接口稳定性。

**同事的地盘（ADRMATS 侧）**：桥接模块（adapter）、prompt 改造（把 brief 喂给设计 Agent）、优雅降级、PG 迁移。

**交接点**：`BiomimeticContext.query()` 的输入输出契约。你保证这个接口稳定、返回数据可信、honesty_ledger 有意义；他基于这个接口建桥接模块和 PG 后端。

**建议你跟同事同步的信息**：

1. 当前库的 4 个缺口（上面列的），让他知道 brief 中的 verification tier 暂时不可靠、design-rules 是 LLM 草稿。他的 prompt 应该加上"对待 brief 中的信息要审慎，尤其是 applicable_rules 部分"。

2. 你的修复时间线：本周修 chimera + pollutant 跳过 + rules 标记，下周补 verification + README。交接报告预计下周中可以给。

3. 给他的 ADRMATS 侧建议：桥接模块先按 `BiomimeticContext.query()` 的现有签名写，后续不会改签名；enrichment 层已分离，重跑重建不会丢数据；`find_applicable_rules` 的输出需要标注为 `pending_validation`。
