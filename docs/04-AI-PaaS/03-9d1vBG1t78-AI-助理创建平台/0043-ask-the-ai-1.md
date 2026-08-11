---
title: "向 AI 提问"
source_url: "https://open.dingtalk.com/document/aipass/ask-the-ai-1"
namespace: "aipass"
slug: "ask-the-ai-1"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 工作流 > 执行动作 > AI 能力 > 向 AI 提问"
doc_id: "Yw48gprKze"
updated_at: "2025-09-23 19:19:43"
---

> Source: https://open.dingtalk.com/document/aipass/ask-the-ai-1
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 工作流 > 执行动作 > AI 能力 > 向 AI 提问
> Updated: 2025-09-23 19:19:43

# 向 AI 提问

如果你需要使用向 AI 提问的执行动作，请了解如何在[创建 AI 助理工作流](0037-create-an-ai-assistant-workflow-1.md)时添加执行动作。

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理/助理市场创建的 AI 助理**

## **操作步骤**

1. 单击**选择执行动作**，选择 **AI 能力 > 向 AI 提问**。
2. 配置向 AI 提问内容：

   | **配置项** | **说明** |
   | --- | --- |
   | 用到的 AI 模型 | 选择该执行动作用到的底层大模型，可选模型包括：  - 通义千问-plus - 通义千问-max - 通义法睿 - MiniMax abab6.5s-245k - 月之暗面128K - ChatGLM4 - 零一万物-large - 猎户星空 |
   | 问题 | 输入提示词，让AI生成文本内容，或回答你的问题。专注于创作、解答问题等生成文本内容的场景。  示例1：请为芋泥奶茶生成一段营销文案。  示例2：芋泥奶茶要怎么做？ |

> AI 的回答内容不会在该页面显示，如需引用其返回内容，请在之后步骤中选择引用。

## **示例**

以为芋泥奶茶生成营销策划为例，配置向 AI 助理提问：

| **配置项** | **说明** |
| --- | --- |
| 用到的 AI 模型 | 选择：通义千问-plus。 |
| 问题 | 填写：请为芋泥奶茶生成一段营销文案。 |

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3645361271/p823883.png)

设置完成后，你就可以在后续节点引用该执行动作中 AI 的回答内容了。
