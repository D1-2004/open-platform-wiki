---
title: "智能查询内部数据"
source_url: "https://open.dingtalk.com/document/connection/intelligent-query-of-internal-data"
namespace: "connection"
slug: "intelligent-query-of-internal-data"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "群聊自动化 > 模板教学 > 智能查询内部数据"
doc_id: "74rQfGzaCL"
updated_at: "2026-08-03 09:13:30"
---

> Source: https://open.dingtalk.com/document/connection/intelligent-query-of-internal-data
> Path: 连接平台 / 连接平台自动化 / 群聊自动化 > 模板教学 > 智能查询内部数据
> Updated: 2026-08-03 09:13:30

# 智能查询内部数据

## **场景介绍**

在日常工作中，你是否经常遇到以下困扰：

- ❌ **系统太多**：需要登录 ERP、CRM、库存等多个系统才能查到完整信息。
- ❌ **操作繁琐**：每次查数据都要点选菜单、输入条件、等待加载，耗时费力。
- ❌ **响应延迟**：同事在群里问数据，你需要切出去查完再复制回来，沟通断档。

AI 智能查数自动化流程可以让"一句话查数据"成为现实！

## **预期效果**

在群内提出问题后，AI 将自动帮助你分析查询对象，并发起HTTP请求，查询内部系统的详细信息，然后将其发送到群内。

当群成员 @自动化小助手并提出数据查询问题时，自动化流程会自动完成以下工作：

- **意图识别**：AI 自动分析消息内容，判断是否为数据查询请求，并提取查询对象（如商品名称、订单号等）。
- **接口调用**：根据提取的信息，自动发起 HTTP 请求到内部系统 API，获取实时数据。
- **结果返回**：将查询到的详细信息格式化后发送到群内，无需人工干预。

通过这一流程，你可以实现：

- ✅ **全自动处理，零人力投入**：7×24 小时响应查询请求。
- ✅ **跨系统聚合**：一次提问，打通多个内部数据源。
- ✅ **沟通零断档**：查询结果直接在群内呈现，保持对话连贯性。
- ✅ **权限可控**：通过条件节点过滤非查询类消息，避免误触发。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7030645871/p755058.png)

## **操作步骤**

1. 在**流程新建**Tab下，选择**AI能力**，然后选择模板**AI查数据**并点击**立即使用**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0169175871/p754904.png)
2. 设置**机器人被@时**触发条件，根据需要修改配置，如图所示。

   > **[!NOTE]**
   >
   > 模板配置了所有成员、所有消息均可触发，也就是任何人发送一条@自动化小助手的消息，都会触发流程。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0169175871/p754905.png)
3. 设置**字段提取**，你可以根据需要修改配置。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0169175871/p754908.png)

   同时也可以设置字段提取后的格式，如下图所示：

   > **[!NOTE]**
   >
   > 模板内容表示AI以固定的JSON结构提取内容，并以返回值示例作为参考，即需要返回**是否询问商品信息、商品名称这两个字段的内容。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0169175871/p1091747.png)
4. 设置**条件**执行动作**，**当满足条件时流程继续执行，否则流程将在此步骤终止。

   > **[!NOTE]**
   >
   > 模板中条件设置为了“是否询问商品信息”等于“是”时，流程才会继续往下执行。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0169175871/p754913.png)
5. 设置**发起HTTP请求**执行动作，你可以修改配置从而获取内部系统的数据。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0169175871/p754914.png)
6. 步骤5为**发送消息到该群组**，可根据需要修改消息内容。

   > **[!NOTE]**
   >
   > 消息来源支持：
   >
   > - 自定义：可自定义标题和自定义内容。
   > - 源数据解析：会提取上方节点的源数据的返回结果，作为机器人的消息内容。
   >
   >   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0169175871/p1091751.png)

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0169175871/p754915.png)
7. 若需修改流程名称，可点击左上角编辑流程（图示中①），然后点击右上角**保存**（图示中②），最后点击**发布**（图示中③）即可。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0169175871/p754917.png)
