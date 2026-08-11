---
title: "流程暂停"
source_url: "https://open.dingtalk.com/document/connection/process-pause"
namespace: "connection"
slug: "process-pause"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "内置工具 > 流程暂停 > 流程暂停"
doc_id: "E5tPchi7Q8"
updated_at: "2025-09-23 19:20:37"
---

> Source: https://open.dingtalk.com/document/connection/process-pause
> Path: 连接平台 / 连接器中心 / 内置工具 > 流程暂停 > 流程暂停
> Updated: 2025-09-23 19:20:37

# 流程暂停

## **简介**

在流程设计中，你可能需要临时中断流程的执行，并在之后某个合适的时间点再次启动流程。为此，我们提供了**流程暂停**功能，它允许你暂停并在之后恢复流程的运行。这样，就可以灵活地处理那些需要较长时间完成的业务操作。

## **能力说明**

**流程暂停**功能赋予了节点流程可暂停及恢复执行的能力。用户可以按照业务需求，在流程的特定节点处将其暂停，并选择在合适的时间或收到特定回调后继续执行流程。接下来，我们将介绍**流程暂停**的执行动作：

### **延时执行**

当流程执行到当前节点时暂停运行，在某个特定时间点或固定延时时间后，恢复运行。支持两种延时类型：

| **类型** | **描述** |
| --- | --- |
| 固定时间 | 设置一个延时时长T，当流程暂停T时刻后自动恢复运行。  **[!NOTE]**  T最大支持31天，支持以 秒/分钟/小时/天 为单位。 |
| 指定时间 | 设置一个固定日期，到达该日期时自动恢复运行。  **[!NOTE]**  日期需要在31天内。 |

### **从当前节点暂停**

当流程执行到当前节点时暂停运行，可按照提供的流程恢复方式来恢复流程运行。

#### **恢复方式**

目前支持使用 webhook 回调的方式来恢复流程运行。回调 URL 可在流程的执行记录中获取。

> **[!NOTE]**
>
> 回调 URL 说明：
>
> - URL格式：https://connector.dingtalk.com/task/resume?taskId={taskId}
> - URL特征：每次触发流，都会新的唯一 taskId。

## **相关文档**

- [使用流程暂停控制机器人发送消息](https://open.dingtalk.com/document/dingstart/controlling-robot-message-process)
