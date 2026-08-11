---
title: "创建 AI 助理工作流"
source_url: "https://open.dingtalk.com/document/aipass/create-an-ai-assistant-workflow-1"
namespace: "aipass"
slug: "create-an-ai-assistant-workflow-1"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 工作流 > 创建 AI 助理工作流"
doc_id: "NOQOn5WVOV"
updated_at: "2025-09-23 19:19:37"
---

> Source: https://open.dingtalk.com/document/aipass/create-an-ai-assistant-workflow-1
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 工作流 > 创建 AI 助理工作流
> Updated: 2025-09-23 19:19:37

# 创建 AI 助理工作流

如果你需要添加 AI 助理工作流，请了解[创建组织内使用的 AI 助理](0005-create-a-dingtalk-ai-assistant-1.md)/[创建市场 AI 助理](0006-share-dingtalk-ai-assistant.md)如何进入创建 AI 助理页面。

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理/助理市场创建的 AI 助理**

## **创建工作流**

创建工作流的方式有以下两种：

- 从模板创建流程：适用于新手用户等希望快速启动和实施工作流的用户或组织，模板内提供预置的触发条件和执行动作，可在此基础上进行修改。
- 从空白创建流程：适用于对工作流有特定需求或者希望完全定制化的用户或组织，可以自定义选择并配置触发条件和执行动作。

### **从模板创建流程**

1. 在 AI 助理创建页面，单击**技能** > **添加，进入技能市场列表。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7020207471/p920983.png)
2. 在技能市场列表，切换工作流Tab，选择任一工作流模板，并单击**添加**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7020207471/p953537.png)
3. 在弹出的新建工作流页面，完成流程配置，配置完成后，单击右上角**保存并启用。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4491999171/p816950.png)

### **从空白创建流程**

#### **创建工作流**

| **创建方式** | **说明** |
| --- | --- |
| 方式一：在 AI 助理创建页面，单击**技能** > **添加技能**，选择**新建工作流**。 | image |
| 方式二：在 AI 助理创建页面，单击**技能 > 添加工作流。** | image |

> 创建工作流时，需要填写技能名称和技能描述。

#### **配置工作流**

1. 配置触发条件“步骤 1：调用工作流时”：

   | **配置项** | **说明** |
   | --- | --- |
   | 提取向下执行需要的参数 | 与 AI 对话过程中希望被提取的参数信息。  - 例如：在执行“搜索商品”工作流前，需要输入商品的名称、价格等，这些输入的内容就是入参，AI会根据参数的定义，智能提取参数的内容。 目前支持的参数类型有：文本、数字、是否、人员、日期、时间、日期时间。 |

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4179114271/p837739.png)
2. 配置执行动作，单击**步骤2：选择执行动作**，各项执行动作内容请参考[内置工具](0040-workflow-built-in-tools-1.md)。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4179114271/p837740.png)

   > 1. 如果你需要操作执行节点，你可以单击 **“···”，**可以选择 **“↑向上添加”、“↓向下添加”或“删除”。**

   > **2.** 完整的工作流须包含**触发条件**和至少一个**执行动作。**
3. 配置完成后，单击右上角**保存并启用**，返回 AI 助理编辑页面。

## **测试与发布工作流**

1. 在AI助理编辑页，单击**保存**，你可以在右侧测试区域进行工作流的测试。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7020207471/p920982.png)
2. 测试通过后，单击发布，进入 AI 助理发布页面，选择合适的发布范围，完成发布操作即可。

## **常见问题**

- ### **如何关闭对话确认框？**

  答：

  1. 如果你希望关闭对话确认框，如下图例：

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9765329171/p813981.png)
  2. 你可以在“步骤1：调用工作流时”中，进行确认框的启用和关闭。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4179114271/p837741.png)
