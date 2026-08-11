---
title: "用户离职审批通过后删除用户"
source_url: "https://open.dingtalk.com/document/connection/delete-resignation-approval"
namespace: "connection"
slug: "delete-resignation-approval"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 通讯录 > 使用教程 > 用户离职审批通过后删除用户"
doc_id: "h2Q0cKRvRZ"
updated_at: "2026-05-19 16:01:52"
---

> Source: https://open.dingtalk.com/document/connection/delete-resignation-approval
> Path: 连接平台 / 连接器中心 / 官方连接器 > 通讯录 > 使用教程 > 用户离职审批通过后删除用户
> Updated: 2026-05-19 16:01:52

# 用户离职审批通过后删除用户

本文档介绍通过连接平台实现员工离职后删除该员工。

## **准备工作**

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 已开通[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)。

## **操作步骤**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击**开放能力** > **连接平台**，进入连接平台页面。
2. 单击我的连接 > 我的连接流 > 创建连接流。
3. 配置**实例通过（高阶版）**触发事件：

   1. 单击**触发事件** > **官方连接器** > **审批**，选择**实例通过（高阶版）**。
   2. 配置参数，请选择流程表单：

      1. 选择 **OA 审批**应用。
      2. 选择你企业的离职审批单。
4. 配置**获取单个审批示例详情**执行动作：

   1. 单击**执行动作** > **官方连接器** > **审批，**选择**获取单个审批实例详情**。
   2. 配置参数，设置审批实例ID。

      ![审批示例ID.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6151640071/p737386.png)
5. 配置**删除用户**执行动作：

   1. 单击“⊕”，添加执行动作。
   2. 单击**执行动作** > **官方连接器** > **通讯录，**选择**删除用户**。
   3. 配置参数，设置员工id，选择**返回结果.返回结果.发起人的userId**。

      ![用户id.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6151640071/p737392.png)

## 恭喜，你已完成全部配置！

你已完成本教程的全部内容，可以体验员工提交离职审批单通过后同步在企业通讯录中删除该员工。
