---
name: notion
description: Notion 页面/数据库与 API 集成思路（ClawHub 热门改编）
author: clawhub-popular
version: "1.0.0"
triggers:
  - Notion
  - 笔记数据库
  - notion api
tags:
  - notion
  - docs
  - api
---

> **来源**：ClawHub 热门技能 [`notion`](https://clawhub.ai/skills/notion)，本文件为 HexClaw 场景改编，非上游 SKILL.md 原文。

## 角色
帮助用户用 **Notion API** 或官方集成完成：页面创建、数据库查询、模板化写入。

## 步骤
1. 确认 Integration Token 与页面/数据库已共享给集成。  
2. 选择 REST 端点（`/pages`、`/databases/{id}/query` 等）。  
3. 给出最小 `curl` 或伪代码示例与 JSON 属性结构提示。

## 约束
- 不索要或存储用户 Token；用占位符。  
- 大页面注意分页 `start_cursor`。
