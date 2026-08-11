---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/management-parameter-description"
namespace: "connection"
slug: "management-parameter-description"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 应用管理 > 参数说明"
doc_id: "ozd6bvLCqs"
updated_at: "2025-09-23 19:21:25"
---

> Source: https://open.dingtalk.com/document/connection/management-parameter-description
> Path: 连接平台 / 连接器中心 / 官方连接器 > 应用管理 > 参数说明
> Updated: 2025-09-23 19:21:25

# 参数说明

本文详细介绍了应用管理的执行动作中的参数说明。

## **执行动作**

## **获取应用列表**

无入参

## **设置应用的可见范围**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| agentId | String | 是 | 应用[实例 ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md) 。 |
| userVisibleScopes | Array of String | 否 | 设置可见的[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)列表。 |
| deptVisibleScopes | Array of Long | 否 | 设置可见的[部门 ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md) 列表。 |
| isHidden | Booelan | 否 | 是否仅限管理员可见：   - true：代表仅限管理员可见。 - false：根据上述员工ID和部门ID同步。 |

## **获取应用的可见范围**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| agentId | String | 是 | 应用[实例 ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md) 。 |

## **获取员工可见的应用列表**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userid | String | 是 | 待查询[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)。 |
