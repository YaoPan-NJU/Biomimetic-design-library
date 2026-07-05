# BMDL Stage 7 Handoff for ADRMATS Integration

**日期：** 2026-07-05
**状态：** Release Candidate 冻结，待 Axl 审阅接入

---

## 一、仓库信息

| 项 | 值 |
|---|---|
| BMDL repo | `/Users/panyao/Desktop/Biomimetic-design-library` |
| 远端 | `origin/review` (GitHub: YaoPan-NJU/Biomimetic-design-library) |
| BMDL latest commit | `60cb899` (stage7 audit-fix) |
| BMDL release export commit | `4f420f5` (stage7: promote stage5 match weights to RC) |
| ADRMATS repo | `/Users/panyao/Documents/ADRMATS` |
| ADRMATS commit | `5cb5902` (fix: allow BMDL schema selection via BMDL_SCHEMA) |

## 二、本轮 BMDL 改了什么

### a. MOF/CNC 等 quarantined 隔离

- `metal-organic-framework` → `quarantined/`（organism.scientific 误填 "Bombyx mori"，实际是合成材料）
- `diatom-inspired-porous` → `quarantined/`（已废弃，合并至 diatom-frustule）
- `silkworm-silk` → `quarantined/`（已废弃，合并至 silk-fibroin）
- `cellulose-nanocrystal` → `quarantined/`（降级为 material_realization_examples）
- 原有 4 个 quarantined 保持不变（algae-polysaccharide, bacterial-surfactant, microbial-biomineralization, plant-gum）
- **Primary 集：48 → 40 个原型**（8 个 quarantined）

### b. source_category='primary' 查询过滤契约

- `src/adapters/bmdl_repository.py` L344: 将 Axl 失效的 `ILIKE '%metal-organic%'/'%mof%'` 替换为 `source_category='primary'`
- ETL 按文件目录派生 `source_category`：顶层 → primary，quarantined/ → quarantined
- 验证：MOF 不在 query_candidates 结果中

### c. ETL --schema、幂等 DELETE、安全锁

- `scripts/import_bmdl_to_rds.py` 加 `--schema` 参数（默认 bmdl，支持 bmdl_staging）
- 非 staging schema 禁止 `--drop`（安全锁）
- 导入前清空目标 schema 所有表（幂等 DELETE，防止重复导入）
- 连续两次导入验证 count 稳定（1020 performance_data）

### d. 少量 AC/BC high-confidence capacity 补强

- Batch 1: 3 条 PFOA/BPA capacity（Vitis vinifera AC + pine-fruit shell hydrochar），写入 `plant-lignocellulosic-architecture`
- Batch 2: 4 条 BPA capacity（corn straw biochar + sycamore leaf hydrochar + lignin biochar + β-CD rice husk biochar），写入 `plant-lignocellulosic-architecture`
- Batch 3: 4 条 BPA/PFOA capacity（coconut husk biochar + lignin biochar + eucalyptus biochar + wheat straw biochar）
- Batch 4: 8 条 chitosan/alginate capacity（去集中化补强，写入 chitosan/alginate）
- PDF promotion audit: 1 条 promoted (ALG-P71 PFOA/alginate page 1 verified), 3 条 moved to side evidence (综述/qmax未确认)
- **当前 AC+BC = 36/499 = 7.2%**（目标 15%，高质量证据已耗尽）

### e. match_weights 132 rows release candidate

- Baseline: 130 rows → Release candidate: 132 rows (+2 plant-lignocellulosic PFOA/BPA)
- `adrmats_export/match_export.json` = release candidate (SHA256[:16] = `4bdbd34c5a3921bd`)
- `adrmats_export/match_weights.csv` = 132 data rows
- Baseline backup: `docs/bmdl_rebalance/stage7_match_export_baseline_20260705.json` (SHA256[:16] = `4c5ab4773e1d70e8`)

### f. 权重规则

- exploratory_no_source_evidence → cap ≤0.3
- non-direct lead → cap ≤0.5（bone-structure/oyster-shell 逐条评估）
- direct evidence / fact lane → 保留原权重
- PDA/mussel 重叠污染物：PDA cap 0.3，mussel 保留
- **Top-5 concentration: ~70% → 61.8%**

### g. BPA/PFOA 新增 plant-lignocellulosic direct evidence

- PFOA: weight=0.6, direct=True, basis=direct_source_evidence (Stage 4 PDF-verified capacity)
- BPA: weight=0.65, direct=True, basis=direct_source_evidence (Stage 4 PDF-verified capacity)
- Query regression: BPA/PFOA 的 #1 候选是 plant-lignocellulosic-architecture (direct)，不再是 exploratory

## 三、当前验证结果

| 验证项 | 结果 |
|---|---|
| `tools/validate_consistency.py` | 0 errors ✅ |
| match_export.json rows | 132 ✅ |
| match_weights.csv data rows | 132 ✅ |
| quarantined in match_weights | 0 ✅ |
| exploratory weight > 0.3 | 0 ✅ |
| non-direct weight > 0.5 | 0 ✅ |
| BPA/PFOA plant-lignocellulosic direct #1 | ✅ |
| BMDL_SCHEMA env var (ADRMATS) | 5/5 ad-hoc ✅ |

## 四、Axl 接入步骤

1. **拉取 BMDL review**:
   ```bash
   cd /path/to/Biomimetic-design-library
   git fetch origin
   git checkout review
   git pull origin review  # HEAD = 60cb899
   ```

2. **审阅导出文件**:
   - `adrmats_export/match_export.json` (132 rows, stage=7_release_candidate)
   - `adrmats_export/match_weights.csv` (132 data rows)
   - `docs/bmdl_rebalance/stage7_*.md` (6 份审计文档)

3. **ADRMATS 使用 BMDL_SCHEMA 指向 staging/candidate schema 做 E2E**:
   ```bash
   # ADRMATS 已有 BMDL_SCHEMA 环境变量支持 (commit 5cb5902)
   # 导入 release candidate 到 staging
   cd /path/to/ADRMATS
   python scripts/import_bmdl_to_rds.py --schema bmdl_staging --drop \
     --source /path/to/Biomimetic-design-library
   
   # 设置环境变量
   export BMDL_SCHEMA=bmdl_staging
   
   # 重启 ADRMATS
   ```

4. **必跑 smoke tests**:
   - BPA 设计流程 → 确认 plant-lignocellulosic-architecture direct #1
   - PFOA 设计流程 → 确认 plant-lignocellulosic-architecture direct #1
   - PFOS → 确认无 direct evidence（严格分桶，所有 exploratory ≤0.3）
   - Cd(II) → 确认 chitosan evidence-based 高排
   - Pb(II) → 确认多原型竞争
   - Cr(VI) → 确认 bone/oyster 降权
   - PO43- → 确认 oyster-shell direct 保留
   - **医院废水 fallback** → 确认不误导航成生活污水（`_get_relevant_water_data` 三种场景）

5. **E2E 通过后按 cutover runbook 切 production**:
   - 参考 `docs/bmdl_rebalance/stage7_cutover_runbook.md`
   - 推荐方案：环境变量切换（零 drop production）
   - 需潘老师明确授权

## 五、已知保留风险

| 风险 | 严重性 | 说明 |
|---|---|---|
| PFOS 无 direct evidence | 低 | 严格分桶 PFOS≠PFOA，正确行为。后续可补充 |
| AC+BC 7.2% 未达 15% | 中 | 高质量证据已耗尽（PKB/污染物文献/仿生文献/litextract 全量搜索），接受为 Stage 4 最终值 |
| chitosan 占比 21.8% | 中 | evidence-based (12 条 lead+direct, 102 条 performance_data)，不做机械迁移 |
| production bmdl schema 尚未切换 | - | 待 Axl E2E + 潘老师授权后执行 |

## 六、文档索引

| 文档 | 路径 |
|------|------|
| Stage 7 release candidate report | `docs/bmdl_rebalance/stage7_release_candidate_report.md` |
| Stage 7 candidate import report | `docs/bmdl_rebalance/stage7_candidate_import_report.md` |
| Stage 7 regression report | `docs/bmdl_rebalance/stage7_regression_report.md` |
| Stage 7 cutover runbook | `docs/bmdl_rebalance/stage7_cutover_runbook.md` |
| Stage 7 rollback plan | `docs/bmdl_rebalance/stage7_rollback_plan.md` |
| Stage 7 final go/no-go | `docs/bmdl_rebalance/stage7_final_go_no_go.md` |
| Stage 5 formal rules | `docs/bmdl_rebalance/stage5_formal_rules.md` |
| Stage 5 risk resolution | `docs/bmdl_rebalance/stage5_risk_resolution_report.md` |
| Stage 4.5 exhaustion report | `docs/bmdl_rebalance/stage5_readiness_audit.md` |
| Baseline backup | `docs/bmdl_rebalance/stage7_match_export_baseline_20260705.json` |
| git tag | `bmdl-pre-rebalance-20260704` |
