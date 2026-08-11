# 变更维护协议（ingest 与所有权）

> 答疑 Agent 不需要读本文件。本文件面向被明确要求维护本库的人/Agent。

## 所有权速查：什么能改，什么不能

| 层 | 内容 | 谁改 |
|---|---|---|
| 原始层 | `docs/`、`meta/documents.jsonl` 等 | 只由 ingest 的 `--apply` 整体换入，手改会被下次快照覆盖 |
| 结构层 | `index/`（除 TOPICS.md）、`graph/`（除 GRAPH.md）、`meta/kb_manifest.jsonl` | 脚本全量重建，手改会被 lint 报漂移 |
| 认知层 | `index/TOPICS.md`、README/AGENTS/CLAUDE、`graph/GRAPH.md`、`ops/scripts/` 内策展数据（TAB_HINTS/TIER_BY_TAB）、`evals/` | 人 / LLM 手改 |

改完 AGENTS.md/索引/dkdoc 后跑 `evals/run_opencode.sh` 做质量回归（见 [../evals/README.md](../evals/README.md)），对照 `evals/RESULTS.md` 防退化；结构一致性用 `lint.py`。

设计沿用 llm-wiki 范式的生命周期合同（dongxiang-workspace `wiki/concepts/llm-wiki-pattern.md`，2026-08-07/08-10 结论），针对"上游是可全量重爬的官方文档站"做了简化：**结构层不需要 LLM 增量编译，全量脚本重建即可；LLM 只维护认知层一页（TOPICS.md）。**

## 五条原则

1. **稳定身份**：文档身份 = `doc_id`（钉钉文档树 ID），`source_url` 只是 provenance。改名、挪目录、换 URL 都不算新文档。
2. **add / update / delete 全生命周期**：变更判定用 `html_sha256` 内容指纹；**删除不是静默消失**——写入 `meta/tombstones.jsonl` 留档，"旧知识不可再答"变成可追踪事件。
3. **全量对账，不做增量修补**：`index/`、`graph/`、`meta/kb_manifest.jsonl` 全部是派生物，每次 ingest 由脚本从头重建（幂等、确定性输出）。增量修补必然漂移，全量重建 10 秒内跑完，没有理由增量。
4. **关系级重编译**：一篇文档变更/下线，影响不止它自己。用 `graph/links.jsonl` 反查引用方、`rg <path> index/TOPICS.md` 查认知层命中，凡命中都要复核。
5. **新鲜度验收**：ingest 完成的标准不是"跑完了"，而是"新增可答、下线不可答、冲突显式"（见下方验收清单）。

## 常规更新流程

```bash
cd open-platform-wiki

# 1) 重跑爬虫，产出新快照目录（在库外，如 ~/Downloads/dingtalk-open-platform-docs-<date>）
python3 ops/scripts/build_dingtalk_open_docs_kb.py <新快照目录>

# 2) 按 doc_id 对账，先预览（只出报告，不动本库）
python3 ops/scripts/diff_snapshot.py <新快照目录>
#    → ops/changes/<date>-<label>.md：新增/更新/移动/删除四张清单

# 3) 应用：换入原始层 + 写 tombstone + 全量重建派生层 + lint
python3 ops/scripts/diff_snapshot.py <新快照目录> --apply

# 4) 认知层复核（唯一需要 LLM/人的步骤）：
#    对照对账报告，反查每条变更是否命中 TOPICS.md 或高入度枢纽：
#      rg -F "<变更文档路径>" index/TOPICS.md
#      jq -c 'select(.to=="<变更文档路径>")' graph/links.jsonl
#    命中则复核/改写对应主题条目，并更新 TOPICS.md 头部的「最后复核」日期。

# 5) 体检 + 提交（建议本库用 git 管理：diff 天然暴露每次快照的增删改）
python3 ops/scripts/lint.py
git add -A && git commit -m "ingest: snapshot <date>"
```

## 决策表：什么变更动哪些层

| 对账报告里出现 | 原始层 | 结构层 | 认知层（TOPICS.md） |
|---|---|---|---|
| 新增文档 | apply 自动换入 | 自动重建（进 L2/L3 与图谱） | 属高频主题才加条目（纪律：只收会饱和的主题） |
| 内容更新 | 自动 | 自动 | 反查命中才复核 |
| 目录移动 | 自动 | 自动（索引行自动跟随） | 反查命中则改链接 |
| 删除 | 自动 + tombstone | 自动（索引/图谱中消失） | **必查**：命中过的条目要改写或删除 |
| 新大类/新 tab 出现 | 自动 | 重建能跑，但要补两处人工归类：`build_index.py` 的 `TAB_HINTS`（路由提示）、`compile_qa_kb.py` 的 `TIER_BY_TAB`（答疑分层） | 视重要性加主题 |
| 某 tab 篇数暴涨 | — | 超过 200 篇会自动按功能域拆 L3，无需干预 | — |

## 验收清单（新鲜度 eval）

- [ ] `lint.py` 通过（结构一致、索引零漂移、入口无断链、tombstone 无复活）
- [ ] 抽 1-2 篇**新增**文档提问，能沿 索引/图谱 找到并回答
- [ ] 抽 1 篇**删除**文档提问，回答会声明已下线（tombstone 可查到下线时间）而不是沉默或答旧内容
- [ ] 对账报告已入 `ops/changes/`，TOPICS.md「最后复核」日期已更新

## 手工修正的例外通道

发现某篇文档内容错误想修：**不要改 docs/**（那是上游镜像，下次 apply 会被覆盖）。正确姿势：把勘误写进 TOPICS.md 对应主题（或单独的勘误段），注明与官方原文的分歧；根因在上游的，去官方渠道反馈。
