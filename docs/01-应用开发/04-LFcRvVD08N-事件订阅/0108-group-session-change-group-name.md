---
title: "群会话更换群名称"
source_url: "https://open.dingtalk.com/document/development/group-session-change-group-name"
namespace: "development"
slug: "group-session-change-group-name"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "即时通讯 IM > 会话管理 > 群会话更换群名称"
doc_id: "RnTxcVsCp7"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/group-session-change-group-name
> Path: 应用开发 / 事件订阅 / 即时通讯 IM > 会话管理 > 群会话更换群名称
> Updated: 2022-01-19 19:29:22

# 群会话更换群名称

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 群会话更换群名称 |
| 英文名称 | chat\_update\_title |

## 功能描述

开发者监听群回调事件可以更及时地响应群的变化，与业务集成。该文档为群会话更换群名称事件数据说明。

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
  "eventType": "chat_update_title",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "timeStamp": 1608027247528,
    "chatId": "chat676e50a07xxxx",
    "corpId": "dinge8a56572f80bxxxx",
    "operatorUnionId": "ZPbvHDqDOxxxxLLtBDplS",
    "title": "开放平台",
    "openConversationId": "cidmfWxxxx",
    "operator": "user456"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "chat_update_title",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "timeStamp": 1608027247528,
  "chatId": "chat676e50a07xxxx",
  "corpId": "dinge8a56572f80bxxxx",
  "operatorUnionId": "ZPbvHDqDOxxxxLLtBDplS",
  "title": "开放平台",
  "openConversationId": "cidmfWxxxx",
  "operator": "user456"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=181)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 181,
  "biz_data": {
    "timeStamp": 1608027247528,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "chatId": "chat676e50a07xxxx",
    "corpId": "dinge8a56572f80bxxxx",
    "syncAction": "chat_update_title",
    "operatorUnionId": "ZPbvHDqDOxxxxLLtBDplS",
    "title": "开放平台",
    "openConversationId": "cidmfWxxxx",
    "operator": "user456"
  }
}
```
