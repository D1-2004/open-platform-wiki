---
title: "表单加载外部数据源"
source_url: "https://open.dingtalk.com/document/connection/load-external-source"
namespace: "connection"
slug: "load-external-source"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > OA审批 > 操作手册 > 表单加载外部数据源"
doc_id: "RVZBdmvGeG"
updated_at: "2026-01-22 21:28:05"
---

> Source: https://open.dingtalk.com/document/connection/load-external-source
> Path: 连接平台 / 连接器中心 / 官方连接器 > OA审批 > 操作手册 > 表单加载外部数据源
> Updated: 2026-01-22 21:28:05

# 表单加载外部数据源

本教程将实现表单自动加载CRM客户列表，并自动填充客户信息功能。员工在提交表单时，通过输入客户名称关键字实现客户检索，客户列表将填充到表单的单选列表，当用户选择某一具体客户后，到CRM中查询该客户的详细信息，并将信息填充到当前表单的相应字段。

## 教程说明

本例中涉及到两个外部接口：

- **根据名字模糊搜索客户**：入参为客户名，出参为客户列表信息。
- **根据客户ID获取客户详情**：入参为客户id，出参为客户详情信息。

## 前提条件

在开始本教程前，确保你已经完成了以下准备工作：

- 已经完成了钉钉开发者的注册与激活并拥有了子管理员和开发者权限。若尚未完成，请参考[成为钉钉开发者](https://open.dingtalk.com/document/dingstart/dingtalk-developer)。
- 已经成为钉钉专业版用户，若未完成，请参考[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)。
- 已完成连接器和执行动作的创建，若未完成，详情请参考[创建连接器](../02-iO2mVD3wB2-开发指南/0013-create-connector.md)、[添加触发事件](../02-iO2mVD3wB2-开发指南/0014-add-trigger-event-1.md)、[添加执行动作](../02-iO2mVD3wB2-开发指南/0015-add-execution-action-1.md)。

## 新建审批单

在**表单设计**界面，添加流程表单必要参数。

![表单](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7769486661/p381082.png)

- **搜索客户**：单行输入框，用户输入客户名称关键字。
- **客户列表**：单选框，用户接收外部数据源的客户列表。
- **客户名称**：单行输入框，用于接收外部数据源中客户的名称。
- **手机号**：单行输入框，用于接收外部数据源中客户的手机号。
- **年龄**：单行输入框，用于接收外部数据源中客户的年龄。

## 新建搜索客户列表连接器实例

1. 在**表单设计**界面，单击**连接器**，然后单击**配置连接器**。

   ![设计表单](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7769486661/p381080.png)
2. 在配置连接器界面**设置触发条件**下，选择**控件值发生变化时**，绑定触发事件的控件并**确定**，单击**下一步**。

   ![设置触发条件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7769486661/p381084.png)
3. 在配置连接器界面**选择连接器**下，依次选择相应的连接器和执行动作，然后单击**下一步**。

   ![选择连接器](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7769486661/p381086.png)
4. 在配置连接器界面**配置执行动作**下，填写控件的值用于获取数据，并设置获取的数据填充到控件。![值](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7769486661/p381100.png)

   - **客户列表.选项列表.ID列表**：表示选项的key，类似于身份证号码，每一个选项的key唯一，不展示。
   - **客户列表.选项列表.值列表**：表示选项展示的值，可重复。
5. 单击**保存**后，在**表单设计**界面可看到已配置的执行动作。![配置完成](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7769486661/p381109.png)

## 新建查询客户信息连接器实例

1. 在**表单设计**界面，单击**连接器**，然后单击**配置连接器**。

   ![单击连接器-单击配置连接器](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7769486661/p508809.png)
2. 在配置连接器界面**设置触发条件**下，选择**控件值发生变化时**，绑定触发事件的控件并**确定**，单击**下一步**。

   ![设置触发条件-控件值发生变化时](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7769486661/p508807.png)
3. 在配置连接器界面**选择连接器**下，依次选择相应的连接器和执行动作，然后单击**下一步**。

   ![选择连接器-执行动作](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7899486661/p508811.png)
4. 在配置连接器界面**配置执行动作**下，填写控件的值用于获取数据，并设置获取的数据填充到控件。

   > **[!NOTE]**
   >
   > 在**新建****搜索客户列表连接器实例**中已经把**customerId**映射到**客户列表.选项列表.ID列表**，这样就可以获取**客户列表.ID**的值。

   ![出参](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7769486661/p381113.png)

   - **客户列表.ID：**表示获取**客户列表**单选框选中后的ID值。
5. 配置完成后，单击**发布**，发布当前流程表单。

   ![加载外部数据源-保存发布](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7769486661/p508817.png)
