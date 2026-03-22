# HexClaw Hub — 技能市场数据仓库

**GitHub 仓库名：`hexagon-codes/hexclaw-hub`**（与 HexClaw 引擎仓库 `hexclaw` 分离，单独维护技能内容。）

HexClaw Agent 的在线技能目录。技能以 Markdown 格式定义，通过 YAML frontmatter 描述元数据，正文作为 LLM 系统指令注入上下文。

当前仓库已收录 **37** 个技能条目，包含三类来源：

| 来源 | 数量 | 说明 |
|------|------|------|
| 原生条目 | 18 | 直接为 HexClaw 技能市场维护的技能 |
| ClawHub 热门改编 | 12 | 参考 ClawHub 热门榜公开条目，按 HexClaw 场景重写 |
| OpenClaw / playbooks 改编 | 7 | 参考 OpenClaw Skills / playbooks 公开条目，按 HexClaw 场景重写 |

第三方改编条目的来源说明见 [`THIRD_PARTY_CLAWHUB.md`](./THIRD_PARTY_CLAWHUB.md)。

## 目录结构

```text
hexclaw-hub/
├── index.json              # 技能目录索引
├── THIRD_PARTY_CLAWHUB.md  # ClawHub 热门榜改编条目的来源说明
├── skills/                 # 技能文件
│   ├── code-review-pro.md
│   ├── openclaw-agent-browser.md
│   ├── tavily-search-pro.md
│   └── ...
└── README.md
```

## 仓库约定

- `skills/*.md` 是单个技能的定义文件，frontmatter 用于市场元数据，正文用于运行时系统提示词。
- `index.json` 是客户端拉取的技能目录索引，需和 `skills/*.md` 中的名称、版本、分类保持一致。
- `THIRD_PARTY_CLAWHUB.md` 记录所有第三方改编条目的来源页面、slug 与作者信息。

HexClaw 引擎默认从本仓库 `main` 分支拉取 `index.json` 与 `skills/*.md`（见 `hexclaw` 中 `skill/hub` 默认 `repo_url`）。

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

## 索引字段

`index.json` 中每个技能条目使用统一结构，供技能市场列表、搜索和详情页消费：

```json
{
  "name": "code-review-pro",
  "display_name": "Code Review Pro",
  "description": "自动化代码审查...",
  "version": "2.1.0",
  "author": "openclaw",
  "category": "coding",
  "tags": ["code-review", "security", "lint"],
  "downloads": 28430,
  "rating": 4.8
}
```

建议保持以下一致性：

- `name` 必须与技能文件名和 frontmatter 中的 `name` 一致。
- `version` 更新时，同时同步技能文件 frontmatter。
- `category` 只能使用仓库定义的标准分类。
- `description` 应与技能正文能力范围一致，避免市场描述和实际提示词脱节。

## 使用方式

在 HexClaw 桌面端的「技能市场」中浏览和安装技能。安装后的技能会在用户消息匹配触发词时自动激活。

## 分类

| 分类 | 数量 | 说明 |
|------|------|------|
| coding | 4 | 编程开发 |
| research | 6 | 研究调研 |
| writing | 6 | 内容写作 |
| data | 4 | 数据处理 |
| automation | 6 | 自动化 |
| productivity | 11 | 效率工具 |

## 维护流程

新增或更新技能时，按下面顺序维护：

1. 在 `skills/` 下新增或修改对应的 `.md` 文件，保证 frontmatter 完整。
2. 同步更新 `index.json` 中的元数据、`version` 和 `updated_at`。
3. 如果是第三方改编技能，在 [`THIRD_PARTY_CLAWHUB.md`](./THIRD_PARTY_CLAWHUB.md) 中补来源信息。
4. 提交前检查技能文件名、frontmatter `name`、`index.json` `name` 三者完全一致。
