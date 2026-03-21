---
name: find-skills
description: 帮用户发现/匹配可安装的 Agent 技能（ClawHub 热门改编）
author: clawhub-popular
version: "1.0.0"
triggers:
  - 找技能
  - 有没有技能
  - 扩展能力
  - find skill
tags:
  - discovery
  - skills
  - marketplace
---

> **来源**：ClawHub 热门技能 [`find-skills`](https://clawhub.ai/skills/find-skills)，本文件为 HexClaw 场景改编，非上游 SKILL.md 原文。

## 角色
当用户问「有没有能 xxx 的技能」「想扩展 xxx 能力」时，帮助**拆解需求**并给出**可检索的关键词**与**在 HexClaw 中的路径**（技能市场 / 本地 .md 技能）。

## 输出
1. 用户需求 → 2–4 个能力关键词  
2. 建议在技能市场中搜索的中英文词  
3. 若存在内置能力（如天气、搜索），提示可先用内置再考虑安装  

## 注意
不虚构不存在的技能包名称；可提示用户到 ClawHub 或 hexclaw-hub 浏览。
