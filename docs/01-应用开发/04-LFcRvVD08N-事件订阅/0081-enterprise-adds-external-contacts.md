---
title: "企业增加外部联系人"
source_url: "https://open.dingtalk.com/document/development/enterprise-adds-external-contacts"
namespace: "development"
slug: "enterprise-adds-external-contacts"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 企业增加外部联系人"
doc_id: "ps5ZKclym3"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-adds-external-contacts
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 企业增加外部联系人
> Updated: 2022-01-19 19:29:22

# 企业增加外部联系人

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业增加外部联系人 |
| 英文名称 | contact\_add\_org |

## 功能描述

该数据为在授权的第三方企业应用中，企业增加外部联系人的推送信息。

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
  "eventType": "contact_add_org",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": 0,
    "labelIds": [
      1234567
    ],
    "shareUserIds": [
      "ding***xd1"
    ],
    "followerUserId": "2000121002668",
    "companyName": "企业1",
    "name": "潜在客户小张",
    "mobile": "12345678910",
    "errmsg": "ok",
    "stateCode": "86",
    "userId": "12345",
    "shareDeptIds": [
      122
    ]
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=20)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 20,
  "biz_data": {
    "errcode": 0,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "shareUserIds": [
      "ding***xd1"
    ],
    "syncAction": "contact_add_org",
    "companyName": "企业1",
    "mobile": "12345678910",
    "errmsg": "ok",
    "userId": "12345",
    "shareDeptIds": [
      122
    ],
    "labelIds": [
      1234567
    ],
    "followerUserId": "2000121002668",
    "name": "潜在客户小张",
    "stateCode": "86"
  }
}
```
