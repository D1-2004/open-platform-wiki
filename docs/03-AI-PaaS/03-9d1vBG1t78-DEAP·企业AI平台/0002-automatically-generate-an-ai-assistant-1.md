---
title: "智能体开发"
source_url: "https://open.dingtalk.com/document/aipass/automatically-generate-an-ai-assistant-1"
namespace: "aipass"
slug: "automatically-generate-an-ai-assistant-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "智能体开发"
doc_id: "cdlgtMbj2X"
updated_at: "2026-08-03 09:18:58"
---

> Source: https://open.dingtalk.com/document/aipass/automatically-generate-an-ai-assistant-1
> Path: AI PaaS / DEAP·企业AI平台 / 智能体开发
> Updated: 2026-08-03 09:18:58

# 智能体开发

无论你是否有代码基础，都可以基于 DEAP 打造属于自己的智能体。本文我们将以【行政助理】为例，详细讲解如何创建智能体。

## **步骤一**：新建智能体

1. 进入[Deap开发后台](https://deap.dingtalk.com/#/deap-home)。
2. 在Deap开发后台，在**开发模式**下依次选择**智能体 > 新建智能体**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1086136.png)
3. 在创建智能体弹窗中，填写智能体基本信息，最后单击**确定**即可。

   - **智能体名称**：最多 20 个字符
   - **智能体功能描述**：简单介绍下智能体能做什么
   - **归属部门**：可以选择有管理权限的部门
   - **智能体头像**：可以上传本地图片，建议 200\*200 大小的 JPG 或 PNG 图片

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1085456.png)

## 步骤二：**完善人设信息**

智能体的**人设主要**包括了**角色与设定、兜底回复、设定记忆、欢迎语、引导问题、快捷按钮**六个部分，人设信息会持续影响智能体在所有会话中的回复效果，请根据自己的需求进行设定，让智能体对话更符合预期。

### **角色与设定**

**角色与设定**即对大模型的指令，通常称之为提示词（Prompt），最多可输入 5000 个字符。

提示词是你在创建 智能体时与大模型交流的自然语言，它至关重要，直接决定了 智能体的功能以及如何回答用户问题。人物设定和提示词的质量会影响 智能体的理解效果，因此设定描述越清晰明确，智能体的表现就越符合你的预期。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1085462.png)

例如行政助理的提示词可以设置为：

```
##角色：
你是一个专业的行政管理助手，能够为用户提供行政知识问答、人事申请等服务，确保用户在日常工作中更加高效。
当涉及到知识问答场景时，请基于知识问答能力构建。保证准确回答用户关于知识库中内容的问题，确保信息的准确性和一致性。、
##技能：
1. 仔细理解用户提问的核心意图和关键点
2. 支持知识库中检索最相关的信息（需要提前配置知识库）
3. 组织信息形成清晰、直接的回答
##限制：
1. 拒绝回答涉及敏感信息（违法违规内容、未公开财务数据等）的问题
2. 当知识库中信息不足以完整回答问题时，明确说明并提供已有的相关信息
```

### **兜底回复**

**兜底回复**即AI助理通过学习的知识无法回答时的兜底回复文案，最多可输入 100 个字符。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1085469.png)

例如行政助理的兜底回复可以设置为：

```
抱歉，我暂时无法回答这个问题，请联系行政同学进行咨询。
```

### **设定记忆**

根据实际需求完成记忆设置。

- **是否开启多轮会话**：默认会话轮数为3轮。
- **多轮对话轮次**：设置带入智能体上下文的对话历史轮数。轮数越多，多轮对话的相关性越高，但消耗的 Token 也越多。
- **是否开启长期记忆**：开启后，智能体将重复出现、内容固定的会话内容存储在记忆中，后续调用时无需向大模型传递完整会话内容，仅需传递对话摘要，从而降低token消耗，增强推理准确性。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8296943871/p1085470.png)

### **欢迎语**

**欢迎语**即当用户打开智能体时，会展示的开场文案，主要作用是和用户打招呼、介绍智能体核心功能等，最多可输入 300 个字符。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1085493.png)

例如行政助理的欢迎语可以设置为：

```
您好！我是行政助理小D，可以为您解答各种行政问题，有什么可以帮您？
```

### **引导问题**

**引导问题**用于当用户打开智能体时，引导用户体如何和智能体进行互动，默认 3 个问题，每个问题最多可输入 100 个字符。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8296943871/p1085494.png)

例如行政助理的引导问题可以设置为：

```
1. 公司的差旅报销标准是什么？
2. 病假申请需要提供什么证明？
3. 如何申领办公用品？
```

### **快捷按钮【可选】**

**快捷按钮**即对话框上方的快捷按钮，支持配置链接、锁定技能、预设提示词

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8296943871/p1085498.png)

## 步骤三：添加知识

1. 点击左侧**知识**功能，然后点击**添加知识集**按钮。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8296943871/p1085472.png)
2. 在添加知识集弹窗中，选择已经创建好的知识，然后点击**添加**。

   > **[!NOTE]**
   >
   > 在知识列表中，也可以点击**新建知识集**按钮，创建新的知识集。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8296943871/p1085477.png)
3. 添加成功后，如下所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1085478.png)

## **步骤四：添加技能**

### **添加Skill 技能包**

如果你想让智能体可以执行更丰富的任务，可以在这里添加更多的Skill技能包。

1. 点击左侧**Skill**功能，然后点击**添加Skill**按钮。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1085488.png)
2. 上传准备好的Skill技能zip包，然后点击**确定**即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1085490.png)
3. 添加成功后，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1085492.png)

### **安装MCP工具**

如果你想让智能体可以执行更具体的任务，可以在这里添加更多的MCP工具。

1. 点击左侧**MCP**功能，然后点击**添加MCP**按钮。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1085505.png)
2. 选择目标MCP工具，然后点击右侧的添加即可。

   > **[!NOTE]**
   >
   > 如果你想创建新的MCP工具，可参考[自定义 MCP](0007-manage-ai-assistant-workflow-1.md)。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8296943871/p1085514.png)
3. 添加成功后，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8296943871/p1085515.png)

#### **添加工作流**

如果你想让智能体按照你设置的流程执行某个复杂任务，则可以配置工作流实现。

1. 点击左侧**工作流**功能，然后点击**添加工作流**按钮。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8296943871/p1085519.png)
2. 选择目标工作流，或**新建工作流**后并启用。

   > **[!NOTE]**
   >
   > 如何创建工作流，可参考[新建工作流](0004-create-an-ai-assistant-workflow-1.md)。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8296943871/p1085524.png)
3. 添加成功后，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1085525.png)

## **步骤五：设置权限**

点击左侧**权限**功能，设置权限信息：

- 可以按照**部门**或**人员**为智能体添加权限，只有有权限的部门或个人才能使用该智能体
- 可以选择共同管理员，一起开发和使用智能体

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1085529.png)

## **步骤六：调试与发布**

### **智能体调试**

在发布智能体前，可以在调试面板提前测试下智能体的表现，DEAP 提供了全链路trace追踪调试能力：

- 如果上传了知识集，可提问知识集里的内容，测试回答准确性
- 如果添加了技能，输入和技能相关的提示词，测试技能调用情况

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8296943871/p1085531.png)

### **智能体发布**

完成以上步骤后，就可以发布智能体，智能体可在钉钉内和钉钉外使用。

1. 发布前先点击右上角的**保存**按钮，然后点击**发布**按钮。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1085532.png)
2. 选择发布的渠道，然后点击**发布**即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8296943871/p1085533.png)
3. 发布成功后，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7296943871/p1085536.png)
