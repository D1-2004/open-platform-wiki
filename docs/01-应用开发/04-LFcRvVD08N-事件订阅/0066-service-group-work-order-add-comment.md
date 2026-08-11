---
title: "服务群工单添加备注"
source_url: "https://open.dingtalk.com/document/development/service-group-work-order-add-comment"
namespace: "development"
slug: "service-group-work-order-add-comment"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群工单添加备注"
doc_id: "5KsDtGVSkE"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/service-group-work-order-add-comment
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群工单添加备注
> Updated: 2022-01-19 19:29:22

# 服务群工单添加备注

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群工单添加备注 |
| 英文名称 | servicegroup\_ticket\_memo\_add |

## 功能描述

服务群工单添加备注的推送数据。

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
  "eventType": "servicegroup_ticket_memo_add",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiTicketModel": {
      "operateType": "ADD_MEMO",
      "operatorNickName": "张宇航小号",
      "operatorUnionId": "NK0qMkt7e03wGiS26tiPf8hgiEiE",
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
  "EventType": "servicegroup_ticket_memo_add",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiTicketModel": {
    "operateType": "ADD_MEMO",
    "operatorNickName": "张宇航小号",
    "operatorUnionId": "NK0qMkt7e03wGiS26tiPf8hgiEiE",
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
