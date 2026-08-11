---
title: "企业角色变更"
source_url: "https://open.dingtalk.com/document/development/enterprise-role-change"
namespace: "development"
slug: "enterprise-role-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 企业角色变更"
doc_id: "IvNopNqFMW"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-role-change
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 企业角色变更
> Updated: 2022-01-19 19:29:22

# 企业角色变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业角色变更 |
| 英文名称 | org\_role\_modify |

## 功能描述

企业角色的最新状态事件。该数据为在授权的第三方企业应用中，发生角色的修改的时刻推送。

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
  "eventType": "org_role_modify",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "groupName": "默认角色组",
    "roleId": 12345,
    "groupId": 1234,
    "roleName": "角色01"
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
    "role_name": "角色01",
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "org_role_modify",
    "role_id": 12345,
    "group_id": 1234,
    "group_name": "默认角色组"
  }
}
```
