---
title: "直播状态变更"
source_url: "https://open.dingtalk.com/document/development/event-live-status-change-event"
namespace: "development"
slug: "event-live-status-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 直播 > 直播状态变更"
doc_id: "Q69qs8bKPA"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-live-status-change-event
> Path: 应用开发 / 事件订阅 / 音视频 > 直播 > 直播状态变更
> Updated: 2022-01-19 19:29:22

# 直播状态变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 直播状态变更 |
| 英文名称 | live\_status\_change\_event |

## 功能描述

该文档为直播状态变化事件推送数据说明。

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
  "eventType": "live_status_change_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "liveId": "1fc2eaca-****-****-****-b23e1bda4225",
    "liveStatus": 3
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "live_status_change_event",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "liveId": "1fc2eaca-****-****-****-b23e1bda4225",
  "liveStatus": 3
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=220)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 220,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "live_status_change_event",
    "liveId": "1fc2eaca-****-****-****-b23e1bda4225",
    "liveStatus": 3
  }
}
```
