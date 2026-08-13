---
title: "批量支付消息通知"
source_url: "https://open.dingtalk.com/document/development/event-open-batch-trade-callback"
namespace: "development"
slug: "event-open-batch-trade-callback"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > 钉工牌 > 批量支付消息通知"
doc_id: "19NQ9Gnm9t"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-open-batch-trade-callback
> Path: 应用开发 / 事件订阅 / 办公 > 钉工牌 > 批量支付消息通知
> Updated: 2022-01-19 19:29:22

# 批量支付消息通知

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 批量支付消息通知 |
| 英文名称 | open\_batch\_trade\_callback |

## 功能描述

批量支付完成事件回调，创建批量付款单并支付后，当支付处理完成时，给对应归属的ISV应用定向推送回调。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "open_batch_trade_callback",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "failCount": 1,
    "gmtFinish": "2023-07-21 14:00:00",
    "successAmount": 19.5,
    "paymentAmount": 21.0,
    "totalAmount": 21.0,
    "outBatchNo": "2023XXXXXXX06",
    "successCount": 5,
    "alipayTransId": "2002XXXXXXX92",
    "gmtSubmit": "2023-07-21 13:58:57",
    "failAmount": 1.5,
    "failReason": "账号异常",
    "payerStaffId": "332XXXX011",
    "paymentCurrency": "CNY",
    "status": "SUCCESS"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=134)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 134,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "open_batch_trade_callback",
    "failCount": 1,
    "gmtFinish": "2023-07-21 14:00:00",
    "successAmount": 19.5,
    "paymentAmount": 21.0,
    "totalAmount": 21.0,
    "outBatchNo": "2023XXXXXXX06",
    "successCount": 5,
    "alipayTransId": "2002XXXXXXX92",
    "gmtSubmit": "2023-07-21 13:58:57",
    "failAmount": 1.5,
    "failReason": "账号异常",
    "payerStaffId": "332XXXX011",
    "paymentCurrency": "CNY",
    "status": "SUCCESS"
  }
}
```
