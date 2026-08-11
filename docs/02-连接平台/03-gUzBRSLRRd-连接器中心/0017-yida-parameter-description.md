---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/yida-parameter-description"
namespace: "connection"
slug: "yida-parameter-description"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 宜搭 > 参数说明"
doc_id: "WtyzAH5f1b"
updated_at: "2025-09-23 19:20:44"
---

> Source: https://open.dingtalk.com/document/connection/yida-parameter-description
> Path: 连接平台 / 连接器中心 / 官方连接器 > 宜搭 > 参数说明
> Updated: 2025-09-23 19:20:44

# 参数说明

# **执行动作**

## **发起宜搭审批流程**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| formUuid | String | 是 | 输入[表单编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，表单唯一ID。 |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |
| formDataJson | String | 是 | 表单数据。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |

## **更新流程实例**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| processInstanceId | String | 是 | 流程实例ID。 |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |
| updateFormDataJson | String | 是 | 表单数据。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |

## **删除流程实例**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| processInstanceId | String | 是 | 流程实例ID。 |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |

## **终止流程实例**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| processInstanceId | String | 是 | 流程实例ID。 |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |

## **获取流程实例**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| formUuid | String | 是 | 输入[表单编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，表单唯一ID。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |

## **批量获取流程实例列表**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| processInstanceIds | String | 是 | 流程实例ID列表。 |

## **根据实例ID获取流程实例**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| id | String | 是 | 流程实例ID。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |

## **保存表单数据**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| formUuid | String | 是 | 输入[表单编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，表单唯一ID。 |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |
| formDataJson | String | 是 | 表单数据。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |

## **更新表单数据**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |
| updateFormDataJson | String | 是 | 更新的表单数据。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| formInstanceId | String | 是 | 流程实例ID。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |

## **删除表单数据**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| formInstanceId | String | 是 | 流程实例ID。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |

## **查询表单实例数据**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| formUuid | String | 是 | 输入[表单编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，表单唯一ID。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |

## **获取子表组件数据**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| formUuid | String | 是 | 输入[表单编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，表单唯一ID。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| formInstanceId | String | 是 | 要查询的实例的实例ID。 |
| tableFieldId | String | 是 | 需要查找的子表单组件ID。 |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |

## **获取多个表单实例ID**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| formUuid | String | 是 | 输入[表单编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，表单唯一ID。 |
| pageNumber | Integer | 是 | 分页页码。 |
| pageSize | Integer | 是 | 分页大小。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |

## **获取表单组件定义列表**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| formUuid | String | 是 | 输入[表单编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，表单唯一ID。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |

## **转交任务**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| processInstanceId | String | 是 | 流程实例ID。 |
| remark | String | 是 | 审批意见。 |
| nowActionExecutorId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| taskId | Long | 是 | 任务ID。 |

## **提交评论**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| formInstanceId | String | 是 | 示例ID。 |
| content | String | 是 | 评论内容。 |

## **获取审批评论**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| processInstanceId | String | 是 | 流程实例ID。 |

## **获取发送给用户的通知**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| token | String | 是 | 验权token。 校验方式如下：md5(corpId + userId + code)。md5取32位大写值。  **[!NOTE]**   - 每个企业有自己的唯一code。 - code可在宜搭**平台管理 > 基本信息**中获取**CorpToken。** |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| pageNumber | Integer | 是 | 分页页码。 |
| pageSize | Integer | 是 | 分页大小。 |
| corpId | String | 是 | 输入[组织ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，组织corpId。 |

## **获取任务列表（组织维度）**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| token | String | 是 | 验权token。 校验方式如下：md5(corpId + userId + code)。md5取32位大写值。  **[!NOTE]**   - 每个企业有自己的唯一code。 - code可在宜搭**平台管理 > 基本信息**中获取**CorpToken。** |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| corpId | String | 是 | 输入[组织ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，组织corpId。 |

## **查询流程运行任务（vpc）**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| processInstanceId | String | 是 | 流程实例ID。 |

## **获取组织内某人提交的任务**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| token | String | 是 | 验权token。 校验方式如下：md5(corpId + userId + code)。md5取32位大写值。  **[!NOTE]**   - 每个企业有自己的唯一code。 - code可在宜搭**平台管理 > 基本信息**中获取**CorpToken。** |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| corpId | String | 是 | 输入[组织ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，组织corpId。 |

## **获取组织内已完成的审批任务**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| token | String | 是 | 验权token。 校验方式如下：md5(corpId + userId + code)。md5取32位大写值。  **[!NOTE]**   - 每个企业有自己的唯一code。 - code可在宜搭**平台管理 > 基本信息**中获取**CorpToken。** |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| corpId | String | 是 | 输入[组织ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，组织corpId。 |

## **查询抄送我的任务列表（应用维度）**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| appType | String | 是 | 输入[编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用编码。 |
| systemToken | String | 是 | 输入[密钥](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，应用密钥。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户 ID。 |
| pageNumber | Integer | 是 | 分页页码。 |
| pageSize | Integer | 是 | 分页大小。 |
