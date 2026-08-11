---
title: "通过免登码获取用户信息（不推荐）"
source_url: "https://open.dingtalk.com/document/development/get-user-userid-through-login-free-code"
namespace: "development"
slug: "get-user-userid-through-login-free-code"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 身份验证（免登） > 通过免登码获取用户信息（不推荐）"
doc_id: "n1Al2zCrny"
updated_at: "2025-09-08 19:07:45"
---

> Source: https://open.dingtalk.com/document/development/get-user-userid-through-login-free-code
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 身份验证（免登） > 通过免登码获取用户信息（不推荐）
> Updated: 2025-09-08 19:07:45

# 通过免登码获取用户信息（不推荐）

在第三方企业应用免登和企业内部应用免登场景中，开发者需要使用本接口通过access\_token和免登接口中获取的code来获取用户userid。

> **[!NOTE]**
>
> 接口升级，接口文档已于2021年10月27日移动至**历史文档（不推荐）**目录。已经接入的用户可继续使用，正在准备接入的用户请参考[通过免登码获取用户信息](https://open.dingtalk.com/document/orgapp/obtain-the-userid-of-a-user-by-using-the-log-free)。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保对应用已经添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 默认开通，无需申请 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingtalk.oapi.user.getuserinfo) |
| 第三方企业应用 | 是 | 默认开通，无需申请 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=dingtalk.oapi.user.getuserinfo) |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/user/getuserinfo`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6ed1bxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 - 第三方企业应用可通过[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |
| code | String | 是 | 677e73b724edxxxx | 免登授权码。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码**。** |
| errmsg | String | ok | 对返回码的文本描述内容。 |
| userid | String | user456 | 员工在当前企业内的唯一标识，也称staffId。 |
| name | String | 张xx | 员工姓名。 |
| deviceId | String | 12drtfxxxxx | 设备ID。 |
| is\_sys | Boolean | true | 是否是管理员。   - **true**：是 - **false**：不是 |
| sys\_level | Number | 1 | 级别。   - **1**：主管理员 - **2**：子管理员 - **100**：老板 - **0**：其他（如普通员工） |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/user/getuserinfo?access_token=ACCESS_TOKEN&code=123456
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/getuserinfo");
OapiUserGetuserinfoRequest req = new OapiUserGetuserinfoRequest();
req.setCode("677e73b724edxxxx");
req.setHttpMethod("GET");
OapiUserGetuserinfoResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "sys_level": 1,
    "is_sys": true,
    "name": "张xx",
    "errmsg": "ok",
    "deviceId": "12drtfxxxxx",
    "userid": "user456"
}
```
