---
title: "获取员工花名册字段信息"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-obtain-employee-roster-information"
namespace: "development"
slug: "intelligent-personnel-obtain-employee-roster-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 智能人事 > 花名册 > 获取员工花名册字段信息"
doc_id: "cML4vGTM12"
updated_at: "2025-09-08 19:05:07"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-obtain-employee-roster-information
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 智能人事 > 花名册 > 获取员工花名册字段信息
> Updated: 2025-09-08 19:05:07

# 获取员工花名册字段信息

调用本接口，查询员工花名册指定字段的信息，支持明细分组字段。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对智能人事-花名册接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档预计于 2024 年 6 月 22 日迁移至历史文档目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[获取员工花名册字段信息](https://open.dingtalk.com/document/orgapp/api-getemployeerosterbyfield)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

例如，张三个人档案如下图所示。调用本接口，可获取张三花名册指定字段的信息。

![iShot2021-12-17 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3319279361/p371353.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 智能人事个人信息读权限 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingtalk.oapi.smartwork.hrm.employee.v2.list) |
| 第三方企业应用 | 是 | 智能人事个人信息读权限 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=dingtalk.oapi.smartwork.hrm.employee.v2.list) |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/v2/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | af21xxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用，通过[获取第三方企业应用的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid\_list | String | 是 | user123,user456 | 员工的userid列表，多个userid之间使用逗号分隔，一次最多支持传100个值。 |
| field\_filter\_list | String | 否 | sys01-positionLevel,sys05-nowContractEndTime | 需要获取的花名册字段field\_code值列表，多个字段之间使用逗号分隔，一次最多支持传100个值。  **[!NOTE]**   - 该参数不传时，获取全部字段信息。 - 查询字段越少，RT越低，建议按需查询。   - 企业内部应用：    - 查看[花名册自定义字段业务code](https://open.dingtalk.com/document/orgapp/roster-custom-field-business-code)中field\_code字段。   - 调用[获取花名册元数据](https://open.dingtalk.com/document/orgapp/intelligent-personnel-roster-metadata-query)接口获取field\_code参数值。 - 第三方企业应用，调用[查询花名册中有权限的字段列表](https://open.dingtalk.com/document/isvapp/query-the-list-of-fields-with-permissions-in-the-roster)接口获取field\_code参数值。 |
| agentid | Number | 是 | 1 | 应用的AgentId。   - 企业内部应用，应用详情页获取[应用 AgentId](https://open.dingtalk.com/document/orgapp/basic-concepts-beta#813cbd7067yn0)。 - 第三方企业应用，通过[获取企业授权信息](https://open.dingtalk.com/document/isvapp/obtains-the-basic-information-of-an-enterprise)接口获取agentid参数值。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | EmpRosterFieldVo[] |  | 返回结果。 |
| corp\_id | String | ding20a11xxx | 企业的corpid。 |
| field\_data\_list | EmpFieldDataVo[] |  | 返回的字段信息列表。 |
| field\_name | String | 员工状态 | 字段名称。 |
| field\_code | String | sys01-employeeStatus | 字段标识。 |
| group\_id | String | sys01 | 分组标识。 |
| field\_value\_list | FieldValueVo[] |  | 字段值列表。   - 明细分组字段包含多条。 - 非明细分组仅一条记录。 |
| item\_index | Number | 0 | 第几条的明细标识，下标从0开始。 |
| label | String | 正式 | 字段展示值，选项类型字段对应选项的value。 |
| value | String | 3 | 字段取值，选项类型字段对应选项的key。 |
| userid | String | 042519 | 员工的userid。 |
| success | Boolean | true | 调用是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 8badquf9r90f | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/v2/list?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "agentid": 957064202,
    "userid_list": "user123,user456",
    "field_filter_list": "sys01-positionLevel,sys05-nowContractEndTime"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/v2/list");
OapiSmartworkHrmEmployeeV2ListRequest req = new OapiSmartworkHrmEmployeeV2ListRequest();
req.setUseridList("1,2,3");
req.setFieldFilterList("sys01-employeeStatus, sys01-regularTime");
req.setAgentid(1L);
OapiSmartworkHrmEmployeeV2ListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
     "errcode": 0,
     "errmsg": "ok",
     "result": [
          {
               "corp_id": "dinge8a5xxx",
               "field_data_list": [
                    {
                         "field_code": "sys01-positionLevel",
                         "field_name": "岗位职级",
                         "field_value_list": [
                              {
                                   "item_index": 0，
                                   "label":"本地城镇",
                                   "value":"1"
                              }
                         ],
                         "group_id": "sys01"
                    },
                    {
                         "field_code": "sys05-nowContractEndTime",
                         "field_name": "现合同到期日",
                         "field_value_list": [
                              {
                                   "item_index": 0，
                                   "label":"本地城镇",
                                   "value":"1"
                              }
                         ],
                         "group_id": "sys05"
                    }
               ],
               "userid": "user456"
          },
          {
               "corp_id": "dinge8a56xxx",
               "field_data_list": [
                    {
                         "field_code": "sys01-positionLevel",
                         "field_name": "岗位职级",
                         "field_value_list": [
                              {
                                   "item_index": 0，
                                   "label":"本地城镇",
                                   "value":"1"
                              }
                         ],
                         "group_id": "sys01"
                    },
                    {
                         "field_code": "sys05-nowContractEndTime",
                         "field_name": "现合同到期日",
                         "field_value_list": [
                              {
                                   "item_index": 0，
                                   "label":"本地城镇",
                                   "value":"1"
                              }
                         ],
                         "group_id": "sys05"
                    }
               ],
               "userid": "user123"
          }
     ],
     "success": true,
     "request_id": "7dw5ezodufiy"
}
```
