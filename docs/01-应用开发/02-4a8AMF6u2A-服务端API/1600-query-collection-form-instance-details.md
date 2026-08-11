---
title: "获取实例详情"
source_url: "https://open.dingtalk.com/document/development/query-collection-form-instance-details"
namespace: "development"
slug: "query-collection-form-instance-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 智能填表 > 获取实例详情"
doc_id: "XiMS38qsGG"
updated_at: "2025-09-08 19:04:55"
---

> Source: https://open.dingtalk.com/document/development/query-collection-form-instance-details
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 智能填表 > 获取实例详情
> Updated: 2025-09-08 19:04:55

# 获取实例详情

本接口用于根据表单实例ID获取表单实例详情。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对**智能填表**相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于**2022年8月5日**迁移至**历史文档（不推荐）**目录，且**本接口仅保持现有功能，不再新增支持其他能力。**
>
> - 如果未使用本接口，推荐使用新版规范[获取单条填表实例详情](https://open.dingtalk.com/document/orgapp/obtains-the-instance-details-of-a-single-fill-table)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

例如，第2条回复的表单实例ID是620faa73-915f-41ae-8ab7-7d27589a314a，调用接口后，可以获取到第2条回复的详细内容。![智能填表-获取实例详情](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7102317361/p353148.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/collection/instance/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| formInstance\_id | String | 是 | ea4bc238-6155-xxxx | 表单实例ID，可调用[获取填表实例数据](https://open.dingtalk.com/document/orgapp/obtains-multiple-form-filling-records)接口获取。 |
| biz\_type | Number | 否 | 0 | 表单类型：   - **0**：通用填表 - **1**：教育版填表 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码信息。 |
| result | FormInstanceVo |  | 表单详细信息。 |
| form\_code | String | PROC-E5BD2166-xxxx | 表单code。 |
| title | String | 沙龙报名 | 标题。 |
| creator | String | 10203029011 | 创建者userid。 |
| create\_time | Date | 2020-11-19 17:40:39 | 创建时间。 |
| modify\_time | Date | 2020-11-19 17:40:39 | 修改时间。 |
| form\_list | FormData[] |  | 表单信息。 |
| label | String | 你喜欢的主题 | 表单标签名。 |
| key | String | TextareaField\_KGAW58AQ | 控件名。 |
| value | String | 低代码开发 | 表单值。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/collection/instance/get?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "formInstance_id":"ea4bc238-6155-466f-9b4a-c5944977b737",
        "biz_type":"0"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/collection/instance/get");
OapiCollectionInstanceGetRequest req = new OapiCollectionInstanceGetRequest();
req.setFormInstanceId("aaa");
req.setBizType(0L);
OapiCollectionInstanceGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "result": {
        "create_time": "2020-11-19 17:40:39",
        "creator": "10203029011219896",
        "form_code": "PROC-E5BD2166-B6F4-49C3-A662-8F956B0C442E",
        "form_list": [
            {
                "key": "TextareaField_KGAW58AQ",
                "label": "你希望的主题",
                "value": "都希望能有一天能够实现"
            },
            {
                "key": "HiddenField_interval",
                "value": "21208"
            }
        ],
        "modify_time": "2020-11-19 17:40:39",
        "title": "沙龙报名"
    },
    "request_id": "sybxpsuxb6hs"
}
```
