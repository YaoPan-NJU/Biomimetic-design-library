# Baseline Statistics Report - 2026-06-10

## 分支信息
- 主线分支: feature/extraction-results
- 当前头: 7bceb3b12fba0a9829283c50d42d99479d5762c3
- 子模块头: 203b0cfd0122ad43df5bc1658fbc08ddd0ff2e06

## 统计数据
- 顶层 JSON 数: 31
- 全目录 JSON 数: 36（含 separation/）
- 总 performance 数据: 764
- 总 mechanism 数据: 1326
- Verified performance: 252
- 空 pollutant 数量: 238
- 已知 organism 错误: 3

## 一致性检查
- Warnings: 0
- Errors: 0

## 安全处理
- [x] 移除 openclaw.json 中的硬编码 token
- [ ] 轮换 token（需要用户手动操作）

## 下一步
1. 创建整改分支
2. 扩展 check_chimera.py 覆盖 mussel/cellulose 污染
3. 开始 Phase 1: 建立 canon 入库闭环
