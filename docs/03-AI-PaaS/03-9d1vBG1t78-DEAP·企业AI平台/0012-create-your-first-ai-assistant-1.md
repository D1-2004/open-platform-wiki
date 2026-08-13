---
title: "自有模型接入"
source_url: "https://open.dingtalk.com/document/aipass/create-your-first-ai-assistant-1"
namespace: "aipass"
slug: "create-your-first-ai-assistant-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "模型管理 > 企业模型 > 自有模型接入"
doc_id: "9m7T53oyaw"
updated_at: "2026-07-08 15:00:31"
---

> Source: https://open.dingtalk.com/document/aipass/create-your-first-ai-assistant-1
> Path: AI PaaS / DEAP·企业AI平台 / 模型管理 > 企业模型 > 自有模型接入
> Updated: 2026-07-08 15:00:31

# 自有模型接入

## **概述**

自有模型对接功能旨在为开发者或企业提供高效和灵活的方式，将其自有的大模型服务无缝集成到平台中，满足其多样化的业务需求。无论您是希望通过阿里云百炼SDK调用大模型，还是对接在云上部署的自有模型，本功能都能提供便捷的接入途径。

## **目标用户**

- 拥有自研的大模型平台，并希望将其集成到钉钉业务流程中的开发者和企业。
- 希望通过灵活的模型对接方案，定制化满足特定大模型生成需求的平台用户。

## **自有模型对接**

> **[!NOTE]**
>
> 自有模型接入不支持DEAP标准版，需要开通**DEAP旗舰版**，如需接入请咨询钉钉企业AI业务专家。

1. 进入 [DEAP 开发后台](https://deap.dingtalk.com/#/sub-app/model-manage)，在**管理模式**下，依次选择**模型管理 > 自有模型 > 自有模型对接**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1304943871/p1085690.png)
2. 在弹出的弹窗中填写自有模型对接的信息，填写完成后点击**确定**按钮。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1304943871/p1086149.png)

   - **模型名称**：在 "模型名称" 输入框中输入您的模型名称。
   - **图标**：上传一个图片作为模型图标。请注意，建议尺寸为 240\*240，格式为 JPG 或 PNG
   - **模型描述**：在 "模型描述" 文本框中填写您模型的详细描述，这将帮助用户了解模型的特点与优势
   - **模型类型**：在 "模型类型" 部分，目前已默认选中 "文本生成"
   - **模型安全等级**：点击 "请选择模型安全等级" 下拉框。您可以点击 "[钉钉 AI 模型安全策略说明](0011-dingtalk-ai-model-security-policy-description-1.md)" 了解更多信息
   - 根据您的模型部署情况，选择合适的接入方式。目前有两个选项：

     - 通过阿里云百炼 SDK 来调用大模型：

       ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1304943871/p1086150.png)

       - 在 "ModelId" 输入框中填写您模型的ID
       - 在 "API-KEY" 输入框中填写您模型的 API-KEY
     - 接入在云上部署的自有模型：

       ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1304943871/p1086151.png)

       - 点击 "请选择模型提供商" 下拉框，选择您的模型所属的提供商
       - 在 "ModelId" 输入框中填写您自有模型的 ID
       - 在 "BaseUrl" 输入框中填写您的模型调用地址。请注意，这里需要填写完整的调用地址，例如示例中给出的 `https://api.abc.com/v1/chat/completions`
       - 在 "API-KEY" 输入框中填写您模型的 API 密钥
   - **测试连通性**：点击 "测试连通性" 按钮，以验证您的模型连接是否正常。
3. 点击**提交**按钮，进行保存。
