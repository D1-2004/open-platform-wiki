---
title: "加入企业后用户激活"
source_url: "https://open.dingtalk.com/document/development/user-activation-after-joining-the-enterprise"
namespace: "development"
slug: "user-activation-after-joining-the-enterprise"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 加入企业后用户激活"
doc_id: "aesle8v6sV"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/user-activation-after-joining-the-enterprise
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 加入企业后用户激活
> Updated: 2022-01-19 19:29:22

# 加入企业后用户激活

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 加入企业后用户激活 |
| 英文名称 | user\_active\_org |

## 功能描述

该数据为在授权的企业内部应用中，通讯录用户加入企业后用户激活事件的推送数据。

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
  "eventType": "user_active_org",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "userId": [
      "015xxxx227"
    ]
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "user_active_org",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "userId": [
    "015xxxx227"
  ]
}
```
