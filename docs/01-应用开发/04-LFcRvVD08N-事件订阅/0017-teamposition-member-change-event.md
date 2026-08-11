---
title: "Teambition成员变更事件"
source_url: "https://open.dingtalk.com/document/development/teamposition-member-change-event"
namespace: "development"
slug: "teamposition-member-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 项目管理 > Teambition成员变更事件"
doc_id: "C97EIxYSDh"
updated_at: "2025-08-27 16:10:55"
---

> Source: https://open.dingtalk.com/document/development/teamposition-member-change-event
> Path: 应用开发 / 事件订阅 / 协同 > 项目管理 > Teambition成员变更事件
> Updated: 2025-08-27 16:10:55

# Teambition成员变更事件

> **[!IMPORTANT]**
>
> Teambition事件属于灰度阶段，如需使用请填写[宜搭申请单](https://kqu4sn.aliwork.com/o/teambition_event_apply)进行申请。

## **事件信息**

| **名称** | **值** |
| --- | --- |
| 中文名称 | Teambiton项目成员变更事件 |
| 英文名称 | project\_project\_member\_changed |
| 事件BizType | 257 |

## 功能描述

当Teambiton项目成员发生变更时，钉钉通过事件订阅的方式将项目成员变更内容推送给开发者，用于监听Teambiton项目成员变更信息。

## **事件体描述**

### **企业内部应用**

#### 项目成员角色加入

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_project\_member\_changed**：Teambition成员变更事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.project.member.create**：项目成员角色加入 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| memberUserId | 成员用户userId。 |
| memberRoleIds | 成员角色id集合。 |
| created | 创建时间。 |
| updated | 更新时间。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_project_member_changed",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.project.member.create",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "memberUserId": "0715153011125xxxx",
    "memberRoleIds": [
      "61a6dec77049d6003f94xxxx"
    ],
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z"
  }
}
```

#### 项目成员移除

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_project\_member\_changed**：Teambition成员变更事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.project.member.remove**：项目成员移除 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| memberUserId | 成员用户userId。 |
| created | 创建时间。 |
| updated | 更新时间。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_project_member_changed",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.project.member.remove",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "memberUserId": "0715153011125xxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z"
  }
}
```

#### 项目成员角色更新

| 参数 | 说明 |
| --- | --- |
| CorpId | 使用Teambition项目的企业corpId。 |
| EventType | 事件类型：   - **project\_project\_member\_changed**：Teambition成员变更事件 |
| EventTime | 事件发生的时间。 |
| BizId | Teambition项目的实例Id。 |
| eventSubType | 事件子类型：   - **tb.v3.project.member.role.update**：项目成员角色更新 |
| creatorId | 创建者userId。 |
| projectId | 项目Id。 |
| memberUserId | 成员用户userId。 |
| oldRoleIds | 更新前的角色id集合。 |
| roleIds | 新的角色id集合。 |
| created | 创建时间。 |
| updated | 更新时间。 |

#### **事件体示例**

```
{
  "CorpId": "dingc23b7b9682b4xxxx",
  "EventType": "project_project_member_changed",
  "EventTime": 1672046863855,
  "BizId": "tb_63a9690f89217deca9a3xxxx",
  "data": {
    "eventSubType": "tb.v3.project.member.role.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "memberUserId": "0715153011125xxxx",
    "oldRoleIds": [
      "6136dec77049d6003f94xxxx"
    ],
    "roleIds": [
      "62a6dec77049d6003f94xxxx"
    ],
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z"
  }
}
```

### **第三方企业应用**

#### 项目成员角色加入

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 项目成员角色加入对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.project.member.create**：项目成员角色加入 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| memberUserId | String | 成员用户userId。 |
| memberRoleIds | Array | 成员角色id集合。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_project_member_changed",
    "eventSubType": "tb.v3.project.member.create",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "memberUserId": "0715153011125xxxx",
    "memberRoleIds": [
      "61a6dec77049d6003f94xxxx"
    ],
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z"
  }
}
```

#### 项目成员移除

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 项目成员移除对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.project.member.remove**：项目成员移除 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| memberUserId | String | 成员用户userId。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_project_member_changed",
    "eventSubType": "tb.v3.project.member.remove",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "memberUserId": "0715153011125xxxx",
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z"
  }
}
```

#### 项目成员角色更新

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| corp\_id | String | 企业corp\_id。 |
| biz\_id | String | biz\_id无业务意义，幂等。 |
| biz\_type | Integer | 事件bizType。 |
| biz\_data | Object | 事件bizData介绍。 |
| data | Object | 项目成员角色更新对象。 |
| syncAction | String | 事件英文名。 |
| eventSubType | String | 事件子类型：   - **tb.v3.project.member.role.update**：项目成员角色更新 |
| creatorId | String | 创建者userId。 |
| projectId | String | 项目Id。 |
| memberUserId | String | 成员用户userId。 |
| oldRoleIds | Array | 更新前的角色id集合。 |
| roleIds | Array | 新的角色id集合。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |

#### **biz\_data数据示例如下：**

```
{
  "data": {
    "syncAction": "project_project_member_changed",
    "eventSubType": "tb.v3.project.member.role.update",
    "creatorId": "0715153011125xxxx",
    "projectId": "64ba333e4206372f3f5cxxxx",
    "memberUserId": "0715153011125xxxx",
    "oldRoleIds": [
      "6136dec77049d6003f94xxxx"
    ],
    "roleIds": [
      "62a6dec77049d6003f94xxxx"
    ],
    "created": "2022-12-26T09:27:43.733Z",
    "updated": "2022-12-26T09:27:43.733Z"
  }
}
```
