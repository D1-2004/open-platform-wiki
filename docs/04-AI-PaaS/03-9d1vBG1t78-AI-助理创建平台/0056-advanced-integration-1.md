---
title: "高级集成"
source_url: "https://open.dingtalk.com/document/aipass/advanced-integration-1"
namespace: "aipass"
slug: "advanced-integration-1"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 工作流 > 执行动作 > 高级集成"
doc_id: "Zo5bgvNY6c"
updated_at: "2025-09-23 19:20:06"
---

> Source: https://open.dingtalk.com/document/aipass/advanced-integration-1
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 工作流 > 执行动作 > 高级集成
> Updated: 2025-09-23 19:20:06

# 高级集成

当你发现工作流中的执行动作无法满足你的需求，你可以选择集成钉钉连接平台，你可以使用连接平台的子流程和连接器。

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理**

## **背景信息**

通过高级集成，可以在工作流内实现**更丰富的执行动作**和**更高级的流程编排能力**。具体来说，可以在 AI 助理工作流中直接调用钉钉连接平台的连接器和子流程。

| **调用连接平台的连接器** | **调用连接平台的子流程** |
| --- | --- |
| 连接平台有丰富的触发条件和执行动作，涵盖各类应用场景  image.png | 连接平台有丰富的流程编排能力，比如循环、分支、暂停、错误处理等。  image.png |

## **前提条件**

1. 了解并已经使用[连接平台](../../02-连接平台/01-6Ar2XD4H6b-平台介绍/0001-what-is-a-connected-platform.md)。

## **步骤一：连接平台配置授权**

1. 登录[钉钉连接平台](https://open-dev.dingtalk.com/fe/connector)，单击左侧导航栏**我的连接** > **连接场域**。
2. 选择 AI 助理的连接场域。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1965329171/p805634.png)
3. 选择在 AI 助理中使用的连接资源，包括官方连接器、三方连接器、自建连接器和自建子流程。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1965329171/p805640.png)
4. 选择你需要的能力，单击配置。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1965329171/p805642.png)
5. 进入场域授权页面，配置授权信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 在 AI 助理中授权使用 | 是否允许该能力在 AI 助理工作流中使用。  如果你需要取消在 AI 助理中的授权，关闭开关即可。 |
   | 可用范围 | 你需要决定谁能使用这个功能。只有你指定的成员，才能在 AI 助理的工作流中看到并使用该能力。 |
   | 授权的触发事件和执行动作 | 一个连接器可能会拥有多个触发条件和执行动作，你需要选择具体在 AI 助理工作流中使用哪些触发条件和执行动作。  使用自建子流程，无授权的触发事件和执行动作的配置项。 |

   选择完成后，单击保存即可。

## **步骤二：AI 助理的工作流中查看并使用**

1. 完成[创建 AI 助理工作流](0037-create-an-ai-assistant-workflow-1.md)的流程。
2. 在工作流配置页面，单击**执行动作**，选择你需要添加的能力。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1965329171/p805654.png)

   添加完成后，你就可以配置使用了。

## **相关文档**

- [创建连接流](../../02-连接平台/02-iO2mVD3wB2-开发指南/0002-create-a-connection-flow-1.md)
- [创建连接器](../../02-连接平台/02-iO2mVD3wB2-开发指南/0013-create-connector.md)
