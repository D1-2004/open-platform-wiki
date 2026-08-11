---
title: "AI 助理回提问卡片给当前用户"
source_url: "https://open.dingtalk.com/document/aipass/the-ai-assistant-returns-the-question-card-to-the-current-1"
namespace: "aipass"
slug: "the-ai-assistant-returns-the-question-card-to-the-current-1"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 工作流 > 钉钉协作 > 消息通知 > AI 助理回提问卡片给当前用户"
doc_id: "bz55trMXqo"
updated_at: "2025-09-23 19:19:58"
---

> Source: https://open.dingtalk.com/document/aipass/the-ai-assistant-returns-the-question-card-to-the-current-1
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 工作流 > 钉钉协作 > 消息通知 > AI 助理回提问卡片给当前用户
> Updated: 2025-09-23 19:19:58

# AI 助理回提问卡片给当前用户

AI 助理回提问卡片给当前用户，用于 AI 助理在流程执行中途主动向用户提问，收集必要信息后继续执行后续步骤，请了解如何在[创建 AI 助理工作流](0037-create-an-ai-assistant-workflow-1.md)时添加执行动作。

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理**

## **操作步骤**

1. 在 AI 助理工作流搭建页面，单击**选择执行动作** > **钉钉协作** > **消息通知**，选择 AI 助理回提问卡片给当前用户。
2. 配置 AI 助理回提问卡片给当前用户执行动作：

   | **配置项** | | **说明** |
   | --- | --- | --- |
   | 标题 | | 提问卡片标题信息。 |
   | 提问字段列表  可单击下方“ + 添加字段 ”按钮，新增多个字段。 | 字段名称 | 用户待确认字段名称信息。 |
   | 字段类型 | 字段类型：  - 文本 - 是否 - 单选 - 日期 - 日期时间 - 多行文本 |
   | 默认值 | 字段默认值。  支持单击 “⊕”，进行动态配置。 |
   | 等待用户点击按钮再继续此流程  当前仅支持等待模式。 | 确认按钮 > 按钮名称 | 填写按钮名称。 |

   至此，AI 助理回提问卡片就已经配置完成。

## **示例**

### **智能招聘发布**

### **视频展示**

[](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250113/uznpoc/%E6%8F%90%E9%97%AE%E5%8D%A1%E7%89%87-%E8%8C%83%E4%BE%8B.mp4)

### **实践指南**

| **功能使用效果** | **功能搭建流程** |
| --- | --- |
| 1. 用户对招聘 AI 助理说出自己的要求，要求助理生成岗位描述。  image | 1. 向 AI 提问。让AI根据用户的输入生成岗位描述。  image |
| 2. AI 助理生成岗位描述并发给用户。  image | 2. .AI 助理回消息给当前用户。将上一步生成的岗位描述发送给用户。  image |
| 3. **AI 助理主动询问用户是否要将这些内容要发布到网站，向用户确认发布的渠道和相关信息**：     1. 发布渠道（可选：BOSS直聘、智联招聘、脉脉、不发布）    2. 学历要求（可选：本科、研究生）    3. 招聘截止时间    4. 备注image | 3. **AI 助理回提问卡片给当前用户。 AI助理主动询问用户是否需要发布到网站，包括发布渠道、学历要求、招聘截止时间等信息**。  image 4. 条件分支。根据用户选择，生成不同的分支。  image 5. 发起 HTTP 请求。如果用户的选择是 boss 直聘，则在这个分支下发起一个请求，将内容发布到 boss 直聘。其他分支同理。  image |
| 4. AI 助理根据用户提交的内容，将职位发布到指定的平台。  image | 6. AI 助理回消息给当前用户。发布成功后，提示用户已发布完成。image |
