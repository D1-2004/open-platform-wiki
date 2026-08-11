---
title: "微应用四端调试工具—网页版"
source_url: "https://open.dingtalk.com/document/download/micro-application-four-terminal-debugging-tool-web-edition"
namespace: "download"
slug: "micro-application-four-terminal-debugging-tool-web-edition"
group: "应用开发"
tab: "开发工具"
breadcrumb: "开发者工具 > 微应用调试工具 > 微应用四端调试工具—网页版"
doc_id: "XZt8XihRTh"
updated_at: "2026-01-22 19:53:07"
---

> Source: https://open.dingtalk.com/document/download/micro-application-four-terminal-debugging-tool-web-edition
> Path: 应用开发 / 开发工具 / 开发者工具 > 微应用调试工具 > 微应用四端调试工具—网页版
> Updated: 2026-01-22 19:53:07

# 微应用四端调试工具—网页版

本文介绍钉钉开放平台提供的 H5 微应用四端调试工具及其使用方法，帮助开发者高效定位和解决应用在多端运行中的问题。

## **简介**

H5 微应用四端调试工具是钉钉开放平台推出的网页调试解决方案，支持在 Mac、Windows、Android 和 iOS 客户端中实时查看应用的 **Elements**、**Console**、**Network** 和 **AppLog** 信息，功能类似于 Chrome DevTools。

该工具适用于企业内部 H5 微应用的开发与调试。若需使用，请确保您具备以下权限和条件：

- 拥有管理员或开发者角色权限；
- 应用已开通“网页应用”能力。

### **支持功能**

- 调试标签和样式
- 打印调试语句、执行命令
- 查看网络请求情况
- 查看JSAPI调用情况

### **支持客户端**

Mac、Windows、Android、iOS

## 前置条件

使用本调试工具前，请确认已完成以下准备工作：

- 已创建 H5 微应用；
- 应用已配置“网页应用”能力；
- 开发者已登录钉钉开发者后台；
- 使用的钉钉客户端版本支持远程调试功能（建议最低版本：Mac/Windows v7.0+，Android/iOS v6.5+）；
- 微应用首页地址可正常访问并支持引入外部脚本。

## **使用方法**

使用方法分为两种，在首次开始调试前，任选其中一种进行代码改造，后续不需要再做改动。

### **方法一：CDN引入（推荐）**

将以下脚本插入微应用的 `<head></head>` 标签中：

```
<script src='https://g.alicdn.com/code/npm/@ali/dingtalk-h5-remote-debug/0.1.3/index.js'></script>
```

### **方法二：npm引入（不推荐）**

1. 使用 npm 安装 `dingtalk-h5-remote-debug` 包：

   ```
   npm install dingtalk-h5-remote-debug
   ```
2. 在项目入口，引入`initDingH5RemoteDebug`函数，并执行。

```
import { initDingH5RemoteDebug } from "dingtalk-h5-remote-debug";
initDingH5RemoteDebug();
```

### **使用调试平台进行调试**

#### 线上调试步骤

1. 登录开发者后台，[创建应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
2. 单击**应用能力** > **添加应用能力**，选择**网页应用**。
3. 添加完成后，单击**应用能力** > **网页应用** > **去调试**，即可进入调试平台。也可以直接点击[调试平台链接](https://open-dev.dingtalk.com/fe/api-tools#/debug/h5)进入。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1995565171/p799844.png)
4. 进入平台首先选择需要调试的网页应用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1995565171/p799847.png)
5. 选择应用后，可以看到应用首页和 PC 端首页的地址，这里对应的是网页应用管理页面填写的「应用首页地址」和「PC端首页地址」。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1995565171/p799850.png)
6. 单击「钉钉端内调试」按钮，此时调试链接已复制到剪贴板。
7. 打开钉钉客户端对话框，将调试链接复制到钉钉中并打开。

   > **[!NOTE]**
   >
   > 若需他人协助调试，可将复制的调试链接发送给对方，在其钉钉客户端中打开即可。
8. 打开后，首先会展示远程调试服务条款，建议详细阅读。之后点击「点击跳转至调试页面」进入应用首页。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1447220861/p611800.png)
9. 进入应用首页后，可以看到页面右上角显示调试标识，红色代表连接尚未建立。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1447220861/p611802.png)
10. 返回调试平台，可以看到此时后台已经收到应用首页上报的调试信息。

    ![应用首页地址](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1447220861/p611807.png)
11. 单击「调试」按钮，打开调试工具，即可进行调试。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1447220861/p611810.png)
12. 此时，应用首页中的调试标志已经变为绿色，标识调试连接已经建立。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1447220861/p611811.png)

#### 开发阶段调试

调试工具也支持开发阶段的调试，同时支持开发阶段实现免登。使用方式和线上调试一致。

![免登](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1447220861/p611813.png)

## **终止调试**

可通过以下两种方式终止当前调试连接：

- 方式一：在平台中，单击「断开」按钮即可终止调试。

  ![断开调试](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1447220861/p612934.png)
- 方式二：关闭被调试的H5微应用页面。

## **常见问题**

- ### **支持第三方企业应用的网页应用调试吗？**

  **答：** 支持第三方企业应用的网页应用调试，但需提前提交申请并通过审核。
- ### **npm 包引入后，可以发布到线上吗？**

  **答：** 可以。调试工具仅在通过调试平台生成的特定链接中激活，不会影响应用在线上环境的正常运行。
- ### **同一个地址可以同时进行创建多条调试连接吗？**

  **答：** 不可以。每个调试地址默认最多支持 1 条调试连接。
- ### **调试JSAPI时报错【No permission info for action: xxx】。**

  **答：**请参考[钉钉JSAPI](https://www.npmjs.com/package/dingtalk-jsapi)完成 JSAPI 初始化配置，确保权限正确声明。
- ### **调试JSAPI时报错【当前微应用不在企业内】。**

  **答：**请新建一个用于调试的h5微应用，将当前微应用的ip:port填入该新建应用的首页地址中。
- ### **网络请求时请求头和响应头缺失。**

  **答：**请求头缺失与浏览器的安全策略有关。响应头缺失可以看下接口响应头是否配置了Access-Control-Expose-Headers字段。
