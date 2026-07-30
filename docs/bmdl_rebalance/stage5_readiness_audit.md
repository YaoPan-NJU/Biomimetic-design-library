# Stage 4.5 Exhaustion Report + Stage 5 Readiness Audit

**日期：** 2026-07-05
**状态：** 高质量证据已耗尽，建议进入 Stage 5

---

## 一、Exhaustion Report

### 搜索路径总结

| 路径 | 搜索范围 | 候选数 | high_confidence | 原因 |
|------|---------|--------|-----------------|------|
| PKB adsorption_performance_flat.jsonl | 2347 条 | 38 biochar+qmax | 0 | 大量 pollutant-parameter 错配；PDF 找不到或 qmax 不同页 |
| 污染物文献库（BPA 1416篇 + PFOA 275篇 + 其他） | 全量 pdftotext | 17 BPA+biochar+qmax | 4 (已写入 Batch 1-3) | 多数是综述引用/非直接实验/非 BPA 主题 |
| 仿生文献库（643篇） | 188 候选索引 | 12 非综述 BPA/PFOA/有机 | 0 | qmax 在表格图片中，pdftotext + 多模态均无法提取 |
| litextract extractions（558文件） | 全量递归搜索 | 183 AC/BC+qmax | 0 | 字段不规整（缺 pollutant/material/DOI） |
| materials_reference（4文件） | 4 条 AC/BC | 0 | 0 | 无 qmax_mg_g 字段 |

### 每条路径耗尽原因

1. **PKB**：20 条 biochar+qmax 中 10 条 pollutant-parameter 错配（如 BPA 标了 Cr(VI)/caffeine/雌三醇），剩余 10 条 PDF 找不到或 qmax 在 PDF 中不匹配
2. **污染物文献库**：BPA 目录找到 17 篇含 biochar+BPA+qmax，但多数是综述引用或非直接实验数据；PFOA 目录仅 2 篇 biochar+PFOA+qmax
3. **仿生文献库**：188 个候选文件，12 个非综述 BPA/PFOA/有机候选，但 qmax 全在表格图片中——pdftotext 提取不到表格数值，多模态视觉精读也未能正确提取（Liao 2022 读了 4 个 data page 但 0 条结果）
4. **litextract extractions**：183 条 AC/BC+qmax 但字段名不统一，缺 pollutant/material/DOI，无法直接使用
5. **materials_reference**：4 条 AC/BC 但无 qmax_mg_g 数值字段

### 结论

**高质量 capacity 证据已耗尽**。当前无法通过既有数据源继续补充 high_confidence capacity 条目。进一步突破需要：
- 对仿生文献库的表格图片做 OCR/多模态精读（当前多模态提取成功率低）
- 或新建 root prototype 并从零做文献证据接地
- 或调整 15% 目标

---

## 二、Stage 5 Readiness Audit

### 当前数据状态

| 指标 | 数值 |
|------|------|
| primary canon | 499 |
| AC+BC (biochar/AC) | 36 (7.2%) |
| 15% target | 74 |
| static gap | 38 |
| dynamic gap (含 chitosan/alginate partial) | 34 |
| plant-lignocellulosic 占比 | 33% (12/36) |
| high_confidence capacity | 1 (ALG-P71, PFOA/alginate, PDF verified) |
| partial evidence (PKB-only) | 4 (chitosan BPA + alginate PFOA) |
| side_evidence | 10 (KF/qe/综述引用/错配) |

### AC+BC 分布

| prototype | AC+BC count | 说明 |
|-----------|-------------|------|
| plant-lignocellulosic-architecture | 12 | 含 Batch 1-3 写入的 9 条 capacity |
| alginate | 7 | 含 1 条 high_confidence + 2 条 partial |
| chitosan | 7 | 含 3 条 partial |
| chlorella-cell-wall | 7 | 既有数据 |
| oyster-shell | 2 | 既有数据 |
| cell-membrane-ion-channel | 1 | 既有数据 |

### Stage 5 重算需要降权的原型

| prototype | 降权原因 | 当前状态 |
|-----------|---------|---------|
| metal-organic-framework | 已隔离到 quarantined/ | source_category='quarantined' |
| bone-structure | 高 weight(0.86) 低数据(2条pd) | 需复查 17 条 match_weights 的 matching_basis |
| oyster-shell | 高 weight(0.84) 低数据(6条pd) | 需复查 14 条 match_weights |
| polydopamine-coating | 与 mussel-foot-adhesion 重复 | 需去重（Stage 5 处理） |
| chitosan | 霸榜第1(27条match) | 需评估是否降权 |

### Stage 5 dry-run 方案

1. **不提交最终 match_weights**，只做 readiness audit
2. 降权规则：
   - exploratory lane: weight ≤ 0.3（当前有 0.6-0.75 的 exploratory match）
   - 非 direct_evidence: weight ≤ 0.5
   - bone-structure/oyster-shell: 复查 matching_basis，如 exploratory_no_source_evidence 则 weight ≤ 0.3
3. 新原型 match_weights：plant-lignocellulosic-architecture 新增 9 条 capacity → 可为 PFOA/BPA 增加 match_weights
4. 去重：polydopamine-coating ⇄ mussel-foot-adhesion 合并

### Stage 5 启动条件

- [x] ETL 幂等性验证通过
- [x] MOF + 2 deprecated + CNC 隔离完成
- [x] source_category='primary' 过滤生效
- [x] EC 回填完成（5 原型 16 条）
- [x] Validator 0 errors
- [x] Stage 4.5 证据耗尽报告完成
- [ ] 高质量 capacity 达到 15%（当前 7.2%）— **未达标，但证据已耗尽**
- [ ] plant-lignocellulosic 占比降至 30% 以下（当前 33%）— **接近但未达标**

**建议**：接受 7.2% 作为 Stage 4 最终值，进入 Stage 5 dry-run。
