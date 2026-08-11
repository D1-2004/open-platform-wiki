---
title: "步骤二：服务商发起定制工作台委托"
source_url: "https://open.dingtalk.com/document/services/step-2-a-service-provider-initiates-a-custom-console-commission-1"
namespace: "services"
slug: "step-2-a-service-provider-initiates-a-custom-console-commission-1"
group: "应用开发"
tab: "平台服务"
breadcrumb: "合作指南 > 产品方案商 > 定制业务的合作指引 > 自定义工作台开发流程 > 步骤二：服务商发起定制工作台委托"
doc_id: "TJNeyVGqzO"
updated_at: "2025-09-23 19:22:10"
---

> Source: https://open.dingtalk.com/document/services/step-2-a-service-provider-initiates-a-custom-console-commission-1
> Path: 应用开发 / 平台服务 / 合作指南 > 产品方案商 > 定制业务的合作指引 > 自定义工作台开发流程 > 步骤二：服务商发起定制工作台委托
> Updated: 2025-09-23 19:22:10

# 步骤二：服务商发起定制工作台委托

当企业有定制工作台需求时，需要先联系产品方案商。产品方案商在开发者后台生成委托单，然后企业做为客户完成授权后，服务商方可进行工作台的定制开发。

> **[!IMPORTANT]**
>
> 只有产品方案商身份可以开通定制工作台服务权限。无论你是服务商身份为客户提供服务，还是客户身份为自己的组织提供服务，都需要先成为钉钉产品方案商。相关流程，请参见[入驻成为产品方案商](0028-become-an-application-service-provider.md)。

1. 服务商登录[开发者后台](https://open-dev.dingtalk.com/)，依次选择**定制服务 > 工作台定制 > 定制工作台**，单击**生成委托单**，生成定制工作台委托单链接。

   > **[!IMPORTANT]**
   >
   > 客户在开发者后台的“**应用开发** > **工作台**”模块进行定制工作台委托的入口已下线，现统一使用客户移动端委托入口。

   ![服务商发起定制工作台委托](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8637175261/p262346.png)

   工作台项目名称默认生成（可修改），格式为“工作台项目{日期时间戳}”，点击**复制链接**后，包含工作台名称的定制委托单链接即可生成。你可以将该链接分发给需要委托的客户对接人，如下图所示：

   ![服务商发起定制工作台委托2 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9202031161/p229876.png)

   页面链接的组成和创建方式如下：

   1. 委托单链接模板：

      ```
      点击查看委托详情，选择委托组织并完成委托。
      dingtalk://dingtalkclient/action/open_mini_app?miniAppId=2019080266076709&page=pages%2Ftemplate-create-apply%2Findex%3FserviceCorpId%3D{serviceCorpId}%26worktabName%3D{worktabName}%26cardMessageBizType%3DdingPortalEntrust%26serviceStaffId%3D{serviceStaffId}
      ```
   2. 链接参数说明：

      | 参数 | 说明 |
      | --- | --- |
      | {serviceCorpId} | 服务商CorpId，根据当前登录的服务商组织自行生成。 |
      | {worktabName} | 工作台名称，点击生成委托单时填写的工作台项目名称。  **[!NOTE]**  该字段不会透出展示给客户，仅在客户完成委托后服务商将在后台看到工作台名称。 |
      | {serviceStaffId} | 服务商组织内的服务小二，根据当前登录并点击生成委托单的人自动生成  后续该工作台服务状态变化相关的通知、服务群拉群等都会通过该服务小二。 |
2. 客户对接人收到委托单链接后，打开页面。

   1. 若对接人为其组织管理员，则可选择委托组织，填写相关信息，勾选确认[《委托定制服务协议》](https://page.dingtalk.com/wow/dingtalk/act/dingzhixieyi?wh_biz=tm)，提交后即对服务商完成了定制工作台的委托。

      > **[!IMPORTANT]**
      >
      > 若同一个客户组织多次尝试委托同一个服务商时，此时将请客户进行二次确认，确认再次对服务商进行委托。

      ![p229878](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3514031161/p230694.png)
   2. 若对接人非其组织管理员，则可将委托单转发给其组织管理员，组织管理员完成定制工作台的委托。
3. 客户完成对该服务商的委托后，客户可登录[开发者后台](https://open-dev.dingtalk.com/)，选择**应用开发>工作台**，后台可查询到该委托记录，工作台状态为“方案配置中”，此时可联系服务商进行需求沟通。

   ![服务商方案咨询中](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9202031161/p229887.png)
4. 客户可单击**撤回委托单**，撤回后，服务商将无法进行后续服务的提供。
