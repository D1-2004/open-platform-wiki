---
title: "发送文本消息到企业群"
source_url: "https://open.dingtalk.com/document/connection/send-message-enterprise"
namespace: "connection"
slug: "send-message-enterprise"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 使用教程 > 消息通知 > 发送文本消息到企业群"
doc_id: "qMA0g708DG"
updated_at: "2026-05-19 19:46:14"
---

> Source: https://open.dingtalk.com/document/connection/send-message-enterprise
> Path: 连接平台 / 连接器中心 / 官方连接器 > 使用教程 > 消息通知 > 发送文本消息到企业群
> Updated: 2026-05-19 19:46:14

# 发送文本消息到企业群

## **简介**

消息通知是以企业的名义推送到企业内部群，例如生日祝福、入职提醒等。可以发送文本、语音、链接等。本文以文本消息为例。

## 准备工作

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 已经创建了一个[企业内部应用](../../01-应用开发/01-XOnnmGCTbn-开发指南/0007-create-application.md)。

## **预期效果**

通过连接平台，编排连接流，完成消息通知文本消息的发送。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6291769861/p694916.png)

## **步骤一：创建连接器**

- 如果无连接器，详情参见[创建连接器](../02-XdgyZifJkr-我的连接/0010-create-connector.md)。
- 如果已有连接器，可直接使用已有连接器。

## **步骤二：配置触发事件**

1. 选择创建的连接器进入详情页面，然后依次选择**触发事件 > 创建触发事件**。![连接器-创建触发事件..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7984055861/p674345.png)
2. 填写触发事件的基础信息。
3. 在模型配置界面下，配置**触发事件入参**参数，然后单击**下一步**。

   ![设置文本消息字段.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0163548861/p689603.png)
4. 在调试界面下，填写**触发事件入参**参数，然后单击**立即调试**。

   ![立即调试-工作通知文本内容.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0163548861/p689610.png)
5. 调试完成之后，选择**发布**。

   ![发布文本消息text.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0163548861/p689613.png)

## **步骤三：创建连接流**

1. [创建连接流](../02-XdgyZifJkr-我的连接/0001-create-a-connection-flow-1.md)，并完善连接流基本信息。
2. 配置触发事件：

   1. 选择自建连接器。

      > **[!NOTE]**
      >
      > 选择步骤一中创建的自建连接器。

      ![触发事件选择-消息通知文本消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6291769861/p694943.png)
   2. 选择触发事件。

      > **[!NOTE]**
      >
      > 选择步骤二中发布的触发事件。

      ![触发事件-消息通知文本消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6291769861/p694934.png)
   3. 完成配置。

      ![完成-消息通知文本消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6291769861/p694936.png)
3. 配置执行动作：

   1. 选择官方连接器。

      ![消息通知文本消息-选择连接器.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6291769861/p694938.png)
   2. 选择执行动作。

      ![发送消息到企业群-文本消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6291769861/p694945.png)
   3. 配置参数。
   4. 测试并预览：

      1. 输入测试值。

         ![测试并预览-消息通知文本消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6291769861/p694952.png)
      2. 完成测试。

         ![完成测试-消息通知文本消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6291769861/p694959.png)

         此时可以在企业群内收到文本消息。
   5. 发布连接流。

      ![发布-消息通知文本消息连接流.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6291769861/p694963.png)

## 恭喜，你已完成全部配置！

你已完成本教程的全部内容，可以通过以下方式进行体验。

1. 获取触发事件[方式一（推荐）：通过Webhook地址触发事件](../02-XdgyZifJkr-我的连接/0013-using-connectors-1.md#636e0c4a67u8r)地址。
2. 根据Webhook地址，体验工作通知消息发送。

![消息通知文本消息发送.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6291769861/p694966.png)
