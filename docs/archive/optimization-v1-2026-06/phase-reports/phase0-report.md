# Phase 0 — 准备与基线冻结 · 报告

## ① 修改文件列表

| 文件 | 操作 |
|------|------|
| `tools/snapshot_stats.py` | 新建 |
| `docs/optimization-v1/PLAN.md` | 新建（从方案复制） |
| `docs/optimization-v1/phase0-baseline.md` | 新建（脚本生成） |
| `docs/optimization-v1/phase0-report.md` | 新建（本报告） |

## ② 执行的命令

```bash
git fetch origin adsorption/dev
git checkout -b opt/curation-grounding-v1 origin/adsorption/dev
mkdir -p docs/optimization-v1
cp docs/优化方案_仿生库策展与接地_v1.md docs/optimization-v1/PLAN.md
python3 -X utf8 tools/snapshot_stats.py          # 生成基线
python3 -X utf8 tools/snapshot_stats.py && md5   # 可复现性检查（两轮 MD5 一致）
git rev-parse --abbrev-ref HEAD                    # 确认分支名
```

## ③ 验收实际输出

### 分支
```
opt/curation-grounding-v1
```

### 可复现性
```
两轮 MD5 均为 d74a03330feee5c507cfe3a814f4c48a ✅
```

### 基线统计

| 指标 | 值 |
|------|-----|
| 原型总数 | 31 |
| 机制总数 | 864 |
| 接地机制数（§1.3） | 0（预期：因果链未建立） |
| performance_data 总数 | 963 |
| 空 pollutant（总计） | 308 |
| 空 pollutant（非 needs_review） | 304 |

### Verification 分布（mechanisms）

| 等级 | 数量 |
|------|------|
| unverified | 864 |

### Verification 分布（performance_data）

| 等级 | 数量 |
|------|------|
| needs_review | 16 |
| single_source | 236 |
| unverified | 711 |

### 空壳原型（0 mechanism + 0 performance）

- `biomineralization-template`
- `coral-skeleton`
- `diatom-inspired-porous`
- `dna-aptamer`
- `magnetic-bacteria`
- `silkworm-silk`

### 与方案 §3 一致性检查

方案 §3 声明 31 个原型，实际 31 个 ✅
6 个空壳与方案描述一致 ✅

## ④ 残留风险

1. **enrichment 机制数（624）与 active 机制数（864）差异**：enrichment 只有 21 个原型，且格式为 dict 而非 list，部分机制在 enrichment 中被截断或未导出。Phase 4 需确认合并后数据完整性。
2. **304 条非 needs_review 的空 pollutant**：Phase 4 需按 §1.7 回填或标 needs_review。
3. **6 个空壳原型**：Phase 5 需从零建因果链（或判定为不可建并入待裁决）。

---

**Phase 0 验收：全绿 ✅，等待 Yao 确认后进入 Phase 1。**
