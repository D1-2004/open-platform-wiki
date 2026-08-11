---
title: "添加执行动作"
source_url: "https://open.dingtalk.com/document/connection/add-execution-action-1"
namespace: "connection"
slug: "add-execution-action-1"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发连接器 > 添加执行动作"
doc_id: "iwonWZnM31"
updated_at: "2025-09-23 19:20:08"
---

> Source: https://open.dingtalk.com/document/connection/add-execution-action-1
> Path: 连接平台 / 开发指南 / 开发连接器 > 添加执行动作
> Updated: 2025-09-23 19:20:08

# 添加执行动作

本文将介绍如何配置并调试自建连接器的执行动作。

## **背景信息**

执行动作是连接器的重要功能之一。执行动作一般由 API 和其对应的出入参构成，它能够携带入参，调用具有业务逻辑的 API，将业务处理结果通过出参返回。执行动作能够作为连接流的执行节点，在流程运行到该节点时，完成特定的业务处理。连接流也因此具备了便捷的流程编排能力及集成自动化能力。

## **前提条件**

完成[创建连接器](0013-create-connector.md)流程。

## **操作步骤**

1. 选择创建的连接器进入详情页面，单击**执行动作** > **创建执行动作**，进入执行动作配置页。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3393460571/p976076.png)
2. 填写执行动作基础信息。

   | **配置项** | **说明** |
   | --- | --- |
   | 名称 | 请填写执行动作名称。 |
   | 描述 | 请填写执行动作描述。 |
   | 展示分组 | 触发事件在连接器中的分组。 |
   | API类型 | 执行动作API接口类型，包含：  - HTTP（默认） - FAAS，详情参考 [FAAS脚本](0049-nodejs-script-connector-1.md)。 |

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3393460571/p976077.png)

   配置完成后，单击下一步，进入入参配置页面。
3. 在入参配置界面，根据接口的实际入参结构进行配置。

   | **HTTP类型入参配置** | **说明** |
   | --- | --- |
   | 接口路径 | 请填写接口请求类型和请求 URL。  填写完成后，可以单击检测联通性，保证接口可以被请求到。image |
   | API入参 | 请配置接口的请求参数结构：  - 手动添加接口参数字段：请根据实际情况录入，连接平台提供 HTTP 请求头、HTTP 请求体、URL 查询参数和 URL 路径参数。  image - 导入 JSON：可以根据具体的JSON格式分别录入对应的HTTP 请求头、HTTP 请求体、URL 查询参数和 URL 路径参数。  image |
   | 入参映射（可选） | 在不改变 API ⼊参的情况下，重新定义该执⾏动作对外的⼊参模型。  image |

   配置完成后，单击下一步，进入出参配置页面。
4. 在出参配置界面，根据接口的实际出参结构进行配置。

   | **HTTP类型出参配置** | **说明** |
   | --- | --- |
   | API出参 | 请配置接口的返回参数结构。  image |
   | 出参映射（可选） | 在不改变 API 出参的情况下，重新定义该执⾏动作对外的出参模型。  image |

   配置完成后，单击下一步。
5. 在调试界面下，填写执行动作**入参**参数，然后单击**立即调试**。

   > **[!NOTE]**
   >
   > 1. 调试成功的用例，可以点击**保存调试用例**，方便下一次调试。
   > 2. 如果在入参配置和出参配置开启了参数映射，则在调试结果中，可以查看API入参结果和API出参结果。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3393460571/p976092.png)
6. 调试完成之后，可以选择**保存草稿**或者直接**发布**。发布后可在连接流中使用该执行动作。

## **后续步骤**

执行动作配置完成后，你可以[使用连接器](0016-using-connectors-1.md)。

> 如果你需要配置触发事件，可以参考[添加触发事件](0014-add-trigger-event-1.md)。
