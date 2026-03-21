---
name: tavily-search
description: 使用 Tavily API 做面向 AI 的网页检索摘要（ClawHub 热门改编）
author: clawhub-popular
version: "1.0.0"
triggers:
  - Tavily
  - 联网搜索
  - web search
  - 检索
tags:
  - search
  - api
  - tavily
---

> **来源**：ClawHub 热门技能 [`tavily-search`](https://clawhub.ai/skills/tavily-search)，本文件为 HexClaw 场景改编，非上游 SKILL.md 原文。

## 角色
指导用户通过 **Tavily**（或同类搜索 API）获取适合注入 LLM 的简洁检索结果。

## 流程
1. 将用户问题改写为 1–3 条搜索查询。
2. 说明应使用的 API 字段（如 `query`、`search_depth`、`include_answer` 等）及推荐取值。
3. 教用户如何把返回的 `results` 压缩成带引用的要点列表（标题 + 1 句摘要 + URL）。

## 约束
- **不得伪造** API 返回；无密钥时只给集成步骤与环境变量名示例。
- 提醒注意速率限制与费用。
