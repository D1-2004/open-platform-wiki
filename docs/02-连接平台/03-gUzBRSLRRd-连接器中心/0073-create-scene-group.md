---
title: "创建场景群"
source_url: "https://open.dingtalk.com/document/connection/create-scene-group"
namespace: "connection"
slug: "create-scene-group"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 会话管理（场景群） > 使用教程 > 创建场景群"
doc_id: "otzEpfNfsS"
updated_at: "2026-05-19 19:46:13"
---

> Source: https://open.dingtalk.com/document/connection/create-scene-group
> Path: 连接平台 / 连接器中心 / 官方连接器 > 会话管理（场景群） > 使用教程 > 创建场景群
> Updated: 2026-05-19 19:46:13

# 创建场景群

## **简介**

场景群是钉钉特有的一个协同办公能力，为用户提供基于具体业务场景下的群内服务。创建群聊会话之后，相关的群快捷栏、群助手、群消息推送等能力将同时初始化完毕，用户即刻就可以使用。本文将指导用户如何创建一个场景群。

查看更多执行动作

## 准备工作

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 已经创建了一个[企业内部应用](../../01-应用开发/01-XOnnmGCTbn-开发指南/0007-create-application.md)。

## **预期效果**

通过连接平台，编排连接流，完成场景群的创建。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1003409861/p691874.png)

## **步骤一：创建连接器**

- 如果无连接器，详情参见[创建连接器](../02-iO2mVD3wB2-开发指南/0013-create-connector.md)。
- 如果已有连接器，可直接使用已有连接器。

## **步骤二：配置触发事件**

1. 选择创建的连接器进入详情页面，然后依次选择**触发事件 > 创建触发事件**。![连接器-创建触发事件..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7984055861/p674345.png)
2. 填写触发事件的基础信息。
3. 在模型配置界面下，配置**触发事件入参**参数，然后单击**下一步**。

   ![配置场景群触发事件.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1003409861/p691975.png)
4. 在调试界面下，填写**触发事件入参**参数，然后单击**立即调试**。

   ![场景群触发事件-调试.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1003409861/p691979.png)
5. 调试完成之后，选择**发布**。

   ![发布触发事件-场景群.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1003409861/p692009.png)

## **步骤三：创建连接流**

1. [创建连接流](../02-iO2mVD3wB2-开发指南/0002-create-a-connection-flow-1.md)，并完善连接流基本信息。
2. 配置触发事件：

   1. 选择自建连接器。

      > **[!NOTE]**
      >
      > 选择步骤一中创建的自建连接器。

      ![选择连接器-工作通知文本.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0163548861/p689676.png)
   2. 选择触发事件。

      > **[!NOTE]**
      >
      > 选择步骤二中发布的触发事件。

      ![触发事件选择-场景群.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1003409861/p692215.png)
   3. 完成配置。

      ![场景群-完成触发事件.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1003409861/p692216.png)
3. 配置执行动作：

   1. 选择官方连接器。

      ![会话管理执行动作-场景群.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1003409861/p692218.png)
   2. 选择执行动作。

      ![场景群创建执行动作选择-场景群.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1003409861/p692220.png)
   3. 配置参数。

      ![点击进行配置-场景群.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1003409861/p692221.png)
   4. 测试并预览

      1. 输入测试值。

         ![测试并预览-场景群.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1003409861/p692222.png)
      2. 完成测试。

         ![完成测试-场景群.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1003409861/p692227.png)

         此时场景群就已经创建完成。
   5. 发布连接流。

      ![连接流发布-场景群.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1003409861/p692232.png)

## 恭喜，你已完成全部配置！

你已完成本教程的全部内容，可以通过以下方式进行体验。

1. 获取触发事件[方式一（推荐）：通过Webhook地址触发事件](../02-iO2mVD3wB2-开发指南/0016-using-connectors-1.md#636e0c4a67u8r)地址。
2. 根据Webhook地址，体验场景群的创建。

![Webhook测试-场景群.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1003409861/p692238.png)
