---
type: note
title: Gbrain Cli Fix
status: active
updated: '2026-06-27T00:00:00.000Z'
ingested_via: 'mcp:put_page'
ingested_at: '2026-06-27T12:12:50.934Z'
source_kind: 'mcp:put_page'
---

# gbrain CLI Bun WASM Bug 修复记录

## 问题现象

Bun 1.3.14 编译产物有 WASM 运行时 bug，编译后的单文件 `gbrain` 无法初始化 PGLite，导致所有 gbrain 命令失败。

## 根因

Bun 1.3.14 的编译产物在初始化 PGLite WASM 模块时卡住，无法完成数据库连接。

## 修复方案

创建 wrapper 脚本，绕过编译产物，直接用 `bun run src/cli.ts` 源码方式运行。

### wrapper 脚本位置

`~/.bun/bin/gbrain`

### wrapper 脚本内容

```bash
#!/bin/bash
cd "$HOME/.bun/install/global/node_modules/gbrain" || exit 1
exec bun run src/cli.ts "$@"
```

## 验证命令

```bash
# 版本号
gbrain --version
# 预期输出：gbrain 0.42.53.0

# autopilot 状态
gbrain autopilot status

# 快速体检
gbrain doctor --fast
```

## 相关文件

- gbrain 源码：`~/.bun/install/global/node_modules/gbrain/src/cli.ts`
- 配置：`~/.gbrain/config.json`
- 数据：`~/.gbrain/brain.pglite/`

## 时间线

- 2026-06-27: 发现 Bun WASM bug
- 2026-06-27: 创建 wrapper 脚本修复
