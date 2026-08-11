---
title: "企业增加员工事件"
source_url: "https://open.dingtalk.com/document/development/enterprise-increases-employee-events"
namespace: "development"
slug: "enterprise-increases-employee-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 企业增加员工事件"
doc_id: "Kp4jDPAHtF"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-increases-employee-events
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 企业增加员工事件
> Updated: 2022-01-19 19:29:22

# 企业增加员工事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业增加员工事件 |
| 英文名称 | user\_add\_org |

## 功能描述

该数据为在授权的企业内部应用通讯录事件，该文档为通讯录用户增加事件数据说明。

## **支持应用类型**

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
  "eventType": "user_add_org",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "timeStamp": "1685501863357",
    "userId": [
      "015xxxx227"
    ]
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "user_add_org",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "timeStamp": "1685501863357",
  "userId": [
    "015xxxx227"
  ]
}
```
