---
title: "待办任务删除"
source_url: "https://open.dingtalk.com/document/development/event-todo-task-delete"
namespace: "development"
slug: "event-todo-task-delete"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > 待办 > 待办任务删除"
doc_id: "Elg5rtQiV1"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-todo-task-delete
> Path: 应用开发 / 事件订阅 / 办公 > 待办 > 待办任务删除
> Updated: 2022-01-19 19:29:22

# 待办任务删除

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 待办任务删除 |
| 英文名称 | todo\_task\_delete |

## 功能描述

删除钉钉待办任务信息时，会触发待办任务删除事件。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "todo_task_delete",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "unionIdList": [
      "QWRGux2l4MuiSa0vxxxEiE"
    ],
    "taskId": "task98cd5581178bfc6f123800dxxx"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "todo_task_delete",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "taskId": "task98cd5581178bfc6f123800dxxx",
  "UnionIdList": [
    "QWRGux2l4MuiSa0vxxxEiE"
  ]
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=109)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 109,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "todo_task_delete",
    "taskId": "task98cd5581178bfc6f123800dxxx",
    "UnionIdList": [
      "QWRGux2l4MuiSa0vxxxEiE"
    ]
  }
}
```
