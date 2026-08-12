---
title: "配置执行动作"
source_url: "https://open.dingtalk.com/document/connection/configure-execution-actions-1"
namespace: "connection"
slug: "configure-execution-actions-1"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发连接流 > 编排连接流程 > 配置执行动作"
doc_id: "0uCY2xEYK6"
updated_at: "2026-07-27 17:36:51"
---

> Source: https://open.dingtalk.com/document/connection/configure-execution-actions-1
> Path: 连接平台 / 我的连接 / 开发连接流 > 编排连接流程 > 配置执行动作
> Updated: 2026-07-27 17:36:51

# 配置执行动作

在连接流中，执行动作是完成某些业务处理的节点，本文将介绍如何在流程中添加执行动作节点。

## **前提条件**

- 完成[配置触发事件](0002-configure-trigger-events-1.md)流程。

## **操作步骤**

1. 单击**执行动作**节点，在连接流配置界面右侧弹出执行动作配置页。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2306584871/p760004.png)
2. 在连接器选择页面，浏览并找到你需要的连接器，并单击选中它。选定连接器后，系统会在“执行动作”页面，自动显示该连接器提供的所有可用执行动作。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2306584871/p760008.png)
3. 选择需要的执行动作，进入配置参数页面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2306584871/p760011.png)
4. 配置参数，对字段进行参数配置时，有三种映射方式，默认为引用值：

   | **映射方式** | **说明** |
   | --- | --- |
   | 引用值 | 单击字段配置框，在参数配置页左上方弹出上文参数节点，选择对应字段即可。  image |
   | 输入值 | 将映射方式设置为**输入值**，并输入文本内容。  image |
   | 表达式 | 将映射类型设置为**表达式**，单击配置框输入相应表达式即可。  image |

   配置完成后，如果你需要配置多个执行动作，可参考上述流程继续进行配置。

## **后续步骤**

- 如果你已经配置完成，你可以[保存并调试连接流](0005-save-and-debug-the-connection-flow.md)。
- 如果你需要添加执行逻辑，请参考：[配置执行逻辑](0004-configuration-branch-1.md)。

## **常见问题**

- **如何添加执行动作？**

  进入连接流程编排页面，单击 **“⊕”** > **请选择连接器和执行动作**。

  > **[!NOTE]**
  >
  > - 连接流程默认包含一个执行动作节点。
  > - 一个连接流程可以包含多个执行动作节点。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2306584871/p759997.png)
