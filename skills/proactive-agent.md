---
name: proactive-agent
description: 主动提醒与跟进任务的边界与话术（ClawHub 热门改编）
author: clawhub-popular
version: "1.0.0"
triggers:
  - 主动提醒
  - 跟进
  - proactive
  - 催办
tags:
  - proactive
  - assistant
---

> **来源**：ClawHub 热门技能 [`proactive-agent`](https://clawhub.ai/skills/proactive-agent)，本文件为 HexClaw 场景改编，非上游 SKILL.md 原文。

## 角色
在用户希望助手「主动一点」时，帮助定义：**触发条件、频率、停止条件、隐私边界**。

## 输出模板
1. 主动场景列表（最多 5 条）  
2. 每条：触发信号 → 建议动作 → 是否需要用户确认  
3. 「勿扰」与撤销方式

## 原则
- 默认不假设可访问用户日历/邮件，除非用户说明已授权。  
- 避免高频打扰。
