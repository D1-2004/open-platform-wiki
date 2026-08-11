---
title: "使用标准问答对"
source_url: "https://open.dingtalk.com/document/aipass/using-the-faq-knowledge-template-1"
namespace: "aipass"
slug: "using-the-faq-knowledge-template-1"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 知识 > 知识维护 > 使用标准问答对"
doc_id: "OxKqlTKZ0e"
updated_at: "2025-09-23 19:20:12"
---

> Source: https://open.dingtalk.com/document/aipass/using-the-faq-knowledge-template-1
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 知识 > 知识维护 > 使用标准问答对
> Updated: 2025-09-23 19:20:12

# 使用标准问答对

如果你需要使用 AI 助理知识问答技能回答 FAQ 相关内容，你可以提前了解[维护知识内容](0075-management-knowledge-1.md)。

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理**

## **背景信息**

高频问题答案输出不稳定，使用FAQ多维表维护标准问答对，FAQ 知识模板主要使用于智能问答场景，在该场景下可以通过 FAQ 的方式维护标准问题，在问答过程中一旦命中标准问题，则强制保障输出结果的一致性。该方式重点适用于医疗、法律等对问答结果有标准化要求的行业，不希望模型回答的内容过于发散。

## **操作步骤**

1. 登录[钉钉文档](https://alidocs.dingtalk.com/i/desktop/my-space)，单击右上角**模板**按钮，进入钉钉文档模板中心。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4201139171/p814455.png)
2. 选择**热门推荐** > **FAQ 知识**模板，并单击**使用**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4201139171/p814466.png)
3. 配置 FAQ 知识多维表：

   | **字段信息** | **说明** |
   | --- | --- |
   | 标准问题（必填） | 必填字段，用于描述问题。  - **示例：**忘记密码应该怎么办？ |
   | 相似问题（非必填） | 非必填字段，用于添加与标准问题相似的问法，多个问法通过换行（回车）进行区分。  - **示例：** 如何找回密码？  忘记密码如何登录？  忘记密码如何处理？  **[!NOTE]**  多个相似问题，无需添加富文本内的其他格式（例如无序列表），换行即可。 |
   | 分类（非必填） | 非必填字段，单选，用于将问题进行类别区分，分类选项可以自行添加。 |
   | 答案（必填） | 必填字段，用于填写该问答的答案。    - **示例：**通过以下三种方式找回密码：1.通过信任手机找回密码：使用您的信任手机号码获取短信验证码，之后需要输入证件/护照后四位进行身份校验，最后重新设置密码。2.通过安全码找回：在界面输入您的域账号或者工号，之后需要输入证件/护照后四位进行身份校验，最后系统会将安全码发到您的主管手机上。请您联系主管获取安全码输入完成重置密码（安全码有效时间为15分钟，请用户尽快联系主管获取安全码）。3.原有忘记密码重置方式：输入您的域账号与验证码，选择重置方式：A.使用预留手机（信任手机验证码重置），需要校验您的身份证号码、员工工号、获取信任的验证码，验证通过之后即可来重设您的密码。B.如果不符合使用预留手机号码来重置密码，请点击此处，由IT同学协助您处理。 **[!NOTE]**  本区域支持富文本内的所有格式。 |
   | 创建人 | FAQ 创建用户。 |
   | 创建时间 | FAQ 创建时间。 |
   | 更新人 | FAQ 更新用户。 |
   | 更新时间 | FAQ 更新时间。 |

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4201139171/p814478.png)

   FAQ 知识补充完成后，你可以在智能问答中进行添加了。

## **注意事项**

- **请勿改动 FAQ 知识模板表头。**
- **请勿改动 FAQ 知识模板表头。**
- **请勿改动 FAQ 知识模板表头。**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5651139171/p814489.png)
