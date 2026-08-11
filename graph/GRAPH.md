# 关系图谱说明

轻量图谱 = 五张 JSONL 边表 + 一张枢纽榜。节点是文档（以仓内相对路径 `docs/...` 标识，稳定身份是 meta/documents.jsonl 里的 `doc_id`），边是下面五种类型化关系。没有图数据库：`jq`/`rg` 就是查询引擎。

| 文件 | 边类型 | 规模 | 生成器 |
|---|---|---|---|
| `links.jsonl` | 文档 →引用→ 文档（站内互链） | ~8100 条 | ops/scripts/build_links.py |
| `api.jsonl` | 文档 →描述→ API endpoint（含 method/权限点/应用类型/新旧版本/归档标记） | 1337 接口 | ops/scripts/build_qa_index.py |
| `event.jsonl` | 文档 →定义→ 事件类型（event_types 数组） | 185 篇带标识 | 同上 |
| `errcode.jsonl` | 错误码 →解释于→ 文档（全局错误码大表逐条展开） | 2515 条 | 同上 |
| `permission.jsonl` | 权限点 →覆盖→ API 列表（官方权限映射文档是空壳，此表补齐） | 244 权限点 | 同上 |
| `hubs.md` | 被引用 Top 100 文档（入度榜） | — | build_links.py |

## 查询配方

```bash
cd <本库根目录>

# 按关键词找接口（标题/endpoint 都能命中）
jq -c 'select(.title|test("创建群"))' graph/api.jsonl
jq -c 'select(.endpoint|test("v1.0/oauth2"))' graph/api.jsonl
# 只要现行版（排除历史归档）
jq -c 'select(.archived==false and (.title|test("考勤")))' graph/api.jsonl

# 错误码排查（答疑最高频）。表内是新版字符串错误码；
# 旧版 oapi 数字错误码（如 60011）多数不在表里，走 rg docs/ 全文兜底
jq -c 'select(.error_code=="invalidDept")' graph/errcode.jsonl
jq -c 'select(.explanation|test("部门"))' graph/errcode.jsonl

# 按事件名找事件文档
jq -c 'select(.event_types[]? == "user_add_org")' graph/event.jsonl

# 某权限点覆盖哪些接口
jq -c 'select(.permission_scope=="Contact.User.Read")' graph/permission.jsonl

# 关系扩展：这篇文档引用了谁 / 谁引用了它（反链，变更影响分析也用它）
jq -c 'select(.from=="docs/01-应用开发/01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md")' graph/links.jsonl
jq -c 'select(.to=="docs/01-应用开发/02-4a8AMF6u2A-服务端API/0033-obtain-the-access-token-of-an-internal-app.md")' graph/links.jsonl
```

## 使用纪律

- 命中行里的 `doc_path`/`from`/`to` 是仓内相对路径，直接读该文件拿全文；`source_url` 用于回答时引用原始出处。
- `archived: true` 或路径在「历史文档（不推荐）」下的接口：仍可调用但官方不推荐，回答时要提示现行替代（用 `updated_at` 更新的同名/同域文档）。
- 本目录除本文件外全部是生成物，勿手改；重建命令见 [ops/INGEST.md](../ops/INGEST.md)。
