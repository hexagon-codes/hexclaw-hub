---
name: clawhub-weather
description: 天气查询与出行提示（ClawHub 热门改编，可与内置天气能力并存）
author: clawhub-popular
version: "1.0.0"
triggers:
  - 天气
  - 气温
  - weather
  - forecast
tags:
  - weather
  - outdoor
---

> **来源**：ClawHub 热门技能 [`weather`](https://clawhub.ai/skills/weather)（内置 skill 名为 weather，故本条目改名为 clawhub-weather），本文件为 HexClaw 场景改编，非上游 SKILL.md 原文。

## 角色
提供清晰、**可核对来源**的天气与出行提示。若系统已有内置天气工具，可建议用户优先使用自动查询。

## 输出
- 地点 + 时段 + 温度/降水/风（若数据可得）  
- 简短穿衣/出行建议  
- 说明数据为第三方公共服务，极端天气以当地预警为准
