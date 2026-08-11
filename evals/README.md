# evals：答疑质量评测集

来自真实开发者答疑（2026-08-11 取样）的脱敏问题集，用于回归验证"Agent + 本知识库"的答疑质量：改了 AGENTS.md、索引或 dkdoc 之后跑一轮，对比历史成绩，防止优化退化。

## 文件

| 文件 | 说明 |
|---|---|
| `questions.jsonl` | 36 题。`set=core`（12 题，带库内 key_points 与 ref_docs，可精确判卷）+ `set=extended`（24 题，仅问题与参考难度）。`ref_grade` 是当时线上另一套助理的人工分级（A准确完整/B基本可用/C部分偏差/D未有效回答），作难度参照，不是标准答案 |
| `run_opencode.sh` | 用 opencode 逐题答题 → `runs/<日期>/`。含三条踩坑经验（前台管道/--pure/cwd=库根），换其它 Agent CLI 时同理 |
| `judge_prompt.md` | 判卷提示词模板 + 历史教训 |
| `runs/` | 各轮回答与判卷的本地留档（已 gitignore，不入库；每轮成绩摘要写进 RESULTS.md 入库） |
| `RESULTS.md` | 各轮成绩摘要（日期/被测组合/评级分布/主要失败模式/由此做的修改） |

## 脱敏口径

只保留问题文本与人工分级；提问者、提问时间、群名、原始回答（含人名）一律不入库。新增题目时同样只入这两样，入库前跑一遍 PII 检查（手机号/整段ID/人名）。

## 怎么跑一轮

```bash
evals/run_opencode.sh            # core 12 题（默认）
evals/run_opencode.sh all        # 36 题全量
evals/run_opencode.sh - q024     # 指定题
# 然后按 judge_prompt.md 判卷，把摘要追加进 RESULTS.md
```

## 怎么扩充

从新的答疑记录里挑题 → 脱敏 → 追加进 `questions.jsonl`（extended）；反复出现的题型补进 core 并写 key_points（要点必须引库内文件+行号，写之前先核原文——见 judge_prompt.md 的历史教训）。
