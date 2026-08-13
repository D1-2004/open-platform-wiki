---
title: "自定义 MCP"
source_url: "https://open.dingtalk.com/document/aipass/manage-ai-assistant-workflow-1"
namespace: "aipass"
slug: "manage-ai-assistant-workflow-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "MCP 管理 > 自定义 MCP"
doc_id: "G1uy1TFWSO"
updated_at: "2026-07-08 15:48:52"
---

> Source: https://open.dingtalk.com/document/aipass/manage-ai-assistant-workflow-1
> Path: AI PaaS / DEAP·企业AI平台 / MCP 管理 > 自定义 MCP
> Updated: 2026-07-08 15:48:52

# 自定义 MCP

技能中心通过MCP协议，接入用户自定义的技能，所以我们首先要了解MCP协议是什么。

## **什么是MCP协议**

模型上下文协议（MCP）是一种开放规范，使大语言模型驱动的智能体能够调用外部工具和资源，从而大幅扩展其能力边界。借助社区丰富的示例，开发者可以快速搭建 MCP Server，将自定义能力集成到智能体中。

此外，在 MCP 协议基础上，我们还兼容了 OpenAI 的 Widget 能力，支持用户在智能体中自定义展示组件。

## **如何绑定一个MCP技能**

进入 [DEAP 开发后台](https://deap.dingtalk.com/#/sub-app/model-manage)，在**开发模式**下，选择**MCP**，然后选择**自定义 MCP**。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2396943871/p1085966.png)

技能中心提供了两种方式快速创建MCP技能，快速创建（向导模式）和JSON导入：

### **方式一：快速创建**

在场景MCP服务表单界面，填写MCP基本信息，并通过**MCP检测**后，点击右上角的**确定创建**即可。

> **[!NOTE]**
>
> 若点击右上角**MCP检测**按钮后，配置MCP服务通过后，右侧MCP工具列表会显示技能的工作列表，如下图所示。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2396943871/p1085970.png)

- **技能图标：**用户可以上传自己的头像，建议200\*200的JPG或PNG。
- **名称（必填）：**技能名称，不要超过30个字符。
- **描述（必填）：**技能简要描述，描述技能的能力，智能体会将这个描述信息提供给大语言模型用于调用规划。
- **功能介绍：**技能应用场景介绍，可以提供丰富的用例，便于大语言模型更准确地调用技能。
- **可用人员范围：**选择技能开放的范围。
- **标签：**给技能打上对应的标签，标签长度不要超过4个字符，不要多余3个标签。
- **MCP配置**

  - **类型：**支持**SSE**和**Streamable HTTP**，不支持Stdio。
  - **HTTP URL：**MCP Server的Endpoint。
  - **请求头：**需要携带的自定义，系统预置Header:

    > **[!NOTE]**
    >
    > 注册 MCP 服务时，有些接口需要在请求头里带鉴权信息。这里填 key/value，平台会在调用该服务时自动携带。

    - X-DingTalk-User-Id : 用户UID
    - X-DingTalk-User-Job-Number: 用户工号

### **方式二：JSON导入**

从 MCP Servers 的介绍页面复制配置JSON（优先使用NPX或UVX配置），并粘贴到输入框中，最后点击**确定**即可。

> **[!NOTE]**
>
> 支持标准的MCP JSON配置（注意： type只支持Sse和Streamable Http模式，不支持Stdio模式）。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2396943871/p1086070.png)

系统会基于JSON中配置的内容，自动填充到MCP服务表单页面中，如下图所示：

> **[!NOTE]**
>
> 若点击右上角**MCP检测**按钮后，配置MCP服务通过后，右侧MCP工具列表会显示技能的工作列表，如下图所示。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2396943871/p1086077.png)

- **技能图标：**用户可以上传自己的头像，建议200\*200的JPG或PNG。
- **名称（必填）：**技能名称，不要超过30个字符。
- **描述（必填）：**技能简要描述，描述技能的能力，智能体会将这个描述信息提供给大语言模型用于调用规划。
- **功能介绍：**技能应用场景介绍，可以提供丰富的用例，便于大语言模型更准确地调用技能。
- **可用人员范围：**选择技能开放的范围。
- **标签：**给技能打上对应的标签，标签长度不要超过4个字符，不要多余3个标签。
- **MCP配置**

  - **类型：**支持**SSE**和**Streamable HTTP**，不支持Stdio。
  - **HTTP URL：**MCP Server的Endpoint。
  - **请求头：**需要携带的自定义，系统预置Header:

    > **[!NOTE]**
    >
    > 注册 MCP 服务时，有些接口需要在请求头里带鉴权信息。这里填 key/value，平台会在调用该服务时自动携带。

    - X-DingTalk-User-Id : 用户UID
    - X-DingTalk-User-Job-Number: 用户工号
