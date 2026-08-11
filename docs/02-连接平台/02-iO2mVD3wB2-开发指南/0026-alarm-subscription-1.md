---
title: "告警订阅"
source_url: "https://open.dingtalk.com/document/connection/alarm-subscription-1"
namespace: "connection"
slug: "alarm-subscription-1"
group: "连接平台"
tab: "开发指南"
breadcrumb: "管理连接 > 监控中心 > 告警订阅"
doc_id: "kGBYnfNQ8z"
updated_at: "2025-09-23 19:20:17"
---

> Source: https://open.dingtalk.com/document/connection/alarm-subscription-1
> Path: 连接平台 / 开发指南 / 管理连接 > 监控中心 > 告警订阅
> Updated: 2025-09-23 19:20:17

# 告警订阅

## **告警订阅**

告警订阅提供多个分组关联群机器人，用于订阅流运行过程中的错误告警信息。主要有**搜索订阅组**、**添加告警订阅**、**编辑**、**停/启用**操作，如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3541736761/p557417.png)

- **搜索订阅组：**搜索订阅组功能提供了对告警订阅的关键字查询。
- **添加告警订阅：**添加告警订阅功能，用自定义机器人实现配置连接器的告警订阅，告警信息会自动推送到钉钉群内。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4541736761/p557418.png)

  - **订阅组名称：**填写告警订阅的名称，如连接流告警订阅。
  - **告警对象：**支持连接流和全局告警。选择连接流，则为该流配置告警订阅；选择全局，则新建连接流时自动配置告警订阅。
  - **通知方式**：固定为机器人。
  - **机器人AccessToken**：填写access\_token值，如何获取access\_token值，请参考[自定义机器人接入](https://open.dingtalk.com/document/group/custom-robot-access#title-5lo-5hy-zme)[步骤一：获取自定义机器人Webhook](https://open.dingtalk.com/document/group/custom-robot-access#section-51v-glo-n6z)。
- **操作：**操作功能提供了对告警订阅的编辑和停/启用操作。
