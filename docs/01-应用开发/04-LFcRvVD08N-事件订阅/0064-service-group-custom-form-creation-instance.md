---
title: "服务群自定义表单创建实例"
source_url: "https://open.dingtalk.com/document/development/service-group-custom-form-creation-instance"
namespace: "development"
slug: "service-group-custom-form-creation-instance"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群自定义表单创建实例"
doc_id: "NJgyjTDQax"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/service-group-custom-form-creation-instance
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群自定义表单创建实例
> Updated: 2022-01-19 19:29:22

# 服务群自定义表单创建实例

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群自定义表单创建实例 |
| 英文名称 | servicegroup\_custom\_object\_create |

## 功能描述

服务群自定义表单创建实例推送的数据。

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
  "eventType": "servicegroup_custom_object_create",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiCrmModel": {
      "openTeamId": "iPXXXXXXXXX",
      "externalBizId": "XXXXX",
      "formScene": "DING_CUSTOMER",
      "openDataInstanceId": "eOGXXXXXXXXXX",
      "operateType": "CREATE_CUSTOM",
      "operatorNickName": "李四",
      "formData": {
        "customerType": 1,
        "customerName": "testCorpInfo_1"
      },
      "operatorUnionId": "Shxxxxxxxxxxxxxxx"
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "servicegroup_custom_object_create",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiCrmModel": {
    "openTeamId": "iPXXXXXXXXX",
    "externalBizId": "XXXXX",
    "formScene": "DING_CUSTOMER",
    "openDataInstanceId": "eOGXXXXXXXXXX",
    "operateType": "CREATE_CUSTOM",
    "operatorNickName": "李四",
    "formData": {
      "customer_type": 1,
      "customer_name": "testCorpInfo_1"
    },
    "operatorUnionId": "Shxxxxxxxxxxxxxxx"
  }
}
```
