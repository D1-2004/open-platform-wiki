---
title: "审批模板状态变更"
source_url: "https://open.dingtalk.com/document/development/events-workflow-form-change"
namespace: "development"
slug: "events-workflow-form-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > OA审批 > 审批模板状态变更"
doc_id: "O4wE7Vy92O"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-workflow-form-change
> Path: 应用开发 / 事件订阅 / 办公 > OA审批 > 审批模板状态变更
> Updated: 2022-01-19 19:29:22

# 审批模板状态变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 审批模板状态变更 |
| 英文名称 | workflow\_form\_change |

## 功能描述

OA审批表单模板变更事件，用户在OA审批管理后台操作模板变更后（包括 create：创建、update：编辑、published：启用、invalid：停用、delete：删除、sort：排序等），同时推送给客户业务系统，用于客户业务系统处理内部业务逻辑。

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
  "eventType": "workflow_form_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "creatorUserId": "userId123",
    "corpId": "ding123",
    "formCode": "PROC-123",
    "resource": "/workflow_form_change/bizCategoryId/hrm.xxx/processCode/PROC-123/type/create",
    "type": "create",
    "modifierUserId": "userId123",
    "appUuid": "ding123",
    "appIds": [
      "1"
    ],
    "modifyTime": "1638326995000",
    "createTime": "1638326995000",
    "appType": "0",
    "bizCategoryId": "hrm.xxx",
    "name": "模板测试"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "workflow_form_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "creatorUserId": "userId123",
  "corpId": "ding123",
  "formCode": "PROC-123",
  "resource": "/workflow_form_change/bizCategoryId/hrm.xxx/processCode/PROC-123/type/create",
  "type": "create",
  "modifierUserId": "userId123",
  "appUuid": "ding123",
  "appIds": [
    "1"
  ],
  "modifyTime": "1638326995000",
  "createTime": "1638326995000",
  "appType": "0",
  "bizCategoryId": "hrm.xxx",
  "name": "模板测试"
}
```
