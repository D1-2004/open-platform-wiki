---
title: "概述"
source_url: "https://open.dingtalk.com/document/aipass/ai-assistant-overview"
namespace: "aipass"
slug: "ai-assistant-overview"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "概述"
doc_id: "spgNklWkpm"
updated_at: "2026-08-07 14:51:49"
---

> Source: https://open.dingtalk.com/document/aipass/ai-assistant-overview
> Path: AI PaaS / DEAP·企业AI平台 / 概述
> Updated: 2026-08-07 14:51:49

# 概述

## **什么是DEAP**

[**钉钉企业AI平台（Dingtalk Enterprise AI Platform，简称“DEAP”）**](https://deap.dingtalk.com/#/deap-home)，是钉钉面向企业客户打造的新一代企业级AI平台，致力于为企业提供从底层模型管理到上层智能应用落地的全链路、可治理、高安全、易集成的AI应用及能力支持体系。

DEAP围绕企业真实业务场景，打通 「模型-数据-技能-应用」 四大核心环节，构建覆盖「海量模型管理-业务数据治理-企业技能接入-智能体轻量搭建」的端到端一站式AI解决方案，助力企业构建效果稳定、逻辑可靠、体验流畅的高质量（90分以上）的AI智能体。

钉钉企业AI平台（Dingtalk Enterprise AI Platform，简称"DEAP"），是钉钉面向企业客户打造的新一代企业级AI平台，致力于为企业提供从底层模型管理到上层智能应用落地的全链路、可治理、高安全、易集成的AI应用及能力支持体系。

DEAP围绕企业真实业务场景，打通「模型-数据-技能-应用」四大核心环节，构建覆盖「海量模型管理-业务数据治理-企业技能接入-智能体轻量搭建」的端到端一站式AI解决方案，助力企业构建效果稳定、逻辑可靠、体验流畅的高质量（90分以上）的AI智能体。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6296943871/p1085443.png)

## 企业智能体落地的五大挑战

在企业落地AI智能体的过程中，普遍面临以下核心痛点：

- **智能体搭建门槛高**

  企业的场景和流程繁多，AI应用的需求层出不穷，但智能体搭建的门槛使得需要专业AI人员去构建应用。
- **担忧企业数据泄露**

  AI应用强依赖企业内部的知识、经营数据等有较高隐私性的内容，智能体部署在云端有数据泄露的风险。
- **AI资产难管理**

  对于中大型组织，如何实现企业AI资产（模型、技能、知识、智能体）的分级、分权的有效管理与运营。
- **企业集成难度高**

  专属企业级智能体需要调用内部的系统、流程等，并且需要将智能体嵌入到已有的业务系统中。
- **应用效果难以保障**

  从头构建复杂应用的试错成本高，构建出来的智能体难以达到生产级效果，缺乏专业的评测体系保证应用效果。

## **核心功能模块**

DEAP 提供六大核心模块，覆盖智能体从搭建到运营的全生命周期：

### **智能体管理**

涵盖[智能体开发](0002-automatically-generate-an-ai-assistant-1.md)**、**[智能体评测](0003-experience-preset-ai-assistant-1.md)两部分。在这里完成智能体的创建与管理、效果评测以及全链路观测分析。

### **MCP 管理**

涵盖[内置 MCP](0005-prompt-word-prompt-1.md)**、**[三方 MCP](0006-role-setting-in-ai-assistant-1.md)**、**[自定义 MCP](0007-manage-ai-assistant-workflow-1.md)三部分。钉钉提供19个官方技能和13个三方技能（持续上新中），企业也可自定义创建MCP技能。

### **知识管理**

涵盖[知识集](0008-distribution-of-ai-assistant-1.md)**、**[评测集](0009-add-skills-to-the-organizational-skills-library.md)两部分。统一管理智能体所需的知识集、评测数据集和模型训练数据集。

### **模型管理**

涵盖[模型广场](0010-distribution-of-ai-assistant.md)**、**[企业模型](0012-create-your-first-ai-assistant-1.md)两部分。汇聚33款模型供选择（持续上新中），并支持对接自有模型、训练专属模型。

### **运营中心**

提供[数据看板](0013-operation-process.md)，帮助企业实时掌握智能体的使用情况，包括创建量、活跃度、满意度等关键指标。

### **安全与权限**

涵盖[角色授权](0014-share-dingtalk-ai-assistant.md)**、**[敏感词管控](0015-debugging-skill-call-1.md)两部分，确保智能体权限可控、安全运行。

## **典型应用场景**

### **智能感知场景**

通过智能情景识别，**主动&实时监测**群消息等相关信息事件，结合**上下文理解、精准知识推理及检索、深度分析**决定响应策略，同时完成**自然回应**及**自动化操作**的专业闭环执行，可实现7\*24小时覆盖，标准化问题100%秒级响应。

**应用场景举例：客户群答疑Agent**

![客户群答疑Agent](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6296943871/p1085444.png)

### **智能问答场景**

**打通钉钉文档、企业本地知识、在线网页等**，支持5000量级文件的知识库学习；具备丰富**知识调优**能力，可编辑切片、修改解析策略、添加经验/术语/FAQ等提升回答准确性与相关性，助力企业构建并沉淀高质量知识资产。

![售后维修助理Agent](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6296943871/p1085445.png)

### **智能问数场景**

支持**复杂场景多维度指标查询**，**对话式数据分析**，即问即答，快速响应，低门槛上手完成自助式数据洞察；洞察分析现状的同时，可**预测未来趋势**，并提出优化建议，为企业带来数据驱动的智能化运营，赋能企业高效决策。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6296943871/p1085446.png)

## **为什么选择DEAP**

### **安全可控（敢用）**

- **权限继承**：完整继承钉钉组织架构与权限体系，实现细粒度分级管控
- **资产可控**：企业数据、模型、智能体资产统一管理，保障所有权与可控性
- **安全无损**：企业既有数据权限“无损”集成，避免数据泄露风险
- **高规格保障（本地）**：支持AI数据本地化部署，满足高合规要求

### **深度融合（可用）**

- **全域感知**：全域感知钉钉产品能力，触发Agent执行
- **业务协同**：深度嵌入钉钉日常协作场景，实现智能体自然触达，支持MCP、Response API、H5 Copilot等多类型企业业务系统集成，打通跨系统协作瓶颈
- **全域投放**：支持单聊、群聊、网页版等多渠道投放

### **效果保障（好用）**

- **专业进化**：支持知识与模型精细化调优，打造专业级智能体
- **闭环优化**：构建“数据观测—效果评估—迭代优化”的闭环机制，实现AI能力持续进化

## **联系我们**

- **获取专业服务**：点击[联系我们](https://page.dingtalk.com/wow/dingtalk/default/dingtalk/216383e63f2c4de28bca529572153f63)，填写企业信息，专属客服会尽快与你取得联系。
- **产品问题反馈**：若您在使用过程中遇到产品问题，可通过填写[DEAP·企业AI平台 问题反馈表](https://alidocs.dingtalk.com/notable/share/form/v01Mp7ld7bdowpmvOBQ_dv19yqvsgs3oebp3pcjys_iqwfn5noxsbxnbs45oafp)进行反馈。
