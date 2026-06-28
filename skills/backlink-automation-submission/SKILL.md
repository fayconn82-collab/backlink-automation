---
name: backlink-automation-submission
description: 白帽外链半自动化提交流程。Use when 用户要求发外链、提交产品到目录平台、做技术检测页外链、或运行每日外链配额。NOT for 黑帽外链、群发垃圾外链、自动绕过验证码。
version: 1.0.0
author: Friday023
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [seo, backlink, outreach, automation, opencli]
    related_skills: [opencli-browser]
---

# 外链自动化提交

Hermes = 大脑，OpenCLI = 手和眼睛，Chrome = 真实操作现场，记录表 = 账本。

每个外链提交流程：选平台 → 前台打开 → 填写/提交 → 验证链接性质 → 记录。

## 信息归宿规则

工作中产生的信息严格按去向分流，不要全塞 gbrain：

| 信息类型 | 去向 | 例子 |
|---------|------|------|
| 世界知识/事实 | gbrain 页面 | 平台经验、OpenCLI 架构、外链方法论 |
| 项目数据/产物 | repo 文件（git 管理） | 每日记录 records/daily/、产品档案 sites/、脚本 scripts/ |
| 操作偏好 | Memory | 用户喜欢中文、关键操作确认 |

## 前置检查

每次 session 开始或 compact 后，必须先做：

```bash
opencli doctor
```

确认 daemon + browser extension 都正常连接。不通则汇报用户，不继续。

## 用户主权规则（硬约束）

以下规则优先级高于一切流程：

1. **你说多少我做多少** — 用户没明确授权的操作不做，不擅自扩展、不自动跳到下一步
2. **改动前先汇报** — 任何实质性修改（编辑文件、改配置、写 skill）必须先汇报并取得同意，只读操作无需确认
3. **完成即停** — 发完一个平台后停下来汇报，等用户指示再发下一个
4. **阻塞即停即报** — 遇到 Cloudflare/403/登录墙/验证码，立即停止操作，向用户汇报阻塞类型和建议方案，不自行切换平台重试
5. **禁止高频重试** — 同一平台失败 2 次后放弃，同一域名访问间隔 ≥ 30 秒，禁止连续快速访问多个平台

## 路由

| 场景 | 加载 |
|------|------|
| 当前任务是提交外链 | 读正文下方的「核心流程」 |
| 需要确认产品信息或写 site profile | 读 [rules/site-profile.md](rules/site-profile.md) |
| 遇到 Cloudflare/403/登录墙/验证码 | 读 [rules/blocking-handling.md](rules/blocking-handling.md) |
| 需要区分产品目录 vs 技术检测页 vs Add URL | 读 [rules/platform-types.md](rules/platform-types.md) |
| compact 后恢复或新 session 接手 | 读 [rules/compact-recovery.md](rules/compact-recovery.md) |
| 平台要求上传截图 | 读 [rules/screenshots.md](rules/screenshots.md) |
| 发完需要验证外链性质 | 先读 [references/backlink-verification.md](references/backlink-verification.md)，再运行 `scripts/verify-backlink.py` |
| 需要查 OpenCLI 命令用法 | 读 [references/opencli-quick-ref.md](references/opencli-quick-ref.md) |
| 需要查原作者文章要点 | 读 [references/original-article-key-points.md](references/original-article-key-points.md) |
| 需要查原作者文章要点 | 读 [references/original-article-key-points.md](references/original-article-key-points.md) |
| 准备或更新产品档案 | 读 [references/site-profile.md](references/site-profile.md) |
| 需要理解外链验证方法论、链接层次分类 | 读 [references/backlink-verification.md](references/backlink-verification.md) |
| 需要查已验证平台清单和经验 | 读 `platforms/public-platforms.csv`，查看「避坑说明」列 |
| verify-backlink.py 返回空/Just a moment（Cloudflare 拦截） | 读 [references/verification-cloudflare-workaround.md](references/verification-cloudflare-workaround.md) |
| gbrain MCP 调用连续报错或断连 | 读 [references/gbrain-interaction.md](references/gbrain-interaction.md) |

## 核心流程

### Step 1: 确认产品信息

读 `sites/<product>.md`，确认网站名称、URL、描述、分类、标签、Logo 路径、截图路径。

### Step 2: 选平台

从 `platforms/public-platforms-list.md` 选平台。优先级：产品目录 > 技术检测页 > Add URL。优先选以前验证过可用的。

### Step 3: 前台打开平台页面

**所有 opencli browser 命令必须加 OPENCLI_WINDOW=foreground 环境变量。** 禁止后台窗口。

```bash
OPENCLI_WINDOW=foreground opencli browser <session-name> open "<platform-url>"
```

使用固定的 session 名（如 `backlink-submit`），不要每次换名字。

### Step 4: 模拟真人操作

**无论打开的是什么页面，必须通过页面上的交互元素完成操作，不许跳过输入/点击步骤直接到达结果页。**

统一流程（所有平台类型适用）：

1. 用 `state` 获取页面结构，找到输入框/搜索框的 ref
2. 用 `type` 输入目标域名或其他必要信息
3. 用 `click` 点击搜索/检测/提交按钮
4. 用 `wait time <seconds>` 等待结果生成
5. 用 `state` 确认结果页包含目标域名
6. 用 `get url` 记录最终结果页 URL

每次写操作后用 `get value` 验证写入是否成功。提交产品目录时上传 Logo 和截图（如果平台要求）。【读 rules/screenshots.md】

### Step 5: 判断是否成功

**可以计数的状态：**
- submitted / pending review
- public / live / verified
- HTTP 200 + 页面/URL 包含目标域名

**不能计数的状态：**
- requires login / captcha / paid / failed
- 只填了表但没提交
- 没有明确回执

**遇到阻塞 → 立即停，读 [rules/blocking-handling.md](rules/blocking-handling.md)。**

### Step 6: 验证链接性质

发完后运行验证脚本：

```bash
python3 scripts/verify-backlink.py "<result-url>" "<target-domain>"
```

脚本输出：backlink_type（dofollow/nofollow/mention）、pass_weight、实际 <a> 标签数量。

验证结论同时追加到 `platforms/public-platforms.csv` 对应平台的「避坑说明」列，格式：
```
实测结论 | 链接情况 | 日期
```
例：`curl被CF拦截需用browser eval | 1个nofollow直链不传权 | 2026-06-28`

### Step 7: 记录

写入 `records/daily/YYYY-MM-DD.md`，使用模板格式。

备注使用结构化写法，不引入复杂标签系统（避免标签无限蔓延）：
```
type: 技术检测页 | links: 2个a标签 | rel: 无(默认dofollow) | pass_weight: true | 说明: 全球多节点DNS解析结果
```

**记录完成后向用户汇报：** 平台名称、URL、链接类型、是否传递权重、今日进度（x/目标）。

**汇报后停下来等用户指示，不要自动继续下一个平台。**

## FORBIDDEN

- 后台窗口提交外链（所有 opencli browser 必须 OPENCLI_WINDOW=foreground）
- 跳过页面交互直接拼 URL 到达结果页（所有平台都必须走 type→click→wait 流程）
- 同一个平台连续失败后换 URL 重试
- 连续访问间隔 < 30 秒
- 遇到 Cloudflare/验证码后反复尝试
- 把技术检测页描述为"某某平台推荐了我的产品"

## Stop Conditions

遇到以下任一，**立即停，汇报用户：**

- Cloudflare / JS Challenge / 人机验证
- HTTP 403 / 401
- 登录墙（需要账号密码或 OAuth）
- 付费墙（要求升级套餐）
- 验证码（reCAPTCHA / 图形验证码）
- 同一平台连续失败 2 次

汇报格式：平台名、URL、遇到的阻塞类型、建议下一步（人工登录/换平台/放弃）。

## 验证脚本

`scripts/verify-backlink.py` — 用 curl 拉取页面 HTML，分析 <a> 标签的 href 和 rel 属性。已知局限：对 JS 渲染页面（SPA）只能抓到静态壳。**Cloudflare 保护的站点 curl 会被拦截返回 JS Challenge 页**，此时改用 OpenCLI `browser eval` 在真实浏览器页面中查 DOM。详见 [references/verification-cloudflare-workaround.md](references/verification-cloudflare-workaround.md)。

## Verification Checklist

- [ ] opencli doctor 通过
- [ ] 所有 opencli browser 命令带 OPENCLI_WINDOW=foreground
- [ ] 平台访问间隔 ≥ 30 秒
- [ ] 成功后运行 verify-backlink.py
- [ ] 记录写入 records/daily/YYYY-MM-DD.md
- [ ] 结构化备注包含 link_type + pass_weight
