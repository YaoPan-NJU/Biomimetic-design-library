# Session Handoff — 2026-06-15

## 当前状态

- **分支**: `opt/curation-grounding-v1`（已推送到 GitHub）
- **最新 commit**: `2d0889c`（docs: 更新README + 补齐交接文档）
- **Phase 进度**: Phase 0–6 全部完成，Phase 7 待开始

## Phase 0–6 完成摘要

| Phase | Commit | 内容 | 结果 |
|-------|--------|------|------|
| 0 | `9633aeb` | baseline snapshot | 31 prototypes, 864 mechanisms, 963 perf |
| 1 | `9633aeb` | 接口诚实度 P0 bug | 3处修复（verification_tier/空pollutant/brief key） |
| 2 | `9633aeb` | 策展落地 | PARK 1 + DEMOTE 4 + DEDUP 2 + ANTIFOULING 1 = 24 active |
| 3 | `48e2cf4` | chimera 全字段清理 | 30条删除（mechanism+perf+narrative+instances） |
| 4 | `48e2cf4` | 字段语义+诚实标注 | pollutant回填49 + causal_chain骨架528 + verification统一 |
| 5 | `0b49533` | 因果链补全 | 28张合格卡覆盖24原型，506空骨架已清 |
| 6 | `c7bee7f` | PDF核验 | 23 verified / 5 needs_review |

## Phase 6 最终结果

### 23 张 verified（源论文与原型一致）
mussel(PDA粘附+自聚+铀酰)、chitosan(pH+络合)、chlorella(程2021小球藻)、diatom(Guo2022硅藻土)、polydopamine(PDA catechol)、SRB(Kumar2021)、IOB(Luo2021施氏矿物)、bone(Bambaeero2021 HAp)、oyster(李2017)、scallop(Wang2024)、fish-scale(Balasooriya2022)、mangrove(刘2022)、mycelium(刘2021真菌菌丝)、wood(Mo2021)、silk-fibroin(Prasad2022 ×2)、dna-aptamer(Li2021)、biomineralization(Wang2025)、plant-tannin(Zhu2022)、cell-membrane(BerattoRamos2022)

### 5 张 needs_review（本地无对口文献）
coral-skeleton、magnetic-bacteria、pitcher-plant、lobster-exoskeleton、spider-silk

### literature-requests.md
5个待下载原型的7条检索式已写好

## 关键铁律（后续session必须遵守）

1. **严禁运行 build_prototypes_db.py** — 会冲掉 Phase 2-6 清理
2. **canon = prototypes_db/*.json** — 只在其上直接编辑
3. **DEFINITIONS.md 全程挂载** — 判定标准权威源
4. **宁可少而真，不可多而假**
5. **unverified/single_source 不得作为 active 终态**
6. **from_source 必须有 DOI/source_file，否则降 llm_inferred**

## 下一步：Phase 7（设计转译重做）

- 为每个 active 原型写 ≥1 条 design_translation
- 必须含三要素：specific_functional_group / material_handle / target_interaction
- 删除/改写所有套话
- 禁用泛词清单：良好的吸附性能、优异的、广泛的应用前景等

## 其他同事工作

- ADRMATS 集成：由同事负责，本库只需提供 BiomimeticContext.query() 接口
- 5篇文献下载：学生负责，按 literature-requests.md 检索词执行

## 关键文件位置

| 文件 | 用途 |
|------|------|
| `docs/DEFINITIONS.md` | 判定标准/字段schema（权威） |
| `docs/optimization-v1/PLAN.md` | 9阶段执行手册 |
| `docs/optimization-v1/交接文档_HANDOFF.md` | 复核角色交接 |
| `docs/optimization-v1/coverage-gaps.md` | 策展后缺口（Boron/Co(II)真缺口） |
| `docs/optimization-v1/literature-requests.md` | 5篇待下载文献检索词 |
| `tools/biomimetic_context.py` | ADRMATS 接口 |
| `tools/check_chimera.py` | chimera 检查（mechanism+perf+narrative+instances） |
| `tools/check_causal_chain.py` | 因果链合格率检查 |
| `prototypes_db/*.json` | canon（24 active + 4 materials_reference + 1 parked） |
