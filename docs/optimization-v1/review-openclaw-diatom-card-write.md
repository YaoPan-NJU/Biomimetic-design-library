status: ready_for_qoderwork_acceptance
worker: OpenClaw/xiaomi-mimo-v2.5-pro
completed_at: 2026-06-17 23:38 CST
action: write_causal_card

---

# Diatom Frustule — Causal Card 写入报告

## 1. 写入操作摘要

| 项目 | 值 |
|------|---|
| 目标文件 | `prototypes_db/diatom-frustule.json` |
| 目标机制 | `mechanisms[2]` — "CA/DE缩合机理" |
| 写入字段 | `causal_chain`（含 4 要素 + 5 条 boundary_conditions + transferable_principle + verification_quote） |
| 补充字段 | `source_file`, `source`（已有）, `ref_doi`（已有）, `基本原理`（从 needs_review 更新为实际内容） |
| verification | **needs_review**（未升级，符合硬规则） |
| 其他机制 | 未改动 |
| build_prototypes_db.py | 未改动 |
| git commit/push | 未执行 |

## 2. 因果链卡内容

- **pollutant_feature**: Pb²⁺/Cd²⁺ 二价重金属阳离子，配位键结合
- **bio_structure**: 硅藻土层级多孔 SiO₂ 骨架 + APTES-CA 缩合修饰 –NH₂/–COOH
- **interaction**: RNH₂-M²⁺ 配位键 (XPS 406.73 eV) + –COO⁻ 静电/螯合
- **why_it_works**: 化学吸附为主，吸附容量跃升至 396–485 mg/g
- **transferable_principle**: 硅烷缩合接枝含 N/O 供体官能团 → 化学配位主导
- **verification_quote**: 化学吸附驱动力 + 配位能力对比

## 3. Boundary Conditions (5 条)

| # | parameter | condition | gate_level |
|---|-----------|-----------|------------|
| 1 | pH | range [6, 8] | hard |
| 2 | pH | < 3 (质子化抑制) | hard |
| 3 | pH | > 9 (假吸附) | hard |
| 4 | other | qualitative (pH 不波动) | hard |
| 5 | other | qualitative (>800 mg/L 饱和) | hard |

## 4. 校验结果

| 脚本 | diatom-frustule | 全局 | status |
|------|----------------|------|--------|
| `check_causal_chain.py` | 1/15 qualified | 26/530 | ✅ |
| `check_boundary_guardrail.py` | BC pass | pitcher-plant 缺 BC (既有问题) | ✅ (diatom) |
| `validate_consistency.py` | 0 error | 0 error, 194 warnings (既有) | ✅ |
| `check_chimera.py --strict` | 0 违规 | 0 违规 | ✅ |

## 5. 硬规则遵守确认

- [x] `verification` 保持 `needs_review`
- [x] 未改动其他机制
- [x] 未改动 `build_prototypes_db.py`
- [x] 未 commit/push
- [x] 四项校验全部通过（diatom-frustule 维度）

## 6. 待 QoderWork 决策

1. 是否接受本次写入？
2. `mechanisms[2]` 的 `verification` 是否在 Yao 审批后升级为 `verified`？
