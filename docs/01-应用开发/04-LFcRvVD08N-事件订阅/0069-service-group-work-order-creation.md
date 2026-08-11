---
title: "服务群工单创建"
source_url: "https://open.dingtalk.com/document/development/service-group-work-order-creation"
namespace: "development"
slug: "service-group-work-order-creation"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群工单创建"
doc_id: "5LCr2Ru96d"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/service-group-work-order-creation
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群工单创建
> Updated: 2022-01-19 19:29:22

# 服务群工单创建

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群工单创建 |
| 英文名称 | servicegroup\_ticket\_create |

## 功能描述

服务群工单创建的推送数据。

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
  "eventType": "servicegroup_ticket_create",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiTicketModel": {
      "operateType": "CREATE",
      "operatorNickName": "王鸿程",
      "operatorUnionId": "9dQurQX3VspSKB3lvssfOgiEiE",
      "openTicketId": "ISeGR7JOP8IiE"
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "servicegroup_ticket_create",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiTicketModel": {
    "operateType": "CREATE",
    "operatorNickName": "王鸿程",
    "operatorUnionId": "9dQurQX3VspSKB3lvssfOgiEiE",
    "openTicketId": "ISeGR7JOP8IiE"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=115)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 115,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "servicegroup_ticket_create",
    "spiTicketModel": {
      "operateType": "CREATE",
      "operatorNickName": "王鸿程",
      "operatorUnionId": "9dQurQX3VspSKB3lvssfOgiEiE",
      "openTicketId": "ISeGR7JOP8IiE"
    }
  }
}
```
