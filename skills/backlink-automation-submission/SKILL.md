---
name: backlink-automation-submission
description: Use Hermes + OpenCLI to run repeatable white-hat backlink submission workflows for indie websites, including platform selection, browser operation rules, success criteria, and daily logging.
---

# Backlink Automation Submission

## When to use

Use this skill when the user wants to submit backlinks / product listings / directory listings / technical audit pages for one or more websites, especially when using Hermes Agent with a real Chrome browser controlled by OpenCLI.

This skill is designed for white-hat, low-volume, manual-review-friendly backlink work. It is not for spam, mass posting, cloaking, fake accounts, comment spam, or bypassing anti-abuse systems.

## Core principle

The goal is not to click as many buttons as possible.

The goal is to create a reliable daily backlink SOP:

1. Read website profile.
2. Select relevant platforms.
3. Submit or generate public pages carefully.
4. Stop at sensitive checkpoints.
5. Verify evidence before counting.
6. Record every success, block, and failure.
7. Improve the platform notes after each run.

## Inputs required

For each target website, require a site profile markdown file with:

- Website Name
- Website URL
- One-liner
- Short Description CN, optional
- Long Description EN
- Target Users
- Categories
- Tags
- Logo Path, if available
- Screenshot Path, if available
- Contact Email
- GitHub / social links, if available
- Notes / constraints

Do not invent missing business claims. If a field is missing and it materially affects submission, ask the user or skip platforms requiring that field.

## Daily target

Default daily target:

- 3 counted submissions / public pages per website per day.
- Prefer quality and relevance over quantity.
- Do not brute force dozens of directories in one day.

A counted item must have evidence. Filling a form is not enough.

## Platform priority

Prefer in this order:

1. Relevant product / SaaS / tool directories.
2. Niche directories that match the site category.
3. Technical / security / SEO audit pages that produce public URLs containing the target domain.
4. Add URL / search discovery submissions with explicit confirmation.

Avoid or skip:

- Irrelevant AI directories for non-AI products.
- Obvious link farms.
- Platforms requiring payment unless the user explicitly approves.
- Platforms requiring website badge unless the user explicitly approves.
- Platforms requiring fake reviews, fake votes, fake accounts, or comment spam.

## Browser operation rules

When using OpenCLI / browser control:

1. Use the user's real Chrome session only for normal browsing and already-approved login states.
2. Never type passwords, API keys, recovery codes, credit cards, or payment details.
3. Stop and ask the user to take over when encountering:
   - login
   - OAuth confirmation
   - password prompt
   - reCAPTCHA / hCaptcha
   - email verification
   - payment page
   - required badge installation
   - account security warning
   - unclear destructive action
4. After the user completes a checkpoint, continue from the current page.
5. Do not bypass anti-bot systems.
6. Do not create fake identities.

## What counts as success

Count only if one of these is true:

- Platform shows submitted / pending review / submission received.
- Platform shows live / public listing.
- Dashboard contains a clear record of the submitted product or site.
- A public verification URL returns HTTP 200 and contains the target domain.
- A scheduled listing has a clear scheduled state and platform-owned URL.

Record the evidence URL whenever possible.

## What does NOT count

Do not count:

- only filled form, not submitted
- draft
- incomplete profile
- payment required
- captcha blocked
- email verification pending
- duplicate without a new counted action
- login required and not completed
- badge required and not installed
- unclear confirmation
- platform not relevant
- final page does not contain target domain

Record these as not counted with reason.

## Status taxonomy

Use these statuses consistently:

Counted statuses:

- submitted
- pending review
- public
- live
- verified
- scheduled
- existing-active, only if the task is auditing existing backlinks, not daily new count

Not-counted statuses:

- login-required
- captcha
- email-verification
- paid
- badge-required
- duplicate
- draft
- incomplete
- failed
- not-relevant
- unclear

## Daily log format

Write or update `records/daily/YYYY-MM-DD.md`.

Use this structure:

```markdown
# 外链提交记录 - YYYY-MM-DD

## 今日计数表

| 网站 | 目标 | 已计数 | 还差 | 已计数平台 |
|---|---:|---:|---:|---|
| DemoSite | 3 | 2 | 1 | Platform A, Platform B |

## 明细记录

| 时间 | 网站 | 平台 | 平台网址 | 提交/验证 URL | 状态 | 是否计数 | 备注 |
|---|---|---|---|---|---|---|---|
| YYYY-MM-DD HH:mm | DemoSite | Platform A | https://example.com | https://example.com/demo | pending review | 是 | Submission Received |

## 未计数/阻塞记录

| 时间 | 网站 | 平台 | 阻塞类型 | 是否计数 | 下一步 |
|---|---|---|---|---|---|
| YYYY-MM-DD HH:mm | DemoSite | Platform B | paid | 否 | 暂不付费，跳过 |
```

## Platform-specific notes from field experience

### Uneed

If a product is only created as edit / waiting-line data and fields like `ready=false` or `launchDate=null` are present, treat it as draft/incomplete. Do not count unless there is a scheduled or public listing state.

### SaaSHub

A managed listing may already exist. If so, record the public URL. Do not count it as a new daily submission unless the current task is backlink inventory or profile completion.

### BetaList

Often leads to payment/package steps. If payment is required, record as paid/incomplete and do not count.

### ToolFame

Verify the public item URL, commonly `/item/<slug>`, or a clear dashboard record. Rich text editors and tag components may fail silently. If form state does not persist, record incomplete.

### Launching Next

Count only with clear `Submission Received` or equivalent confirmation. If it routes to paid upgrade without confirmation, record paid/incomplete.

### Fazier

Free submission may require helpful comments, badge, English site, or DR > 0. If requirements are not met, record not counted.

### Tiny Startups

May show paid upsells. If a free continuation exists, it can be used. If email is rejected as auto-generated or suspicious, stop and ask the user.

### ProductFame / Turbo0

Dynamic forms may fail to save category/tag state. Do not repeatedly fight broken UI. Record incomplete and move on.

## Technical audit page rules

Technical audit pages are useful as public footprint / index discovery support, but they are not product recommendations.

When recording them, write:

- public SSL/TLS check page
- public security header check page
- public SEO audit page
- public technology profile page

Do not write:

- platform recommended us
- platform featured us
- high-quality editorial backlink

Count only if the public page or final URL contains the target domain and is accessible.

## Suggested platform categories

Product / SaaS / tool directories:

- Uneed
- SaaSHub
- Launching Next
- BetaPage
- PitchWall
- ToolFame
- Tiny Startups
- ProductFame
- Turbo0

AI / tool directories:

- Futurepedia
- Toolify
- Fazier
- Aimyflow
- AICavo

Technical / security / SEO check pages:

- SSL Labs
- Sucuri SiteCheck
- SecurityHeaders
- PageSpeed Insights
- Mozilla Observatory
- HackerTarget
- Shodan
- BlackListAlert
- SEO SiteCheckup
- WhatRuns
- Wappalyzer
- WhatCMS
- OpenAdminTools
- Host.io
- VirusTotal
- Robtex
- Netcraft
- MXToolbox

Add URL / discovery:

- Active Search Results
- InfoTiger
- Free Web Submission

## Final response after each run

Always summarize:

1. Count table per website.
2. Counted platforms with evidence URLs.
3. Not-counted platforms with reasons.
4. Human actions needed.
5. Suggested next platforms.

Never overstate SEO impact. Say what was actually verified.
