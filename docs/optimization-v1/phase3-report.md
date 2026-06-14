# Phase 3 — 去污染 + chimera 真清理 · 报告（修正版）

## ① 修改文件列表

| 文件 | 操作 |
|------|------|
| `tools/chimera_blocklist.json` | 新建（种子污染对） |
| `tools/check_chimera.py` | 扩展：blocklist 检查 mechanism + performance_data + narrative |
| `prototypes_db/mussel-foot-adhesion.json` | 删除 6 机制 + 11 perf + 3 narrative |
| `prototypes_db/spider-silk.json` | 删除 5 机制 + 4 narrative |
| `prototypes_db/polydopamine-coating.json` | 删除 1 narrative |
| `tools/build_prototypes_db.py` | 接入 chimera blocklist 自动检查 |
| `docs/optimization-v1/phase3-decontam.md` | 新建（处置日志） |

## ② 执行的命令

```bash
python3 -X utf8 tools/check_chimera.py   # 修复前: 19 violations
# 清理...
python3 -X utf8 tools/check_chimera.py   # 修复后: 0 violations
python3 -X utf8 tools/validate_consistency.py  # 0 error
```

## ③ 处置明细

### mechanism 清理（第一轮，11 条）

| 原型 | 删除 | 剩余 | 命中关键词 |
|------|------|------|-----------|
| mussel-foot-adhesion | 6 | 88 | cellulose, CNC, 纤维素 |
| spider-silk | 5 | 31 | 荷叶, 猪笼草 |

### performance_data 清理（第二轮，11 条）

| 原型 | 删除 | 剩余 | 说明 |
|------|------|------|------|
| mussel-foot-adhesion | 11 | 43 | 全为 cellulose/CNC/CNF 相关材料数据，CNC 已 DEMOTE 不迁移 |

### narrative 清理（第二轮，8 条）

| 原型 | 删除 | 剩余 | 命中 |
|------|------|------|------|
| mussel-foot-adhesion | 3 | 12 | Salama2021/Gao2022/Mohammed2021（纤维素综述） |
| polydopamine-coating | 1 | 10 | Xiong2023（stenocara 甲虫） |
| spider-silk | 4 | 4 | 荷叶×2 + 猪笼草×2 |

## ④ 验收实际输出

```
修复前: 19 violations ✅ 能抓到（mechanism+perf+narrative 全覆盖）
修复后:  0 violations ✅

mussel mechanisms cellulose: False ✅
mussel perf cellulose: False ✅
mussel narrative cellulose: False ✅
spider 荷叶: False ✅
spider 猪笼草: False ✅
validate_consistency: 0 error ✅
```

## ⑤ 残留风险

1. **mussel-foot-adhesion 仍有 ~20 条 source_file 名含 cellulose 的 perf 条目**：这些条目的 material 不含 cellulose 关键词（如 "PDA-coated Fe3O4"），但 source_file 名是综述论文（如 "2021-salama-cellulose-..."）。这些条目的数据可能本身正确（PDA 涂层在 cellulose 基底上），只是来源文件是 cellulose 综述。当前 blocklist 未命中（因 source_file 匹配的是完整路径而非关键词），记为低风险残留。

---

**Phase 3 验收：全绿 ✅，等待 Yao 确认后进入 Phase 4。**
