---
title: "Teambiton工时变更事件"
source_url: "https://open.dingtalk.com/document/development/event-project-worktime-updated"
namespace: "development"
slug: "event-project-worktime-updated"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 项目管理 > Teambiton工时变更事件"
doc_id: "SLcSImeuQx"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-project-worktime-updated
> Path: 应用开发 / 事件订阅 / 协同 > 项目管理 > Teambiton工时变更事件
> Updated: 2022-01-19 19:29:22

# Teambiton工时变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | Teambiton工时变更事件 |
| 英文名称 | project\_worktime\_updated |

## 功能描述

当Teambiton项目中工时属性内容发生更新时，钉钉通过事件订阅的方式将对应的项目中工时属性内容的变更推送给开发者，用于监听项目中工时属性更新的信息。

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
  "eventType": "project_worktime_updated",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "eventSubType": "worktime.create",
    "executorId": "0715153011125xxxx",
    "created": "2023-04-13T00:00:00Z",
    "approveOpenId": "63c7f91f6ff268bcab40xxxx",
    "action": "re-submit",
    "dates": "2023-04-13T00:00:00Z",
    "userId": "0715153011125xxxx",
    "updated": "2023-04-13T00:00:00Z",
    "workTime": 100000,
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "workTimeIds": [
      "63c7f91f6ff268bcab40xxxx"
    ]
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "project_worktime_updated",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventSubType": "worktime.create",
  "executorId": "0715153011125xxxx",
  "created": "2023-04-13T00:00:00Z",
  "approveOpenId": "63c7f91f6ff268bcab40xxxx",
  "action": "re-submit",
  "dates": "2023-04-13T00:00:00Z",
  "userId": "0715153011125xxxx",
  "updated": "2023-04-13T00:00:00Z",
  "workTime": 100000,
  "taskId": "63c7f91f6ff268bcab40xxxx",
  "workTimeIds": [
    "63c7f91f6ff268bcab40xxxx"
  ]
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=297)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 297,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "eventSubType": "worktime.create",
    "syncAction": "project_worktime_updated",
    "executorId": "0715153011125xxxx",
    "created": "2023-04-13T00:00:00Z",
    "approveOpenId": "63c7f91f6ff268bcab40xxxx",
    "dates": "2023-04-13T00:00:00Z",
    "userId": "0715153011125xxxx",
    "workTime": 100000,
    "action": "re-submit",
    "updated": "2023-04-13T00:00:00Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "workTimeIds": [
      "63c7f91f6ff268bcab40xxxx"
    ]
  }
}
```
