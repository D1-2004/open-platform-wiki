---
title: "配置字段模型"
source_url: "https://open.dingtalk.com/document/connection/configure-the-field-model"
namespace: "connection"
slug: "configure-the-field-model"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发参考 > 高级功能 > 字段模型 > 配置字段模型"
doc_id: "VmjG74IiCL"
updated_at: "2025-09-23 19:20:32"
---

> Source: https://open.dingtalk.com/document/connection/configure-the-field-model
> Path: 连接平台 / 开发指南 / 开发参考 > 高级功能 > 字段模型 > 配置字段模型
> Updated: 2025-09-23 19:20:32

# 配置字段模型

本文将介绍如何配置字段模型。

## **前提条件**

1. 登录[集成与自动化服务](https://open-dev.dingtalk.com/fe/connector#/myFlow)平台。
2. 如果无连接器，详情参考[创建连接器](0013-create-connector.md)，如果已有连接器，可直接使用已有连接器。

## **操作步骤**

1. 单击连接器**基本信息 > 高级设置**，开启**字段模型**。

   ![开启字段模型.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8402004961/p714737.png)
2. 执行动作关联字段模型：

   1. 单击**执行动作 >** [添加执行动作](0015-add-execution-action-1.md)。
   2. 配置字段模型，执行动作的入参字段是可以关联字段模型的，本示例关联的是钉钉用户ID模型：

      > **[!IMPORTANT]**
      >
      > 目前仅支持 String、Array<String> 去关联，Array<String> 表示多选。

      1. 单击**可指定字段内容格式**输入框。![配置字段模型.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8402004961/p714703.png)
      2. 选择**钉钉用户ID > UserId**，单击**确认**。

         ![用户ID字段模型.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8402004961/p714732.png)
3. 执行动作调试字段模型，执行动作结创建最后会有调试流程，这里可以看到关联了用户ID的字段直接可以弹出选人组件。

   ![请选择成员模型选择.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8402004961/p714740.png)

   此时，你就可以选择组织内的成员了。

## **更多内容**

### **连接流使用字段模型**

在执行动作的出入参配置，选择关联了字段模型的节点，则会弹出相应的前端组件

例如使用**官方连接器 > 机器人 > 发送文本消息[自定义机器人]**的执行动作，在配置**被@人的工号**时，选择**多种类型**，即可选择成员。![请选择成员使用执行动作.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8402004961/p714763.png)

## **相关文档**

- [字段模型介绍](0045-what-is-a-field-model.md)
