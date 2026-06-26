# Backlink Workspace

外链自动化工作目录，基于 Hermes + OpenCLI 的半自动化外链提交流程。

## 目录结构

```
backlink-workspace/
├── sites/                          # 网站资料
│   └── *.md                        # 每个网站一个 Markdown 文件
├── assets/
│   ├── logos/                      # 网站 Logo
│   └── screenshots/                # 网站截图
├── records/
│   └── daily/                      # 每日提交记录
│       └── YYYY-MM-DD.md
├── skills/
│   └── backlink-automation-submission/
│       └── SKILL.md                # 外链自动化 Skill
└── platforms/
    └── public-platforms.csv        # 外链平台列表
```

## 每日目标

- 每个网站 3 个有效提交/公开资料页
- 优先产品目录 → 技术检测页 → Add URL 补充
- 遇到登录/验证码/付费/badge 要求，记录并跳过

## 状态说明

**计数状态**：submitted / pending review / public / live / verified / scheduled
**不计数状态**：login-required / captcha / email-verification / paid / badge-required / duplicate / draft / incomplete / failed / not-relevant / unclear

## 使用流程

1. 准备网站资料 → `sites/网站名.md`
2. 加载 Skill → `skills/backlink-automation-submission/SKILL.md`
3. 选择平台 → 参考 `platforms/public-platforms.csv`
4. 执行提交 → 使用 OpenCLI 控制 Chrome
5. 记录结果 → `records/daily/YYYY-MM-DD.md`

## 参考

- 完整教程见：`自动化外链提交实战教程-正文.md`
