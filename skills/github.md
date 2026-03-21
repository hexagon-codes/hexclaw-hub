---
name: github
description: 使用 GitHub CLI `gh` 处理 issue/PR/Actions/API（ClawHub 热门改编）
author: clawhub-popular
version: "1.0.0"
triggers:
  - gh 
  - GitHub PR
  - 提 issue
  - Actions
tags:
  - github
  - cli
  - gh
---

> **来源**：ClawHub 热门技能 [`github`](https://clawhub.ai/skills/github)，本文件为 HexClaw 场景改编，非上游 SKILL.md 原文。

## 角色
在用户已安装 `gh` 且完成 `gh auth login` 的前提下，协助编写 **gh** 子命令与查询。

## 常用模式
- Issues：`gh issue list/create/view/comment`
- PRs：`gh pr list/create/diff/checkout`
- Actions：`gh run list/watch`
- 高级：`gh api` + GraphQL/REST 路径

## 输出
- 直接可复制的命令  
- 说明需替换的占位符（owner/repo/编号）  
- 对 `--json` 过滤给简单 jq 示例（可选）
