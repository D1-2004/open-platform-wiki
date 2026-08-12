---
title: "异步转译通讯录id任务完成通知"
source_url: "https://open.dingtalk.com/document/development/asynchronous-translation-address-book-id-task-completion-notification"
namespace: "development"
slug: "asynchronous-translation-address-book-id-task-completion-notification"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 异步转译通讯录id任务完成通知"
doc_id: "9Qe771g0Dk"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/asynchronous-translation-address-book-id-task-completion-notification
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 异步转译通讯录id任务完成通知
> Updated: 2022-01-19 19:29:22

# 异步转译通讯录id任务完成通知

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 异步转译通讯录id任务完成通知 |
| 英文名称 | transfer\_contact\_id\_job\_result |

## 功能描述

企业异步转译通讯录id任务完成，发送的异步转译通讯录事件数据。

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
  "eventType": "transfer_contact_id_job_result",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "jobId": "seejaRmXY8RQgo2SJSHS92xxxxxxx",
    "status": "1"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=139)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 139,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "jobId": "seejaRmXY8RQgo2SJSHS92xxxxxxx",
    "syncAction": "transfer_contact_id_job_result",
    "status": "1"
  }
}
```
