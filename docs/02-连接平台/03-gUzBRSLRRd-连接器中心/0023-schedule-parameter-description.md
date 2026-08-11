---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/schedule-parameter-description"
namespace: "connection"
slug: "schedule-parameter-description"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 日程 > 参数说明"
doc_id: "nbuZG1IxP5"
updated_at: "2025-09-23 19:20:50"
---

> Source: https://open.dingtalk.com/document/connection/schedule-parameter-description
> Path: 连接平台 / 连接器中心 / 官方连接器 > 日程 > 参数说明
> Updated: 2025-09-23 19:20:50

# 参数说明

# **触发事件**

## **日程变更**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| calendarEventId | String | 发生变更的日程ID。 |
| corpId | String | 日程组织者所属的主企业。 |
| unionIdList | Array of String | 本次日程变更影响的用户unionId列表。 |
| calendarId | String | 日历Id。 |
| changeType | String | 业务类型。 |
| eventTime | Long | 事件发生时间。 |
| eventType | String | 事件类型。 |

# **执行动作**

## **创建日程（userId版本）**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| summary | String | 是 | 日程标题。 |
| reminders | Array | 否 | 日程提醒，可以添加多个。   - 如果不传默认提醒时间为：    - **非全天日程**：开始前15分钟提醒   - **全天日程**：开始前一天9点提醒 - 如果传空数据表示不创建任何提醒。 |
| method | String | 否 | 提醒方式。   - **dingtalk**: 钉钉内提醒 |
| minutes | Integer | 否 | 在日程开始前N分钟发出提醒。 |
| corpId | String | 是 | 输入[组织ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| attendees | Array | 否 | 日程参与人列表，最多支持500个参与人。 |
| id | String | 否 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，用户的userid。 |
| start | Object | 是 | 日程开始时间。 |
| date | String | 否 | 日程开始日期，格式：yyyy-MM-dd。  **[!NOTE]**   - 全天日程必须有值。 - 非全天日程必须留空。 |
| dateTime | String | 否 | 日程开始时间，格式为ISO-8601的date-time格式。  **[!NOTE]**  全天日程必须有值。  非全天日程必须留空。 |
| timeZone | String | 否 | 日程开始时间所属时区，TZ database name格式。  **[!NOTE]**  全天日程必须有值。  非全天日程必须留空。 |
| description | String | 否 | 日程描述，最大不超过5000个字符。 |
| onlineMeetingInfo | Object | 否 | 创建日程同时创建线上会议。 |
| type | String | 否 | 线上会议类型。   - **dingtalk**: 钉钉视频会议 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，日程组织者的userid。 |
| recurrence | Object | 否 | 日程循环规则。 |
| pattern | Object | 否 | 循环规则。 |
| dayOfMonth | Integer | 否 | 当循环规则的**type**值为**absoluteMonthly**时，用于指定是每个月的第几天。 |
| index | String | 否 | 当**type**值为**relativeMonthly**时，用于指定每月第几周。   - **first**：第一周 - **second**：第二周 - **third**：第三周 - **fourth**：第四周 - **last**：最后一周 |
| interval | Integer | 否 | 循环间隔，根据type不同单位不同。  **[!NOTE]**   - 当type取值为daily时表示间隔N天。 - 当type取值为absoluteYearly则表示间隔N年。 |
| type | String | 否 | 循环规则类型。   - **daily**：每**interval**天重复 - **weekly**：每**interval**周的第**daysOfWeek**天重复 - **absoluteMonthly**：每**interval**月的第**dayOfMonth**天重复 - **relativeMonthly**：每**interval**月的第**index**周的第**daysOfWeek**天重复 - **absoluteYearly**：每**interval**年重复 |
| daysOfWeek | String | 否 | 英文小写单词指定星期几，如果有多个值逗号分割。 |
| range | Object | 否 | 循环范围。 |
| endDate | String | 否 | 循环结束时间。  **[!NOTE]**  endDate和numberOfOccurrences不可同时设定。 |
| numberOfOccurrences | Integer | 否 | 循环次数。  **[!NOTE]**  endDate和numberOfOccurrences不可同时设定。 |
| type | String | 否 | 循环范围类型。   - **noEnd**：永不结束 - **endDate**：循环至指定日期结束 - **numbered**：循环指定次数后结束 |
| isAllDay | Boolean | 否 | 是否全天日程。   - **true**：是 - **false**：不是 |
| calendarId | String | 是 | 日程所属的日历ID，统一为**primary**，表示用户的主日历。 |
| end | Object | 否 | 日程结束时间。 |
| date | String | 否 | 日程结束日期，格式：yyyy-MM-dd。  **[!NOTE]**  全天日程必须有值。  非全天日程必须留空。 |
| dateTime | String | 否 | 日程结束时间，格式为ISO-8601的date-time格式。  **[!NOTE]**  全天日程必须有值。  非全天日程必须留空。 |
| timeZone | String | 否 | 日程结束时间所属时区，必须和开始时间所属时区相同，TZ database name格式。  **[!NOTE]**  全天日程必须有值。  非全天日程必须留空。 |
| location | Object | 否 | 日程地点。 |
| displayName | String | 否 | 日程地点的名称。 |

## **修改日程（userId版本）**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| summary | String | 是 | 日程标题。 |
| reminders | Array | 否 | 日程提醒，可以添加多个。   - 如果不传默认提醒时间为：    - **非全天日程**：开始前15分钟提醒   - **全天日程**：开始前一天9点提醒 - 如果传空数据表示不创建任何提醒。 |
| method | String | 否 | 提醒方式。   - **dingtalk**: 钉钉内提醒 |
| minutes | Integer | 否 | 在日程开始前N分钟发出提醒。 |
| corpId | String | 是 | 输入[组织ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| attendees | Array | 否 | 日程参与人列表，最多支持500个参与人。 |
| id | String | 否 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，用户的userid。 |
| start | Object | 是 | 日程开始时间。 |
| date | String | 否 | 日程开始日期，格式：yyyy-MM-dd。  **[!NOTE]**   - 全天日程必须有值。 - 非全天日程必须留空。 |
| dateTime | String | 否 | 日程开始时间，格式为ISO-8601的date-time格式。  **[!NOTE]**  全天日程必须有值。  非全天日程必须留空。 |
| timeZone | String | 否 | 日程开始时间所属时区，TZ database name格式。  **[!NOTE]**  全天日程必须有值。  非全天日程必须留空。 |
| description | String | 否 | 日程描述，最大不超过5000个字符。 |
| onlineMeetingInfo | Object | 否 | 创建日程同时创建线上会议。 |
| type | String | 否 | 线上会议类型。   - **dingtalk**: 钉钉视频会议 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，日程组织者的userid。 |
| recurrence | Object | 否 | 日程循环规则。 |
| pattern | Object | 否 | 循环规则。 |
| dayOfMonth | Integer | 否 | 当循环规则的**type**值为**absoluteMonthly**时，用于指定是每个月的第几天。 |
| index | String | 否 | 当**type**值为**relativeMonthly**时，用于指定每月第几周。   - **first**：第一周 - **second**：第二周 - **third**：第三周 - **fourth**：第四周 - **last**：最后一周 |
| interval | Integer | 否 | 循环间隔，根据type不同单位不同。  **[!NOTE]**   - 当type取值为daily时表示间隔N天。 - 当type取值为absoluteYearly则表示间隔N年。 |
| type | String | 否 | 循环规则类型。   - **daily**：每**interval**天重复 - **weekly**：每**interval**周的第**daysOfWeek**天重复 - **absoluteMonthly**：每**interval**月的第**dayOfMonth**天重复 - **relativeMonthly**：每**interval**月的第**index**周的第**daysOfWeek**天重复 - **absoluteYearly**：每**interval**年重复 |
| daysOfWeek | String | 否 | 英文小写单词指定星期几，如果有多个值逗号分割。 |
| range | Object | 否 | 循环范围。 |
| endDate | String | 否 | 循环结束时间。  **[!NOTE]**  endDate和numberOfOccurrences不可同时设定。 |
| numberOfOccurrences | Integer | 否 | 循环次数。  **[!NOTE]**  endDate和numberOfOccurrences不可同时设定。 |
| type | String | 否 | 循环范围类型。   - **noEnd**：永不结束 - **endDate**：循环至指定日期结束 - **numbered**：循环指定次数后结束 |
| isAllDay | Boolean | 否 | 是否全天日程。   - **true**：是 - **false**：不是 |
| calendarId | String | 是 | 日程所属的日历ID，统一为**primary**，表示用户的主日历。 |
| end | Object | 否 | 日程结束时间。 |
| date | String | 否 | 日程结束日期，格式：yyyy-MM-dd。  **[!NOTE]**  全天日程必须有值。  非全天日程必须留空。 |
| dateTime | String | 否 | 日程结束时间，格式为ISO-8601的date-time格式。  **[!NOTE]**  全天日程必须有值。  非全天日程必须留空。 |
| timeZone | String | 否 | 日程结束时间所属时区，必须和开始时间所属时区相同，TZ database name格式。  **[!NOTE]**  全天日程必须有值。  非全天日程必须留空。 |
| location | Object | 否 | 日程地点。 |
| displayName | String | 否 | 日程地点的名称。 |
| id | String | 是 | 日程ID。 |

## **删除日程（userId版本）**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| eventId | String | 是 | 日程ID。 |
| calendarId | String | 是 | 日程所属的日历ID，统一为**primary**，表示用户的主日历。 |
| corpId | String | 是 | 输入[组织ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，日程组织者的userid。 |

## **查询日历本（userId版本）**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| corpId | String | 是 | 输入[组织ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，查询目标的userid。 |

## **添加日程参与者（userId版本）**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| eventId | String | 是 | 日程ID。 |
| corpId | String | 是 | 输入[组织ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| attendeesToAdd | Array of Object | 否 | 日程参与人列表，最多支持500个参与人。 |
| id | String | 否 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，用户的userid。 |
| userId | String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，日程组织者的userid。 |
| calendarId | String | 是 | 日程所属的日历ID，统一为**primary**，表示用户的主日历。 |
