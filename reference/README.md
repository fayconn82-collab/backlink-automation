# 自动化外链提交工作目录模板

这个目录用于配合《我是怎么用 Hermes + OpenCLI，把外链提交跑成半自动化 SOP 的》文章使用。

建议先用 `sites/demo-site.md` 跑通一遍，再替换成自己的真实网站。

## 目录结构

```text
workspace-template/
├── sites/
│   └── demo-site.md
├── assets/
│   ├── logos/
│   │   └── .gitkeep
│   └── screenshots/
│       └── .gitkeep
├── records/
│   └── daily/
│       └── YYYY-MM-DD.md
├── skills/
│   └── backlink-automation-submission/
│       └── SKILL.md
└── platforms/
    └── public-platforms.csv
```

## 使用步骤

1. 复制整个目录到你的工作区。
2. 把 `sites/demo-site.md` 改成你的网站资料。
3. 把网站 Logo 放到 `assets/logos/`。
4. 把网站截图放到 `assets/screenshots/`。
5. 把文章附件中的 `SKILL.md` 放到 `skills/backlink-automation-submission/SKILL.md`。
6. 把文章附件中的 `外链平台公开列表-读者版.csv` 复制到 `platforms/public-platforms.csv`。
7. 在 Hermes 中读取 Skill 和网站资料后开始执行。

## 推荐第一次 Prompt

```text
请先读取 skills/backlink-automation-submission/SKILL.md。
然后读取 sites/demo-site.md。

请为 DemoSite 选择一个低阻塞平台进行第一次外链提交。
如果遇到登录、验证码、邮箱验证、付费、badge 要求或不确定提交按钮，请停下来让我确认。
提交后请判断是否可以计数，并写入 records/daily/YYYY-MM-DD.md。
```

## 重要提醒

- 不要把 API Key、Cookie、账号密码放进这个目录。
- 公开截图前记得打码邮箱、账号、真实站点和本地路径。
- 技术检测页只能写成技术检测/公开资料页，不要包装成平台推荐。
- 只有有证据的 submitted / pending review / public / verified 才能计数。
