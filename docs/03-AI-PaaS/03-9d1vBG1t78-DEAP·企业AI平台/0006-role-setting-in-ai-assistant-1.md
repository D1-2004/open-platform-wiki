---
title: "三方 MCP"
source_url: "https://open.dingtalk.com/document/aipass/role-setting-in-ai-assistant-1"
namespace: "aipass"
slug: "role-setting-in-ai-assistant-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "MCP 管理 > 三方 MCP"
doc_id: "zV3Im3CPzN"
updated_at: "2026-07-09 10:04:28"
---

> Source: https://open.dingtalk.com/document/aipass/role-setting-in-ai-assistant-1
> Path: AI PaaS / DEAP·企业AI平台 / MCP 管理 > 三方 MCP
> Updated: 2026-07-09 10:04:28

# 三方 MCP

## **什么是三方技能**

三方技能是 DEAP 平台 MCP 技能体系的重要组成部分，用于引入和管理由外部平台或生态合作伙伴开发的 MCP 技能。它与官方技能互为补充，帮助用户快速扩展平台能力、降低接入成本。

主要特性如下：

- **开放性** ：支持第三方开发者或合作伙伴以标准接口形式接入自有 AI 能力。
- **标准化接入** ：遵循平台统一的技能接入规范，包括接口格式、认证方式和调用标准。
- **可视化管理** ：在技能中心可直接查看三方技能的描述、工具列表及提供方信息。
- **安全可控** ：对外部技能实行严格审核与沙箱机制，确保数据安全与调用合规。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1396943871/p1086087.png)

目前提供的核心能力包括（但不限于）以下功能模块：

| **模块** | **技能描述** |
| --- | --- |
| MCP 中文趋势聚合 | 基于 Model Context Protocol (MCP) 协议的全网热点趋势一站式聚合服务。 |
| 必应搜索中文 | 一个基于 MCP (Model Context Protocol) 的中文必应搜索工具，可以直接通过 Claude 或其他支持 MCP 的 AI 来搜索必应并获取网页内容。 |
| 搜论文 | 该工具允许用户通过主题名称在 arXiv 上搜索研究论文，优化关键词以提升搜索效果，查看详细信息，并以多种格式导出结果（TXT、DOCX、PDF、Excel）。它还可以基于搜索结果生成 学术总结/结论，并记录导出活动，以便智能系统或代理后续使用。 |
| 通义千问-语音合成 | 通义千问-语音合成是通义千问官方提供的 MCP，支持将文本内容转换为自然流畅的音频文件，适用于语音播报、有声阅读、智能客服等多种场景。 |
| 通义千问-图生图 | 本服务调用的是通义前文的wan2.5-i2i-preview大模型，同步的方式实现图片编辑、图生图能力。 |
| 通义千问-模型翻译 | 本服务使用的是qwen-mt-turbo大模型，把输入的文本按照指定要求语种进行翻译，输入 Token 上限为 8192。 |
| 高德地图 | 提供基于位置服务、地点信息搜索、路径规划、天气查询等12大核心高鲜度数据，让用户在出行规划、位置信息检索场景下轻松获取即时信息。 |
| 火车票查询 | 火车票查询是聚美智数官方提供的 MCP，支持查询车站信息、查询火车票余票等操作。 |
| 通义万相-文生视频 | 通义万相-文生视频是 开放平台官方提供的 MCP，支持通过文本描述生成高质量视频内容，实现从文字到动态视觉的自动化创作。 |
| 秘塔AI-链接速读 | 秘塔AI-链接速读是秘塔科技提供的 MCP（Model-Context-Protocol）能力插件，支持快速解析和读取网页链接内容，提取核心信息并生成简洁摘要，帮助用户高效获取关键知识，提升阅读与决策效率。 |
| 合合-文件解析 | 合合-文件解析是合合信息提供的 MCP，支持将PDF文件解析为结构化的Markdown格式内容，便于后续信息提取与处理。 |
| OpenClaw | OpenClaw 为钉钉 DEAP Agent 提供与本地设备的深度集成能力，通过自然语言驱动实现设备操作,执行复杂的抽象任务，包括操控浏览器、文件系统、截图、搜索及打开特定 App。 |
| 通义万相-文生图 | 通义万相-文生图是基于通义大模型的AI绘画生成MCP，支持通过文本描述生成高质量图像，并可查询生成结果。 |
| **更多技能** | 可以通过钉钉客服反馈期望的三方MCP技能上架到DEAP平台。 |

## **如何使用三方技能**

我们以添加三方技能-火车票查询服务为例，实现查询火车票的能力。

1. 进入 [DEAP 开发后台](https://deap.dingtalk.com/#/sub-app/model-manage)，在**开发模式**下，选择**智能体**，然后找到目标智能体，点击**编辑**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1085917.png)
2. 点击左侧**MCP**功能，然后点击**添加MCP**按钮。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1085505.png)
3. 选择目标MCP工具，然后点击右侧的添加即可。

   > **[!NOTE]**
   >
   > - 点击**添加**之后，若该MCP技能需要依赖三方密钥，需先在三方平台申请密钥后，配置密钥。
   > - 若不依赖密钥，可直接添加成功。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1396943871/p1086092.png)
4. 技能添加成功后，可在右侧调试页面进行调试，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1396943871/p1086095.png)
5. 测试通过后，点击右上角的**发布**按钮。

   > **[!NOTE]**
   >
   > 修改配置后，必须重新发布才会生效。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1086130.png)
