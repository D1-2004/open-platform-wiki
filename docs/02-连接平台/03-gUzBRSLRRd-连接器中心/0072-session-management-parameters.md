---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/session-management-parameters"
namespace: "connection"
slug: "session-management-parameters"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 会话管理（场景群） > 参数说明"
doc_id: "Qp5obnD7Xh"
updated_at: "2025-09-23 19:21:28"
---

> Source: https://open.dingtalk.com/document/connection/session-management-parameters
> Path: 连接平台 / 连接器中心 / 官方连接器 > 会话管理（场景群） > 参数说明
> Updated: 2025-09-23 19:21:28

# 参数说明

## 执行动作说明

## **创建场景群**

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| title | String | 是 | 群名称。 |
| template\_id | String | 是 | 输入[群模板ID（templateId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#5ee8fb30ff7ll)，创建群会话的模板。 |
| owner\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，创建群会话的群主。 |

## **更新场景群**

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| open\_conversation\_id | String | 是 | 输入[群会话ID（chatId/openConversationId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#37be9ff0ffhrb)，待更新群的会话ID。 |

## **新增群成员**

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| open\_conversation\_id | String | 是 | 输入[群会话ID（chatId/openConversationId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#37be9ff0ffhrb)，待新增群成员的会话ID。 |
| user\_ids | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，待新增群成员的UserId。 |

## **删除群成员**

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| open\_conversation\_id | String | 是 | 输入[群会话ID（chatId/openConversationId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#37be9ff0ffhrb)，待删除群成员的会话ID。 |
| user\_ids | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，待删除群成员的UserId。 |

## **获取场景群成员**

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| open\_conversation\_id | String | 是 | 输入[群会话ID（chatId/openConversationId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#37be9ff0ffhrb)，待获取群成员的会话ID。 |
| cursor | String | 是 | 分页游标 |
| size | Number | 是 | 分页大小。 |

## **停用群模板**

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| openConversationId | String | 是 | 输入[群会话ID（chatId/openConversationId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#37be9ff0ffhrb)，待停用群模板的会话ID。 |
| templateId | String | 是 | 输入[群模板ID（templateId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#5ee8fb30ff7ll)，待停用的群模板ID。 |
| ownerUserId | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，待停用群模板所在会话的群主UserId。 |

## **查询场景群基本信息**

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| open\_conversation\_id | String | 是 | 输入[群会话ID（chatId/openConversationId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#37be9ff0ffhrb)，待查询群基本信息的会话ID。 |
