---
title: "知识集"
source_url: "https://open.dingtalk.com/document/aipass/distribution-of-ai-assistant-1"
namespace: "aipass"
slug: "distribution-of-ai-assistant-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "知识管理 > 知识集"
doc_id: "oe8QVy8Y35"
updated_at: "2026-07-08 15:48:53"
---

> Source: https://open.dingtalk.com/document/aipass/distribution-of-ai-assistant-1
> Path: AI PaaS / DEAP·企业AI平台 / 知识管理 > 知识集
> Updated: 2026-07-08 15:48:53

# 知识集

## **概述**

知识集是一系列知识（文档、网页、术语、FAQ）的集合，相当于给大模型“外挂”一个“知识仓库”，通过构建该“知识仓库”，大模型可以通过结合该“知识仓库”，回答一些“即时”知识、专业领域知识和私有知识。

一个常见的场景是企业内部的规章制度，每个企业都会有各种规定，每个企业的规章制度都是不同的，所以每个企业都会有一个“逻辑”上的规章制度的“知识集”。

## **实现原理**

当知识添加后，系统会对知识进行一定的加工处理，以便于更好的服务于大模型使用。常见知识处理流程如下：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3396943871/p1085729.png)

### **解析**

文档解析是智能问答的起点，负责将 PDF、Word、扫描件等非结构化数据转换为机器可读的结构化格式（如纯文本、Markdown、JSON 等），实现知识来源的数字化。

知识库中的内容通常来自多种格式的文档，包括 PDF、Office 文档、网页和图片扫描件等。这些数据未经处理时，机器几乎无法理解。通过文档解析，可以提取其中的文本、表格、图像说明等信息，并保留章节标题、段落、列表、表格等原始结构，形成规范化的内容表示。只有完成这一结构化处理，后续的内容清洗、分块和向量化才能有效执行。

简言之，文档解析的质量直接决定了召回内容的准确性和最终答案的生成质量。

### **切片**

文档存入知识库时会被自动分段，每段控制在 200–1000 字之间，以便于高效检索。如下图所示，左侧为原始文件，右侧为分段后的实际效果。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3396943871/p1085730.png)

### **关键词提取**

在文档学习过程中，系统会自动提取关键词以识别核心概念和重要信息。这些关键词作为知识索引，帮助系统在后续检索和内容匹配时更快、更准确地定位相关内容，从而提升知识使用的效率与稳定性。

### **向量化**

向量化是将文本、图像、视频甚至用户行为等数据转换为高维数值数组（即向量）的过程，用以表示其蕴含的语义信息，便于并行计算和高效处理。例如 [0.25, -0.1, 0.7] 就是一组向量。这些数值并非随机生成，而是通过模型训练得到，使得语义相近的内容在向量空间中的距离也更近。

## **操作步骤**

1. 进入 [DEAP 开发后台](https://deap.dingtalk.com/#/sub-app/model-manage)，在**开发模式**下，依次选择**知识集 > 新建知识集**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3396943871/p1085733.png)
2. 在新建知识集界面，填写**知识集名称、知识集描述、选择归属部门**和**可用人员范围**后，单击创建即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3396943871/p1085734.png)
3. 创建成功后，会自动跳转到知识集页面，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3396943871/p1085735.png)
4. 在知识集页面，点击**添加知识**按钮，然后添加知识源，最后单击**确定**即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3396943871/p1085736.png)

   导入数据源时，支持已下数据源：

   - **钉钉文件**：支持钉钉文档、钉钉知识库，并且可以选择单次导入和自动同步。

     - **单次导入**：直接导入源文件，内容与权限不随源文件更新。
     - **自动同步**：实时连接源文件，内容与权限始终与源文件保持同步。
   - **本地文件**：支持docx、doc、txt、xlsx、xls、pptx、ppt、pdf、png、jpg、wps、md等格式，每个文件不超过100MB，可同时批量上传20个文件等相关文导入。
   - **在线网页**：支持一次添加10个在线网页。
5. 数据源导入成功后，如下图所示：

   > **[!NOTE]**
   >
   > 导入数据源后，会知识状态会显示学习中，直到学习结束。
   >
   > - 若知识状态显示为**学习成功**，则代表当前知识已经学习完成；
   > - 若知识状态显示为**学习失败**，则代表当前知识学习失败，可点击后方**重试**进行重新学习。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3396943871/p1085739.png)
6. 学习成功后，点击**查看分块**，可对当前学习的内容实现分块预览。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3396943871/p1085741.png)

   你也可以在分块预览时，对当前某个分块进行**禁用/启用、删除**和**编辑**操作。

   > **[!NOTE]**
   >
   > 为确保内容更精准，建议对已修改的知识在知识列表中重新学习。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3396943871/p1085742.png)
