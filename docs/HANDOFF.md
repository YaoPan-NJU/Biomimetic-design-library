# HANDOFF — 换设备续工作入口

> 最后更新：2026-06-08 12:30
> 当前分支：`feature/extraction-results`
> 最新 commit：`2736a3a` (docs: 更新 HANDOFF.md + README.md - MOF 验证完成)

---

## 项目目标（一句话）

本库是**仿生设计智能体的检索基座**，产物是 **brief**（不是材料）。详见 [design.md 第 0 节](design.md#0-库的定位北极星)。

**ADRMATS 集成**：分层检索策略（direct evidence + feature-based retrieval）详见 [ADRMATS_INTEGRATION.md](ADRMATS_INTEGRATION.md)。

## 当前进度（实测数据 2026-06-08 10:00）

| 指标 | 数值 | 说明 |
|------|------|------|
| prototypes_db 文件数 | 31 | active=23, needs_literature=8 |
| 性能数据总数 | 752 | verified=0, needs_review=16, unverified=736 |
| 缺 pollutant 的性能数据 | 191 | 无法按污染物匹配 |
| 机制总数 | 723 | 缺 active_features=602 |
| Chimera 违规 | 1 | polydopamine-coating 含不相关关键词 |
| 校验错误 | 2 | 断链 5 个原型 + separation 目录不存在 |
| 校验警告 | 190 | 主要是 R14 机制含实例级数据 |

**当前状态**：数据地基扎实（311 个提取 JSON 有接地），但 prototype.md 和 feature-mapping 尚不能交给 ADRMATS 使用。**verified=0**，任何"已 verified / 验证完成"的表述均与实测不符。

## 已定关键决定

1. **质量七条准则**：质量为上、可溯源、单一身份、unverified 不当事实、空白优于错配、有引用不等于可信、拿不准就问
2. **Gating 1**：超疏水/分离簇停放 `separation/`，标 `parked_separation`，从吸附匹配排除
3. **Gating 2**：PDA 与 mussel 分立，加 `inspired_by` / `material_realization` 互链，去重
4. **Gating 3**：核查用混合策略，verification 五级（verified/corroborated/single_source/unverified/needs_review）
5. **Brief 中心**：库的交付单元是 brief 三件套（match + mechanism + design_translation），不是材料
6. **Schema 冻结**：仅允许任务布置第 2 节的小幅增补（基本原理、design_translation、verification_tier、source_tier）
7. **分层核查**：定性归属必须接地（Path A）；定量性能只需诚实分级（Path B）；身份必须单一（Path C）；LLM 外推标 llm_inference（Path D）

## 当前在用计划（v1.1，最高优先级）

**执行入口**：`任务布置_brief中心_交本地AI执行.md`（v1.1）
**配合规格**：`分层核查标准_交本地AI执行.md`（v1.1）+ `金标准闭环_启发质量评分卡.md`（v1.1）

三份文档关系：
- 任务布置 = 流程主干（Phase 0→4）
- 分层核查标准 = 每条数据怎么判（Path A/B/C/D/**E**）
- 评分卡 = brief 合不合格（D1-D8）

**v1.1 新增**：
- Path E：污染物画像与匹配依据核查
- 新污染物匹配原则：pollutant_prototype_map 只作为 direct evidence 层，不能作为唯一入口
- brief 结构新增 pollutant_profile、match_basis、molecular_feature_links
- 分层检索策略详见 [ADRMATS_INTEGRATION.md](ADRMATS_INTEGRATION.md)

**若旧文档（README、HANDOFF、SESSION-CONTEXT、旧优化方案、旧审计报告）与这三份 v1.1 文档冲突，以 v1.1 为准。**

## 下一步任务（按任务布置 v1.1 Phase 0→3）

### Phase 0 — 定位与状态对齐 ✅ 完成
- [x] 把定位 + brief 结构写进 design.md（含 v1.1 新增 pollutant_profile）
- [x] 新建 docs/ADRMATS_INTEGRATION.md（分层检索策略）
- [x] README / HANDOFF 同步指向 design.md + ADRMATS_INTEGRATION.md
- [x] 冻结 schema（design.md 第 0.1 节）
- [x] 状态文档对齐（HANDOFF.md 已更新为实测数据）

### Phase 1 — brief 三件套就绪 ✅ 金标准完成
- [x] 1a 身份纯净（Path C）：五个金标准均无 chimera 问题
- [x] 1b 机制接地 + 基本原理（Path A）：五个金标准共 341/394 条机制有基本原理（86.5%）
- [x] 1c 设计转译（Path D）：五个金标准均有 design_mapping
- [x] 1d 污染物画像（Path E）：生成了 direct evidence 和 feature-based 查询的 pollutant_profile

### Phase 2 — 诚实标注 + 接口契约 ✅ 完成
- [x] 2a 性能分级（Path B）：752 条性能数据按五级打标签（verified=0, single_source=236, unverified=500, needs_review=16）
- [x] 2b 分层匹配层补齐：6 个原型补进 pollutant_prototype_map；保留为 direct evidence 层
- [x] 2c 接口契约：实现 BiomimeticContext（tools/biomimetic_context.py）

### Phase 3 — 金标准 brief 闭环 ✅ 关口通过
- [x] 选 5 个高价值吸附原型作金标准：MOF, Chitosan, Alginate, CNC, Starch
- [x] 按评分卡 D1-D8 打分：10 个测试用例全部通过（5 direct + 5 feature-based）
- [x] 5 个金标准全部通过 → 可进 Phase 4
- 详细报告：five_gold_standards_evaluation.md

### Phase 4 — 扩库 ✅ 完成
- [x] 对 18 个剩余 active 原型按 Phase 1 三件套验收
- [x] 批量补充基本原理（73 条已更新，158 条 needs_review）
- [x] 分类结果：
  - 能出 brief (active): 8 个（bone-structure, chlorella-cell-wall, diatom-frustule, lobster-exoskeleton, mycelium, oyster-shell, silk-fibroin, wood-xylem）
  - 低覆盖 (low_coverage): 5 个（cell-membrane-ion-channel, fish-scale-hydroxyapatite, mangrove-root, pitcher-plant-slippery-surface, polydopamine-coating）
  - 需补文献 (needs_literature): 5 个（coral-skeleton, magnetic-bacteria, namib-beetle, plant-tannin, sulfate-reducing-bacteria）

**最终状态**：
- 能出 brief 的原型总计：13 个（5 金标准 + 8 个新验收）
- 低覆盖原型：5 个（标 low_coverage，不进 active）
- 需补文献原型：5 个（标 needs_literature，不进 active）

## 关键文件位置

| 文件 | 用途 |
|------|------|
| `docs/design.md` | 库的定位 + brief 结构（北极星）|
| `docs/ADRMATS_INTEGRATION.md` | ADRMATS 集成 + 分层检索策略|
| `任务布置_brief中心_交本地AI执行.md` | 执行入口 v1.1（Phase 0→4）|
| `分层核查标准_交本地AI执行.md` | 每条数据怎么判 v1.1（Path A/B/C/D/E）|
| `金标准闭环_启发质量评分卡.md` | brief 合不合格 v1.1（D1-D8）|
| `tools/validate_consistency.py` | 校验脚本（14 条规则）|
| `tools/check_chimera.py` | chimera 检测 |
| `tools/build_prototypes_db.py` | 构建正典 |
| `tools/biomimetic_context.py` | BiomimeticContext 接口（Phase 2 产出）|
| `prototypes_db/` | 正典数据（31 个 JSON）|
| `feature-mapping.json` | 四层映射 |

## 怎么续上

1. Phase 0-4 + Phase 2 已完成
2. 13 个原型能出 brief（5 金标准 + 8 个新验收）
3. BiomimeticContext 接口已实现（tools/biomimetic_context.py）
4. 下一步：
   - 补充更多污染物的分子特征画像
   - 优化 feature-based retrieval 的匹配规则
   - 对剩余原型进行 Phase 1 验收

## 已知问题（实测 2026-06-08 12:00）

- **verified=0**（任何"已 verified / 验证完成"的表述均与实测不符）
- **752 条性能数据**：verified=0, needs_review=16, unverified=736
- **191 条性能数据缺 pollutant**（无法按污染物匹配）
- **723 条机制**：缺 active_features=602；已补充基本原理（341+73=414 条）
- **1 个 chimera 违规**（polydopamine-coating 含不相关关键词 "Stenocara"）
- **5 个断链原型**（cactus-spine, lotus-leaf, shark-skin, superhydrophobic-artificial, water-strider-leg）
- **5 个低覆盖原型**（cell-membrane-ion-channel, fish-scale-hydroxyapatite, mangrove-root, pitcher-plant-slippery-surface, polydopamine-coating）
- **5 个需补文献原型**（coral-skeleton, magnetic-bacteria, namib-beetle, plant-tannin, sulfate-reducing-bacteria）
- **8 个 needs_literature 原型**（无数据）
- **190 个校验警告**（主要是 R14 机制含实例级数据）
- **2 个校验错误**（断链 5 个原型 + separation 目录不存在）

## Phase 3 关口通过 ✅

五个金标准全部通过（10 个测试用例，通过率 100%）：
- direct evidence 查询：86.1% (42.6/49.5)
- feature-based inspiration 查询：79.0% (39.1/49.5)

## Phase 4 扩库完成 ✅

13 个原型能出 brief（5 金标准 + 8 个新验收）：
- bone-structure, chlorella-cell-wall, diatom-frustule, lobster-exoskeleton
- mycelium, oyster-shell, silk-fibroin, wood-xylem
- + 5 个金标准（MOF, Chitosan, Alginate, CNC, Starch）

5 个低覆盖原型（标 low_coverage）：
- cell-membrane-ion-channel, fish-scale-hydroxyapatite, mangrove-root
- pitcher-plant-slippery-surface, polydopamine-coating

5 个需补文献原型（标 needs_literature）：
- coral-skeleton, magnetic-bacteria, namib-beetle, plant-tannin, sulfate-reducing-bacteria

下一步：Phase 2（诚实标注 + 接口契约）

## 最新规格文档（2026-06-08 · v1.1 · 最高优先级）

- `任务布置_brief中心_交本地AI执行.md` — 执行入口 v1.1，Phase 0→4，含新污染物匹配原则
- `分层核查标准_交本地AI执行.md` — Path A/B/C/D/**E** 五条核查路径 v1.1
- `金标准闭环_启发质量评分卡.md` — D1-D8 八维评分 v1.1，含 pollutant_profile 要求
- `docs/ADRMATS_INTEGRATION.md` — ADRMATS 集成分层检索策略（Phase 0 产出）
- `five_gold_standards_evaluation.md` — 五个金标准完整评估报告（Phase 3 产出）

## 最近 Changelog

- `2736a3a` docs: 更新 HANDOFF.md + README.md - MOF 验证完成
- `9495f3a` feat: MOF 金标准验证 - pollutant 补全 + verification 状态更新
- `cc1b89d` docs: 更新 HANDOFF.md - MOF 核查脚本完成
- `58a29f6` feat: Step 5 - 金标准核查脚本 + MOF 核查报告
- `a42ab53` docs: 更新 HANDOFF.md - mussel 无数据，改用 MOF 作为金标准
