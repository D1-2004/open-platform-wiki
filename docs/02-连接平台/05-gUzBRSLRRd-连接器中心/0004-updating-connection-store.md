---
title: "使用数据存储更新连接项目数据"
source_url: "https://open.dingtalk.com/document/connection/updating-connection-store"
namespace: "connection"
slug: "updating-connection-store"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "内置工具 > 使用教程 > 数据存储 > 使用数据存储更新连接项目数据"
doc_id: "7vrQrYNnAE"
updated_at: "2026-07-30 09:18:42"
---

> Source: https://open.dingtalk.com/document/connection/updating-connection-store
> Path: 连接平台 / 连接器中心 / 内置工具 > 使用教程 > 数据存储 > 使用数据存储更新连接项目数据
> Updated: 2026-07-30 09:18:42

# 使用数据存储更新连接项目数据

本文档将通过一个简单的流程示例为你介绍**数据存储**的使用方式。

## **前提条件**

在使用**数据存储**内置工具前，首先要在当前流程所属的**连接项目**下，创建一个**数据存储项**。

## **操作步骤**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 单击**开放能力** > **连接平台** > **我的连接** > **我的连接流** > **创建连接流**。

   ![我的连接流  创建连接流](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9134735871/p1091131.png)
3. 配置触发事件，选择**内置工具** > **webhook** > **当接受到数据时触发，**无需配置参数。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9134735871/p1091173.png)
4. 配置执行动作（节点2），选择**内置工具 > 数据存储 > 新增或更新键值对**，并配置参数：

   | **配置项** | **值** |
   | --- | --- |
   | 选择需要操作的数据存储 | 选择数字映射。  **[!NOTE]**  在选择前，需要在连接项目中的数据存储功能中创建一张**数字映射**的数据存储表 |
   | 键 | 填写**6**，表示要新增或更新的键为“6”。 |
   | 值 | 填写**这是一个数字6**，表示要将“数字映射”表中键为“6”的值设为“这是一个数字6”，如果键已存在则更新，否则为插入操作。 |

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2234735871/p754443.png)
5. 配置执行动作（节点3），选择**内置工具 > 数据存储 > 查询键值对**，并配置参数：

   | **配置项** | **值** |
   | --- | --- |
   | 选择需要操作的数据存储 | 选择数字映射。  **[!NOTE]**  在选择前，需要在连接项目中的数据存储功能中创建一张**数字映射**的数据存储表 |
   | 键 | 填写**6**，查询“数字映射”存储表中键“6”的值，用于验证上一步是否操作成功。 |

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2234735871/p754444.png)
6. 单击**保存草稿** > **调试**，查看调试效果。

   1. 保存并调试：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2234735871/p754449.png)
   2. 查看调试效果：

      - 新增货更新键值对：

        ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2234735871/p754450.png)
      - 查询键值对：

        ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2234735871/p754452.png)
