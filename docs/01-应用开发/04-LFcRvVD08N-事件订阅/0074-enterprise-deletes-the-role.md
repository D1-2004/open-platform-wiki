---
title: "企业删除角色"
source_url: "https://open.dingtalk.com/document/development/enterprise-deletes-the-role"
namespace: "development"
slug: "enterprise-deletes-the-role"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 企业删除角色"
doc_id: "immyCpKMn3"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-deletes-the-role
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 企业删除角色
> Updated: 2022-01-19 19:29:22

# 企业删除角色

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业删除角色 |
| 英文名称 | org\_role\_remove |

## 功能描述

数据为企业角色的最新状态。该数据为在授权的第三方企业应用中，发生角色的删除的时刻推送。

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
  "eventType": "org_role_remove",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "roleId": "1234"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=15)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 15,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "org_role_remove",
    "role_id": "1234"
  }
}
```
