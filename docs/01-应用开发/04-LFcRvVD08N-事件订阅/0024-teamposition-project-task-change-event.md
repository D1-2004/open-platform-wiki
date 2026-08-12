---
title: "Teambition项目任务变更事件"
source_url: "https://open.dingtalk.com/document/development/teamposition-project-task-change-event"
namespace: "development"
slug: "teamposition-project-task-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 项目管理 > Teambition项目任务变更事件"
doc_id: "s9olh0pLK3"
updated_at: "2025-08-27 16:10:56"
---

> Source: https://open.dingtalk.com/document/development/teamposition-project-task-change-event
> Path: 应用开发 / 事件订阅 / 协同 > 项目管理 > Teambition项目任务变更事件
> Updated: 2025-08-27 16:10:56

# Teambition项目任务变更事件

> **[!IMPORTANT]**
>
> Teambition事件属于灰度阶段，如需使用请填写[宜搭申请单](https://kqu4sn.aliwork.com/o/teambition_event_apply)进行申请。

## **事件信息**

| **名称** | **值** |
| --- | --- |
| 中文名称 | Teambition项目任务变更事件 |
| 英文名称 | project\_task\_changed |
| 事件BizType | 258 |

## 功能描述

当Teambiton项目中任务本身发生变更时，钉钉通过事件订阅的方式将对应的项目中任务本身发生的变更内容推送给开发者，用于监听项目中任务变更信息。

## **事件体描述**

### **企业内部应用**

#### 任务归档

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_changed**：Teambition项目任务变更事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.archive**：任务归档 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_changed",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.archive",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务恢复归档

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_changed**：Teambition项目任务变更事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.unarchive**：任务恢复归档 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_changed",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.unarchive",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务删除

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_changed**：Teambition项目任务变更事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.remove**：任务删除 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |
| parentId | 父任务Id。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_changed",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.remove",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "parentId": "64c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务评论

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_changed**：Teambition项目任务变更事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.comment**：任务评论 |
| creatorId | 创建者userId。 |
| activityId | 动态Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |
| content | 动态内容。  **[!NOTE]**  包含附件Id 和 动态文本内容。 |
| mentionIds | 动态需提醒的人userId集合。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_changed",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.comment",
    "creatorId": "0715153011125xxxx",
    "activityId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "content": {
      "attachments": [],
      "text": "内容"
    },
    "mentionIds": [
      "0715153011125xxxx"
    ]
  }
}
```

#### 任务创建

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_changed**：Teambition项目任务变更事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.create**：任务创建 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |
| content | 任务标题。 |
| note | 任务备注。 |
| visible | 可见性。 |
| involveMembers | 参与者。 |
| startDate | 开始时间。 |
| dueDate | 截止时间。 |
| priority | 优先级。 |
| executorId | 执行者Id。 |
| stageId | 任务列表Id。 |
| tasklistId | 任务分组Id。 |
| sfcId | 任务类型Id。 |
| tfsId | 任务状态Id。 |
| organizationId | 企业Id。 |
| labels | 任务标签。 |
| ancestorIds | 父任务Id。 |
| customfields | 自定义字段Id。 |
| recurrence | 重复规则，使用rrule格式。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_changed",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.create",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "content": "任务标题",
    "note": "备注",
    "visible": "members",
    "involveMembers": [
      "0715153011125xxxx"
    ],
    "startDate": "2022-12-26T09:27:43.733Z",
    "dueDate": "2022-12-28T09:27:43.733Z",
    "priority": -10,
    "executorId": "0715153011125xxxx",
    "stageId": "65ba333e4206372f3f5cxxxx",
    "tasklistId": "62ba333e4206372f3f5cxxxx",
    "sfcId": "69ba333e4206372f3f5cxxxx",
    "tfsId": "6097f91f6ff268bcab40xxxx",
    "organizationId": "dingc23b7b9682b4xxxx",
    "labels": [],
    "ancestorIds": [
      "67ba333e4206372f3f5cxxxx"
    ],
    "customfields": [
      "601ba333e4206372f3f5cxxxx"
    ],
    "recurrence": [
      "RRULE:FREQ=WEEKLY;INTERVAL=1;DTSTART=20230126T030000Z"
    ]
  }
}
```

### **第三方企业应用**

#### 任务归档

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务归档对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.archive**：任务归档 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | String | 任务Id。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_changed",
    "eventSubType": "tb.v3.task.archive",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务恢复归档

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务恢复归档对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.unarchive**：任务恢复归档 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | String | 任务Id。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_changed",
    "eventSubType": "tb.v3.task.unarchive",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务删除

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务删除对象。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.remove**：任务删除 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | String | 任务Id。 |
| parentId | String | 父任务Id。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_changed",
    "eventSubType": "tb.v3.task.remove",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "parentId": "64c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务评论

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务评论对象。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.comment**：任务评论 |
| creatorId | String | 创建者userId。 |
| activityId | String | 动态Id。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | String | 任务Id。 |
| content | Object | 动态内容。  **[!NOTE]**  包含附件Id 和 动态文本内容。 |
| mentionIds | Array | 动态需提醒的人userId集合。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_changed",
    "eventSubType": "tb.v3.task.comment",
    "creatorId": "0715153011125xxxx",
    "activityId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "content": {
      "attachments": [],
      "text": "内容"
    },
    "mentionIds": [
      "0715153011125xxxx"
    ]
  }
}
```

#### 任务创建

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务创建对象。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.create**：任务创建 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | String | 任务Id。 |
| content | Object | 任务标题。 |
| note | String | 任务备注。 |
| visible | String | 可见性。 |
| involveMembers | Array | 参与者。 |
| startDate | String | 开始时间。 |
| dueDate | String | 截止时间。 |
| priority | Integer | 优先级。 |
| executorId | String | 执行者Id。 |
| stageId | String | 任务列表Id。 |
| tasklistId | String | 任务分组Id。 |
| sfcId | String | 任务类型Id。 |
| tfsId | String | 任务状态Id。 |
| organizationId | String | 企业Id。 |
| labels | Array | 任务标签。 |
| ancestorIds | Array | 父任务Id。 |
| customfields | Array | 自定义字段Id。 |
| recurrence | Array | 重复规则，使用rrule格式。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_changed",
    "eventSubType": "tb.v3.task.create",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "content": "任务标题",
    "note": "备注",
    "visible": "members",
    "involveMembers": [
      "0715153011125xxxx"
    ],
    "startDate": "2022-12-26T09:27:43.733Z",
    "dueDate": "2022-12-28T09:27:43.733Z",
    "priority": -10,
    "executorId": "0715153011125xxxx",
    "stageId": "65ba333e4206372f3f5cxxxx",
    "tasklistId": "62ba333e4206372f3f5cxxxx",
    "sfcId": "69ba333e4206372f3f5cxxxx",
    "tfsId": "6097f91f6ff268bcab40xxxx",
    "organizationId": "dingc23b7b9682b4xxxx",
    "labels": [],
    "ancestorIds": [
      "67ba333e4206372f3f5cxxxx"
    ],
    "customfields": [
      "601ba333e4206372f3f5cxxxx"
    ],
    "recurrence": [
      "RRULE:FREQ=WEEKLY;INTERVAL=1;DTSTART=20230126T030000Z"
    ]
  }
}
```
