---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/announcement-parameter-description"
namespace: "connection"
slug: "announcement-parameter-description"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 公告 > 参数说明"
doc_id: "TERqYhwKXN"
updated_at: "2025-09-23 19:20:52"
---

> Source: https://open.dingtalk.com/document/connection/announcement-parameter-description
> Path: 连接平台 / 连接器中心 / 官方连接器 > 公告 > 参数说明
> Updated: 2025-09-23 19:20:52

# 参数说明

## **执行动作**

## **创建企业公告**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| push\_top | Boolean | 否 | 公告是否置顶：   - true：置顶 - false：不置顶 |
| operation\_userid | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，操作人的userId。 |
| ding | Boolean | 否 | 是否发送应用内钉提醒：   - true：发送 - false：不发送 |
| downloadable | Boolean | 否 | 附件是否允许下载：   - true：允许，默认值 - false：不允许 |
| attachments | Array | 否 | 附件信息。 |
| spaceId | String | 否 | 钉盘空间id，可通过调用[获取公告钉盘空间信息](https://open-dev.dingtalk.com/fe/connector#/market/connector/G-CONN-101886C44A9A213DF5B1000Q/action/view/G-ACT-102469A45EBD213CCBB8001F?orgId=&corpId=ding32fff839a3e0105d)执行动作，获取返回参数`spaceId`字段值。 |
| size | String | 否 | 文件大小。 |
| name | String | 否 | 文件名。 |
| fileType | String | 否 | 文件类型。 |
| fileId | String | 否 | 钉盘文件id。 |
| category\_id | String | 否 | 公告分类id，可通过调用[获取公告分类列表](https://open-dev.dingtalk.com/fe/connector#/market/connector/G-CONN-101886C44A9A213DF5B1000Q/action/view/G-ACT-1024697E9E1321075B75001Y?orgId=&corpId=ding32fff839a3e0105d)执行动作，获取返回参数`id`字段。 |
| author | String | 否 | 公告作者。 |
| private\_level | String | 否 | 保密等级。 |
| coverpic\_mediaid | String | 否 | 封面图，可以通过调用[上传媒体文件](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)执行动作，获取`mediaId`参数值。 |
| blackboard\_receiver | Object | 是 | 接收信息。 |
| deptid\_list | Array of Long | 否 | 接收部门id。 |
| userid\_list | Array of String | 否 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，接收用户的userid列表。 |
| title | String | 是 | 公告标题。 |
| content | String | 是 | 公告内容。 |

## 更新公告

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| ding | Boolean | 否 | 是否发送应用内钉提醒：   - true：发送 - false：不发送 |
| operation\_userid | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，操作人的userId。 |
| category\_id | String | 否 | 公告分类id，可通过调用[获取公告分类列表](https://open-dev.dingtalk.com/fe/connector#/market/connector/G-CONN-101886C44A9A213DF5B1000Q/action/view/G-ACT-1024697E9E1321075B75001Y?orgId=&corpId=ding32fff839a3e0105d)执行动作，获取返回参数`id`字段。 |
| author | String | 否 | 公告作者。 |
| blackboard\_id | String | 是 | 公告id，可通过调用[获取公告ID列表](https://open-dev.dingtalk.com/fe/connector#/market/connector/G-CONN-101886C44A9A213DF5B1000Q/action/view/G-ACT-1024698E4159213DC488001Y?orgId=&corpId=ding32fff839a3e0105d)执行动作获取。 |
| coverpic\_mediaid | String | 否 | 封面图，可以通过调用[上传媒体文件](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)执行动作，获取`mediaId`参数值。 |
| title | String | 是 | 公告标题。 |
| content | String | 是 | 公告内容。 |
| notify | Boolean | 否 | 修改后是否再次通知接收人：   - true：发送 - false：不发送 |

## **删除公告**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| operation\_userid | String | 否 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，操作人的userId。 |
| blackboard\_id | String | 是 | 公告id，可通过调用[获取公告ID列表](https://open-dev.dingtalk.com/fe/connector#/market/connector/G-CONN-101886C44A9A213DF5B1000Q/action/view/G-ACT-1024698E4159213DC488001Y?orgId=&corpId=ding32fff839a3e0105d)执行动作，获取返回参数`id`字段。 |

## **获取公告详情**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| operation\_userid | String | 否 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，操作人的userId。 |
| blackboard\_id | String | 是 | 公告id，可通过调用[获取公告ID列表](https://open-dev.dingtalk.com/fe/connector#/market/connector/G-CONN-101886C44A9A213DF5B1000Q/action/view/G-ACT-1024698E4159213DC488001Y?orgId=&corpId=ding32fff839a3e0105d)执行动作获取。 |

## **获取公告ID列表**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| operation\_userid | String | 否 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，操作人的userId。 |
| start\_time | String | 否 | 开始时间（闭区间）：   - 如果只传**start\_time**，**start\_time**距当前时间不能超过180天。 - 如果传**start\_time**和**end\_time**，时间间隔不能超过180天。 - 如果不传**start\_time**和**end\_time**，默认获取近一个月内的公告信息。 |
| category\_id | String | 否 | 公告分类id，可通过调用[获取公告分类列表](https://open-dev.dingtalk.com/fe/connector#/market/connector/G-CONN-101886C44A9A213DF5B1000Q/action/view/G-ACT-1024697E9E1321075B75001Y?orgId=&corpId=ding32fff839a3e0105d)执行动作，获取返回参数`id`字段。 |
| end\_time | String | 否 | 结束时间（开区间）：   - 如果只传**start\_time**，**start\_time**距当前时间不能超过180天。 - 如果传**start\_time**和**end\_time**，时间间隔不能超过180天。 - 如果不传**start\_time**和**end\_time**，默认获取近一个月内的公告信息。 |
| page | Integer | 是 | 页码。  **[!NOTE]**  从1开始且必须为正整数。 |
| page\_size | Integer | 是 | 分页大小。  **[!NOTE]**  必须为正整数，且不超过30。 |

## **获取公告分类列表**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| operation\_userid | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，操作人的userId。 |

## **获取用户可查看的公告**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userid | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，被查询用户的userId。 |

## **获取公告钉盘空间信息**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| operationUserId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，操作人的userId。 |
