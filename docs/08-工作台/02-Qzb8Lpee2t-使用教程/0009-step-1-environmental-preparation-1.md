---
title: "步骤一：环境准备"
source_url: "https://open.dingtalk.com/document/dingstart/step-1-environmental-preparation-1"
namespace: "dingstart"
slug: "step-1-environmental-preparation-1"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > 基础教程 > 步骤一：环境准备"
doc_id: "6y6TrSv45q"
updated_at: "2025-09-03 15:57:02"
---

> Source: https://open.dingtalk.com/document/dingstart/step-1-environmental-preparation-1
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > 基础教程 > 步骤一：环境准备
> Updated: 2025-09-03 15:57:02

# 步骤一：环境准备

如果你需要进行全码组件的开发，你首先需要搭建开发环境，你可以参考本文档内容完成搭建。

## **第一步：安装DingTalk CLI**

请参考以下步骤完成 DingTalk Design CLI 工具的安装：

1. 执行以下命令，检查 Node.js 版本

   > **[!NOTE]**
   >
   > DingTalk Design CLI 需要使用 Node.js 12.15.x 或更高版本。如果你未安装[Node.js](https://nodejs.org/en)，请前往 Node.js 官网下载并安装。

   ```
   node -v
   ```
2. 执行以下命令，安装 CLI 工具。

   ```
   npm install dingtalk-design-cli -g
   # or
   yarn global add dingtalk-design-cli
   ```
3. 执行以下命令，检查 CLI 工具是否安装成功。

   ```
   ding -v
   ```

   如图返回 dingtalk-design-cli 版本号，表示安装成功。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0280640071/p739456.png)

## **第二步：安装小程序开发 IDE**

安装方式可以查看[小程序开发工具](../../01-应用开发/06-JDICnQyZLF-开发工具/0001-miniapp-tool.md)。

> **[!NOTE]**
>
> 确保小程序IDE的版本不低于 1.12.19。
