---
title: "自定义能力概述"
source_url: "https://open.dingtalk.com/document/aipass/overview-6"
namespace: "aipass"
slug: "overview-6"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 能力 > 自定义能力 > 自定义能力概述"
doc_id: "XuL1Dp8ILH"
updated_at: "2025-09-23 19:19:26"
---

> Source: https://open.dingtalk.com/document/aipass/overview-6
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 能力 > 自定义能力 > 自定义能力概述
> Updated: 2025-09-23 19:19:26

# 自定义能力概述

本文介绍了钉钉 AI 自定义能力开发的基本信息和开发方式。

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理/助理市场创建的 AI 助理**

## 介绍

钉钉 AI 的自定义能力，使开发者可以根据自身业务特性，量身定制 AI 助理的行为。利用这一开发方式，开发者能够将 AI 助理与自身的业务系统无缝衔接，从而提供更为个性化的服务体验。借助于自定义功能，开发者可赋予 AI 助理多样化的技能，如查询天气、生成业务报表、预订机票与酒店、自动化填写审批表单等。

## **自定义能力类型**

钉钉 AI 自定义能力提供了 OpenAPI 开发方式。

### **OpenAPI**

开发者可以将现有业务接口用于开发 AI 的自定义能力。你只需根据 [OpenAPI 标准规范](https://swagger.io/specification/)来编写当前接口的描述文件，并将该描述文件上传至高级自定义能力开发页面，即可完成自定义能力的开发。具体的开发流程和细节参考 [开发指南](0025-development-guide.md)。

## **基本概念**

#### **Action**

AI 助理执行的一个具体的 OpenAPI 接口 或 自动化脚本。

#### **Actions**

一组 Action（OpenAPI或自动化脚本）的集合，通常使用一个 OpenAPI 或 自动化脚本 描述文件来描述。

#### **OpenAPI 描述文件**

符合 OpenAPI 3.0 规范的描述文件，采用 YAML 格式描述，该文件可以描述 OpenAPI 的元信息，方便大模型理解和调用接口。

## **相关文档**

### **OpenAPI**

- [开发指南](0025-development-guide.md)
- [高级设置](0026-advanced-settings.md)
- [鉴权方式](0027-authentication-method.md)
