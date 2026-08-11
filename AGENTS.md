# Agent 协议：怎么用、怎么维护

本目录是**外挂知识库**，不是你的工作区（cwd 通常在别处）。你只需要被告知它的路径——下文用 `$WIKI` 指代本目录绝对路径（`python3 $WIKI/bin/dkdoc where` 可打印）。内容：钉钉开放平台文档中心 2026-07-07 快照（3781 篇）+ 三级索引 + 关系图谱。答疑不需要联网、不需要向量库、不需要任何第三方依赖。

## 一、怎么用（答疑，只读）

### 首选工具：`dkdoc`（零依赖、cwd 无关）

```bash
python3 $WIKI/bin/dkdoc find 免登 小程序      # 按标题/面包屑/小标题找文档
python3 $WIKI/bin/dkdoc api 创建群            # 查接口（名称/endpoint/method/权限/新旧）
python3 $WIKI/bin/dkdoc err invalidDept       # 查错误码（未命中自动全文兜底）
python3 $WIKI/bin/dkdoc event user_add_org    # 按事件名找事件文档
python3 $WIKI/bin/dkdoc perm Contact.User.Read # 权限点 → 覆盖的接口
python3 $WIKI/bin/dkdoc links <路径|slug>     # 正链+反链（读一篇后扩展关联）
python3 $WIKI/bin/dkdoc cat <路径|slug>       # 打印正文
python3 $WIKI/bin/dkdoc grep '关键词' [子路径] # 全文检索兜底
```

### 按问题类型选入口

1. **高频主题**（token/免登/机器人/事件订阅/卡片/AI 助理…）→ 读 `$WIKI/index/TOPICS.md`，直达权威文档。
2. **精确实体**（接口/错误码/事件名/权限点）→ `dkdoc api|err|event|perm`；手写 jq 配方见 `$WIKI/graph/GRAPH.md`。
3. **领域浏览**（"考勤都有哪些接口"）→ `$WIKI/index/INDEX.md`（L1）→ 子类 L2 → 功能域 L3 清单。
4. **兜底** → `dkdoc find` / `dkdoc grep`；仍无 → 查 `$WIKI/meta/UNAVAILABLE.md` 与 `meta/failures.json` 确认是否抓取盲区，如是要向用户明说。
5. **读到一篇要扩展** → `dkdoc links` 看它引用谁/谁引用它；不知从哪读起看 `$WIKI/graph/hubs.md`。

### 回答纪律

- **参考文档一律用线上链接**：最终回答里引用/罗列参考文档时，直接给该篇的 `source_url`（`https://open.dingtalk.com/...`，每篇文档 frontmatter、正文 `> Source:` 行和 dkdoc 输出里都有）。本地 `docs/...` 路径只是你自己的检索中间态，**不允许出现在给用户的回答里**。建议回答末尾固定加一节「参考文档」，逐条列线上链接。
- **新旧冲突**：同主题多篇以 `updated_at` 新者为准；`api.dingtalk.com`（新版）优先于 `oapi.dingtalk.com`（旧版）。
- **归档内容**：带 `⚠归档` / `archived: true` / 路径含「历史文档（不推荐）」→ 必须提示不推荐并优先给现行替代。
- **时效**：这是 2026-07-07 静态快照，涉及计费/灰度/上线时间等问题要声明快照日期。
- `◇边缘` 标记（商务/运营/端侧/硬件）在库但非开发答疑主线。

## 二、怎么维护（写操作，走协议）

- **何时**：快照过时需更新、用户要求 ingest 新快照、lint 报漂移。日常答疑**永远不要**写这个目录。
- **怎么做**：一切维护走 [ops/INGEST.md](ops/INGEST.md)（重爬 → `diff_snapshot.py` 按 doc_id 对账 → `--apply` 全量重建派生层 → 复核 TOPICS.md → `lint.py`）。所有脚本幂等，cwd 无关。
- **分层纪律**：`docs/`+`meta/` 是上游镜像（改了会被下次 apply 覆盖）；`index/`（TOPICS.md 除外）、`graph/`（GRAPH.md 除外）、`meta/kb_manifest.jsonl` 是生成物（手改会被 lint 报漂移）。**可以手改的只有**：`index/TOPICS.md`、各入口说明文件、`ops/scripts/` 里的生成器（改 TAB_HINTS/TIER_BY_TAB 等策展数据）。
- **体检**：`python3 $WIKI/ops/scripts/lint.py`（只读，7 项检查）。
