---
title: "生成数据图表"
source_url: "https://open.dingtalk.com/document/dataopen/generate-data-charts"
namespace: "dataopen"
slug: "generate-data-charts"
group: "数据资产"
tab: "平台介绍"
breadcrumb: "企业客户手册 > 生成数据图表"
doc_id: "pvhgzG0nZD"
updated_at: "2026-08-12 09:23:54"
---

> Source: https://open.dingtalk.com/document/dataopen/generate-data-charts
> Path: 数据资产 / 平台介绍 / 企业客户手册 > 生成数据图表
> Updated: 2026-08-12 09:23:54

# 生成数据图表

本文档主要介绍数据资产平台中生成数据图表的功能。

## **简介**

自主选择数据字段，自动生成实时更新的数据图表，无缝触达钉钉场域和业务场景。

## **步骤一：选择数据指标**

可根据图表展示需要，选择相应的业务场景下的数据指标。

1. 选择**创建数据服务**，单击**去生成**。

   ![去生成](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4387946871/p632607.png)
2. 查看数据资产目录。

   ![查看数据资产目录](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3387946871/p632571.png)

## **步骤二：分组发布数据接口**

不同维度的数据字段不能打包在同一个API中，所以需要分组发布接口。

1. 选择不同维度数据。

   > **[!NOTE]**
   >
   > 根据自身需求，选择相应字段。

   - 组织维度：

     ![组织维度](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3387946871/p632578.png)
   - 员工维度：

     ![员工维度](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3387946871/p632579.png)
2. 单击**下一步。**

   ![下一步](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3387946871/p632580.png)
3. 进行分组发布。

![分组发布](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3387946871/p632582.png)

## **步骤三：数据图表配置**

进行数据图表配置并确认发布。

![图表配置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4387946871/p632612.png)

图表发布形式有两种选项：

#### **动态卡片：可发送到指定人或群**

![动态卡片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4387946871/p632618.png)

#### **工作台组件**

> **[!NOTE]**
>
> 该能力仅适用于有自定义设计器权限的客户，包括专业钉、专属钉等。

1. 在数据资产平台选择工作台组件发布后需进入[卡片平台](https://open-dev.dingtalk.com/fe/card)创建互动卡片，选择卡片类型为**工作台卡片。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1803171861/p630760.png) ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1803171861/p630761.png)
2. 选择图表组件，在右侧给图表命名一个变量（变量只能选择图表类型），保存并发布。

   ![工作台卡片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1803171861/p632628.png)
3. 单击右上角卡片实例管理后进行动态数据源的绑定，选择创建数据资产平台数据源，配置拉取方式和时间。

   ![实例创建](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1803171861/p632633.png)
4. 把图表的变量和数据资产平台生成的数据图表服务进行绑定；创建实例并投放到工作台。

   ![创建并投放](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4387946871/p632636.png)

## **步骤四：确认发布**

所有信息配置完成后，即确认发布，该接口服务进入审批流程，可以在**数据服务管理**中查看具体的审批进度。

![图表发布](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1803171861/p632638.png)

## **步骤五：数据服务管理**

审批流程完成后，可在“数据服务管理”页面点击**上架**，该服务即可被调用。

![上架](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3387946871/p632600.png)
