---
title: "获取用户创建的填表模板"
source_url: "https://open.dingtalk.com/document/development/obtains-the-template-that-a-user-creates"
namespace: "development"
slug: "obtains-the-template-that-a-user-creates"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 智能填表 > 获取用户创建的填表模板"
doc_id: "ngXRXVJZbi"
updated_at: "2025-09-08 19:04:53"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-template-that-a-user-creates
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 智能填表 > 获取用户创建的填表模板
> Updated: 2025-09-08 19:04:53

# 获取用户创建的填表模板

调用本接口获取用户创建的填表模板。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对**智能填表**相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于**2022年8月5日**迁移至**历史文档（不推荐）**目录，且**本接口仅保持现有功能，不再新增支持其他能力。**
>
> - 如果未使用本接口，推荐使用新版规范[获取用户创建的填表模板列表](https://open.dingtalk.com/document/orgapp/new-obtains-the-template-that-a-user-creates)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

例如，用户创建了“智能填表测试2”、“智能填表测试”，调用接口后可以获取这2个模板的信息，如下图所示。![智能填表-获取用户创建模板](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5859117361/p353105.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 是 | **[!NOTE]**  暂不支持新增申请。 | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/collection/form/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 - 第三方企业应用可通[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential) |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| biz\_type | Number | 否 | 0 | 填表类型：   - **0**：通用填表 - **1**：教育版填表 |
| creator | String | 否 | manager4220 | 填表创建人的userid。 |
| offset | Number | 是 | 0 | 分页游标，从0开始。后续取返回结果中next\_cursor的值。 |
| size | Number | 是 | 200 | 分页大小，最大200。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 10ly87iw2l0zb | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | PageResult |  | 返回结果。 |
| has\_more | Boolean | true | 是否有下一页数据。 |
| next\_cursor | Number | 62630080661 | 下次分页的起始offset。 |
| list | FormSchemaResponse[] |  | 创建的填表列表。 |
| form\_code | String | PROC-E5BD2166-B6F4-xxxx | 填表code，用此code可调接口获取填表列表。 |
| name | String | 沙龙报名 | 填表名称。 |
| memo | String | 请大家仔细填写，谢谢合作 | 填表提示。 |
| setting | FormSchemaSettingVo |  | 设置。 |
| form\_type | Number | 0 | 表单类型：   - **0**：一次性填表 - **1**：周期性填表 |
| loop\_time | String | 2020-10-15 22:01:18 | 填表时间。 |
| loop\_days | Number[] | 1 | 填表周期，周一到周日分别用1-7表示。 |
| should\_participation\_cnt | Number | 4 | 应填人数。 |
| end\_time | Date | 2020-10-15 22:01:18 | 填表截止时间。 |
| create\_time | Date | 2020-10-15 22:01:18 | 创建时间。 |
| biz\_type | Number | 0 | 填表类型：   - **0**：通用填表 - **1**：教育版填表 |
| stop | Boolean | true | 填表是否终止的标记。 |
| creator | String | manager4220 | 创建人。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/collection/form/list?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "creator":"manager4220",
        "offset":"0",
        "size":"200",
        "biz_type":"0"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/collection/form/list");
OapiCollectionFormListRequest req = new OapiCollectionFormListRequest();
req.setBizType(0L);
req.setCreator("manager4220");
req.setOffset(0L);
req.setSize(200L);
OapiCollectionFormListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "result": {
        "has_more": false,
        "list": [
            {
                "creator": "manager4220",
                "form_code": "PROC-E5BD2166-B6F4-xxxx",
                "memo": "请大家仔细填写，谢谢合作",
                "name": "沙龙报名",
                "setting": {
                    "biz_type": 0,
                    "create_time": "2020-10-15 22:01:18",
                    "form_type": 0,
                    "stop": false
                }
            }
        ],
        "next_cursor": 62630080661
    },
    "request_id": "10ly87iw2l0zb"
}
```
