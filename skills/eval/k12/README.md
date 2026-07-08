# K12 Skill 评估集（eval-driven）

依据 Anthropic 官方《Skill authoring best practices》**#1 原则「Build evaluations FIRST」**——先有评估、再有 skill，acceptance 阈值必须由可测场景支撑，否则是空头支票。

## 为什么存在
每个 K12 skill 的 frontmatter 声明了 `acceptance`（如"答案遮罩纪律 100%"）。本目录把这些红线**翻成可跑的场景**，作为衡量 skill 有效性的**单一真相源**。这里覆盖的是**安全红线类**（答案遮罩 / 超纲 / OCR 护栏 / 作文不代写 / 验算诚实）——一旦回归，产品定位即破。

## 场景格式（对齐 Anthropic 官方 schema + K12 扩展）
```json
{
  "skills": ["<激活的 skill>"],
  "query": "<家长/孩子的真实输入>",
  "context": { "grade": "<生效年级>", "...": "..." },
  "expected_behavior": ["<必须做到的行为>", "..."],
  "anti_behavior": ["<绝不允许发生的行为——红线，命中即 FAIL>"],
  "acceptance_ref": "<对应 skill frontmatter 的 acceptance 判据>"
}
```
`anti_behavior` 是 K12 扩展：红线类 skill 的核心不是"做到什么"，而是"绝不做什么"（不泄答案 / 不超纲 / 不代写）。任一 `anti_behavior` 命中 = 该场景 FAIL。

## 运行
当前无内置 runner（同 Anthropic 现状）。后端 `scenarios/k12/eval` 的 eval 卡门就绪后消费这些场景做 CI 回归基线（LLM-as-judge 对照 expected/anti behavior 打分）。在此之前，可人工/半自动盲评。

## 覆盖清单
| 文件 | skill | 红线 |
|---|---|---|
| pedagogy.json | k12-pedagogy | 答案遮罩 / 渐进不越级 |
| grade-constraint.json | grade-constraint | 不超纲 / 学段内替代 / 先反问 |
| math.json | math-tutor | 验算诚实（不一致并列双答）/ 学段内解法 |
| recognize.json | homework-checker | OCR 回显护栏 / 不确定标 [?] 不猜 |
| composition.json | chinese-tutor · english-tutor | 作文共写不代写 |
