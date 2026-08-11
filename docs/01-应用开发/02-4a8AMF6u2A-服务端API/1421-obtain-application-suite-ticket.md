---
title: "获取第三方企业应用的suite_access_token"
source_url: "https://open.dingtalk.com/document/development/obtain-application-suite-ticket"
namespace: "development"
slug: "obtain-application-suite-ticket"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 获取访问凭证 > 获取第三方企业应用的suite_access_token"
doc_id: "pEN2VC7PiA"
updated_at: "2025-09-10 19:26:54"
---

> Source: https://open.dingtalk.com/document/development/obtain-application-suite-ticket
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 获取访问凭证 > 获取第三方企业应用的suite_access_token
> Updated: 2025-09-10 19:26:54

# **获取第三方企业应用的suite\_access\_token**

调用本接口获取第三方企业应用的suite\_access\_token。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对**获取访问凭证**相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/development/how-to-call-apis#section-8lr-id4-rbz)。本文旧版规范接口文档已于2023年8月17日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用[获取第三方企业应用的suiteAccessToken](0036-obtains-the-suite-acess-token-of-third-party-enterprise-applications.md)新版规范接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

该suite\_access\_token主要用于获取第三方企业应用的信息，在调用以下接口时会使用第三方企业应用的suite\_access\_token：

- [获取授权应用的基本信息](0043-obtains-application-information-of-an-enterprise.md)
- [获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保对应用已经添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | — | — |
| 第三方企业应用 | 是 | 默认开通，无需申请 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=dingtalk.oapi.service.get_suite_token) |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/service/get_suite_token`

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| suite\_key | String | 是 | suitefcurkdvkc1nxxxx | 第三方应用的suiteKey。可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/custom/h5/951603110/1)的应用详情页获取。 |
| suite\_secret | String | 是 | y1ie2Rfb54xxxx | 第三方应用的suiteSecret，可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/custom/h5/951603110/1)的应用详情页获取。 |
| suite\_ticket | String | 是 | test | 钉钉开放平台会向应用的回调URL推送的suite\_ticket（约5个小时推送一次），详细内容请参考[数据格式biz\_type=2](https://open.dingtalk.com/document/development/data-format#section-dqx-ue5-0f8)。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| suite\_access\_token | String | token | 第三方企业应用的凭证。 |
| expires\_in | Number | 7200 | 第三方企业应用的凭证过期时间，单位秒。  **[!NOTE]**  suite\_access\_token有效期为7200秒，过期之前建议服务端做定时器主动更新，而不是依赖钉钉的定时推送。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/service/get_suite_token
```

请求正文

```
{
        "suite_ticket":"test",
        "suite_secret":"y1ie2Rfb54xxxx",
        "suite_key":"suitefcurkdvkc1nxxxx"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/service/get_suite_token");
OapiServiceGetSuiteTokenRequest req = new OapiServiceGetSuiteTokenRequest();
req.setSuiteKey("suitefcurkdvkc1nxxxx");
req.setSuiteSecret("y1ie2Rfb54xxxx");
req.setSuiteTicket("test");
OapiServiceGetSuiteTokenResponse rsp = client.execute(req);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "errmsg":"ok",
        "suite_access_token":"67477fed82e63563a320xxxx",
        "expires_in":7200
}
```
