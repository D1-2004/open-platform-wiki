---
title: "获取当前企业所有可管理的表单"
source_url: "https://open.dingtalk.com/document/development/obtains-the-information-about-all-manageable-templates-of-the-current"
namespace: "development"
slug: "obtains-the-information-about-all-manageable-templates-of-the-current"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 获取当前企业所有可管理的表单"
doc_id: "zJGXaU4wLD"
updated_at: "2025-09-08 19:04:36"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-information-about-all-manageable-templates-of-the-current
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 获取当前企业所有可管理的表单
> Updated: 2025-09-08 19:04:36

# 获取当前企业所有可管理的表单

调用本接口获取当前企业所有可管理的审批表单。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对OA审批相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2022年10月8日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[获取当前企业所有可管理的表单](https://open.dingtalk.com/document/orgapp/get-all-manageable-forms-for-the-current-enterprise)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

> **[!IMPORTANT]**
>
> 调用本接口，userid对应的人员必须拥有该企业OA审批的权限。

调用本接口，获取在当前企业，该用户可以管理的表单。比如，用户可以管理“审批模板测试”，调用该接口，只能获取到“审批模板测试”表单的信息。![表单管理1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2217796361/p352513.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/template/manage/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | user123 | 用户的userid。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ProcessSimpleVO[] |  | 模版列表。 |
| icon\_name | String | common | 模板图标名。 |
| flow\_title | String | 通用审批 | 模版名称。 |
| process\_code | String | PROC-44E84FC1-16E2-4A69-BB3C-xxxx | 模版code。 |
| gmt\_modified | Date | 2020-07-14 14:24:59 | 修改时间。 |
| attendance\_type | Number | 0 | 关联考勤类型，取值。   - **0**：无 - **1**：补卡申请 - **2**：请假 |
| icon\_url | String | `https://gw.alicdn.com/tfs/xxxx-112-112.png` | 图标URL地址。 |
| is\_new\_process | Boolean | false | 是否新模版。 |
| success | Boolean | true | 调用是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | o1ud59ekq12g | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/template/manage/get?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "userid":"user123"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/template/manage/get");
OapiProcessTemplateManageGetRequest req = new OapiProcessTemplateManageGetRequest();
req.setUserid("user123");
OapiProcessTemplateManageGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "result": [
        {
            "attendance_type": 0,
            "flow_title": "物品领用",
            "gmt_modified": "2020-07-14 14:24:59",
            "icon_name": "common",
            "icon_url": "https://gw.alicdn.com/tfs/xxxx-112-112.png",
            "is_new_process": false,
            "process_code": "PROC-E580A0F2-AAAE-4B7C-B42A-xxxx"
        },
        {
            "attendance_type": 0,
            "flow_title": "通用审批",
            "gmt_modified": "2020-07-14 14:24:59",
            "icon_name": "common",
            "icon_url": "https://gw.alicdn.com/tfs/xxxx-112-112.png",
            "is_new_process": false,
            "process_code": "PROC-598BB40C-9C32-4C60-9EA0-xxxx"
        },
        {
            "attendance_type": 0,
            "flow_title": "采购",
            "gmt_modified": "2020-07-14 14:24:59",
            "icon_name": "procurement",
            "icon_url": "https://gw.alicdn.com/tfs/TB1oQi.xxxx-112-112.png",
            "is_new_process": false,
            "process_code": "PROC-44E84FC1-16E2-4A69-BB3C-xxxx"
        }
    ],
    "success": true,
    "request_id": "o1ud59ekq12g"
}
```
