---
type: note
title: Gbrain Governance
status: active
updated: '2026-06-27T00:00:00.000Z'
ingested_via: 'mcp:put_page'
ingested_at: '2026-06-27T12:11:42.521Z'
source_kind: 'mcp:put_page'
---

# gbrain 自动治理系统

## 组件概览

| 组件 | 功能 | 频率 | 状态 |
|------|------|------|------|
| autopilot | 自动维护：同步、链接、嵌入、清理 | 每天 19:00 | 正常运行 |
| eval | 搜索质量评估 | 暂不运行 | 待设计 qrels |
| advisor | 实时诊断 | 按需 | 已开启 |
| onboard | 初始化向导 | 安装/升级时 | 已完成 |
| jobs | 后台任务队列 | 持续 | 正常 |

## autopilot

- **时间**：每天北京时间 19:00
- **逻辑**：扫描指定 repo 的 markdown 文件，导入 gbrain，建立链接，补全嵌入
- **当前 repo**：`~/Coding/backlink-automation`
- **未来多 repo**：可为每个工作区创建独立 autopilot cron 任务，错开时间

## eval

- **暂不运行**，原因：
  - 页面太少（23 个），eval 参考意义不大
  - 需要手工维护 qrels 文件，目前无自动生成方案
  - 等页面 50+ 时再设计

## advisor

- **状态**：已开启（`mcp.publish_advisor: true`）
- **用法**：`gbrain advisor` 或 MCP `mcp_gbrain_advisor`

## cron deliver

- **当前**：`local`（只写日志，不推送）
- **日志位置**：`~/.hermes/profiles/backlink/cron/output/`
- **未来如需推送**：可改 `origin`（当前 session）或 `all`（所有平台）

## 相关命令

```bash
# 查看 autopilot 状态
gbrain autopilot status

# 手动运行一次
gbrain autopilot --repo ~/Coding/backlink-automation --once

# 查看 jobs
gbrain jobs list

# 查看配置
gbrain config show
```
