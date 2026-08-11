---
title: "服务群工单催办"
source_url: "https://open.dingtalk.com/document/development/service-group-work-order-reminder"
namespace: "development"
slug: "service-group-work-order-reminder"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群工单催办"
doc_id: "eE8N4R2fgp"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/service-group-work-order-reminder
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群工单催办
> Updated: 2022-01-19 19:29:22

# 服务群工单催办

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群工单催办 |
| 英文名称 | servicegroup\_ticket\_urge |

## 功能描述

服务群工单催办的推送数据。

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
  "eventType": "servicegroup_ticket_urge",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiTicketModel": {
      "operateData": {
        "receivers": [
          {
            "unionId": "1AE3AiiPwsBZSKB3lvssfOgiEiE",
            "nickName": "李航宇"
          }
        ]
      },
      "operateType": "URGE",
      "operatorNickName": "王鸿程",
      "operatorUnionId": "9dQurQX3VspSKB3lvssfOgiEiE",
      "openTicketId": "ISeGR7JOP8IiE",
      "operateMemo": {
        "attachments": [
          {
            "fileName": "01d11e438f03410d53693fcf5efed334.jpeg",
            "type": "img",
            "key": "ticket/image/41661019/123001/8812788f16574d9d891f6186d7b629e4_1626174465926.jpeg"
          }
        ],
        "memo": "测试"
      }
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "servicegroup_ticket_urge",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiTicketModel": {
    "operateData": {
      "receivers": [
        {
          "unionId": "1AE3AiiPwsBZSKB3lvssfOgiEiE",
          "nickName": "李航宇"
        }
      ]
    },
    "operateType": "URGE",
    "operatorNickName": "王鸿程",
    "operatorUnionId": "9dQurQX3VspSKB3lvssfOgiEiE",
    "openTicketId": "ISeGR7JOP8IiE",
    "operateMemo": {
      "attachments": [
        {
          "fileName": "01d11e438f03410d53693fcf5efed334.jpeg",
          "type": "img",
          "key": "ticket/image/41661019/123001/8812788f16574d9d891f6186d7b629e4_1626174465926.jpeg"
        }
      ],
      "memo": "测试"
    }
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=122)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 122,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "servicegroup_ticket_urge",
    "spiTicketModel": {
      "operateData": {
        "receivers": [
          {
            "unionId": "1AE3AiiPwsBZSKB3lvssfOgiEiE",
            "nickName": "李航宇"
          }
        ]
      },
      "operateType": "URGE",
      "operatorNickName": "王鸿程",
      "operatorUnionId": "9dQurQX3VspSKB3lvssfOgiEiE",
      "openTicketId": "ISeGR7JOP8IiE",
      "operateMemo": {
        "attachments": [
          {
            "fileName": "01d11e438f03410d53693fcf5efed334.jpeg",
            "type": "img",
            "key": "ticket/image/41661019/123001/8812788f16574d9d891f6186d7b629e4_1626174465926.jpeg"
          }
        ],
        "memo": "测试"
      }
    }
  }
}
```
