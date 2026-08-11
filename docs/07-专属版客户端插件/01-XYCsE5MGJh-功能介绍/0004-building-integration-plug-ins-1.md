---
title: "构建集成插件"
source_url: "https://open.dingtalk.com/document/development/building-integration-plug-ins-1"
namespace: "development"
slug: "building-integration-plug-ins-1"
group: "专属版客户端插件"
tab: "功能介绍"
breadcrumb: "操作指南 > 构建集成插件"
doc_id: "D0gBykatSY"
updated_at: "2025-10-15 17:01:41"
---

> Source: https://open.dingtalk.com/document/development/building-integration-plug-ins-1
> Path: 专属版客户端插件 / 功能介绍 / 操作指南 > 构建集成插件
> Updated: 2025-10-15 17:01:41

# 构建集成插件

上传插件完成后，你需要构建集成，你可以参考本文档操作步骤完成构建操作。

## **前提条件**

完成[上传并发布插件](0003-upload-and-publish-plug-ins-1.md)流程。

## **操作步骤**

### **构建测试版本**

> **[!NOTE]**
>
> 构建正式版本前，可以先完成测试版本的集成测试。

发布插件，插件生效状态为**测试版本**时，单击**钉钉专属版** > **App定制** > **专属插件** > **集成测试 > 打包测试**。选择我们期望集成的模块以及对应版本号，单击**确定**发起构建。

构建完成后（大约1个小时）在打包列表中单击**查看**，然后下载安装集成包并测试插件功能。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1515628171/p803545.png)

### **构建正式版本**

1. 发布插件，插件生效状态为**正式版本**时，单击**钉钉专属版** > **App定制** > **App打包** > **专属App配置** > **SDK选配**，再勾选期望集成的插件。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6802489961/p715731.png)
2. 单击**钉钉专属版** > **App定制** > **App打包** > **创建打包** > **创建**发起构建。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6132883861/p631835.png)

## **后续步骤**

插件打包完成后，你可以再构建结果中获取插件的专属钉钉App安装包，请自行安装并验收插件功能。
