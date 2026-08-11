---
title: "创建数据集"
source_url: "https://open.dingtalk.com/document/dataopen/dataopen-create-data-set"
namespace: "dataopen"
slug: "dataopen-create-data-set"
group: "数据资产"
tab: "平台介绍"
breadcrumb: "企业客户手册 > 数据集成管理 > 创建数据集"
doc_id: "xhBJChVnPy"
updated_at: "2025-10-20 18:48:23"
---

> Source: https://open.dingtalk.com/document/dataopen/dataopen-create-data-set
> Path: 数据资产 / 平台介绍 / 企业客户手册 > 数据集成管理 > 创建数据集
> Updated: 2025-10-20 18:48:23

# 创建数据集

数据源搭建完成后，你需要创建数据集，你可以参考本文档操作步骤完成创建数据集。

## **背景信息**

数据集根据不同数据源类型，大致分为两种。一种是**数据库直连**的数据集，由Mysql或Hologres等数据库提供数据来源，另一种是**连接器触发**的数据集，由连接平台的触发事件提供数据来源。

## **前提条件**

完成[搭建数据源](0008-using-data-integration-management.md)的流程。

## **方式一：数据库直联**

1. 登录[数据资产平台 > 数据集成管理](https://open-dev.dingtalk.com/fe/daas#/dataSet)，单击已搭建的数据源。
2. 进入目标数据源页面，单击**确认**按钮，进入数据集配置页面。
3. 配置数据集信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 业务场景名称 | 用于在后续的数据服务中筛选出该数据集。 |
   | 数据集名称 | 用于标识此数据集，不可重名。 |
   | 业务日期 | 用于标识数据集时间维度的字段，例如数据的创建日期、更新日期等Date类型的字段。  要求所选中的数据表中，必须含有Date类型的字段，否则业务日期就没有可选字段，同时数据集也无法保存。 |

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3826179071/p772539.png)
4. 设置数据集字段：

   1. 选择单张表选择目标数据表，拖拽至指示板中。

      > 你也可以选择两张数据表进行 JOIN，详情参看下方相关内容。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3826179071/p772543.png)
   2. 拖拽后，单击数据表名，进入选择字段页面。

      > 勾选你需要的字段，勾选需要字段后，✓ 状态发生变化，字段别名变为可编辑状态。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3826179071/p772551.png)

      选择完成后，单击确认。既可以自动预览字段内容。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3826179071/p772567.png)
   3. 设置完成后，单击**保存数据集**。

## **方式二：**连接器触发

1. 登录[数据资产平台 > 数据集成管理](https://open-dev.dingtalk.com/fe/daas#/dataSet)，单击**新建数据集**。
2. 单击下方 **“⊕”**，选择连接器，并单击确认。

   > 入口虽然是新增数据源，但连接器的数据源已由系统预置。
3. 配置数据集的信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 业务场景名称 | 用于在后续的数据服务中筛选出该数据集。 |
   | 数据集名称 | 用于标识此数据集，不可重名。 |
   | 数据集字段 | 上架到数据资产平台的字段：  - 系统默认字段biz\_time，用于标识数据集时间维度的字段，例如数据的创建日期、更新日期等Date类型的字段，建议选为主键加快查询效率。 - 自定义字段，由用户按需创建。 |

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3826179071/p772584.png)配置完成后，保存数据集。

   > **[!NOTE]**
   >
   > 保存后无法编辑，如若修改，需要删除重新创建。
4. 跳转到连接平台，配置连接流：

   1. 创建完数据集后，跳转到[连接平台](https://open-dev.dingtalk.com/fe/connector#/myFlow)，单击**我的连接流** > **创建连接流**。
   2. 配置触发事件，用户可自定义触发事件，以实际业务为准。配置请参考[配置触发事件](../../02-连接平台/02-iO2mVD3wB2-开发指南/0004-configure-trigger-events-1.md)。
   3. 配置执行动作：

      | **配置项** | **说明** |
      | --- | --- |
      | 选择连接器 | 选择数据资产平台 |
      | 执行动作 | 选择接收并储存数据。 |
      | 配置参数 | 选择，上述创建的数据集。  在数据资产平台配置的连接器类型数据集，都会在这里回显。 |
   4. 执行动作配置完成后，可以进行调试并发布。

## **后续步骤**

数据集创建完成后，你就可以进行使用了，详情参考[使用数据集](https://open.dingtalk.com/document/dataopen/using-data-sets)。

## **常见问题**

### **数据表是否支持 JOIN，如何实现？**

在方式一中，设置数据集字段时，你可以选择需要 JOIN 的两张表：

1. 选中需要 JOIN 的数据表，拖拽至指示板，并设置每张表所需字段。
2. 设置所需字段完成后，将两张表通过箭头连接。
3. 设置连接关系。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3826179071/p772581.png)
