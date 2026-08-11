---
title: "服务群自定义表单删除实例"
source_url: "https://open.dingtalk.com/document/development/service-group-custom-form-delete-instance"
namespace: "development"
slug: "service-group-custom-form-delete-instance"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群自定义表单删除实例"
doc_id: "wLAQadVLmQ"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/service-group-custom-form-delete-instance
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群自定义表单删除实例
> Updated: 2022-01-19 19:29:22

# 服务群自定义表单删除实例

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群自定义表单删除实例 |
| 英文名称 | servicegroup\_custom\_object\_delete |

## 功能描述

服务群自定义表单删除实例推送的数据。

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
  "eventType": "servicegroup_custom_object_delete",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiCrmModel": {
      "openTeamId": "iPxxxxxxx",
      "externalBizId": "xxxx",
      "formScene": "DING_CUSTOMER",
      "openDataInstanceId": "exxxxxxxxxx",
      "operateType": "DELETE_CUSTOM",
      "operatorNickName": "李四",
      "operatorUnionId": "4kIxxxxxxxxxxxxxxx"
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "servicegroup_custom_object_delete",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiCrmModel": {
    "openTeamId": "iPxxxxxxx",
    "externalBizId": "xxxx",
    "formScene": "DING_CUSTOMER",
    "openDataInstanceId": "exxxxxxxxxx",
    "operateType": "DELETE_CUSTOM",
    "operatorNickName": "李四",
    "operatorUnionId": "4kIxxxxxxxxxxxxxxx"
  }
}
```
