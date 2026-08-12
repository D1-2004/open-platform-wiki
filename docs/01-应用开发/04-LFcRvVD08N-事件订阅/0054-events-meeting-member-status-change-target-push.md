---
title: "视频会议成员状态变更App定向推送"
source_url: "https://open.dingtalk.com/document/development/events-meeting-member-status-change-target-push"
namespace: "development"
slug: "events-meeting-member-status-change-target-push"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 视频会议成员状态变更App定向推送"
doc_id: "9EfDKBKAOS"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-meeting-member-status-change-target-push
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 视频会议成员状态变更App定向推送
> Updated: 2022-01-19 19:29:22

# 视频会议成员状态变更App定向推送

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 视频会议成员状态变更App定向推送 |
| 英文名称 | meeting\_member\_status\_change\_target\_push |

## 功能描述

视频会议成员状态变更定向推送，目前支持定向推送通过开放接口创建的会议成员事件，定向推送给调用方所属的应用。

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
  "eventType": "meeting_member_status_change_target_push",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "openMemberModels": [
      {
        "duration": 1000,
        "leaveTime": 1663143344000,
        "deviceType": "Android",
        "pstnJoin": false,
        "joinTime": 1663143334000,
        "userNick": "会议参会者",
        "conferenceId": "6321*******9b6ed40",
        "attendStatus": 3,
        "host": false,
        "coHost": true,
        "userId": "2iPO*********wiEiE"
      }
    ],
    "statusSeqNum": 2,
    "changeScene": "user_join"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "meeting_member_status_change_target_push",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "openMemberModels": [
    {
      "duration": 1000,
      "leaveTime": 1663143344000,
      "deviceType": "Android",
      "pstnJoin": false,
      "joinTime": 1663143334000,
      "userNick": "会议参会者",
      "conferenceId": "6321*******9b6ed40",
      "attendStatus": 3,
      "host": false,
      "coHost": true,
      "userId": "2iPO*********wiEiE"
    }
  ],
  "statusSeqNum": 2,
  "changeScene": "user_join"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=349)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 349,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "meeting_member_status_change_target_push",
    "openMemberModels": [
      {
        "duration": 1000,
        "leaveTime": 1663143344000,
        "deviceType": "Android",
        "pstnJoin": false,
        "joinTime": 1663143334000,
        "userNick": "会议参会者",
        "conferenceId": "6321*******9b6ed40",
        "attendStatus": 3,
        "host": false,
        "coHost": true,
        "userId": "2iPO*********wiEiE"
      }
    ],
    "statusSeqNum": 2,
    "changeScene": "user_join"
  }
}
```
