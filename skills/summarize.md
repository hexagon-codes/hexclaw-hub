---
name: summarize
description: 总结网页、PDF、音视频等的流程与提示词模板（ClawHub 热门改编）
author: clawhub-popular
version: "1.0.0"
triggers:
  - 总结链接
  - 摘要
  - summarize
  - 长文压缩
tags:
  - summary
  - url
  - cli
---

> **来源**：ClawHub 热门技能 [`summarize`](https://clawhub.ai/skills/summarize)，本文件为 HexClaw 场景改编，非上游 SKILL.md 原文。

## 角色
帮助用户用 **summarize 类 CLI/服务**（或手动复制正文）对 URL、PDF、图片、音频、YouTube 等做高质量摘要。

## 步骤建议
1. 确认输入类型与是否可合法访问。  
2. 选择策略：抽取大纲 / 一页纸执行摘要 / 技术文档 API 级摘要。  
3. 输出：要点列表 + 关键引用位置（时间戳/页码/章节标题占位）。

## 约束
- 受版权保护的全文勿要求绕过付费墙。  
- 对音视频说明需先转写再摘要（若用户无转写工具则给工具链建议）。
