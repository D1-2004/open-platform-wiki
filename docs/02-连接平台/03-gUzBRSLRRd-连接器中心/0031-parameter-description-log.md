---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/parameter-description-log"
namespace: "connection"
slug: "parameter-description-log"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 日志 > 参数说明"
doc_id: "fIFQ3RqqrV"
updated_at: "2025-09-23 19:20:56"
---

> Source: https://open.dingtalk.com/document/connection/parameter-description-log
> Path: 连接平台 / 连接器中心 / 官方连接器 > 日志 > 参数说明
> Updated: 2025-09-23 19:20:56

# 参数说明

## **执行动作**

## **获取模板详情**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| template\_name | String | 是 | 模板名称。 |
| userid | String | 是 | 钉钉[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |

## **获取日志评论详情**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| offset | Long | 否 | 偏移量，最开始传0，后续传返回参数中的 next\_cursor 值，默认值为 0 。 |
| size | Long | 否 | 每页大小，最多传 20 ，默认值为 20 。 |
| report\_id | String | 是 | 日志 ID 。 |

## **获取日志统计数据**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| report\_id | String | 是 | 日志 ID 。 |

## **获取用户日志未读数**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userid | String | 是 | 待查询[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |

## **获取日志接收人员列表**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| offset | Long | 否 | 偏移量，最开始传0，后续传返回参数中的 next\_cursor 值，默认值为 0 。 |
| size | Long | 否 | 每页大小，最大传值 100 ，默认值为 100 。 |
| report\_id | String | 是 | 日志 ID 。 |

## **获取日志相关人员列表**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| offset | Long | 否 | 偏移量，最开始传0，后续传返回参数中的 next\_cursor 值，默认值为 0 。 |
| size | Long | 否 | 每页大小，最大传值 100 ，默认值为 100 。 |
| report\_id | String | 是 | 日志 ID 。 |
| type | Integer | 是 | 查询类型：   - **0**：已读人员列表 - **1**：评论人员列表 - **2**：点赞人员列表 |

## **获取用户发出的日志列表**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| cursor | Integer | 是 | 偏移量，初始传入0，后续从上一次的返回值中获取。 |
| size | Integer | 是 | 每页大小。 |
| start\_time | Long | 是 | 开始时间戳，单位毫秒。  **[!NOTE]**  start\_time参数和end\_time参数最多相隔180天。 |
| end\_time | Long | 是 | 结束时间戳，单位毫秒。  **[!NOTE]**  start\_time参数和end\_time参数最多相隔180天。 |
| template\_name | String | 否 | 模板名称。 |
| modified\_end\_time | Long | 否 | 查询的日志修改的结束时间戳，单位毫秒。 |
| modified\_start\_time | Long | 否 | 查询的日志修改的开始时间戳，单位毫秒。 |
| userid | String | 是 | 待查询[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |

## **获取用户可见的日志模板**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| offset | Long | 否 | 偏移量，最开始传0，后续传返回参数中的 next\_cursor 值，默认值为 0 。 |
| size | Long | 否 | 每页大小，最大传值 100 。 |
| userid | String | 是 | 待查询[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |

## **获取用户发送日志的概要信息**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| cursor | Integer | 是 | 偏移量，初始传入0，后续从上一次的返回值中获取。 |
| size | Integer | 是 | 每页大小。 |
| start\_time | Long | 是 | 开始时间戳，单位毫秒。  **[!NOTE]**  start\_time参数和end\_time参数最多相隔180天。 |
| end\_time | Long | 是 | 结束时间戳，单位毫秒。  **[!NOTE]**  start\_time参数和end\_time参数最多相隔180天。 |
| template\_name | String | 否 | 模板名称。 |
| userid | String | 是 | 待查询[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
