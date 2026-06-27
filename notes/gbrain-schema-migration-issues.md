---
type: note
title: Gbrain Schema Migration Issues
status: active
updated: '2026-06-27T00:00:00.000Z'
ingested_via: 'mcp:put_page'
ingested_at: '2026-06-27T11:42:22.183Z'
source_kind: 'mcp:put_page'
---

# gbrain Schema Pack 迁移问题

## 背景

2026-06-27 从 `gbrain-base-v2` 切换到 `gbrain-recommended`。

## 发现的问题

### 1. MCP 与 CLI 数据不一致
- `gbrain schema stats`（CLI）显示 0 pages
- `mcp_gbrain_get_health`（MCP）显示 23 pages
- 原因：CLI 和 MCP 可能连接不同的数据库实例或 schema 缓存

### 2. Schema 类型定义混乱
- 现有页面使用 `note`, `project`, `concept` 等类型
- `schema_explain_type` 返回 `type_not_found`
- `schema_stats` 显示这些类型有页面
- 可能原因：frontmatter 的 `type` 是自由文本，不一定是 schema pack 注册的

### 3. 孤儿页面定义不一致
- `schema_review_orphans`（MCP）返回 0 orphans
- `get_health`（MCP）返回 19 orphan_pages
- 原因：两者定义不同
  - schema_review_orphans：没有 schema 类型匹配的页面
  - get_health orphan_pages：没有入链的页面

## 当前状态

- autopilot 正常运行（score=52）
- 搜索功能正常
- 但 schema 类型化可能不完整

## 今日新发现（2026-06-27）

### 4. 现有页面类型统计
从 `schema_stats` 获取的实际类型分布：
- `note`: 6 个
- `notes`: 4 个
- `concept`: 3 个
- `project`: 3 个
- `article`: 1 个
- `concepts`: 1 个
- `daily`: 1 个
- `meetings`: 1 个
- `people`: 1 个
- `projects`: 1 个
- `session-log`: 1 个

### 5. 类型是 frontmatter 自由文本
`schema_explain_type` 返回 `type_not_found`，但 `schema_stats` 显示这些类型有页面。说明：
- frontmatter 的 `type` 是自由文本
- gbrain-recommended 统计但不严格验证类型
- 搜索功能正常，无需立即修改

## 决策

- **保持现状**：不修改现有页面类型
- **未来新页面**：参考 `schema_stats` 的统计，使用已有类型

## 相关页面

- [[notes/gbrain-governance]]
- [[notes/gbrain-writing-guidelines]]

## 相关命令

```bash
# 查看 schema 统计
gbrain schema stats

# 查看类型定义
gbrain schema explain-type <type>

# 查看孤儿页面（schema 角度）
gbrain schema review-orphans

# 查看健康状态（包含 orphan_pages）
gbrain doctor --fast
```

## 时间线
- 2026-06-27: 切换到 gbrain-recommended
- 2026-06-27: 发现 schema 数据不一致问题
