---
title: "使用数据集"
source_url: "https://open.dingtalk.com/document/dataopen/dataopen-using-data-sets"
namespace: "dataopen"
slug: "dataopen-using-data-sets"
group: "数据资产"
tab: "平台介绍"
breadcrumb: "企业客户手册 > 数据集成管理 > 使用数据集"
doc_id: "nZVIejJArK"
updated_at: "2025-10-21 14:17:11"
---

> Source: https://open.dingtalk.com/document/dataopen/dataopen-using-data-sets
> Path: 数据资产 / 平台介绍 / 企业客户手册 > 数据集成管理 > 使用数据集
> Updated: 2025-10-21 14:17:11

# 使用数据集

本文档将以自定义仪表盘为例，帮助你快速使用数据集。

## **前提条件**

完成[创建数据集](0009-dataopen-create-data-set.md)的流程。

## **操作步骤**

1. 登录[数据资产平台 > 自定义仪表盘](https://open-dev.dingtalk.com/fe/daas#/myDashboard)，单击**新建仪表盘**。
2. 添加组件（以柱状图为例）。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6036179071/p772679.png)
3. 配置柱状图：

   | **配置项** | **说明** |
   | --- | --- |
   | 数据源 | 单击点击添加，选择图标数据源：  - 数据域：选择自有数据。 - 业务场景：选择创建数据集中定义的业务场景 - 数据表：选择所需数据表。 |
   | 维度 | 柱状图横轴。  平台将业务日期自动生成日、周、月三个维度，其他字段不变。 |
   | 指标 | 柱状图纵轴，选择数值类型的字段。 |
   | 数据时间范围 | 按数据集的业务日期字段计算，只统计所选时间范围的数据。 |
   | 排序值 | 按需配置即可。 |

   配置完成后，单击添加。
4. 添加完成后，你可以保存并发布自定义仪表盘。
