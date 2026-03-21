# HexClaw Hub — 技能市场数据仓库

**GitHub 仓库名：`hexagon-codes/hexclaw-hub`**（与 HexClaw 引擎仓库 `hexclaw` 分离，单独维护技能内容。）

HexClaw Agent 的在线技能目录。技能以 Markdown 格式定义，通过 YAML frontmatter 描述元数据，正文作为 LLM 系统指令注入上下文。

## 目录结构

```
hexclaw-hub/
├── index.json              # 技能目录索引
├── THIRD_PARTY_CLAWHUB.md  # ClawHub 热门榜改编条目的来源说明
├── skills/                 # 技能文件
│   ├── code-review-pro.md
│   ├── git-commit-craft.md
│   └── ...
└── README.md
```

部分技能为 **ClawHub 公开热门榜** 的 HexClaw 场景改编（非上游 `SKILL.md` 原文），详见 [`THIRD_PARTY_CLAWHUB.md`](./THIRD_PARTY_CLAWHUB.md)。

## 技能格式

```markdown
---
name: my-skill
description: 技能描述
author: author-name
version: "1.0.0"
triggers:
  - 触发词1
  - trigger-word
tags:
  - tag1
  - tag2
---

# 技能标题

详细的 Prompt 指令内容...
```

## 使用方式

在 HexClaw 桌面端的「技能市场」中浏览和安装技能。安装后的技能会在用户消息匹配触发词时自动激活。

引擎默认从本仓库 `main` 分支拉取 `index.json` 与 `skills/*.md`（见 `hexclaw` 中 `skill/hub` 默认 `repo_url`）。

## 分类

| 分类 | 说明 |
|------|------|
| coding | 编程开发 |
| research | 研究调研 |
| writing | 内容写作 |
| data | 数据处理 |
| automation | 自动化 |
| productivity | 效率工具 |
