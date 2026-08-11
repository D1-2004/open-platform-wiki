---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/todo-parameter-description"
namespace: "connection"
slug: "todo-parameter-description"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 待办事项 > 参数说明"
doc_id: "lDBZY9BniW"
updated_at: "2025-09-23 19:21:23"
---

> Source: https://open.dingtalk.com/document/connection/todo-parameter-description
> Path: 连接平台 / 连接器中心 / 官方连接器 > 待办事项 > 参数说明
> Updated: 2025-09-23 19:21:23

# 参数说明

## **执行动作**

## **新增钉钉待办任务**

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| sourceId | String | 否 | 业务系统侧的唯一标识ID，即业务ID。 |
| subject | String | 是 | 待办标题，最大长度1024。 |
| notifyConfigs | Object | 否 | 待办通知配置。 |
| dingNotify | String | 否 | DING通知配置，目前仅支持取值为**1**，表示应用内DING。 |
| creatorId | String | 否 | 待创建的[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)。 |
| description | String | 否 | 待办备注描述，最大长度4096。 |
| dueTime | Long | 否 | 截止时间，Unix时间戳，单位毫秒。 |
| priority | Integer | 否 | 优先级，取值：   - **10**：较低 - **20**：普通 - **30**：紧急 - **40**：非常紧急 |
| userId | String | 是 | 当前访问资源所归属用户ID，和创建者ID保持一致。 |
| isOnlyShowExecutor | Boolean | 否 | 生成的待办是否仅展示在执行者的待办列表中。 |
| accessKey | String | 否 | 应用AccessKey：   - 企业内部应用，填写应用的appKey - 第三方企业应用，填写应用suiteKey |
| appType | String | 否 | 应用类型：   - ORG：组织 - ISV：三方 |
| participantIds | Array of String | 否 | 参与者的用户ID。 |
| detailUrl | Object | 否 | 详情页url跳转地址。  **[!NOTE]**   - 创建钉钉官方待办时，该字段无需传入。 - 创建企业待办时，需传入自身应用详情页链接。 |
| pcUrl | String | 否 | PC端详情页url跳转地址。 |
| appUrl | String | 否 | APP端详情页url跳转地址。 |
| executorIds | Array of String | 否 | 待执行用户userId。 |
| operatorId | String | 否 | 当前操作者用户的userId。 |

## **更新钉钉待办任务**

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| done | Booelan | 否 | 完成状态。 |
| subject | String | 否 | 待办标题，最大长度1024。 |
| creatorId | String | 否 | 待创建的[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)。 |
| description | String | 否 | 待办备注描述，最大长度4096。 |
| dueTime | Long | 否 | 截止时间，Unix时间戳，单位毫秒。 |
| priority | Integer | 否 | 优先级，取值：   - **10**：较低 - **20**：普通 - **30**：紧急 - **40**：非常紧急 |
| userId | String | 是 | 当前访问资源所归属用户ID，和创建者ID保持一致。 |
| accessKey | String | 否 | 应用AccessKey：   - 企业内部应用，填写应用的appKey - 第三方企业应用，填写应用suiteKey |
| appType | String | 否 | 应用类型：   - ORG：组织 - ISV：三方 |
| participantIds | Array of String | 否 | 参与者的用户userId列表。 |
| executorIds | Array of String | 否 | 待执行用户userId列表。 |
| operatorId | String | 否 | 当前操作者用户的userId。 |
| taskId | String | 是 | 待办ID。 |

## **删除钉钉待办任务**

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 当前访问资源所归属用户ID，和创建者ID保持一致。 |
| accessKey | String | 否 | 应用AccessKey：   - 企业内部应用，填写应用的appKey - 第三方企业应用，填写应用suiteKey |
| appType | String | 否 | 应用类型：   - ORG：组织 - ISV：三方 |
| operatorId | String | 否 | 当前操作者用户的userId。 |
| taskId | String | 是 | 待办ID。 |

## **获取钉钉待办任务详情**

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 当前访问资源所归属用户ID，和创建者ID保持一致。 |
| accessKey | String | 否 | 应用AccessKey：   - 企业内部应用，填写应用的appKey - 第三方企业应用，填写应用suiteKey |
| appType | String | 否 | 应用类型：   - ORG：组织 - ISV：三方 |
| taskId | String | 是 | 待办ID。 |

## **根据sourceId获取钉钉待办任务详情**

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 当前访问资源所归属用户ID，和创建者ID保持一致。 |
| accessKey | String | 否 | 应用AccessKey：   - 企业内部应用，填写应用的appKey - 第三方企业应用，填写应用suiteKey |
| appType | String | 否 | 应用类型：   - ORG：组织 - ISV：三方 |
| sourceId | String | 是 | 待办业务来源sourceId。  **[!NOTE]**  sourceId为创建待办时传入的sourceId。 |

## **查询企业下用户待办列表**

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| isDone | Booelan | 否 | 完成状态。 |
| userId | String | 是 | 用户userId。 |
| accessKey | String | 否 | 应用AccessKey：   - 企业内部应用，填写应用的appKey - 第三方企业应用，填写应用suiteKey |
| appType | String | 否 | 应用类型：   - ORG：组织 - ISV：三方 |
| nextToken | String | 否 | 分页游标。如果一个查询条件一次无法全部返回结果，会返回分页token，下次查询带上该token后会返回后续数据，直到分页token为null表示数据已经全部查询完毕。 |
