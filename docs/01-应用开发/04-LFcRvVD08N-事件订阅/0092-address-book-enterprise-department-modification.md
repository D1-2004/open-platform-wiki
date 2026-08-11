---
title: "通讯录企业部门修改"
source_url: "https://open.dingtalk.com/document/development/address-book-enterprise-department-modification"
namespace: "development"
slug: "address-book-enterprise-department-modification"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 通讯录企业部门修改"
doc_id: "LFL6QkYxpx"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/address-book-enterprise-department-modification
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 通讯录企业部门修改
> Updated: 2022-01-19 19:29:22

# 通讯录企业部门修改

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 通讯录企业部门修改 |
| 英文名称 | org\_dept\_modify |

## 功能描述

该数据为在授权的企业内部应用中，通讯录企业部门修改的数据推送说明。

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
  "eventType": "org_dept_modify",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "deptId": [
      432825033
    ]
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "org_dept_modify",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "deptId": [
    432825033
  ]
}
```
