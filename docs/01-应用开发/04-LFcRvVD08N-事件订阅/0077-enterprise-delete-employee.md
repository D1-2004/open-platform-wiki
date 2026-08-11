---
title: "企业删除员工"
source_url: "https://open.dingtalk.com/document/development/enterprise-delete-employee"
namespace: "development"
slug: "enterprise-delete-employee"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 企业删除员工"
doc_id: "zk5JPMbMcS"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-delete-employee
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 企业删除员工
> Updated: 2022-01-19 19:29:22

# 企业删除员工

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业删除员工 |
| 英文名称 | user\_leave\_org |

## 功能描述

企业内部用户变更事件，该文档表示企业删除员工推送信息。

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
  "eventType": "user_leave_org",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "unionid": "zvLdpxxxxxiEiE",
    "dingId": "$:LWCP_v1:$G5YX0l5yOKZ2oxxxx",
    "userId": "ding12345"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=13)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 13,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "unionid": "zvLdpxxxxxiEiE",
    "syncAction": "user_leave_org",
    "dingId": "$:LWCP_v1:$G5YX0l5yOKZ2oxxxx",
    "userId": "ding12345"
  }
}
```
