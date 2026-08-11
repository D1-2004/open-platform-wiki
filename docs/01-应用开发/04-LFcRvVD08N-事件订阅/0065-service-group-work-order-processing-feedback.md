---
title: "服务群工单处理反馈"
source_url: "https://open.dingtalk.com/document/development/service-group-work-order-processing-feedback"
namespace: "development"
slug: "service-group-work-order-processing-feedback"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群工单处理反馈"
doc_id: "fHTHsiLiHT"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/service-group-work-order-processing-feedback
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群工单处理反馈
> Updated: 2022-01-19 19:29:22

# 服务群工单处理反馈

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群工单处理反馈 |
| 英文名称 | servicegroup\_ticket\_deal\_feedback |

## 功能描述

服务群工单处理反馈。

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
  "eventType": "servicegroup_ticket_deal_feedback",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpId": "dingadc88253b4d581bd35c2f4657eb6378f",
    "bizId": "88888",
    "spiTicketModel": {
      "operateData": {
        "dealResult": "SOLVED"
      },
      "operateType": "DEAL_RESULT",
      "operatorNickName": "张宇航小号",
      "operatorUnionId": "NK0qMkt7e03wGiS26tiPf8hgiEiE",
      "openTicketId": "dkp1jLhLpgMiE",
      "operateMemo": {
        "memo": "8888"
      }
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "servicegroup_ticket_deal_feedback",
  "EventTime": 1663143335567,
  "CorpId": "dingadc88253b4d581bd35c2f4657eb6378f",
  "BizId": "88888",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiTicketModel": {
    "operateData": {
      "dealResult": "SOLVED"
    },
    "operateType": "DEAL_RESULT",
    "operatorNickName": "张宇航小号",
    "operatorUnionId": "NK0qMkt7e03wGiS26tiPf8hgiEiE",
    "openTicketId": "dkp1jLhLpgMiE",
    "operateMemo": {
      "memo": "8888"
    }
  }
}
```
