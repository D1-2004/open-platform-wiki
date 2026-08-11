---
title: "文档内容写入"
source_url: "https://open.dingtalk.com/document/aipass/document-write-1"
namespace: "aipass"
slug: "document-write-1"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 工作流 > 钉钉协作 > 钉钉文档 > 文档内容写入"
doc_id: "ZcPPIzzEN8"
updated_at: "2025-09-23 19:19:55"
---

> Source: https://open.dingtalk.com/document/aipass/document-write-1
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 工作流 > 钉钉协作 > 钉钉文档 > 文档内容写入
> Updated: 2025-09-23 19:19:55

# 文档内容写入

如果你需要使用文档写入的执行动作，请了解如何在[创建 AI 助理工作流](0037-create-an-ai-assistant-workflow-1.md)时添加执行动作。

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理**

## **操作步骤**

1. 单击**选择执行动作**，选择**钉钉文档 > 文档写入**。
2. 配置**文档写入**执行动作：

   | **配置项** | **说明** |
   | --- | --- |
   | 要写入的文档 | 在钉钉文档中选择要写入的文档。 |
   | 写入方式 | 选择合适的写入方式：  - 新起段落续写 - 完全覆盖已有内容 |
   | 要写入的内容 | 输入要写入的文档内容。  **[!NOTE]**  - 新起段落续写方式，目前仅支持写入纯文档。 - 完全覆盖已有内容方式，支持 Markdown 格式。详情参考[Markdown 变量](../../06-互动卡片/02-MhNX42mFB1-卡片模板搭建器/0019-markdown-variable-new.md)语法。 - 支持手动输入或单击 “⊕” 引用动态变量。 |

## **示例**

以文档写入信息为例，配置文档内容写入执行动作：

| **配置项** | **说明** |
| --- | --- |
| 要写入的文档 | 选择钉钉文档下“周报文档”，创建过程可参考[新增空白文档](0066-new-blank-document-1.md)示例中新增“周报文档”。 |
| 写入方式 | 选择新起段落续写。 |
| 要写入的内容 | 输入：这是周报文档正文部分。 |

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7929549171/p815269.png)

此时，文档写入的执行动作已经配置完成。
