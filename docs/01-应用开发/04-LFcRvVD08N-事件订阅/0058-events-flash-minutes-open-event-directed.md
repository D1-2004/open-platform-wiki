---
title: "闪记状态变更定向开放事件"
source_url: "https://open.dingtalk.com/document/development/events-flash-minutes-open-event-directed"
namespace: "development"
slug: "events-flash-minutes-open-event-directed"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 闪记状态变更定向开放事件"
doc_id: "Xzb6ymf0Hz"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-flash-minutes-open-event-directed
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 闪记状态变更定向开放事件
> Updated: 2022-01-19 19:29:22

# 闪记状态变更定向开放事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 闪记状态变更定向开放事件 |
| 英文名称 | flash\_minutes\_open\_event\_directed |

## 功能描述

音视频会议闪记的开放接口状态同步事件：

1. 当摘要已生成后，会发送状态同步事件，同步闪记状态为：摘要已生成。
2. 当视频转码或合并完成后，发送状态同步事件，通知闪记状态为：视频已生成 客户接收到该状态后可以通过开放接口获取相关闪记资源。

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
  "eventType": "flash_minutes_open_event_directed",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "openConfModel": {
      "conferenceId": "66f100462fe0c1******aa90",
      "scheduleConferenceId": "5ba0a5ce-xxxx-4a4f-bc68-xxxx81980eea"
    },
    "bizType": "cloud_record",
    "minutesEventType": "summary_generated",
    "minutesTaskId": "115****09"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "flash_minutes_open_event_directed",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "openConfModel": {
    "conferenceId": "66f100462fe0c1******aa90",
    "scheduleConferenceId": "5ba0a5ce-xxxx-4a4f-bc68-xxxx81980eea"
  },
  "bizType": "cloud_record",
  "minutesEventType": "summary_generated",
  "minutesTaskId": "115****09"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=400)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 400,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "openConfModel": {
      "conferenceId": "66f100462fe0c1******aa90",
      "scheduleConferenceId": "5ba0a5ce-xxxx-4a4f-bc68-xxxx81980eea"
    },
    "bizType": "cloud_record",
    "minutesEventType": "summary_generated",
    "syncAction": "flash_minutes_open_event_directed",
    "minutesTaskId": "115****09"
  }
}
```
