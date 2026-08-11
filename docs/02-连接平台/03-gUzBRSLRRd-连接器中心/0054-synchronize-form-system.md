---
title: "表单数据同步到外部系统"
source_url: "https://open.dingtalk.com/document/connection/synchronize-form-system"
namespace: "connection"
slug: "synchronize-form-system"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > OA审批 > 操作手册 > 表单数据同步到外部系统"
doc_id: "9tRM8rMcho"
updated_at: "2026-01-22 21:27:14"
---

> Source: https://open.dingtalk.com/document/connection/synchronize-form-system
> Path: 连接平台 / 连接器中心 / 官方连接器 > OA审批 > 操作手册 > 表单数据同步到外部系统
> Updated: 2026-01-22 21:27:14

# 表单数据同步到外部系统

在本教程中，将实现在入库审批单中添加数据同步连接器节点，当入库审批单完成审批后，在ERP对应仓库、商品条目下实现商品数目变更。

## 教程说明

本教程中涉及到一个外部接口：
**同步出库信息**：入参为出库数量（**amount**）、商品名（**goodName**）、商品编号（**goodId**）和入库地点（**warehouse**）。

![接口图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8347956661/p380928.png)

## 前提条件

在开始本教程前，确保你已经完成了以下准备工作：

- 已经完成了钉钉开发者的注册与激活并拥有了子管理员和开发者权限。若尚未完成，请参考[成为钉钉开发者](https://open.dingtalk.com/document/dingstart/dingtalk-developer)。
- 已经成为钉钉专业版用户，若未完成，请参考[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)。
- 已完成连接器和执行动作的创建，若未完成，详情请参考[创建连接器](../02-iO2mVD3wB2-开发指南/0013-create-connector.md)、[添加触发事件](../02-iO2mVD3wB2-开发指南/0014-add-trigger-event-1.md)、[添加执行动作](../02-iO2mVD3wB2-开发指南/0015-add-execution-action-1.md)。

## 新建审批单

在**表单设计界面**，设计并添加OA审批表单控件。

![审批表单](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7347956661/p380924.png)

- **商品名**：单行输入框，用于输入商品名称。
- **商品编码**：单行输入框，用于输入商品编码。
- **商品数量**：数字输入框，用于输入商品数量。
- **仓库**：单行输入框，用于输入仓库名称。

## 添加连接器节点

在**流程设计**界面添加连接器节点，当前节点通过后，将进入该连接器节点，用户可以自定义该节点名称。

![添加连接器节点](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8347956661/p380933.png)

## 选择执行动作

在连接器模块下，选择相应的连接器和执行动作。

![选择执行动作](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7347956661/p380934.png)

## 配置执行动作

将**仓库**、**商品名称**、**商品数量**、**商品编码**接口参数与表单字段完成数据映射配置。

> **[!NOTE]**
>
> 本示例中流程引擎无需等待数据同步结果，**是否开启同步调用**保持默认关闭即可。

![配置执行动作](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7347956661/p380938.png)

## 保存发布

配置完成后，单击**保存**并**发布**审批单。
