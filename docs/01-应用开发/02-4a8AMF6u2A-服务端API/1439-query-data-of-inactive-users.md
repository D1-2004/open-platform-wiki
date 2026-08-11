---
title: "获取未登录钉钉的员工列表"
source_url: "https://open.dingtalk.com/document/development/query-data-of-inactive-users"
namespace: "development"
slug: "query-data-of-inactive-users"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 获取未登录钉钉的员工列表"
doc_id: "hsJ3OMDehI"
updated_at: "2025-09-08 19:07:30"
---

> Source: https://open.dingtalk.com/document/development/query-data-of-inactive-users
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 获取未登录钉钉的员工列表
> Updated: 2025-09-08 19:07:30

# 获取未登录钉钉的员工列表

调用本接口查询指定日期内未登录钉钉的企业员工列表。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，提供更加规范的接口，钉钉针对通讯录**用户管理**和**部门管理**接口进行了升级，**用户管理1.0**、**部门管理1.0**的接口文档已于2021年10月21日迁移至**历史文档（不推荐）**目录下，且**用户管理1.0和部门管理1.0接口将不再添加新的能力，仅保持原有功能。**
>
> - 如果未接入1.0版接口，推荐使用新的[用户管理](https://open.dingtalk.com/document/orgapp/user-information-creation)、[部门管理](https://open.dingtalk.com/document/orgapp/create-a-department-v2)接口。
> - 如果已接入1.0版接口，建议您根据自身实际情况评估是否切换至新接口。

> **[!NOTE]**
>
> - 每天9点后调用接口才能确保获取前一天数据。
> - 调用本接口只能获取一个月内未登录钉钉的员工列表。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/inactive/user/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| query\_date | String | 是 | 20190808 | 查询日期，日期格式为yyyyMMdd。 |
| offset | Number | 是 | 0 | 支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。 |
| size | Number | 是 | 100 | 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | PageVo |  | 未登录用户数据。 |
| has\_more | Boolean | true | 是否有更多数据。   - **true**：是 - **false**：否 |
| list | String[] | ["user123","user456"] | 用户列表。 |
| request\_id | String | 16n58y0i9mk4l | 请求ID。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/inactive/user/get?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "offset":1,
        "size":100,
        "query_date":"20190808"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/inactive/user/get");
OapiInactiveUserGetRequest req = new OapiInactiveUserGetRequest();
req.setQueryDate("20190808");
req.setOffset(1L);
req.setSize(100L);
OapiInactiveUserGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "result": {
        "has_more": false,
        "list": ["usxxxx3","uxxxx6"]
    },
    "request_id": "16n58y0i9mk4l"
}
```
