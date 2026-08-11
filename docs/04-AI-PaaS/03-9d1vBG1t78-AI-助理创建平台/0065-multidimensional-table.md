---
title: "多维表"
source_url: "https://open.dingtalk.com/document/aipass/multidimensional-table"
namespace: "aipass"
slug: "multidimensional-table"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 工作流 > 钉钉协作 > 多维表"
doc_id: "9fUWTDQOQI"
updated_at: "2025-09-23 19:19:52"
---

> Source: https://open.dingtalk.com/document/aipass/multidimensional-table
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 工作流 > 钉钉协作 > 多维表
> Updated: 2025-09-23 19:19:52

# 多维表

如果你需要使用多维表的执行动作，请了解如何在[创建 AI 助理工作流](0037-create-an-ai-assistant-workflow-1.md)时添加执行动作。

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理**

## 操作步骤

1. 单击**选择执行动作**，选择**多维表 > 新增记录**。
2. 配置新增记录：

   | **配置项** | | **说明** |
   | --- | --- | --- |
   | 选择多维表 | 选择多维表 | 选择一个你具有编辑权限的多维表 |
   | 选择数据表 | 选择多维表内的一个数据表。  **[!NOTE]**  - 如果你需要查看多维表内容，你可以单击查看表格，可跳转到该多维表页。 - 若你对数据表的字段有增删改，单击刷新字段，会自动刷新字段内容 image.png |
   | 设置字段内容 | | 数据表的字段内容。  **[!NOTE]**  - 当你选择数据表后，数据表的字段会自动展现在这里。当前仅支持文本、数字、单选、人员、日期类型的字段。 - 你可以手动输入内容，也可以单击“⊕”，引用变量进行动态传参。变量详情参考[变量](0054-variable-overview-1.md)。 |

## **示例**

以在任务管理的多维表加入周报任务为例：

1. 打开[钉钉文档](https://alidocs.dingtalk.com/i/desktop)，单击**我的文档 > 新建。**![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2865329171/p813733.png)
2. 单击**多维表**，在热门推荐中，选择**任务管理**并**使用。**![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2865329171/p813734.png)此时，你的多维表就已经创建完成了。
3. 在多维表的执行动作中，配置多维表信息：

   | **字段内容** | | **说明** |
   | --- | --- | --- |
   | 选择多维表 | 选择多维表 | 选择上述新建的**任务管理**多维表。 |
   | 选择数据表 | 选择上述新建的**任务管理**数据表。 |
   | 待办内容 | | 填写：周报。  该字段为文本类型。 |
   | 重要程度 | | 选择：重要且紧急  该字段为单选类型。 |
   | 负责人 | | 你可以单击“人员标识”，使用选人组件，选择组织内人员。  **[!NOTE]**  - 支持单击 **“⊕”**，设置变量信息，需选择钉钉用户 UserID。 - 支持单击 “人员标识”，使用选人组件，选择组织内人员。 |
   | 截止日期 | | 选择：2024-06-21。  该字段为日期类型，支持“YYYY-MM-DD”格式。 |
   | 任务进度 | | 选择：进行中。  该字段为单选类型。 |

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2865329171/p813735.png)
