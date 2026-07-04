# Stage 3 Engineering Constraints 回填报告

**日期：** 2026-07-04
**修改文件：** `prototypes_db/alginate.json`, `starch-granule.json`, `oyster-shell.json`, `lotus-leaf.json`, `scallop-shell.json`

---

## 一、回填方法

每条 high relevance EC 基于：
1. 原型 `mechanisms[].causal_chain.boundary_conditions` 的已有约束
2. `design_translation[].constraints` 和 `failure_modes` 的已有描述
3. 不编造约束——所有 EC 都能在原型的已有数据中找到依据

## 二、回填结果

| 原型 | EC 前 | EC 后 | high relevance | 关键约束 |
|------|:-:|:-:|:-:|------|
| alginate | 0 | 3 | 2 | pH<3 质子化、盐竞争、机械强度 |
| starch-granule | 0 | 4 | 3 | 需改性、酸碱水解、糊化温度、生物降解 |
| oyster-shell | 0 | 3 | 3 | 需煅烧、CaO 水化放热、竞争阳离子 |
| lotus-leaf | 0 | 3 | 2 | 机械磨损、不适用亲水场景、酸碱腐蚀 |
| scallop-shell | 0 | 3 | 2 | 低 pH 溶解、煅烧成本、竞争阳离子 |
| **合计** | 0 | **16** | **12** | |

## 三、deferred 项

以下原型的 EC 回填已 deferred（原因合理）：

| 原型 | 原因 |
|------|------|
| metal-organic-framework | 已隔离到 quarantined/，无需回填 |
| diatom-inspired-porous | 已隔离（deprecated），无需回填 |
| silkworm-silk | 已隔离（deprecated），无需回填 |
| cellulose-nanocrystal | 已降级到 quarantined/，无需回填 |
| dna-aptamer | 已在 Q3 中回填 3 条 high EC（温度、核酸酶、低证据守卫） |
| namib-beetle | lifecycle=parked，无需回填 |
| cactus-spine / coral-skeleton / biomineralization-template / water-strider-leg | performance_data=0，需先补数据再回填 EC |

## 四、验证

- `validate_consistency.py --report-only`：**0 错误**，40 个 primary 原型一致
- `git commit 38ab3cc` 已 push 到 review

## 五、commit 状态

- BMDL 仓库 commit: `38ab3cc` (review 分支)
- ADRMATS 仓库 ETL 幂等性修复: 待 push
