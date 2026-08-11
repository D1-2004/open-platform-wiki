---
title: "直播结束数据处理完成事件"
source_url: "https://open.dingtalk.com/document/development/event-live-statistic-done-event"
namespace: "development"
slug: "event-live-statistic-done-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 直播 > 直播结束数据处理完成事件"
doc_id: "q4SC5Abx5r"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-live-statistic-done-event
> Path: 应用开发 / 事件订阅 / 音视频 > 直播 > 直播结束数据处理完成事件
> Updated: 2022-01-19 19:29:22

# 直播结束数据处理完成事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 直播结束数据处理完成事件 |
| 英文名称 | live\_statistic\_done\_event |

## 功能描述

直播相关的事件回调，直播结束数据处理任务完成事件数据说明。

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
  "eventType": "live_statistic_done_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "finishTime": 166011401308,
    "liveId": "1fc2eaca-****-****-****-b23e1bda4225"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "live_statistic_done_event",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "finishTime": 166011401308,
  "liveId": "1fc2eaca-****-****-****-b23e1bda4225"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=229)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 229,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "finishTime": 166011401308,
    "syncAction": "live_statistic_done_event",
    "liveId": "1fc2eaca-****-****-****-b23e1bda4225"
  }
}
```
