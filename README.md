# ClawHub - HexClaw 技能市场

HexClaw Agent 的在线技能仓库。技能以 Markdown 格式定义，通过 YAML frontmatter 描述元数据，正文作为 LLM 系统指令注入上下文。

## 目录结构

```
clawhub/
├── index.json          # 技能目录索引
├── skills/             # 技能文件
│   ├── code-review-pro.md
│   ├── git-commit-craft.md
│   └── ...
└── README.md
```

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

## 分类

| 分类 | 说明 |
|------|------|
| coding | 编程开发 |
| research | 研究调研 |
| writing | 内容写作 |
| data | 数据处理 |
| automation | 自动化 |
| productivity | 效率工具 |
