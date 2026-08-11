---
title: "智能分配任务"
source_url: "https://open.dingtalk.com/document/connection/intelligent-task-allocation"
namespace: "connection"
slug: "intelligent-task-allocation"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "群聊自动化 > 模板教学 > 智能分配任务"
doc_id: "bOHwVAXfxX"
updated_at: "2025-09-23 19:21:40"
---

> Source: https://open.dingtalk.com/document/connection/intelligent-task-allocation
> Path: 连接平台 / 连接平台自动化 / 群聊自动化 > 模板教学 > 智能分配任务
> Updated: 2025-09-23 19:21:40

# 智能分配任务

## **场景介绍**

需求太过零散和杂乱？

反复切换应用太麻烦？

自动化小助手，帮你实现**一句话分配Teambition任务**！

## **预期效果**

说一句话，AI会自动帮你**分析需求内容**，**新建一个Teambition任务**，并自动**提示创建成功**。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9859964071/p755073.png)

## **操作步骤**

1. 在**流程模板**中选择模板**智能任务**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3853786071/p754929.png)
2. 步骤1为**机器人被@时**，可根据需要修改配置。如图所示，模板配置了所有成员、所有消息均可触发，也就是任何人发送一条@自动化小助手的消息，都会触发流程。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3853786071/p754930.png)
3. 步骤2为**向AI提问**，你可以根据需要修改配置。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4853786071/p754931.png)

   1. **填写问题**。如图所示，模板内容表示，需要AI分析步骤1的输出数据——消息内容，从而提取出几个关键信息：**是否创建任务、任务名称。**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3853786071/p754932.png)
   2. **设置AI的回答格式**。如图所示，模板内容表示，需要AI以固定的JSON结构回答问题，并以「返回值示例」作为参考，即需要返回**是否创建任务、任务名称这两个字段的内容。**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3853786071/p754933.png)
4. 步骤3为**条件。**只有满足你设定的条件时，流程才会继续往下执行，否则流程将在此步骤终止。如图所示，模板中条件设置为了“是否创建任务”等于“是”时，流程才会继续往下执行。其中，“是否创建任务”是步骤2**向 AI 提问**的输出数据，即 AI 返回的内容答案。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3853786071/p754935.png)
5. 步骤4为**创建任务**，如图所示，新建任务的标题为步骤2**向 AI 提问**的输出数据—任务名称。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3853786071/p754936.png)
6. 步骤5为**发送消息到该群组**，可根据需要修改消息内容。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3853786071/p754938.png)
7. 单击左上角，用户可以更改流程的标题名称。单击右上角**保存并启用**即可发布流程。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3853786071/p754939.png)
