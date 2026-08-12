---
title: "机器人发送单聊文本消息"
source_url: "https://open.dingtalk.com/document/connection/robot-sends-message"
namespace: "connection"
slug: "robot-sends-message"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 使用教程 > 机器人 > 机器人发送单聊文本消息"
doc_id: "YOQB4WErh9"
updated_at: "2026-07-30 09:19:02"
---

> Source: https://open.dingtalk.com/document/connection/robot-sends-message
> Path: 连接平台 / 连接器中心 / 官方连接器 > 使用教程 > 机器人 > 机器人发送单聊文本消息
> Updated: 2026-07-30 09:19:02

# 机器人发送单聊文本消息

## **简介**

机器人发送单聊消息是以某个机器人的名义推送到与员工的聊天框内，例如生日祝福、入职提醒等。可以发送文本、语音、链接等消息类型，本文以机器人发送单聊文本消息为例。

## 准备工作

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 已经创建了一个[企业内部应用](../../01-应用开发/01-XOnnmGCTbn-开发指南/0007-create-application.md)。

## 预期效果

通过连接平台，编排连接流，完成机器人单聊文本消息的发送。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6697240961/p698155.png)

## 步骤一：创建连接器

- 如果无连接器，详情参见[创建连接器](../02-XdgyZifJkr-我的连接/0010-create-connector.md)。
- 如果已有连接器，可直接使用已有连接器。

## 步骤二：配置触发事件

1. 选择创建的连接器进入详情页面，然后依次选择**触发事件 > 创建触发事件**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6697240961/p698157.png)
2. 填写触发事件的基础信息。
3. 在模型配置界面下，配置**触发事件入参**参数，然后单击**下一步**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6697240961/p698158.png)
4. 在调试界面下，填写**触发事件入参**参数，然后单击**立即调试**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6697240961/p698159.png)
5. 调试完成之后，选择**发布**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6697240961/p698160.png)

## 步骤三：创建连接流

1. [创建连接流](../02-XdgyZifJkr-我的连接/0001-create-a-connection-flow-1.md)，并完善连接流基本信息。
2. 配置触发事件：

   1. 选择自建连接器。

      > **[!NOTE]**
      >
      > 选择步骤一中创建的自建连接器。

      ![机器人-选择官方连接器.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6697240961/p698163.png)
   2. 选择触发事件。

      > **[!NOTE]**
      >
      > 选择步骤二中发布的触发事件。

      ![单聊文本消息-触发事件.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6697240961/p698174.png)
   3. 完成配置。

      ![完成配置-触发条件.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6697240961/p698176.png)
3. 配置执行动作：

   1. 选择官方连接器。

      ![机器人-官方连接器.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6697240961/p698183.png)
   2. 选择执行动作。

      ![文本消息-单聊.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6697240961/p698339.png)
   3. 配置参数。
   4. 测试并预览：

      1. 输入测试值。

         ![单聊-测试.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6697240961/p698356.png)
      2. 完成测试。

         ![完成测试-单聊.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6697240961/p698362.png)

         此时，可以在与机器人聊天会话内查看信息了。
   5. 发布连接流。

      ![发布-单聊.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6697240961/p698366.png)

## 恭喜，你已完成全部配置！

你已完成本教程的全部内容，可以通过以下方式进行体验。

1. 获取触发事件[方式一（推荐）：通过Webhook地址触发事件](../02-XdgyZifJkr-我的连接/0013-using-connectors-1.md#636e0c4a67u8r)地址。
2. 根据Webhook地址，体验工作通知消息发送。

![发送消息-单聊.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6697240961/p698368.png)
