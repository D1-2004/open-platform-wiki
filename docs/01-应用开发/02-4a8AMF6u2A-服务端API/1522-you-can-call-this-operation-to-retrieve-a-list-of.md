---
title: "获取指定用户可见的审批表单列表"
source_url: "https://open.dingtalk.com/document/development/you-can-call-this-operation-to-retrieve-a-list-of"
namespace: "development"
slug: "you-can-call-this-operation-to-retrieve-a-list-of"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 获取指定用户可见的审批表单列表"
doc_id: "t2l7pvBxWw"
updated_at: "2025-09-08 19:04:35"
---

> Source: https://open.dingtalk.com/document/development/you-can-call-this-operation-to-retrieve-a-list-of
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 获取指定用户可见的审批表单列表
> Updated: 2025-09-08 19:04:35

# 获取指定用户可见的审批表单列表

调用本接口根据员工的userid分页获取该用户可见的审批表单列表，每次最多获取100个表单。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对OA审批相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2022年10月8日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[获取指定用户可见的审批表单列表](https://open.dingtalk.com/document/orgapp/obtains-a-list-of-approval-forms-visible-to-the-specified)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

调用本接口，可以展示指定用户可见的审批表单列表。![用户可见1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0017796361/p352514.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/listbyuserid`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 - 第三方企业应用可通[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential) |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 否 | manager7078 | 要查询的员工的userId。  不传表示查询企业下所有审批表单。 |
| offset | Number | 是 | 0 | 分页游标，从0开始。根据返回结果里的next\_cursor是否为空来判断是否还有下一页，且再次调用时offset设置成next\_cursor的值。 |
| size | Number | 是 | 100 | 分页大小，最大可设置成100。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 72hy9suzb5cg | 请求ID。 |
| errmsg | String | ok | 返回描述。 |
| errcode | Number | 0 | 返回码。 |
| result | HomePageProcessTemplateVo |  | 查询结果。 |
| process\_list | ProcessTopVo[] |  | 可见表单列表。 |
| name | String | 物品领用 | 表单名称。 |
| icon\_url | String | https://gw.xxxx/T-102-102.png | 图标URL。 |
| process\_code | String | PROC-YMLA1-xxxx-11WFJ-1 | 表单唯一标识。 |
| url | String | https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?xxxx | 表单URL。 |
| next\_cursor | Number | 2 | 下一次分页调用的offset值，当返回结果里没有nextCursor时，表示分页结束。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/listbyuserid?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "userid":"manager7078",
    "offset": 0,
    "size": "100"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/listbyuserid");
OapiProcessListbyuseridRequest req = new OapiProcessListbyuseridRequest();
req.setUserid("manager7078");
req.setOffset(0L);
req.setSize(100L);
OapiProcessListbyuseridResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "result": {
        "next_cursor": 2,
        "process_list": [
            {
                "icon_url": "https://gw.xxxx/T-102-102.png",
                "name": "物品领用",
                "process_code": "PROC-YMLA1-xxxx-11WFJ-1",
                "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?xxxx"
            },
            {
                "icon_url": "https://gw.xxxx/T-102-103.png",
                "name": "通用审批",
                "process_code": "PROC-YMLA1-xxxx-11WFJ-2",
                "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?xxxx"
            }
        ]
    },
    "request_id": "72hy9suzb5cg"
}
```
