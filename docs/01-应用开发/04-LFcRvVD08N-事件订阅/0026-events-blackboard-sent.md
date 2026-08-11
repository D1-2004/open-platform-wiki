---
title: "公告发送"
source_url: "https://open.dingtalk.com/document/development/events-blackboard-sent"
namespace: "development"
slug: "events-blackboard-sent"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 公告 > 公告发送"
doc_id: "16t95tbE8i"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-blackboard-sent
> Path: 应用开发 / 事件订阅 / 协同 > 公告 > 公告发送
> Updated: 2022-01-19 19:29:22

# 公告发送

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 公告发送 |
| 英文名称 | blackboard\_sent |

## 功能描述

发送公告的事件数据。如果选择了定时发布，那么会在公告真正被发出来的时候才会触发。

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
  "eventType": "blackboard_sent",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "unionId": "AlmxxxxwiEiE",
    "receivers": {
      "openConversationIds": "[\"12345\"]",
      "labelIds": "[100]",
      "staffIds": "[\"20240418\",\"20240419\"]",
      "dgCodes": "[\"abc\"]",
      "deptIds": "[123,456]"
    },
    "blackboardType": "blackboard",
    "dentry": {
      "sourceDentryUuid": "O0002Gg0l5BW7Z9XEdgk8v000YbnKEek"
    },
    "blackboardId": "300a540d6b94005d8638f16e00603ae9",
    "categoryName": "规则制度",
    "categoryId": "e000462b5a92c1000d63b1f2dd00029e"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "blackboard_sent",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "unionId": "AlmxxxxwiEiE",
  "receivers": {
    "openConversationIds": "[\"12345\"]",
    "labelIds": "[100]",
    "staffIds": "[\"20240418\",\"20240419\"]",
    "dgCodes": "[\"abc\"]",
    "deptIds": "[123,456]"
  },
  "blackboardType": "blackboard",
  "dentry": {
    "sourceDentryUuid": "O0002Gg0l5BW7Z9XEdgk8v000YbnKEek"
  },
  "blackboardId": "300a540d6b94005d8638f16e00603ae9",
  "categoryName": "规则制度",
  "categoryId": "e000462b5a92c1000d63b1f2dd00029e"
}
```
