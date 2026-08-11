---
title: "根据unionid获取用户userid"
source_url: "https://open.dingtalk.com/document/development/you-can-call-this-operation-to-retrieve-the-userids-of"
namespace: "development"
slug: "you-can-call-this-operation-to-retrieve-the-userids-of"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 根据unionid获取用户userid"
doc_id: "OtGCDDB9AN"
updated_at: "2025-09-08 19:07:32"
---

> Source: https://open.dingtalk.com/document/development/you-can-call-this-operation-to-retrieve-the-userids-of
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 根据unionid获取用户userid
> Updated: 2025-09-08 19:07:32

# 根据unionid获取用户userid

调用本接口根据unionid获取用户的userid。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，提供更加规范的接口，钉钉针对通讯录**用户管理**和**部门管理**接口进行了升级，**用户管理1.0**、**部门管理1.0**的接口文档已于2021年10月21日迁移至**历史文档（不推荐）**目录下，且**用户管理1.0和部门管理1.0接口将不再添加新的能力，仅保持原有功能。**
>
> - 如果未接入1.0版接口，推荐使用新的[用户管理](https://open.dingtalk.com/document/isvapp/query-user-details)、[部门管理](https://open.dingtalk.com/document/isvapp/query-department-details0-v2)接口。
> - 如果已接入1.0版接口，建议您根据自身实际情况评估是否切换至新接口。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/user/getUseridByUnionid`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |
| unionid | String | 是 | gliiW0piiii02zBUjUxxxx | 用户在当前钉钉开放平台账号范围内的唯一标识，同一个钉钉开放平台账号可以包含多个开放应用，同时也包含ISV的套件应用及企业应用。  可通过调用[查询用户详情](https://open.dingtalk.com/document/isvapp/obtains-user-details-based-on-the-userid)接口获取。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| contactType | Number | 1 | 联系人类型：   - **0**：表示企业内部员工 - **1**：表示企业外部联系人 |
| userid | String | 1 | 用户userid。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/user/getuseridbyunionid?access_token=ACCESS_TOKEN&unionid=gliiW0piiii02zBUjUxxxx
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/getUseridByUnionid");
OapiUserGetUseridByUnionidRequest req = new OapiUserGetUseridByUnionidRequest();
req.setUnionid("gliiW0piiii02zBUjUxxxx");
req.setHttpMethod("GET");
OapiUserGetUseridByUnionidResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "contactType": 1,
    "userid": "1"
}
```
