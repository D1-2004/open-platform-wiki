---
title: "电商评价实时同步到群并保存到多维表"
source_url: "https://open.dingtalk.com/document/connection/commerce-synchronizedl-time"
namespace: "connection"
slug: "commerce-synchronizedl-time"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "群聊自动化 > 电商评价实时同步到群并保存到多维表"
doc_id: "DOwCLL6M4d"
updated_at: "2025-09-23 19:21:42"
---

> Source: https://open.dingtalk.com/document/connection/commerce-synchronizedl-time
> Path: 连接平台 / 连接平台自动化 / 群聊自动化 > 电商评价实时同步到群并保存到多维表
> Updated: 2025-09-23 19:21:42

# 电商评价实时同步到群并保存到多维表

「感知到机器人消息时」触发器是一个面向群主和群管理员的高级功能。

## **简介**

电商平台中，客户对商品或者客服小二的评价，对店铺的后续运营动作都有重大参考意义，根据本文档的操作流程，可快速实现千牛后台的评价信息，自动发送到钉钉群，并且将评价保存到多维表，方便后续经营分析。

## **准备工作**

- 拥有一个钉钉内部群，并且是本群的群主或者管理员。
- 创建一个钉钉 AI 表格，并设置该表格的字段，表格字段名称需要与后续配置时保持一致。

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8294813571/p988637.png)
- 在群内添加自定义机器人，步骤参考[创建自定义机器人](../../01-应用开发/01-XOnnmGCTbn-开发指南/0081-custom-bot-creation-and-installation.md)。
- 在千牛商家后台的自动化节点中，配置自定义机器人 WebHook 地址。

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8294813571/p988638.png)

## **预期效果**

预期效果，如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8294813571/p988644.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8294813571/p988645.png)

## **操作步骤**

1. 点击企业内部群右上角设置按钮--点击机器人--点击自动化小助手--新建流程。

   ![iShot_2025-07-22_09](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8294813571/p988649.gif)
2. 触发节点，从右侧面板中的「群内事件」选择「感知到机器人消息时」即可，无需其他配置。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8294813571/p988650.png)
3. 查看出参说明，方便后续引用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8294813571/p988651.png)

   | 输出结果 | 说明 |
   | --- | --- |
   | 机器人名称 | 感知到的机器人名称，如以下示例，机器人名称为：自定义机器人。  image.png |
   | 消息内容 | 机器人发送的消息内容。 |
   | 消息类型 | 机器人发送的消息类型，目前支持三种类型：  - **Text**：纯文本消息 - **Markdown**：Markdown 类型 - **ActionCard**：待跳转 更多详情，请参考[自定义机器人发送消息的消息类型](https://open.dingtalk.com/document/dingstart/custom-bot-send-message-type)。 |
   | 消息发送时间 | 毫秒时间戳**。** |
4. 添加「参数提取」节点，引入第一步机器人消息为待提取的文本。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8294813571/p988652.png)
5. 配置要提取的参数，如下示例，按照需要提取的字段信息进行设置即可。

   > **[!IMPORTANT]**
   >
   > 这里需要提前的字段信息，需要与创建的 AI 表格字段名称保持一致。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8294813571/p988653.png)
6. 把通过大模型提取的结构化数据，写入到钉钉 AI 表格。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8294813571/p988655.png)
7. 【可选】将记录到 AI 表格的信息再发送给某人或者某群。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8294813571/p988656.png)
8. 右上角点击保存和发布。

## **恭喜，你已完成全部配置！**

你已完成本教程的全部内容，可以开始测试。

当千牛商家收到客服被投诉事件时，你的 IM 群内会收到一条推送消息，并且在创建的多维表内可查看该条记录，可以使用多维表的仪表盘功能，进行统计分析。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8294813571/p988663.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8294813571/p988664.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8294813571/p988665.png)
