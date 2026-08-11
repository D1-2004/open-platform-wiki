---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/log-overview"
namespace: "connection"
slug: "log-overview"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 签到 > 参数说明"
doc_id: "4RQ81kFi1A"
updated_at: "2025-09-23 19:20:54"
---

> Source: https://open.dingtalk.com/document/connection/log-overview
> Path: 连接平台 / 连接器中心 / 官方连接器 > 签到 > 参数说明
> Updated: 2025-09-23 19:20:54

# 参数说明

## **触发事件**

## **用户签到**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| CorpId | String | 用户签到企业的CorpId |
| EventType | String | 事件类型。 |
| StaffId | String | 签到[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| TimeStamp | Long | 签到时间戳。 |

## **执行动作**

## **获取部门用户签到记录**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| start\_time | Long | 开始时间戳，单位毫秒。 |
| offset | Integer | 偏移量，与 size 参数同时设置时才生效，从 0 开始。 |
| size | Integer | 分页大小，与 offset 参数同时设置时才生效，最大值 100 。 |
| department\_id | String | 待查询[部门 ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，1 表示根部门。 |
| end\_time | Long | 结束时间戳，单位毫秒。 |
| order | String | 排序。 |

## **获取用户签到记录**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| start\_time | Long | 开始时间戳，单位毫秒。 |
| cursor | Integer | 偏移量，与 size 参数同时设置时才生效，从 0 开始。 |
| size | Integer | 分页大小，最大值 100 。 |
| end\_time | Long | 结束时间戳，单位毫秒。 |
| userid\_list | String | 签到[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)列表。 |
