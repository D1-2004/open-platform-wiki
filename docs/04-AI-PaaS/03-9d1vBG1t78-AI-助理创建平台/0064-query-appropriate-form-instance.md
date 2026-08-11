---
title: "查询宜搭表单实例"
source_url: "https://open.dingtalk.com/document/aipass/query-appropriate-form-instance"
namespace: "aipass"
slug: "query-appropriate-form-instance"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 工作流 > 钉钉协作 > 宜搭 > 查询宜搭表单实例"
doc_id: "SdeX9GelNk"
updated_at: "2025-09-23 19:19:51"
---

> Source: https://open.dingtalk.com/document/aipass/query-appropriate-form-instance
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 工作流 > 钉钉协作 > 宜搭 > 查询宜搭表单实例
> Updated: 2025-09-23 19:19:51

# 查询宜搭表单实例

用于设置筛选条件，查找符合条件的宜搭表单数据（暂不支持流程表单），在查询宜搭表单实例前，请了解如何在[创建 AI 助理工作流](0037-create-an-ai-assistant-workflow-1.md)时添加执行动作。

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理**

## **操作步骤**

1. 在工作流搭建页面，单击**选择执行动作** > **钉钉协作** > **宜搭**，选择查询宜搭表单实例。
2. 配置查询表单实例执行动作：

   | **配置项** | | **说明** |
   | --- | --- | --- |
   | 应用表单信息 | 应用编码 | 打开你的宜搭应用，单击**应用设置** > **部署运营**，复制获取应用编码和应用密钥。  image |
   | 应用密钥 |
   | 宜搭表单 | 填写应用信息完成后，单击**刷新**按钮。即可选择对应宜搭表单。 |
   | 过滤条件 | | 通过设置表单字段的过滤条件，查找满足条件的实例。  例如，你有一张库存管理表单，你想筛选库存数量大于 5 的实例数据，就可以这样进行配置。  image |
   | 排序规则 | | 按照表单中的某个字段进行升序或降序排列。 |
   | 查询条数 | | 仅支持查询排序后的前 n 条实例，最大可设置为前 50 条。 |
