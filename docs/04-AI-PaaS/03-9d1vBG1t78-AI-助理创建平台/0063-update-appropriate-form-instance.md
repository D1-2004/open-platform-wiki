---
title: "更新宜搭表单实例"
source_url: "https://open.dingtalk.com/document/aipass/update-appropriate-form-instance"
namespace: "aipass"
slug: "update-appropriate-form-instance"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 工作流 > 钉钉协作 > 宜搭 > 更新宜搭表单实例"
doc_id: "MOlQHbOQSZ"
updated_at: "2025-09-23 19:19:51"
---

> Source: https://open.dingtalk.com/document/aipass/update-appropriate-form-instance
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 工作流 > 钉钉协作 > 宜搭 > 更新宜搭表单实例
> Updated: 2025-09-23 19:19:51

# 更新宜搭表单实例

用于对宜搭表单中已有的某行数据进行更新（暂不支持流程表单），在使用更新宜搭表单实例前，请了解如何在[创建 AI 助理工作流](0037-create-an-ai-assistant-workflow-1.md)时添加执行动作。

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理**

## **操作步骤**

1. 在工作流搭建页面，单击**选择执行动作** > **钉钉协作** > **宜搭**，选择更新宜搭表单实例。
2. 配置更新宜搭表单实例执行动作：

   | **配置项** | | **说明** |
   | --- | --- | --- |
   | 应用表单信息 | 应用编码 | 打开你的宜搭应用，单击**应用设置** > **部署运营**，复制获取应用编码和应用密钥。  image |
   | 应用密钥 |
   | 宜搭表单 | 填写应用信息完成后，单击**刷新**按钮。即可选择对应宜搭表单。 |
   | 要更新的实例 | 固定条数 | 填写待更新的实例ID。  image |
   | 动态条数 | 动态赋值实例ID，例如，你可以在前置步骤添加 「查询宜搭表单实例」执行动作，然后在此处引用它的输出变量「查询到的表单实例-实例 ID」。这样，你就可以对查找到的符合条件的实例进行更新。  image |
   | 表单字段内容 | | 填写宜搭表单中的字段内容。  当前仅支持日期、数值、下拉复选、下拉单选、单行文本、多行文本、人员这几种类型的字段。 |
