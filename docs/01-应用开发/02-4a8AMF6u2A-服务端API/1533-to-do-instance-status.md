---
title: "更新实例状态"
source_url: "https://open.dingtalk.com/document/development/to-do-instance-status"
namespace: "development"
slug: "to-do-instance-status"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 更新实例状态"
doc_id: "sml9gsxb6m"
updated_at: "2025-09-08 19:04:45"
---

> Source: https://open.dingtalk.com/document/development/to-do-instance-status
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 更新实例状态
> Updated: 2025-09-08 19:04:45

# 更新实例状态

调用本接口更新实例状态。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对OA审批相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2023年1月9日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[更新实例状态](https://open.dingtalk.com/document/orgapp/update-instance-status)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

例如，用户A提交待办任务，待办处理节点有3级，B1、B2、B3三级处理人，当前B1已同意，处理节点在B2，B3尚未收到待办任务。

当调用该接口后，待办状态查询路径如下图所示，状态变更如下表所示：

![IMG_1888](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2806566161/p254727.jpg)

以上图中的审批流为例，当状态置为**COMPLETED**时，审批流状态如下：

| 提交/待办处理人 | 更新前 | 更新后 |
| --- | --- | --- |
| 用户A | 工作台-待办-已发起，审批中 | 工作台-待办-已发起，已通过 |
| 审批节点B1 | 工作台-待办-已处理，已通过 | 工作台-待办-已处理，已通过 |
| 审批节点B2 | 无此条待办任务 | 无此条待办任务 |
| 审批节点B3 | 无此条待办任务 | 无此条待办任务 |

以上图中的审批流为例，当状态置为**TERMINATED**时，审批流状态如下：

| 提交/待办处理人 | 更新前 | 更新后 |
| --- | --- | --- |
| 用户A | 工作台-待办-已发起，审批中 | 工作台-待办-已发起，已撤销 |
| 审批节点B1 | 工作台-待办-已处理，已通过 | 工作台-待办-已处理，已撤销 |
| 审批节点B2 | 无此条待办任务 | 无此条待办任务 |
| 审批节点B3 | 无此条待办任务 | 无此条待办任务 |

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/workrecord/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用，通过[获取第三方企业应用的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | UpdateProcessInstanceRequest | 否 |  | 请求对象。 |
| agentid | Number | 否 | 111 | 应用的agentid。   - 企业内部应用可在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。 - 第三方企业应用可调用[获取企业授权信息](https://open.dingtalk.com/document/isvapp/obtains-the-basic-information-of-an-enterprise)接口获取。 |
| process\_instance\_id | String | 是 | proc | 审批实例ID。   - 企业内部应用，由[创建实例](https://open.dingtalk.com/document/orgapp/initiate-an-approval-process-without-a-process)接口返回。 - 第三方企业应用，由[创建实例](https://open.dingtalk.com/document/isvapp/initiate-an-approval-process-without-a-process)接口返回。 |
| status | String | 是 | COMPLETED | 实例状态：   - **COMPLETED**：结束审批流 - **TERMINATED**：终止审批流 |
| result | String | 是 | agree | 实例结果：   - 实例状态是**COMPLETED**，必须设置代表以下含义。    - **agree**：同意   - **refuse**：拒绝 - 实例状态为**TERMINATED，**必须设置代表含义，result取值**agree**和**refuse**均代表撤销审批流。 |
| cancel\_running\_task | Boolean | 否 | true | 取消任务。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 65v5c56q2wv9 | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/workrecord/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "request":{
                "result":"agree",
                "agentid":"111",
                "process_instance_id":"proc",
                "cancel_running_task":true,
                "status":"COMPLETED"
        }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/workrecord/update");
OapiProcessWorkrecordUpdateRequest req = new OapiProcessWorkrecordUpdateRequest();
UpdateProcessInstanceRequest obj1 = new UpdateProcessInstanceRequest();
obj1.setAgentid(111L);
obj1.setProcessInstanceId("proc");
obj1.setStatus("COMPLETED");
obj1.setResult("agree");
obj1.setCancelRunningTask(true);
req.setRequest(obj1);
OapiProcessWorkrecordUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "request_id": "65v5c56q2wv9"
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
| 8100017 | 无操作审批流的权限，请检查审批实例或者模板是否正确 | 实例ID（process\_instance\_id）参数不正确 | 实例ID（process\_instance\_id）必须是[创建实例](https://open.dingtalk.com/document/orgapp/initiate-an-approval-process-without-a-process)接口返回的process\_instance\_id值，不能使用官方审批流的实例值 |
| 810003 | 审批流的表单格式错误 | 审批流的表单格式错误 | 请参照[创建实例](https://open.dingtalk.com/document/orgapp/initiate-an-approval-process-without-a-process)中「支持的表单参数」部分进行传值 |
| 820008 | 审批系统错误，原因为【审批表单已被管理员修改】 | 没有传result参数 | 更新审批单实例时，请传入result值后，再尝试 |
