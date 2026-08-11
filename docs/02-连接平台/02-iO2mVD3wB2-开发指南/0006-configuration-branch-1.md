---
title: "配置分支"
source_url: "https://open.dingtalk.com/document/connection/configuration-branch-1"
namespace: "connection"
slug: "configuration-branch-1"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发连接流 > 编排连接流程 > 配置执行逻辑 > 配置分支"
doc_id: "CZFGdZRcYF"
updated_at: "2025-09-23 19:20:01"
---

> Source: https://open.dingtalk.com/document/connection/configuration-branch-1
> Path: 连接平台 / 开发指南 / 开发连接流 > 编排连接流程 > 配置执行逻辑 > 配置分支
> Updated: 2025-09-23 19:20:01

# 配置分支

本文为您介绍如何为连接流添加分支节点。

## **前提条件**

- 完成[配置触发事件](0004-configure-trigger-events-1.md)流程。

## **操作步骤**

1. 通过点击**“**⊕**”**，选择**分支**，可为该连接流的流程中添加一个分支。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7643786071/p762266.png)
2. 单击条件设置，在表达式中设置分支条件，当条件为true时，将进入该条件分支。

   > **[!NOTE]**
   >
   > - 在同一级流程中，如果同时设置了多个相同的条件分支，那么只会执行其中一个条件（从左到右）。
   > - 分支内，可以单击 **“⊕”** 继续添加连接流节点。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7643786071/p762269.png)

## **后续步骤**

如果你已经配置完成，你可以[保存并调试连接流](0008-save-and-debug-the-connection-flow.md)。

> 如果你需要添加其他节点，请参考：[配置执行动作](0005-configure-execution-actions-1.md)和[配置子流程](0007-configure-sub-processes-1.md)。
