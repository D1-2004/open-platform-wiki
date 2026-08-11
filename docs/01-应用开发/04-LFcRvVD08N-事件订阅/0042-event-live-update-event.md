---
title: "直播信息修改"
source_url: "https://open.dingtalk.com/document/development/event-live-update-event"
namespace: "development"
slug: "event-live-update-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 直播 > 直播信息修改"
doc_id: "Io80geyqwJ"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-live-update-event
> Path: 应用开发 / 事件订阅 / 音视频 > 直播 > 直播信息修改
> Updated: 2022-01-19 19:29:22

# 直播信息修改

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 直播信息修改 |
| 英文名称 | live\_update\_event |

## 功能描述

该文档为直播状态变化的数据推送说明。

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
  "eventType": "live_update_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "coverUrl": "http://xxx.png",
    "preEndTime": 1660268147000,
    "title": "测试直播",
    "liveId": "1fc2eaca-****-****-****-b23e1bda4225",
    "preStartTime": 1660266147700,
    "introduction": "测试直播简介"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "live_update_event",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "coverUrl": "http://xxx.png",
  "preEndTime": 1660268147000,
  "title": "测试直播",
  "liveId": "1fc2eaca-****-****-****-b23e1bda4225",
  "preStartTime": 1660266147700,
  "introduction": "测试直播简介"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=221)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 221,
  "biz_data": {
    "coverUrl": "http://xxx.png",
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "live_update_event",
    "preEndTime": 1660268147000,
    "title": "测试直播",
    "liveId": "1fc2eaca-****-****-****-b23e1bda4225",
    "preStartTime": 1660266147700,
    "introduction": "测试直播简介"
  }
}
```
