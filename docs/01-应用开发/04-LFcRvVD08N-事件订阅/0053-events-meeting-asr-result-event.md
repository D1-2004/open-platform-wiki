---
title: "视频会议ASR转写结果开放事件"
source_url: "https://open.dingtalk.com/document/development/events-meeting-asr-result-event"
namespace: "development"
slug: "events-meeting-asr-result-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 视频会议ASR转写结果开放事件"
doc_id: "fbr7ixmOBM"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-meeting-asr-result-event
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 视频会议ASR转写结果开放事件
> Updated: 2022-01-19 19:29:22

# 视频会议ASR转写结果开放事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 视频会议ASR转写结果开放事件 |
| 英文名称 | meeting\_asr\_result\_event |

## 功能描述

会议中的闪记ASR转写识别结果事件。

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
  "eventType": "meeting_asr_result_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "recordId": "1232141245",
    "openConfModel": {
      "conferenceId": "67566af32fe07a026db9a940",
      "scheduleConferenceId": "5c7c9bb1-b256-4dc5-xxxx-xxxxxxxxxxxx"
    },
    "bizType": "minutes : 闪记  cloud_record : 云录制",
    "payload": {
      "result": "可以听到",
      "speakerUnionId": "lmvUrEjpboFrSMtgsiS9V3AiEiE",
      "words": [
        {
          "startTime": 32710,
          "text": "可",
          "endTime": 32770
        }
      ],
      "index": "1",
      "time": "33790",
      "beginTime": "33710"
    },
    "header": {
      "messageNo": "39",
      "name": "TranscriptionResultChanged",
      "messageId": "c76910d55f2649fdab594f572ef442e0"
    },
    "timestamp": 1733716797727
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "meeting_asr_result_event",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "recordId": "1232141245",
  "openConfModel": {
    "conferenceId": "67566af32fe07a026db9a940",
    "scheduleConferenceId": "5c7c9bb1-b256-4dc5-xxxx-xxxxxxxxxxxx"
  },
  "bizType": "minutes : 闪记  cloud_record : 云录制",
  "payload": {
    "result": "可以听到",
    "speakerUnionId": "lmvUrEjpboFrSMtgsiS9V3AiEiE",
    "words": [
      {
        "startTime": 32710,
        "text": "可",
        "endTime": 32770
      }
    ],
    "index": "1",
    "time": "33790",
    "beginTime": "33710"
  },
  "header": {
    "messageNo": "39",
    "name": "TranscriptionResultChanged",
    "messageId": "c76910d55f2649fdab594f572ef442e0"
  },
  "timestamp": 1733716797727
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=411)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 411,
  "biz_data": {
    "recordId": "1232141245",
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "openConfModel": {
      "conferenceId": "67566af32fe07a026db9a940",
      "scheduleConferenceId": "5c7c9bb1-b256-4dc5-xxxx-xxxxxxxxxxxx"
    },
    "bizType": "minutes : 闪记  cloud_record : 云录制",
    "syncAction": "meeting_asr_result_event",
    "payload": {
      "result": "可以听到",
      "speakerUnionId": "lmvUrEjpboFrSMtgsiS9V3AiEiE",
      "words": [
        {
          "startTime": 32710,
          "text": "可",
          "endTime": 32770
        }
      ],
      "index": "1",
      "time": "33790",
      "beginTime": "33710"
    },
    "header": {
      "messageNo": "39",
      "name": "TranscriptionResultChanged",
      "messageId": "c76910d55f2649fdab594f572ef442e0"
    },
    "timestamp": 1733716797727
  }
}
```
