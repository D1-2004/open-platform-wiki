# Agent 操作手册

## 这是什么

钉钉开放平台文档中心的**离线知识库**：2026-07-07 官方全量快照（8 大类 / 26 子类 / 3781 篇），配三级索引、关系图谱和查询 CLI。你的任务场景：用它回答钉钉开放平台的开发问题——服务端 API、鉴权/免登、机器人、事件订阅、JSAPI、互动卡片、AI 助理、连接平台、错误码、权限点等。

三个前提，先记住再干活：

1. **这是外挂文件夹，不是你的工作区。** 下文用 `$WIKI` 指代本目录绝对路径（`python3 $WIKI/bin/dkdoc where` 可打印），所有命令 cwd 无关。
2. **答疑对本目录只读。** 任何写操作只发生在维护流程里（见文末）。
3. **不需要联网。** 答案在库内找；确实找不到再明确告诉用户"快照未覆盖"。

## 快速开始

```bash
python3 $WIKI/bin/dkdoc find <关键词>...    # 按标题/面包屑/小标题找文档（多词=AND）
python3 $WIKI/bin/dkdoc api 创建群          # 查接口：名称/endpoint/method/权限/新旧版本
python3 $WIKI/bin/dkdoc err invalidDept     # 查错误码；未命中自动转全文兜底
python3 $WIKI/bin/dkdoc event user_add_org  # 按事件名找事件文档
python3 $WIKI/bin/dkdoc perm Contact.User.Read  # 权限点 → 覆盖的接口
python3 $WIKI/bin/dkdoc links <路径|slug>   # 一篇文档的正链与反链
python3 $WIKI/bin/dkdoc cat <路径|slug>     # 打印正文
python3 $WIKI/bin/dkdoc grep '词' [子路径]  # 全文检索兜底
```

## 最佳实践：按问题类型选入口

**从窄到宽，命中即停**，不要一上来全文搜：

| 问题长什么样 | 入口 | 示例 |
|---|---|---|
| 高频主题：token/免登/机器人/事件订阅/卡片/AI 助理… | `$WIKI/index/TOPICS.md` 直达权威文档 | "怎么获取 accessToken" |
| 精确实体：接口名/endpoint/错误码/事件名/权限点 | `dkdoc api / err / event / perm` | "invalidDept 什么意思" |
| 领域盘点："X 都有哪些接口/能力" | `$WIKI/index/INDEX.md` → L2 子类 → L3 功能域清单 | "考勤开放了哪些 API" |
| 模糊描述、不知道术语 | `dkdoc find`（换 2-3 组关键词）| "群里自动发消息那个东西" |
| 存在性问法："是否有/支不支持 X 的接口" | 先 `dkdoc find <能力关键词>` 或 INDEX.md 盘点，按"有哪些/没有哪些"作答 | "知识库正文有接口吗" |
| 以上都没中 | `dkdoc grep`（正文全文） | 报错原文、字段名 |

**追问前必检索**：任何向用户的澄清追问之前，必须先完成至少一轮 `dkdoc find/grep`；确需追问时附上已检索到的候选方向（"知识库管理接口有这些，你问的是正文读写吗"）。单发/非交互场景禁止只反问不作答——反问不答等于没回答。

读到一篇之后的两个扩展动作：

- `dkdoc links <路径>` 看它引用谁（前置概念）、谁引用它（下游用法）；
- 吃不准从哪读起 → `$WIKI/graph/hubs.md`（被引用 Top100 = 事实上的核心页）。

多篇文档说法冲突时的裁决顺序：`updated_at` 新者优先 → 现行版优先于 `⚠归档` → `api.dingtalk.com`（新版）优先于 `oapi.dingtalk.com`（旧版）。

## 找不到怎么办（升级路径，按序执行）

1. **换关键词再 find**：中文换英文 slug（文件名就是官方 URL slug，如 `obtain-user-token`）、全称换缩写、产品名换功能描述。
2. **降到全文**：`dkdoc grep '<报错原文或字段名>'`——错误码数字、JSON 字段名、SDK 方法名往往只在正文里。
3. **查图谱表的盲区说明**：graph 四表是从正文抽取的，没抽全是已知情况（如旧版数字错误码）；`dkdoc err` 未命中会自动兜底，其它表未命中就手动 `grep`。
4. **确认是否抓取盲区**：`$WIKI/meta/UNAVAILABLE.md`（目录存在但正文不可用）与 `meta/failures.json`（抓取失败清单）。
5. **确认是否被裁剪归类**：`◇边缘` 内容（商务/运营/端侧插件/硬件）在库但不在答疑主线，`meta/kb_manifest.jsonl` 的 `tier` 字段可查归层与原因。
6. **仍然没有 → 如实收尾**：明确告诉用户本快照（2026-07-07）未覆盖该问题，建议查线上文档中心，并给出你判断最接近的官方入口链接。**不要编造接口、参数或错误码。**

## 回答纪律

（以下条款来自真实评测的失败模式，每条都有对应的翻车案例，不是套话。）

- **字段语义红线**：凡陈述接口/事件字段的行为——列表顺序、默认值、包含关系、跨事件不变性等隐含语义——必须有文档原文支持，落笔前先 `dkdoc grep <字段名>` 核对；文档没写的行为一律写"文档未说明"，**不得推断补全**。（翻车案例：把"所属部门id列表"补全成"第一个是主部门"。）
- **实体名与 URL 逐字核实**：回答中出现的每个接口/JSAPI/事件/字段/权限点名称，必须先在库内定位到具体文档、逐字复制，禁止凭印象手写；引用 URL 一律取该文档 frontmatter 的 `source_url`，禁止手写或改写命名空间。快照未收录的实体不得给推测名称，要给必须标注"（推测）"。（翻车案例：编出库内不存在的 `biz.chat.chooseConversation`。）
- **参考文档一律用线上链接**：给用户的引用只用 `source_url`（`https://open.dingtalk.com/...`）。本地 `docs/...` 路径、快照文件名（`NNNN-*.md`）、`:行号` 都是检索中间态，**任何一种出现在回答正文或参考列表里都算违规**。回答末尾固定加一节「参考文档」逐条列线上链接。
- **归档三查**：① 引用长度/限额/有效期/QPS 等**数字规格**前，确认所在文档非 `⚠归档`（归档规格常与现行版冲突，冲突时以现行版为准）；② 「参考文档」列表**逐条**标注（归档），不是只在正文首次提及处标；③ dkdoc 输出里的 `⚠归档` 必须透传到回答，并给现行替代。
- **子维度不静默**：用户问题里的每个子维度都要回应；库内没有的子维度显式写"快照（2026-07-07）未见"，不得静默略过，也不得用推断带过。
- **时效声明**：涉及计费、灰度、上线时间等时效敏感问题，声明快照日期 2026-07-07。

**发送前自检**（三条，逐条过）：① 正文与参考列表不含 `docs/` 路径、快照文件名、行号；② 每个数字规格已确认来源非归档；③ 问题的每个子维度都有回应或有"快照未见"声明。

## 怎么做 ingest（更新快照）

只在用户要求更新、或快照明显过时时执行。五步，全程幂等：

```bash
cd $WIKI
python3 ops/scripts/build_dingtalk_open_docs_kb.py <新快照目录>   # 1. 重爬（库外落盘）
python3 ops/scripts/diff_snapshot.py <新快照目录>                 # 2. 按 doc_id 对账，出增/删/改/移报告
python3 ops/scripts/diff_snapshot.py <新快照目录> --apply         # 3. 换入原始层+写 tombstone+全量重建派生层+lint
# 4. 按报告"后续动作"复核 index/TOPICS.md：变更文档命中 TOPICS 或高反链的，改写对应条目
python3 ops/scripts/lint.py && git add -A && git commit           # 5. 体检 + 提交
```

原则、变更决策表（哪类变更动哪层、哪些要人工）、新鲜度验收清单，都在 [ops/INGEST.md](ops/INGEST.md)——执行前先读它。

## 文档是怎么维护的（所有权与纪律）

| 层 | 内容 | 谁改 | 你能不能手改 |
|---|---|---|---|
| 原始层 | `docs/` `meta/documents.jsonl` 等 | 只由 ingest 的 apply 整体换入 | ✗（改了会被下次快照覆盖） |
| 结构层 | `index/`(除 TOPICS) `graph/`(除 GRAPH) `meta/kb_manifest.jsonl` | 脚本全量重建 | ✗（lint 会报漂移） |
| 认知层 | `index/TOPICS.md`、README/AGENTS/CLAUDE、`graph/GRAPH.md`、`ops/scripts/` 内的策展数据（TAB_HINTS/TIER_BY_TAB） | 人 / LLM | ✓ |

- 体检：`python3 $WIKI/ops/scripts/lint.py`（7 项只读检查：结构一致/索引漂移/断链/tombstone）。
- 发现文档内容本身有错：**不改 docs/**，把勘误写进 TOPICS.md 对应主题并注明与官方原文的分歧；根因在上游的去官方渠道反馈。
- 本仓库用 git 管理，每次 ingest 一个 commit，diff 即变更审计日志。
