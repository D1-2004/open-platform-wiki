---
title: "弹内服务群话题变更事件"
source_url: "https://open.dingtalk.com/document/development/internal-cloud-service-group-topic-change-event"
namespace: "development"
slug: "internal-cloud-service-group-topic-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 弹内服务群话题变更事件"
doc_id: "tOgsblGrS8"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/internal-cloud-service-group-topic-change-event
> Path: 应用开发 / 事件订阅 / 服务群 > 弹内服务群话题变更事件
> Updated: 2022-01-19 19:29:22

# 弹内服务群话题变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 弹内服务群话题变更事件 |
| 英文名称 | servicegroup\_voc\_topic\_detail |

## 功能描述

服务群话题变更事件。

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
  "eventType": "servicegroup_voc_topic_detail",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "body": {
      "bizData": {
        "openTeamId": "kiPoxS9ZR9WsiE",
        "titleSenderNick": "花花",
        "corpId": "dingadc88253b4d581bd35c2f4657eb6378f",
        "groupId": "1111111",
        "channel": "DING_GROUP",
        "source": "DING_CCM",
        "title": "返佣政策啥时候公布",
        "openConversationId": "cidZxwqOqdpqnUu61Q4qHNm6Q\u003d\u003d",
        "orgId": "41661019",
        "labels": "返佣##返佣标准##忽略##返佣政策##公布",
        "groupName": "群名称11111",
        "titleCreateAt": "2021-09-06 20:47:10",
        "participantsNum": "2",
        "titleSenderRole": "SERVER",
        "teamId": "419001",
        "bizTopic": "SG_TOPIC_DETAIL",
        "topic": "返佣标准",
        "chatContext": "[]",
        "msgCount": "10",
        "uniqueId": "b58eb057e7dc84bd39509282ba467630",
        "titleSenderUuid": "2222222"
      }
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "servicegroup_voc_topic_detail",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "body": {
    "bizData": {
      "title_sender_nick": "花花",
      "unique_id": "b58eb057e7dc84bd39509282ba467630",
      "group_name": "群名称11111",
      "open_conversation_id": "cidZxwqOqdpqnUu61Q4qHNm6Q\u003d\u003d",
      "channel": "DING_GROUP",
      "source": "DING_CCM",
      "team_id": "419001",
      "title": "返佣政策啥时候公布",
      "labels": "返佣##返佣标准##忽略##返佣政策##公布",
      "participants_num": "2",
      "chat_context": "[]",
      "title_sender_role": "SERVER",
      "open_team_id": "kiPoxS9ZR9WsiE",
      "title_sender_uuid": "2222222",
      "group_id": "1111111",
      "title_create_at": "2021-09-06 20:47:10",
      "org_id": "41661019",
      "topic": "返佣标准",
      "biz_topic": "SG_TOPIC_DETAIL",
      "corp_id": "dingadc88253b4d581bd35c2f4657eb6378f",
      "msg_count": "10"
    }
  }
}
```
