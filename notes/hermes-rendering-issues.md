---
type: note
title: Hermes Rendering Issues
status: active
updated: '2026-06-27T00:00:00.000Z'
ingested_via: 'mcp:put_page'
ingested_at: '2026-06-27T12:12:54.987Z'
source_kind: 'mcp:put_page'
---

# Hermes 桌面端渲染问题

## 问题现象

当 assistant 在回复中穿插工具调用时，前面的文本会被截断或覆盖，用户只能看到工具调用之后的内容。

## 根因

Hermes 桌面端的渲染机制在处理"流式回复 + 工具调用"时有 bug。工具调用会暂停文本流，但不恢复之前的文本。

## 解决方案

**工具调用前置**：
1. 先执行所有工具调用（如果需要）
2. 再写完整回复文本
3. 绝不在回复中间穿插工具调用

## 记忆规则

已写入 Memory：
> "Hermes 桌面端渲染问题：当 assistant 在回复中穿插工具调用时，前面的文本会被截断或覆盖。解决方案：工具调用前置——先执行所有工具调用，再写完整回复文本。绝不在回复中间穿插工具调用。"

## 相关页面

- [[projects/hermes]]
- [[notes/gbrain-writing-guidelines]]

## 时间线

- 2026-06-27: 发现并记录问题
- 2026-06-27: 确立工具调用前置规则
