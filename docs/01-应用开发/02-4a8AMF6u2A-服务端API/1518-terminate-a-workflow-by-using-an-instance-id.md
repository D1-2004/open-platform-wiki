---
title: "撤销审批实例"
source_url: "https://open.dingtalk.com/document/development/terminate-a-workflow-by-using-an-instance-id"
namespace: "development"
slug: "terminate-a-workflow-by-using-an-instance-id"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 撤销审批实例"
doc_id: "I34WyV3qpv"
updated_at: "2025-09-08 19:04:32"
---

> Source: https://open.dingtalk.com/document/development/terminate-a-workflow-by-using-an-instance-id
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 撤销审批实例
> Updated: 2025-09-08 19:04:32

# 撤销审批实例

调用本接口，撤销发起的审批实例。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对OA审批相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2022年10月8日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[撤销审批实例](https://open.dingtalk.com/document/orgapp/revoke-an-approval-instance)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

撤销审批实例后，审批状态为“已撤销”。

> **[!IMPORTANT]**
>
> 审批发起15秒内不能撤销审批流程。

调用本接口，可以在审批单看到审批实例已撤销，如下图所示。![撤销测试](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9291796361/p352436.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/instance/terminate`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | be311xxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | TerminateProcessInstanceRequestV2 | 是 |  | 终止审批请求。 |
| process\_instance\_id | String | 是 | a171de6c-8bxxxx | 审批实例ID，可通过调用[获取审批实例ID列表](https://open.dingtalk.com/document/orgapp/operation-to-retrieve-a-list-of)接口获取。 |
| is\_system | Boolean | 是 | false | 是否通过系统操作：   - **true**：由系统直接终止 - **false**：由指定的操作者终止 |
| remark | String | 否 | 说明 | 终止说明。 |
| operating\_userid | String | 否 | 133743186427339452 | 操作人的userid。  当**is\_system**为**false**时，该参数必传。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Boolean | true | 终止成功。 |
| success | Boolean | true | 调用成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | ny1xyyws0k2f | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/instance/terminate?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "request":{
                "is_system":false,
                "process_instance_id":"a171de6c-8bxxxx",
                "operating_userid":"133743186427339452",
                "remark":"说明"
        }
}
```

**请求示例（JAVA SDK）**

```
  DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/instance/terminate");
  OapiProcessInstanceTerminateRequest req = new OapiProcessInstanceTerminateRequest();
  TerminateProcessInstanceRequestV2 processInstanceRequestV2 = new TerminateProcessInstanceRequestV2();
  processInstanceRequestV2.setProcessInstanceId("a171de6c-8bxxxx");
  processInstanceRequestV2.setIsSystem(false);
  processInstanceRequestV2.setRemark("说明");
  processInstanceRequestV2.setOperatingUserid("133743186427339452");
  req.setRequest(processInstanceRequestV2);
  OapiProcessInstanceTerminateResponse rsp = client.execute(req, access_token);
  System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "result":true,
        "errcode":0,
        "success":true,
        "errmsg":"ok",
        "request_id":"ny1xyyws0k2f"
}
```
