---
title: "如何使用表达式（公式）模式"
source_url: "https://open.dingtalk.com/document/aipass/how-to-use-the-expression-formula-pattern"
namespace: "aipass"
slug: "how-to-use-the-expression-formula-pattern"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 工作流 > 执行动作 > 公式编辑 > 如何使用表达式（公式）模式"
doc_id: "8oPtxMdsWZ"
updated_at: "2025-09-23 19:20:08"
---

> Source: https://open.dingtalk.com/document/aipass/how-to-use-the-expression-formula-pattern
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 工作流 > 执行动作 > 公式编辑 > 如何使用表达式（公式）模式
> Updated: 2025-09-23 19:20:08

# 如何使用表达式（公式）模式

如果你是第一次使用公式编辑的表达式模式，请了解如何在[创建 AI 助理工作流](0037-create-an-ai-assistant-workflow-1.md)时进入新建工作流页面，本文档内容将帮助你快速体验表达式能力。

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理/助理市场创建的 AI 助理**

## **明确需求**

利用工作流的表达式模式计算数字`x`的`y`次方。

## **操作步骤**

1. 在工作流配置页面，单击**设置入参**，配置如下：

   | **配置项** | | **说明** |
   | --- | --- | --- |
   | 工作流名称 | | 乘方计算器 |
   | 工作流描述 | | 计算x的y次方的结果，例如请帮我计算3的2次方。 |
   | 入参 | X | - 参数类型：数字 - 描述信息：乘方中的基数，例如 3 的 2 次方中的 3 |
   | Y | - 参数类型：数字 - 描述信息：乘方中的指数，例如 3 的 2 次方中的 2 |

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8278639171/p814521.png)这将帮助大模型准确找到和使用该工作流。
2. 添加**发送消息**执行动作：

   1. 在步骤 2 中，选择**卡片** > **发送消息**执行动作。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3965329171/p813872.png)
   2. 在发送消息的自定义消息内容中，单击 “⊕” > 使用公式编辑。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3965329171/p813873.png)
   3. 选择表达式（公式）模式，由于需要计算乘方，你需要从“函数列表”中选择`POWER`函数，设置为`POWER(X,Y)`。

      > **[!NOTE]**
      >
      > 此处 X 和 Y，均为 步骤 1 中的 X 和 Y。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3965329171/p813875.png)

      设置完成后，单击右下角确认。
3. 设置完成后，单击保存并启用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3965329171/p813880.png)
4. 此时，你已经返回到 AI 助理创建页面，你可以单击右上角保存按钮，在调试区在与 AI 助理对话：请为我计算 4 的 3 次方。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3965329171/p813896.png)

   此时，你可以得到 64.0 的正确结果。
