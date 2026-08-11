---
title: "智能需求收集"
source_url: "https://open.dingtalk.com/document/connection/intelligent-demand-collection"
namespace: "connection"
slug: "intelligent-demand-collection"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "群聊自动化 > 模板教学 > 智能需求收集"
doc_id: "czArxl4PN3"
updated_at: "2025-09-23 19:21:39"
---

> Source: https://open.dingtalk.com/document/connection/intelligent-demand-collection
> Path: 连接平台 / 连接平台自动化 / 群聊自动化 > 模板教学 > 智能需求收集
> Updated: 2025-09-23 19:21:39

# 智能需求收集

## **场景介绍**

在客户服务群中，遇到太多问题没有时间逐一答疑回复？

在反馈收集群中，面对太多反馈需求而无暇进行分析和保存？

AI 客服可以帮助您解决这些问题！

## **预期效果**

客户在群里进行提出建议反馈，**AI自动进行分析**，智能**总结满意程度、改进方向等关键信息**，并给出**智能官方回复**，同时将这些信息**备份到多维表**中。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9753786071/p754880.png)

## **操作步骤**

1. 在**流程模板**中选择模板**AI收集**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0853786071/p754881.png)
2. 步骤1为**机器人被@时**，可根据需要修改配置。如图所示，模板配置了所有成员、所有消息均可触发，也就是任何人发送一条@自动化小助手的消息，都会触发流程。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0853786071/p754882.png)
3. 步骤2为**向AI提问**，你可以根据需要修改配置。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0853786071/p754883.png)

   1. **填写问题**：如图所示，模板内容表示，需要AI分析步骤1的输出数据——消息内容，从而提取出几个关键信息：**是否为客服场景、现状问题、改进的方向、官方回应、满意程度**。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0853786071/p754884.png)
   2. **设置AI的回答格式**。如图所示，模板内容表示，需要AI以固定的JSON结构回答问题，并以**返回值示例**作为参考，即需要返回**是否为客服场景、现状问题、改进的方向、官方回应、满意程度这五个字段的内容。**![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9753786071/p754886.png)
4. 步骤3为**条件。**只有满足你设定的条件时，流程才会继续往下执行，否则流程将在此步骤终止。如图所示，模板中条件设置为了“是否为客服场景”等于“是”时，流程才会继续往下执行。其中，“是否为客服场景”是步骤2**向 AI 提问**的输出数据，即AI返回的内容答案。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0853786071/p754887.png)
5. 步骤4为**发送消息到该群组**，**你可以根据需要修改发送内容。**如图所示，模板内容表示，消息内容中包含了官方回应内容，即**引用**了步骤2**向AI提问时**的**返回内容。**![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1853786071/p754888.png)
6. 步骤5为**新增记录**，支持向已有的多维表中新增一条数据记录进行备份。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0853786071/p754889.png)

   1. **选择数据表**。请输入关键词**搜索一张已有的多维表**，并选择多维表中的数据表。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1853786071/p754891.png)
   2. **设置字段内容**。多维表中的字段标题将一一显示在流程配置界面，请进行字段内容的配置，比如“反馈原话”字段就配置步骤1的输出数据——消息内容，“AI回应”字段配置步骤2的输出数据——官方回应……（目前仅支持文本、数字字段的内容配置）

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0853786071/p754893.png)

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0853786071/p754895.png)
7. 单击左上角，用户可以更改流程的标题名称。单击右上角**保存并启用**即可发布流程。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0853786071/p754897.png)
