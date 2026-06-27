---
type: note
title: Gbrain Pglite Lock
status: active
updated: '2026-06-27T00:00:00.000Z'
ingested_via: 'mcp:put_page'
ingested_at: '2026-06-27T12:12:52.277Z'
source_kind: 'mcp:put_page'
---

# gbrain PGLite 锁问题

## 问题现象

autopilot 异常退出后，PGLite 的锁文件未清理，导致后续所有 gbrain 命令报 "Timed out waiting for PGLite lock"。

## 锁文件位置

```
~/.gbrain/brain.pglite/.gbrain-lock        # 目录
~/.gbrain/brain.pglite/.gbrain-resolve.sock  # 套接字
~/.gbrain/autopilot.lock                   # autopilot 锁
~/.gbrain/cycle.lock                       # cycle 锁
```

## 清理命令

```bash
rm -rf ~/.gbrain/brain.pglite/.gbrain-lock \
       ~/.gbrain/brain.pglite/.gbrain-resolve.sock \
       ~/.gbrain/autopilot.lock \
       ~/.gbrain/cycle.lock
```

## 监控建议

- 明晚 19:00 观察 autopilot 是否正常运行
- 如果再次卡住，检查锁文件是否残留
- 长期方案：评估是否需要升级 Bun 或 gbrain 版本

## 相关页面

- [[notes/gbrain-governance]]
- [[notes/gbrain-cli-fix]]

## 时间线

- 2026-06-27: 发现 PGLite 锁问题
- 2026-06-27: 清理锁文件，恢复正常
