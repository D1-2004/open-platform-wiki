---
title: "新建工作流"
source_url: "https://open.dingtalk.com/document/aipass/create-an-ai-assistant-workflow-1"
namespace: "aipass"
slug: "create-an-ai-assistant-workflow-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "智能体管理 > 新建工作流"
doc_id: "NOQOn5WVOV"
updated_at: "2026-07-08 15:48:50"
---

> Source: https://open.dingtalk.com/document/aipass/create-an-ai-assistant-workflow-1
> Path: AI PaaS / DEAP·企业AI平台 / 智能体管理 > 新建工作流
> Updated: 2026-07-08 15:48:50

# 新建工作流

## 为什么需要工作流

在企业日常运营中，请假审批、费用报销、IT 服务申请、客户工单处理等业务流程往往涉及跨系统、跨角色、跨部门的协同。传统应对方式主要有两种：

- **人工操作** ：通过邮件、即时消息或在多个平台间手动填写表单推进流程，效率低、易出错、难追溯。
- **代码集成** ：由 IT 部门定制开发连接各业务系统，虽能实现自动化，但周期长、成本高、灵活性差，业务规则变更时需重新开发部署。

随着企业数字化深入，员工频繁在 CRM、ERP、HRM、OA 等多个 SaaS 系统间切换，信息割裂严重。而大模型虽具备强大的理解与生成能力，却无法直接操作业务系统、执行审批或调用接口—只能"说"，不能"做"。

为此，Deap的工作流应运而生，打通"认知"与"执行"的鸿沟，将大模型的智能理解能力与企业真实业务流程深度融合。

### **核心能力**

- **自动化执行业务流程** ：将创建工单、发送通知、更新状态等重复性操作交由工作流自动完成，大幅减少人工干预。
- **连接多系统，打破数据孤岛** ：通过标准化连接器（Connector），无缝集成钉钉内部应用（审批、考勤等）及外部系统（163 邮箱、企业自建系统等），实现端到端自动化。
- **增强大模型行动能力** ：在智能对话中，用户提出"帮我提交一个服务器故障报修"时，大模型可调用工作流自动填充表单、创建工单并通知负责人，真正做到"说到即做到"。
- **低代码灵活编排** ：提供可视化拖拽界面，业务人员无需编码即可设计和修改流程，快速响应业务变化。
- **安全可控** ：严格遵循企业组织架构与权限体系，所有节点操作均被完整记录，确保合规可审计。

### 工作流编排

用户通过 DEAP 提供的可视化界面，以拖拽方式编排业务流程。系统支持多种节点类型，可灵活组合实现复杂的逻辑流转，满足多样化的业务场景需求。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1085749.png)

### 工作流执行

工作流的执行过程分为三个阶段：

1. **意图识别与参数提取** ：当用户向 Agent 发起请求（如"帮我申请一台开发用笔记本"）时，大模型自动识别意图、匹配对应工作流，并从对话中提取关键参数（设备类型、用途、所属项目等）。
2. **自动触发与流程执行** ：确认信息后，系统自动触发工作流实例。执行引擎按预设流程调用钉钉原生能力（审批、待办等）或企业自建系统接口，整个过程状态可追踪、操作可审计。
3. **结果反馈** ：执行完成后，结果以自然语言或卡片形式反馈给用户，实现"说一句，就办好"的智能自动化体验。

整体流程，如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1085750.png)

## **如何搭建一个工作流**

1. 进入 [DEAP 开发后台](https://deap.dingtalk.com/#/sub-app/model-manage)，在**开发模式**下，选择**智能体**，然后找到目标智能体，点击**编辑**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1085917.png)
2. 在智能体功能编辑页面，依次选择**工作流 > 添加工作流**，添加一个新的工作流。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1085919.png)
3. 在弹窗中，点击右上角**新建工作流**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1085923.png)
4. 在新建工作流表单中，填写工作流名称、工作流描述和示例问题（可选），填写完成后点击**确定**。

   > **[!NOTE]**
   >
   > 请准确填写技能名称和技能描述，这两项信息将直接影响 Agent 的任务规划与调用决策。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1085928.png)
5. 点击**+号**图标，添加执行动作，并编排其他节点。

   > **[!NOTE]**
   >
   > 系统提供四种执行动作，可根据业务需求自由搭配：
   >
   > - **逻辑/工具**：执行条件判断、循环、筛选等逻辑操作，控制流程走向。
   > - **AI** ：调用 AI 模型对原始数据进行加工处理，生成新内容后传递至下一步。
   > - **钉钉协作** ：调用钉钉原生能力（如创建待办、发送消息等），并返回执行结果。
   > - **其他业务** ：调用外部服务（如 QQ 邮箱、高德天气查询等），获取结果后进入下一步。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1085938.png)
6. 工作流编排结束后，可以在右侧预览和调试该工作流。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1085958.png)
7. 调试无误后，点击**启用**即可正式发布工作流，至此完成一个工作流的创建、编排和发布内容。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0396943871/p1085960.png)
