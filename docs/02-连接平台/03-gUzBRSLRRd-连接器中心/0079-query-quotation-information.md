---
title: "查询指定类目价格最低的三家供应商和报价信息"
source_url: "https://open.dingtalk.com/document/connection/query--quotation-information"
namespace: "connection"
slug: "query--quotation-information"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "三方连接器 > 1688 > 使用教程 > 查询指定类目价格最低的三家供应商和报价信息"
doc_id: "WRWCPiholJ"
updated_at: "2026-05-19 19:46:20"
---

> Source: https://open.dingtalk.com/document/connection/query--quotation-information
> Path: 连接平台 / 连接器中心 / 三方连接器 > 1688 > 使用教程 > 查询指定类目价格最低的三家供应商和报价信息
> Updated: 2026-05-19 19:46:20

# 查询指定类目价格最低的三家供应商和报价信息

本教程介绍了通过钉钉连接平台配置连接流，实现同步获取指定类目下报价最低的三家供应商和报价信息。

## **准备工作**

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 入驻[1688开放平台](https://open.1688.com/console?spm=a260s.11051009.jb7hjul7.7.77fe55edxZ8PH3)，订购[关键词检索代采解决方案](https://open.1688.com/solution/detail?spm=a260s.26059361.0.0.bad555ed86uGMu&key=1675408994871&category=null)，获取 1688 开放应用的 App Key 和 App Secret 。

## **操作步骤**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 单击**开放能力** > **连接平台** > **我的连接 >** **我的连接流** > **创建连接流**。
3. 配置触发事件：

   1. 选择**内置工具** > **子流程 > 当被调用时触发**。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7670239961/p735305.png)
   2. 单击**设置入参，填写参数信息。**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7670239961/p735306.png)
   3. 单击**保存草稿，**选择**编辑，**并开启**同步调用。**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7670239961/p735308.png)
4. 配置执行动作：

   1. 选择三方连接器，搜索 **1688**，单击 **1688** 连接器。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7670239961/p735311.png)
   2. 选择**执行动作** > **采购商品比价。**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7670239961/p735313.png)
   3. 配置账号，填写准备工作中获取的 1688 开放应用的凭证信息。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7670239961/p735319.png)
   4. 配置参数：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7670239961/p735332.png)
   5. 单击**测试并预览**，

      1. 输入**测试值**，单击**确定。**

         ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7670239961/p735334.png)
      2. 完成测试。

         ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7670239961/p735338.png)
5. 配置出参：

   1. 单击**流程出参** > **设置出参。**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7670239961/p735342.png)
   2. 配置参数：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7670239961/p735345.png)
   3. 单击**测试并预览**，完成测试。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7670239961/p735347.png)
6. 发布连接流。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7670239961/p735349.png)

## 恭喜，你已完成全部配置！

你可以通过配置子流程产生的同步调用 http 接口，在浏览器访问即可获取流程的结果返回。
