# HexClaw Hub — 技能 & MCP 市场

**GitHub 仓库名：`hexagon-codes/hexclaw-hub`**（与 HexClaw 引擎仓库 `hexclaw` 分离，单独维护市场内容。）

HexClaw Agent 的在线技能目录和 MCP 服务器市场。

- **技能 (Skills)**：以 Markdown 格式定义，通过 YAML frontmatter 描述元数据，正文作为 LLM 系统指令注入上下文
- **MCP 服务器**：以 JSON 格式定义，包含安装命令、参数、环境变量等，支持一键安装

当前仓库已收录 **78** 个技能条目 + **59** 个 MCP 服务器，按已登记的改编来源分为三组：

| 来源 | 数量 | 说明 |
|------|------|------|
| 其他市场维护条目 | 59 | 除下列两组改编外的技能定义与资源包 |
| ClawHub 热门改编 | 12 | 参考 ClawHub 热门榜公开条目，按 HexClaw 场景重写 |
| OpenClaw / playbooks 改编 | 7 | 参考 OpenClaw Skills / playbooks 公开条目，按 HexClaw 场景重写 |

第三方改编条目的来源说明见 [`THIRD_PARTY_CLAWHUB.md`](./THIRD_PARTY_CLAWHUB.md)。

## 目录结构

```text
hexclaw-hub/
├── index.json              # 技能目录索引 (78 skills)
├── mcp-registry.json       # MCP 服务器市场 (59 servers)
├── THIRD_PARTY_CLAWHUB.md  # ClawHub 热门榜改编条目的来源说明
├── skills/                 # 技能文件
│   ├── code-review-pro.md
│   ├── openclaw-agent-browser.md
│   ├── tavily-search-pro.md
│   ├── homework-pdf/        # 含模板、Schema 和示例的目录包
│   │   ├── SKILL.md
│   │   ├── bundle.json
│   │   └── assets/
│   └── ...
└── README.md
```

## MCP 服务器市场

`mcp-registry.json` 收录了 59 个 MCP 服务器，涵盖 21 个分类。所有可执行条目必须固定精确包版本和官方 registry 完整性；当前 49 个为 `pinned`，10 个上游包已不存在并标为 `quarantined`，隔离条目不得进入安装/执行链。

| 分类 | 服务器 |
|------|--------|
| 推理增强 | Sequential Thinking |
| 系统工具 | Filesystem, Everything |
| 开发工具 | GitHub, GitLab, Git, Postman |
| 搜索引擎 | Brave Search, DuckDuckGo, Exa Search, Tavily Search, Wikipedia |
| 网页工具 | Fetch, Firecrawl |
| 文档查询 | Context7 |
| 自动化 | Playwright, Puppeteer |
| 数据库 | SQLite, PostgreSQL, MySQL, Redis, MongoDB |
| 记忆存储 | Memory (Knowledge Graph) |
| 通讯协作 | Slack, Discord, Telegram, Email |
| 效率工具 | Notion, Linear, Jira, Obsidian, Google Drive, Hugging Face |
| 办公文档 | Excel, MarkItDown, Pandoc |
| 运维部署 | Docker, Kubernetes, Cloudflare, Vercel |
| 监控告警 | Sentry |
| 云服务 | AWS |
| 金融支付 | Stripe, 老虎证券 (Tiger), 富途牛牛 (Futu) |
| 地图定位 | Google Maps |
| 媒体内容 | YouTube |
| 实用工具 | Time, 天气 (Open-Meteo), 汇率 (Frankfurter) |
| 汽车出行 | Car Database, Car Price (FIPE), Vehicle Diagnostics |
| 视频制作 | Video & Audio Editor, FFmpeg Video Processor |
| 教育学习 | Wolfram Alpha, Math Operations, Educational Tutor, Anki |

数据来源：[Smithery.ai](https://smithery.ai) 热门排行 + [mcp.so](https://mcp.so) + [Glama.ai](https://glama.ai/mcp/servers) + [MCP 官方参考实现](https://github.com/modelcontextprotocol/servers)。

## 仓库约定

- `skills/*.md` 是单个技能的定义文件，frontmatter 用于市场元数据，正文用于运行时系统提示词。
- `skills/<name>/SKILL.md` 是目录包的技能定义，同目录的 `bundle.json` 固定模板、Schema、示例等资源的路径、大小和摘要。
- `index.json` 是客户端拉取的技能目录索引，需和单文件或目录包定义中的名称、版本、分类保持一致。目录包同时提供 `bundle_sha256`，按资源清单的确定性 JSON 计算。
- `THIRD_PARTY_CLAWHUB.md` 记录所有第三方改编条目的来源页面、slug 与作者信息。

HexClaw 引擎只应从发布 BOM 固定的不可变 tag/commit 拉取索引、技能定义及目录包资源，禁止使用浮动 `main`。可用标签以仓库 Tags 为准，运行时版本以应用发布 BOM 为准；工作树内容需在新 tag 发布并同步 BOM 后才可成为远程默认源。目录包需要宿主支持完整资源安装与加载，Hub 发版本身不代表应用已启用新版教学报告。

### MCP 供应链约束

- `status=pinned` 才允许安装；`status=quarantined` 必须带 `quarantine_reason`，运行时 fail-closed。
- npm 参数必须绑定 `package@exact-version`，并记录官方 registry 返回的 SHA-512 SRI。
- PyPI 参数必须绑定 `package==exact-version`，并记录官方 release SHA-256。
- `artifact` 只证明包身份和内容完整性，不代表代码已经安全审计；运行时仍必须使用最小环境、文件 capability 和受控网络出口。
- 修改 registry 后必须运行 `python3 scripts/validate-mcp-registry.py`，并同步 HexClaw 的 embedded registry；普通测试不得自动更新 lock 或 golden。

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
- 目录包的 `name` 与目录名、`bundle.json` 的 `skill_id` 一致；`file` 指向 `skills/<name>/SKILL.md`。索引中的 `sha256/size` 对应该定义文件，`bundle_sha256` 对应整个包清单的语义摘要。
- `version` 更新时，同时同步技能文件 frontmatter。
- `category` 只能使用仓库定义的标准分类。
- `description` 应与技能正文能力范围一致，避免市场描述和实际提示词脱节。

## 使用方式

在 HexClaw 桌面端的「技能市场」中浏览和安装技能。安装后的技能会在用户消息匹配触发词时自动激活。

## 分类

| 分类 | 数量 | 说明 |
|------|------|------|
| coding | 7 | 编程开发 |
| research | 6 | 研究调研 |
| writing | 6 | 内容写作 |
| data | 4 | 数据处理 |
| automation | 6 | 自动化 |
| productivity | 16 | 效率工具 |
| education | 26 | 教育辅导 |
| automotive | 2 | 汽车出行 |
| media | 5 | 媒体制作 |

## 维护流程

新增或更新技能时，按下面顺序维护：

1. 新增或修改 `skills/<name>.md`，或 `skills/<name>/SKILL.md` 目录包，保证 frontmatter 完整。
2. 目录包资源修改后，同步 `bundle.json` 中的大小和 SHA-256。清单不包含自身，身份与版本须和 `SKILL.md` 一致；包摘要遵循包内合同。
3. 运行 `python3 scripts/generate-index.py`，由 frontmatter 重新生成 `index.json`。生成器核对目录包资源后输出 `bundle_sha256`，资源不匹配时停止生成。
4. 如果是第三方改编技能，在 [`THIRD_PARTY_CLAWHUB.md`](./THIRD_PARTY_CLAWHUB.md) 中补来源信息。
5. 提交前检查文件名或目录名、frontmatter `name`、`index.json` `name`，以及目录包身份完全一致。
