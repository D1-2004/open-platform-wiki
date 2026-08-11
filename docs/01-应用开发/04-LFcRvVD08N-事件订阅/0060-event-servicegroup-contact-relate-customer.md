---
title: "服务群联系人关联客户"
source_url: "https://open.dingtalk.com/document/development/event-servicegroup-contact-relate-customer"
namespace: "development"
slug: "event-servicegroup-contact-relate-customer"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群联系人关联客户"
doc_id: "5cKfZkLe1b"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-servicegroup-contact-relate-customer
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群联系人关联客户
> Updated: 2022-01-19 19:29:22

# 服务群联系人关联客户

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群联系人关联客户 |
| 英文名称 | servicegroup\_contact\_relate\_customer |

## 功能描述

服务群联系人关联客户事件推送的数据内容。

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
  "eventType": "servicegroup_contact_relate_customer",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiCrmModel": {
      "openTeamId": "iPxxxxxxxx",
      "externalBizId": "iPxxxxxxxxxxxx",
      "formScene": "DING_JOIN_GROUP",
      "openDataInstanceId": "qsxxxxxxxxxxx",
      "operateType": "CONTACT_JOIN_GROUP_FORM",
      "operatorNickName": "李四",
      "formData": {
        "belongCustomerId": "xxxxxxx"
      },
      "operatorUnionId": "4kIxxxxxxxxxxxxxxxxx"
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "servicegroup_contact_relate_customer",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiCrmModel": {
    "openTeamId": "iPxxxxxxxx",
    "externalBizId": "iPxxxxxxxxxxxx",
    "formScene": "DING_JOIN_GROUP",
    "openDataInstanceId": "qsxxxxxxxxxxx",
    "operateType": "CONTACT_JOIN_GROUP_FORM",
    "operatorNickName": "李四",
    "formData": {
      "belong_customer_id": "xxxxxxx"
    },
    "operatorUnionId": "4kIxxxxxxxxxxxxxxxxx"
  }
}
```
