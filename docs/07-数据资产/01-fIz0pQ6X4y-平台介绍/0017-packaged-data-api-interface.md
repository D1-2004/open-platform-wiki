---
title: "打包数据API接口"
source_url: "https://open.dingtalk.com/document/dataopen/packaged-data-api-interface"
namespace: "dataopen"
slug: "packaged-data-api-interface"
group: "数据资产"
tab: "平台介绍"
breadcrumb: "企业客户手册 > 打包数据API接口"
doc_id: "Z4RARLtsBB"
updated_at: "2026-08-12 09:23:53"
---

> Source: https://open.dingtalk.com/document/dataopen/packaged-data-api-interface
> Path: 数据资产 / 平台介绍 / 企业客户手册 > 打包数据API接口
> Updated: 2026-08-12 09:23:53

# 打包数据API接口

本文档主要介绍数据资产平台中打包数据API接口的功能。

## **功能简介**

基于数据资产目录，企业可以自由选择数据指标生成API接口，通过审批后快速集成到自主开发的应用中。

[](https://cloud.video.taobao.com/play/u/null/p/1/e/6/t/1/404609313951.mp4?SBizCode=xiaoer)

## **步骤一：选择数据资产**

可根据本组织需要，选择相应的业务场景下的数据资产。

1. 选择**创建数据服务**，单击**去打包。**

   ![去打包](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3387946871/p632406.png)
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

## **步骤三：完成接口信息配置**

定义接口基础配置并**确认发布**。

![完成接口配置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3387946871/p632589.png)

> **[!NOTE]**
>
> 该页面还有两个关键的功能，自定义指标和数据过滤。
>
> - **自定义指标：**是指用户可以基于返回的数据项进行二次计算，生成新的返回指标；
> - **数据过滤：**是指针对返回的数据，根据返回的字段提前进行条件过滤，剔除掉不需要的数据。

## **步骤四：确认发布**

所有信息配置完成后，即确认发布，该接口服务进入审批流程，可以在**数据服务管理**中查看具体的审批进度。

![等待审核](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3387946871/p632590.png)

## **步骤五：上架调用**

1. 审批流程完成后，可在**数据服务管理**页面点击**上架**，该服务即可被调用。

   ![上架](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3387946871/p632600.png)
2. 上架完成后，即可调用该接口serviceID，具体使用参见示例代码和接口文档。

   ![使用接口](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3387946871/p632603.png)

## **步骤六：调用示范操作**

下方视频是具体的接口调用过程参考。

[](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20240220/pwgmbk/2%E6%9C%8820%E6%97%A5.mp4)
