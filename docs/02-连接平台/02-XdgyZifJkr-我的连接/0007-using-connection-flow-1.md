---
title: "使用连接流"
source_url: "https://open.dingtalk.com/document/connection/using-connection-flow-1"
namespace: "connection"
slug: "using-connection-flow-1"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发连接流 > 使用连接流"
doc_id: "qVNgOzCWvW"
updated_at: "2026-07-27 17:36:59"
---

> Source: https://open.dingtalk.com/document/connection/using-connection-flow-1
> Path: 连接平台 / 我的连接 / 开发连接流 > 使用连接流
> Updated: 2026-07-27 17:36:59

# 使用连接流

连接流配置完成并发布后，就可以使用您创建好的连接流。本文将为您介绍如何去使用连接流。

## **前提条件**

完成[发布连接流](0006-publish-connection-flow.md)的流程。

## **操作步骤**

1. 单击**我的连接** > **我的连接流**，在连接流列表中找到已发布的连接流，并确保流程为已启用状态。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9795774871/p762306.png)
2. 触发连接流。当连接流的触发事件发生后，流程将开始运行。

   > **[!NOTE]**
   >
   > - 你可以主动触发事件：
   >
   >   - 当你触发事件选择了**官方连接器** > **通讯录** > **修改部门**，当你企业的部门信息发生变更后，流程将会监听到该变更事件，从而触发流程运行，并执行后续执行动作。
   >   - 当你触发事件选择了**内置工具** > **webhook**，你可以复制 webhook 地址，并请求 URL 触发该连接流。
   > - 被动触发：
   >
   >   - 当你触发事件选择了**内置工具** > **定时触发**，当到达你设置的时间，将会执行该连接流。
   >   - 当你触发事件选择了**内置工具 > 子流程**，使用了该子流程的流被触发后，将会执行当前子流程。
3. 流程执行后，你可以查看执行记录。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9795774871/p762309.png)
