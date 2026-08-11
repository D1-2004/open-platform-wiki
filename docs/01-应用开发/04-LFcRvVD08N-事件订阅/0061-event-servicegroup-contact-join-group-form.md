---
title: "服务群入群表单保存"
source_url: "https://open.dingtalk.com/document/development/event-servicegroup-contact-join-group-form"
namespace: "development"
slug: "event-servicegroup-contact-join-group-form"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群入群表单保存"
doc_id: "179vyWHv92"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-servicegroup-contact-join-group-form
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群入群表单保存
> Updated: 2022-01-19 19:29:22

# 服务群入群表单保存

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群入群表单保存 |
| 英文名称 | servicegroup\_contact\_join\_group\_form |

## 功能描述

服务群入群表单事件推送的数据。

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
  "eventType": "servicegroup_contact_join_group_form",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiCrmModel": {
      "openTeamId": "iPxxxxxxxx",
      "formScene": "DING_JOIN_GROUP",
      "openDataInstanceId": "qsxxxxxxxxxxx",
      "operateType": "CONTACT_JOIN_GROUP_FORM",
      "formData": {
        "dINGCUSTOMER": {
          "dingCustomerId": "Oidxxxxxxxx",
          "customerName": "李四"
        }
      }
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "servicegroup_contact_join_group_form",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiCrmModel": {
    "openTeamId": "iPxxxxxxxx",
    "formScene": "DING_JOIN_GROUP",
    "openDataInstanceId": "qsxxxxxxxxxxx",
    "operateType": "CONTACT_JOIN_GROUP_FORM",
    "formData": {
      "DING_CUSTOMER": {
        "ding_customer_id": "Oidxxxxxxxx",
        "customer_name": "李四"
      }
    }
  }
}
```
