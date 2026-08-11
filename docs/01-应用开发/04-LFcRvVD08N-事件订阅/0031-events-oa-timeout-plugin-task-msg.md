---
title: "OA限时审批事件变更"
source_url: "https://open.dingtalk.com/document/development/events-oa-timeout-plugin-task-msg"
namespace: "development"
slug: "events-oa-timeout-plugin-task-msg"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > OA审批 > OA限时审批事件变更"
doc_id: "CWkrttlpXZ"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-oa-timeout-plugin-task-msg
> Path: 应用开发 / 事件订阅 / 办公 > OA审批 > OA限时审批事件变更
> Updated: 2022-01-19 19:29:22

# OA限时审批事件变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | OA限时审批事件变更 |
| 英文名称 | oa\_timeout\_plugin\_task\_msg |

## 功能描述

OA限时审批事件，在OA限时审批插件通知相应人员的时候，同时推送给客户业务系统，用于客户业务系统处理内部业务逻辑。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "oa_timeout_plugin_task_msg",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "msg": "{\\\"taskExeTime\\\":1734679849000,\\\"actionType\\\":\\\"remind\\\",\\\"taskContent\\\":\\\"{\\\\\\\"expiresUnit\\\\\\\":\\\\\\\"days\\\\\\\",\\\\\\\"activityId\\\\\\\":\\\\\\\"1918_5cd3\\\\\\\",\\\\\\\"groups\\\\\\\":{\\\\\\\"reminders\\\\\\\":[{\\\\\\\"name\\\\\\\":\\\\\\\"当前审批人\\\\\\\",\\\\\\\"id\\\\\\\":\\\\\\\"approver\\\\\\\",\\\\\\\"type\\\\\\\":\\\\\\\"sys\\\\\\\"}],\\\\\\\"actionType\\\\\\\":\\\\\\\"remind\\\\\\\",\\\\\\\"triggerUnit\\\\\\\":\\\\\\\"minutes\\\\\\\",\\\\\\\"triggerAtMoment\\\\\\\":\\\\\\\"2024-11-26T09:38:03.003Z\\\\\\\",\\\\\\\"id\\\\\\\":\\\\\\\"L0JB9762\\\\\\\",\\\\\\\"triggerTime\\\\\\\":3,\\\\\\\"remindTypes\\\\\\\":[\\\\\\\"dingMsg\\\\\\\"],\\\\\\\"addTaskRemark\\\\\\\":true},\\\\\\\"id\\\\\\\":\\\\\\\"L0JB975Z\\\\\\\",\\\\\\\"triggerType\\\\\\\":1,\\\\\\\"expiresTime\\\\\\\":0}\\\",\\\"userIds\\\":[\\\"1451694214729725262\\\"],\\\"isRemind\\\":true,\\\"pluginTaskId\\\":1870008191718281218,\\\"triggerType\\\":1}",
    "activityId": "1918_123",
    "instanceId": "qVJvZ-123",
    "corpId": "ding123",
    "processCode": "PROC-123",
    "sysParam": {},
    "msgTag": "taskTrigger",
    "taskId": "90935123"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "oa_timeout_plugin_task_msg",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "msg": "{\\\"taskExeTime\\\":1734679849000,\\\"actionType\\\":\\\"remind\\\",\\\"taskContent\\\":\\\"{\\\\\\\"expiresUnit\\\\\\\":\\\\\\\"days\\\\\\\",\\\\\\\"activityId\\\\\\\":\\\\\\\"1918_5cd3\\\\\\\",\\\\\\\"groups\\\\\\\":{\\\\\\\"reminders\\\\\\\":[{\\\\\\\"name\\\\\\\":\\\\\\\"当前审批人\\\\\\\",\\\\\\\"id\\\\\\\":\\\\\\\"approver\\\\\\\",\\\\\\\"type\\\\\\\":\\\\\\\"sys\\\\\\\"}],\\\\\\\"actionType\\\\\\\":\\\\\\\"remind\\\\\\\",\\\\\\\"triggerUnit\\\\\\\":\\\\\\\"minutes\\\\\\\",\\\\\\\"triggerAtMoment\\\\\\\":\\\\\\\"2024-11-26T09:38:03.003Z\\\\\\\",\\\\\\\"id\\\\\\\":\\\\\\\"L0JB9762\\\\\\\",\\\\\\\"triggerTime\\\\\\\":3,\\\\\\\"remindTypes\\\\\\\":[\\\\\\\"dingMsg\\\\\\\"],\\\\\\\"addTaskRemark\\\\\\\":true},\\\\\\\"id\\\\\\\":\\\\\\\"L0JB975Z\\\\\\\",\\\\\\\"triggerType\\\\\\\":1,\\\\\\\"expiresTime\\\\\\\":0}\\\",\\\"userIds\\\":[\\\"1451694214729725262\\\"],\\\"isRemind\\\":true,\\\"pluginTaskId\\\":1870008191718281218,\\\"triggerType\\\":1}",
  "activityId": "1918_123",
  "instanceId": "qVJvZ-123",
  "corpId": "ding123",
  "processCode": "PROC-123",
  "sysParam": {},
  "msgTag": "taskTrigger",
  "taskId": "90935123"
}
```
