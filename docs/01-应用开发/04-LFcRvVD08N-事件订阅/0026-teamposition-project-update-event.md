---
title: "Teambition项目更新事件"
source_url: "https://open.dingtalk.com/document/development/teamposition-project-update-event"
namespace: "development"
slug: "teamposition-project-update-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 项目管理 > Teambition项目更新事件"
doc_id: "KjcBXi9EIo"
updated_at: "2025-08-27 16:10:58"
---

> Source: https://open.dingtalk.com/document/development/teamposition-project-update-event
> Path: 应用开发 / 事件订阅 / 协同 > 项目管理 > Teambition项目更新事件
> Updated: 2025-08-27 16:10:58

# Teambition项目更新事件

> **[!IMPORTANT]**
>
> Teambition事件属于灰度阶段，如需使用请填写[宜搭申请单](https://kqu4sn.aliwork.com/o/teambition_event_apply)进行申请。

## **事件信息**

| **名称** | **值** |
| --- | --- |
| 中文名称 | Teambition项目更新事件 |
| 英文名称 | project\_project\_updated |
| 事件BizType | 255 |

## 功能描述

当Teambiton项目属性发生更新操作时，钉钉通过事件订阅的方式将对应的项目属性的更新推送给开发者，用于监听项目属性更新信息。

## **事件体描述**

### **企业内部应用**

#### 项目名称更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_project\_updated**：Teambition项目更新事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.project.name.update**：项目名称更新 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| description | 描述内容。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_project_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.project.name.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "name": "项目2"
  }
}
```

#### 项目自定义字段更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_project\_updated**：Teambition项目更新事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.project.customfield.update**：项目自定义字段更新 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| customfieldId | 自定义字段Id。 |
| old | 更新前的自定义字段值。 |
| new | 新的自定义字段值。 |
| isDeleted | 标记该字段是否被移除：   - **true**：移除 - **false**：不移除 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_project_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.project.customfield.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "customfieldId": "64ba333e4206372f3f5cxxxx", 
    "old":[{"title":"国外继电保护元件 / 测试盒","meta":{"path":[{"value":"国外继电保护元件"},{"value":"测试盒"}]}}], 
    "new":[{"title":"国外继电保护元件 / 测试盒","meta":{"path":[{"value":"国外继电保护元件"},{"value":"测试盒"}]}},{"title":"国外继电保护元件 / 跳闸保持继电器-11TA","meta":{"path":[{"value":"国外继电保护元件"},{"value":"跳闸保持继电器-11TA"}]}}],
    "isDeleted": false
  }
}
```

#### 项目描述更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_project\_updated**：Teambition项目更新事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.project.description.update**：项目描述更新 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| description | 描述内容。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_project_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.project.description.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "description": "项目描述内容"
  }
}
```

#### 项目logo更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_project\_updated**：Teambition项目更新事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.project.logo.update**：项目logo更新 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| logo | 项目logo。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_project_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.project.logo.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "log": "https://tcs.teambition.net/thumbnail/312q1cc9d234c06599ab10cc***cb09/w/600/h/*****"
  }
}
```

#### 项目周期更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_project\_updated**：Teambition项目更新事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.project.period.update**：项目周期更新 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| created | 创建时间。 |
| startDate | 开始时间。 |
| endDate | 结束时间。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_project_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.project.period.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "startDate": "2023-01-01T00:30:00.000Z",
    "endDate": "2023-04-30T13:00:00.000Z"
  }
}
```

#### 项目状态更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_project\_updated**：Teambition项目更新事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.project.status.update**：项目状态更新 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| created | 创建时间。 |
| updated | 更新时间。 |
| degree | 项目进展。 |
| name | 名称。 |
| content | 内容。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_project_updated",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.project.status.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "degree": "normal",
    "name": "进度正常",
    "content": "本周开发进度正常，整体开发进度完成80%"
  }
}
```

### **第三方企业应用**

#### 项目自定义字段更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 项目自定义字段更新对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.project.customfield.update**：项目自定义字段更新 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| customfieldId | String | 自定义字段Id。 |
| old | Array | 更新前的自定义字段值。 |
| new | Array | 新的自定义字段值。 |
| isDeleted | Boolean | 标记该字段是否被移除：   - **true**：移除 - **false**：不移除 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_project_updated",
    "eventSubType": "tb.v3.project.customfield.update",
		"creatorId": "0715153011125xxxx",
		"projectId": "64ba333e4206372f3f5cxxxx",
		"created": "2022-12-26T09:27:43.733Z",
		"updated": "2022-12-26T09:27:43.733Z",
    "customfieldId": "64ba333e4206372f3f5cxxxx",
    "old":[{"title":"国外继电保护元件 / 测试盒","meta":{"path":[{"value":"国外继电保护元件"},{"value":"测试盒"}]}}],
    "new":[{"title":"国外继电保护元件 / 测试盒","meta":{"path":[{"value":"国外继电保护元件"},{"value":"测试盒"}]}},{"title":"国外继电保护元件 / 跳闸保持继电器-11TA","meta":{"path":[{"value":"国外继电保护元件"},{"value":"跳闸保持继电器-11TA"}]}}],
    "isDeleted": false
	}
}
```

#### 项目描述更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 项目描述更新对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.project.description.update**：项目描述更新 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| description | String | 描述内容。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_project_updated",
    "eventSubType": "tb.v3.project.description.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "description": "项目描述内容"
  }
}
```

#### 项目logo更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 项目logo更新对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.project.logo.update**：项目logo更新 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| logo | String | 项目logo。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_project_updated",
    "eventSubType": "tb.v3.project.logo.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "log": "https://tcs.teambition.net/thumbnail/312q1cc9d234c06599ab10cc***cb09/w/600/h/*****"
  }
}
```

#### 项目周期更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 项目周期更新对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.project.period.update**：项目周期更新 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| created | String | 创建时间。 |
| startDate | String | 开始时间。 |
| endDate | String | 结束时间。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_project_updated",
    "eventSubType": "tb.v3.project.period.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "startDate": "2023-01-01T00:30:00.000Z",
    "endDate": "2023-04-30T13:00:00.000Z"
  }
}
```

#### 项目状态更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 项目状态更新对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.project.status.update**：项目状态更新 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| degree | String | 项目进展。 |
| name | String | 名称。 |
| content | String | 内容。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_project_updated",
    "eventSubType": "tb.v3.project.status.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "degree": "normal",
    "name": "进度正常",
    "content": "本周开发进度正常，整体开发进度完成80%"
  }
}
```

#### 项目名称更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 项目名称更新对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.project.name.update**：项目名称更新 |
| BizId | String | Teambition事件Id。 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| name | String | 项目名称。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_project_updated",
    "eventSubType": "tb.v3.project.name.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z",
    "name": "项目2"
  }
}
```
