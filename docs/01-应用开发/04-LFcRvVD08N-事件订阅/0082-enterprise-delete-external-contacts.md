---
title: "企业删除外部联系人"
source_url: "https://open.dingtalk.com/document/development/enterprise-delete-external-contacts"
namespace: "development"
slug: "enterprise-delete-external-contacts"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 企业删除外部联系人"
doc_id: "aKPiuW53PX"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-delete-external-contacts
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 企业删除外部联系人
> Updated: 2022-01-19 19:29:22

# 企业删除外部联系人

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业删除外部联系人 |
| 英文名称 | contact\_leave\_org |

## 功能描述

该数据为在授权的第三方企业应用中，企业外部联系人删除的推送信息。

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
  "eventType": "contact_leave_org",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "userId": "user123456"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=20)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 20,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "contact_leave_org",
    "userId": "user123456"
  }
}
```
