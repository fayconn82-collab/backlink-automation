---
type: note
title: Information Routing Rules
status: active
updated: '2026-06-27T00:00:00.000Z'
ingested_via: 'mcp:put_page'
ingested_at: '2026-06-27T12:12:53.683Z'
source_kind: 'mcp:put_page'
---

# 信息路由规则（三层路由）

## 核心规则

| 层级 | 存什么 | 位置 | 例子 |
|------|--------|------|------|
| 世界知识/事实 | 人、项目、笔记、概念、会议 | gbrain 页面 | PhotoEditingPrompts 项目信息 |
| 操作偏好 | 用户喜欢什么、不喜欢什么 | Memory | 喜欢中文、只说多少做多少 |
| 任务进度/TODO | 今天做了什么 | 不存 | 用 session_search 查 |

## 执行规则

1. **每次聊天结束后**，用户会提醒记录进入 gbrain 和 repo
2. **知识流失靠两个方式处理**：
   - A. 手动迁移（聊天后主动写入 gbrain）
   - B. 定期回顾（用 session_search 找回历史）
3. **Memory 只存操作偏好**，不存事实/人物/项目

## 常见问题

### 为什么 Hermes 还是会自己写 memory？

因为 Memory 工具是"我主动调用"的，没有内置路由检查。需要每次写之前强制过一遍检查：
- 这是世界知识？→ 写 gbrain
- 这是操作偏好？→ 写 Memory
- 这是任务进度？→ 不写

## 相关页面

- [[notes/gbrain-writing-guidelines]]
- [[projects/hermes]]

## 时间线

- 2026-06-25: 首次讨论三层路由
- 2026-06-27: 强化规则，清理 memory
