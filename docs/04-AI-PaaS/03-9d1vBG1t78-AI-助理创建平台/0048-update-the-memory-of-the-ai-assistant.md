---
title: "更新 AI 助理的记忆"
source_url: "https://open.dingtalk.com/document/aipass/update-the-memory-of-the-ai-assistant"
namespace: "aipass"
slug: "update-the-memory-of-the-ai-assistant"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 工作流 > 执行动作 > AI 助理 > 更新 AI 助理的记忆"
doc_id: "oZNJzSzDEN"
updated_at: "2025-09-23 19:19:47"
---

> Source: https://open.dingtalk.com/document/aipass/update-the-memory-of-the-ai-assistant
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 工作流 > 执行动作 > AI 助理 > 更新 AI 助理的记忆
> Updated: 2025-09-23 19:19:47

# 更新 AI 助理的记忆

如果你需要使用更新 AI 助理的记忆的执行动作，请了解如何在[创建 AI 助理工作流](0037-create-an-ai-assistant-workflow-1.md)时添加执行动作。

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理/助理市场创建的 AI 助理**

## **前提条件**

完成[配置个性化信息](0084-configuration-memory-1.md)的流程。

## **操作步骤**

1. 单击**选择执行动作**，选择 **AI 能力 > 更新AI助理的记忆**。
2. 配置更新 AI 助理的记忆执行动作：

   | **配置项** | **说明** |
   | --- | --- |
   | 要更新的变量 | 选择要更新的变量。  仅支持拥有编辑权限的记忆变量。 |
   | 更新后的值 | 输入预期更新后的记忆值。  **[!NOTE]**  支持手动输入或单击 “⊕” 引用动态变量。 |

## **示例**

以更新“你关注的行业”记忆变量为例：

1. 你需要添加自定义记忆变量“你关注的行业”，具体配置参见[配置个性化信息](0084-configuration-memory-1.md)。

   > 用户是否可修改，要设置为允许。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1551749171/p815416.png)
2. 配置更新 AI 助理的记忆执行动作：

   | **配置项** | **说明** |
   | --- | --- |
   | 要更新的变量 | 选择上述创建的变量：你关注的行业。 |
   | 更新后的值 | 输入：互联网。 |

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1551749171/p815419.png)

   此时，你的更新 AI 助理的记忆执行动作就已经配置完成了。
