---
title: "文档解读"
source_url: "https://open.dingtalk.com/document/aipass/document-interpretation-1"
namespace: "aipass"
slug: "document-interpretation-1"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 工作流 > 执行动作 > AI 能力 > 文档解读"
doc_id: "PuXTClccE0"
updated_at: "2025-09-23 19:19:45"
---

> Source: https://open.dingtalk.com/document/aipass/document-interpretation-1
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 工作流 > 执行动作 > AI 能力 > 文档解读
> Updated: 2025-09-23 19:19:45

# 文档解读

文档解读用于根据用户问题理解、总结和改写钉钉文档内容，在使用文档解读前，请了解如何在[创建 AI 助理工作流](0037-create-an-ai-assistant-workflow-1.md)时添加执行动作。

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理**

## **操作步骤**

1. 在工作流搭建页面，单击**选择执行动作** > **AI** > **AI 能力**，选择文档解读。
2. 配置文档解读执行动作：

   | **配置项** | **说明** |
   | --- | --- |
   | 文档链接 | 方式：  - 手动选择一篇钉钉文档  手动选择文档，需确保是钉钉文档的链接。 - 单击“⊕”，引用文档/文件链接变量。  用户发给 AI 助理的文件均会转存为钉钉文档，可以引用首节点中的文件链接变量。 请确保文档内容不要超过3万字，否则将解读失败。 |
   | 问题 | 请输入针对这篇文档的问题或要求，比如你可以输入“这篇文档的核心观点是什么？”，或者“请根据这篇文档的内容撰写宣传文稿”。 |

## **示例**

| **功能说明** | **功能搭建预览** |
| --- | --- |
| 产品经理在需求上线时，只需将 PRD 文档链接发送给 AI 助理，即可自动生成宣传稿。  image | 1. 在 AI 助理工作流中，设置提取用户对话中的提到的对产品功能的介绍。  image 2. **添加文档解读执行动作，让 AI 根据用户发送的文档链接，自动读取文档内容并生成宣传稿。**  image |
