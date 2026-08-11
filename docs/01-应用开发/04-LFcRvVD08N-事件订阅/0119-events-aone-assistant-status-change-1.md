---
title: "DingTalkA1小助理状态变更"
source_url: "https://open.dingtalk.com/document/development/events-aone-assistant-status-change-1"
namespace: "development"
slug: "events-aone-assistant-status-change-1"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "DingTalk A1 > DingTalkA1小助理状态变更"
doc_id: "Pd3qUJcsGA"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-aone-assistant-status-change-1
> Path: 应用开发 / 事件订阅 / DingTalk A1 > DingTalkA1小助理状态变更
> Updated: 2022-01-19 19:29:22

# DingTalkA1小助理状态变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | DingTalkA1小助理状态变更 |
| 英文名称 | aone\_assistant\_status\_change |

## 功能描述

DingTalkA1小助理状态变更事件

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
  "eventType": "aone_assistant_status_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "agentId": "1234-test",
    "operatorUnionId": "z8zsxxxxxxiEiE",
    "agentStatus": "2"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "aone_assistant_status_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "agentId": "1234-test",
  "operatorUnionId": "z8zsxxxxxxiEiE",
  "agentStatus": "2"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=467)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 467,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "agentId": "1234-test",
    "syncAction": "aone_assistant_status_change",
    "operatorUnionId": "z8zsxxxxxxiEiE",
    "agentStatus": "2"
  }
}
```
