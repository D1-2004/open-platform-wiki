---
title: "文件更新"
source_url: "https://open.dingtalk.com/document/development/event-storage-dentry-update"
namespace: "development"
slug: "event-storage-dentry-update"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 存储 > 文件更新"
doc_id: "VOvw7COjsh"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-storage-dentry-update
> Path: 应用开发 / 事件订阅 / 协同 > 存储 > 文件更新
> Updated: 2022-01-19 19:29:22

# 文件更新

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 文件更新 |
| 英文名称 | storage\_dentry\_update |

## 功能描述

文件或文件夹更新事件数据。如果仅在开发者后台开启存储事件订阅开关，无法接收回调事件，必须与接口配合使用，接口详情参见[订阅文件变更事件](https://open.dingtalk.com/document/orgapp/subscribe-to-file-change-events)。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "storage_dentry_update",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spaceId": "xxx",
    "dentryId": "xxx",
    "eventScope": "ORG",
    "extension": "pdf",
    "unionId": "xx",
    "eventScopeId": "xx",
    "type": "FILE"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "storage_dentry_update",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spaceId": "xxx",
  "dentryId": "xxx",
  "eventScope": "ORG",
  "extension": "pdf",
  "unionId": "xx",
  "eventScopeId": "xx",
  "type": "FILE"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=234)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 234,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "spaceId": "xxx",
    "dentryId": "xxx",
    "eventScope": "ORG",
    "extension": "pdf",
    "unionId": "xx",
    "syncAction": "storage_dentry_update",
    "eventScopeId": "xx",
    "type": "FILE"
  }
}
```
