---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/official-connector-parameter-description"
namespace: "connection"
slug: "official-connector-parameter-description"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 考勤 > 参数说明"
doc_id: "8u32plHzxe"
updated_at: "2025-12-08 17:45:37"
---

> Source: https://open.dingtalk.com/document/connection/official-connector-parameter-description
> Path: 连接平台 / 连接器中心 / 官方连接器 > 考勤 > 参数说明
> Updated: 2025-12-08 17:45:37

# 参数说明

# **触发事件**

## **员工打卡事件**

> **[!NOTE]**
>
> 配置员工打卡事件前，必须接入[配置 Stream 推送（推荐）](../../01-应用开发/04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md#151be9e66238j)，并且**开启**员工打卡事件。否则**员工打卡触发事件**无法正常获取员工打卡数据。
>
> ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1541370571/p976682.png)

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| DataList | Array | 打卡列表。 |
| address | String | 打卡位置。 |
| checkTime | Double | 打卡时间。 |
| corpId | String | 企业corpId。 |
| groupId | String | 考勤组的groupId。 |
| latitude | Double | 纬度信息。 |
| bizId | String | 关联的业务ID。 |
| locationMethod | String | 打卡方式：   - MAP：定位打卡 - WIFI：wifi打卡 - ATM：考勤机打卡或考勤机蓝牙打卡 |
| userId | String | 员工的userId。 |
| deviceSN | String | 考勤机SN。  **[!NOTE]**  当打卡方式为考勤机打卡时返回此字段。 |
| longitude | Double | 经度信息。 |
| EventType | String | 事件类型。 |

## **员工排班变更事件**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| DataList | Array | 员工排班变更列表。 |
| workDateEnd | Double | 排班结束时间。 |
| corpId | String | 企业corpId。 |
| userIds | Array of String | 员工的userIds列表。 |
| type | String | 变更类型：   - modify：修改排班 - delete：删除排班 |
| workDateBegin | Double | 排班开始时间。 |
| EventType | String | 事件类型。 |

## **员工加班事件**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| DataList | Array | 打卡列表。 |
| overtimeDay | Double | 打卡位置。 |
| workDate | Double | 打卡时间。 |
| corpId | String | 企业corpId。 |
| overtimeHour | Double | 纬度信息。 |
| userid | String | 员工的userid。 |
| EventType | String | 事件类型。 |

# **执行动作**

## **创建考勤组**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| top\_group | Object | 是 | 考勤组信息。 |
| type | String | 是 | 考勤组类型：   - FIXED：固定班制考勤组 - TURN：排班制考勤组 - NONE：自由工时考勤组 |
| members | Array | 是 | 考勤组成员设置信息。 |
| role | String | 是 | 角色，固定值`Attendance`。 |
| user\_id | String | 是 | 钉钉用户ID。 |
| type | String | 是 | 类型，固定值`StaffMember`。 |
| name | String | 是 | 考勤组名。 |

## **更新考勤组**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| top\_group | Object | 是 | 考勤组信息。 |
| id | Integer | 是 | 考勤组ID。 |

## **删除考勤组**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| group\_key | String | 是 | 考勤组groupKey。 |

## **获取考勤组详情**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| group\_id | Integer | 是 | 考勤组ID。 |

## **批量获取考勤组详情**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| offset | Integer | 是 | 偏移位置。  **[!NOTE]**  与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始，下次调用传上次调用时的size与offset之和。 |
| size | Integer | 是 | 分页大小。 |

## **搜索考勤组摘要**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| group\_name | String | 是 | 考勤组名称。 |

## **获取参与考勤人员**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| group\_id | Integer | 是 | 考勤组ID。 |
| cursor | Integer | 是 | 游标值。  **[!NOTE]**  表示从第几个开始，不传默认从第1个开始。 |

## **校验用户是否在当前考勤组**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| member\_type | Integer | 是 | 成员类型：   - 0：员工 - 1：部门 |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| group\_id | Integer | 是 | 考勤组ID。 |
| member\_ids | String | 是 | 成员ids。  示例：user123,user456。  **[!NOTE]**  可以是钉钉用户ID或者部门ID，多个ID之间使用英文逗号分割，每次调用最多支持传20个元素值。 |

## **根据groupKey查询考勤组信息**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| group\_key | String | 是 | 考勤组groupKey。 |

## **groupId转换为groupKey**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| group\_id | Integer | 是 | 考勤组ID。 |

## **groupKey转换为groupId**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| group\_key | String | 是 | 考勤组groupKey。 |

## **批量新增参与考勤人员**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| user\_id\_list | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，新增考勤人员用户ID。  示例：user01,user02。  **[!NOTE]**  每次调用最多传100个。 |
| op\_userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| group\_key | String | 是 | 考勤组groupKey。 |

## **批量删除参与考勤人员**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| user\_id\_list | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，删除考勤人员用户ID。  示例：user01,user02。  **[!NOTE]**  每次调用最多传100个。 |
| op\_userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| group\_key | String | 是 | 考勤组groupKey。 |

## **创建/修改班次**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| shift | Object | 是 | 班次。 |
| name | String | 是 | 班次名称。 |
| sections | Array | 是 | 卡段。 |
| times | Array | 是 | 打卡信息。 |
| across | Integer | 是 | 是否跨天。 |
| check\_type | String | 是 | 打卡类型：   - OnDuty：上班 - OffDuty：下班 |
| check\_time | String | 是 | 打卡时间。 |

## **删除班次**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| shift\_id | Integer | 是 | 班次ID。 |

## **获取班次详情**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| shift\_id | Integer | 是 | 班次ID。 |

## **按名称搜索班次**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| shift\_name | String | 是 | 班次名称。 |

## **获取班次摘要信息**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| cursor | Integer | 是 | 游标位置。  **[!NOTE]**  起始值为0。 |

## **排班制考勤组排班**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| group\_id | Integer | 是 | 考勤组ID。 |
| schedules | Array | 是 | 排班详情。 |
| work\_date | Double | 是 | 排班日期。 |
| shift\_id | Integer | 是 | 班次ID。  **[!NOTE]**  休息班次传1。 |
| userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |

## **查询排班打卡结果**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_user\_id | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者钉钉用户ID。 |
| schedule\_ids | String | 是 | 排班ID。  **[!NOTE]**  多个排班ID之间用英文逗号分割，每次调用最多支持100个排班ID |

## **查询企业考勤排班详情**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| workDate | String | 是 | 排班日期。  示例：2020-09-06。 |

## **上传打卡记录**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| device\_name | String | 是 | 考勤机名称。 |
| device\_id | String | 是 | 考勤机ID。 |
| user\_check\_time | Long | 是 | 员工打卡的时间。 |
| userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |

## **获取打卡结果**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| workDateFrom | String | 是 | 起始时间。  示例：2020-11-07 08:00:00。 |
| offset | Integer | 是 | 偏移量。  **[!NOTE]**  表示获取考勤数据的起始点。第一次传0，如果还有多余数据，下次获取传的offset值为之前的offset+limit，0、1、2...依次递增。 |
| userIdList | Array of String | 是 | 要查询的钉钉用户ID列表。  **[!NOTE]**  单次最多50个。 |
| limit | Integer | 是 | 单次获取条数。  **[!NOTE]**  单次最多50条。 |
| workDateTo | String | 是 | 结束时间。  示例：2020-11-07 18:00:00。 |

## **获取打卡详情**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| checkDateFrom | String | 是 | 考勤机名称。 |
| userIds | Array of String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。  **[!NOTE]**  最多不能超过50个。 |
| checkDateTo | String | 是 | 结束时间。  示例：2020-09-08 00:00:00  **[!NOTE]**  起始与结束工作日最多相隔7天。 |

## **添加假期规则**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| leave\_view\_unit | String | 是 | 可以按照天半天或者小时请假：   - day：天 - halfDay：半天 - hour：小时 |
| leave\_name | String | 是 | 假期名称。 |
| biz\_type | String | 是 | 类型：   - general\_leave：普通假期 - lieu\_leave：加班转调休假期 |
| op\_userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |
| natural\_day\_leave | Boolean | 是 | 是否按照自然日统计请假时长。  **[!NOTE]**  当为false的时候，用户发起请假时候会根据用户在请假时间段内的排班情况来计算请假时长。 |
| hours\_in\_per\_day | Integer | 是 | 每天折算的工作时长。  **[!NOTE]**  百分之一，例如1天=10小时=1000 |

## **更新假期规则**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |
| leave\_code | String | 是 | 假期类型唯一标识。 |

## **删除假期规则**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |
| leave\_code | String | 是 | 假期类型唯一标识。 |

## **查询假期规则列表**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |
| vacation\_source | String | 是 | 假期来源。取值：   - "all"：获取的是所有假期类型 - ""：获取的是调用添加假期规则接口新建的假期。 |

## **初始化假期余额**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |
| leave\_quotas | Array of Object | 是 | 待初始化的假期余额记录。 |
| start\_time | Long | 是 | 额度有效期开始时间戳。 |
| end\_time | Long | 是 | 额度有效期结束时间戳。 |
| leave\_code | String | 是 | 假期类型唯一标识。 |
| userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |

## **批量更新假期余额**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| op\_userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |
| leave\_quotas | Array of Object | 是 | 待初始化的假期余额记录。 |
| leave\_code | String | 是 | 假期类型唯一标识。 |
| userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |

## **查询假期余额**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| offset | Integer | 是 | 分页偏移。 |
| size | Integer | 是 | 分页条数。 |
| userids | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，要查询的钉钉用户ID列表。 |
| leave\_code | String | 是 | 假期类型唯一标识。 |
| op\_userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，操作者的钉钉用户ID。 |

## **查询是否启用智能统计报表**

无入参

## **获取考勤报表列定义**

无入参

## **获取考勤报表列值**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| column\_id\_list | String | 是 | 报表列ID列表。  **[!NOTE]**  多值用英文逗号分隔，最大长度20。 |
| from\_date | String | 是 | 开始时间。  示例：2018-07-11 12:12:12。 |
| to\_date | String | 是 | 结束时间。  示例：2018-07-13 12:12:12。  **[!NOTE]**  结束时间减去开始时间必须在31天以内。 |
| userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |

## **获取报表假期数据**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| leave\_names | String | 是 | 假期名称。  示例：年假。  **[!NOTE]**  多个用英文逗号分隔。最大长度20。 |
| from\_date | String | 是 | 开始时间。  示例：2018-07-11 12:12:12。 |
| to\_date | String | 是 | 结束时间。  示例：2018-07-13 12:12:12。  **[!NOTE]**  结束时间减去开始时间必须在31天以内。 |
| userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |

## **获取用户考勤数据**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| work\_date | String | 是 | 查询日期。  示例：2021-01-14 09:00:00。 |
| userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |

## **查询员工智能考勤机列表**

| 入参 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| param | Object | 是 | 请求参数。 |
| offset | Integer | 是 | 偏移值。  **[!NOTE]**  分页游标，从0开始的非负整数。 |
| size | Integer | 是 | 每页大小。  **[!NOTE]**  每页大小，最大50。 |
| userid | String | 是 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，钉钉用户ID。 |
