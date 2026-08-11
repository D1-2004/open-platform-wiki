---
title: "Teambiton项目变更事件"
source_url: "https://open.dingtalk.com/document/development/teambiton-project-change-event"
namespace: "development"
slug: "teambiton-project-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 项目管理 > Teambiton项目变更事件"
doc_id: "MPvNIMJkBx"
updated_at: "2025-08-27 16:10:54"
---

> Source: https://open.dingtalk.com/document/development/teambiton-project-change-event
> Path: 应用开发 / 事件订阅 / 协同 > 项目管理 > Teambiton项目变更事件
> Updated: 2025-08-27 16:10:54

# Teambiton项目变更事件

> **[!IMPORTANT]**
>
> Teambition事件属于灰度阶段，如需使用请填写[宜搭申请单](https://kqu4sn.aliwork.com/o/teambition_event_apply)进行申请。

## **事件信息**

| **名称** | **值** |
| --- | --- |
| 中文名称 | Teambiton项目变更事件 |
| 英文名称 | project\_project\_changed |
| 事件BizType | 254 |

## 功能描述

当Teambiton项目本身发生变更时，钉钉通过事件订阅的方式将对应的项目本身的变更内容推送给开发者，用于监听项目变更信息。

## **事件体描述**

### **企业内部应用**

#### **项目创建**

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_project\_changed**：Teambition项目变更事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.project.create**：项目创建 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| organizationId | 企业Id。 |
| sourceId | 模板项目Id。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_project_changed",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "creatorId": "0715153011125xxxx",
    "eventSubType": "tb.v3.project.create",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "organizationId": "dingc23b7b9682b4xxxx",
    "sourceId": "64ba333e4206372f3f5cxxxx"
  }
}
```

#### **项目删除**

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_project\_changed**：Teambition项目变更事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition事件Id。 |
| eventSubType | 事件子类型：   - **tb.v3.project.remove**：项目删除 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| id | 项目Id。 |
| name | 项目名称。 |
| description | 项目描述。 |
| logo | 项目logo地址。 |
| created | 创建时间。 |
| updated | 更新时间。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_project_changed",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.project.remove",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "project": {
      "id": "63a9690f89217deca9a3xxxx",
      "name": "项目2",
      "description": "项目描述信息",
      "logo": "http://xxxxxxx"
    },
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z"
  }
}
```

#### **项目回收/恢复回收**

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_project\_changed**：Teambition项目变更事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.project.isArchived.update**：项目回收/恢复回收 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| isArchived | 是否归档：   - **true**：归档 - **false**：不归档 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_project_changed",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.project.isArchived.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "isArchived": true
  }
}
```

#### **项目归档**

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_project\_changed**：Teambition项目 变更事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.project.suspend.update**：项目归档 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_project_changed",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.project.suspend.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z"
  }
}
```

#### **项目解归档**

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_project\_changed**：Teambition项目 变更事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.project.unsuspend**：项目解归档 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_project_changed",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.project.unsuspend",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z"
  }
}
```

### **第三方企业应用**

#### 项目创建

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 项目创建对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.project.create**：项目创建 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| organizationId | String | 企业Id。 |
| sourceId | String | 模板项目Id。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_project_changed",
    "creatorId": "0715153011125xxxx",
    "eventSubType": "tb.v3.project.create",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "organizationId": "dingc23b7b9682b4xxxx",
    "sourceId": "64ba333e4206372f3f5cxxxx"
  }
}
```

#### 项目删除

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 项目删除对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.project.remove**：项目删除 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| project | Object | 项目对象。 |
| id | String | 项目Id。 |
| name | String | 项目名称。 |
| description | String | 项目描述。 |
| logo | String | 项目logo地址。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_project_changed",
    "eventSubType": "tb.v3.project.remove",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "project": {
      "id": "63a9690f89217deca9a3xxxx",
      "name": "项目2",
      "description": "项目描述信息",
      "logo": "http://xxxxxxx"
    },
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z"
  }
}
```

#### 项目回收/恢复回收

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 项目回收/恢复回收对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.project.isArchived.update**：项目回收/恢复回收 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| isArchived | Boolean | 是否归档：   - **true**：归档 - **false**：不归档 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_project_changed",
    "eventSubType": "tb.v3.project.isArchived.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "isArchived": true
  }
}
```

#### **项目归档**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 项目归档对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.project.suspend.update**：项目归档 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_project_changed",
    "eventSubType": "tb.v3.project.suspend.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z"
  }
}
```

#### **项目解归档**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 项目解归档对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.project.unsuspend**：项目解归档 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_project_changed",
    "eventSubType": "tb.v3.project.unsuspend",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z"
  }
}
```
