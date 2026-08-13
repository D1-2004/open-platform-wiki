---
title: "数据批量同步服务"
source_url: "https://open.dingtalk.com/document/dataopen/data-batch-synchronization-service"
namespace: "dataopen"
slug: "data-batch-synchronization-service"
group: "数据资产"
tab: "平台介绍"
breadcrumb: "企业客户手册 > 数据批量同步服务"
doc_id: "hklPUf5Pgf"
updated_at: "2026-08-12 09:23:55"
---

> Source: https://open.dingtalk.com/document/dataopen/data-batch-synchronization-service
> Path: 数据资产 / 平台介绍 / 企业客户手册 > 数据批量同步服务
> Updated: 2026-08-12 09:23:55

# 数据批量同步服务

本文档主要介绍数据资产平台中数据批量同步服务的功能。

## **简介**

数据资产平台支持对数据进行批量的导出后，进入本地分析和处理，目前支持导出到钉钉表格。

## 步骤一：自由选择数据资产

1. 选择**首页**，并单击**去同步**。

   ![去同步..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5387946871/p677851.png)
2. 根据业务分析需要，选择相应的业务场景下的数据资产。本示例选用**用户考勤明细。**

   > **[!NOTE]**
   >
   > 选择明细中需要字段并单击下一步。

   ![用户考勤明细](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5387946871/p632432.png)

## **步骤二：分组发布数据接口**

不同维度的数据字段不能打包在同一个API中，所以需要分组发布接口。

![选中并发布](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5387946871/p632436.png)

## **步骤三：完成数据同步信息配置**

定义好同步文件的名称，选择时间范围。配置好后，该页面会显示导出数据项，点击确认后，系统会自动计算导出的数据行数。

![数据发布](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8013171861/p632494.png)

> **[!IMPORTANT]**
>
> 该页面还有两个关键的功能，自定义指标和数据过滤。

- **自定义指标：**是指用户可以基于返回的数据项进行二次计算，生成新的返回指标。
- **数据过滤：**是指针对返回的数据，根据返回的字段提前进行条件过滤，剔除掉不需要的数据。

## **步骤四：确认发布**

所有信息配置完成后，即确认发布，该接口服务进入审批流程，可以在“数据服务管理”中查看具体的审批进度。

![审核中](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5387946871/p632450.png)

## 步骤五：数据同步至钉钉表格

数据同步申请审核完成后，在数据服务管理中，找到该服务，并点击右侧**同步**按钮，即可完成数据同步。

![同步](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5387946871/p632457.png)
