---
title: "新人入职自动发送培训日程"
source_url: "https://open.dingtalk.com/document/connection/new-recruits-automatically-send-training-schedule"
namespace: "connection"
slug: "new-recruits-automatically-send-training-schedule"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 使用教程 > 日程 > 新人入职自动发送培训日程"
doc_id: "jkYuIKOL36"
updated_at: "2026-07-29 11:47:02"
---

> Source: https://open.dingtalk.com/document/connection/new-recruits-automatically-send-training-schedule
> Path: 连接平台 / 连接器中心 / 官方连接器 > 使用教程 > 日程 > 新人入职自动发送培训日程
> Updated: 2026-07-29 11:47:02

# 新人入职自动发送培训日程

本教程介绍了通过日程连接器，当企业新人入职后向指定人员发送培训日程。

## **预期效果**

![发送日程消息.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5880471961/p705367.png)

## **准备工作**

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。

## **步骤一：**创建连接流

1. 登录[开发者后台](https://open-dev.dingtalk.com/fe/connector#/myFlow)。
2. 单击**开放能力 > 连接平台 > 我的连接流 > 创建连接流。**

   ![创建连接流-新版.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5880471961/p705241.png)

## **步骤二：配置连接流**

1. 配置触发事件：

   1. 选择官方连接器 > 通讯录。

      ![选择连接器-新版-日程.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4880471961/p705252.png)
   2. 选择触发事件 > 通讯录用户增加。

      ![选择触发事件-新版-日程.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5880471961/p705257.png)
2. 配置执行动作：

   1. 选择官方连接器 > 日程。

      ![执行动作官方连接器-日程.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5880471961/p705270.png)
   2. 选择执行动作 > 创建日程（userId版本）。

      ![执行动作-新版-创建日程.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4880471961/p705286.png)
   3. 配置出入参：

      ![参数设置-日程.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2286925871/p705336.png)

      - 日程标题：选择表达式，设置参考如下：

        > **[!NOTE]**
        >
        > `root.用户姓名`参数，需要在**触发事件**中进行选择，否则无法获取用户姓名。

        ```
        CONCATENATE(root.用户姓名,"新人培训")
        ```
      - 组织ID：选择**引用值 > 系统参数 > 流程参数.当前组织ID**。
      - 日程参与人列表：选择**引用值 > 触发事件 >** **root.员工的userid**。
      - 日程开始时间：

        - 日程开始时间：选择表达式，设置参考如下：

          ```
          CONCATENATE(REPLACE(DATEFORMAT(NOW(),'yyyy-MM-dd HH:mm:ss'),11,1,"T"),".000+08:00")
          ```
        - 日程开始时间所属时区：选择**输入值 > 中国标准时间**。
      - 日程描述：选择表达式，设置参考如下：

        > **[!NOTE]**
        >
        > `root.用户姓名`参数，需要在**触发事件**中进行选择，否则无法获取用户姓名。

        ```
        CONCATENATE("欢迎",root.用户姓名,"加入xxxx科技有限责任公司,请xxxx尽快完成新人培训任务。")
        ```
      - 日程组织者的userid：**选择输入值 >** 通过选人组件**选择日程组织者。**
      - 日程所属的日历ID：选择**输入值 > 主日程。**
      - 日程结束时间：

        - 日程结束时间：选择表达式，设置参考如下：

          ```
          CONCATENATE(REPLACE(DATEFORMAT(NOW(),'yyyy-MM-dd HH:mm:ss'),11,3,CONCATENATE("T",IF(HOUR(NOW())>7,SUM(HOUR(NOW()),2),CONCATENATE("0",SUM(HOUR(NOW()),2))))),".000+08:00")
          ```
        - 日程结束时间所属时区：选择**输入值 > 中国标准时间**。
   4. **发布**连接流。

      ![发布-连接流-日程.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4880471961/p705356.png)

## **恭喜，你已完成全部配置！**

你已完成本教程的全部内容，可以通过以下步骤进行体验：

1. 打开钉钉工作台，选择**智能人事 > 员工关系 > 入职管理 > 办理入职**。
2. 员工入职成功后，会创建一个日程并发送给入职员工。
