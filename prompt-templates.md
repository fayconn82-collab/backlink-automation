# Hermes + OpenCLI 自动化外链提交 Prompt 模板

> 使用方式：复制对应模板到 Hermes 中，根据自己的目录和站点文件名替换变量即可。

---

## 1. 初始化任务：读取 Skill 和网站资料

```text
请先读取 skills/backlink-automation-submission/SKILL.md。

然后读取 sites/demo-site.md，理解这个网站的名称、URL、描述、分类、标签、Logo、截图和联系邮箱。

接下来请帮我判断：
1. 这个网站适合哪些类型的外链平台？
2. 哪些平台适合先提交？
3. 哪些平台可能需要登录、验证码、付费或人工接管？

请先输出计划，不要马上提交。
```

---

## 2. 第一次跑通：一个网站，一个平台

```text
请根据 sites/demo-site.md，为 DemoSite 提交一个外链平台。

要求：
1. 优先选择无需登录或低阻塞的平台。
2. 使用 OpenCLI 控制真实 Chrome 打开平台页面。
3. 根据网站资料填写网站名称、URL、描述、分类、标签等信息。
4. 如果遇到登录、验证码、邮箱验证、付费按钮、badge 要求或不确定的提交按钮，请停下来让我确认。
5. 提交后不要立刻算成功，先判断是否有 submitted、pending review、public listing、dashboard record 或明确 confirmation。
6. 把结果写入 records/daily/2026-xx-xx.md。
7. 如果失败，也要记录失败原因和是否计数。
```

---

## 3. 单站三平台：产品目录 + 技术检测页 + Add URL

```text
请根据 sites/demo-site.md，为 DemoSite 完成 3 个有效外链/公开资料页提交。

平台类型要求：
1. 尝试 1 个产品目录或工具目录。
2. 尝试 1 个技术检测/安全检测/SEO 检测页。
3. 尝试 1 个 Add URL 或搜索发现提交。

执行规则：
- 遇到登录、验证码、邮箱验证、付费、badge 要求，不要死磕，记录并跳过。
- submitted / pending review / public / live / verified 才计数。
- paid / captcha / email verification / draft / duplicate 不计数。
- 每个提交或阻塞都写入 records/daily/2026-xx-xx.md。
- 最后输出今日计数表。
```

---

## 4. 多站每日 SOP

```text
请为以下网站执行今日外链提交 SOP：

- sites/demo-site-a.md：目标 3 个
- sites/demo-site-b.md：目标 3 个
- sites/demo-site-c.md：目标 3 个

要求：
1. 每个网站完成 3 个有效提交/公开资料页。
2. 优先产品目录，其次技术检测页，最后 Add URL 补充。
3. 不要重复提交同一网站到同一平台。
4. 遇到登录、验证码、付费、badge 要求，记录原因并跳过。
5. 每次成功或阻塞都写入 records/daily/2026-xx-xx.md。
6. 最后输出：网站、目标、已计数、还差、已计数平台。
```

---

## 5. 遇到登录后的继续 Prompt

```text
我已经在浏览器中完成登录了。
请继续当前平台的提交流程。

注意：
- 不要点击付费按钮。
- 不要跳过最终确认状态检查。
- 提交后请判断是否有 submitted、pending review、public listing、dashboard record 或明确 confirmation。
- 把结果写入 records/daily/2026-xx-xx.md。
```

---

## 6. 遇到验证码后的处理 Prompt

```text
这个平台出现验证码，先不要继续死磕。
请把当前平台记录为 captcha / not counted。

记录内容包括：
- 平台名称
- 平台网址
- 目标网站
- 当前卡点：captcha
- 是否计数：否
- 下一步建议：需要人工处理或下次再试

然后继续寻找下一个候选平台。
```

---

## 7. 遇到付费墙后的处理 Prompt

```text
这个平台最后一步需要付费，暂时不付费。
请记录为 paid / incomplete，不计数。

然后继续下一个候选平台。
不要点击任何付费按钮。
```

---

## 8. 遇到重复提交后的处理 Prompt

```text
这个平台提示网站已经存在或已经提交过。
请记录为 existing / duplicate。

如果存在公开页面，请记录公开 URL，但不要计为今天的新提交。
如果没有公开页面，只记录为 duplicate / not counted。

然后继续下一个平台。
```

---

## 9. 技术检测页验证 Prompt

```text
请为 sites/demo-site.md 生成并验证 3 个技术检测/安全检测/SEO 检测公开页面。

要求：
1. 优先选择无需登录的平台。
2. 打开或请求平台 URL，确认 HTTP 200。
3. 确认最终 URL 或页面正文包含目标域名。
4. 记录为技术检测页/安全检测页/SEO audit 页面，不要写成产品推荐。
5. 把验证结果写入 records/daily/2026-xx-xx.md。
```

---

## 10. 收录追踪 Prompt

```text
请根据 records/daily/ 里的外链记录，追踪 DemoSite 的外链收录情况。

请分三层判断：
1. 页面存在：HTTP status、final URL、title、是否包含目标域名。
2. 搜索收录：使用 exact URL 查询，只有搜索结果中真实出现目标 URL 才算有证据。
3. SEO 效果：如果有 GSC/Analytics 数据，再判断 external links、referring domains、impressions/clicks、referral traffic。

请不要把页面存在说成 Google 已收录。

输出 CSV 字段：
date,domain,platform,url,status,http_status,final_url,contains_domain,title,indexed,index_evidence_url,index_note
```

---

## 11. 最终日报总结 Prompt

```text
请根据 records/daily/2026-xx-xx.md，生成今日外链提交总结。

格式：

1. 先输出今日计数表：网站、目标、已计数、还差、已计数平台。
2. 再输出平台级总结：平台名称、网址、提交方式、避坑指南、本次提交网站。
3. 单独列出未计数平台：paid、captcha、email verification、duplicate、incomplete。
4. 不要把技术检测页包装成产品推荐。
5. 不要夸大 SEO 效果，只说明提交/验证状态。
```
