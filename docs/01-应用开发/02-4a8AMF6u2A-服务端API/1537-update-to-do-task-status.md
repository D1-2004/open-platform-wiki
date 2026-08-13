---
title: "更新待办状态"
source_url: "https://open.dingtalk.com/document/development/update-to-do-task-status"
namespace: "development"
slug: "update-to-do-task-status"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 更新待办状态"
doc_id: "He7ThM5tPr"
updated_at: "2025-09-08 19:04:48"
---

> Source: https://open.dingtalk.com/document/development/update-to-do-task-status
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 更新待办状态
> Updated: 2025-09-08 19:04:48

# 更新待办状态

调用本接口更新待办任务的状态。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对OA审批相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2023年1月9日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[更新流程中心任务状态](https://open.dingtalk.com/document/orgapp/update-process-center-task-status)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

调用该接口后，相对应的待办卡片会在钉钉待办里面消失，移到“**已完成**”列表中。钉钉审批页面，对应的审批单会移到“**已处理**”页面，如下图所示。

**钉钉工作台 -> OA审批 -> 审批中心 -> 已处理：**

![image ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7244825661/p500693.png)

**钉钉客户端 -> 待办 -> OA审批 -> 已完成：**

![image ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7244825661/p500694.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/workrecord/task/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用，通过[获取第三方企业应用的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | UpdateTaskRequest | 是 |  | 请求对象。 |
| agentid | Number | 是 | 111 | 应用标识。可在开发者后台的应用详情页获取。 |
| process\_instance\_id | String | 是 | proc-zzz | 实例ID。   - 企业内部应用，由[创建实例](https://open.dingtalk.com/document/orgapp/initiate-an-approval-process-without-a-process)接口获取。 - 第三方企业应用，由[创建实例](https://open.dingtalk.com/document/isvapp/initiate-an-approval-process-without-a-process)接口获取。 |
| tasks | TaskTopVo[] | 是 |  | 待办任务列表。 |
| task\_id | Number | 是 | 111 | 待办任务ID。   - 企业内部应用，需要在调用[查询待办列表](https://open.dingtalk.com/document/orgapp/query-a-user-s-to-do-items)接口时，主动设置该值。 - 第三方企业应用，需要在调用[查询待办列表](https://open.dingtalk.com/document/isvapp/query-a-user-s-to-do-items)接口时，主动设置该值。 |
| status | String | 是 | COMPLETED | 任务状态：   - **CANCELED**：取消  例如一个或签节点，同时有多个任务，其中一个审批人完成审批后，剩余的审批任务可以置为CANCELED状态。 - **COMPLETED**：完成  COMPLETED表示任务被完成，此时需要传**result**参数，分别表示审批通过（agree）和审批拒绝（refuse）。 |
| result | String | 是 | AGREE | 当status为COMPLETED时，必须指定任务结果：   - **AGREE**：同意 - **REFUSE**：拒绝   **[!NOTE]**  当status为**CANCELED**时，不需要传result。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |
| request\_id | String | 7jtw2fl4kmlm | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/workrecord/task/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "request": {
        "agentid":111,
        "process_instance_id": "b6a42e32-1867-499c-94f2-e0b221423313",
        "tasks": [
            {
                "result": "AGREE",
                "task_id": 65429579088,
                "status": "COMPLETED"
            }
        ]
    }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/workrecord/task/update");
OapiProcessWorkrecordTaskUpdateRequest req = new OapiProcessWorkrecordTaskUpdateRequest();
UpdateTaskRequest obj1 = new UpdateTaskRequest();
obj1.setAgentid(111L);
obj1.setProcessInstanceId("b6a42e32-1867-499c-94f2-e0b221423313");
List<TaskTopVo> list3 = new ArrayList<TaskTopVo>();
TaskTopVo obj4 = new TaskTopVo();
list3.add(obj4);
obj4.setTaskId(65429579088L);
obj4.setStatus("COMPLETED");
obj4.setResult("AGREE");
obj1.setTasks(list3);
req.setRequest(obj1);
OapiProcessWorkrecordTaskUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "errmsg":"ok",
        "request_id": "146262d9p0xmi"
}
```

## 错误码

| **错误码（errorcode）** | **错误码描述（errmsg）** | **错误原因** | **解决方案** |
| --- | --- | --- | --- |
| 43007 | 需要授权 | access\_token不正确 | 请确认access\_token是否正确 |
| 40056 | 无效的微应用ID | 微应用ID参数错误 | 请确认微应用ID是否正确 |
| 40083 | 无效的suiteKey | 应用suiteKey参数错误 | 请确认应用suiteKey是否正确 |
| -1 | 系统繁忙 | 系统繁忙 | 请稍后重试 |
| 400001 | 系统繁忙 | 系统繁忙 | 请稍后重试 |
| 820004 | 流程实例不存在 | 流程实例参数错误 | 请确认流程实例参数是否正确 |
| 8100017 | 无操作审批流的权限，请检查审批实例或者模板是否正确 | 无操作审批流的权限，审批实例或者模板参数错误 | 实例ID（process\_instance\_id）必须是[创建实例](https://open.dingtalk.com/document/orgapp/initiate-an-approval-process-without-a-process)接口返回的process\_instance\_id值，不能使用官方审批流的实例值。 |
