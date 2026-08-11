---
title: "不纳入调用量限制的接口清单"
source_url: "https://open.dingtalk.com/document/development/basic-interfaces-such-as-log-off-and-address-book"
namespace: "development"
slug: "basic-interfaces-such-as-log-off-and-address-book"
group: "应用开发"
tab: "服务端API"
breadcrumb: "平台公告与计费 > 资源与计费 > API调用量配额 > 不纳入调用量限制的接口清单"
doc_id: "GnKegSScKl"
updated_at: "2026-05-09 11:48:57"
---

> Source: https://open.dingtalk.com/document/development/basic-interfaces-such-as-log-off-and-address-book
> Path: 应用开发 / 服务端API / 平台公告与计费 > 资源与计费 > API调用量配额 > 不纳入调用量限制的接口清单
> Updated: 2026-05-09 11:48:57

# 不纳入调用量限制的接口清单

本文介绍了不纳入每月调用量限制的接口清单，包括基础接口（获取访问凭证、身份验证（免登）和通讯录）和生态接口的清单。

## **基础接口清单**

### **获取访问凭证接口**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token) | 调用本接口获取access\_token，调用服务端API获取应用资源时，需要通过access\_token来鉴权调用者身份进行授权。 | 服务端 |
| [获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app) | 调用本接口获取access\_token，调用服务端API获取应用资源时，需要通过access\_token来鉴权调用者身份进行授权。 | 新版服务端 |
| [获取第三方个人应用的access\_token](https://open.dingtalk.com/document/personalapp/obtain-the-access_token-of-a-third-party-personal-application) | 调用本接口获取第三方个人应用的access\_token。 | 服务端 |
| [获取用户token](https://open.dingtalk.com/document/orgapp/obtain-user-token) | 调用本接口获取用户token。 | 新版服务端 |
| [获取jsapi\_ticket](https://open.dingtalk.com/document/orgapp/obtain-jsapi_ticket) | 当开发H5微应用时，需要先通过本接口获取jsapi\_ticket，然后再生成鉴权签名，最后调用dd.config完成鉴权。 | 服务端 |
| [创建jsapi ticket](https://open.dingtalk.com/document/orgapp/create-a-jsapi-ticket) | 当开发H5微应用时，需要先通过本接口获取jsapi\_ticket，然后再生成鉴权签名，最后调用dd.config完成鉴权。 | 新版服务端 |
| [获取微应用后台免登的access\_token](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-the-micro-application-background-without-log-on) | 调用本接口获取微应用后台免登的access\_token。获取的access\_token即ssotoken只在应用管理后台免登场景中使用。 | 服务端 |
| [获取微应用后台免登的access\_token](https://open.dingtalk.com/document/orgapp/obtain-the-ssotoken-for-micro-application-background-logon-free) | 调用本接口获取微应用后台免登的access\_token。获取的access\_token只在应用管理后台免登场景中使用。 | 新版服务端 |
| [查询个人授权记录](https://open.dingtalk.com/document/orgapp/query-individual-authorization-records) | 当需要查询用户的授权记录信息时，可以调用本接口查询用户的个人授权记录。 | 新版服务端 |

### **身份验证（免登）接口**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [通过免登码获取用户信息](https://open.dingtalk.com/document/orgapp/obtain-the-userid-of-a-user-by-using-the-log-free) | 在第三方企业应用免登和企业内部应用免登场景中，开发者需要使用本接口通过access\_token和免登接口中获取的code来获取用户userid。 | 服务端 |
| [获取应用管理后台免登的用户信息](https://open.dingtalk.com/document/orgapp/exchange-code-for-the-identity-information-of-a-microapplication-administrator) | 在应用管理后台免登场景中，需要本接口通过获取到的免登授权码code和获取到的应用后台免登的access\_token来换取应用管理员的身份信息。 | 服务端 |
| [获取应用管理后台免登的用户信息](https://open.dingtalk.com/document/orgapp/obtains-the-identity-of-an-application-administrator) | 在应用管理后台免登场景中，需要本接口通过获取到的免登授权码code和获取到的应用后台免登的access\_token来换取应用管理员的身份信息。 | 新版服务端 |
| [根据sns临时授权码获取用户信息](https://open.dingtalk.com/document/orgapp/obtain-the-user-information-based-on-the-sns-temporary-authorization) | 调用本接口根据sns临时授权码获取用户信息。 | 服务端 |

### **通讯录管理接口**

**用户管理**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [创建用户](https://open.dingtalk.com/document/orgapp/user-information-creation) | 调用本接口创建新用户。 | 服务端 |
| [更新用户信息](https://open.dingtalk.com/document/orgapp/user-information-update) | 调用本接口更新指定的用户信息。 | 服务端 |
| [查询用户详情](https://open.dingtalk.com/document/orgapp/query-user-details) | 调用本接口获取指定用户的详细信息。 | 服务端 |
| [删除用户](https://open.dingtalk.com/document/orgapp/delete-a-user) | 调用本接口根据用户的userid删除指定用户。 | 服务端 |
| [获取部门用户基础信息](https://open.dingtalk.com/document/orgapp/queries-the-simple-information-of-a-department-user) | 调用本接口获取指定部门的用户基础信息。 | 服务端 |
| [获取部门用户详情](https://open.dingtalk.com/document/orgapp/queries-the-complete-information-of-a-department-user) | 调用本接口获取指定部门中的用户详细信息。 | 服务端 |
| [获取部门用户userid列表](https://open.dingtalk.com/document/orgapp/query-the-list-of-department-userids) | 调用本接口获取指定部门的userid列表。 | 服务端 |
| [获取员工人数](https://open.dingtalk.com/document/orgapp/obtain-the-number-of-employees-v2) | 调用本接口获取员工人数。 | 服务端 |
| [获取未登录钉钉的员工列表](https://open.dingtalk.com/document/orgapp/queries-the-inactive-users-or-active-users-under-an-enterprise) | 调用本接口查询指定日期内未登录钉钉的企业员工列表。 | 服务端 |
| [根据手机号查询用户](https://open.dingtalk.com/document/orgapp/query-users-by-phone-number) | 调用本接口根据手机号获取专属账号用户的userId。 | 服务端 |
| [根据unionid获取用户userid](https://open.dingtalk.com/document/orgapp/query-a-user-by-the-union-id) | 调用本接口根据unionid获取用户的userid。 | 服务端 |
| [获取管理员列表](https://open.dingtalk.com/document/orgapp/query-the-administrator-list) | 调用本接口查询管理员列表。 | 服务端 |
| [获取管理员通讯录权限范围](https://open.dingtalk.com/document/orgapp/query-permissions-of-the-administrator-address-book) | 调用本接口获取管理员通讯录权限范围。 | 服务端 |
| [查询离职记录列表](https://open.dingtalk.com/document/orgapp/query-the-details-of-employees-who-have-left-office) | 调用本接口查询企业离职记录列表，包含离职员工的离职日期、手机号码和退出企业方式等信息。 | 新版服务端 |
| [设置高管模式](https://open.dingtalk.com/document/orgapp/update-executive-settings) | 调用本接口设置员工的高管模式。 | 新版服务端 |
| [获取用户高管模式设置](https://open.dingtalk.com/document/orgapp/get-user-executive-mode-settings) | 调用本接口获取用户高管模式设置。 | 新版服务端 |
| [删除用户属性可见性设置](https://open.dingtalk.com/document/orgapp/delete-enterprise-employee-attribute-field-visibility-settings) | 调用本接口删除企业员工属性字段可见性设置。 | 新版服务端 |
| [获取用户属性可见性设置](https://open.dingtalk.com/document/orgapp/pull-hidden-property-field-for-enterprise-employees) | 调用本接口获取用户属性可见性设置。 | 新版服务端 |
| [设置用户属性可见性](https://open.dingtalk.com/document/orgapp/add-or-update-the-hidden-settings-of-the-employee-property) | 调用本接口设置用户属性可见性。 | 新版服务端 |
| [获取用户通讯录个人信息](https://open.dingtalk.com/document/orgapp/dingtalk-retrieve-user-information) | 调用本接口获取企业用户通讯录中的个人信息。 | 新版服务端 |

**部门管理**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [创建部门](https://open.dingtalk.com/document/orgapp/create-a-department-v2) | 调用本接口创建新部门。 | 服务端 |
| [更新部门](https://open.dingtalk.com/document/orgapp/update-a-department-v2) | 调用本接口更新部门信息。 | 服务端 |
| [删除部门](https://open.dingtalk.com/document/orgapp/delete-a-department-v2) | 调用本接口根据部门ID删除指定部门。 | 服务端 |
| [获取部门详情](https://open.dingtalk.com/document/orgapp/query-department-details0-v2) | 调用本接口根据部门ID获取指定部门详情。 | 服务端 |
| [获取部门列表](https://open.dingtalk.com/document/orgapp/obtain-the-department-list-v2) | 调用本接口获取下一级部门基础信息。 | 服务端 |
| [获取子部门ID列表](https://open.dingtalk.com/document/orgapp/obtain-a-sub-department-id-list-v2) | 调用本接口获取企业部门下的所有直属子部门列表。 | 服务端 |
| [获取指定部门的所有父部门列表](https://open.dingtalk.com/document/orgapp/query-the-list-of-all-parent-departments-of-a-department) | 调用本接口获取指定部门的所有父部门ID列表。 | 服务端 |
| [获取指定用户的所有父部门列表](https://open.dingtalk.com/document/orgapp/queries-the-list-of-all-parent-departments-of-a-user) | 调用本接口查询指定用户所属的所有父级部门。 | 服务端 |

**角色管理**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [创建角色](https://open.dingtalk.com/document/orgapp/add-role) | 调用本接口创建新角色。 | 服务端 |
| [创建角色组](https://open.dingtalk.com/document/orgapp/add-a-role-group) | 调用本接口创建角色组。 | 服务端 |
| [更新角色名称](https://open.dingtalk.com/document/orgapp/update-role) | 调用本接口更新角色名称。 | 服务端 |
| [批量增加员工角色](https://open.dingtalk.com/document/orgapp/add-role-information-to-employees-in-batches) | 调用本接口批量增加员工角色。 | 服务端 |
| [删除角色](https://open.dingtalk.com/document/orgapp/delete-role-information) | 调用本接口根据角色ID删除指定的角色。 | 服务端 |
| [批量删除员工角色](https://open.dingtalk.com/document/orgapp/delete-the-color-information-of-employee-corners-in-batches) | 调用本接口批量删除员工的角色。 | 服务端 |
| [设定角色成员管理范围](https://open.dingtalk.com/document/orgapp/update-role-member-management-department-scope) | 调用本接口设定角色成员管理范围。 | 服务端 |
| [获取角色组列表](https://open.dingtalk.com/document/orgapp/obtains-the-role-group-information) | 调用本接口获取角色组信息。 | 服务端 |
| [获取角色列表](https://open.dingtalk.com/document/orgapp/obtains-a-list-of-enterprise-roles) | 调用本接口获取角色列表。 | 服务端 |
| [获取角色详情](https://open.dingtalk.com/document/orgapp/queries-role-details) | 调用本接口根据角色ID获取指定角色详情。 | 服务端 |
| [获取指定角色的员工列表](https://open.dingtalk.com/document/orgapp/obtain-the-list-of-employees-of-a-role) | 调用本接口获取指定角色的员工列表。 | 服务端 |

**外部联系人**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [添加外部联系人](https://open.dingtalk.com/document/orgapp/add-enterprise-external-contacts) | 调用本接口添加企业外部联系人。 | 服务端 |
| [删除外部联系人](https://open.dingtalk.com/document/orgapp/delete-external-contact) | 调用本接口删除企业外部联系人。 | 服务端 |
| [更新外部联系人](https://open.dingtalk.com/document/orgapp/update-enterprise-external-contacts) | 调用本接口更新企业外部联系人。 | 服务端 |
| [获取外部联系人列表](https://open.dingtalk.com/document/orgapp/obtain-the-external-contact-list) | 调用本接口获取企业外部联系人列表。 | 服务端 |
| [获取外部联系人标签列表](https://open.dingtalk.com/document/orgapp/obtains-a-list-of-external-contact-tags) | 调用本接口获取企业外部联系人的标签。 | 服务端 |
| [获取外部联系人详情](https://open.dingtalk.com/document/orgapp/obtains-the-external-contact-details-of-an-enterprise) | 调用本接口获取企业外部联系人的详细信息。 | 服务端 |

**企业管理**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [获取企业邀请信息](https://open.dingtalk.com/document/orgapp/obtain-invitation-information) | 调用本接口获取企业的邀请信息。 | 新版服务端 |
| [获取企业最新钉钉指数信息](https://open.dingtalk.com/document/orgapp/queries-the-latest-dingtalk-index-information) | 调用本接口获取企业最新钉钉指数信息。 | 新版服务端 |
| [获取企业认证信息](https://open.dingtalk.com/document/orgapp/obtain-enterprise-authentication-information) | 调用本接口获取企业认证信息。 | 新版服务端 |

**通讯录可见性管理**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [获取通讯录隐藏设置](https://open.dingtalk.com/document/orgapp/obtains-the-hide-settings-of-the-address-book) | 调用本接口批量获取通讯录隐藏的设置列表。 | 新版服务端 |
| [删除通讯录隐藏设置](https://open.dingtalk.com/document/orgapp/delete-hide-settings) | 调用本接口删除通讯录隐藏设置。 | 新版服务端 |
| [更新通讯录隐藏设置](https://open.dingtalk.com/document/orgapp/update-address-book-hide-settings) | 调用本接口更新通讯录隐藏设置。 | 新版服务端 |
| [设置部门可见性优先级](https://open.dingtalk.com/document/orgapp/set-address-book-visibility-sub-department-settings-to-take-precedence) | 调用本接口设置通讯录部门可见性优先级。 | 新版服务端 |

## **智能人事接口清单**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [添加企业待入职员工](https://open.dingtalk.com/document/orgapp/add-employees-to-be-hired-through-intelligent-personnel) | 添加企业待入职员工。 | 服务端 |
| [获取待入职员工列表](https://open.dingtalk.com/document/orgapp/intelligent-personnel-query-the-list-of-employees-to-be-hired) | 查询企业待入职员工userid列表。 | 服务端 |
| [获取在职员工列表](https://open.dingtalk.com/document/orgapp/intelligent-personnel-query-the-list-of-on-the-job-employees-of-the) | 查询企业在职员工userid列表。 | 服务端 |
| [更新员工花名册信息](https://open.dingtalk.com/document/orgapp/intelligent-personnel-update-employee-file-information) | 更新员工档案信息，支持明细分组。 | 服务端 |
| [获取员工花名册字段信息](https://open.dingtalk.com/document/orgapp/intelligent-personnel-obtain-employee-roster-information) | 查询员工花名册指定字段的信息，支持明细分组字段。 | 服务端 |
| [获取花名册元数据](https://open.dingtalk.com/document/orgapp/intelligent-personnel-roster-metadata-query) | 获取员工花名册的元数据，包括花名册分组、字段等。 | 服务端 |
| [批量获取员工离职信息](https://open.dingtalk.com/document/orgapp/obtain-resignation-information-of-employees-new-version) | 批量查询员工的离职信息，如离职人员的部门ID、离职主动原因和被动原因等。 | 新版服务端 |
| [智能人事员工调岗](https://open.dingtalk.com/document/orgapp/intelligent-personnel-staff-transfer) | 给智能人事员工调岗，支持以下内容调整，如员工部门列表、主部门、职务、职位和职级。 | 新版服务端 |
| [获取离职员工列表](https://open.dingtalk.com/document/orgapp/obtain-the-list-of-employees-who-have-left) | 查询企业离职员工userId列表。 | 新版服务端 |

## **钉钉客联接口清单**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [创建钉外账号](https://open.dingtalk.com/document/orgapp/create-bc-account-association) | 创建钉外用户账号，并建立与钉内用户的账号关联关系。 | 新版服务端 |
| [创建普通群或跨钉两人群](https://open.dingtalk.com/document/orgapp/create-group-sessions) | 创建钉钉客联互通群，群类型为普通群或跨钉两人群。 | 新版服务端 |
| [创建钉外两人群](https://open.dingtalk.com/document/orgapp/create-two-people-outside-the-nail) | 创建钉外两人群。 | 新版服务端 |
| [创建店铺群](https://open.dingtalk.com/document/orgapp/create-a-store-group) | 创建店铺群。 | 新版服务端 |
| [获取钉钉客联群会话地址](https://open.dingtalk.com/document/orgapp/get-the-dingtalk-guest-group-session-address) | 获取钉钉客联群会话地址，钉外用户可通过该地址进入对应群内。 | 新版服务端 |
| [添加互通群成员](https://open.dingtalk.com/document/orgapp/add-a-group-member-1) | 向互通群内添加群成员。 | 新版服务端 |
| [查询互通群成员列表](https://open.dingtalk.com/document/orgapp/queries-the-group-member-list) | 查询互通群成员列表，包括普通群、跨钉两人群、钉外两人群和店铺群。 | 新版服务端 |
| [移除互通群成员](https://open.dingtalk.com/document/orgapp/remove-group-members) | 移除互通群成员。 | 新版服务端 |
| [修改互通群头像](https://open.dingtalk.com/document/orgapp/modify-the-avatar-of-a-communication-group) | 修改互通群头像，包括普通群、跨钉两人群、钉外两人群和商铺群。 | 新版服务端 |
| [修改互通群名称](https://open.dingtalk.com/document/orgapp/modify-the-group-name) | 修改群名称，包括普通群、跨钉两人群、钉外两人群和店铺群。 | 新版服务端 |
| [更换互通群群主](https://open.dingtalk.com/document/orgapp/change-group-owner) | 更换互通群的群主。 | 新版服务端 |
| [钉外用户向钉内用户或互通群发送消息](https://open.dingtalk.com/document/orgapp/send-c2b-messages) | 实现钉外用户向钉内用户或互通群发送消息。 | 新版服务端 |
| [钉内用户向互通群或钉外用户发送消息](https://open.dingtalk.com/document/orgapp/send-b2c-messages) | 实现钉内用户给钉外用户或者互通群发送消息。 | 新版服务端 |
| [互通群机器人发送群消息](https://open.dingtalk.com/document/orgapp/group-communication-robots-send-group-messages) | 通过互通群内机器人向群内发送消息。 | 新版服务端 |
| [查询钉外用户未读消息的数量](https://open.dingtalk.com/document/orgapp/querying-the-number-of-unread-messages-of-the-user) | 查询钉外用户未读消息的数量。 | 新版服务端 |
| [批量查询跨钉两人群列表](https://open.dingtalk.com/document/orgapp/queries-the-session-information-of-two-population-groups) | 根据群成员批量查询跨钉两人群列表。 | 新版服务端 |
| [解散互通群](https://open.dingtalk.com/document/orgapp/disband-bc-interconnection-group) | 解散互通群，包括普通群、跨钉两人群、钉外两人群和店铺群。 | 新版服务端 |

## 生态**接口列表**

### **阿里商旅接口**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [机票城市搜索](https://open.dingtalk.com/document/orgapp/air-ticket-city-search) | 搜索火车票城市。 | 服务端 |
| [火车票城市搜索](https://open.dingtalk.com/document/orgapp/train-ticket-city-search) | 搜索机票城市。 | 服务端 |
| [新建成本中心](https://open.dingtalk.com/document/orgapp/new-cost-center) | 新建成本中心。 | 服务端 |
| [修改成本中心](https://open.dingtalk.com/document/orgapp/modify-basic-cost-center-information) | 修改成本中心基本信息。 | 服务端 |
| [删除成本中心](https://open.dingtalk.com/document/orgapp/delete-cost-center) | 删除成本中心。 | 服务端 |
| [查询成本中心](https://open.dingtalk.com/document/orgapp/query-cost-center) | 查询成本中心信息。 | 服务端 |
| [设置成本中心人员信息](https://open.dingtalk.com/document/orgapp/set-up-cost-center-personnel-information) | 设置成本中心人员信息。 | 服务端 |
| [删除成本中心人员信息](https://open.dingtalk.com/document/orgapp/delete-cost-center-personnel-information) | 删除成本中心人员信息。 | 服务端 |
| [商旅成本中心转换为外部成本中心](https://open.dingtalk.com/document/orgapp/business-travel-cost-center-converted-to-external-cost-center) | 商旅成本中心转换为外部成本中心。 | 服务端 |
| [添加项目](https://open.dingtalk.com/document/orgapp/add-a-project) | 添加商旅项目。 | 服务端 |
| [修改项目](https://open.dingtalk.com/document/orgapp/project-change) | 修改项目信息。 | 服务端 |
| [删除项目](https://open.dingtalk.com/document/orgapp/delete-a-project) | 删除项目。 | 服务端 |
| [新建审批单](https://open.dingtalk.com/document/orgapp/user-new-approval-form) | 新建审批单。 | 服务端 |
| [获取申请单列表](https://open.dingtalk.com/document/orgapp/search-enterprise-approval-form-data) | 查询企业审批单数据。 | 服务端 |
| [获取申请单详情](https://open.dingtalk.com/document/orgapp/obtains-the-detailed-data-of-a-single-request) | 获取单个申请单的详细信息。 | 服务端 |
| [修改申请单](https://open.dingtalk.com/document/orgapp/user-modify-approval-form) | 修改出差申请单。 | 服务端 |
| [更新申请单状态](https://open.dingtalk.com/document/orgapp/update-approval-form) | 更新审批单状态。 | 服务端 |
| [搜索第三方酒店超标审批单](https://open.dingtalk.com/document/orgapp/dingtalk-oapi-alitrip-btrip-exceedapply-hotel-get) | 搜索第三方酒店超标审批单。 | 服务端 |
| [搜索第三方火车票超标审批单](https://open.dingtalk.com/document/orgapp/dingtalk-oapi-alitrip-btrip-exceedapply-train-get) | 搜索第三方火车票超标审批单。 | 服务端 |
| [回传第三方超标审批结果](https://open.dingtalk.com/document/orgapp/dingtalk-oapi-alitrip-btrip-exceedapply-sync) | 回传第三方超标审批结果。 | 服务端 |
| [搜索第三方机票超标审批单](https://open.dingtalk.com/document/orgapp/dingtalk-oapi-alitrip-btrip-exceedapply-flight) | 搜索第三方机票的超标审批单。 | 服务端 |
| [获取企业机票订单数据](https://open.dingtalk.com/document/orgapp/obtains-enterprise-ticket-order-data) | 获取企业机票订单数据 | 服务端 |
| [获取企业商旅酒店订单数据](https://open.dingtalk.com/document/orgapp/enterprises-obtain-order-data-for-business-hotels) | 获取商旅酒店订单数据。 | 服务端 |
| [获取企业火车票订单数据](https://open.dingtalk.com/document/orgapp/obtains-the-enterprise-train-ticket-order-data) | 获取企业火车票订单数据。 | 服务端 |
| [获取用车订单数据](https://open.dingtalk.com/document/orgapp/vehicle-order-query-interface) | 获取企业用车订单数据。 | 服务端 |
| [关联单号查询相关订单信息列表](https://open.dingtalk.com/document/orgapp/link-no-to-query-the-list-of-related-order-information) | 申请单中关联单号获取订单信息。 | 新版服务端 |
| [获取商旅访问地址](https://open.dingtalk.com/document/orgapp/obtain-business-travel-access-addresses) | 获取各个场景预订访问地址，以及我的订单地址。 | 服务端 |
| [新增发票配置](https://open.dingtalk.com/document/orgapp/new-invoice-configuration) | 新增发票配置。 | 服务端 |
| [配置发票适用人群](https://open.dingtalk.com/document/orgapp/configure-invoice-users) | 配置发票适用人群。 | 服务端 |
| [查询可用发票列表](https://open.dingtalk.com/document/orgapp/query-available-invoices) | 查询可用发票列表。 | 服务端 |
| [修改发票配置](https://open.dingtalk.com/document/orgapp/modify-invoice-configuration) | 修改发票配置。 | 服务端 |
| [删除发票信息](https://open.dingtalk.com/document/orgapp/delete-invoice-information) | 删除发票信息。 | 服务端 |
| [同步市内用车申请单](https://open.dingtalk.com/document/orgapp/synchronize-third-party-city-vehicle-approval-form) | 同步市内用车申请单。 | 服务端 |
| [审批市内用车申请单](https://open.dingtalk.com/document/orgapp/approval-of-third-party-city-car-application-form) | 审批市内用车申请单。 | 服务端 |
| [查询市内用车申请单](https://open.dingtalk.com/document/orgapp/query-the-application-form-for-third-party-vehicles-in-the-city) | 查询市内用车申请单。 | 服务端 |
| [查询用车结算记录](https://open.dingtalk.com/document/orgapp/query-interface-for-vehicle-settlement-and-bookkeeping) | 查询商旅用车的结算记账数据。 | 新版服务端 |
| [查询商旅火车票结算数据](https://open.dingtalk.com/document/orgapp/business-travel-train-ticket-settlement-bookkeeping-query-interface) | 查询商旅火车票结算记账数据。 | 新版服务端 |
| [查询酒店结算数据](https://open.dingtalk.com/document/orgapp/hotel-settlement-bookkeeping-query-interface) | 查询商旅酒店结算记账数据。 | 新版服务端 |
| [查询机票结算数据](https://open.dingtalk.com/document/orgapp/ticket-settlement-bookkeeping-query-interface) | 查询机票结算记账数据。 | 新版服务端 |
| [获取月对账结算数据](https://open.dingtalk.com/document/orgapp/obtain-monthly-reconciliation-settlement-data) | 获取月对账结算数据下载地址。 | 服务端 |
| [查询预估价](https://open.dingtalk.com/document/orgapp/query-estimated-price) | 查询预估价。 | 服务端 |

### **小蜜客服接口**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [智能问答](https://open.dingtalk.com/document/orgapp/alimebot-intelligent-q-a-interface) | 使用小蜜客服机器人的能力进行智能问答。 | 新版服务端 |
| [推送小蜜机器人单聊O2O消息](https://open.dingtalk.com/document/orgapp/push-xiaomi-customer-service-robot-single-chat-message) | 通过小蜜客服机器人发送O2O（即Online To Offline）线上线下消息。 | 新版服务端 |
| [小蜜客服机器人消息回复](https://open.dingtalk.com/document/orgapp/xiaomi-customer-service-robot-message-reply) | 根据小蜜客服机器人sessionId进行异步消息回复。 | 新版服务端 |
| [查询机器人基础指标数据](https://open.dingtalk.com/document/orgapp/query-robot-data-indicators) | 根据机器人ID查询某时间段机器人的基础指标数据。 | 新版服务端 |
| [获取用户登录凭证](https://open.dingtalk.com/document/orgapp/obtains-the-user-login-credential-of-the-third-party-system-of) | 获取用户的登录凭证。 | 新版服务端 |

### **智能客服接口**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [创建自助单](https://open.dingtalk.com/document/orgapp-server/create-a-self-service-ticket#doc-api-dingtalk-CreateTicket) | 创建用户自定义的自助单。 | 新版服务端 |
| [执行工单活动](https://open.dingtalk.com/document/orgapp-server/intelligent-customer-service-execute-work-order-activities#topic-2083994) | 执行工单活动。 | 新版服务端 |
| [查询动作记录](https://open.dingtalk.com/document/orgapp-server/intelligent-customer-service-query-action-records#doc-api-dingtalk-PageListAction) | 查询动作记录。 | 新版服务端 |
| [分页查询工单](https://open.dingtalk.com/document/orgapp-server/intelligent-customer-service-paging-query-work-order#doc-api-dingtalk-PageListTicket) | 分页查询工单。 | 新版服务端 |

### **员工服务台**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| 使用服务助手推送消息 | 通过服务助手机器人给企业员工发送消息。 | 服务端 |

### **制造业接口**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [计件报工](https://open.dingtalk.com/document/orgapp/riqing-monthly-settlement-piece-rate-reporting-interface) | 用于MES系统上报计件数据到平台。 | 新版服务端 |
| [查询计件报工数据](https://open.dingtalk.com/document/orgapp/riqing-monthly-settlement-query-interface-for-piece-rate-reporting) | 查询计件报工的数据。 | 新版服务端 |

### **e签宝接口**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [e签宝数据初始化](https://open.dingtalk.com/document/orgapp/isv-service-provider-data-initialization) | 帮助钉钉企业进行e签宝开放平台的数据初始化。 | 新版服务端 |
| [获取授权的页面地址](https://open.dingtalk.com/document/orgapp/obtain-the-address-of-the-authorized-page) | 获取企业授权的页面地址。 | 新版服务端 |
| [取消企业授权](https://open.dingtalk.com/document/orgapp/cancel-enterprise-authorization) | 取消授权过企业的授权状态。 | 新版服务端 |
| [套餐转售—分润模式](https://open.dingtalk.com/document/orgapp/package-resale-1-distribution-mode) | 为使用电子合同的用户创建转售订单。 | 新版服务端 |
| [套餐转售—底价结算模式](https://open.dingtalk.com/document/orgapp/package-resale-2-reserve-price-settlement-mode) | 直接转售e签宝订单给最终真正使用电子合同的用户。 | 新版服务端 |
| [查询套餐余量](https://open.dingtalk.com/document/orgapp/query-package-balance) | 查询当前企业的套餐余量。 | 新版服务端 |
| [获取企业的e签宝微应用状态](https://open.dingtalk.com/document/orgapp/obtain-the-current-status-of-the-company-s-e-sign-micro-application) | 获取企业的e签宝微应用状态。 | 新版服务端 |
| [查询企业是否实名认证](https://open.dingtalk.com/document/orgapp/query-enterprise-information) | 查询企业是否已在e签宝完成实名认证。 | 新版服务端 |
| [获取企业控制台地址](https://open.dingtalk.com/document/orgapp/get-enterprise-console-address) | 获取的企业在e签宝的控制台地址。 | 新版服务端 |
| [查询个人是否实名认证](https://open.dingtalk.com/document/orgapp/query-personal-information) | 查询当前用户是否已在e签宝完成实名认证。 | 新版服务端 |
| [获取个人实名的地址](https://open.dingtalk.com/document/orgapp/obtain-the-address-that-is-redirected-to-the-user-s-real) | 通过个人信息接口查询到个人未实名时，可调用本接口获取个人实名认证地址。 | 新版服务端 |
| [获取跳转到企业实名的地址](https://open.dingtalk.com/document/orgapp/obtain-the-address-that-is-redirected-to-the-enterprise-s-real) | 通过企业信息接口查询到企业未实名时，可调用本接口获取实名地址，在应用内展示给企业。 | 新版服务端 |
| [获取文件上传地址](https://open.dingtalk.com/document/orgapp/obtain-the-upload-url-of-a-file-1) | 获取到文件上传地址。 | 新版服务端 |
| [获取文件详情](https://open.dingtalk.com/document/orgapp/gets-the-file-details) | 查询文件详情。 | 新版服务端 |
| [获取发起签署任务的地址](https://open.dingtalk.com/document/orgapp/obtain-the-address-used-to-initiate-a-signed-task) | 获取发起签署任务的地址。 | 新版服务端 |
| [创建签署流程](https://open.dingtalk.com/document/orgapp/use-the-api-to-initiate-a-signature-process) | 当ISV侧企业有文件需签署时，可调用本接口获取发起签署地址。 | 新版服务端 |
| [获取签署人签署地址](https://open.dingtalk.com/document/orgapp/get-signatory-address) | 获取签署人签署地址。 | 新版服务端 |
| [获取流程的签署详情](https://open.dingtalk.com/document/orgapp/get-the-details-of-process-signing) | 根据taskId获取流程签署相关的详细信息。 | 新版服务端 |
| [获取流程任务用印审批列表](https://open.dingtalk.com/document/orgapp/obtains-the-print-approval-list-for-process-tasks) | 获取流程任务用印审批列表。 | 新版服务端 |
| [获取流程详细信息及操作记录](https://open.dingtalk.com/document/orgapp/obtains-the-task-details) | 获取流程详细信息及操作记录。 | 新版服务端 |
| [获取流程任务的所有合同列表](https://open.dingtalk.com/document/orgapp/get-a-list-of-all-contracts-for-the-process-task) | 获取流程任务的所有合同列表，收到签署完成消息后查询。 | 新版服务端 |

### 金智CRM接口

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [客户资料](https://open.dingtalk.com/document/orgapp/add-or-edit-customer-profile) | 新增或编辑客户资料。 | 新版服务端 |
| [客户公共池](https://open.dingtalk.com/document/orgapp/add-or-edit-customer-public-pools) | 新增或编辑客户公共池。 | 新版服务端 |
| [联系人](https://open.dingtalk.com/document/orgapp/add-or-edit-contacts) | 新增或编辑联系人。 | 新版服务端 |
| [合同订单](https://open.dingtalk.com/document/orgapp/add-or-edit-contract-orders) | 新增或编辑合同订单。 | 新版服务端 |
| [发货单](https://open.dingtalk.com/document/orgapp/add-or-edit-invoices) | 新增或编辑发货单。 | 新版服务端 |
| [销售换货单](https://open.dingtalk.com/document/orgapp/add-or-edit-a-sales-order) | 新增或编辑销售换货单。 | 新版服务端 |
| [销售机会](https://open.dingtalk.com/document/orgapp/add-or-edit-opportunities) | 新增或编辑销售机会。 | 新版服务端 |
| [报价记录](https://open.dingtalk.com/document/orgapp/add-or-edit-quotation-records) | 新增或编辑报价记录。 | 新版服务端 |
| [采购单](https://open.dingtalk.com/document/orgapp/edit-purchase-order) | 新增或编辑采购单。 | 新版服务端 |
| [生产单](https://open.dingtalk.com/document/orgapp/add-or-edit-a-production-order) | 新增或编辑生产单。 | 新版服务端 |
| [产品信息](https://open.dingtalk.com/document/orgapp/add-or-edit-product-information) | 新增或编辑产品信息。 | 新版服务端 |
| [入库单](https://open.dingtalk.com/document/orgapp/add-or-edit-a-shipment-record) | 新增或编辑入库单。 | 新版服务端 |
| [出库单](https://open.dingtalk.com/document/orgapp/add-or-edit-an-issue-ticket) | 新增或编辑出库单。 | 新版服务端 |
| [获取数据列表](https://open.dingtalk.com/document/orgapp/obtain-the-data-list) | 获取各种单据的列表数据。 | 新版服务端 |
| [获取数据详情](https://open.dingtalk.com/document/orgapp/queries-data-details) | 获取各种单据的详情数据。 | 新版服务端 |

### 氚云接口

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [获取应用列表](https://open.dingtalk.com/document/orgapp/queries-applications) | 查询氚云的应用信息。 | 新版服务端 |
| [获取应用功能节点](https://open.dingtalk.com/document/orgapp/queries-the-application-feature-nodes) | 获取应用的功能节点信息。 | 新版服务端 |
| [获取组织数据](https://open.dingtalk.com/document/orgapp/queries-organization-data) | 获取组织部门数据信息。 | 新版服务端 |
| [获取用户数据](https://open.dingtalk.com/document/orgapp/obtain-user-data) | 获取用户基础数据信息。 | 新版服务端 |
| [获取角色数据](https://open.dingtalk.com/document/orgapp/obtain-role-data) | 获取角色组、角色数据等信息。 | 新版服务端 |
| [获取角色用户数据](https://open.dingtalk.com/document/orgapp/obtain-role-data-1) | 获取指定角色包含的用户。 | 新版服务端 |
| [获取表单对象结构](https://open.dingtalk.com/document/orgapp/gets-the-form-object-structure) | 获取表单对象结构信息。 | 新版服务端 |
| [创建表单业务数据](https://open.dingtalk.com/document/orgapp/create-form-business-data) | 创建单条表单、流程表单的业务数据对象。 | 新版服务端 |
| [查询表单业务数据列表](https://open.dingtalk.com/document/orgapp/querying-form-business-data) | 查询表单业务数据实例集合。 | 新版服务端 |
| [修改表单业务对象数据](https://open.dingtalk.com/document/orgapp/modify-form-business-object-data) | 修改表单的单条业务实例数据。 | 新版服务端 |
| [批量新增表单业务数据](https://open.dingtalk.com/document/orgapp/batch-add-form-business-data) | 批量新增表单的业务实例数据。 | 新版服务端 |
| [删除业务对象](https://open.dingtalk.com/document/orgapp/delete-a-business-object) | 批量新增表单的业务实例数据。 | 新版服务端 |
| [获取业务实例信息](https://open.dingtalk.com/document/orgapp/queries-business-instance-information) | 获取表单的单条业务实例数据。 | 新版服务端 |
| [创建流程实例](https://open.dingtalk.com/document/orgapp/create-a-process-instance) | 创建流程表单的流程实例数据。 | 新版服务端 |
| [删除流程实例数据](https://open.dingtalk.com/document/orgapp/delete-process-instance-data) | 流程表单的单条流程实例数据。 | 新版服务端 |
| [取消流程实例](https://open.dingtalk.com/document/orgapp/cancel-a-process-instance) | 取消流程实例，取消后的流程实例状态为已取消。 | 新版服务端 |
| [查询流程实例](https://open.dingtalk.com/document/orgapp/query-flow-instances) | 查询流程表单的流程实例数据。 | 新版服务端 |
| [查询流程实例节点工作项](https://open.dingtalk.com/document/orgapp/query-flow-instance-node-work-items) | 获取流程实例节点工作项的相关信息。 | 新版服务端 |
| [获取附件临时访问地址](https://open.dingtalk.com/document/orgapp/obtain-the-temporary-attachment-free-address) | 获取附件临时免登的访问地址。 | 新版服务端 |
| [获取文件上传地址](https://open.dingtalk.com/document/orgapp/obtain-the-upload-url-of-a-file-2) | 返回表单中指定图片、附件等控件的文件上传地址。 | 新版服务端 |
