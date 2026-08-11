---
title: "企业修改员工事件"
source_url: "https://open.dingtalk.com/document/development/enterprise-modify-employee-event"
namespace: "development"
slug: "enterprise-modify-employee-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 企业修改员工事件"
doc_id: "f8GwNq5O44"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-modify-employee-event
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 企业修改员工事件
> Updated: 2022-01-19 19:29:22

# 企业修改员工事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业修改员工事件 |
| 英文名称 | user\_modify\_org |

## 功能描述

企业内部用户变更事件。该文档为企业修改员工信息字段说明，字段值来自于[根据userId获取用户详情](https://open.dingtalk.com/document/isvapp/queries-the-details-of-a-dedicated-account)接口 。

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
  "eventType": "user_modify_org",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": 0,
    "unionEmpExt": {
      "corpId": "ding351234",
      "unionEmpMapList": [
        {
          "corpId": "ding351234",
          "staffId": "12345"
        }
      ],
      "staffId": "1234"
    },
    "unionid": "m8axYHBIiSxxxx",
    "exclusiveAccount": false,
    "orderInDepts": "{1234:12345}",
    "dingId": "$:LWCP_v1:$LT",
    "active": true,
    "errmsg": "ok",
    "avatar": "http://xxxxx",
    "isAdmin": true,
    "userid": "user123",
    "isHide": true,
    "jobnumber": "1",
    "isLeaderInDepts": "{1:false}",
    "isBoss": true,
    "isSenior": false,
    "name": "张三",
    "position": "技术支持",
    "department": [
      1
    ],
    "realAuthed": true
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
    "errcode": 0,
    "unionEmpExt": {
      "corpId": "ding351234",
      "unionEmpMapList": [
        {
          "corpId": "ding351234",
          "staffId": "12345"
        }
      ],
      "staffId": "1234"
    },
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "unionid": "m8axYHBIiSxxxx",
    "exclusiveAccount": false,
    "syncAction": "user_modify_org",
    "orderInDepts": "{1234:12345}",
    "dingId": "$:LWCP_v1:$LT",
    "active": true,
    "errmsg": "ok",
    "avatar": "http://xxxxx",
    "isAdmin": true,
    "userid": "user123",
    "isHide": true,
    "jobnumber": "1",
    "isLeaderInDepts": "{1:false}",
    "isBoss": true,
    "isSenior": false,
    "name": "张三",
    "position": "技术支持",
    "department": [
      1
    ],
    "realAuthed": true
  }
}
```
