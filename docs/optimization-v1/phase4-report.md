# Phase 4 — 字段语义修复 + 诚实标注 · 报告

## ① 修改文件列表

| 文件 | 操作 |
|------|------|
| `prototypes_db/*.json`（全部 24 个） | pollutant 回填、causal_chain 骨架、verification 统一 |
| `prototypes_db/enrichment/*.json` | 重新导出 24 个（清理 5 个过期文件） |
| `tools/build_prototypes_db.py` | 修复 chimera 检查的 sys 引用 |

## ② 步骤执行

### Step 1: organism 复核
全部 24 个 active 原型 organism 无明显错误。category 使用约定：仿生材料（chitosan, cell-membrane, dna-aptamer, biomineralization-template）、动物（mussel, bone, fish-scale 等）、微生物（chlorella, diatom, SRB, IOB 等）、植物（mangrove, pitcher-plant, plant-tannin, wood-xylem）。

### Step 2: pollutant 回填
- **可确定**: 49 条（从 parameter/value/material/conditions 识别单一污染物）
- **歧义**: 63 条（多个候选，置 needs_review + note "pollutant ambiguous"）
- **无法识别**: 79 条（完全无线索，置 needs_review + note "pollutant unidentifiable"）
- **空 pollutant 非 needs_review**: 0 ✅

### Step 3: causal_chain 骨架
- 528 条 mechanism 全部添加 `causal_chain` 空骨架（四要素 + boundary_conditions + transferable_principle）
- 缺 causal_chain: 0 ✅

### Step 4: verification 统一
- 所有 `unverified` / `single_source` → `needs_review`（重建后验证：无残留）

### Step 5: enrichment 导出
- 导出 24 个 enrichment 文件（从当前 canon 直接导出，非重建）
- 清理 5 个过期文件（alginate, cellulose-nanocrystal, metal-organic-framework, starch-granule, namib-beetle）

## ③ 验收实际输出

```
defects= 0 ✅
  空 pollutant 非 needs_review: 0
  缺 causal_chain: 0
enrichment: 24 files ✅
validate_consistency: 0 error ✅
check_chimera: 0 violations ✅
```

## ④ 残留风险

1. **build_prototypes_db.py 会覆盖 canon**：从 prototypes/ markdown 重建时，merge_with_existing 会重引入已删除的机制。本 Phase 采用直接编辑 canon JSON + 手动导出 enrichment 的方式绕过。后续 Phase 若需重建，须先确认 markdown 源已同步。
2. **49 条回填的 pollutant 标为 needs_review**：推断内容，Phase 6 核验时需确认。
3. **63 条歧义 + 79 条无法识别**：进入待裁决清单，留 Yao 处理。

---

**Phase 4 验收：全绿 ✅，等待 Yao 确认后进入 Phase 5。**
