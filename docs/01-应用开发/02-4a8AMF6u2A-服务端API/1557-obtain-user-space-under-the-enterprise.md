---
title: "获取企业下的自定义空间"
source_url: "https://open.dingtalk.com/document/development/obtain-user-space-under-the-enterprise"
namespace: "development"
slug: "obtain-user-space-under-the-enterprise"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 获取企业下的自定义空间"
doc_id: "Zpgaf3Ji8W"
updated_at: "2025-09-08 19:06:36"
---

> Source: https://open.dingtalk.com/document/development/obtain-user-space-under-the-enterprise
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 获取企业下的自定义空间
> Updated: 2025-09-08 19:06:36

# 获取企业下的自定义空间

调用本接口获取企业下的自定义空间。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，提供更加规范的接口，钉钉针对**钉盘**产品进行了升级，目前已升级为**存储**产品。本接口文档后续将迁移至**历史文档（不推荐）**目录下，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用存储产品[添加空间](https://open.dingtalk.com/document/orgapp/add-space)接口。
> - 如果已使用本接口，建议您根据自身实际情况切换至推荐接口。

针对企业或ISV的个性化需求，钉钉在企业下开辟了自定义空间来供企业或ISV使用：

- 每个企业可以自定义若干存储空间，如使用preview空间来存放需要预览的文件。
- 每个存储空间不能有重名的文件（全路径）。
- 不同存储空间可以存在同名文件。
- 不同存储空间的文件是隔离的，不会相互影响。
- 企业下的自定义空间属于企业，共享使用企业的容量，其中的文件只有企业内部人员才可能有权限访问，访问需要企业或ISV进行授权。
- 每个ISV的应用在企业下对应一个自定义空间。这些存储空间在钉钉客户端不可见，在电脑管理后台可以查看其占用企业空间的情况。

> **[!IMPORTANT]**
>
> 浏览器可能会转义某些字符导致请求失败，调试时请使用curl或者代码模拟请求。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 钉盘访问权限 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingtalk.oapi.cspace.get_custom_space) |
| 第三方企业应用 | 是 | 钉盘访问权限 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=dingtalk.oapi.cspace.get_custom_space) |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/cspace/get_custom_space`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用，通过[获取第三方企业应用的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |
| domain | String | 是 | aaa | 企业调用时传入，需要为10个字节以内的字符串，仅可包含字母和数字，大小写不敏感。 |
| agent\_id | String | 否 | 86881016 | 应用的AgentId。   - 企业内部应用可以在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。 - 第三方企业应用可以调用[获取企业授权信息](https://open.dingtalk.com/document/isvapp/obtains-the-basic-information-of-an-enterprise)接口获取。   **[!NOTE]**  第三方企业应用调用时，该参数必传。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| spaceid | String | 4006896815 | 获取到的空间ID。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/cspace/get_custom_space?access_token=ACCESS_TOKEN&domain=aaa&agent_id=123
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/cspace/get_custom_space");
OapiCspaceGetCustomSpaceRequest req = new OapiCspaceGetCustomSpaceRequest();
req.setDomain("aaa");
req.setAgentId("123");
req.setHttpMethod("GET");
OapiCspaceGetCustomSpaceResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "spaceid": 4006896815
}
```
