---
title: "设备绑定会议室变更"
source_url: "https://open.dingtalk.com/document/development/event-open-meeting-room-device-bind-change"
namespace: "development"
slug: "event-open-meeting-room-device-bind-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 设备绑定会议室变更"
doc_id: "n8NuT1hxgo"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-open-meeting-room-device-bind-change
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 设备绑定会议室变更
> Updated: 2022-01-19 19:29:22

# 设备绑定会议室变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 设备绑定会议室变更 |
| 英文名称 | open\_meeting\_room\_device\_bind\_change |

## 功能描述

当钉钉视频会议设备绑定、解绑钉钉会议室时，钉钉推送的设备绑定会议室变更事件内容。

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
  "eventType": "open_meeting_room_device_bind_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "operateTime": 1678089509609,
    "openRoomId": "96f5fde38c89021c3bb6dd2ee365c4e8808b09d6ca6282ed",
    "deviceUnionId": "NHG8h6XIe3NzjPaO1sWzMAiEiE",
    "operatorUnionId": "aRHcUT4yHjdzjPaO1sWzMAiEiE",
    "type": "bind",
    "deviceId": "1980190595"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "open_meeting_room_device_bind_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "operateTime": 1678089509609,
  "openRoomId": "96f5fde38c89021c3bb6dd2ee365c4e8808b09d6ca6282ed",
  "deviceUnionId": "NHG8h6XIe3NzjPaO1sWzMAiEiE",
  "operatorUnionId": "aRHcUT4yHjdzjPaO1sWzMAiEiE",
  "type": "bind",
  "deviceId": "1980190595"
}
```
