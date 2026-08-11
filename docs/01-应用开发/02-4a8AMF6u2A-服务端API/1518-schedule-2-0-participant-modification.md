---
title: "修改日程参与者"
source_url: "https://open.dingtalk.com/document/development/schedule-2-0-participant-modification"
namespace: "development"
slug: "schedule-2-0-participant-modification"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 协同办公 > 日程 > 修改日程参与者"
doc_id: "LdK0qdVquP"
updated_at: "2025-09-08 19:03:27"
---

> Source: https://open.dingtalk.com/document/development/schedule-2-0-participant-modification
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 协同办公 > 日程 > 修改日程参与者
> Updated: 2025-09-08 19:03:27

# 修改日程参与者

调用本接口新增或删除日程参与者。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，提供更加规范的接口，钉钉针对日程相关接口进行了升级。本接口文档已于2021年11月09日迁移至**历史文档（不推荐）**目录下，接口不会下线。
>
> - 新版和旧版日程API的ID体系不同，不能混合使用，推荐使用新版日程接口。
> - 已接入的用户建议您根据自身实际情况评估是否切换至新接口。
> - 新接入的用户建议直接使用新接口[修改日程参与者](https://open.dingtalk.com/document/orgapp/add-schedule-participant)。

> **[!NOTE]**
>
> 本接口使用说明：
>
> - 只能修改通过**创建日程**接口创建的日程。
> - 确保已经申请了**修改并查询日程**接口权限。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。详情请参考。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/calendar/v2/attendee/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| calendar\_id | String | 是 | primary | 日历ID。  目前仅支持传**primary**表示修改当前用户“我的日程”下的日程。 |
| event\_id | String | 是 | 053Exxxx | 加密后的日程ID。 |
| attendees | Attendee[] | 是 |  | 参与者列表。 |
| attendee\_status | String | 是 | add | 添加或者删除状态：   - **add**: 添加参会者 - **remove**：删除参会者 |
| userid | String | 是 | user123 | 日程参与者userid。 |
| agentid | Number | 否 | 1212 | 应用对应的AgentId。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码说明。 |
| request\_id | String | zbbs6uxpei1r | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/calendar/v2/attendee/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "agentid": 923680251,
    "event_id": "5E6355BC9BA7D5576D602509E0B3A1FE",
    "calendar_id": "primary",
    "attendees": [
        {
            "userid": "user123",
            "attendee_status": "add"
        }
    ]
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/calendar/v2/attendee/update");
OapiCalendarV2AttendeeUpdateRequest req = new OapiCalendarV2AttendeeUpdateRequest();
req.setCalendarId("primary");
req.setEventId("5E6355BC9BA7D5576D602509E0B3A1FE");
List<Attendee> list2 = new ArrayList<Attendee>();
Attendee obj3 = new Attendee();
list2.add(obj3);
obj3.setAttendeeStatus("add");
obj3.setUserid("user123");
req.setAttendees(list2);
req.setAgentid(923680251L);
OapiCalendarV2AttendeeUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "success": true,
    "request_id": "60b00r1cjwab"
}
```
