---
title: "文档知识库中小组变更"
source_url: "https://open.dingtalk.com/document/development/event-doc-spaces-team-change"
namespace: "development"
slug: "event-doc-spaces-team-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 文档 > 文档知识库中小组变更"
doc_id: "YmS108IvWX"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-doc-spaces-team-change
> Path: 应用开发 / 事件订阅 / 协同 > 文档 > 文档知识库中小组变更
> Updated: 2022-01-19 19:29:22

# 文档知识库中小组变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 文档知识库中小组变更 |
| 英文名称 | doc\_spaces\_team\_change |

## 功能描述

文档知识库中小组变更事件数据说明。

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
  "eventType": "doc_spaces_team_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "unionId": "h3ZErk0**giEiE",
    "teamId": "YRB****4Jm",
    "type": "TEAM_MODIFY"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "doc_spaces_team_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "unionId": "h3ZErk0**giEiE",
  "teamId": "YRB****4Jm",
  "type": "TEAM_MODIFY"
}
```
