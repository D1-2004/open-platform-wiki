---
title: "AIoT设备上行事件"
source_url: "https://open.dingtalk.com/document/development/events-aiot-device-uplink-event"
namespace: "development"
slug: "events-aiot-device-uplink-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能硬件 > AIoT平台 > AIoT设备上行事件"
doc_id: "eYPW7UFiGZ"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-aiot-device-uplink-event
> Path: 应用开发 / 事件订阅 / 智能硬件 > AIoT平台 > AIoT设备上行事件
> Updated: 2022-01-19 19:29:22

# AIoT设备上行事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | AIoT设备上行事件 |
| 英文名称 | aiot\_device\_uplink\_event |

## 功能描述

设备上行事件，包括设备状态变更事件、物模型事件。具体需要订阅哪些事件，可以在AIoT平台产品开发阶段选择

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
  "eventType": "aiot_device_uplink_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "schemaVersion": "1.0",
    "eventTime": "1783585444709",
    "topic": "/sys/***/***/thing/event/property/post",
    "eventType": "PROPERTY_REPORT",
    "category": "DEVICE_DATA",
    "sourceJson": "{\"type\":\"DEVICE_DATA_SOURCE\",\"productKey\":\"dFydxxxxQcK\",\"deviceName\":\"dn_0000000004\",\"identifier\":null,\"payloadJson\":\"{\\\\\"trace_id\\\\\":{\\\\\"value\\\\\":\\\\\"2104exxxx0a00\\\\\",\\\\\"time\\\\\":1783653857509}}\"}"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "aiot_device_uplink_event",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "schemaVersion": "1.0",
  "eventTime": "1783585444709",
  "topic": "/sys/***/***/thing/event/property/post",
  "eventType": "PROPERTY_REPORT",
  "category": "DEVICE_DATA",
  "sourceJson": "{\"type\":\"DEVICE_DATA_SOURCE\",\"productKey\":\"dFydxxxxQcK\",\"deviceName\":\"dn_0000000004\",\"identifier\":null,\"payloadJson\":\"{\\\\\"trace_id\\\\\":{\\\\\"value\\\\\":\\\\\"2104exxxx0a00\\\\\",\\\\\"time\\\\\":1783653857509}}\"}"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=498)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 498,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "schemaVersion": "1.0",
    "syncAction": "aiot_device_uplink_event",
    "eventTime": "1783585444709",
    "topic": "/sys/***/***/thing/event/property/post",
    "eventType": "PROPERTY_REPORT",
    "category": "DEVICE_DATA",
    "sourceJson": "{\"type\":\"DEVICE_DATA_SOURCE\",\"productKey\":\"dFydxxxxQcK\",\"deviceName\":\"dn_0000000004\",\"identifier\":null,\"payloadJson\":\"{\\\\\"trace_id\\\\\":{\\\\\"value\\\\\":\\\\\"2104exxxx0a00\\\\\",\\\\\"time\\\\\":1783653857509}}\"}"
  }
}
```
