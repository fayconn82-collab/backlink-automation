---
type: note
title: Gbrain Writing Guidelines
status: active
updated: '2026-06-27T00:00:00.000Z'
ingested_via: 'mcp:put_page'
ingested_at: '2026-06-27T12:12:56.377Z'
source_kind: 'mcp:put_page'
---

# gbrain 写作规范

## 每次写页面时必须做的事

### 1. 添加 Wikilinks

在内容中用 `[[slug]]` 格式链接到相关页面，例如：
```markdown
PhotoEditingPrompts 使用 [[projects/hermes]] 的技术栈。
```

### 2. 添加 Timeline（如有日期相关事件）

在页面末尾添加：
```markdown
## 时间线
- 2026-06-25: 项目启动
- 2026-06-27: 完成产品档案
```

## 类型使用建议

当前使用 gbrain-recommended schema，但类型是 frontmatter 自由定义。建议：
- 保持现有类型（搜索正常）
- 未来新页面时参考 `gbrain schema stats` 的统计

## 记忆规则

已写入 Memory：
> "Wikilinks 和 Timeline 规则：每次写 gbrain 页面时，必须检查并添加 wikilinks 和 timeline 条目。这是持续要求，不是一次性任务。如果忘记，用户会提醒。"

## 相关页面

- [[notes/information-routing-rules]]
- [[notes/gbrain-governance]]

## 时间线

- 2026-06-27: 确立写作规范
