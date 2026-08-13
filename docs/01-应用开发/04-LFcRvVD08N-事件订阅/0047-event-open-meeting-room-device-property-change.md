---
title: "设备属性变更"
source_url: "https://open.dingtalk.com/document/development/event-open-meeting-room-device-property-change"
namespace: "development"
slug: "event-open-meeting-room-device-property-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 设备属性变更"
doc_id: "lCIhH8fNJ1"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-open-meeting-room-device-property-change
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 设备属性变更
> Updated: 2022-01-19 19:29:22

# 设备属性变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 设备属性变更 |
| 英文名称 | open\_meeting\_room\_device\_property\_change |

## 功能描述

当钉钉视频会议设备属性变更时，钉钉推送的设备属性变更事件内容。

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
  "eventType": "open_meeting_room_device_property_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "changeTime": 1678095931684,
    "openRoomId": "7263defed6b361fedf0fe6a3b578b96e808b09d6ca6282ed",
    "deviceUnionId": "ErmYnJ7U7FcY27nsDDRVOQiEiE",
    "deviceId": "577944900",
    "properties": [
      {
        "propertyName": "dev_app_status",
        "propertyValue": "conf_running"
      }
    ]
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "open_meeting_room_device_property_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "changeTime": 1678095931684,
  "openRoomId": "7263defed6b361fedf0fe6a3b578b96e808b09d6ca6282ed",
  "deviceUnionId": "ErmYnJ7U7FcY27nsDDRVOQiEiE",
  "deviceId": "577944900",
  "properties": [
    {
      "propertyName": "dev_app_status",
      "propertyValue": "conf_running"
    }
  ]
}
```
