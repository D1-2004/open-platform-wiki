---
title: "获取日志统计数据"
source_url: "https://open.dingtalk.com/document/development/query-log-statistics"
namespace: "development"
slug: "query-log-statistics"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 协同办公 > 日志 > 获取日志统计数据"
doc_id: "oG0dIG1XWk"
updated_at: "2025-09-08 19:03:30"
---

> Source: https://open.dingtalk.com/document/development/query-log-statistics
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 协同办公 > 日志 > 获取日志统计数据
> Updated: 2025-09-08 19:03:30

# 获取日志统计数据

调用本接口，获取日志的已读人数、评论条数、评论人数、点赞人数。

> **[!IMPORTANT]**
>
> 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的[数据资产类OpenAPI](https://open.dingtalk.com/document/dataservice/data-asset-interface-adjustment-description)接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)获取相应的数据服务。
> 2. 本文档已于 2023 年 9 月 1 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力，说明如下：
>
>    - 如果未使用本接口，推荐使用[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。
>    - 如果已使用本接口，建议您根据自身实际情况评估是否切换至[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。

调用本接口，如下图所示，可获取日志的已读人数、评论条数、评论人数、点赞人数。

![日志统计信息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6680518361/p359458.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 查询企业员工日志权限 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/report/statistics`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| report\_id | String | 是 | 174xxxx | 日志ID。   - 调用[获取用户发送日志的概要信息](https://open.dingtalk.com/document/orgapp/view-log-summary-data)接口获取report\_id参数值。 - 调用[获取用户发出的日志列表](https://open.dingtalk.com/document/orgapp/query-logs-sent-by-an-employee)接口获取report\_id参数值。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ReportStatisticsVo |  | 返回结果。 |
| read\_num | Number | 1 | 已读人数。 |
| comment\_num | Number | 1 | 评论个数。 |
| comment\_user\_num | Number | 1 | 去重后的评论人数。 |
| like\_num | Number | 1 | 点赞人数。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 43knzyjc6f2b | 请求ID。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/report/statistics?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "report_id":"174xxxx"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/statistics");
OapiReportStatisticsRequest req = new OapiReportStatisticsRequest();
req.setReportId("174xxxx");
OapiReportStatisticsResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "result": {
        "comment_num": 1,
        "comment_user_num": 1,
        "like_num": 1,
        "read_num": 0
    },
    "success": true,
    "request_id": "43knzyjc6f2b"
}
```
