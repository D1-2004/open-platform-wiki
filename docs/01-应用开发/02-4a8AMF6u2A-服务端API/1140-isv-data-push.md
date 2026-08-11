---
title: "课堂数据推送"
source_url: "https://open.dingtalk.com/document/development/isv-data-push"
namespace: "development"
slug: "isv-data-push"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 在线课堂 > 课堂数据推送"
doc_id: "DWkSu4HYeL"
updated_at: "2025-09-23 19:22:59"
---

> Source: https://open.dingtalk.com/document/development/isv-data-push
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 在线课堂 > 课堂数据推送
> Updated: 2025-09-23 19:22:59

# 课堂数据推送

本文主要介绍第三方应用服务商在线课堂数据事件的数据推送格式。

## RDS数据推送

| 数据类型 | 数据类别 | 数据因子 |
| --- | --- | --- |
| 课堂概要数据 | 课堂基础数据（BASIC\_INFO） | 进入课堂时间（joinClassroomTime） |
| 退出课堂时间（leaveClassroomTime） |

在使用前，需要先申请“排课授课接口权限”，然后在开发管理中，推送回调事件勾选“教育课程数据”选项。

![回调事件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0944173061/p176632.png)当 biz\_type = 62，对应的数据为课堂数据。

| 字段 | 说明 |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 套件所属企业的corpid。 |
| biz\_id | 业务ID。 |
| biz\_data | 推送的业务数据，格式为JSON。 |
| └ type | 数据类型：   - **1**：表示课堂的概要数据 - **2**：表示课堂明细数据 |
| └ data | 推送的具体数据。 |

- type=1时，biz\_data数据格式如下。

  | type | Number | 1 | 数据类型。  1表示课堂的概要数据。 |
  | --- | --- | --- | --- |
  | data | Json |  | 数据。 |
  | └ category\_code | String | BASIC\_INFO | 数据类别编码。 |
  | └ category\_biz\_key | String | 1\_6d20b8ae-edd3-4ac8-b8d0-70be7837b4b4 | 数据类别业务唯一键。 |
  | └ data | Json | {"classroomMemberCount":2,"classroomEndTime":1600696867000,"classroomStartTime":1600696128000,"classroomMessageCount":2} | 数据：  - **key**：数据因子编码 - **value**： 对应的数据 |
  | └ course\_code | String | GJKI49001 | 课堂编码。 |

  数据示例：

  ```
  {
    "data":"{
      "categoryBizKey":"1_6d20b8ae-edd3-4ac8-b8d0-70be7837b4b4",
      "categoryCode":"BASIC_INFO,
      "courseCode":"GJKI49001",
      "data":{
          "classroomMemberCount":2,
          "classroomEndTime":1600696867000,
          "classroomStartTime":1600696128000,
          "classroomMessageCount":2
        }
    }",
    "type":1
  }
  ```
- type=2时，biz\_data数据格式如下。

  | type | Number | 2 | 数据类型。  2表示课堂明细数据。 |
  | --- | --- | --- | --- |
  | data | Json |  | 数据。 |
  | └ user\_cropid | String | ding4220d8e5128d0edd | 用户组织ID。 |
  | └ userid | String | user01 | 用户的userid。 |
  | └ category\_code | String | BASIC\_INFO | 数据类别编码。 |
  | └ category\_biz\_key | String | b3540b13-60bf-4xxx | 数据业务唯一键，例如标识具体哪一次进入教室。 |
  | └ value | String | 1600741723451 | 数据值，例如进入教室的时间戳。 |
  | └ course\_code | String | GJKI49001 | 课堂编码。 |
  | └ factor\_code | String | joinClassroomTime | 数据因子编码。 |

  数据示例：

  ```
  {
    "data":"{
      "categoryBizKey":"b3540b13-60bf-4375-bfe5-633bbe5adef3_JOIN_1600741723451",
      "categoryCode""BASIC_INFO",
      "courseCode":"GJKI49001",
      "factorCode":"joinClassroomTime",
      "userCropId":"ding4220d8e5128d0edd",
      "userId":"user01",
      "value":"1600741723451"
    }",
    "type":2
  }
  ```
