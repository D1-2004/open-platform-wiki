---
title: "预计算时长"
source_url: "https://open.dingtalk.com/document/development/calculate-duration-based-on-attendance-scheduling"
namespace: "development"
slug: "calculate-duration-based-on-attendance-scheduling"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 协同办公 > 考勤 > 预计算时长"
doc_id: "erii904pjn"
updated_at: "2025-09-08 19:03:19"
---

> Source: https://open.dingtalk.com/document/development/calculate-duration-based-on-attendance-scheduling
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 协同办公 > 考勤 > 预计算时长
> Updated: 2025-09-08 19:03:19

# 预计算时长

调用本接口，根据考勤系统的排班情况，预计算员工加班、出差及请假的时长信息。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，提供更加规范的接口，钉钉对本文档接口进行了升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)，本接口文档将于 **2024 年 6 月 11 日**迁移至**历史文档**目录，且本接口**仅保持现有功能，不再新增支持其他能力**。
>
> - 如果未使用本接口，推荐使用新版[预计算时长](https://open.dingtalk.com/document/orgapp/api-calculateduration)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

例如，企业某员工11月2日排班（上班时间09:00，下班时间18:00），11月3日排休。

该员工计划需要请假，请假开始时间是11月02日的09:00:00，结束是11月3日的18:00:00，那么调用本接口可获取这个请假时长范围内，该员工预计请假的时长只有一天。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 考勤组查询权限 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingtalk.oapi.attendance.approve.duration.calculate) |
| 第三方企业应用 | 是 | 考勤组查询权限 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=dingtalk.oapi.attendance.approve.duration.calculate) |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/attendance/approve/duration/calculate`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用，通过[获取第三方企业应用的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager123 | 员工的userId。 |
| biz\_type | Number | 是 | 3 | 审批单类型：   - **1**：加班 - **2**：出差 - **3**：请假 |
| from\_time | String | 是 | 2019-08-15 | 开始时间。开始时间不能早于当前时间前31天。  支持以下格式：   - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43 |
| to\_time | String | 是 | 2019-08-17 | 结束时间。   - biz\_type为1时，结束时间减去开始时间不能超过1天。 - biz\_type为2或3时，结束时间减去开始时间的天数不能超过31天。   支持以下格式：   - 2019-08-15 - 2019-08-15 AM - 2019-08-15 12:43 |
| duration\_unit | String | 是 | day | 时长单位，支持格式如下：   - day - halfDay - hour：biz\_type为1时仅支持hour。   时间格式必须与时长单位对应：   - 2019-08-15对应day - 2019-08-15 AM对应halfDay - 2019-08-15 12:43对应hour |
| calculate\_model | Number | 是 | 1 | 计算方法：   - **0**：按自然日计算 - **1**：按工作日计算 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | TopDurationVo | demo | 返回结果。 |
| duration | String | 2.0 | 总时长，该字段的单位与本企业内对应审批单设置的单位一致。 |
| duration\_details | TopDayDurationVo[] | demo | 详细信息。 |
| date | String | 2019-08-15 | 日期。 |
| duration | String | 1.0 | 每日时长，该字段的单位与本企业内对应审批单设置的单位一致。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/attendance/approve/duration/calculate?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "biz_type":"3",
        "calculate_model":"1",
        "to_time":"2019-08-17",
        "userid":"dd_dd",
        "from_time":"2019-08-15",
        "duration_unit":"day"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/approve/duration/calculate");
OapiAttendanceApproveDurationCalculateRequest req = new OapiAttendanceApproveDurationCalculateRequest();
req.setUserid("dd_dd");
req.setBizType(3L);
req.setFromTime("2019-08-15");
req.setToTime("2019-08-17");
req.setDurationUnit("day");
req.setCalculateModel(1L);
OapiAttendanceApproveDurationCalculateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode":0,
    "errmsg":"ok",
    "result":{
        "duration":"2.0",
        "duration_details":[
            {
                    "date":"2019-08-15",
                    "duration":"1.0"
            }
        ]
    }
}
```
