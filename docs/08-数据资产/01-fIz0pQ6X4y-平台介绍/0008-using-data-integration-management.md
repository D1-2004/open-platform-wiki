---
title: "搭建数据源"
source_url: "https://open.dingtalk.com/document/dataopen/using-data-integration-management"
namespace: "dataopen"
slug: "using-data-integration-management"
group: "数据资产"
tab: "平台介绍"
breadcrumb: "企业客户手册 > 数据集成管理 > 搭建数据源"
doc_id: "h1zruySY1o"
updated_at: "2025-10-21 14:16:59"
---

> Source: https://open.dingtalk.com/document/dataopen/using-data-integration-management
> Path: 数据资产 / 平台介绍 / 企业客户手册 > 数据集成管理 > 搭建数据源
> Updated: 2025-10-21 14:16:59

# 搭建数据源

如果你需要使用数据集成管理的能力，你可以参考本文档操作步骤。

## **前提条件**

完成[成为钉钉开发者](https://open.dingtalk.com/document/dingstart/dingtalk-developer)的流程。

## **操作步骤**

1. 登录[数据资产平台 > 数据集成管理](https://open-dev.dingtalk.com/fe/daas#/dataSet)，单击**新建数据集**。
2. 单击下方 **“⊕”**，进行新建数据源。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5626179071/p772507.png)
3. 选择数据类型：

   | **数据类型** | **说明** |
   | --- | --- |
   | Mysql | 适用于业务数据存储在Mysql数据库中。 |
   | Hologres | 适用于业务数据存储在Hologres数据库中。 |
   | 连接器 | 系统预置的特殊数据源，用户无需创建，创建数据源时**可忽略**，创建数据集时才会用到。 |
4. 填写数据库信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 数据源名称 | 填写数据源名称。 |
   | 数据源描述 | 填写数据源简要信息。 |
   | JDBC URL | 填写 JDBC 路径。    示例：  jdbc:<databaseType>://<server>:<port>/<databaseName> |
   | 用户名 | 填写用户名信息。 |
   | 密码 | 填写密码信息。 |

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6626179071/p772513.png)

   信息填写完成后，你可以单击**点击测试**，测试连通是否成功。
5. 测试完成后，单击确认。

## **后续步骤**

数据源搭建完成后，你需要创建数据集，详情参考[创建数据集](0009-dataopen-create-data-set.md)。
