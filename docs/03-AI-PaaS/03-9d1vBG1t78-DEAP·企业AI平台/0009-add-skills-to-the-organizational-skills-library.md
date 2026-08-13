---
title: "评测集"
source_url: "https://open.dingtalk.com/document/aipass/add-skills-to-the-organizational-skills-library"
namespace: "aipass"
slug: "add-skills-to-the-organizational-skills-library"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "知识管理 > 评测集"
doc_id: "9eT1ljlLA1"
updated_at: "2026-07-08 15:48:54"
---

> Source: https://open.dingtalk.com/document/aipass/add-skills-to-the-organizational-skills-library
> Path: AI PaaS / DEAP·企业AI平台 / 知识管理 > 评测集
> Updated: 2026-07-08 15:48:54

# 评测集

评测集是经过人工标注或权威来源验证的标准化数据集合，用于评测智能体在指定目标下的表现。

> **[!NOTE]**
>
> 评测集功能不支持DEAP标准版，需要开通**DEAP旗舰版**，如需接入请咨询钉钉企业AI业务专家。

## **操作步骤**

1. 进入 [DEAP 开发后台](https://deap.dingtalk.com/#/sub-app/model-manage)，依次选择**评测集 > 新建评测集**。

   > **[!NOTE]**
   >
   > 评测集功能不支持DEAP标准版，需要开通**DEAP旗舰版**，如需接入请咨询钉钉企业AI业务专家。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4396943871/p1085719.png)
2. 在添加数据界面，选择评测对象类型、导入方式和智能体知识，点击**下一步**进入评测集设置界面。

   - **评测对象类型**：选择智能体评测。
   - **选择导入方式**：选择智能生成，DEAP 提供了两种评测集创建方式，一种是智能生成，一种是本地上传：

     - **智能生成：**大模型将根据智能体知识自动生成样本问题和答案，随机抽样，最多100条
     - **本地上传：**支持csv、xlsx、xls格式，每个文件不超过100M，仅支持单个文件上传，请按照[评测集模板.xlsx](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20260706/mmkoky/%E8%AF%84%E6%B5%8B%E9%9B%86%E6%A8%A1%E6%9D%BF.xlsx)模板上传。
   - **选择智能体知识**：选择已经创建好的智能体。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4396943871/p1085723.png)
3. 在设置评测集界面，填写**评测集名称、评测集描述**、选择**评测集可用范围**后，最后点击**确认创建**即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4396943871/p1085725.png)
4. 创建完评测集后，如下图所示：

   > **[!NOTE]**
   >
   > 创建评测集后，需等待几分钟，等状态从**处理中**变为**可用**，即可使用该评测集。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4396943871/p1085727.png)
