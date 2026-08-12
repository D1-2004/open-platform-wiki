---
title: "智能需求收集"
source_url: "https://open.dingtalk.com/document/connection/intelligent-demand-collection"
namespace: "connection"
slug: "intelligent-demand-collection"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "群聊自动化 > 模板教学 > 智能需求收集"
doc_id: "czArxl4PN3"
updated_at: "2026-08-03 09:13:28"
---

> Source: https://open.dingtalk.com/document/connection/intelligent-demand-collection
> Path: 连接平台 / 连接平台自动化 / 群聊自动化 > 模板教学 > 智能需求收集
> Updated: 2026-08-03 09:13:28

# 智能需求收集

## **场景介绍**

在客户服务群或反馈收集群中，你是否经常遇到以下困扰：

- ❌ **消息太多**：客户/用户的问题和反馈源源不断，人工逐一回复耗时耗力。
- ❌ **分析困难**：面对大量反馈信息，难以快速提炼关键问题和改进方向。
- ❌ **记录分散**：有价值的建议散落在聊天记录中，缺乏系统化的归档和分析。

AI 客服自动化流程可以帮助你解决这些问题！

## **预期效果**

当客户或用户在群里提出建议或反馈时，自动化流程会自动完成以下工作：

- **智能分析**：AI 自动识别消息内容，提取关键信息（现状问题、改进方向、满意程度等）。
- **即时响应**：根据分析结果，自动生成并发送官方回复到群内，无需人工干预。
- **自动归档**：将原始反馈、AI 分析结果、官方回复等信息同步保存到钉钉 AI 表格，便于后续统计分析和趋势追踪。

通过这一流程，你可以实现：

- ✅**7×24 小时自动响应**：即使非工作时间也能及时回复用户。
- ✅ **标准化处理**：确保每条反馈都得到一致、专业的回应。
- ✅ **数据沉淀**：所有反馈结构化存储，为产品优化和运营决策提供数据支撑。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7030645871/p755046.png)

## **操作步骤**

1. 在**流程新建**Tab下，选择**AI能力**，然后选择模板**需求收集**并点击**立即使用**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8069175871/p754881.png)
2. 设置**机器人被@时**的触发条件，可根据需要修改配置，如图所示。

   > **[!NOTE]**
   >
   > 模板配置了所有成员、所有消息均可触发，也就是任何人发送一条@自动化小助手的消息，都会触发流程。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8069175871/p754882.png)
3. 设置**字段提取**，你可以根据需要修改配置。

   > **[!NOTE]**
   >
   > 此处可以提取几个关键信息：**是否为客服场景、现状问题、改进的方向、官方回应、满意程度**等。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8069175871/p754883.png)

   同时也可以设置字段提取后的格式，如下图所示：

   > **[!NOTE]**
   >
   > 模板内容表示AI以固定的JSON结构提取内容，并以返回值示例作为参考，即需要返回**需求内容**和**需求分类。**

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8069175871/p754886.png)
4. 设置**新增记录**节点，通过选择多维表，并向已有的AI 表格中新增一条数据记录进行备份。

   > **[!NOTE]**
   >
   > 选择多维表后，多维表中的字段标题会显示在配置界面，请根据字段内容进行配置，比如[需求原文]匹配[消息内容]。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8069175871/p754889.png)
5. 配置**发送消息到该群组**，你可以根据需要修改发送内容，如图所示。

   > **[!NOTE]**
   >
   > 消息来源支持：
   >
   > - 自定义：可自定义标题和自定义内容。
   > - 源数据解析：会提取上方节点的源数据的返回结果，作为机器人的消息内容。
   >
   >   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8069175871/p1091729.png)

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8069175871/p1091727.png)
6. 若需修改流程名称，可点击左上角编辑流程（图示中①），然后点击右上角**保存**（图示中②），最后点击**发布**（图示中③）即可。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8069175871/p754897.png)
