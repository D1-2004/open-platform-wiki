---
title: "授权预览审批附件"
source_url: "https://open.dingtalk.com/document/development/preview-authorization-attachment"
namespace: "development"
slug: "preview-authorization-attachment"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 授权预览审批附件"
doc_id: "OZO8mhzxQZ"
updated_at: "2025-09-08 19:04:38"
---

> Source: https://open.dingtalk.com/document/development/preview-authorization-attachment
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 授权预览审批附件
> Updated: 2025-09-08 19:04:38

# 授权预览审批附件

调用本接口授权预览审批附件。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对OA审批相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2022年10月8日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[授权预览审批附件](https://open.dingtalk.com/document/orgapp/preview-authorization-attachment-pop)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

> **[!IMPORTANT]**
>
> 此接口需配合钉盘JSAPI使用，调用本接口只支持授予审批附件组件中文件的预览权限，不支持授予审批评论附件的预览权限。
>
> 使用方法如下：
>
> 1. 调用[获取审批钉盘空间信息](https://open.dingtalk.com/document/orgapp/query-the-space-of-an-approval-nail)接口，获取审批钉盘空间space\_id。
> 2. 根据space\_id，调用H5微应用-[上传附件到钉盘/从钉盘选择文件](https://open.dingtalk.com/document/orgapp/upload-attachment-to-nail-plate-select-file-from-nail-plate-h5)接口或者小程序[上传附件到钉盘/从钉盘选择文件](https://open.dingtalk.com/document/orgapp/upload-attachment-to-nail-plate-select-file-from-nail-plate)接口，获取上传附件的信息。
> 3. 调用[发起审批实例](https://open.dingtalk.com/document/orgapp/initiate-approval)接口，获取审批实例process\_instance\_id。
> 4. 根据上述获取信息，调用本文接口，授权用户审批附件预览权限。每一次预览审批附件前，都需要调用该接口进行授权。
> 5. 调用H5微应用[预览钉盘文件](https://open.dingtalk.com/document/orgapp/preview-nail-plate-file)或者小程序[钉盘文件预览](https://open.dingtalk.com/document/orgapp/nail-plate-file-preview)接口，进行预览。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/processinstance/cspace/preview`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 - 第三方企业应用可通[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential) |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | GrantCspaceRequest | 是 |  | 请求信息。 |
| agentid | Number | 否 | 868810166 | 应用标识。可在开发者后台的应用详情页获取。 |
| process\_instance\_id | String | 是 | a17444d1-075b-4a4d-xxxx | 实例ID   - 企业内部应用   可通过[获取审批实例ID列表](https://open.dingtalk.com/document/orgapp/operation-to-retrieve-a-list-of)接口获取。   - 第三方企业应用   可以通过推送的审批事件中获取，参考[biz\_type=22](https://open.dingtalk.com/document/isvapp/approval-events-3#section-m8l-k59-3qb)。 |
| file\_id | String | 是 | 11 | 审批附件ID。  **[!NOTE]**  file\_id必须与发起审批实例中附件组件中的文件fileId保持一致，否则出现无权限错误信息。 |
| userid | String | 是 | user123 | 授权允许预览附件的用户userid。 |
| fileid\_list | String[] | 否 | 123 | 附件ID列表，支持批量授权，最大列表长度：20。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | OK | 返回码描述。 |
| result | AppSpaceResponse |  | 授权结果。 |
| space\_id | Number | 1 | 审批所在的钉盘空间ID。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 3vp6ui8jeroa | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/processinstance/cspace/preview?access_token=ACCESS_TOKEN
```

请求正文

```
{
   "request":{
      "agentid":868810166,
      "file_id":"11",
      "process_instance_id":"a17444d1-075b-4a4d-xxxx",
      "userid":"manager4220"
   }
}
```

**请求示例（JAVA SDK）**

```
  DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/processinstance/cspace/preview");
  OapiProcessinstanceCspacePreviewRequest req = new OapiProcessinstanceCspacePreviewRequest();
  GrantCspaceRequest grantCspaceRequest = new GrantCspaceRequest();
  grantCspaceRequest.setAgentid(868810166L);
  grantCspaceRequest.setProcessInstanceId("a17444d1-075b-4a4d-xxxx");
  grantCspaceRequest.setFileId("11");
  grantCspaceRequest.setUserid("manager4220");
  req.setRequest(grantCspaceRequest);
  OapiProcessinstanceCspacePreviewResponse rsp = client.execute(req, access_token);
  System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "result":{
                "space_id":"1"
        },
        "errcode":0,
        "request_id": "3vp6ui8jeroa"
}
```
