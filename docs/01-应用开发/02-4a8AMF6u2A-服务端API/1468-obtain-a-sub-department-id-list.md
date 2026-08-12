---
title: "获取子部门ID列表"
source_url: "https://open.dingtalk.com/document/development/obtain-a-sub-department-id-list"
namespace: "development"
slug: "obtain-a-sub-department-id-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 部门管理1.0(不推荐) > 获取子部门ID列表"
doc_id: "ovdZVoq8Pa"
updated_at: "2025-09-08 19:07:36"
---

> Source: https://open.dingtalk.com/document/development/obtain-a-sub-department-id-list
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 通讯录管理 > 部门管理1.0(不推荐) > 获取子部门ID列表
> Updated: 2025-09-08 19:07:36

# 获取子部门ID列表

调用本接口获取子部门ID列表。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，提供更加规范的接口，钉钉针对通讯录**用户管理**和**部门管理**接口进行了升级，**用户管理1.0**、**部门管理1.0**的接口文档已于2021年10月21日迁移至**历史文档（不推荐）**目录下，且**用户管理1.0和部门管理1.0接口将不再添加新的能力，仅保持原有功能。**
>
> - 如果未接入1.0版接口，推荐使用新的[用户管理](https://open.dingtalk.com/document/orgapp/user-information-creation)、[部门管理](https://open.dingtalk.com/document/orgapp/create-a-department-v2)接口。
> - 如果已接入1.0版接口，建议您根据自身实际情况评估是否切换至新接口。

> **[!NOTE]**
>
> 该接口不受授权范围限制，产品方案商可以根据该接口完成企业部门的遍历。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/department/list_ids`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6ed1bxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |
| id | String | 是 | 1 | 部门ID，查询根部门输入1。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| sub\_dept\_id\_list | Number[] | [379661095,399388496] | 子部门ID列表。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/department/list_ids?access_token=ACCESS_TOKEN&id=1
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/department/list_ids");
OapiDepartmentListIdsRequest req = new OapiDepartmentListIdsRequest();
req.setId("1");
req.setHttpMethod("GET");
OapiDepartmentListIdsResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "sub_dept_id_list": [
        379661095,
        399388496
    ],
    "errmsg": "ok"
}
```
