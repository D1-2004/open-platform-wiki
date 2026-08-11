---
title: "用户信息授权结果"
source_url: "https://open.dingtalk.com/document/development/user-information-authorization-result"
namespace: "development"
slug: "user-information-authorization-result"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 服务窗 > 用户信息授权结果"
doc_id: "fxCSAOeYXu"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/user-information-authorization-result
> Path: 应用开发 / 事件订阅 / 组织关系 > 服务窗 > 用户信息授权结果
> Updated: 2022-01-19 19:29:22

# 用户信息授权结果

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 用户信息授权结果 |
| 英文名称 | official\_account\_user\_data\_apply\_result |

## 功能描述

用户信息授权结果事件，用户授权同意或者拒绝后会收到这个事件。

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
  "eventType": "official_account_user_data_apply_result",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "accountId": "ding20e5e3e5f6b6ada5acaaa37764f94726",
    "msgType": "official_account_user_data_apply_result",
    "userId": "rw6bwlpaiv7nig22kmyx7qhrze",
    "content": {
      "authorized": true
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "official_account_user_data_apply_result",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "accountId": "ding20e5e3e5f6b6ada5acaaa37764f94726",
  "msgType": "official_account_user_data_apply_result",
  "userId": "rw6bwlpaiv7nig22kmyx7qhrze",
  "content": {
    "authorized": true
  }
}
```
