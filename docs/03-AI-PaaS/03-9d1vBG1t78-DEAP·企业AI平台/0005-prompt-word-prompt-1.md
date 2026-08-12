---
title: "内置 MCP"
source_url: "https://open.dingtalk.com/document/aipass/prompt-word-prompt-1"
namespace: "aipass"
slug: "prompt-word-prompt-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "MCP 管理 > 内置 MCP"
doc_id: "LxSQFOLzL8"
updated_at: "2026-07-08 15:48:50"
---

> Source: https://open.dingtalk.com/document/aipass/prompt-word-prompt-1
> Path: AI PaaS / DEAP·企业AI平台 / MCP 管理 > 内置 MCP
> Updated: 2026-07-08 15:48:50

# 内置 MCP

## **什么是内置 MCP**

钉钉平台深度整合 DEAP 框架，通过标准化接口开放了内置 MCP 技能套件。该套件实现了钉钉原生应用与企业智能体的无缝对接，显著提升了智能体与企业组织系统间的数据交互效率。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1086125.png)

目前提供的核心能力包括（但不限于）以下功能模块：

| **模块** | **技能描述** |
| --- | --- |
| 智能问数 | 通过对话的方式，实现对表格数据和数据库数据的分析洞察。 |
| 签到 | - 获取部门用户签到记录，以部门维度获取员工签到记录进行统计分析 - 获取指定用户的签到记录，可获取指定人员的签到记录进行统计分析 |
| 工作通知 | 发送工作通知消息，支持text、link、markdown三种类型。 |
| 提醒(Ding) | 使用机器人发送具有强提醒功能的DING消息。 |
| 钉钉日程 | 支持创建日程，查询日程，约空闲会议室等能力。 |
| 钉钉通讯录 | 钉钉通讯录MCP支持搜索人员/部门、查询成员详情及部门结构，快速获取组织架构信息。 |
| 钉钉待办 | 钉钉待办MCP服务提供高效的任务管理能力，支持创建待办事项、更新任务状态（如完成/未完成）、以及按条件查询待办列表。 |
| Teambition 项目管理 | Teambition MCP 助您高效管理项目与任务，支持创建/更新任务、设置截止日期、分配执行人及查看任务进展等，无缝集成 Teambition 平台，提升团队协作效率。 |
| 钉钉OA审批 | 钉钉OA审批MCP插件，支持查询当前用户待处理的审批单，快速掌握待办事项。 |
| 钉钉群聊 | 钉钉群聊MCP支持通过自然语言快速创建内部群，高效启动团队协作。 |
| 钉钉邮箱 | 钉钉邮箱MCP支持查询邮箱账号、收件内容及发送邮件，实现自然语言驱动的高效邮件处理。 |
| 基于关系链查找用户 | 基于关系链查找用户。 |
| AI印设计服务 | 钉钉AI印 MCP Server 是专为视觉内容创作与管理打造的能力组件，支持通过自然语言指令对图像进行全生命周期处理。 |
| 钉钉AI表格 | 钉钉 AI 表格 MCP 让 AI 直接操作表格数据与字段，快速打通查询、维护与自动化办公流程。 |
| 钉钉文档 | 钉钉文档MCP支持查找、创建文档，助力高效协同与内容管理。 |
| 机器人消息 | 钉钉机器人消息MCP服务，支持创建企业机器人、根据关键词搜索群会话openconversationId、将企业机器人添加到指定的群内、企业机器人发送群消息和单聊消息、企业机器人取消发送的群或单聊消息等能力。 |
| **更多技能** | 可以通过钉钉客服反馈期望的内置MCP技能上架到DEAP平台。 |

## **如何使用内置 MCP**

我们以添加钉钉通讯录 MCP为例，查询自己的组织架构信息。

1. 进入 [DEAP 开发后台](https://deap.dingtalk.com/#/sub-app/model-manage)，在**开发模式**下，选择**智能体**，然后找到目标智能体，点击**编辑**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1085917.png)
2. 点击左侧**MCP**功能，然后点击**添加MCP**按钮。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1085505.png)
3. 选择目标MCP工具，然后点击右侧的添加即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1086128.png)
4. 技能添加成功后，可在右侧调试页面进行调试，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1086129.png)
5. 测试通过后，点击右上角的**发布**按钮。

   > **[!NOTE]**
   >
   > 修改配置后，必须重新发布才会生效。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1086130.png)
