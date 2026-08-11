---
title: "智能查询内部数据"
source_url: "https://open.dingtalk.com/document/connection/intelligent-query-of-internal-data"
namespace: "connection"
slug: "intelligent-query-of-internal-data"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "群聊自动化 > 模板教学 > 智能查询内部数据"
doc_id: "74rQfGzaCL"
updated_at: "2025-09-23 19:21:40"
---

> Source: https://open.dingtalk.com/document/connection/intelligent-query-of-internal-data
> Path: 连接平台 / 连接平台自动化 / 群聊自动化 > 模板教学 > 智能查询内部数据
> Updated: 2025-09-23 19:21:40

# 智能查询内部数据

## **场景介绍**

登录多个系统查看数据太麻烦？

自动化小助手帮你实现**一句话连接内部系统，随时查询内部数据**！

## **预期效果**

在群内提出问题后，AI 将自动帮助你分析查询对象，并发起HTTP请求，查询内部系统的详细信息，然后将其发送到群内。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7859964071/p755070.png)

## **操作步骤**

1. 在**流程模板**中选择模板**AI查数据**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2853786071/p754904.png)
2. 步骤1为**机器人被@时**，可根据需要修改配置。如图所示，模板配置了所有成员、所有消息均可触发，也就是任何人发送一条@自动化小助手的消息，都会触发流程。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2853786071/p754905.png)
3. 步骤2为**向 AI 提问**，你可以根据需要修改配置。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1853786071/p754908.png)

   1. **填写问题**：如图所示，模板内容表示，需要 AI 分析步骤1的输出数据——消息内容，从而提取出几个关键信息：**是否询问商品信息、商品名称。**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2853786071/p754909.png)
   2. **设置AI的回答格式**。如图所示，模板内容表示，需要AI以固定的JSON结构回答问题，并以**返回值示例**作为参考，即需要返回**是否询问商品信息、商品名称这两个字段的内容。**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2853786071/p754911.png)
4. 步骤3为**条件。**只有满足你设定的条件时，流程才会继续往下执行，否则流程将在此步骤终止。如图所示，模板中条件设置为了“是否询问商品信息”等于“是”时，流程才会继续往下执行。其中，“是否询问商品信息”是步骤2**向 AI 提问**的输出数据，即 AI 返回的内容答案。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1853786071/p754913.png)
5. 步骤4为**发起HTTP请求**，你可以修改配置从而获取内部系统的数据。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1853786071/p754914.png)
6. 步骤5为**发送消息到该群组**，可根据需要修改消息内容。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1853786071/p754915.png)
7. 单击左上角，用户可以更改流程的标题名称。单击右上角**保存并启用**即可发布流程。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2853786071/p754917.png)
