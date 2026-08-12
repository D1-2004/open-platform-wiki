---
title: "员工角色信息发生变更"
source_url: "https://open.dingtalk.com/document/development/employee-role-information-changes"
namespace: "development"
slug: "employee-role-information-changes"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 员工角色信息发生变更"
doc_id: "jvII1ER3v7"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/employee-role-information-changes
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 员工角色信息发生变更
> Updated: 2022-01-19 19:29:22

# 员工角色信息发生变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 员工角色信息发生变更 |
| 英文名称 | label\_user\_change |

## 功能描述

该数据为在授权的企业内部应用中，员工角色信息发生变更的数据推送。

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
  "eventType": "label_user_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "userIdList": [
      "84597xxx464"
    ],
    "action": "add",
    "labelIdList": [
      1881
    ]
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "label_user_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "userIdList": [
    "84597xxx464"
  ],
  "action": "add",
  "labelIdList": [
    1881
  ]
}
```
