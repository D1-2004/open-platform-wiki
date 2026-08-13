---
title: "Teambition任务更新事件"
source_url: "https://open.dingtalk.com/document/development/teamposition-task-update-event"
namespace: "development"
slug: "teamposition-task-update-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 项目管理 > Teambition任务更新事件"
doc_id: "gEUYMPCllP"
updated_at: "2025-08-27 16:10:57"
---

> Source: https://open.dingtalk.com/document/development/teamposition-task-update-event
> Path: 应用开发 / 事件订阅 / 协同 > 项目管理 > Teambition任务更新事件
> Updated: 2025-08-27 16:10:57

# Teambition任务更新事件

> **[!IMPORTANT]**
>
> Teambition事件属于灰度阶段，如需使用请填写[宜搭申请单](https://kqu4sn.aliwork.com/o/teambition_event_apply)进行申请。

## **事件信息**

| **名称** | **值** |
| --- | --- |
| 中文名称 | Teambition任务更新事件 |
| 英文名称 | project\_task\_updated |
| 事件BizType | 259 |

## 功能描述

当Teambiton项目中任务属性内容发生更新时，钉钉通过事件订阅的方式将对应的项目中任务属性内容的变更推送给开发者，用于监听项目中任务属性更新的信息。

## **事件体描述**

### **企业内部应用**

#### 任务标题更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_updated**：Teambition任务更新事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.content.update**：任务标题更新 |
| creatorId | 创建者userId。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |
| content | 任务标题。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.content.update",
    "creatorId": "0715153011125xxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "content": "任务标题"
  }
}
```

#### 任务自定义字段更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_updated**：Teambition任务更新事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.customfield.update**：任务自定义字段更新 |
| creatorId | 创建者userId。 |
| customfieldId | 自定义字段Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |
| customfieldType | 自定义字段类型。 |
| customfieldValue | 自定义字段内容。 |
| customfieldOldValue | 自定义字段更新前内容。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.customfield.update",
    "creatorId": "0715153011125xxxx",
    "customfieldId": "638e0e06788b2b484b87xxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "customfieldType": "lookup2",
    "customfieldValue": [{"_id":"worktime:total:plantime","title":"0","meta":{"unit":"ms"}}],
    "customfieldOldValue": [{"_id":"worktime:total:plantime","title":"0","meta":{"unit":"ms"}}]
  }
}
```

#### 任务截止时间更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_updated**：Teambition任务更新事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.dueDate.update**：任务截止时间更新 |
| creatorId | 创建者userId。 |
| dueDate | 截止时间。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.dueDate.update",
    "creatorId": "0715153011125xxxx",
    "dueDate": "2023-01-25T10:00:00.000Z",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务执行者更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_updated**：Teambition任务更新事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.executor.update**：任务执行者更新 |
| creatorId | 创建者userId。 |
| executorId | 执行者Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.executor.update",
    "creatorId": "0715153011125xxxx",
    "executorId": "0715153011125xxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务参与者更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_updated**：Teambition任务更新事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.involveMembers.update**：任务参与者更新 |
| creatorId | 创建者userId。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |
| oldInvolveMembers | 更新之前的参与者userId集合。 |
| involveMembers | 更新后的参与者userId集合。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.involveMembers.update",
    "creatorId": "0715153011125xxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "oldInvolveMembers": [
      "0715153011125xxxx"
    ],
    "involveMembers": [
      "0715153011125xxxx",
      "0823153011125xxxx"
    ]
  }
}
```

#### 任务备注更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_updated**：Teambition任务更新事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.note.update**：任务备注更新 |
| creatorId | 创建者userId。 |
| note | 任务备注。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.note.update",
    "creatorId": "0715153011125xxxx",
    "note": "任务备注",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```

#### **任务的父任务更新（同项目）**

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_updated**：Teambition任务更新事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.parent.update**：任务的父任务更新（同项目） |
| creatorId | 创建者userId。 |
| parentId | 父任务Id。 |
| old | 变更前父任务Id。 |
| taskId | 任务Id。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.parent.update",
    "creatorId": "0715153011125xxxx",
    "parentId": "64ba333e4206372f3f5cxxxx",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "old": {
      "parentId": "63ca154641b12773821eee83"
    }
  }
}
```

#### 任务优先级更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_updated**：Teambition任务更新事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.priority.update**：任务优先级更新 |
| creatorId | 创建者userId。 |
| priority | 优先级。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.parent.update",
    "creatorId": "0715153011125xxxx",
    "parentId": "64ba333e4206372f3f5cxxxx",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "old": {
      "parentId": "63ca154641b12773821eee83"
    }
  }
}
```

#### 任务开始时间更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_updated**：Teambition任务更新事件。 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.startDate.update**：任务开始时间更新 |
| creatorId | 创建者userId。 |
| startDate | 开始时间。  **[!NOTE]**  如清除，则 startDate = ''。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.startDate.update",
    "creatorId": "0715153011125xxxx",
    "startDate": "2022-12-26T09:27:43.733Z",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务状态更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_updated**：Teambition任务更新事件。 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.taskflowstatus.update**：任务状态更新 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |
| tfsId | 任务状态Id。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.taskflowstatus.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "tfsId": "62eb322f414019003fbdxxxx"
  }
}
```

#### 任务进度更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_updated**：Teambition任务更新事件。 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.progress.update**：任务进度更新 |
| creatorId | 创建者userId。 |
| progress | 任务进度。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.task.progress.update",
    "creatorId": "0715153011125xxxx",
    "progress": 70,
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务标签更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_task\_updated**：Teambition任务更新事件。 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.task.tagIds.update**：任务标签更新 |
| creatorId | 创建者userId。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| taskId | 任务Id。 |
| oldTagIds | 标签集合（过去）。 |
| tagIds | 标签集合。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_task_changed",
  "EventTime": 1672046863855,
  "tag": "tb.v3.task.tagIds.update",
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "creatorId": "0715153011125xxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "oldTagIds": [],
    "tagIds": [
      "63cb5e7370410600180bxxxx",
      "63ca227f851050001889xxxx"
    ]
  }
}
```

### **第三方企业应用**

#### 任务标题更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务标题更新对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.content.update**：任务标题更新 |
| creatorId | String | 创建者userId。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | String | 任务Id。 |
| content | String | 任务标题。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_updated",
    "eventSubType": "tb.v3.task.content.update",
    "creatorId": "0715153011125xxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "content": "任务标题"
  }
}
```

#### 任务自定义字段更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务自定义字段更新对象。 |
| syncAction | String | 事件英文名称。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.customfield.update**：任务自定义字段更新 |
| creatorId | String | 创建者userId。 |
| customfieldId | String | 自定义字段Id。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | String | 任务Id。 |
| customfieldType | String | 自定义字段类型。 |
| customfieldValue | Array | 自定义字段内容。 |
| customfieldOldValue | Array | 自定义字段更新前内容。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_updated",
    "eventSubType": "tb.v3.task.customfield.update",
    "creatorId": "0715153011125xxxx",
    "customfieldId": "638e0e06788b2b484b87xxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "customfieldType": "lookup2",
    "customfieldValue": [{"_id":"worktime:total:plantime","title":"0","meta":{"unit":"ms"}}],
    "customfieldOldValue": [{"_id":"worktime:total:plantime","title":"0","meta":{"unit":"ms"}}]
  }
}
```

#### 任务截止时间更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务截止时间更新对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.dueDate.update**：任务截止时间更新 |
| creatorId | String | 创建者userId。 |
| dueDate | String | 截止时间。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | String | 任务Id。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_updated",
    "eventSubType": "tb.v3.task.dueDate.update",
    "creatorId": "0715153011125xxxx",
    "dueDate": "2023-01-25T10:00:00.000Z",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务执行者更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务执行者更新对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.executor.update**：任务执行者更新 |
| creatorId | String | 创建者userId。 |
| executorId | String | 执行者Id。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | String | 任务Id。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_updated",
    "eventSubType": "tb.v3.task.executor.update",
    "creatorId": "0715153011125xxxx",
    "executorId": "0715153011125xxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务参与者更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务参与者更新对象。 |
| syncAction | String | 事件英文名称。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.involveMembers.update**：任务参与者更新 |
| creatorId | String | 创建者userId。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | String | 任务Id。 |
| oldInvolveMembers | Array | 更新之前的参与者userId集合。 |
| involveMembers | Array | 更新后的参与者userId集合。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_updated",
    "eventSubType": "tb.v3.task.involveMembers.update",
    "creatorId": "0715153011125xxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "oldInvolveMembers": [
      "0715153011125xxxx"
    ],
    "involveMembers": [
      "0715153011125xxxx",
      "0823153011125xxxx"
    ]
  }
}
```

#### 任务备注更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务备注更新对象。 |
| syncAction | String | 事件英文名称。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.note.update**：任务备注更新 |
| creatorId | String | 创建者userId。 |
| note | String | 任务备注。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | Array | 任务Id。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_updated",
    "eventSubType": "tb.v3.task.note.update",
    "creatorId": "0715153011125xxxx",
    "note": "任务备注",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务的父任务更新（同项目）

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务的父任务更新（同项目）对象。 |
| syncAction | String | 事件英文名称。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.parent.update**：任务的父任务更新（同项目） |
| creatorId | String | 创建者userId。 |
| parentId | String | 父任务Id。 |
| old | Object | 变更前父任务对象。 |
| taskId | String | 任务Id。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_updated",
    "eventSubType": "tb.v3.task.parent.update",
    "creatorId": "0715153011125xxxx",
    "parentId": "64ba333e4206372f3f5cxxxx",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "old": {"parentId":"63ca154641b12773821eee83"}
  }
}
```

#### 任务优先级更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务优先级更新对象。 |
| syncAction | String | 事件英文名称。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.priority.update**：任务优先级更新 |
| creatorId | String | 创建者userId。 |
| priority | String | 优先级。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | String | 任务Id。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_updated",
    "eventSubType": "tb.v3.task.priority.update",
    "creatorId": "0715153011125xxxx",
    "priority": "2",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务开始时间更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务开始时间更新对象。 |
| syncAction | String | 事件英文名称。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.startDate.update**：任务开始时间更新 |
| creatorId | String | 创建者userId。 |
| startDate | String | 开始时间。  **[!NOTE]**  如清除，则 startDate = ''。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | String | 任务Id。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_updated",
    "eventSubType": "tb.v3.task.startDate.update",
    "creatorId": "0715153011125xxxx",
    "startDate": "2022-12-26T09:27:43.733Z",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务状态更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务状态更新对象。 |
| syncAction | String | 事件英文名称。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.startDate.update**：任务开始时间更新 |
| creatorId | String | 创建者userId。 |
| startDate | String | 开始时间。  **[!NOTE]**  如清除，则 startDate = ''。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | String | 任务Id。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_updated",
    "eventSubType": "tb.v3.task.taskflowstatus.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "tfsId": "62eb322f414019003fbdxxxx"
  }
}
```

#### 任务进度更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务进度更新对象。 |
| syncAction | String | 事件英文名称。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.progress.update**：任务进度更新 |
| creatorId | String | 创建者userId。 |
| progress | Integer | 任务进度。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | String | 任务Id。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_updated",
    "eventSubType": "tb.v3.task.progress.update",
    "creatorId": "0715153011125xxxx",
    "progress": 70,
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```

#### 任务标签更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 任务标签更新对象。 |
| syncAction | String | 事件英文名称。 |
| eventSubType | String | 事件子类型：   - **tb.v3.task.progress.update**：任务进度更新 |
| creatorId | String | 创建者userId。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| taskId | String | 任务Id。 |
| oldTagIds | Array | 标签集合（过去）。 |
| tagIds | Array | 标签集合。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_task_updated",
    "eventSubType": "tb.v3.task.tagIds.update",
    "creatorId": "0715153011125xxxx",
    "oldTagIds": [],
    "tagIds": [
      "63cb5e7370410600180bxxxx",
      "63ca227f851050001889xxxx"
    ],
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "taskId": "63c7f91f6ff268bcab40xxxx"
  }
}
```
