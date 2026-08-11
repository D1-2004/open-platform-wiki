---
title: "AI销售管理设备使用人变更事件"
source_url: "https://open.dingtalk.com/document/development/events-dvi-device-owner-change"
namespace: "development"
slug: "events-dvi-device-owner-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "视听智能服务 > AI销售管理设备使用人变更事件"
doc_id: "D8e3ahngX3"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-dvi-device-owner-change
> Path: 应用开发 / 事件订阅 / 视听智能服务 > AI销售管理设备使用人变更事件
> Updated: 2022-01-19 19:29:22

# AI销售管理设备使用人变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | AI销售管理设备使用人变更事件 |
| 英文名称 | dvi\_device\_owner\_change |

## 功能描述

AI销售管理中的设备使用人发生变更时产生的事件

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
  "eventType": "dvi_device_owner_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "teamCode": "b7***4fa-088a-43f5-****-daf***6",
    "sn": "SSYX410****6",
    "type": "bind",
    "userId": "300*******21"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "dvi_device_owner_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "teamCode": "b7***4fa-088a-43f5-****-daf***6",
  "sn": "SSYX410****6",
  "type": "bind",
  "userId": "300*******21"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=489)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 489,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "dvi_device_owner_change",
    "teamCode": "b7***4fa-088a-43f5-****-daf***6",
    "sn": "SSYX410****6",
    "type": "bind",
    "userId": "300*******21"
  }
}
```
