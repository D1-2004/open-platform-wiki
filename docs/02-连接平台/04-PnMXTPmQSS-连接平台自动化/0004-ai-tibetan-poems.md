---
title: "AI 藏头诗"
source_url: "https://open.dingtalk.com/document/connection/ai-tibetan-poems"
namespace: "connection"
slug: "ai-tibetan-poems"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "群聊自动化 > 模板教学 > AI 藏头诗"
doc_id: "yCE0jdFXb7"
updated_at: "2025-09-23 19:21:39"
---

> Source: https://open.dingtalk.com/document/connection/ai-tibetan-poems
> Path: 连接平台 / 连接平台自动化 / 群聊自动化 > 模板教学 > AI 藏头诗
> Updated: 2025-09-23 19:21:39

# AI 藏头诗

## **场景介绍**

固定的新人欢迎方式太过单调乏味？不妨让 AI 来为你撰写一首藏头诗，作为独特的欢迎方式！

## **预期效果**

当有新成员加入群时，将自动邀请 AI 为其创作一首藏头诗，同时配置个性化的内容提醒，使新人的欢迎过程更加有趣。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4859964071/p755067.png)

## **操作步骤**

1. 在**流程模板**中选择模板**AI藏头诗**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9753786071/p754865.png)
2. 步骤1为**新人入群时**，**该步骤无需配置。**该节点表示，每当有新人入群时，流程就会被触发。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8753786071/p754867.png)
3. 步骤2为**向 AI 提问，你可以根据需要修改问题内容。**如图所示，模板内容表示，需要AI为人名写一首藏头诗。这个人名就是步骤1「新人入群」的输出数据——入群成员名单。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9753786071/p754869.png)
4. 步骤3为**发送消息到该群组**，**你可以根据需要修改发送内容。**如图所示，模板内容表示，消息内容中包含了藏头诗内容，即**引用**了步骤2**向AI提问时**的**返回内容。**

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8753786071/p754870.png)
5. 单击左上角，用户可以更改流程的标题名称。单击右上角**保存并启用**即可发布流程。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8753786071/p754871.png)
