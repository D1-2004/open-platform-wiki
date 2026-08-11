---
title: "群会话添加人员"
source_url: "https://open.dingtalk.com/document/development/group-session-add-persons"
namespace: "development"
slug: "group-session-add-persons"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "即时通讯 IM > 会话管理 > 群会话添加人员"
doc_id: "BED6iH4jfK"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/group-session-add-persons
> Path: 应用开发 / 事件订阅 / 即时通讯 IM > 会话管理 > 群会话添加人员
> Updated: 2022-01-19 19:29:22

# 群会话添加人员

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 群会话添加人员 |
| 英文名称 | chat\_add\_member |

## 功能描述

开发者监听群回调事件可以更及时地响应群的变化，与业务集成。该文档为群会话添加人员事件字段说明。

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
  "eventType": "chat_add_member",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "timeStamp": 1608027106990,
    "unionId": [
      "3rBUxxxQiEiE"
    ],
    "chatId": "chat28367b03e4b4ca4b5074e1dbfb5d6088",
    "corpId": "dinge8a56572f80bxxxx",
    "operatorUnionId": "iis6fGqqqt87xxxxiEiE",
    "eventType": "chat_add_member",
    "userId": [
      "user456"
    ],
    "openConversationId": "iis6fGqqqt87xxxxiEiE",
    "operator": "10203029011219896"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "chat_add_member",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "timeStamp": 1608027106990,
  "unionId": [
    "3rBUxxxQiEiE"
  ],
  "chatId": "chat28367b03e4b4ca4b5074e1dbfb5d6088",
  "corpId": "dinge8a56572f80bxxxx",
  "operatorUnionId": "iis6fGqqqt87xxxxiEiE",
  "eventType": "chat_add_member",
  "userId": [
    "user456"
  ],
  "openConversationId": "iis6fGqqqt87xxxxiEiE",
  "operator": "10203029011219896"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=177)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 177,
  "biz_data": {
    "timeStamp": 1608027106990,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "unionId": [
      "3rBUxxxQiEiE"
    ],
    "chatId": "chat28367b03e4b4ca4b5074e1dbfb5d6088",
    "corpId": "dinge8a56572f80bxxxx",
    "syncAction": "chat_add_member",
    "operatorUnionId": "iis6fGqqqt87xxxxiEiE",
    "eventType": "chat_add_member",
    "userId": [
      "user456"
    ],
    "openConversationId": "iis6fGqqqt87xxxxiEiE",
    "operator": "10203029011219896"
  }
}
```
