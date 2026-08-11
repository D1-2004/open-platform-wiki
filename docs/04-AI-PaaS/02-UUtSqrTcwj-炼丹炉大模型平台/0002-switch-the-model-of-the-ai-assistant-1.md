---
title: "快速入门"
source_url: "https://open.dingtalk.com/document/aipass/switch-the-model-of-the-ai-assistant-1"
namespace: "aipass"
slug: "switch-the-model-of-the-ai-assistant-1"
group: "AI PaaS"
tab: "炼丹炉大模型平台"
breadcrumb: "快速入门"
doc_id: "5JVWIS3gGh"
updated_at: "2025-09-23 19:20:34"
---

> Source: https://open.dingtalk.com/document/aipass/switch-the-model-of-the-ai-assistant-1
> Path: AI PaaS / 炼丹炉大模型平台 / 快速入门
> Updated: 2025-09-23 19:20:34

# 快速入门

本文档介绍如何快速接入企业自有专属大模型和切换钉钉 AI 助理的底模型。

## **炼丹炉大模型服务平台定位**

炼丹炉大模型服务平台是企业级 AI 模型的全生命周期解决方案，不仅集成全球前沿大模型即开即用，更提供从数据治理、高效训练到灵活部署的端到端工具链，助力企业构建安全可控的专属智能引擎。

## **为什么要切换模型**

钉钉炼丹炉一直致力于为企业提供先进的模型一站式服务，我们深知企业在应用 AI 技术时，对**专业性要求、性能要求、多模态要求、计算资源与成本**和**安全合规**上有着迫切且多样化的需求。

基于这些考量，钉钉炼丹炉将不断引进业界顶尖的三方大模型服务，如DeepSeek、MiniMax、智谱AI、月之暗面Kimi、零一万物等，以便客户能够根据具体业务需求，灵活选择和切换不同的大模型服务。

## **接入企业自有专属大模型**

> **[!NOTE]**
>
> 本文档内容主要介绍如何对接企业已有的大模型服务，如果需要在炼丹炉上进行模型精调，请阅读[知识问答](https://open.dingtalk.com/document/aipass/knowledge-creation-nl2knowledge-1)文档。

### **前提条件**

- 在当前企业内申请成为拥有开发者权限的子管理员。
- 购买[魔法棒-AI生产力平台付费版](https://open.dingtalk.com/developer/aipaas)。

### **步骤一：进入炼丹炉大模型训练平台**

1. 登录企业[开发者后台](https://open-dev.dingtalk.com/)。
2. 单击**企业专属大模型平台**，进入炼丹炉大模型训练平台。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8397225471/p946314.png)

### **步骤二：****进入炼丹炉大模型训练平台-我的模型**

1. 在我的模型页面，单击顶部 TAB 的**专属模型**。
2. 单击**对接自有模型**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5660478371/p911869.png)

### **步骤三：对接自有模型**

1. 填写模型基本信息。
2. 配置模型接入 KEY。
3. 联通测试以及提交后，即可出现在**我的模型** > **专属模型**页面中。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5660478371/p911871.png)

## **管理 AI 助理模型列表**

> **[!NOTE]**
>
> 本文档以切换公共大模型为例，如果需要切换为企业训练的专属大模型，可参考该流程的步骤三，直接设置企业专属大模型的使用范围。

### **前提条件**

- 需要在当前企业内申请成为拥有开发者权限的子管理员。

### **步骤一：进入炼丹炉大模型训练平台**

1. 登录企业[开发者后台](https://open-dev.dingtalk.com/)。
2. 单击**企业专属大模型平台**，进入炼丹炉大模型训练平台。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8397225471/p946314.png)

### **步骤二：进入炼丹炉大模型训练平台-体验中心**

1. 单击左侧TAB为体验中心。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4666778171/p810097.png)
2. 选择并授权开启模型（以通义千问-plus为例）：

   - 单击授权按钮。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4666778171/p810099.png)
   - 勾选《钉钉三方订购协议》并点击确定按钮。

### **步骤三：设置模型使用范围**

1. 进入“我的模型”页面。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4666778171/p810100.png)
2. 单击使用范围，设置该模型使用范围。

   使用范围内的员工可在创建钉钉AI助理时切换该模型。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8194659171/p815889.png)
3. 单击提交。

### **步骤四：创建钉钉AI助理**

1. 进入钉钉AI助理创建页面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4666778171/p810107.png)
2. 左上角切换模型。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4666778171/p810109.png)
