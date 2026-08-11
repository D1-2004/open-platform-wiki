---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/description-of-tiktok-parameters"
namespace: "connection"
slug: "description-of-tiktok-parameters"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "三方连接器 > 抖音 > 参数说明"
doc_id: "X11HyKZoh0"
updated_at: "2025-09-23 19:21:31"
---

> Source: https://open.dingtalk.com/document/connection/description-of-tiktok-parameters
> Path: 连接平台 / 连接器中心 / 三方连接器 > 抖音 > 参数说明
> Updated: 2025-09-23 19:21:31

# 参数说明

## **执行动作说明**

抖音开放平台的 OAuth API 与 其他功能 API，域名为`https://open.douyin.com`。

## **获取用户公开信息**

| **入参** | **类型** | **是否必填** | **详细说明** |
| --- | --- | --- | --- |
| access\_token | string | 是 | 调用[获取 access\_token](https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/account-permission/get-access-token)获取，此 token 需要用户授权。 |
| open\_id | string | 是 | 调用[获取 access\_token](https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/account-permission/get-access-token)获取，用户唯一标识。 |

## 查询视频列表

| **入参** | **类型** | **是否必填** | **详细说明** |
| --- | --- | --- | --- |
| open\_id | string | 是 | 调用[获取 access\_token](https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/account-permission/get-access-token)获取，用户唯一标识。 |
| cursor | i64 | 否 | 分页游标, 第一页请求 cursor 是 0, response 中会返回下一页请求用到的 cursor , 同时 response 还会返回 has\_more 来表明是否有更多的数据。 |
| count | i32 | 是 | 每页数量。 |

## **查询评论列表**

| **入参** | **类型** | **是否必填** | **详细说明** |
| --- | --- | --- | --- |
| open\_id | string | 是 | 调用[获取 access\_token](https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/account-permission/get-access-token)获取，用户唯一标识。 |
| cursor | i64 | 否 | 分页游标, 第一页请求 cursor 是 0, response 中会返回下一页请求用到的 cursor , 同时 response 还会返回 has\_more 来表明是否有更多的数据。 |
| count | i32 | 是 | 每页的数量，最大不超过 20，最小不低于 1。 |
| item\_id | string | 是 | 视频id。 |
| sort\_type | string | 否 | 列表排序方式，不传默认按推荐序，可选值：time(时间逆序)、time\_asc(时间顺序)。 |

## 获取直播间基础数据/看播数据

| **入参** | **类型** | **是否必填** | **详细说明** |
| --- | --- | --- | --- |
| open\_id | string | 是 | 调用[获取 access\_token](https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/account-permission/get-access-token)获取，用户唯一标识。 |
| live\_id | int64 | 是 | 业务线id：   - 1：抖火 - 3：西瓜头条 |
| room\_id | int64 | 是 | 房间id。 |

## 获取抖音星图达人指数

| **入参** | **类型** | **是否必填** | **详细说明** |
| --- | --- | --- | --- |
| open\_id | string | 是 | 调用[获取 access\_token](https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/account-permission/get-access-token)获取，用户唯一标识。 |
