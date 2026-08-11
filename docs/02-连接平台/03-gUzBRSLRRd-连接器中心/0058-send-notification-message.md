---
title: "发送工作通知文本消息"
source_url: "https://open.dingtalk.com/document/connection/send-notification-message"
namespace: "connection"
slug: "send-notification-message"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 工作通知 > 使用教程 > 发送工作通知文本消息"
doc_id: "bwEalLyeAl"
updated_at: "2026-05-19 19:46:11"
---

> Source: https://open.dingtalk.com/document/connection/send-notification-message
> Path: 连接平台 / 连接器中心 / 官方连接器 > 工作通知 > 使用教程 > 发送工作通知文本消息
> Updated: 2026-05-19 19:46:11

# 发送工作通知文本消息

## **简介**

工作通知消息是以某个应用的名义推送到员工的工作通知消息，例如生日祝福、入职提醒等。可以发送文本、语音、链接等消息类型，本文以工作通知文本消息为例。

查看更多执行动作

## 准备工作

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 已经创建了一个[企业内部应用](../../01-应用开发/01-XOnnmGCTbn-开发指南/0007-create-application.md)。

## **预期效果**

通过连接平台，编排连接流，完成工作通知文本消息的发送。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4788548861/p689801.png)

## **视频展示**

[](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20230705/hgrt/文本内容最终版.mp4)

## **步骤一：创建连接器**

- 如果无连接器，详情参见[创建连接器](../02-iO2mVD3wB2-开发指南/0013-create-connector.md)。
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

1. [创建连接流](../02-iO2mVD3wB2-开发指南/0002-create-a-connection-flow-1.md)，并完善连接流基本信息。
2. 配置触发事件：

   1. 选择自建连接器。

      > **[!NOTE]**
      >
      > 选择步骤一中创建的自建连接器。

      ![选择连接器-工作通知文本.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0163548861/p689676.png)
   2. 选择触发事件。

      > **[!NOTE]**
      >
      > 选择步骤二中发布的触发事件。

      ![选择触发事件-工作通知文本消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9063548861/p689678.png)
   3. 完成配置。

      ![完成配置-工作通知文本消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9063548861/p689680.png)
3. 配置执行动作：

   1. 选择官方连接器。

      ![选择执行动作-工作通知文本消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0163548861/p689687.png)
   2. 选择执行动作。

      ![选择执行动作-文本消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9063548861/p689692.png)
   3. 配置参数：

      1. 单击**点击进行配置。**
      2. 出入参配置：

         - [微应用id](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)：选择输入值。
         - 接收者的用户userid列表：选择输入值，通过选人组件，完成用户填充。
         - 文本消息。

           ![文本消息-工作通知文本消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4788548861/p689749.png)
   4. 测试并预览：

      1. 输入测试值。

         ![输入测试值-文本消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4788548861/p689754.png)
      2. 完成测试。

         ![完成配置-文本消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4788548861/p689777.png)

         此时可以收到工作通知文本消息。
   5. 发布连接流。

      ![发布连接流-文本消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4788548861/p689783.png)

## 恭喜，你已完成全部配置！

你已完成本教程的全部内容，可以通过以下方式进行体验。

1. 获取触发事件[方式一（推荐）：通过Webhook地址触发事件](../02-iO2mVD3wB2-开发指南/0016-using-connectors-1.md#636e0c4a67u8r)地址。
2. 根据Webhook地址，体验工作通知消息发送。

![工作通知文本发送.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4788548861/p689798.png)
