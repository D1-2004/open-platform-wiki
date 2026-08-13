---
title: "设备告警事件"
source_url: "https://open.dingtalk.com/document/development/event-open-meeting-room-device-alarm"
namespace: "development"
slug: "event-open-meeting-room-device-alarm"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 设备告警事件"
doc_id: "Z6FpggqFBO"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-open-meeting-room-device-alarm
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 设备告警事件
> Updated: 2022-01-19 19:29:22

# 设备告警事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 设备告警事件 |
| 英文名称 | open\_meeting\_room\_device\_alarm |

## 功能描述

钉钉视频会议设备发生告警时，钉钉推送的设备告警事件内容。

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
  "eventType": "open_meeting_room_device_alarm",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "ruleLevel": 1,
    "alarmTime": 1678091092976,
    "eventStatus": 0,
    "eventDescription": "App/6.0.6-Release.1000064",
    "deviceUnionId": "cny8R8PFjhuYmpiP6zbcGdwiEiE",
    "ruleKey": "device_offline_lwp",
    "deviceId": "546587609"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "open_meeting_room_device_alarm",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "ruleLevel": 1,
  "alarmTime": 1678091092976,
  "eventStatus": 0,
  "eventDescription": "App/6.0.6-Release.1000064",
  "deviceUnionId": "cny8R8PFjhuYmpiP6zbcGdwiEiE",
  "ruleKey": "device_offline_lwp",
  "deviceId": "546587609"
}
```
