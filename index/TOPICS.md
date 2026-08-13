# 高频主题路由（认知层，LLM 维护）

> 答疑最常命中的主题 → 权威文档直达。**这是本库唯一一个由人/LLM 维护的索引页**：快照更新后按 `ops/INGEST.md` 的「后续动作」复核本页。
> 纪律：只收会饱和的高频主题，不做全量目录（那是 [INDEX.md](INDEX.md) 的事）；条目只指路不复述内容；每条链接必须可达（lint 会查）。
>
> 最后复核：2026-08-12（对应 2026-08-12 快照）

## ID 体系与互转

- 用户标识对照：**userId**（企业内唯一、不可改）/ **unionId**（跨企业唯一）/ **工号 job_number**（企业自维护、可不唯一、非必填，不能作唯一标识）——[基础概念](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md) · [通讯录概述·名词解释](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0047-contacts-overview.md)
- 注意：旧版（归档）JSAPI 文档里的"工号/emplId"多为 userid 的历史命名混用，勿按字面理解
- 会话标识 openConversationId：获取 = [创建群返回](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0738-create-common-group-new-version-v2.md) / [chatId 转换接口](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0745-obtain-group-openconversationid.md) / [JSAPI 选择会话 chooseChat](../docs/01-应用开发/03-Ogu5SlPY4t-客户端JSAPI/0318-jsapi-choose-chat.md) / [机器人接收消息回调](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0078-robot-receive-message.md)；`openChatByConversationId` 是**消费**该 ID 的跳转 JSAPI，不是获取途径

## 凭证与鉴权

- [获取企业内部应用的 accessToken](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0033-obtain-the-access-token-of-an-internal-app.md) — 全库被引用第二多的文档
- [获取第三方应用授权企业的 accessToken](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)（ISV/服务商场景）
- [获取用户 token（OAuth 登录态）](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0032-obtain-user-token.md)
- [JSAPI 鉴权（jsapi_ticket / dd.config）](../docs/01-应用开发/03-Ogu5SlPY4t-客户端JSAPI/0003-jsapi-authentication.md)
- 基础概念（CorpId/UserId/UnionId/AgentId、凭证体系）：[基础概念](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md)

## 免登与登录

- [身份验证（免登）概述](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0016-sso-overview.md)
- [小程序应用免登](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0017-small-program-application-free-of-registration.md) · [网页应用（H5）免登](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0018-enterprise-internal-application-logon-free.md)
- [网页方式登录第三方网站（扫码/账号）](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0019-tutorial-obtaining-user-personal-information.md)

## 服务端 API 调用

- [API 调用步骤详解](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0001-server-api-calling-guide.md) · [服务端 SDK 下载](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0002-download-the-server-side-sdk.md)
- [添加接口调用权限](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0003-add-api-permission.md) · [敏感权限使用](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0004-use-sensitive-permissions.md)
- 找某个接口 / 权限点 → 别翻目录，直接查 [graph/api.jsonl 与 permission.jsonl](../graph/GRAPH.md)
- 新旧双轨：`api.dingtalk.com`（新版）与 `oapi.dingtalk.com`（旧版）并存，`graph/api.jsonl` 的 `version` 字段可判别
- 限流/QPS/调用频率：[调用频率限制](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0012-call-frequency-limit.md)（规避实践/指数退避）+ [调用频次与限流](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/1432-how-to-process-api-throttling-on-the-dingtalk-server.md)（应用/IP/组织/全局四维度阈值与错误码），两篇一并给；按 appKey 维度为主，不按操作人；库内无"带宽"维度条目

## 错误码排查

- 精确查询 → [graph/errcode.jsonl](../graph/GRAPH.md)（2515 条逐条展开）
- [全局错误码原文](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0013-server-api-error-codes-1.md) — 全库被引用最多的文档

## 机器人（Bot）

- [机器人应用概述](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0075-robot-application-overview.md) · [配置企业机器人](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0076-configure-the-robot-application.md)
- [机器人接收消息](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0078-robot-receive-message.md) · [机器人回复/发送消息](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0079-robot-reply-and-send-messages.md)
- 群自定义机器人（Webhook 推送）：[创建](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0081-custom-bot-creation-and-installation.md) · [获取 Webhook 地址](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0083-obtain-the-webhook-address-of-a-custom-robot.md) · [安全设置](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0082-customize-robot-security-settings.md)

## 事件订阅

- [概述](../docs/01-应用开发/04-LFcRvVD08N-事件订阅/0001-overview-of-event-subscription.md) · [事件总览](../docs/01-应用开发/04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)
- [配置事件推送方式（Stream 模式）](../docs/01-应用开发/04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md) · [开发事件推送服务](../docs/01-应用开发/04-LFcRvVD08N-事件订阅/0004-develop-stream-mode-push-server.md) · [数据格式](../docs/01-应用开发/04-LFcRvVD08N-事件订阅/0005-development-data-format-help.md)
- 按事件名（如 `user_add_org`）找文档 → [graph/event.jsonl](../graph/GRAPH.md)；HTTP 回调详见事件订阅「历史文档」域（仍可用，官方主推 Stream）

## 应用开发入门

- [基础概念](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md) · [应用类型与能力说明](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0002-application-type-introduction.md) · [应用创建与配置](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0007-create-application.md)
- 小程序：[客户端 SDK 介绍](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0022-mini-app-client-jsapi-overview.md) · [开发前端](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0026-develop-miniapp-fe.md) · [上传发布](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0027-upload-miniapp.md)
- 网页应用（H5）：[开发前必读](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0029-webapp-read-before-development.md) · [配置](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0030-configure-web-application.md) · [前端](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0031-develop-webapp-frontend.md) · [服务端](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0032-develop-webapp-backend.md)
- [酷应用概述](../docs/01-应用开发/01-XOnnmGCTbn-开发指南/0042-coolapp-overview.md)（群聊/单聊内嵌应用形态）

## 通讯录

- [通讯录概述](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0047-contacts-overview.md) · [查询用户详情](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0056-query-user-details.md) · [获取部门用户 userid 列表](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0065-query-the-list-of-department-userids.md)
- 全量接口清单见 [服务端API/通讯录管理](01-应用开发/02-服务端API/05-通讯录管理.md)（115 篇）
- "主部门"无独立读写接口：文档承载字段是[智能人事员工调岗](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0954-intelligent-personnel-staff-transfer.md)的 `mainDeptIdAfterTransfer`（职位管理升级后修改主部门的文档支持途径）；[用户详情](../docs/01-应用开发/02-4a8AMF6u2A-服务端API/0056-query-user-details.md)的 `dept_id_list` 只是"所属部门id列表"，**文档未定义"第一个是主部门"之类语义**

## 互动卡片

- [普通卡片模板](../docs/05-互动卡片/01-N4KJ5HbqnQ-开发指南/0001-card-template-building-and-publishing.md) · [AI 卡片模板（流式）](../docs/05-互动卡片/01-N4KJ5HbqnQ-开发指南/0002-ai-card-template.md)
- [开放接口创建卡片实例](../docs/05-互动卡片/01-N4KJ5HbqnQ-开发指南/0004-open-the-interface-to-create-a-card-instance.md) · 其余见 [互动卡片索引](05-互动卡片/01-开发指南.md)

## AI 助理（AI PaaS）

- [AI 助理概述](../docs/03-AI-PaaS/03-9d1vBG1t78-DEAP·企业AI平台/0001-ai-assistant-overview.md)，全目录见 [DEAP·企业AI平台索引](03-AI-PaaS/03-DEAP·企业AI平台.md)（15 篇：智能体/工作流/MCP/知识/模型管理）。原「AI 助理创建平台」tab（97 篇）已随 2026-08-12 快照下线并入 DEAP，旧文档下线记录见 meta/tombstones.jsonl

## 连接平台 / 工作台 / 其它产品线

- 走 [总索引 INDEX.md](INDEX.md) 对应大类；这些类目篇数少，L2 一页可读完
