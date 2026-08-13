---
title: "获取用户待审批数量"
source_url: "https://open.dingtalk.com/document/development/obtain-the-number-of-tasks-to-be-approved-by-me"
namespace: "development"
slug: "obtain-the-number-of-tasks-to-be-approved-by-me"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 获取用户待审批数量"
doc_id: "hy9R3UELUe"
updated_at: "2025-09-08 19:04:35"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-number-of-tasks-to-be-approved-by-me
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 获取用户待审批数量
> Updated: 2025-09-08 19:04:35

# 获取用户待审批数量

调用本接口根据用户的userid获取该用户待处理的审批数量。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对OA审批相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2022年10月8日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[获取用户待审批数量](https://open.dingtalk.com/document/orgapp/queries-the-number-of-requests-to-be-approved-by-users)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

> **[!IMPORTANT]**
>
> 开发者可以通过以下链接，使用[H5微应用JSAPI-打开目标页面](https://open.dingtalk.com/document/orgapp/open-link-on-new-window)跳转到钉钉审批移动端微应用（暂不支持PC端）的待我审批页面：
>
> https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?showmenu=false&dd\_share=false&corpid=$CORPID#/upcoming?swfrom=work\_homepage

调用本接口，可以获取用户待审批的数量。如下图所示，待处理有11条审批。![审批数量](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5984796361/p352476.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/gettodonum`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager123 | 要查询的用户userid。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| count | Number | 13 | 待处理的审批数量。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回描述。 |
| request\_id | String | 3x1lrffff9xk | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/gettodonum?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "userid":"manager4220"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/gettodonum");
OapiProcessGettodonumRequest req = new OapiProcessGettodonumRequest();
req.setUserid("manager4220");
OapiProcessGettodonumResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "count": 1,
    "errcode": 0,
    "errmsg":"ok",
    "request_id": "3x1lrffff9xk"
}
```
