---
title: "审批实例状态变更(定向)"
source_url: "https://open.dingtalk.com/document/development/event-workflow-instance-change-directed"
namespace: "development"
slug: "event-workflow-instance-change-directed"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > OA审批 > 审批实例状态变更(定向)"
doc_id: "DQW79c3iDn"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-workflow-instance-change-directed
> Path: 应用开发 / 事件订阅 / 办公 > OA审批 > 审批实例状态变更(定向)
> Updated: 2022-01-19 19:29:22

# 审批实例状态变更(定向)

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 审批实例状态变更(定向) |
| 英文名称 | workflow\_instance\_change\_directed |

## 功能描述

审批定向事件场景，ISV通过开放接口创建的官方OA审批，或用户在OA管理后台创建的“ISV套件”模板，此类场景下该审批模板是归属于ISV的，因此用户在钉钉侧或三方通过API触发相应实例、任务状态变更后，会给对应归属的ISV应用定向推送回调。

### 审批定向事件场景

ISV通过开放接口创建的官方OA审批，或用户在OA管理后台创建的“ISV套件”模板，给对应归属的ISV应用定向推送回调。
![图片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3810961761/p537684.png)该文档表示审批实例状态变更（定向）事件的推送数据。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "workflow_instance_change_directed",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "result": "agree",
    "processInstanceId": "adlB-HLWSEGKe_m-xxx",
    "createTime": 1670983873000,
    "finshTime": 1670983893000,
    "processCode": "PROC-27BBC5E6-DFFA-4EC3-A1F1-xxx",
    "businessId": "1",
    "type": "finsh",
    "title": "xx提交的审批模版测试",
    "version": "2",
    "url": "https://pre-aflow.dingtalk.com/xxx",
    "staffId": "managerxxx"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=247)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 247,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "processInstanceId": "adlB-HLWSEGKe_m-xxx",
    "syncAction": "workflow_instance_change_directed",
    "finshTime": 1670983893000,
    "businessId": "1",
    "type": "finsh",
    "title": "xx提交的审批模版测试",
    "version": "2",
    "url": "https://pre-aflow.dingtalk.com/xxx",
    "result": "agree",
    "createTime": 1670983873000,
    "processCode": "PROC-27BBC5E6-DFFA-4EC3-A1F1-xxx",
    "staffId": "managerxxx"
  }
}
```
