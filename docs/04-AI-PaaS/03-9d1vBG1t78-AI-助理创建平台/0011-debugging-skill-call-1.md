---
title: "调试技能调用"
source_url: "https://open.dingtalk.com/document/aipass/debugging-skill-call-1"
namespace: "aipass"
slug: "debugging-skill-call-1"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "调试 AI 助理 > 调试技能调用"
doc_id: "Dms4kaNvDd"
updated_at: "2025-10-21 14:08:53"
---

> Source: https://open.dingtalk.com/document/aipass/debugging-skill-call-1
> Path: AI PaaS / AI 助理创建平台 / 调试 AI 助理 > 调试技能调用
> Updated: 2025-10-21 14:08:53

# 调试技能调用

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理/助理市场创建的 AI 助理**

## **概述**

善用助理调试平台，自定义技能异常从毫无头绪到 5 分钟自助解决！

开发自定义能力的时候，可能会出现技能调用失败的问题。为了让 AI 助理开发者可以高效地分析和解决这类异常，提供调试技能调用的能力。

## **适用场景**

### **场景一：**开发过程中出现技能调用失败

用户在开发 AI 助理的过程中，通过预览页面调试时候，可能会出现自定义技能调用失败。请求是通过钉钉 AI 助理平台发起，助理开发者可能会缺乏对该问题的快速解决方法。

此时，可以通过钉钉 AI 助理的调试能力来分析问题原因。

#### **操作步骤**

1. 在助理预览页面发现请求异常。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4760682371/p879153.png)
2. 单击右上角**日志**，在调试节点列表中，找到并进入技能调用节点，查看响应的详细信息。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4760682371/p879151.png)
3. 基于响应结果的 403 错误码，查看技能调用的输入（即 HTTP Request 信息），通过查看，发现出现请求 URL 错误，出现了“gett”，正确的应为“get”。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4760682371/p879170.png)
4. 基于以上错误信息，基本可以判断错误原因可能是自定义能力技能的 YAML 配置文件错误，此时：

   1. 检查技能 YAML 配置文件。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4760682371/p879171.png)
   2. 发现配置文件 paths 配置错误，修复错误，重新调试。

## **能力边界**

该调试能力只能诊断钉钉与开发者服务之间调用过程，无法诊断开发者代码内部问题。例如开发者自身的 Java、Python 等代码异常无法通过钉钉的调试能力解决。开发者可以通过 IDE、自身系统日志等方式自行诊断。

## **适用客群**

该能力面向具备代码开发能力，且通过钉钉自定义技能方式，开发 AI 助理的开发者。

## **常见问题**

- ### **助理的使用者，而不是助理的开发者，能否使用该调试能力？**

  **答：**不能。技能调用的调试过程中，涉及大量助理开发过程中的技术细节，一方面这些技术细节有一定的技术深度，普通用户无法理解，另一方面助理开发者也不希望这些技术细节被其他人看到。
- ### **在调试中，发现请求内容不符合预期，怎么修改参数和请求信息？**

  **答：**可以参考这个自定义技能的[高级设置](0026-advanced-settings.md)文档，深入学习钉钉 AI 助理平台提供的丰富能力。
- ### **为什么调试信息中，有些字段显示为星号（\*\*\*\*\*\*）?**

  **答：**基于安全和隐私考虑，在调试中对于隐私信息做了脱敏处理，包括钉钉平台侧非公开信息，以及用于鉴权的 Token 或 Secret 之类的信息。典型的案例包括 HTTP 请求中的 Authorization 头，以及钉钉官方技能中用到的 uid 信息。

  备注：uid 仅用于钉钉平台内部应用，对于生态开发者，钉钉通过开放平台提供 Union ID 和 User ID，详见[基础概念](https://open.dingtalk.com/document/development/development-basic-concepts)文档。
- ### **HTTP 请求头中的 x-dingtalk-unifiedAppId 是什么？**

  **答：**每个钉钉 AI 助理对应一个开放平台的应用，x-dingtalk-unifiedAppId 对应开放平台的统一应用 ID。当你的 AI 助理用到开放平台相关特性的时候，可能会涉及应用开发相关能力。例如通过 Stream 开发自定义技能、在自定义技能中调用钉钉开放平台的 OpenAPI 等。
- **如何诊断 AI 助理响应慢的问题？**

  **答：**在调试台中，每个节点的信息中都显示了开始时间和结束时间，以及当前节点的耗时，通过这些信息可以快速分析为什么响应变慢了。

## **参考文档**

- [AI 助理开发文档：自定义技能的高级设置说明](0026-advanced-settings.md)
- [开放平台基础概念](https://open.dingtalk.com/document/development/development-basic-concepts)
