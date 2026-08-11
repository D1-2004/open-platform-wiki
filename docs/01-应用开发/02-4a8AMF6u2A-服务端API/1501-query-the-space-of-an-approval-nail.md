---
title: "获取审批钉盘空间信息"
source_url: "https://open.dingtalk.com/document/development/query-the-space-of-an-approval-nail"
namespace: "development"
slug: "query-the-space-of-an-approval-nail"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 获取审批钉盘空间信息"
doc_id: "1EDhejZaWH"
updated_at: "2025-09-08 19:04:37"
---

> Source: https://open.dingtalk.com/document/development/query-the-space-of-an-approval-nail
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 获取审批钉盘空间信息
> Updated: 2025-09-08 19:04:37

# 获取审批钉盘空间信息

调用本接口获取审批钉盘空间的ID并授予当前用户上传附件的权限。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对OA审批相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2022年10月8日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[获取审批钉盘空间信息](https://open.dingtalk.com/document/orgapp/obtains-the-information-about-approval-nail-disk)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

建议开发者通过以下方式实现带附件的审批流程：

1. 调用**本接口**，获取钉盘空间的上传权限，并获取space\_id。
2. 使用参数space\_id

   - 企业内部应用，通过H5微应用[上传附件到钉盘/从钉盘选择文件](https://open.dingtalk.com/document/orgapp/upload-attachment-to-nail-plate-select-file-from-nail-plate-h5)或者小程序[上传附件到钉盘/从钉盘选择文件](https://open.dingtalk.com/document/orgapp/upload-attachment-to-nail-plate-select-file-from-nail-plate)后获取钉盘附件的信息。
   - 企业三方企业应用，通过H5微应用[上传附件到钉盘/从钉盘选择文件](https://open.dingtalk.com/document/isvapp/upload-attachments-to-the-nail-plate-or-select-files-from)或者小程序[上传附件到钉盘/从钉盘选择文件](https://open.dingtalk.com/document/isvapp/upload-attachment-to-nail-plate-select-file-from-nail-plate)后获取钉盘附件信息

   space\_id的使用说明：

   > **[!NOTE]**
   >
   > - 一个企业内审批附件钉盘spaceid是唯一的。
   > - 此接口有授权上传权限的作用，每次调用上传附件API接口前，建议使用上传操作人userid再调用一次本接口。
   > - 审批附件钉盘，属于企业钉盘的一部分，占用的是企业钉盘空间，但是审批附件钉盘空间和其中的文件在客户端内是不可见的。
3. 企业内部应用调用[发起审批实例](https://open.dingtalk.com/document/orgapp/initiate-approval)接口；第三方企业应用调用[发起审批实例](https://open.dingtalk.com/document/isvapp/initiate-approval)传递附件信息。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/processinstance/cspace/info`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 - 第三方企业应用可通[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential) |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| user\_id | String | 是 | abcdef | 用户的userid。 |
| agent\_id | String | 否 | 8345000 | 应用的agentid。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | AppSpaceResponse |  | 返回结果。 |
| space\_id | Number | 3996960664 | 钉盘空间ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回描述。 |
| request\_id | String | 7jdciddady4z | 请求ID。 |
| success | Boolean | true | 调用是否成功。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/processinstance/cspace/info?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "user_id":"manager4220",
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/processinstance/cspace/info");
OapiProcessinstanceCspaceInfoRequest req = new OapiProcessinstanceCspaceInfoRequest();
req.setUserId("manager4220");
OapiProcessinstanceCspaceInfoResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "result": {
        "space_id": 3996960664
    },
    "success": true,
    "errmsg":"ok",
    "request_id": "7jdciddady4z"
}
```
