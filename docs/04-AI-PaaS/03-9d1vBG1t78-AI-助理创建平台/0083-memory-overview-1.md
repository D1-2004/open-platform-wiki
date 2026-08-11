---
title: "个性化概述"
source_url: "https://open.dingtalk.com/document/aipass/memory-overview-1"
namespace: "aipass"
slug: "memory-overview-1"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 个性化 > 个性化概述"
doc_id: "V1AJa5EOaZ"
updated_at: "2025-09-23 19:20:17"
---

> Source: https://open.dingtalk.com/document/aipass/memory-overview-1
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 个性化 > 个性化概述
> Updated: 2025-09-23 19:20:17

# 个性化概述

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理/助理市场创建的 AI 助理**

## **什么是个性化**

个性化能力可以让 AI 助理记住使用者的个人信息、企业专有术语等信息，从而让助理回复更加千人千面，当前个性化能力支持以下功能：

- 钉钉数据变量：一键导入用户在钉钉内沉淀的办公数据作为AI助理的记忆，例如用户的岗位。
- 自定义记忆变量：除了导入钉钉数据外，还可以通过创建自定义变量来保存用户信息。定义相关变量后，AI 助理在对话过程中，可以根据用户输入内容进行语义匹配，为定义的变量赋值并保存值。
- 术语库：术语的主要功能是弥补 AI 助理在特定业务领域方面的理解不足，通过具备解释含义的业务数据，帮助AI助理在回答时理解业务内部专有词汇设置术语。

## **应用场景**

- 导入钉钉数据作为记忆，实现基于员工个人信息的日程管理等场景。

  > 创建AI助理时，通过导入钉钉数据变量“用户的部门信息”，AI助理会记住该信息，并在创建相关日程时进行参考。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6014062371/p877631.png)
- 使用自定义变量，创建一个了解招聘背景的HR助理。

  > 例如，HR 部门搭建的招聘助理，可以通过设置“岗位 JD ”和“评估标准”两个记忆变量，来让 AI 助理在评估候选人时根据记忆变量来进行分析，解决了通用AI助理评估过于宽泛的痛点，并且不同员工还可以设置不同的变量值，实现千人千面的效果。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6014062371/p877640.png)
- 利用术语库能力，让AI助理记住企业内部黑话。

  > 例如，可以通过术语库能力来维护企业内部业务词典、企业黑话和企业特有的知识、一些特殊称谓，或者简称、别名、定义之类的内容；还有一些指标的定义，比如总利率的计算方式是 \*\*。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6014062371/p877645.png)

## **适用范围**

个性化能力在有无研发能力的大型企业和中小型企业均可使用落地。
