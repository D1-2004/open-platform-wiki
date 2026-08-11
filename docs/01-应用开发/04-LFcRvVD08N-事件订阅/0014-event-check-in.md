---
title: "用户签到"
source_url: "https://open.dingtalk.com/document/development/event-check-in"
namespace: "development"
slug: "event-check-in"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 签到 > 用户签到"
doc_id: "53fFr0V8Lc"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-check-in
> Path: 应用开发 / 事件订阅 / 协同 > 签到 > 用户签到
> Updated: 2022-01-19 19:29:22

# 用户签到

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 用户签到 |
| 英文名称 | check\_in |

## 功能描述

签到事件数据说明。

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
  "eventType": "check_in",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "timeStamp": 1495542282000,
    "staffId": "08058xxxxxx"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "check_in",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "timeStamp": 1495542282000,
  "staffId": "08058xxxxxx"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=318)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 318,
  "biz_data": {
    "timeStamp": 1495542282000,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "check_in",
    "staffId": "08058xxxxxx"
  }
}
```
