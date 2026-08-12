---
title: "视频会议状态变更App定向推送"
source_url: "https://open.dingtalk.com/document/development/events-meeting-status-change-target-push"
namespace: "development"
slug: "events-meeting-status-change-target-push"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 视频会议状态变更App定向推送"
doc_id: "mjW9UKjyM1"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-meeting-status-change-target-push
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 视频会议状态变更App定向推送
> Updated: 2022-01-19 19:29:22

# 视频会议状态变更App定向推送

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 视频会议状态变更App定向推送 |
| 英文名称 | meeting\_status\_change\_target\_push |

## 功能描述

视频会议状态变更定向推送，目前支持定向推送通过开放接口创建的会议事件，定向推送给调用方所属的应用。

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
  "eventType": "meeting_status_change_target_push",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "openConfModel": {
      "bizType": 0,
      "creatorId": "2iPOLxxxxx",
      "roomCode": "4272xxxxx",
      "title": "开放会议",
      "activeNum": 10,
      "creatorNick": "小钉",
      "attendNum": 15,
      "confDuration": 1000000,
      "conferenceId": "6321*******9b6ed40",
      "startTime": 1663293270000,
      "endTime": 1663294270000,
      "invitedNum": 20,
      "externalLinkUrl": "https://meeting.dingtalk.com/app?roomCode\u003d42726xxx\u0026token\u003d1_7ac9xxx",
      "scheduleConferenceId": "5ba0a5ce-xxxx-4a4f-bc68-xxxx81980eea",
      "status": 1
    },
    "statusSeqNum": 1,
    "changeScene": "conference_created"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "meeting_status_change_target_push",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "openConfModel": {
    "bizType": 0,
    "creatorId": "2iPOLxxxxx",
    "roomCode": "4272xxxxx",
    "title": "开放会议",
    "activeNum": 10,
    "creatorNick": "小钉",
    "attendNum": 15,
    "confDuration": 1000000,
    "conferenceId": "6321*******9b6ed40",
    "startTime": 1663293270000,
    "endTime": 1663294270000,
    "invitedNum": 20,
    "externalLinkUrl": "https://meeting.dingtalk.com/app?roomCode\u003d42726xxx\u0026token\u003d1_7ac9xxx",
    "scheduleConferenceId": "5ba0a5ce-xxxx-4a4f-bc68-xxxx81980eea",
    "status": 1
  },
  "statusSeqNum": 1,
  "changeScene": "conference_created"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=348)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 348,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "openConfModel": {
      "bizType": 0,
      "creatorId": "2iPOLxxxxx",
      "roomCode": "4272xxxxx",
      "title": "开放会议",
      "activeNum": 10,
      "creatorNick": "小钉",
      "attendNum": 15,
      "confDuration": 1000000,
      "conferenceId": "6321*******9b6ed40",
      "startTime": 1663293270000,
      "endTime": 1663294270000,
      "invitedNum": 20,
      "externalLinkUrl": "https://meeting.dingtalk.com/app?roomCode\u003d42726xxx\u0026token\u003d1_7ac9xxx",
      "scheduleConferenceId": "5ba0a5ce-xxxx-4a4f-bc68-xxxx81980eea",
      "status": 1
    },
    "syncAction": "meeting_status_change_target_push",
    "statusSeqNum": 1,
    "changeScene": "conference_created"
  }
}
```
