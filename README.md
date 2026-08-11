# 钉钉开放平台 Wiki（Agent 优先）

钉钉开放平台文档中心的完整快照（2026-07-07 抓取，8 大类 / 26 子类 / 3781 篇 Markdown），加上为 Agent 文件系统检索设计的三级索引、类型化关系图谱和可持续的变更维护协议。**拿到这个文件夹即可开始技术答疑，无需联网、无需向量库。**

**用法定位：外挂文件夹**。本目录不是 Agent 的工作区（cwd），而是挂给任意 Agent 的知识库。唯一接入方式就是一句话：

> 钉钉开放平台知识库在 `<本目录绝对路径>`，先读其中 AGENTS.md，再回答我的问题。

Agent 读完 [AGENTS.md](AGENTS.md) 即掌握全部用法，包括随附的零依赖查询 CLI：`python3 <路径>/bin/dkdoc find|api|err|event|perm|links|cat|grep ...`（cwd 无关）。

## 三层结构

| 层 | 位置 | 谁维护 | 纪律 |
|---|---|---|---|
| 原始层（事实源镜像） | `docs/` `meta/` | 爬虫（重跑快照整体换入） | 只读。以 `doc_id` 为稳定身份，删除留 tombstone |
| 结构层（派生索引） | `index/`（除 TOPICS.md）`graph/` | 脚本全量重建 | 生成物勿手改，改了会被覆盖且 lint 报漂移 |
| 认知层（人工策展） | `index/TOPICS.md` | 人 / LLM | 只收会饱和的高频主题，快照更新后复核 |

## 渐进式披露：从粗到细四条路

1. **高频主题**（多数答疑到此为止）→ [index/TOPICS.md](index/TOPICS.md)
2. **精确实体**：接口名/错误码/事件名/权限点 → `graph/` 五张 JSONL 边表（[graph/GRAPH.md](graph/GRAPH.md) 有查询配方）
3. **按领域浏览** → [index/INDEX.md](index/INDEX.md)（L1 总索引）→ 子类 L2 → 大类目按功能域拆的 L3
4. **兜底全文检索** → `rg "关键词" docs/`

## 目录

```
README.md AGENTS.md CLAUDE.md 入口与 Agent 协议（怎么用 + 怎么维护）
bin/dkdoc                   查询 CLI：find/api/err/event/perm/links/cat/grep（python3 标准库，无依赖）
index/                      L1 INDEX.md → L2 子类 → L3 功能域（107 个生成文件）+ TOPICS.md（认知层）
graph/                      links/api/event/errcode/permission 五张边表 + hubs.md 枢纽榜 + GRAPH.md
docs/                       3781 篇正文快照，每篇头部有 source_url/breadcrumb/updated_at 元数据
meta/                       documents.jsonl（逐篇索引+sha256）kb_manifest.jsonl（答疑分层 T0/T1/T2/DROP）
                            source_manifest.json（快照信息）tombstones.jsonl（下线留档）UNAVAILABLE.md
ops/                        INGEST.md（变更维护协议）changes/（对账报告）scripts/（爬虫+全部生成器+lint）
```

## 维护

快照会过时（抓取于 2026-07-07）。更新流程一页纸：[ops/INGEST.md](ops/INGEST.md)——重跑爬虫出新快照 → `diff_snapshot.py` 按 `doc_id` 对账（增/删/改/移清单）→ `--apply` 换入原始层并全量重建派生层 → 复核 TOPICS.md → `lint.py` 体检。所有脚本幂等，随时可全量重跑。
