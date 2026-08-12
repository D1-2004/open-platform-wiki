---
title: "将抖音多条视频列表数据同步到多维表"
source_url: "https://open.dingtalk.com/document/connection/synchronize-multiple-dimensional"
namespace: "connection"
slug: "synchronize-multiple-dimensional"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "三方连接器 > 使用教程 > 抖音 > 将抖音多条视频列表数据同步到多维表"
doc_id: "kVI0cEo6hw"
updated_at: "2026-05-19 19:46:26"
---

> Source: https://open.dingtalk.com/document/connection/synchronize-multiple-dimensional
> Path: 连接平台 / 连接器中心 / 三方连接器 > 使用教程 > 抖音 > 将抖音多条视频列表数据同步到多维表
> Updated: 2026-05-19 19:46:26

# 将抖音多条视频列表数据同步到多维表

## **准备工作**

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 入驻抖音开放平台，获取 抖音开放平台应用App Key 、 App Secret。

## 操作步骤

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 单击**开放能力** > **连接平台** > **我的连接** > **我的连接流** > **创建连接流**。
3. 配置触发事件：

   1. 选择**内置工具**> **子流程 > 当被调用时触发**。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751036.png)
   2. 单击**设置入参，**填写参数信息**。**![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751037.png)
   3. 开启**同步调用，**获取同步调用地址**。**![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751040.png)
4. 配置执行动作（节点2）:

   1. 选择抖音三方连接器。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751042.png)
   2. 选择**执行动作** > **查询视频列表。**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751043.png)
   3. **配置账号，**填写准备工作中获取的 抖音开放应用 的凭证信息 并 选取授权范围为视频列表。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751046.png)
   4. 配置参数：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751050.png)
5. 配置循环（节点3）:

   1. 选择**内置工具** > **循环执行：**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751051.png)
   2. 选择数据类型为数组，循环内容为抖音连接器获取的视频列表。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751055.png)
6. 配置执行动作（节点4）：

   1. 在循环中选择多维表官方连接器。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751058.png)
   2. 选择**执行动作** > **插入数据**：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751059.png)
   3. 在钉钉文档中创建多维表**视频列表 >** 新建数据表**视频数据列表。**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751062.png)
   4. 在表格视图中设置需要输出的出参列名与类型，具体列名可在[抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/video-management/douyin/search-video/account-video-list)或 连接器出参 中查询

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751064.png)
   5. 配置循环中多维表的参数（数据表若下拉列表中没有，可以手动输入）

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751066.png)
   6. 单击**调试并在多维表中查看同步的数据**，完成测试。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751067.png)

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751068.png)
7. 测试完成后，发布连接流。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4205573071/p751069.png)

## 恭喜，你已完成全部配置！

你可以通过配置子流程产生的同步调用 http 接口，在浏览器或postman中访问，即可获取流程的结果返回。
