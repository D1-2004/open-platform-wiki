---
title: "注册互动卡片回调地址"
source_url: "https://open.dingtalk.com/document/development/registration-card-interaction-callback-address-1"
namespace: "development"
slug: "registration-card-interaction-callback-address-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 机器人 > 注册互动卡片回调地址"
doc_id: "Hj2hChNgc9"
updated_at: "2026-04-29 13:23:55"
---

> Source: https://open.dingtalk.com/document/development/registration-card-interaction-callback-address-1
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 即时通信 > 机器人 > 注册互动卡片回调地址
> Updated: 2026-04-29 13:23:55

# 注册互动卡片回调地址

调用本接口注册互动卡片的回调地址。注册后，开发者后台系统可感知到用户对卡片的操作。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，本文档于 2024 年 12 月 31 日迁移至历史文档（不推荐）目录，不再支持新应用接入，已接入的应用不受影响。如果未使用本接口，请使用[注册卡片回调地址](https://open.dingtalk.com/document/orgapp/register-card-callback-address)接口。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!IMPORTANT]**  不支持新增申请 | — |
| 第三方企业应用 | 是 | **[!IMPORTANT]**  不支持新增申请 | — |
| 第三方个人应用 | 否 | 暂不支持 | 暂不支持 |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/im/chat/scencegroup/interactivecard/callback/register`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | be3xxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用，通过[获取第三方企业应用的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| callback\_url | String | 是 | https://xxx.xxx.xxx | 回调URL地址。  **[!NOTE]**  URL地址不支持携带参数， |
| api\_secret | String | 否 | bgRtxxxx | 加密密钥用于校验来源。 |
| callbackRouteKey | String | 否 | xxxxxx | callback地址的路由Key，一个`callbackRouteKey`仅可映射一个`callback_url`。该参数在**发送钉钉互动卡片**接口中使用。   - 企业内部应用，调用[发送钉钉互动卡片](https://open.dingtalk.com/document/orgapp/send-interactive-dynamic-cards-1)接口。 - 第三方企业应用，调用[发送钉钉互动卡片](https://open.dingtalk.com/document/isvapp/send-interactive-dynamic-cards)接口。 |
| forceUpdate | Boolean | 否 | false | 是否强制覆盖更新（这里是二次确认逻辑，避免线上注册的url被误调用修改影响业务回调；等同第一次调用不存在则插入，存在则结果返回上次注册信息，第二次调用业务方根据第一次返回结果比对确认后要修改则forceUpdate改为true强制更新） |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Json |  | 业务返回结果。 |
| |-apiSecret | String | xxxxxx | api签名密钥 |
| |\_callbackUrl | String | https://xxx.xxx.xxx | 回调URL地址。 |
| success | Boolean | true | 操作是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码信息。 |
| request\_id | String | xxxxxxx | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/im/chat/scencegroup/interactivecard/callback/register?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "callback_url":"https://www.dingtalk.com",
        "api_secret":"bgRtxxxx"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/im/chat/scencegroup/interactivecard/callback/register");
OapiImChatScencegroupInteractivecardCallbackRegisterRequest req = new OapiImChatScencegroupInteractivecardCallbackRegisterRequest();
req.setCallbackUrl("https://www.dingtalk.com");
req.setApiSecret("bgRtxxxx");
OapiImChatScencegroupInteractivecardCallbackRegisterResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "result": "{}",
    "success": true,
    "request_id": "uwwsoosy92r0"
}
```

## 错误码

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 40036 | 入参为空 | 根据接口要求，传入必要参数。 |
| 660009 | 回调地址为空 | 请传入回调地址。 |
| 660019 | 回调地址 Url 解析失败 | 确认传入的回调地址是否合法。 |
| -1 | 系统异常 | 重试后如果还是出现此错误，请在开发者后台提交工单。 |
