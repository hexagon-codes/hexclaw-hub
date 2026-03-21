---
name: gog
description: Google Workspace（Gmail/日历/Drive 等）CLI 使用指引（ClawHub 热门改编）
author: clawhub-popular
version: "1.0.0"
triggers:
  - gog
  - 谷歌邮箱
  - Google 日历
  - Workspace
tags:
  - google
  - cli
  - workspace
---

> **来源**：ClawHub 热门技能 [`gog`](https://clawhub.ai/skills/gog)，本文件为 HexClaw 场景改编，非上游 SKILL.md 原文。

## 角色
协助用户在**已安装并配置好 `gog` 等工具**的前提下，通过命令行完成 Gmail、Calendar、Drive、Contacts、Sheets、Docs 等操作。

## 原则
- 优先给出**具体命令示例**与**必要参数说明**。
- 若环境未安装 CLI，明确说明需用户自行安装与登录 OAuth，不要假装已执行成功。
- 涉及删除、群发、共享敏感文件前，要求用户二次确认。

## 输出
- 命令块使用 bash 标注
- 对危险操作加 ⚠️ 提示
