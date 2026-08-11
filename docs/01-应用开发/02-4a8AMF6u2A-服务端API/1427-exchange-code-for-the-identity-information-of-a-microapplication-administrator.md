---
title: "获取应用管理后台免登的用户信息"
source_url: "https://open.dingtalk.com/document/development/exchange-code-for-the-identity-information-of-a-microapplication-administrator"
namespace: "development"
slug: "exchange-code-for-the-identity-information-of-a-microapplication-administrator"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 身份验证（免登） > 获取应用管理后台免登的用户信息"
doc_id: "mtvC5AWzKo"
updated_at: "2025-09-08 19:07:44"
---

> Source: https://open.dingtalk.com/document/development/exchange-code-for-the-identity-information-of-a-microapplication-administrator
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 身份验证（免登） > 获取应用管理后台免登的用户信息
> Updated: 2025-09-08 19:07:44

# 获取应用管理后台免登的用户信息

在应用管理后台免登场景中，需要本接口通过获取到的免登授权码code和获取到的应用后台免登的access\_token来换取应用管理员的身份信息。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对获取访问凭证相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2023年8月30日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用[获取应用管理后台免登的用户信息](https://open.dingtalk.com/document/isvapp/obtains-the-identity-of-an-application-administrator)新版规范接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

![iShot2021-12-29 19](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7091380461/p378309.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保对应用已经添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 开发者后台申请 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingtalk.oapi.sso.getuserinfo) |
| 第三方企业应用 | 是 | 开发者后台申请 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=dingtalk.oapi.sso.getuserinfo) |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/sso/getuserinfo`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| code | String | 是 | 123 | 通过Oauth认证给URL带上的code。 |
| access\_token | String | 是 | 6ed1bxxx | 调用该API的应用凭证。   - 企业内部应用，调用[获取微应用后台免登的access\_token](https://open.dingtalk.com/document/orgapp/obtain-the-ssotoken-for-micro-application-background-logon-free)接口获取。 - 第三方企业应用，调用[获取微应用后台免登的access\_token](https://open.dingtalk.com/document/isvapp/obtain-the-ssotoken-for-micro-application-background-logon-free)接口获取。 |

**code参数说明**

当企业管理员登录[钉钉管理后台](http://oa.dingtalk.com/)后，点击**工作台**中的应用，会自动跳转到应用的后台地址，钉钉会把code参数追加到此URL地址中，如下图：![开发管理](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2482364951/p131087.png)

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| user\_info | UserInfo |  | 用户信息。 |
| avatar | String | http://xxxxxxx.jpg | 头像地址。 |
| email | String | 123456@aliyun.com | email地址。 |
| name | String | 名称 | 用户名字。 |
| userid | String | 0571 | 员工在企业内的userid。 |
| corp\_info | CorpInfo |  | 企业信息。 |
| corp\_name | String | 一家公司 | 公司名字。 |
| corpid | String | dingxxxxxx | 公司corpid。 |
| is\_sys | Boolean | true | 是否是管理员。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回描述。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/sso/getuserinfo?code=code&access_token=access_token
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/sso/getuserinfo");
OapiSsoGetuserinfoRequest req = new OapiSsoGetuserinfoRequest();
req.setCode("123");
req.setHttpMethod("GET");
OapiSsoGetuserinfoResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "user_info":{
                "name":"名称",
                "avatar":"http://xxxxxxx.jpg",
                "userid":"0571",
                "email":"123456@aliyun.com"
        },
        "is_sys":true,
        "corp_info":{
                "corpid":"dingxxxxxx",
                "corp_name":"一家公司"
        },
        "errmsg":"ok"
}
```

## 相关文档

- 企业内部应用，请参考[应用管理后台免登](https://open.dingtalk.com/document/orgapp/log-on-site-application-management-backend)。
- 第三方企业应用，请参考[应用管理后台免登](https://open.dingtalk.com/document/isvapp/log-on-site-application-management-backend)。
