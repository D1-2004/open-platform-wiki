---
title: "配置个性化信息"
source_url: "https://open.dingtalk.com/document/aipass/configuration-memory-1"
namespace: "aipass"
slug: "configuration-memory-1"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 个性化 > 配置个性化信息"
doc_id: "AbN5HkLBqQ"
updated_at: "2025-09-23 19:20:18"
---

> Source: https://open.dingtalk.com/document/aipass/configuration-memory-1
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 个性化 > 配置个性化信息
> Updated: 2025-09-23 19:20:18

# 配置个性化信息

如果你需要使用记忆相关能力，请了解如何在[创建组织内使用的 AI 助理](0005-create-a-dingtalk-ai-assistant-1.md)时进入 AI 助理创建页面。

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理/助理市场创建的 AI 助理**

## 背景信息

助理开发者可以通过创建变量来保存用户个人信息，并让AI助理记住这些特征，使回复更加个性化。变量以 key-value 形式存储用户的某一行为或偏好。

## **操作步骤**

1. 在 AI 助理创建平台，单击**个性化**，进入个性化配置页面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9114062371/p877658.png)
2. 在个性化配置页面，你可以实现配置：

   - **钉钉数据变量**，你可以选择用户在钉钉平台上的数据作为变量的默认值，例如用户的职位、用户的主管信息等。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9114062371/p877659.png)
   - **自定义记忆变量**，需要设置变量名称、默认值（选填）和描述。建议填写准确的变量名称与描述，来让大模型更好地理解该记忆变量的用途。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9114062371/p877660.png)
   - **术语库，**你可以通过设置术语，来让AI助理理解企业所使用的专业名词或特定业务逻辑。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9114062371/p877661.png)

## **常见问题**

- ### **能否支持记忆变量结合知识问答，实现基于员工信息的个性化问答服务？**

  答：支持。
- ### **公司在自己的业务系统中沉淀了一些数据，能否通过开放的方式导入AI助理的个性化记忆？**

  答：可以通过 API 接口的形式进行导入，需要先在数据资产平台和钉钉的员工主数据 ID 对接。
- ### **能否记录AI助理和用户的所有对话记录？**

  答：不支持。
- ### **最多能添加几条自定义记忆变量？**

  答：你最多只能创建 10 条自定义记忆变量
- ### **如何变更记忆**

  答：当前自定义变量不支持通过语义识别来赋值，必须使用触发指令，例如：帮我记住我的职务是：CIO。

  > 变更的记忆变量必须为自定义变量中存在且支持变更的字段。
