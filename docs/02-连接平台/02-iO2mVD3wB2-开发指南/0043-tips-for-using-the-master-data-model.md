---
title: "主数据"
source_url: "https://open.dingtalk.com/document/connection/tips-for-using-the-master-data-model"
namespace: "connection"
slug: "tips-for-using-the-master-data-model"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发参考 > 高级功能 > 主数据"
doc_id: "Ym55vO90PR"
updated_at: "2025-09-23 19:20:29"
---

> Source: https://open.dingtalk.com/document/connection/tips-for-using-the-master-data-model
> Path: 连接平台 / 开发指南 / 开发参考 > 高级功能 > 主数据
> Updated: 2025-09-23 19:20:29

# 主数据

> **[!NOTE]**
>
> 主数据功能及相关接口因业务调整，功能和接口会逐渐下线并暂停维护，功能下线后不会影响已有的流程数据。

## **简介**

主数据，是钉钉官方统一标准的数据模型，用户可以基于官方主数据模型编排自定义数据模型。

在连接器**基本信息**的**高级设置**中，开启**主数据**之后，当前连接器的所有执行动作都可以使用主数据模型作为出入参数结构，并且也可以选择主数据模型进行入参和出参的映射。

![主数据..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5413155861/p676274.png)

## 操作步骤

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/index)，进入**连接平台**页面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7041736761/p557455.png)
2. 开启主数据后，执行动作入参配置中API入参可以选择“从钉钉官方业务主数据模型导入”。

   ![主数据导入..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5413155861/p676288.png)

   查看主数据类型模型：

   ![主数据模型种类..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5413155861/p676291.png)

   同时也可以开启入参映射，选择钉钉官方业务主数据模型，使用主数据模型进行映射。

   ![入参映射-主数据..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5413155861/p676294.png)
3. 开启主数据后，执行动作出参配置中API出参可以选择“从钉钉官方业务主数据模型导入”。

   ![出参-主数据..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5413155861/p676303.png)

   查看主数据类型模型：

   ![出参-主数据模型类型..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5413155861/p676305.png)

   同时也可以开启出参映射，选择钉钉官方业务主数据模型，使用主数据模型进行映射。

   ![出参映射-主数据..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5413155861/p676311.png)
