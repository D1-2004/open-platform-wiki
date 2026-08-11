---
title: "上传文件块"
source_url: "https://open.dingtalk.com/document/development/upload-file-blocks"
namespace: "development"
slug: "upload-file-blocks"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 文件上传 > 上传文件块"
doc_id: "UWRf3DcLuL"
updated_at: "2025-09-08 19:06:59"
---

> Source: https://open.dingtalk.com/document/development/upload-file-blocks
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 文件上传 > 上传文件块
> Updated: 2025-09-08 19:06:59

# 上传文件块

本接口为文件分块上传中间环节，传输文件块，除最后一块外每块的大小不得小于100KB，最大不超过超过8M。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，提供更加规范的接口，钉钉针对**钉盘**产品进行了升级，目前已升级为**存储**产品。本接口文档已于2023年01月17日迁移至**历史文档（不推荐）**目录下，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用存储产品[获取文件上传信息](https://open.dingtalk.com/document/orgapp/obtain-storage-upload-information)和[提交文件](https://open.dingtalk.com/document/orgapp/submit-documents)接口。
> - 如果已使用本接口，建议您根据自身实际情况切换至推荐接口。

> **[!NOTE]**
>
> - 浏览器可能会转义某些字符导致请求失败，调试时请使用curl或者代码模拟请求。
> - 请保证自己的机器有足够的出口带宽，否则可能导致上传异常缓慢。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/file/upload/chunk`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用，通过[获取第三方企业应用的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |
| upload\_id | String | 是 | lAzPDgCwxxxx | 上传事务ID。 |
| agent\_id | String | 是 | 868810166 | 应用的AgentId。   - 企业内部应用可以在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。 - 第三方企业应用可以调用[获取企业授权信息](https://open.dingtalk.com/document/isvapp/obtains-the-basic-information-of-an-enterprise)接口获取。 |
| chunk\_sequence | Long | 是 | 1 | 文件块号，从1开始计数。  **[!NOTE]**  开启分块上传事务接口中，将文件分为几块，就循环调用本接口几次，直到最后一块文件上传成功后，再调用提交文件上传事务接口，获取media\_id。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| file | FileItem | 是 | C:/Users/Desktop/222.txt | 文件内容。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| media\_id | String | #iAEHAqRmaWxlA6 | 文件的唯一标识media\_id。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
POST /file/upload/chunk?access_token=ACCESSTOKEN&agent_id=AGENTID&upload_id=UPLOADID&chunk_sequence=1 HTTP/1.1
Host:oapi.dingtalk.com
Content-Type: multipart/form-data;
```

**请求示例（JAVA SDK）**

```
OapiFileUploadChunkRequest request = new OapiFileUploadChunkRequest();
request.setAgentId("13xxxxx01");
request.setChunkSequence(1L);
request.setUploadId("99F0F6DBB55A4C82822268192B5909F8_0#iAEAAqRmaWxlA6h5dW5kaXNrMATOC7DaowXNCW0GzQlXB85a863FCM4AAXTG");
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/file/upload/chunk?"+WebUtils.buildQuery(request.getTextParams(),"utf-8"));
request = new OapiFileUploadChunkRequest();
request.setFile(new FileItem("/Users/mxh/Downloads/test.png"));
OapiFileUploadChunkResponse response = client.execute(request,accessToken);
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok"
}
```
