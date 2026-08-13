---
title: "自定义数据模型管理"
source_url: "https://open.dingtalk.com/document/dataopen/custom-data-model-management"
namespace: "dataopen"
slug: "custom-data-model-management"
group: "数据资产"
tab: "平台介绍"
breadcrumb: "生态伙伴手册 > 自定义数据模型管理"
doc_id: "jf6xL63cn6"
updated_at: "2026-08-12 09:23:56"
---

> Source: https://open.dingtalk.com/document/dataopen/custom-data-model-management
> Path: 数据资产 / 平台介绍 / 生态伙伴手册 > 自定义数据模型管理
> Updated: 2026-08-12 09:23:56

# 自定义数据模型管理

本文档主要介绍数据资产平台中ISV身份自定义数据模型的功能。

## **简介**

若应用服务商所需要的字段在数据资产目录已经存在，则如前述直接打包标准数据服务接口。当应用服务商所需要的字段属于OA中企业自建流程的字段，则选择自定义数据模型管理。

## **功能介绍**

ISV应用服务商（以下统一称“ISV”），可以在数据资产平台自定义数据服务，创建自身业务所需要数据模型，模型通过审批后，客户在开通ISV应用后，可以进行字段映射和授权，授权后ISV的应用即可调用客户自定义的OA表单数据。

[](https://cloud.video.taobao.com/play/u/null/p/1/e/6/t/1/405420061307.mp4?SBizCode=xiaoer)

## **步骤一：切换ISV身份**

登录数据资产平台时，默认是“组织身份”，点击即可切换。

![ISV身份](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6387946871/p632120.png)

## **步骤二：创建自定义数据模型**

1. 根据ISV的业务需要，希望获取OA审批中哪些自定义字段，即可配置好相应的字段需求，配置完成后即可直接发布。

   ![自定义模型](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6387946871/p632134.png)
2. 单击**确认**，完成发布。

   ![确认并发布](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5113171861/p632386.png)

## **步骤三：创建字段生成接口**

1. 单击**创建数据服务**中的**去打包**。

   ![创建并打包](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6387946871/p632161.png)
2. 可以在**自定义数据**中，选择已经发布的自定义字段，单击**下一步**。

   ![选择自定义字段](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5113171861/p632391.png)
3. 确认字段，并单击**去发布。**

   ![单击去发布](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6387946871/p632183.png)
4. 配置接口信息。

   > **[!IMPORTANT]**
   >
   > 选择正确的ISV公司关联的第三方企业应用。

   ![应用选择](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6387946871/p632192.png)
5. 确认发布。

   ![确认发布](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6387946871/p632195.png)
6. 发布成功后，进入审核流程。

   ![审核](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6387946871/p632360.png)
7. 审批完成后，在**数据服务管理**将创建好的接口执行**上架**动作，上架后客户组织即可授权。

   ![上架](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6387946871/p632364.png)
8. 上架完成后，ISV即可调用该接口serviceID，具体使用参照接口文档。

   ![serviceId](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6387946871/p632367.png)
