---
title: "钉钉投屏事件"
source_url: "https://open.dingtalk.com/document/development/event-dingtalk-projection"
namespace: "development"
slug: "event-dingtalk-projection"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 钉钉投屏事件"
doc_id: "HSQbPlFtw6"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-dingtalk-projection
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 钉钉投屏事件
> Updated: 2022-01-19 19:29:22

# 钉钉投屏事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 钉钉投屏事件 |
| 英文名称 | dingtalk\_projection |

## 功能描述

钉钉投屏端发起投屏时，产生的钉钉投屏事件数据。

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
  "eventType": "dingtalk_projection",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "unionId": "KiiX59w8ZI***jJZjl3giEiE",
    "projectionConferenceId": "2d2sfsdfeee***291",
    "projectionCode": "511759",
    "projectionBizType": "1",
    "projectionType": "local",
    "sessionId": "mac_5B38DC67-C9****BA-01C9E55AB04F",
    "timestamp": "1677662878594",
    "projectionEventType": "projection_process_start_all"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "dingtalk_projection",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "unionId": "KiiX59w8ZI***jJZjl3giEiE",
  "projectionConferenceId": "2d2sfsdfeee***291",
  "projectionCode": "511759",
  "projectionBizType": "1",
  "projectionType": "local",
  "sessionId": "mac_5B38DC67-C9****BA-01C9E55AB04F",
  "timestamp": "1677662878594",
  "projectionEventType": "projection_process_start_all"
}
```
