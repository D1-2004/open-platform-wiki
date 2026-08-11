---
title: "企业变更"
source_url: "https://open.dingtalk.com/document/development/event-subscription-for-enterprise-changes"
namespace: "development"
slug: "event-subscription-for-enterprise-changes"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 企业变更"
doc_id: "Ih7w9LinIN"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-subscription-for-enterprise-changes
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 企业变更
> Updated: 2022-01-19 19:29:22

# 企业变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业变更 |
| 英文名称 | org\_update |

## 功能描述

数据为企业的最新状态。该数据为在授权的第三方企业应用中，企业信息发生变更的时刻推送。

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
  "eventType": "org_update",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": 0,
    "corpLogoUrl": "https://static.xxx.com",
    "corpid": "dingxxx2cff796",
    "errmsg": "ok",
    "industry": "信息技术咨询",
    "corpName": "企业1",
    "isAuthenticated": true,
    "authLevel": 2
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=16)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 16,
  "biz_data": {
    "errcode": 0,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpid": "dingxxx2cff796",
    "syncAction": "org_update",
    "auth_level": 2,
    "errmsg": "ok",
    "industry": "信息技术咨询",
    "is_authenticated": true,
    "corp_name": "企业1",
    "corp_logo_url": "https://static.xxx.com"
  }
}
```
