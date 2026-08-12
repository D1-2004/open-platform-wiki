---
title: "更新企业内部应用微应用的可使用范围"
source_url: "https://open.dingtalk.com/document/development/set-the-visible-range-of-the-microapplication"
namespace: "development"
slug: "set-the-visible-range-of-the-microapplication"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 应用管理 > 更新企业内部应用微应用的可使用范围"
doc_id: "ogJAcVM1ru"
updated_at: "2025-09-08 19:05:18"
---

> Source: https://open.dingtalk.com/document/development/set-the-visible-range-of-the-microapplication
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 应用管理 > 更新企业内部应用微应用的可使用范围
> Updated: 2025-09-08 19:05:18

# 更新企业内部应用微应用的可使用范围

调用本接口设置指定应用的可见范围。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对**应用管理**相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于**2022年6月24日**迁移至**历史文档（不推荐）**目录，且**本接口仅保持现有功能，不再新增支持其他能力。**
>
> - 如果未使用本接口，推荐使用新版规范[更新企业内部应用微应用的可使用范围](https://open.dingtalk.com/document/orgapp/update-the-visible-range-of-micro-applications)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

![iShot2022-02-22 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6671055461/p407498.png)

> **[!NOTE]**
>
> - 企业内部应用-H5微应用
>
>   - 当前H5微应用是开发版本，调用本接口可指定H5微应用开发版本的可见范围。
>   - 当前H5微应用是线上版本，调用本接口可指定H5微应用线上版本的可见范围。
> - 企业内部应用-小程序应用
>
>   - 仅在小程序线上版本适用。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/microapp/set_visible_scopes`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userVisibleScopes | String[] | 否 | ["userId1","userId2"] | 设置可见的员工userid列表，格式为JSON数组。 |
| deptVisibleScopes | Number[] | 否 | [1,2] | 设置可见的部门ID列表，格式为JSON数组。 |
| isHidden | Boolean | 否 | false | 是否仅限管理员可见：   - **true** - **false** |
| agentId | Number | 是 | 16691682 | 应用AgentID。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码。 |
| errcode | Number | 0 | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/microapp/set_visible_scopes?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "agentId": 852825694,
    "userVisibleScopes": [
        "user123",
        "manager4220"
    ],
    "deptVisibleScopes": [
        1,
        2
    ],
    "isHidden": false
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/microapp/set_visible_scopes");
OapiMicroappSetVisibleScopesRequest req = new OapiMicroappSetVisibleScopesRequest();
req.setUserVisibleScopes(Arrays.asList("user123","manager4220"));
req.setDeptVisibleScopes(Arrays.asList(1L,2L));
req.setIsHidden(false);
req.setAgentId(852825694L);
OapiMicroappSetVisibleScopesResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "errmsg":"ok"
}
```
