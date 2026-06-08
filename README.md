# 生物原型知识库 / Biological Prototype Knowledge Base

ADRMATS 系统的仿生启发检索模块。

> **唯一执行入口：[docs/ADRMATS_DELIVERY_PLAN.md](docs/ADRMATS_DELIVERY_PLAN.md)**

---

## 当前状态（2026-06-08 13:30）

| 指标 | 数值 |
|------|------|
| 分支 | `feature/extraction-results` |
| 最新 commit | `f47a3af` |
| prototypes_db/*.json | 31 |
| 性能数据总数 | 752 |
| verified | 0 |
| single_source | 236 |
| unverified | 500 |
| needs_review | 16 |
| 校验错误 | 0 |
| chimera 违规 | 0 |

## 接口使用

```python
from tools.biomimetic_context import BiomimeticContext

ctx = BiomimeticContext()
brief = ctx.query(
    pollutant="Pb(II)",
    water_quality={"pH": 6.0, "temperature": 25, "salinity": "low"},
    engineering_constraints=["水稳定性", "可回收性"]
)
```

## 相关文档

- [交付计划](docs/ADRMATS_DELIVERY_PLAN.md) — 唯一执行入口
- [库定位与 brief 结构](docs/design.md)
- [分层检索策略](docs/ADRMATS_INTEGRATION.md)

## 相关专利

隶属于《一种水处理仿生吸附材料开发智能体系统》
