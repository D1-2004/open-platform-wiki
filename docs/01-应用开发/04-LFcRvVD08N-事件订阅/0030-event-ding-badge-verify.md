---
title: "钉工牌核验事件"
source_url: "https://open.dingtalk.com/document/development/event-ding-badge-verify"
namespace: "development"
slug: "event-ding-badge-verify"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > 钉工牌 > 钉工牌核验事件"
doc_id: "xPstROsVes"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-ding-badge-verify
> Path: 应用开发 / 事件订阅 / 办公 > 钉工牌 > 钉工牌核验事件
> Updated: 2022-01-19 19:29:22

# 钉工牌核验事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 钉工牌核验事件 |
| 英文名称 | ding\_badge\_verify |

## 功能描述

钉工牌扫码核验事件。

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
  "eventType": "ding_badge_verify",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "codeId": "codexxxxxx",
    "verifyEvent": "Test",
    "corpId": "dingxxxxx",
    "codeIdentity": "PURE_IDENTITY_CODE",
    "verifyLocation": "钉网科技",
    "userCorpRelationType": "INTERNAL_STAFF",
    "verifyResult": "SUCCESS",
    "verifyNo": "123xxx",
    "verifyAmount": "100.00",
    "verifyTime": "2023-07-04 00:00:00",
    "userIdentity": "20xxx123"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=174)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 174,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpId": "dingxxxxx",
    "codeIdentity": "PURE_IDENTITY_CODE",
    "syncAction": "ding_badge_verify",
    "verifyResult": "SUCCESS",
    "verifyTime": "2023-07-04 00:00:00",
    "userIdentity": "20xxx123",
    "codeId": "codexxxxxx",
    "verifyEvent": "Test",
    "verifyLocation": "钉网科技",
    "userCorpRelationType": "INTERNAL_STAFF",
    "verifyNo": "123xxx",
    "verifyAmount": "100.00"
  }
}
```
