---
title: "客服助理操作手册"
source_url: "https://open.dingtalk.com/document/aipass/customer-service-assistant-operation-manual-1"
namespace: "aipass"
slug: "customer-service-assistant-operation-manual-1"
group: "AI PaaS"
tab: "AI 客服助理"
breadcrumb: "客服助理操作手册"
doc_id: "d4rxpGZCTQ"
updated_at: "2025-09-23 19:20:59"
---

> Source: https://open.dingtalk.com/document/aipass/customer-service-assistant-operation-manual-1
> Path: AI PaaS / AI 客服助理 / 客服助理操作手册
> Updated: 2025-09-23 19:20:59

# 客服助理操作手册

本文从三个视角：开发者&管理员的配置视角、用户视角、服务人员视角，阐述了客服助理的操作流程

## **开发者&管理员**

### **创建 AI 客服助理**

1. 打开钉钉客户端，单击 **AI 助理** > **助理市场**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7689655471/p949361.png)
2. 在助理市场页面，单击**客服助理**，进入客服创建页面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7689655471/p949365.png)
3. 在客服助理页面，你可以单击立即体验/新建，创建属于你的 AI 客服助理。

   > 需要开通试用版才能进行使用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7689655471/p949368.png)
4. （可选）如果你需要共同协作开发，管理员可先将开发者设置成助理的共同管理员，方便开发者进行后续的助理编辑和发布。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7689655471/p949374.png)

### **配置 AI 客服助理**

| **能力** | | **说明** |
| --- | --- | --- |
| 基础信息 | 名称 | - 填写助理名称。 - 编辑助理头像。 - 填写助理介绍信息。   image |
| 头像 |
| 介绍 |
| 欢迎语和开场白 | | 填写用户欢迎信息以及预置开场内容。 |
| 兜底回复 | | 当知识问答无法查找到对应信息后，将会路由至兜底回复。支持 markdown 格式。 |
| 知识 | | 你可以上传客服知识信息，可参考[维护知识内容](../03-9d1vBG1t78-AI-助理创建平台/0075-management-knowledge-1.md)。 |
| 人工服务 | | 客服助理核心能力，当知识内容无法回答用户信息时，支持添加服务人员：   - 根据「服务时段」、「技能」分配服务人员。  image - 智能辅助能力，支持开启辅助接待和辅助沉淀能力。  image |
| （可选）端外配置 | | 钉钉 AI 客服支持支持发布到端外：   - 在微信公众号以插件的形式接入。 - 在企业自建 APP 中接入。 - 在 Web 网页中接入。   仅企业主管理员有权限允许端外接入。  image |

配置完成后，即可发布上线。

### **洞察数据信息**

你可以在**分析** > **客服助理**中查看对应的数据信息，帮助你精准分析客服数据。

#### image

## **使用人员**

### **发起问题并转交人工**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7689655471/p949396.png)

所有转人工方式，均以你编辑设置的人工规则为准。

## **人工服务人员**

### **人工服务承接通知**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7689655471/p949404.png)

### **AI 生成推荐方案**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7689655471/p949405.png)

### **完结人工服务**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7689655471/p949409.png)

### **智能沉淀FAQ**

人工服务完结，且用户评价为满意后，人工服务对话内容会被总结生成FAQ并推送给服务人员，服务人员可以选择是否将FAQ添加到问答知识库中：

1. 生成 FAQ 的逻辑说明：

   - 条件1：进入人工服务。
   - 条件2：并且有客户明确的提问以及客服的明确回答。
   - 条件3：完结人工服务并且对人工服务的评价为**满意**。

   三个条件同时满足的前提下，会尝试生成 QA 发送给客服，由客服决策是否需要保存这个 QA 作为标准问答。最后要客服小二明确操作将 QA 保存到标准问答，否则不会被记录。
2. 关注触发助理学习 FAQ 知识，需在智能问答设置里边，设置知识学习的学习频次，修改成每天学习一次，这样新增的内容在第二天就学习完成了。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7689655471/p949411.png)
