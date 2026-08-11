---
title: "获取模板code"
source_url: "https://open.dingtalk.com/document/development/obtains-the-template-code-based-on-the-template-name"
namespace: "development"
slug: "obtains-the-template-code-based-on-the-template-name"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 获取模板code"
doc_id: "15oFA2ERsw"
updated_at: "2025-09-08 19:04:42"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-template-code-based-on-the-template-name
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 获取模板code
> Updated: 2025-09-08 19:04:42

# 获取模板code

调用本接口根据模板名称查询process\_code。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对OA审批相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2023年1月9日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[获取模板code](https://open.dingtalk.com/document/orgapp/obtain-the-template-code)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

调用本文接口可实现根据审批模板名称获取对应的模板code，如下图所示。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7686925661/p500674.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。详情请参考[权限申请](https://open.dingtalk.com/document/app/permission-application-and-basic-concepts#topic-1948077)。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/get_by_name`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用，通过[获取第三方企业应用的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| name | String | 是 | 事假 | 模板名称。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 47fn7lwjrxyt | 请求ID。 |
| process\_code | String | PROC-C54B2B | 模板code。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/get_by_name?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "name":"自定义审批模板"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/get_by_name");
OapiProcessGetByNameRequest req = new OapiProcessGetByNameRequest();
req.setName("自定义审批模板");
OapiProcessGetByNameResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "process_code": "PROC-C54B2B4E-BE61-4DDD-8A63-AB372E64028E",
    "request_id": "47fn7lwjrxyt"
}
```

## 错误码

| **错误码（errorcode）** | **错误码描述（errmsg）** | **错误原因** | **解决方案** |
| --- | --- | --- | --- |
| 43007 | 需要授权 | access\_token不正确 | 请确认access\_token是否正确 |
| 8100017 | 没有访问权限 | 没有访问审批表单的权限 | 请确认表单name参数是否正确 |
| 40056 | 无效的微应用ID | 微应用ID参数错误 | 请确认微应用ID是否正确 |
| 40083 | 无效的suiteKey | 应用suiteKey参数错误 | 请确认应用suiteKey是否正确 |
| -1 | 系统繁忙 | 系统繁忙 | 请稍后重试 |
| 400001 | 系统繁忙 | 系统繁忙 | 请稍后重试 |
| 820004 | 模板不存在 | 模板name参数错误 | 请确认表单name参数是否正确 |
