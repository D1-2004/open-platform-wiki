---
title: "通讯录企业部门创建"
source_url: "https://open.dingtalk.com/document/development/create-department-event"
namespace: "development"
slug: "create-department-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 通讯录企业部门创建"
doc_id: "d1iE5fZeye"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/create-department-event
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 通讯录企业部门创建
> Updated: 2022-01-19 19:29:22

# 通讯录企业部门创建

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 通讯录企业部门创建 |
| 英文名称 | org\_dept\_create |

## 功能描述

该数据为在授权的企业内部应用中，表示通讯录企业部门创建时的数据推送。

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
  "eventType": "org_dept_create",
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
  "EventType": "org_dept_create",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "deptId": [
    432825033
  ]
}
```
