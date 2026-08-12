---
title: "群模板被启用或停用"
source_url: "https://open.dingtalk.com/document/development/group-templates-are-enabled-or-disabled"
namespace: "development"
slug: "group-templates-are-enabled-or-disabled"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "即时通讯 > 会话管理 > 群模板被启用或停用"
doc_id: "m6hhdsEUUr"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/group-templates-are-enabled-or-disabled
> Path: 应用开发 / 事件订阅 / 即时通讯 > 会话管理 > 群模板被启用或停用
> Updated: 2022-01-19 19:29:22

# 群模板被启用或停用

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 群模板被启用或停用 |
| 英文名称 | chat\_template\_change |

## 功能描述

群模板被启用或停用时，给订阅了该事件的开发者推送的数据。

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
  "eventType": "chat_template_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "timeStamp": 43535463645,
    "operatorUnionId": "evdsxxx",
    "templateId": "1111abcd-1234-1234-dcba-123456789012",
    "changedTimeStamp": 43535463645,
    "openConversationId": "cidff2312123ee",
    "operator": "manager0112",
    "status": "on"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "chat_template_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "timeStamp": 43535463645,
  "operatorUnionId": "evdsxxx",
  "templateId": "1111abcd-1234-1234-dcba-123456789012",
  "changedTimeStamp": 43535463645,
  "openConversationId": "cidff2312123ee",
  "operator": "manager0112",
  "status": "on"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=306)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 306,
  "biz_data": {
    "timeStamp": 43535463645,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "chat_template_change",
    "operatorUnionId": "evdsxxx",
    "templateId": "1111abcd-1234-1234-dcba-123456789012",
    "changedTimeStamp": 43535463645,
    "openConversationId": "cidff2312123ee",
    "operator": "manager0112",
    "status": "on"
  }
}
```
