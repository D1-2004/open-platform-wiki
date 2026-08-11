---
title: "服务群工单已读"
source_url: "https://open.dingtalk.com/document/development/service-group-work-order-read"
namespace: "development"
slug: "service-group-work-order-read"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群工单已读"
doc_id: "FLX3DP5Q5P"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/service-group-work-order-read
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群工单已读
> Updated: 2022-01-19 19:29:22

# 服务群工单已读

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群工单已读 |
| 英文名称 | servicegroup\_ticket\_read |

## 功能描述

服务群工单已读事件。

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
  "eventType": "servicegroup_ticket_read",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiTicketModel": {
      "operateData": {
        "operate": "CREATE",
        "ticketSnapshot": {
          "takers": [
            {
              "unionId": "1111",
              "nickName": "张三"
            }
          ],
          "stage": "PROCESSING",
          "processor": {
            "unionId": "1111",
            "nickName": "张三"
          }
        }
      },
      "operateType": "READ",
      "operatorNickName": "张三",
      "operatorUnionId": "11111",
      "openTicketId": "ISeGR7JOP8IiE"
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "servicegroup_ticket_read",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiTicketModel": {
    "operateData": {
      "operate": "CREATE",
      "ticketSnapshot": {
        "takers": [
          {
            "unionId": "1111",
            "nickName": "张三"
          }
        ],
        "stage": "PROCESSING",
        "processor": {
          "unionId": "1111",
          "nickName": "张三"
        }
      }
    },
    "operateType": "READ",
    "operatorNickName": "张三",
    "operatorUnionId": "11111",
    "openTicketId": "ISeGR7JOP8IiE"
  }
}
```
