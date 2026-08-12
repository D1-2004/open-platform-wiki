---
title: "表单提交时校验"
source_url: "https://open.dingtalk.com/document/connection/verification-submission"
namespace: "connection"
slug: "verification-submission"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 使用教程 > OA审批 > 操作手册 > 表单提交时校验"
doc_id: "xuXMpOydgg"
updated_at: "2026-01-22 21:26:11"
---

> Source: https://open.dingtalk.com/document/connection/verification-submission
> Path: 连接平台 / 连接器中心 / 官方连接器 > 使用教程 > OA审批 > 操作手册 > 表单提交时校验
> Updated: 2026-01-22 21:26:11

# 表单提交时校验

本教程将实现员工提交表单时自动到ERP校验库存功能，如果仓库没有足够库存，将阻断员工提交审批单。

## 教程说明

本教程中涉及到一个外部接口：

查询库存：入参为商品名称和出库数量，出参为库存是否足够和提示信息。库存是否足够字段必须为boolean类型，提示信息字段必须为String类型。

> **[!NOTE]**
>
> 如果外部系统接口不满足该规范，可以通过子流程编排实现。

![接口图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9728486661/p380946.png)

## 前提条件

在开始本教程前，确保你已经完成了以下准备工作：

- 已经完成了钉钉开发者的注册与激活并拥有了子管理员和开发者权限。若尚未完成，请参考[成为钉钉开发者](https://open.dingtalk.com/document/dingstart/dingtalk-developer)。
- 已经成为钉钉专业版用户，若未完成，请参考[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)。
- 已完成连接器和执行动作的创建，若未完成，详情请参考[创建连接器](../02-XdgyZifJkr-我的连接/0010-create-connector.md)、[添加触发事件](../02-XdgyZifJkr-我的连接/0011-add-trigger-event-1.md)、[添加执行动作](../02-XdgyZifJkr-我的连接/0012-add-execution-action-1.md)。

## 新建审批单

在**表单设计界面**，设计并添加OA审批表单控件。

![审批单](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9728486661/p380948.png)

- **商品名**：单行输入框，用于输入商品名称。
- **出库数量**：数字输入框，用于输入商品数量。

## 新建连接器实例

### 选择触发条件

选择**表单提交时验证**，然后单击**下一步。**

> **[!NOTE]**
>
> 本教程实现用户提交表单时到外部系统校验，所以触发条件为**表单提交时验证**。

![选择触发条件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0828486661/p380950.png)

### 选择执行动作

在连接器模块下，选择相应的连接器和执行动作，然后单击**下一步**。

![执行动作](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0828486661/p380952.png)

### 配置执行动作

在配置连接器界面**配置执行动作**下，填写控件的值用于校验数据，并设置获取的数据填充到控件。

![配置入参](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0828486661/p380953.png)

​**校验结果**和**校验错误信息**是系统默认的两个字段：

- **校验结果**：用来阻止表单提交的字段，必须为boolean类型。true为校验通过可以提交表单；false为校验不通过阻止表单提交。
- **校验错误信息**：用来提示校验不通过时提示字段，必须为String类型。校验结果为true时不会弹出，校验结果为false时，阻止表单提交并弹出校验错误信息。

### 保存发布

连接器配置完成后，单击**保存**并**发布**审批表单。

![发布](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9728486661/p380957.png)
