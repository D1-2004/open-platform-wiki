---
title: "文档导出任务完成事件"
source_url: "https://open.dingtalk.com/document/development/events-doc-export-completed"
namespace: "development"
slug: "events-doc-export-completed"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 文档 > 文档导出任务完成事件"
doc_id: "Zxq5clS2AI"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-doc-export-completed
> Path: 应用开发 / 事件订阅 / 协同 > 文档 > 文档导出任务完成事件
> Updated: 2022-01-19 19:29:22

# 文档导出任务完成事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 文档导出任务完成事件 |
| 英文名称 | doc\_export\_completed |

## 功能描述

当文档导出任务状态发生变更（如成功、失败等）时，钉钉推送发生变更的文档导出任务信息，以便获得文档导出任务结果。

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
  "eventType": "doc_export_completed",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "body": {}
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "doc_export_completed",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "body": {}
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=493)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 493,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "doc_export_completed",
    "body": {}
  }
}
```
