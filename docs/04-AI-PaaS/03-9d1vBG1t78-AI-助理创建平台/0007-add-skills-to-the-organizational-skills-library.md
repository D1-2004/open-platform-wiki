---
title: "添加技能到组织技能库"
source_url: "https://open.dingtalk.com/document/aipass/add-skills-to-the-organizational-skills-library"
namespace: "aipass"
slug: "add-skills-to-the-organizational-skills-library"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "创建 AI 助理 > 添加技能到组织技能库"
doc_id: "9eT1ljlLA1"
updated_at: "2025-09-23 19:19:07"
---

> Source: https://open.dingtalk.com/document/aipass/add-skills-to-the-organizational-skills-library
> Path: AI PaaS / AI 助理创建平台 / 创建 AI 助理 > 添加技能到组织技能库
> Updated: 2025-09-23 19:19:07

# 添加技能到组织技能库

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理**

## **概述**

**专业开发者和小白用户之间协同开发 AI 助理，进入应用开发的新范式！**

通过共享组织技能库能力，由专业开发者提供 API 来实现 AI 技能，共享给组织全员使用后。组织内的员工可以基于组织内共享的技能来开发个性化 AI 助理，实现业务流程的自定义配置！

让企业的应用开发，从传统的模式中全部由专业开发者来开发，转变为专业开发者提供业务操作的技能，其他员工根据自身需求选择组织技能库定制个性化助理，满足个性化需求。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6634010471/p892817.png)

## **场景一：工程师开发技能共享给其他用户使用**

工程师基于全代码的 API 开发，开发 AI 技能后，共享给组织内全员使用。组织内的员工，不用掌握专业的开发能力，也可以基于共享的技能搭建自己的 AI 助理。

### **操作步骤**

1. 添加“自定义能力”类型的技能或编排“工作流”类型的技能，具体详情可参考文档[自定义能力](0024-overview-6.md)和[工作流](0036-overview-7.md)。

   ![自定义能力:工作流技能](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6634010471/p892840.png)
2. 技能编辑完成后，你可以选择对应技能，并上传至组织技能市场。

   > **[!NOTE]**
   >
   > **上架到组织技能库**按钮仅**企业主管理员**和**具有开发者权限的子管理员**可见，其他成员暂无权限。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6634010471/p892858.png)
3. 操作完成后，其他成员如需要添加该技能，即可进入助理市场，在组织技能库下进行添加。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6634010471/p892876.png)

## **适用客群**

面向有代码开发能力，并通过钉钉 AI 技能方式开发 AI 助理的开发者。

## **所属商业化版本**

钉钉 AI 生产力平台定制版

## **常见问题**

- ### **为什么我看不到“上架到技能库”按钮？**

  答：目前只有企业主管理员以及拥有开发者权限的子管理员才可以看见并操作，其他成员需要申请相应权限。
- ### **如何删除在组织技能库中上架的技能？**

  答：企业主管理员或者应用管理子管理员，在组织技能库找到需要删除的技能，鼠标浮上去后，会显示删除按钮。点击删除按钮即可完成删除动作。
- ### **为什么有的技能不支持上架到技能库？**

  答：当前仅支持“自定义能力”技能和“工作流”技能。

## **相关文档**

- [工作流开发指南](0036-overview-7.md)
- [自定义能力开发指南](0025-development-guide.md)
