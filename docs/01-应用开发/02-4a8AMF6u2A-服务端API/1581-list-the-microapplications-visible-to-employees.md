---
title: "获取用户可见的企业应用列表"
source_url: "https://open.dingtalk.com/document/development/list-the-microapplications-visible-to-employees"
namespace: "development"
slug: "list-the-microapplications-visible-to-employees"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 应用管理 > 获取用户可见的企业应用列表"
doc_id: "3DVtKEmLb5"
updated_at: "2025-09-08 19:05:18"
---

> Source: https://open.dingtalk.com/document/development/list-the-microapplications-visible-to-employees
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 应用管理 > 获取用户可见的企业应用列表
> Updated: 2025-09-08 19:05:18

# 获取用户可见的企业应用列表

调用本接口获取指定员工可见的应用列表。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对**应用管理**相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于**2022年6月24日**迁移至**历史文档（不推荐）**目录，且**本接口仅保持现有功能，不再新增支持其他能力。**
>
> - 如果未使用本接口，推荐使用新版规范[获取用户可见的企业应用列表](https://open.dingtalk.com/document/orgapp/obtains-the-list-of-enterprise-applications-visible-to-a-user)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

> **[!NOTE]**
>
> 企业内所有应用都可以设置可见范围，本接口以员工维度，获取某个员工可见的应用列表。

![iShot2021-12-22 09](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3318891461/p373883.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 不支持 | — | — |
| 第三方个人应用 | 不支持 | — | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/microapp/list_by_userid`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 |
| userid | String | 是 | user123 | 要查询的员工userid。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| appList | Applist[] |  | 应用信息。 |
| name | String | 智能人事 | 应用名称。 |
| agentId | Number | 828893053 | 应用ID。 |
| appIcon | String | https://static-legacy.dingtalk.com/media/lALxxxx | 用图标地址。 |
| appDesc | String | 智能人事 | 应用描述。 |
| isSelf | Boolean | false | 是否是自建应用：   - **false**：不是 - **true**：自建 |
| appStatus | Number | 1 | 应用状态：   - **1**：启用 - **0**：停用 |
| ompLink | String | https://oa.dingtalk.com/hrmregister/web/index#/personManage | 应用的OA后台管理主页。 |
| homepageLink | String | https://hrmregister.dingtalk.com/hrmregister/mobile/index?xxx | 应用的移动端主页。 |
| pcHomepageLink | String | https://hrmregister.dingtalk.com/hrmregister/pc/index?corpIxx | 应用的PC端主页。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/microapp/list_by_userid?access_token=ACCESS_TOKEN&userid=userid123
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/microapp/list_by_userid");
OapiMicroappListByUseridRequest req = new OapiMicroappListByUseridRequest();
req.setUserid("userid123");
req.setHttpMethod("GET");
OapiMicroappListByUseridResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "appList": [
        {
            "appIcon": "https://static-legacy.dingtalk.com/media/lALPDeC2t-i8V8PM4szk_228_226.png",
            "agentId": 828769847,
            "pcHomepageLink": "https://page.dingtalk.com/wow/dingtalk/act/swsaas?wh_biz=tm&corpId=ding1234",
            "appDesc": "智能办公机器人，即时提醒，快速解答",
            "name": "智能工作助理",
            "homepageLink": "https://page.dingtalk.com/wow/dingtalk/act/smartrobotsetting?corpId=ding1234",
            "appStatus": 1,
            "isSelf": false,
            "ompLink": "https://img.alicdn.com/tfs/TB1qwpVLET1gK0jSZFrXXcNCXXa-1920-723.png"
        },
        {
            "appIcon": "https://static-legacy.dingtalk.com/media/lADPDeC2ve4J0rXMiczI_200_137.jpg",
            "agentId": 872313781,
            "pcHomepageLink": "https://account.aliyun.com/dingtalk/get_ding_talk_oauth?oauth_callback=https%3a%2f%2fwww.aliyun.com%2fdingtalk%2fhome",
            "appDesc": "钉钉工作台做为阿里云移动端统一服务与连接客户的服务窗口。",
            "name": "阿里云工作台",
            "homepageLink": "https://account.aliyun.com/dingtalk/get_ding_talk_oauth?oauth_callback=https%3a%2f%2fwww.aliyun.com%2fdingtalk%2fhome",
            "appStatus": 1,
            "isSelf": false,
            "ompLink": ""
        }
    ]
}
```
