---
title: "图片解读"
source_url: "https://open.dingtalk.com/document/aipass/picture-interpretation"
namespace: "aipass"
slug: "picture-interpretation"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 工作流 > 执行动作 > AI 能力 > 图片解读"
doc_id: "a3rw6ZWqHH"
updated_at: "2025-09-23 19:19:43"
---

> Source: https://open.dingtalk.com/document/aipass/picture-interpretation
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 工作流 > 执行动作 > AI 能力 > 图片解读
> Updated: 2025-09-23 19:19:43

# 图片解读

如果你需要使用图片解读的执行动作，请了解如何在[创建 AI 助理工作流](0037-create-an-ai-assistant-workflow-1.md)时添加执行动作。

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理/助理市场创建的 AI 助理**

## **操作步骤**

1. 单击**选择执行动作**，选择 **AI 能力** > **图片解读**。
2. 配置**图片解读**执行动作：

   | **配置项** | **说明** |
   | --- | --- |
   | 用到的 AI 模型 | 目前仅支持通义千问VL。 |
   | 图片链接 | 输入图片 URL 地址。  **[!NOTE]**  - 支持手动输入或单击 “⊕” 引用动态变量。 - 支持 AI 助理上传图片，工作流中获取图片 URL 地址，参见下方示例内容。 |
   | 问题 | 输入关于图片的问题，AI会根据你的问题进行回答。  **示例**：描述这张图片的内容，并分析这个图片里的人的年龄和职业。 |

## **示例**

以描述小猫图片为例，配置工作流：

1. 配置**步骤 1:调用工作流时：**

   | **配置项** | **说明** |
   | --- | --- |
   | 工作流名称 | 输入：图片解读工作流。 |
   | 向AI介绍工作流 | 图片解读，获取图片链接。 |
   | 提取向下执行需要的参数 | 参数一：  - 参数名称：图片链接 - 参数类型：文本 - 描述：获取图片链接 |

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9771142271/p828406.png)
2. 配置**图片解读**执行动作：

   | **配置项** | **说明** |
   | --- | --- |
   | 用到的 AI 模型 | 选择：通义千问VL。 |
   | 图片链接 | 单击 “⊕” 引用动态变量：1.图片链接  **[!NOTE]**  图片链接可见：[小猫图例](https://img.alicdn.com/imgextra/i4/O1CN01rLjsGF1CqVFTGKMGF_!!6000000000132-2-tps-1024-1024.png)。 |
   | 问题 | 描述图片内容。 |

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9771142271/p828413.png)
3. 单击 **“⊕”** ，选择**卡片** > **AI助理回复消息**，并配置执行：

   | **配置项** | **说明** |
   | --- | --- |
   | 自定义消息内容 | 单击**“⊕”，**选择节点2的解析的图片内容。 |

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9771142271/p828415.png)

   此时，图片解读执行动作已经配置完成。你可以向AI助理发送图片，获得图片描述内容。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9771142271/p828420.png)
