---
title: "概述"
source_url: "https://open.dingtalk.com/document/connection/connected-platform-field-integration-1"
namespace: "connection"
slug: "connected-platform-field-integration-1"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "概述"
doc_id: "DNF2mQE6Ls"
updated_at: "2026-08-03 09:16:04"
---

> Source: https://open.dingtalk.com/document/connection/connected-platform-field-integration-1
> Path: 连接平台 / 连接平台自动化 / 概述
> Updated: 2026-08-03 09:16:04

# 概述

## 一句话理解

连接平台通过自动化流程，将**多个系统或应用**串在一起进行**自动通信和协作**。

自动化流程 = "如果发生 A 情况，就自动执行 B 操作"，例如："如果到了早上 9 点，就发送机器人消息到项目群"。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1573735071/p753402.png)

## **为什么要使用自动化**

连接平台通过组件化方案，帮助钉钉用户在官方应用内直接获得自动化和集成能力，无需编写代码即可实现：

- ✅ **降低人力成本**：重复性工作交给自动化，释放人力；
- ✅ **提高工作效率**：7×24 小时不间断运行，响应速度更快；
- **✅** **减少人为错误**：标准化流程执行，避免遗漏和误操作；
- ✅ **打通系统孤岛**：让不同应用之间的数据和指令无缝传输。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1573735071/p758385.png)

## 核心概念

### 触发条件

触发条件是自动化流程的起点，决定了流程在什么情况下被激活。常见的触发条件包括：

| **类型** | **示例** |
| --- | --- |
| 定时触发 | 每天早上 9:00、每周一、每月 1 号 |
| 事件触发 | 新人入群、收到特定关键词消息、考勤打卡 |
| 数据变更触发 | 多维表新增记录、审批状态变更 |
| Webhook 触发 | 外部系统推送消息到指定地址 |

### 执行动作

执行动作是触发条件满足后自动执行的操作。一个流程可以包含多个执行动作，按顺序依次执行。常见的执行动作包括：

| **类型** | **示例** |
| --- | --- |
| 发送消息 | 发送文本/图片/卡片消息到群聊或单聊 |
| 数据写入 | 将数据写入 AI 表格、数据库 |
| 调用 API | 调用外部系统接口 |
| 更新状态 | 更新审批状态、修改记录字段 |

### 节点

节点是构成自动化流程的基本单元。一个完整的自动化流程由以下节点组成：

```
[触发条件节点] → [执行动作节点1] → [执行动作节点2] → ...
```

- 触发条件节点：流程的起点，有且仅有一个
- 执行动作节点：可以有多个，按顺序执行
- 参数提取节点（可选）：从上游节点的输出中提取结构化数据

### 场域

场域是指自动化流程运行的场景环境。目前支持以下场域：

| **场域** | **说明** | **典型场景** |
| --- | --- | --- |
| 群聊自动化 | 在钉钉群聊中通过"自动化小助手"运行，**将日常重复的工作自动化，降低人力成本，提高工作效率**。详情参考[群聊自动化](0005-introduction.md)。 | image |
| 考勤自动化 | 与钉钉考勤系统集成，帮助用户**将考勤数据和不同的应用打通**，实现工作流程的自动化。详情参考[考勤自动化](0011-attendance-introduction.md)。 | image |
| AI 表格自动化 | 与钉钉 AI 表格集成，将**数据的变化自动同步给其他应用**，从而降低人力成本，**提高数据同步的效率和准确性**。详情参考[多维表自动化](0013-multidimensional-introduction.md)。 | image |
| 知识库自动化 | 与钉钉知识库集成，详情参考[知识库自动化](0015-connection-introduction-platform.md)。 | 文档归档、知识沉淀 |

## 用量统计

自动化服务的用量以**连接流节点执行量**为计量单位，统计了当前组织在多维表、机器人、OA 审批、连接平台等场域的节点执行量总和。

- 查看方式：获得开发权限的用户可到钉钉连接平台[查看数据详情](https://open-dev.dingtalk.com/fe/connector#/overView)。
- 计费规则：参考 [钉钉连接平台计费模型](../01-6Ar2XD4H6b-平台介绍/0003-connection-platform-billing-model-1.md)。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9759964071/p755093.png)

## **互助社群**

如果你需要了解更多关于自动化的内容，你可以加入钉钉连接平台自动化[官方互助交流群](https://h5.dingtalk.com/ecologicalOrg/index.html?code=v1%2Ck1%2CgaUnK4duo1eD0GVGfs2yQq61QsmresZlTmqsDIU6j7M%3D&origin=11&dd_darkmode=true&dd_mini_app_id=5000000005018615&dtaction=os#/inviteOutsideJoin)。
