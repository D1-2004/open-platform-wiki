---
title: "发送钉盘文件给指定用户"
source_url: "https://open.dingtalk.com/document/development/sends-a-file-to-a-specified-user"
namespace: "development"
slug: "sends-a-file-to-a-specified-user"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 发送钉盘文件给指定用户"
doc_id: "uE3OPEwzXz"
updated_at: "2025-09-08 19:06:34"
---

> Source: https://open.dingtalk.com/document/development/sends-a-file-to-a-specified-user
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 发送钉盘文件给指定用户
> Updated: 2025-09-08 19:06:34

# 发送钉盘文件给指定用户

调用本接口将文件发送给指定用户，用户将收到以应用名义发送的一条文件消息。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，提供更加规范的接口，钉钉针对**钉盘**产品进行了升级，目前已升级为**存储**产品。本接口文档后续将迁移至**历史文档（不推荐）**目录下，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用存储产品[以应用身份发送文件给指定用户](https://open.dingtalk.com/document/orgapp/sends-a-storage-file-to-a-specified-user)接口。
> - 如果已使用本接口，建议您根据自身实际情况切换至推荐接口。

> **[!IMPORTANT]**
>
> 浏览器可能会转义某些字符导致请求失败，调试时请使用curl或者代码模拟请求。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 钉盘访问权限 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingtalk.oapi.cspace.add_to_single_chat) |
| 第三方企业应用 | 是 | 钉盘访问权限 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=dingtalk.oapi.cspace.add_to_single_chat) |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/cspace/add_to_single_chat`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用，通过[获取第三方企业应用的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| file\_name | String | 是 | 文件.pdf | 文件名包含扩展名，需要utf-8 urlEncode。 |
| media\_id | String | 是 | @123456 | 文件media\_id。   - 企业内部应用，调用[单步文件上传](https://open.dingtalk.com/document/orgapp/single-step-file-upload)接口或者[开启分块上传事务](https://open.dingtalk.com/document/orgapp/enable-upload-transaction)接口获取。 - 第三方企业应用，调用[单步文件上传](https://open.dingtalk.com/document/isvapp/single-step-file-upload)接口或者[开启分块上传事务](https://open.dingtalk.com/document/isvapp/multipart-upload)接口获取。   **[!NOTE]**  参数需要utf-8 urlEncode处理。 |
| userid | String | 是 | 123456 | 文件接收人的userid。 |
| agent\_id | String | 是 | 123 | 文件发送者应用的AgentId。   - 企业内部应用可以在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。 - 第三方企业应用可以调用[获取企业授权信息](https://open.dingtalk.com/document/isvapp/obtains-the-basic-information-of-an-enterprise)接口获取。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/cspace/add_to_single_chat?access_token=ACCESS_TOKEN&agent_id=AGENT_ID&userid=USERID&media_id=MEDIA_ID&file_name=FILE_NAME
```

请求正文

```
{
        "agent_id":"868810166",
        "file_name":"test",
        "media_id":"@lAzPDgCwPn1mJiDOQoLp0s5xiBws",
        "userid":"manager4220"
}
```

**请求示例（JAVA SDK）**

```
OapiCspaceAddToSingleChatRequest request = new OapiCspaceAddToSingleChatRequest();
request.setAgentId("135xxx601");
request.setUserid("01376xxxxxx479");
request.setMediaId("#iAEAAqRmaWxlA6h5dW5kaXNrMATOC7DaowXNCW0GzQlXB85a863FCM4AAXTG");
request.setFileName("文件.pdf");
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/cspace/add_to_single_chat?"+WebUtils.buildQuery(request.getTextParams(),"utf-8"));
OapiCspaceAddToSingleChatResponse response = client.execute(request, accessToken);
```

**返回示例**

```
{
        "errcode":0,
        "errmsg":"ok"
}
```
