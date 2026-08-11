---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/intelligent-personnel-instructions"
namespace: "connection"
slug: "intelligent-personnel-instructions"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 智能人事 > 参数说明"
doc_id: "UytdlxySFK"
updated_at: "2025-09-23 19:21:21"
---

> Source: https://open.dingtalk.com/document/connection/intelligent-personnel-instructions
> Path: 连接平台 / 连接器中心 / 官方连接器 > 智能人事 > 参数说明
> Updated: 2025-09-23 19:21:21

# 参数说明

# **触发事件**

## **人事档案变动**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| actionType | String | 触发事件的动作类型。 |
| EventType | String | 事件类型。 |
| staffId | String | 发生人事变更的员工的ID。 |

# **执行动作**

## **获取花名册元数据**

| **入参** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| agentid | Integer | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |

## **获取员工花名册字段信息**

| **入参** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| agentid | String | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| userid\_list | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，员工id列表。 |

## **获取花名册字段组详情**

| **入参** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| agentid | Integer | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |

## **更新员工花名册信息**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| agentid | String | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| param | Object | 是 | 编辑花名册入参。 |
| groups | Array | 否 | 花名册分组列表。 |
| group\_id | String | 否 | 分组ID。 |
| sections | Array | 否 | 分组明细列表。 |
| section | Array | 否 | 分组下字段列表。 |
| field\_code | String | 否 | 字段标识。 |
| value | String | 否 | 字段值。 |
| old\_index | Integer | 否 | 明细下标。    **[!NOTE]**  当传入该值时，表示当前传入的section为编辑员工花名册现有的第oldIndex条明细，此时系统会只编辑该条明细中传入的字段；当不传入该值时，表示传入的是新增明细，此时系统会保存该条明细传入的字段，未传字段会清空。 |
| userid | String | 否 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |

## **添加企业待入职员工**

| **入参** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| name | String | 是 | 待入职员工姓名。 |
| mobile | String | 是 | 待入职员工手机号。 |

## **获取待入职员工列表**

| **入参** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| offset | Integer | 是 | 偏移量。  **[!NOTE]**  默认0开始 |
| size | Integer | 是 | 分页大小。  **[!NOTE]**  最大50。 |

## **获取在职员工列表**

| **入参** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| offset | Integer | 是 | 偏移量。  **[!NOTE]**  默认0开始 |
| size | Integer | 是 | 分页大小。  **[!NOTE]**  最大50。 |
| status\_list | String | 是 | 在职员工状态。 |

## **获取离职员工列表**

| **入参** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| offset | Integer | 是 | 偏移量。  **[!NOTE]**  默认0开始 |
| size | Integer | 是 | 分页大小。  **[!NOTE]**  最大50。 |
| status\_list | String | 是 | 在职员工状态。 |

## **获取**员工**离职信息**

| **入参** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userid\_list | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |

## **修改员工最后一次离职信息**

| **入参** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| lastWorkDate | Long | 是 | 最后工作日。  **[!NOTE]**  即离职日期，格式为毫秒值时间戳。 |
| dismissionMemo | String | 是 | 离职备注信息。 |
| userId | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |
