---
title: "服务群群信息变更"
source_url: "https://open.dingtalk.com/document/development/event-servicegroup-group-info-change"
namespace: "development"
slug: "event-servicegroup-group-info-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群群信息变更"
doc_id: "D2XGfGz6eo"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-servicegroup-group-info-change
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群群信息变更
> Updated: 2022-01-19 19:29:22

# 服务群群信息变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群群信息变更 |
| 英文名称 | servicegroup\_group\_info\_change |

## 功能描述

服务群群信息变更事件数据信息。

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
  "eventType": "servicegroup_group_info_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiGroupModel": {
      "operateData": {
        "bizId": "11222"
      },
      "openTeamId": "exxxxxxwsKEiE",
      "operateType": "BIZ_ID_BIND_CHANGE",
      "operatorNickName": "xxxx",
      "operatorUnionId": "NK0qMkt7e03wGiS26tiPxxxxxxxx",
      "openConversationId": "cidcxxxxxad4PB5ziwAOzgZGw\u003d\u003d"
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "servicegroup_group_info_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiGroupModel": {
    "operateData": {
      "bizId": "11222"
    },
    "openTeamId": "exxxxxxwsKEiE",
    "operateType": "BIZ_ID_BIND_CHANGE",
    "operatorNickName": "xxxx",
    "operatorUnionId": "NK0qMkt7e03wGiS26tiPxxxxxxxx",
    "openConversationId": "cidcxxxxxad4PB5ziwAOzgZGw\u003d\u003d"
  }
}
```
