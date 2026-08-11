---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/robot-overview"
namespace: "connection"
slug: "robot-overview"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 通讯录 > 参数说明"
doc_id: "CaGGgPJkNG"
updated_at: "2025-09-23 19:21:02"
---

> Source: https://open.dingtalk.com/document/connection/robot-overview
> Path: 连接平台 / 连接器中心 / 官方连接器 > 通讯录 > 参数说明
> Updated: 2025-09-23 19:21:02

# 参数说明

## **触发事件**

## **企业删除**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| corpId | String | 被删除企业的CorpId。 |
| syncAction | String | 事件类型。 |

## **企业信息变更**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| corpId | String | 企业CorpId。 |
| syncAction | String | 事件类型。 |
| corpLogoUrl | String | 企业logo地址。 |
| industry | String | 行业信息。 |
| corpName | String | 企业名称。 |
| isAuthenticated | Boolean | 企业是否认证：   - true 已认证 - false 未认证 |
| authLevel | Integer | 企业认证级别：   - 0：未认证 - 1： 高级认证 - 2： 中级认证 - 3 ：初级认证 |

## **创建角色**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| corpId | String | 企业CorpId。 |
| syncAction | String | 事件类型。 |
| groupName | String | 角色组名称。 |
| roleId | Long | 角色ID。 |
| groupId | Long | 角色组ID。 |
| roleName | String | 角色名称。 |

## **修改角色**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| corpId | String | 企业CorpId。 |
| syncAction | String | 事件类型。 |
| groupName | String | 角色组名称。 |
| roleId | Long | 角色ID。 |
| groupId | Long | 角色组ID。 |
| roleName | String | 角色名称。 |

## **删除角色**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| corpId | String | 企业CorpId。 |
| syncAction | String | 事件类型。 |
| groupName | String | 角色组名称。 |
| roleId | Long | 角色ID。 |
| groupId | Long | 角色组ID。 |
| roleName | String | 角色名称。 |

## **创建部门**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| corpId | String | 企业CorpId。 |
| syncAction | String | 事件类型。 |
| userPermits | String | 用户的权限。 |
| orgDeptOwner | String | 企业群群主userId。 |
| outerDept | Boolean | 是否为仅自己可见部门：   - true：是 - false ：否 |
| deptManagerUseridList | String | 部门管理员列表。 |
| parentid | Long | 父部门ID。 |
| groupContainSubDept | Boolean | 部门群是否包含子部门。 |
| outerPermitUsers | String | 仅自己可见部门的用户列表。 |
| outerPermitDepts | String | 配置的部门员工可见部门Id列表。 |
| deptPerimits | String | 配置可见userId列表。 |
| createDeptGroup | Boolean | 是否同步创建一个关联此部门的企业群：   - true：创建 - false：不创建 |
| name | String | 部门名称。 |
| id | Long | 部门id。 |
| autoAddUser | Boolean | 当部门群已经创建后，是否有新人加入部门会自动加入该群：   - true：自动加入群 - false：不会自动加入群 |
| deptHiding | Boolean | 部门权限是否开启。 |
| order | Long | 在父部门中的次序值。 |

## **修改部门**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| corpId | String | 企业CorpId。 |
| syncAction | String | 事件类型。 |
| userPermits | String | 用户的权限。 |
| orgDeptOwner | String | 企业群群主userId。 |
| outerDept | Boolean | 是否为仅自己可见部门：   - true：是 - false ：否 |
| deptManagerUseridList | String | 部门管理员列表。 |
| parentid | Long | 父部门ID。 |
| groupContainSubDept | Boolean | 部门群是否包含子部门。 |
| outerPermitUsers | String | 仅自己可见部门的用户列表。 |
| outerPermitDepts | String | 配置的部门员工可见部门Id列表。 |
| deptPerimits | String | 配置可见userId列表。 |
| createDeptGroup | Boolean | 是否同步创建一个关联此部门的企业群：   - true：创建 - false：不创建 |
| name | String | 部门名称。 |
| id | Long | 部门ID。 |
| autoAddUser | Boolean | 当部门群已经创建后，是否有新人加入部门会自动加入该群：   - true：自动加入群 - false：不会自动加入群 |
| deptHiding | Boolean | 部门权限是否开启。 |
| order | Long | 在父部门中的次序值。 |

## **删除部门**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| corpId | String | 企业组织的CorpId。 |
| syncAction | String | 事件类型。 |
| id | Long | 部门ID。 |

## **企业员工激活**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| unionid | String | 用户unionId。 |
| corpId | String | 企业CorpId。 |
| syncAction | String | 事件类型。 |
| orderInDepts | String | 部门列表。 |
| openId | String | 该字段为废弃字段。 |
| roles | Array | 角色列表。 |
| groupName | String | 角色组名称。 |
| name | String | 角色名称。 |
| id | Long | 角色ID。 |
| type | Integer | 角色类型。 |
| mobile | String | 手机号。 |
| active | Boolean | 是否激活： |
| avatar | String | 头像URL。 |
| isAdmin | Boolean | 是否为管理员：   - true：是 - false：否 |
| userid | String | 用户ID。 |
| isCustomizedPortal | Boolean | 是否为自定义入口：   - true：是 - false：否 |
| isHide | Boolean | 是否号码隐藏：   - true：隐藏 - false：不隐藏 |
| isLeaderInDepts | String | 是否为部门领导：   - true：是 - false：否 |
| jobnumber | String | 工号。 |
| isBoss | Boolean | 是否为老板：   - true：是 - false：否 |
| isSenior | Boolean | 是否开启高管：   - true：是 - false：否 |
| name | String | 姓名。 |
| stateCode | String | 电话区号。 |
| position | String | 职位名称。 |
| department | Array of Long | 成员所属部门ID列表。 |
| email | String | 邮箱地址。 |

## **企业员工角色变更**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| unionid | String | 用户unionId。 |
| corpId | String | 企业CorpId。 |
| syncAction | String | 事件类型。 |
| orderInDepts | String | 部门列表。 |
| openId | String | 该字段为废弃字段。 |
| roles | Array | 角色列表。 |
| groupName | String | 角色组名称。 |
| name | String | 角色名称。 |
| id | Long | 角色ID。 |
| type | Integer | 角色类型。 |
| mobile | String | 手机号。 |
| active | Boolean | 是否激活： |
| avatar | String | 头像URL。 |
| isAdmin | Boolean | 是否为管理员：   - true：是 - false：否 |
| userid | String | 用户ID。 |
| isCustomizedPortal | Boolean | 是否为自定义入口：   - true：是 - false：否 |
| isHide | Boolean | 是否号码隐藏：   - true：隐藏 - false：不隐藏 |
| isLeaderInDepts | String | 是否为部门领导：   - true：是 - false：否 |
| jobnumber | String | 工号。 |
| isBoss | Boolean | 是否为老板：   - true：是 - false：否 |
| isSenior | Boolean | 是否开启高管：   - true：是 - false：否 |
| name | String | 姓名。 |
| stateCode | String | 电话区号。 |
| position | String | 职位名称。 |
| department | Array of Long | 成员所属部门ID列表。 |
| email | String | 邮箱地址。 |

## **企业员工部门变更**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| unionid | String | 用户unionId。 |
| corpId | String | 企业CorpId。 |
| syncAction | String | 事件类型。 |
| orderInDepts | String | 部门列表。 |
| openId | String | 该字段为废弃字段。 |
| roles | Array | 角色列表。 |
| groupName | String | 角色组名称。 |
| name | String | 角色名称。 |
| id | Long | 角色ID。 |
| type | Integer | 角色类型。 |
| mobile | String | 手机号。 |
| active | Boolean | 是否激活： |
| avatar | String | 头像URL。 |
| isAdmin | Boolean | 是否为管理员：   - true：是 - false：否 |
| userid | String | 用户ID。 |
| isCustomizedPortal | Boolean | 是否为自定义入口：   - true：是 - false：否 |
| isHide | Boolean | 是否号码隐藏：   - true：隐藏 - false：不隐藏 |
| isLeaderInDepts | String | 是否为部门领导：   - true：是 - false：否 |
| jobnumber | String | 工号。 |
| isBoss | Boolean | 是否为老板：   - true：是 - false：否 |
| isSenior | Boolean | 是否开启高管：   - true：是 - false：否 |
| name | String | 姓名。 |
| stateCode | String | 电话区号。 |
| position | String | 职位名称。 |
| department | Array of Long | 成员所属部门ID列表。 |
| email | String | 邮箱地址。 |

## **企业内部用户变更**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| unionid | String | 用户unionId。 |
| corpId | String | 企业CorpId。 |
| syncAction | String | 事件类型。 |
| orderInDepts | String | 部门列表。 |
| dingId | String | 该字段为废弃字段。 |
| roles | Array | 角色列表。 |
| groupName | String | 角色组名称。 |
| name | String | 角色名称。 |
| id | Long | 角色ID。 |
| type | Integer | 角色类型。 |
| mobile | String | 手机号。 |
| active | Boolean | 是否激活： |
| avatar | String | 头像URL。 |
| isAdmin | Boolean | 是否为管理员：   - true：是 - false：否 |
| userid | String | 用户ID。 |
| isHide | Boolean | 是否号码隐藏：   - true：隐藏 - false：不隐藏 |
| isLeaderInDepts | String | 是否为部门领导：   - true：是 - false：否 |
| jobnumber | String | 工号。 |
| isBoss | Boolean | 是否为老板：   - true：是 - false：否 |
| isSenior | Boolean | 是否开启高管：   - true：是 - false：否 |
| name | String | 姓名。 |
| stateCode | String | 电话区号。 |
| position | String | 职位名称。 |
| department | Array of Long | 成员所属部门ID列表。 |
| email | String | 邮箱地址。 |

## **通讯录用户增加**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| unionid | String | 用户unionId。 |
| corpId | String | 企业CorpId。 |
| syncAction | String | 事件类型。 |
| orderInDepts | String | 部门列表。 |
| dingId | String | 该字段为废弃字段。 |
| roles | Array | 角色列表。 |
| groupName | String | 角色组名称。 |
| name | String | 角色名称。 |
| id | Long | 角色ID。 |
| type | Integer | 角色类型。 |
| mobile | String | 手机号。 |
| active | Boolean | 是否激活： |
| avatar | String | 头像URL。 |
| isAdmin | Boolean | 是否为管理员：   - true：是 - false：否 |
| userid | String | 用户ID。 |
| isHide | Boolean | 是否号码隐藏：   - true：隐藏 - false：不隐藏 |
| isLeaderInDepts | String | 是否为部门领导：   - true：是 - false：否 |
| jobnumber | String | 工号。 |
| isBoss | Boolean | 是否为老板：   - true：是 - false：否 |
| isSenior | Boolean | 是否开启高管：   - true：是 - false：否 |
| name | String | 姓名。 |
| stateCode | String | 电话区号。 |
| position | String | 职位名称。 |
| department | Array of Long | 成员所属部门ID列表。 |
| email | String | 邮箱地址。 |

## **通讯录用户离职**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| userid | String | 用户unionId。 |
| syncAction | String | 事件类型。 |
| dingId | String | 该字段为废弃字段。 |

## 创建用户

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| dept\_id\_list | String | 是 | 所属[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)列表。 |
| mobile | String | 是 | 手机号码。  **[!NOTE]**  企业内必须唯一。 |
| name | String | 是 | 员工名称，长度最大80个字符。 |

## 更新用户

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userid | String | 是 | 待更新[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |

## 删除用户

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userid | String | 是 | 待删除[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |

## 查询用户详情

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userid | String | 是 | 待查询[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |

## 获取管理员列表

无入参。

## 获取未登录钉钉的员工列表

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| is\_active | String | 是 | 待查询[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| offset | Integer | 是 | 获取数据偏移量，第一页使用0，后面页使用接口返回的`nextCursor`。 |
| size | Integer | 是 | 分页大小，最大值100。 |
| query\_date | String | 是 | 查询日期，日期格式yyyyMMdd。 |

## 根据userid获取用户unionid

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userid | String | 是 | 待查询[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |

## 根据unionid获取用户userid

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| unionid | String | 是 | 待查询用户unionId。 |

## 创建角色

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| groupId | Long | 是 | 角色组ID。 |
| roleName | String | 是 | 角色名称。 |

## 更新角色

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| roleId | Long | 是 | 待更新角色ID。 |
| roleName | String | 是 | 角色名称。 |

## 删除角色

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| roleId | Long | 是 | 待删除角色ID。 |

## 获取角色详情

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| roleId | Long | 是 | 待查询角色ID。 |

## 获取角色列表

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| size | Integer | 是 | 分页大小。 |
| offset | Integer | 是 | 分页偏移。 |

## 获取角色组列表

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| group\_id | Long | 是 | 角色组ID。 |

## 批量增加员工角色

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| roleIds | String | 是 | 角色ID列表。 |
| userIds | String | 是 | 待添加[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)列表。 |

## 设定角色成员管理范围

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| role\_id | Integer | 是 | 角色ID。 |
| dept\_ids | String | 否 | 待管理[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)列表。 |
| userid | String | 是 | 待管理[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |

## 获取指定角色的员工列表

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| size | Integer | 是 | 分页大小。 |
| offset | Integer | 是 | 分页偏移。 |
| role\_id | Integer | 是 | 角色ID。 |

## 更新部门

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| extension | Object | 否 | 分页大小。 |
| outer\_permit\_users | Array of String | 是 | 分页偏移。 |
| language | Integer | 是 | 角色ID。 |
| source\_identifier | String | 否 | 部门标识字段，开发者可用该字段来唯一标识一个部门，并与钉钉外部通讯录里的部门做映射。 |
| outer\_permit\_depts | Array of Long | 否 | 配置额外可见[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。总数不能超过200。 |
| order | Integer | 否 | 在父部门中的排序值，order值小的排序靠前。 |
| brief | String | 否 | 部门简介。 |
| dept\_permits | Array of Long | 否 | 可以查看指定隐藏部门的其他[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)列表。 |
| group\_contain\_outer\_dept | Boolean | 否 | 部门群是否包含外包部门：   - true：是 - false：否 |
| org\_dept\_owner | String | 否 | 企业群[群主ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| outer\_dept | Boolean | 否 | 是否限制本部门成员查看通讯录：   - true：是 - false：否 |
| telephone | String | 否 | 部门联系方式。 |
| auto\_approve\_apply | Boolean | 否 | 是否默认同意加入该部门的申请：   - true：是 - false：否 |
| group\_contain\_sub\_dept | Boolean | 否 | 部门群是否包含子部门：   - true：是 - false：否 |
| auto\_add\_user | Boolean | 否 | 新人是否会自动加入部门群：   - true：是 - false：否 |
| dept\_manager\_userid\_list | Array of String | 否 | 部门的主管列表，主管ID列表。 |
| parent\_id | Long | 否 | 待更新父[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| hide\_dept | Boolean | 否 | 是否隐藏部门：   - true：隐藏 - false：不隐藏 |
| name | String | 否 | 部门名称。 |
| user\_permits | Array of String | 否 | 可以查看指定隐藏部门的其他用户ID列表。总数不能超过200。  **[!NOTE]**  如果hide\_dept为`true`时，则此值生效。 |
| group\_contain\_hidden\_dept | Boolean | 否 | 部门群是否包含隐藏部门：   - true：是 - false：否 |
| force\_update\_fields | Array of String | 否 | 强制更新的字段，支持清空指定的字段，使用逗号分隔。目前支持字段`dept_manager_userid_list`。 |
| outer\_dept\_only\_self | Boolean | 否 | 是否只能看到所在部门及下级部门通讯录：   - true：是 - false：否 |
| dept\_id | Long | 是 | 待更新[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| create\_dept\_group | Boolean | 否 | 是否创建一个关联此部门的企业群：   - true：是 - false：否，默认 |

## 删除部门

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| dept\_id | Long | 是 | 待删除[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。  **[!NOTE]**   - 根部门不能删除 - 部门中有员工不能删除 - 部门的子部门中有员工不能删除 |

## 获取部门详情

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| language | String | 否 | 通讯录语言，默认zh\_CN。 |
| dept\_id | Long | 是 | 待查询[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，根部门ID为1。 |

## 获取部门员工人数

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| dept\_id | Long | 是 | 待获取[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |

## 获取子部门ID列表

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| dept\_id | Long | 是 | 待查询[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，根部门传1。 |

## 获取部门用户userid列表

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| dept\_id | Long | 是 | 待查询[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |

## 获取指定用户的所有父部门列表

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userid | String | 是 | 待查询[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |

## 获取指定部门的所有父部门列表

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| dept\_id | Long | 是 | 待查询[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |

## 获取管理员通讯录权限范围

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userid | String | 是 | 待查询[管理员ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |

## 添加外部联系人

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| share\_user\_ids | Array of String | 否 | 共享给的[员工ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)列表。 |
| follower\_user\_id | String | 是 | 填写[负责人ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| address | String | 否 | 地址。 |
| share\_dept\_ids | Array of Long | 否 | 共享给的[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| label\_ids | Array of Long | 是 | 标签列表。 |
| company\_name | String | 否 | 企业名。 |
| name | String | 是 | 名称。 |
| mobile | String | 是 | 手机号。 |
| remark | String | 否 | 备注。 |
| title | String | 否 | 职位。 |
| state\_code | String | 否 | 手机号国家码。 |

## 更新外部联系人

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| share\_user\_ids | Array of String | 否 | 共享给的[员工ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)列表。 |
| follower\_user\_id | String | 是 | 填写[负责人ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| address | String | 否 | 地址。 |
| share\_dept\_ids | Array of Long | 否 | 共享给的[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| user\_id | String | 是 | 待更新[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| label\_ids | Array of Long | 是 | 标签列表。 |
| company\_name | String | 否 | 企业名。 |
| name | String | 是 | 名称。 |
| mobile | String | 是 | 手机号。 |
| remark | String | 否 | 备注。 |
| title | String | 否 | 职位。 |
| state\_code | String | 否 | 手机号国家码。 |

## 获取外部联系人列表

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| size | Integer | 是 | 分页大小。 |
| offset | Integer | 是 | 分页偏移。 |

## 获取外部联系人详情

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| user\_id | String | 是 | 待查询外部[联系人ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |

## 获取企业信息（行业通讯录）

无入参。

## 获取部门下人员列表

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| cursor | String | 否 | 分页游标。 |
| size | Integer | 是 | 分页大小。 |
| dept\_id | Long | 是 | 待查询[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| role | String | 否 | 标签。 |

## 获取部门用户详情（行业通讯录）

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userid | String | 是 | 待查询[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
| dept\_id | Long | shi1 | 待查询用户的[部门ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。 |
