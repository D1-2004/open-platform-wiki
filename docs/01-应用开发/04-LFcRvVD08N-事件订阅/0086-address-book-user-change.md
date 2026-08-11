---
title: "通讯录用户更改"
source_url: "https://open.dingtalk.com/document/development/address-book-user-change"
namespace: "development"
slug: "address-book-user-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 通讯录用户更改"
doc_id: "bDF8S1CMb3"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/address-book-user-change
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 通讯录用户更改
> Updated: 2022-01-19 19:29:22

# 通讯录用户更改

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 通讯录用户更改 |
| 英文名称 | user\_modify\_org |

## 功能描述

该数据为在授权的企业内部应用中，通讯录用户更改事件数据推送说明文档。

> 说明：只有当前企业内的用户信息变更时才会触发此事件，用户的个人信息变更并不会触发，例如个人头像、个人昵称、钉钉号等。

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
  "eventType": "user_modify_org",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "timeStamp": "1608017258073",
    "diffInfo": {
      "prev": {
        "managerUserid": "205xxx91",
        "hiredDate": "20xx-xx-xx",
        "name": "测试01",
        "telephone": "1234",
        "email": "xxx@xx.com",
        "jobNumber": "112x422",
        "workPlace": "北京"
      },
      "curr": {
        "managerUserid": "205xxx91",
        "hiredDate": "20xx-xx-xx",
        "name": "测试1",
        "email": "xxx@xx.com",
        "jobNumber": "112x422",
        "workPlace": "北京"
      },
      "userid": "user123456"
    },
    "userId": [
      "user123456"
    ]
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "user_modify_org",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "timeStamp": "1608017258073",
  "diffInfo": {
    "prev": {
      "managerUserid": "205xxx91",
      "hiredDate": "20xx-xx-xx",
      "name": "测试01",
      "telephone": "1234",
      "email": "xxx@xx.com",
      "jobNumber": "112x422",
      "workPlace": "北京"
    },
    "curr": {
      "managerUserid": "205xxx91",
      "hiredDate": "20xx-xx-xx",
      "name": "测试1",
      "email": "xxx@xx.com",
      "jobNumber": "112x422",
      "workPlace": "北京"
    },
    "userid": "user123456"
  },
  "userId": [
    "user123456"
  ]
}
```
