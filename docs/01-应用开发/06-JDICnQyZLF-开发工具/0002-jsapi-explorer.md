---
title: "前端JSAPI调试工具"
source_url: "https://open.dingtalk.com/document/download/jsapi-explorer"
namespace: "download"
slug: "jsapi-explorer"
group: "应用开发"
tab: "开发工具"
breadcrumb: "开发者工具 > 前端JSAPI调试工具"
doc_id: "BTKyXKGiX4"
updated_at: "2025-11-13 09:13:35"
---

> Source: https://open.dingtalk.com/document/download/jsapi-explorer
> Path: 应用开发 / 开发工具 / 开发者工具 > 前端JSAPI调试工具
> Updated: 2025-11-13 09:13:35

# 前端JSAPI调试工具

JSAPI Explorer是钉钉开放平台提供的可视化微应用JSAPI调用工具，方便开发者在线发起JSAPI调用。本文将以JSAPI Explorer工具调用发起DING消息JSAPI给某人发送DING消息为例，帮助您快速了解JSAPI Explorer工具的使用。

## 步骤一：连接控制台

参考以下操作，使用JSAPI Explorer工具连接手机控制台。

1. 打开[JSAPI Explorer](https://open.dingtalk.com/tools/explorer/jsapi)工具，通过搜索“createDing”快速定位JSAPI。本示例以**发起DING****消息**JSAPI为例，给某人发送DING消息为例。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5146992671/p1025952.png)
2. 选择需要预览的类型，使用钉钉移动端扫描右侧二维码，连接控制台。

   > **[!NOTE]**
   >
   > 平台提供了**微应用移动端**和**小程序移动端**调试功能，但部分接口仅支持其中一种，可根据实际情况选择对应类型进行连接。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5146992671/p1025953.png)
3. 根据提示完成手机扫码授权，单击**确定**。

   > **[!NOTE]**
   >
   > 当控制台连接成功后，在没有断开连接的前提下，调用其他API时可忽略步骤一，断开连接后需重新连接手机控制台。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5146992671/p1025958.png)

   若连接成功后，调试台右侧的**运行调试**按钮会变为可点击状态：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5146992671/p1025961.png)

## 步骤二：发起调用

参考以下操作，使用**JSAPI Explorer**工具给某人发送DING消息，完成**发起DING****消息**JSAPI调用：

1. 控制台连接成功后，点击右侧示例代码下方的**运行调试**按钮，发起调试。

   > **[!NOTE]**
   >
   > Android端和iOS端不同系统展示结果可能会出现差别，请以最终的展示效果为准。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5146992671/p1025961.png)
2. 手机端和PC端同时返回调用结果，效果如下图所示。

   手机端效果图：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5146992671/p1026007.png)

   PC端效果图：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5146992671/p1026008.png)
