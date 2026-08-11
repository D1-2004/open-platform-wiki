---
title: "服务号接收用户交互"
source_url: "https://open.dingtalk.com/document/development/service-number-receive-user-interaction"
namespace: "development"
slug: "service-number-receive-user-interaction"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 服务窗 > 服务号接收用户交互"
doc_id: "x6dXM4Xx0t"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/service-number-receive-user-interaction
> Path: 应用开发 / 事件订阅 / 组织关系 > 服务窗 > 服务号接收用户交互
> Updated: 2022-01-19 19:29:22

# 服务号接收用户交互

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务号接收用户交互 |
| 英文名称 | isw\_user\_event\_received |

## 功能描述

服务号收到用户的交互事件, 目前只有菜单点击事件。

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
  "eventType": "isw_user_event_received",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "toUser": "abab1201",
    "actionType": "click",
    "fromUser": "abab124",
    "createTime": 1442027997327,
    "actionKey": "V001_TODAY_AIR"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "isw_user_event_received",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "toUser": "abab1201",
  "actionType": "click",
  "fromUser": "abab124",
  "createTime": 1442027997327,
  "actionKey": "V001_TODAY_AIR"
}
```
