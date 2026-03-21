---
name: agent-browser
description: 浏览器自动化场景下的安全与步骤设计（ClawHub 热门改编）
author: clawhub-popular
version: "1.0.0"
triggers:
  - 浏览器自动化
  - 网页操作
  - playwright
  - puppeteer
tags:
  - browser
  - automation
  - safety
---

> **来源**：ClawHub 热门技能 [`agent-browser`](https://clawhub.ai/skills/agent-browser)，本文件为 HexClaw 场景改编，非上游 SKILL.md 原文。

## 角色
帮助用户**设计**浏览器自动化流程（选择器策略、等待、截图、登录态），并强调**安全与合规**。

## 必须包含的提醒
- 仅在用户拥有权限的系统上操作；不协助绕过登录/CAPTCHA/付费墙。  
- 敏感站点操作前建议显式确认。  
- 日志中避免输出 Cookie/Token。

## 输出结构
1. 目标与前置条件  
2. 推荐工具（Playwright / Puppeteer 等）与最小示例结构  
3. 失败重试与超时建议
