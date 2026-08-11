---
title: "套件票据"
source_url: "https://open.dingtalk.com/document/development/event-suite-ticket"
namespace: "development"
slug: "event-suite-ticket"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "身份与免登 > 套件票据"
doc_id: "RUtDfsITHa"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-suite-ticket
> Path: 应用开发 / 事件订阅 / 身份与免登 > 套件票据
> Updated: 2022-01-19 19:29:22

# 套件票据

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 套件票据 |
| 英文名称 | suite\_ticket |

## 功能描述

数据为第三方企业应用票据最新suiteTicket，定时每5个小时推送一次。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "suite_ticket",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "suiteTicket": "QsfJCEVF1h6E9fAaGwnAzbvYzxxxxxxxx"
  }
}
```

SyncHTTP/RDS推送

高优先级事件，为RDS推送方式时，数据插入表open\_sync\_biz\_data中。SyncHTTP推送方式时EventType为SYNC\_HTTP\_PUSH\_HIGH。

### **biz\_data数据示例(biz\_type=2)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 2,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "suite_ticket",
    "suiteTicket": "QsfJCEVF1h6E9fAaGwnAzbvYzxxxxxxxx"
  }
}
```
