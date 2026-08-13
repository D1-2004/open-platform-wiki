---
title: "审批任务开始，结束，转交"
source_url: "https://open.dingtalk.com/document/development/event-bpms-task-change"
namespace: "development"
slug: "event-bpms-task-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > OA审批 > 审批任务开始，结束，转交"
doc_id: "UVpm3LGZsj"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-bpms-task-change
> Path: 应用开发 / 事件订阅 / 办公 > OA审批 > 审批任务开始，结束，转交
> Updated: 2022-01-19 19:29:22

# 审批任务开始，结束，转交

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 审批任务开始，结束，转交 |
| 英文名称 | bpms\_task\_change |

## 功能描述

当审批事件发生审批任务开始、结束、转交时，推送给订阅者的内容。

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
  "eventType": "bpms_task_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "result": "agree",
    "processInstanceId": "ce133dd0-5b22-9516-xxxxxxxxxxxx",
    "finishTime": 1670983893000,
    "createTime": 1670983873000,
    "processCode": "PROC-27BBC5E6-DFFA-4EC3-A1F1-xxx",
    "bizCategoryId": "attendance.goout",
    "businessId": "20xxxx38",
    "remark": "同意",
    "type": "finish",
    "title": "考勤-测试",
    "taskId": 811165,
    "staffId": "08058646137"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "bpms_task_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "result": "agree",
  "processInstanceId": "ce133dd0-5b22-9516-xxxxxxxxxxxx",
  "finishTime": 1670983893000,
  "createTime": 1670983873000,
  "processCode": "PROC-27BBC5E6-DFFA-4EC3-A1F1-xxx",
  "bizCategoryId": "attendance.goout",
  "businessId": "20xxxx38",
  "remark": "同意",
  "type": "finish",
  "title": "考勤-测试",
  "taskId": 811165,
  "staffId": "08058646137"
}
```
