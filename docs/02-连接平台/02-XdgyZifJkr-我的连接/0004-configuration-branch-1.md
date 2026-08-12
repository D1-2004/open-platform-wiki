---
title: "配置执行逻辑"
source_url: "https://open.dingtalk.com/document/connection/configuration-branch-1"
namespace: "connection"
slug: "configuration-branch-1"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发连接流 > 编排连接流程 > 配置执行逻辑"
doc_id: "CZFGdZRcYF"
updated_at: "2026-07-27 17:36:21"
---

> Source: https://open.dingtalk.com/document/connection/configuration-branch-1
> Path: 连接平台 / 我的连接 / 开发连接流 > 编排连接流程 > 配置执行逻辑
> Updated: 2026-07-27 17:36:21

# 配置执行逻辑

本文为您介绍如何为连接流添加分支节点。

## **前提条件**

- 完成[配置触发事件](0002-configure-trigger-events-1.md)流程。

## **配置分支**

1. 通过点击**“**⊕**”**，选择**条件分支**，可为该连接流的流程中添加一个分支。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7992774871/p762266.png)
2. 单击条件设置，在表达式中设置分支条件，当条件为true时，将进入该条件分支。

   > **[!NOTE]**
   >
   > - 在同一级流程中，如果同时设置了多个相同的条件分支，那么只会执行其中一个条件（从左到右）。
   > - 分支内，可以单击 **“⊕”** 继续添加连接流节点。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7992774871/p762269.png)

## **配置子流程**

1. 通过单击**“**⊕**”**，选择**调用子流程**，可为该连接流的流程中添加一个子流程节点。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4306584871/p762272.png)
2. 单击**请设置子流程**，在右侧弹窗中，选择需要添加的子流程。选择完成后跳到子流程的参数配置界面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4306584871/p762273.png)
3. 配置子流程参数。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4306584871/p762275.png)

## **后续步骤**

- 如果你已经配置完成，你可以[保存并调试连接流](0005-save-and-debug-the-connection-flow.md)。
- 如果你需要添加其他节点，请参考：[配置执行动作](0003-configure-execution-actions-1.md)。
