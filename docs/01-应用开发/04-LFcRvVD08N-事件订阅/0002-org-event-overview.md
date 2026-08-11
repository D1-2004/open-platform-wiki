---
title: "事件订阅总览"
source_url: "https://open.dingtalk.com/document/development/org-event-overview"
namespace: "development"
slug: "org-event-overview"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "事件订阅总览"
doc_id: "XfFwKhqxhk"
updated_at: "2026-05-14 11:38:13"
---

> Source: https://open.dingtalk.com/document/development/org-event-overview
> Path: 应用开发 / 事件订阅 / 事件订阅总览
> Updated: 2026-05-14 11:38:13

# 事件订阅总览

## **通讯录**

| **名称** | **描述** |
| --- | --- |
| [企业增加员工事件](https://open.dingtalk.com/document/orgapp/event-v3user-add-org) | 通讯录用户增加的推送数据。 |
| [通讯录用户更改](https://open.dingtalk.com/document/orgapp/event-v3user-modify-org) | 通讯录用户更改的推送数据。  只有当前企业内的用户信息变更才会触发此事件，用户的个人信息变更并不会触发，例如个人头像、个人昵称、钉钉号等。 |
| [通讯录用户离职](https://open.dingtalk.com/document/orgapp/event-v3user-leave-org) | 通讯录用户离职的推送数据。 |
| [加入企业后用户激活](https://open.dingtalk.com/document/orgapp/event-v3user-active-org) | 通讯录用户加入企业后用户激活的推送数据。 |
| [通讯录用户被设为管理员](https://open.dingtalk.com/document/orgapp/event-org-admin-add) | 通讯录用户被设为管理员的推送数据。 |
| [通讯录用户被取消设置管理员](https://open.dingtalk.com/document/orgapp/event-org-admin-remove) | 通讯录用户被取消设置管理员的推送数据。 |
| [通讯录企业部门创建](https://open.dingtalk.com/document/orgapp/event-org-dept-create) | 通讯录企业部门创建的推送数据。 |
| [通讯录企业部门修改](https://open.dingtalk.com/document/orgapp/event-org-dept-modify) | 通讯录企业部门修改的推送数据。 |
| [通讯录企业部门删除](https://open.dingtalk.com/document/orgapp/event-v3org-dept-remove) | 通讯录企业部门删除的推送数据。 |
| [员工角色信息发生变更](https://open.dingtalk.com/document/orgapp/event-label-user-change) | 企业员工角色信息发生变更的推送数据。 |
| [增加角色或者角色组](https://open.dingtalk.com/document/orgapp/event-label-conf-add) | 增加角色或者角色组的推送数据。 |
| [修改角色或者角色组](https://open.dingtalk.com/document/orgapp/event-label-conf-modify) | 修改角色或者角色组的推送数据。 |
| [删除角色或者角色组](https://open.dingtalk.com/document/orgapp/event-label-conf-del) | 删除角色或者角色组的推送数据。 |
| [企业信息发生变更](https://open.dingtalk.com/document/orgapp/event-org-change) | 企业信息发生变更的推送数据。 |
| [企业删除](https://open.dingtalk.com/document/orgapp/event-v3org-remove) | 企业被解散的推送数据。 |

## **服务窗**

| **名称** | **描述** |
| --- | --- |
| [服务窗关注事件](https://open.dingtalk.com/document/orgapp/event-official-account-follow) | 用户关注服务窗的推送数据。 |
| [服务窗取关事件](https://open.dingtalk.com/document/orgapp/event-official-account-unfollow) | 用户取消关注服务窗的推送数据。 |
| [用户信息授权结果](https://open.dingtalk.com/document/orgapp/event-official-account-user-data-apply-result) | 用户授权同意或者拒绝的推送数据。 |
| [服务号接收用户交互](https://open.dingtalk.com/document/orgapp/event-isw-user-event-received) | 服务号收到用户的交互事件, 目前只有菜单点击事件。 |

## **AI 助理**

| **名称** | **描述** |
| --- | --- |
| [AI助理安装事件](https://open.dingtalk.com/document/orgapp/events-ai-assistant-install) | 当用户组织开通了 AI 助理安装事件后，组织下用户通过分享功能添加（安装）AI 助理时，会触发事件推送。 |
| [AI助理信息变更](https://open.dingtalk.com/document/orgapp/events-ai-assistant-change) | 当 AI 助理的信息变更时，会触发事件推送，包括 AI 助理的创建、修改、删除。 |

## **OA审批**

| **名称** | **描述** |
| --- | --- |
| [审批实例开始、结束、终止、删除](https://open.dingtalk.com/document/orgapp/event-bpms-instance-change) | 审批实例开始、结束的推送数据。 |
| [审批任务开始、结束、取消](https://open.dingtalk.com/document/orgapp/event-bpms-task-change) | 审批任务开始、结束、转交的推送数据 |

## **待办**

| **名称** | **描述** |
| --- | --- |
| [待办任务新增](https://open.dingtalk.com/document/orgapp/event-todo-task-create) | 当用户发起一个钉钉待办任务时，会触发待办任务新增事件。 |
| [待办任务更新](https://open.dingtalk.com/document/orgapp/event-todo-task-update) | 当用户更新待办任务状态，变更执行者和参与者以及参与者的执行状态变更时，触发待办任务更新事件。 |
| [待办任务删除](https://open.dingtalk.com/document/orgapp/event-todo-task-delete) | 删除钉钉待办任务信息时，会触发待办任务删除事件。 |

## **文档**

| **名称** | **描述** |
| --- | --- |
| [文档知识库中创建小组](https://open.dingtalk.com/document/orgapp/event-doc-spaces-create-team) | 文档知识库中创建小组的推送数据。 |
| [文档知识库中小组变更](https://open.dingtalk.com/document/orgapp/event-doc-spaces-team-change) | 文档知识库中变更小组的推送数据。 |
| [文档知识库中小组成员变更](https://open.dingtalk.com/document/orgapp/event-doc-spaces-team-member-change) | 文档知识库中小组成员变更的推送数据。 |

## **签到**

| **名称** | **描述** |
| --- | --- |
| [用户签到](https://open.dingtalk.com/document/orgapp/event-check-in) | 用户签到的推送数据。 |

## **项目管理**

| **名称** | **描述** |
| --- | --- |
| [Teambiton工时变更事件](https://open.dingtalk.com/document/orgapp/event-project-worktime-updated) | 当Teambiton项目中工时属性内容发生更新时，钉钉通过事件订阅的方式将对应的项目中工时属性内容的变更推送给开发者，用于监听项目中工时属性更新的信息。 |
| [Teambiton项目变更事件](https://open.dingtalk.com/document/orgapp/teambiton-project-change-event) | 当Teambiton项目本身发生变更时，钉钉通过事件订阅的方式将对应的项目本身的变更内容推送给开发者，用于监听项目变更信息。 |
| [Teambition项目更新事件](https://open.dingtalk.com/document/orgapp/teamposition-project-update-event) | 当Teambiton项目属性发生更新操作时，钉钉通过事件订阅的方式将对应的项目属性的更新推送给开发者，用于监听项目属性更新信息。 |
| [Teambition应用变更事件](https://open.dingtalk.com/document/orgapp/teamposition-application-change-event) | 当Teambiton项目应用发生变更时，钉钉通过事件订阅的方式将项目应用变更内容推送给开发者，用于监听Teambiton项目应用变更信息。 |
| [Teambition成员变更事件](https://open.dingtalk.com/document/orgapp/teamposition-member-change-event) | 当Teambiton项目成员发生变更时，钉钉通过事件订阅的方式将项目成员变更内容推送给开发者，用于监听Teambiton项目成员变更信息。 |
| [Teambition任务更新事件](https://open.dingtalk.com/document/orgapp/teamposition-task-update-event) | 当Teambiton项目中任务属性内容发生更新时，钉钉通过事件订阅的方式将对应的项目中任务属性内容的变更推送给开发者，用于监听项目中任务属性更新的信息。 |
| [Teambition项目任务变更事件](https://open.dingtalk.com/document/orgapp/teamposition-project-task-change-event) | 当Teambiton项目中任务本身发生变更时，钉钉通过事件订阅的方式将对应的项目中任务本身发生的变更内容推送给开发者，用于监听项目中任务变更信息。 |

## **存储**

| **名称** | **描述** |
| --- | --- |
| [文件更新](https://open.dingtalk.com/document/orgapp/event-storage-dentry-update) | 文件或文件夹更新事件数据。如果仅在开发者后台开启存储事件订阅开关，无法接收回调事件，必须与接口配合使用，接口详情参见[订阅文件变更事件](https://open.dingtalk.com/document/orgapp/subscribe-to-file-change-events)。 |
| [文件或文件夹删除](https://open.dingtalk.com/document/orgapp/event-storage-dentry-delete) | 文件或文件夹删除事件。如果仅在开发者后台开启存储事件订阅开关，无法接收回调事件，必须与接口配合使用，接口详情参见[订阅文件变更事件](https://open.dingtalk.com/document/orgapp/subscribe-to-file-change-events)。 |
| [文件或文件夹添加](https://open.dingtalk.com/document/orgapp/event-storage-dentry-create) | 文件或文件夹添加事件数据。如果仅在开发者后台开启存储事件订阅开关，无法接收回调事件，必须与接口配合使用，接口详情参见[订阅文件变更事件](https://open.dingtalk.com/document/orgapp/subscribe-to-file-change-events)。 |

## **日程**

| **名称** | **描述** |
| --- | --- |
| [日程变更](https://open.dingtalk.com/document/orgapp/event-calendar-event-change) | 用户日程发生变更的推送数据。 |

## **视频/音频会议**

| **名称** | **描述** |
| --- | --- |
| [设备属性变更](https://open.dingtalk.com/document/orgapp/event-open-meeting-room-device-property-change) | 当钉钉视频会议设备属性变更时，钉钉推送的设备属性变更事件内容。 |
| [设备告警事件](https://open.dingtalk.com/document/orgapp/event-open-meeting-room-device-alarm) | 钉钉视频会议设备发生告警时，钉钉推送的设备告警事件内容。 |
| [钉钉投屏事件](https://open.dingtalk.com/document/orgapp/event-dingtalk-projection) | 钉钉投屏端发起投屏的推送数据。 |
| [视频会议状态变更](https://open.dingtalk.com/document/orgapp/event-meeting-status-change) | 视频会议状态变更的推送数据。 |
| [设备绑定会议室变更](https://open.dingtalk.com/document/orgapp/event-open-meeting-room-device-bind-change) | 当钉钉视频会议设备绑定、解绑钉钉会议室时，钉钉推送的设备绑定会议室变更事件内容。 |
| [视频会议成员状态变更](https://open.dingtalk.com/document/orgapp/event-meeting-member-status-change) | 视频会议成员状态变更的推送数据。 |

## **智能会议室**

| **名称** | **描述** |
| --- | --- |
| [会议室事件](https://open.dingtalk.com/document/orgapp/nqrbp8) | - 会议室预定成功、取消事件。 - 会议室创建、更新、删除事件。 |

## **直播**

| **名称** | **描述** |
| --- | --- |
| [直播状态变更](https://open.dingtalk.com/document/orgapp/event-live-status-change-event) | 直播状态变更的推送数据。 |
| [直播信息修改](https://open.dingtalk.com/document/orgapp/event-live-update-event) | 直播信息进行修改的推送数据。 |
| [直播回放观看数据推送](https://open.dingtalk.com/document/orgapp/event-live-watch-playback-event) | 直播回放观看信息的推送数据。 |
| [直播结束数据处理完成事件](https://open.dingtalk.com/document/orgapp/event-live-statistic-done-event) | 直播结束数据处理完成的数据推送。 |

## **应用管理**

| **名称** | **描述** |
| --- | --- |
| [小程序版本发布事件](https://open.dingtalk.com/document/orgapp/event-inner-app-version-publish) | 当开发者在开发者后台操作或者调用开放平台接口对企业内部小程序的开发版本进行体验发布和线上发布，推送的小程序版本发布事件数据。 |
| [小程序版本回滚事件](https://open.dingtalk.com/document/orgapp/event-inner-app-version-rollback) | 开发者在开发者后台操作或者调用开放平台接口对企业内部小程序的历史线上版本进行回滚时，推送的小程序版本回滚事件数据。 |

## **会话管理**

| **名称** | **描述** |
| --- | --- |
| [群会话解散群](https://open.dingtalk.com/document/orgapp/event-chat-disband) | 开发者监听群回调事件可以更及时地响应群的变化，与业务集成。群会话解散事件推送数据说明。 |
| [群会话添加人员](https://open.dingtalk.com/document/orgapp/event-chat-add-member) | 开发者监听群回调事件可以更及时地响应群的变化，与业务集成。为群会话添加人员事件字段说明。 |
| [群会话删除人员](https://open.dingtalk.com/document/orgapp/event-chat-remove-member) | 开发者监听群回调事件可以更及时地响应群的变化，与业务集成。为群会话删除人员事件推送数据说明。 |
| [群会话更换群主](https://open.dingtalk.com/document/orgapp/event-chat-update-owner) | 开发者监听群回调事件可以更及时地响应群的变化，与业务集成。该文档为群会话更换群主事件字段说明。 |
| [群会话更换群名称](https://open.dingtalk.com/document/orgapp/event-chat-update-title) | 开发者监听群回调事件可以更及时地响应群的变化，与业务集成。为群会话更换群名称事件数据说明。 |
| [群会话用户主动退群](https://open.dingtalk.com/document/orgapp/event-chat-quit) | 开发者监听群回调事件可以更及时地响应群的变化，与业务集成。为群会话删除人员事件推送数据说明。 |
| [群模板被启用或停用](https://open.dingtalk.com/document/orgapp/event-chat-template-change) | 群模板被启用或停用的推送数据。 |
| [单聊安装酷应用](https://open.dingtalk.com/document/orgapp/event-single-conversation-cool-app-install) | 单聊安装酷应用的推送数据。 |
| [单聊卸载酷应用](https://open.dingtalk.com/document/orgapp/event-single-conversation-cool-app-uninstall) | 单聊卸载酷应用的推送数据。 |
| [群内安装酷应用事件](https://open.dingtalk.com/document/orgapp/event-im-cool-app-install) | 群内安装酷应用的推送数据。 |
| [群内卸载酷应用事件](https://open.dingtalk.com/document/orgapp/event-im-cool-app-uninstall) | 群内卸载酷应用的推送数据。 |

## **机器人**

| **名称** | **描述** |
| --- | --- |
| [机器人消息已读事件](https://open.dingtalk.com/document/orgapp/event-robot-msg-read) | 开发者操作机器人发消息时，机器人消息被读的推送数据。 |
| [机器人消息撤回事件](https://open.dingtalk.com/document/orgapp/event-robot-msg-recall) | 开发者操作机器人发消息时，机器人消息撤回的推送数据。 |

## **荣誉勋章**

| **名称** | **描述** |
| --- | --- |
| [荣誉授予](https://open.dingtalk.com/document/orgapp/event-honor-grant) | 授予企业成员荣誉勋章时，推送的荣誉授予事件内容。 |
| [荣誉审核结果](https://open.dingtalk.com/document/orgapp/event-honor-audit) | 荣誉审核结果的推送数据。 |

## **客户管理**

| **名称** | **描述** |
| --- | --- |
| [主数据实例新增事件](https://open.dingtalk.com/document/orgapp/events-ding-paas-object-data-create) | 主数据实例新增的推送数据。 |
| [主数据实例删除事件](https://open.dingtalk.com/document/orgapp/event-ding-paas-object-data-delete) | 主数据实例删除的推送数据。 |
| [主数据实例更新事件](https://open.dingtalk.com/document/orgapp/event-ding-paas-object-data-update) | 主数据实例更新的推送数据。 |
| [CRM元数据](https://open.dingtalk.com/document/orgapp/event-ding-crm-object-meta) | 客户管理元数据回调事件，当用户进入客户管理后台编辑并发布客户、联系人、跟进记录表单时会触发推送。 |

## **专属开放**

| **名称** | **描述** |
| --- | --- |
| [服务号接收单聊消息](https://open.dingtalk.com/document/orgapp/event-isw-user-msg-received) | 服务号收到用户单聊消息的事件,钉钉服务器给开发者推送的事件内容，开发者根据收到的用户消息，结合发消息的接口，实现个性化的自动回复功能。 |
| [企业员工发送文件的检测事件](https://open.dingtalk.com/document/orgapp/event-org-file-send-check) | 企业员工发送文件的检测的推送数据。 |
| [专属群扩容审批](https://open.dingtalk.com/document/orgapp/event-approve-open-group-expansion) | 群规模扩容审批的推送数据。 |
| [专属钉钉数据迁移](https://open.dingtalk.com/document/orgapp/event-exclusive-data-transfer) | 专属钉钉数据迁移的推送数据。 |

## **考勤**

| **名称** | **描述** |
| --- | --- |
| [班次变更](https://open.dingtalk.com/document/orgapp/event-attend-shift-change) | 考勤班次变更的推送数据。 |
| [考勤组变更](https://open.dingtalk.com/document/orgapp/event-attend-group-change) | 考勤组变更的推送数据。 |
| [员工打卡事件](https://open.dingtalk.com/document/orgapp/event-attendance-check-record) | 当考勤数据发生员工打卡时，钉钉推送的员工打卡事件数据。 |
| [员工加班事件](https://open.dingtalk.com/document/orgapp/event-attendance-overtime-duration) | 企业内部应用通过考勤接口写入加班，触发加班转调休时，推送的员工加班事件数据。 |
| [水印打卡签到](https://open.dingtalk.com/document/orgapp/event-watermark-check-in) | 水印打卡签到的推送数据。 |
| [考勤结果变更](https://open.dingtalk.com/document/orgapp/event-attend-bosscheck-change) | 当钉钉管理员修改考勤结果变更时，钉钉通过事件订阅的方式将考勤结果变更内容推送给开发者。 |
| [假期规则变更事件](https://open.dingtalk.com/document/orgapp/events-leave-rule-change) | 当假期规则变更时，钉钉通过事件订阅的方式将规则变更内容推送给开发者，规则变更包括：增、删、改。 |
| [手动修改假期余额](https://open.dingtalk.com/document/orgapp/event-leave-quota-update) | 当管理员手动修改假期余额时，钉钉通过事件订阅的方式将规则变更内容推送给开发者。 |
| [考勤日统计变更事件](https://open.dingtalk.com/document/orgapp/event-attend-user-daily-summary-refresh) | 考勤日统计数据发生变更时，钉钉通过事件订阅的方式将变更内容推送给开发者。 |
| [考勤报表字段变更事件](https://open.dingtalk.com/document/orgapp/events-attendance-report-column-change) | 当考勤报表字段发生变更（如新增、删除或修改）时，钉钉推送发生变更的字段的信息。 |
| [请假、加班、出差、外出状态变更事件](https://open.dingtalk.com/document/orgapp/events-attendance-approve-status-change) | 当钉钉审批单状态变更时，钉钉通过事件订阅的方式将审批单变更内容推送给开发者，状态变更包括：发起、审批完成、撤销、删除。 |

## **智能人事**

| **名称** | **描述** |
| --- | --- |
| [人事档案变动](https://open.dingtalk.com/document/orgapp/event-hrm-user-record-change) | 人事档案变动的推送数据。 |
| [人事解决方案变更事件](https://open.dingtalk.com/document/orgapp/event-hrm-solution-manage) | 人事解决方案变更的推送数据。 |
| [人事平台员工异动事件v2](https://open.dingtalk.com/document/orgapp/event-hrm-mdm-user-change) | 人事平台员工异动的推送数据，异动有入职、转正、调岗、离职和晋升。 |

## **智能招聘**

| **名称** | **描述** |
| --- | --- |
| [人事档案变动](https://open.dingtalk.com/document/orgapp/event-hrm-user-record-change) | 招聘平台职位投递相关的推送数据。 |

## **医疗**

| **名称** | **描述** |
| --- | --- |
| [医疗行业用户属性变动](https://open.dingtalk.com/document/orgapp/event-industry-medical-user-prop-event) | 医疗通讯录发生医疗行业用户属性变动时，触发的医疗行业用户属性变动事件推送数据说明。 |
| [医疗行业用户所在科室医疗组变动](https://open.dingtalk.com/document/orgapp/event-industry-medical-user-dept-event) | 医疗通讯录发生医疗行业用户所在科室医疗组变动时，医疗行业用户所在科室医疗组变动的数据推送说明。 |
| [医疗行业科室医疗组变动](https://open.dingtalk.com/document/orgapp/event-industry-medical-dept-event) | 医疗通讯录发生医疗行业科室医疗组变动时，推送的医疗行业科室医疗组变动事件数据。 |
| [医疗行业科室医疗组属性变动](https://open.dingtalk.com/document/orgapp/event-industry-medical-dept-prop-event) | 医疗通讯录发生医疗行业科室医疗组变动时，推送的医疗行业科室医疗组变动事件数据。 |
| [医疗通讯录全量同步](https://open.dingtalk.com/document/orgapp/events-industry-medical-full-sync-1) | 医疗通讯录发生医疗通讯录全量同步时，推送的医疗通讯录全量同步事件数据说明。 |

## **教育**

| **名称** | **描述** |
| --- | --- |
| [教育部门新增](https://open.dingtalk.com/document/orgapp/event-edu-dept-insert) | 家校通讯录2.0，部门信息变更。主要包括家校通讯录架构中各个部门发生变更时的信息,edu\_dept\_insert表示部门节点新增事件数据。 |
| [教育部门更新](https://open.dingtalk.com/document/orgapp/event-edu-dept-update) | 家校通讯录2.0部门信息变更，家校通讯录架构中各个部门发生变更时的信息,edu\_dept\_update为部门节点更新事件数据。 |
| [教育部门删除](https://open.dingtalk.com/document/orgapp/event-edu-dept-delete) | 家校通讯录2.0，部门信息变更。主要包括家校通讯录架构中各个部门发生变更时的信息,该事件为部门节点删除事件数据。 |
| [新教育人员新增](https://open.dingtalk.com/document/orgapp/event-edu-user-insert) | 家校通讯录2.0，家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系（目前关系只有监护人与学生的关系)。教育人员新增事件表示在某个班级中人员相关身份新增触发的事件推送的数据。 |
| [新教育人员更新](https://open.dingtalk.com/document/orgapp/event-edu-user-update) | 家校通讯录2.0，家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系（目前关系只有监护人与学生的关系)。教育人员更新事件表示在某个班级中人员相关身份更新触发的事件推送的数据。 |
| [新教育人员删除](https://open.dingtalk.com/document/orgapp/event-edu-user-delete) | 家校通讯录2.0，家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系（目前关系只有监护人与学生的关系)。该事件表示在某个班级中人员相关身份删除事件数据。 |
| [新教育人员关系新增](https://open.dingtalk.com/document/orgapp/event-edu-user-relation-insert) | 家校通讯录2.0，人员变更推送。家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系。（目前关系只有监护人与学生的关系)。 该事件表示在某个班级中人员关系新增。此事件中各个字段的理解，可以总结为如下一句表达式：在班级${classId}中，${fromUserid}与${toUserid}的关系是 ${relationName}。在家校场景下，fromUserid为监护人，toUserid为学生。此回调事件推送的是最简单的数据。 |
| [新教育人员关系更新](https://open.dingtalk.com/document/orgapp/event-edu-user-relation-update) |
| [新教育人员关系删除](https://open.dingtalk.com/document/orgapp/event-edu-user-relation-delete) |
| [支付状态同步](https://open.dingtalk.com/document/orgapp/event-edu-trade-pay-status-sync) | 为了方便开发者感知用户状态变化，统一支付平台提供了事件推送能力，当前仅支持支付状态同步事件，即当用户订单的支付状态发生变化时，钉钉会通过事件订阅的方式将用户订单的支付状态的变更内容推送给开发者。 |

## **行业通用**

| **名称** | **描述** |
| --- | --- |
| [门店通用户权益变更事件](https://open.dingtalk.com/document/orgapp/event-shop-rights-event) | 门店通用户权益变更事件的推送数据。 |

## **服务群**

| **名称** | **描述** |
| --- | --- |
| [服务群群信息变更](https://open.dingtalk.com/document/orgapp/event-servicegroup-group-info-change) | 服务群群信息变更的推送数据。 |
| [服务群联系人关联客户](https://open.dingtalk.com/document/orgapp/event-servicegroup-contact-relate-customer) | 服务群联系人关联客户的推送数据。 |
| [服务群入群表单保存](https://open.dingtalk.com/document/orgapp/event-servicegroup-contact-join-group-form) | 服务群入群表单保存的推送数据。 |
| [服务群自定义表单删除实例](https://open.dingtalk.com/document/orgapp/event-servicegroup-custom-object-delete) | 服务群自定义表单删除实例的推送数据。 |
| [服务群自定义表单更新实例](https://open.dingtalk.com/document/orgapp/event-servicegroup-custom-object-edit) | 服务群自定义表单更新实例的推送数据。 |
| [服务群自定义表单创建实例](https://open.dingtalk.com/document/orgapp/event-servicegroup-custom-object-create) | 服务群自定义表单创建实例的推送数据。 |
| [服务群工单处理反馈](https://open.dingtalk.com/document/orgapp/event-servicegroup-ticket-deal-feedback) | 服务群工单处理反馈的推送数据。 |
| [服务群工单添加备注](https://open.dingtalk.com/document/orgapp/event-servicegroup-ticket-memo-add) | 服务群工单添加备注的推送数据。 |
| [弹内服务群话题变更事件](https://open.dingtalk.com/document/orgapp/event-servicegroup-voc-topic-detail) | 服务群话题变更的推送数据。 |
| [服务群工单已读](https://open.dingtalk.com/document/orgapp/event-servicegroup-ticket-read) | 服务群工单已读的推送数据。 |
| [服务群工单创建](https://open.dingtalk.com/document/orgapp/event-servicegroup-ticket-create) | 服务群工单创建的推送数据。 |
| [服务群工单申领](https://open.dingtalk.com/document/orgapp/event-servicegroup-ticket-take) | 服务群工单申领的推送数据。 |
| [服务群工单催办](https://open.dingtalk.com/document/orgapp/event-servicegroup-ticket-urge) | 服务群工单催办的推送数据。 |
