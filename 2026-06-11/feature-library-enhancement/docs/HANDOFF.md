# 项目交接说明（接手前必读 / READ FIRST）

> 适用项目：Biomimetic-design-library（生物原型知识库，ADRMATS 系统的仿生检索模块）
> 文档性质：本文件保留项目背景与历史状态；当前权威执行计划为仓库根目录 `下一步执行计划_本地AI.md`。
> 冲突裁决：当本文件与 `下一步执行计划_本地AI.md` 不一致时，**以 `下一步执行计划_本地AI.md` 为准**；目标与设计仍参考 `docs/superpowers/specs/2026-06-05-library-enhancement-design.md`（下称 spec）。
> 最后核对：2026-06-05（第三版，补充证据完整性核查结果）

> **2026-06-05 重要更新**：抽样核查已确认 5 个手工标杆的性能数据与部分引用不可信，不能继续作为"高质量标杆"使用。下一步不是扩写，而是按 `下一步执行计划_本地AI.md` 执行：先清理隔离编造内容，再建立 provenance 模板和双层校验，之后才用真实 PDF 重建标杆。

---

## 0. 给接手 AI 的第一条指令

先阅读仓库根目录 `下一步执行计划_本地AI.md`，再跑下面这一段核对真实状态。不要直接相信旧文档的进度数字。

```bash
# 切到唯一工作分支
git checkout feature/library-enhancement

# 核对原型对齐情况（真实状态，不看文档）
python - <<'PY'
import json, os
meta = set(json.load(open('feature-mapping.json', encoding='utf-8'))['prototype_metadata'].keys())
have = {n for n in os.listdir('prototypes') if os.path.exists(f'prototypes/{n}/prototype.md')}
empty = {n for n in os.listdir('prototypes') if os.path.isdir(f'prototypes/{n}') and not os.path.exists(f'prototypes/{n}/prototype.md')}
aligned = meta & have
print('canonical IDs (feature-mapping):', len(meta))
print('dirs with prototype.md      :', len(have))
print('  -> 已对齐(索引指向有内容)   :', len(aligned))
print('  -> 断链(索引指向空目录)     :', len(meta - have))
print('  -> 孤儿(有内容但索引不到)   :', sorted(have - meta))
PY

# 核对内容完成度：每个 prototype.md 还剩多少 [待补充]
grep -rc '待补充' prototypes/*/prototype.md | sort -t: -k2 -rn | head

# 核对流水线代码健康度
cd extraction && pip install -q -r requirements.txt && python -m pytest tests/ -q; cd ..
```

截至 2026-06-05 最新核对，远端 `feature/library-enhancement` 应看到：33 个 canonical ID、30 个有 `prototype.md` 的目录、23 个已对齐、10 个断链、7 个孤儿内容目录；多数空壳 `prototype.md` 仍有 10 到 11 个 `[待补充]`，5 个手工标杆虽无 `[待补充]` 但因证据污染需先清理。`extraction` 测试为 66 个通过。若数字不同，以实测结果为准并先回报。

> **注意**：Windows 环境下用 `python` 而不是 `python3`。`grep` 命令在 Windows 上需换用 `findstr` 或 Git Bash。

---

## 1. 当前真实状态（Ground Truth）

唯一工作分支是 `feature/library-enhancement`，它是其余分支的超集。`feature/biomimetic-story-v2` 与 `project/tracking` 指向同一旧 commit，`main` 更旧，三者都不要在上面继续开发。

### 1.1 spec 的 Phase 0（Foundation）

| Phase 0 任务 | 状态 |
|---|---|
| 创建 `principles/` 结构与模板 | 已完成 |
| 创建 `design-rules.json`（含 40 条规则） | 已完成，但规则是 LLM 草稿，未经文献验证（`validated_against_exemplars: false`） |
| 实现仿生提取流水线（`extraction/`，四阶段，32 测试） | 已完成 |
| **解决原型命名不一致** | **只做了映射表 `docs/prototype-id-mapping.md`，实际合并改名未执行** |

spec 的 Phase 1a / 1b / 2 / 3 / 4（规则生成、范例深化、交叉验证、批量深化、扩到 100）**全部未开始**。

### 1.2 提取流水线验证进展（2026-06-05 新增）

以下工作已在本轮会话中完成并提交（commit `9cea0ab`）：

| 任务 | 状态 | 说明 |
|---|---|---|
| API 配置与连通性验证 | 已完成 | 3 个 provider（Coding Plan/DashScope/MiMo）全部连通，round-robin 负载均衡 |
| Phase 1 粗扫（流水线内部） | 已完成 | 149/149 论文扫描成功，30 个 coarse profile 生成，耗时 398s，0 错误 |
| Phase 4 深度提取小批量验证 | 已完成 | 3 个 exemplar（chitosan-adsorbent, mussel-foot-adhesion, mof-adsorbent），首次跑暴露 6 个 bug，修复后重跑验证通过 |
| writer.py 六项核心 bug 修复 | 已完成 | features/mechanisms 分离、pollutants 聚合、qmax 单位去重、routing 元数据读取、evidence_level 动态计算、覆写保护 |
| phase4_deep_extract.py 数据通路修复 | 已完成 | routing lookup（ID 映射 + 模糊匹配）、target_pollutants 聚合、evidence_level 聚合、coarse_coverage 传递 |
| 仿生设计方法论补充检索策略 | 已完成 | 4 个缺口领域、61 条检索词（WoS/CNKI/Google Scholar），目标补充 80-120 篇文献 |
| 本地文献库清点 | 已完成 | `C:\Users\15995\Desktop\仿生文献库`：341 文件（302 论文 + 33 专利 + 6 标准），8 组 + 全局综述 |

### 1.3 流水线修复后的残留问题

| 问题 | 严重度 | 说明 |
|---|---|---|
| Narrative 5.1-5.5 全空 | 中 | Phase 2/3（gap analysis + supplementation）未跑，无补充论文；跑完全链路后可解 |
| Structural features 部分为空 | 低 | LLM 对某些论文未返回 material_characterization，可通过增加论文数/字数上限缓解 |
| validators.py qmax schema 不匹配 | 低 | 期望标量 float，Phase 4 返回 dict；需更新 validators 但不影响功能 |
| qmax_range YAML 仍有残余单位 | 低 | "186.6 mg P/g" 中 "mg P/g" 未被完全剥离（body text 已正确）；需扩展正则 |
| 流水线 ID vs canonical ID 不一致 | 中 | 如 chitosan-adsorbent vs chitosan；routing lookup 已做兼容，但根本解是步骤 1 的 ID 重对齐 |

### 1.4 手工标杆文件（需先清理）

以下 5 个 prototype.md 是手工策划的大文件（>28KB），流水线覆写保护会避免直接覆盖它们：

- `prototypes/chitosan/prototype.md`
- `prototypes/lotus-leaf/prototype.md`
- `prototypes/metal-organic-framework/prototype.md`
- `prototypes/mussel-foot-adhesion/prototype.md`
- `prototypes/sulfate-reducing-bacteria/prototype.md`

内容层最新判断：这 5 个手工标杆不能再视为达到质量基线。`mussel-foot-adhesion` 抽样核查已确认性能数据与部分引用存在编造/错引；其余 4 个同一流程产出，默认不可信，必须先按 `下一步执行计划_本地AI.md` 任务 1 清理。25 个左右空壳虽未完成，但比带未核实数值引用的标杆更安全。

---

## 2. 术语消歧（极易混淆，务必先看）

项目里有两套各自的"Phase 1 到 4"，含义完全不同，接手 AI 必须分清：

- **流水线 Phase（提取工具内部阶段）**：粗扫 → 差距分析 → 补充计划 → 深度提取，对应 `extraction/pipeline/phase1..4`。已在 2026-06-04 跑过一轮（仅摘要），产出空壳；2026-06-05 在修复后重新跑了 Phase 1 + Phase 4 小批量验证。
- **spec Phase（项目实施阶段）**：Phase 0 基础 → 1a 规则生成 → 1b 范例深化 → 2 交叉验证 → 3 批量深化 → 4 扩到 100。除 Phase 0 部分完成外，其余未动。

本文件下面所说的"步骤"是旧版执行顺序。当前执行顺序以 `下一步执行计划_本地AI.md` 的任务 1 到任务 7 为准。

---

## 3. 目标（来自 spec，权威）

最终形态是约 100 个达到质量基线的原型，外加经验证的设计规则，作为 ADRMATS 多智能体系统的仿生检索模块。

**单个原型的质量基线（spec 1.2，即"填充完成"的判定标准）**：

- 仿生叙事 5.1 到 5.5：至少 3 个子节有实质内容
- 定量性能：至少 3 种污染物有 qmax 或去除率数值
- 机制分析：至少 2 个机制写全（现象、分子基础、官能团、仿生启示）
- 结构特征：宏观/介观/微观/纳米四个尺度至少描述 2 个
- 工程约束：11 项里至少评估 5 项并给出解释

**边界（spec 1.3，不要越界）**：库只做匹配检索，不做推理与组合（约束识别归 ADRMATS 的 AdaptiveConstrainingAgent，组合推理归对抗设计引擎）；库不替代 LLM 领域知识，只补充其不一定可靠记得的、有证据支撑的规则。

---

## 4. 执行顺序（按此推进，前序步骤未过不许进入下一步）

本节保留旧版执行顺序供追溯。当前优先级已调整为：清理 5 个手工标杆的证据污染 → 建 provenance 模板与双层校验 → ID 对齐和残留 bug 修复 → 用真实 PDF 重建 5 个标杆 → 批量深化 → 核查规则 → 扩到 100。具体验收标准以 `下一步执行计划_本地AI.md` 为准。

### 步骤 1【硬门槛】执行 ID 重对齐

照 `docs/prototype-id-mapping.md` 的对账表执行实际文件操作：孤儿内容目录按表合并/改名进 canonical 目录，删掉空 `.gitkeep` 占位目录，必要时为新增 5 个原型建 canonical 目录。
- 验收：步骤 0 的核对脚本里"断链"为 0、"孤儿"为空，且 `feature-mapping.json` 引用的每个 ID 都有非空 `prototype.md`。

### 步骤 2【硬门槛】修 `extraction/writer.py` — **已完成**

接入 `extraction/config/prototype_routing.json` 填 name/category/biomimetic_dimension，把 `features` 与 `adsorption_mechanisms` 拆成两个不同字段，pollutants 从 coarse coverage + LLM 结果合并填充，qmax 单位去重，覆写保护（>5KB 文件不覆盖）。

- 验收：随便重生成一个原型，frontmatter 的 name 不再是 naive title-case、category 是 taxonomy 四类之一（植物/动物/微生物/仿生材料）、features ≠ mechanisms、pollutants 非空。**已通过 3 个 exemplar 小批量验证。**

仍可改进（非硬门槛）：`vocabulary_mapping.json` 特征标准化接入、pollutants 归一到 `taxonomy/pollutants.md` 标准名、validators.py 的 qmax schema 更新。

### 步骤 3 建立一致性校验脚本（同时是隐患 R1 的处置，见第 5 节）

新建 `tools/validate_consistency.py`，校验四条不变量，接进 pre-commit 或 CI，此后每次改动都跑。
- 验收：脚本能检出断链、孤儿、`feature-mapping.json` 与 `prototype_routing.json` 的 ID 集合差异、frontmatter 缺字段，返回非零即阻断提交。

### 步骤 4 全文补充 + 重跑流水线，把现有原型填到基线

按已生成的 336 条检索词（`extraction/extraction-output/gap-analysis/search-queries.md`）下载全文文献到 `supplemented-papers/<id>/`，放宽 `phase4_deep_extract.py` 的全文字数与篇数上限（当前只取前 5 篇前 8000 字），重跑流水线 Phase 2→3→4 全链路。先做 spec 的 5 个 exemplar（mussel-foot-adhesion、lotus-leaf、metal-organic-framework、sulfate-reducing-bacteria、chitosan），再铺开其余。

**重要**：Phase 1 粗扫产物（30 个 coarse profile JSON）已在 `extraction/extraction-output/coarse-profiles/` 下，可直接从 Phase 2 开始。

- 验收：质量检查脚本（按第 3 节基线判定）对 5 个 exemplar 全部通过，再扩到其余 33 个。

### 步骤 5 扩到 100（spec 第 5 节，Phase 4）

按 spec 阶段二（34 到 60，补薄弱仿生维度，候选已点名：壁虎黏附、藤壶水泥、乌贼喙、鲍鱼壳珍珠层、生物膜、群体感应菌、嗜极古菌、竹维管束等）与阶段三（61 到 100，规则空白驱动）逐个新增。每新增一个原型，走第 6 节的标准动作。

**补充检索**：当前文献库偏"材料→应用"视角，缺少"生物→设计→材料"视角。已准备补充检索策略文档（61 条检索词），涵盖仿生设计方法论、设计原则/标准、跨原型比较研究、设计案例研究 4 个缺口领域。

- 验收：原型目录数约 100，每个都过质量基线与一致性校验。

### 并行轨：验证规则

`design-rules.json` 的 40 条规则目前是 LLM 草稿。随 exemplar 深化做交叉验证（spec 2.2），把通过验证的规则标记 `validated_against_exemplars: true`。**未验证的规则不得喂给匹配层使用**。

---

## 5. 隐患处置（Risk Register）

三个隐患现在不痛，到规模会痛，逐一转成有人盯的护栏：

**R1 三份配置漂移（最高优先）。** 每加一个原型，`prototype_routing.json`、`feature-mapping.json`、必要时 taxonomy 必须同步改，现无校验保证一致，现有 33 个已漂移成 51 个目录的乱象。处置：步骤 3 的 `validate_consistency.py` 作为硬门槛，每次改动后必跑；不变量包括：①`feature-mapping.json` 的每个 ID 有非空 `prototype.md`；②无孤儿内容目录；③`feature-mapping.json` 与 `prototype_routing.json` 的 ID 集合一致；④每个 `prototype.md` frontmatter 字段齐全。

**R2 关键词路由在规模下撞车。** 鲍鱼壳/牡蛎壳/扇贝壳同带"壳"，多种丝、多种菌同理，关键词匹配（match_threshold、每篇最多 3 个）误路由会随原型数上升。处置：先给路由加相关性评分阈值并对模糊命中输出待人工复核清单（不要贪婪自动分配）；原型数超过约 60 之前，按 spec 说的把关键词路由升级为语义匹配。

**R3 间接映射贪婪分配产生噪音。** 看板 TODO-004 已记录 dna-aptamer 与 magnetic-bacteria 论文完全重叠的误配。处置：在 `extraction/prototype_mapper.py` 加论文与原型的相关性评分阈值，低于阈值不映射。R2 与 R3 共用这一处修复。

**R4 LLM 草稿规则未经验证。** 直接用有引入未核实结论的风险。处置：见第 4 节并行轨，验证前不投入匹配，引用文献逐条核实（现 references 多标"require verification"）。

**R5 流水线覆写手工文件（已缓解）。** 此前 writer.py 无覆写保护，曾导致 mussel-foot-adhesion 28KB 手工文件被 2.3KB 骨架覆盖（已 git 恢复）。commit `9cea0ab` 新增覆写保护：>5KB 的 prototype.md 不会被覆盖，pipeline 输出改为 `.pipeline` 后缀。后续仍需注意检查此保护是否生效。

---

## 6. 每加一个原型的标准动作（防止漂移复发）

为保证扩到 100 时不再失配，新增原型固定走这套：

1. 在 `feature-mapping.json#prototype_metadata` 加 ID 与 applicability，并在相关 `pollutant_prototype_map`/`feature_prototype_map` 加权重条目。
2. 在 `prototype_routing.json` 加同名 ID 的中英文路由关键词。
3. 若涉及新类别/新污染物/新机制，先在 `taxonomy/*.md` 登记。
4. 建 `prototypes/<id>/` 并经流水线或人工产出达基线的 `prototype.md`。
5. 跑 `validate_consistency.py`，通过方可提交。

ID 命名沿用 README 规范：英文小写加连字符，偏好更通用的短名（`chitosan` 而非 `chitosan-adsorbent`），仅当确为不同概念才并存（如 `diatom-frustule` 与 `diatom-microspheres`）。

---

## 7. 完成的定义（Definition of Done）

- 单原型：满足第 3 节质量基线。
- 整体（spec 第 8 节指标）：原型约 100；规则 80 到 120 条 CM + 30 到 50 条原则，平均置信度 > 0.8；100% 原型过基线（自动检查脚本）；每个 exemplar ≥ 15 篇文献、其余 ≥ 5 篇；> 80% 规则有至少 1 个 exemplar 验证；ADRMATS 端到端能消费 BiomimeticContext。

---

## 8. 不要做的事（Invariants）

- 不要在还有 `[待补充]`（尤其叙事 5.1 到 5.5）时声称某原型完成。
- 不要只改一份配置就加原型，三份必须同步（见第 6 节）。
- 不要把未验证的 LLM 草稿规则喂给匹配层。
- 不要混淆"流水线 Phase"与"spec Phase"（见第 2 节）。
- 不要在 `main`、`biomimetic-story-v2`、`project/tracking` 上开发；只用 `feature/library-enhancement`。
- 不要相信旧文档的进度数字，以第 0 节核对脚本的实际输出为准。
- 不要让流水线覆盖已有的高质量 prototype.md（>5KB 文件受保护，但需确认）。

---

## 9. 关联项目与外部依赖

### 关联仓库

| 项目 | 地址 | 关系 |
|---|---|---|
| ADRMATS | `github.com/Water-Quality-Risk-Control-Engineering/ADRMATS` | 上游消费者：本库作为其仿生检索模块 |
| Literature-extracting (LitExtract) | `github.com/YaoPan-NJU/Literature-extracting` | 同级工具：生产级批量提取系统，本库 extraction/ 是小批量验证版 |

### API Provider 配置

提取流水线使用 3 个 LLM provider round-robin 负载均衡：

| Provider | Model | 用途 |
|---|---|---|
| Alibaba Coding Plan | qwen3.6-plus | 通用提取 |
| Alibaba DashScope | qwen3.7-max | 高质量提取 |
| Xiaomi MiMo | mimo-v2.5 | 补充提取 |

配置方式：`extraction/.env` 文件（不入 git），字段见 `extraction/config.py`。

### 本地文献库

- 路径：`C:\Users\15995\Desktop\仿生文献库`
- 内容：341 文件（302 论文 + 33 专利 + 6 标准）
- 分组：8 组论文（每组 33-38 篇）+ 20 篇全局综述
- 不在 git 中，需本地存在才能跑流水线

---

## 10. 给接手 AI 的开场提示词（可直接复制）

```
你将接手 Biomimetic-design-library 项目。请先读仓库根目录的 `下一步执行计划_本地AI.md`，它是当前权威行动指南；背景再读 `docs/HANDOFF.md`。两者冲突时以 `下一步执行计划_本地AI.md` 为准。

关联仓库：
- ADRMATS: github.com/Water-Quality-Risk-Control-Engineering/ADRMATS（上游消费者）
- LitExtract: github.com/YaoPan-NJU/Literature-extracting（生产级批量提取）

开始前，按 `下一步执行计划_本地AI.md` 第 0 节的脚本自行核对当前真实状态（不要相信旧文档里的进度描述），把核对结果（断链/孤儿/待补充数量、测试是否通过、本地文献库路径）回报给我确认。

确认后，从 `下一步执行计划_本地AI.md` 的任务 1 开始：先清理 5 个手工标杆的编造内容，再做 provenance 模板和双层校验脚本。前序未过验收不进下一步。

唯一工作分支是 feature/library-enhancement。
```
