---
title: "数据存储"
source_url: "https://open.dingtalk.com/document/connection/connect-platform-data-storage"
namespace: "connection"
slug: "connect-platform-data-storage"
group: "连接平台"
tab: "开发指南"
breadcrumb: "管理连接 > 连接项目 > 参考 > 数据存储"
doc_id: "a18mBn4phT"
updated_at: "2025-12-08 15:56:13"
---

> Source: https://open.dingtalk.com/document/connection/connect-platform-data-storage
> Path: 连接平台 / 开发指南 / 管理连接 > 连接项目 > 参考 > 数据存储
> Updated: 2025-12-08 15:56:13

# 数据存储

## **背景信息**

在你的企业使用连接平台进行业务操作时，可能会需要创建一个公共数据库，以便存储和管理企业或项目相关的数据信息。数据存储服务能够提供强大的数据管理功能。当你构建数据连接流程时，数据存储可作为数据流的来源，使得不同流程之间能够实现数据的共享、管理和同步。

## **前提条件**

数据存储为连接项目的专有功能，在使用前，请先了解[连接项目](https://open.dingtalk.com/document/connector/create-a-connection-project)如何使用。

## **使用****数据存储**

1. 进入你的某个连接项目，单击左侧导航栏的**数据存储**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2001455071/p757889.png)
2. 单击**创建存储**，即可创建用于各种场景的数据存储项，以下是是创建存储时的一些配置说明：

   | **配置项** | **说明** |
   | --- | --- |
   | 存储名称 | 填写存储名称。 |
   | 存储类型 | 类型：  - 键值对：存放的数据均为 K-V 格式，可通过 Key 来索引查询。 |
   | 存储时间 | 时间：  - 15天 - 永久 |
   | 描述 | 简要介绍说明该数据存储。 |

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2001455071/p757891.png)
3. 创建完成后，你可以单击查看，进入数据存储记录页面，你可以在此处新增记录，或删改记录，也可批量导入满足格式的数据。

   > **[!NOTE]**
   >
   > 每行记录的键值对大小不能超过1.00MB，数据列表可能有延迟（不影响连接流中的使用），最长 15 秒左右。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1001455071/p757892.png)
4. 记录添加完成后，你就可以在连接流中使用已经创建的数据存储，详情参考[使用数据存储更新连接项目数据](https://open.dingtalk.com/document/connector/updating-connection-project-data-using-the-data-store)。
