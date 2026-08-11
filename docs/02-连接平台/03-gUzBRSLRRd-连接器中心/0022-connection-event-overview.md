---
title: "概述"
source_url: "https://open.dingtalk.com/document/connection/connection-event-overview"
namespace: "connection"
slug: "connection-event-overview"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 日程 > 概述"
doc_id: "2KevT6uFCU"
updated_at: "2025-10-20 18:41:45"
---

> Source: https://open.dingtalk.com/document/connection/connection-event-overview
> Path: 连接平台 / 连接器中心 / 官方连接器 > 日程 > 概述
> Updated: 2025-10-20 18:41:45

# 概述

## **简介**

钉钉日程管理与即时沟通深度结合，同事间共享日程，便捷发起日程会议，重要事情一目了然，团队协作更高效，给员工良好的使用体验。更多介绍请参见[钉钉使用手册-日程](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmbOpyEdYLGLq2?dontjump=true%23%23)。

# **场景说明**

## **触发事件**

| **连接器名称** | **触发事件** | **描述** |
| --- | --- | --- |
| 日程 | 日程变更 | 当用户日程发生创建、更新、取消，用户在本地删除日程时，会触发日程变更事件。 |

## **执行动作**

| **连接器名称** | **执行动作** | **描述** |
| --- | --- | --- |
| 日程 | 创建日程（userId版本） | 创建日程的userId版本，与原版的区别在于原版的用户信息需传入的是unionId，该版本调整为传入userId，比原版需多传入corpId。 |
| 修改日程（userId版本） | 修改日程的userId版本，与原版的区别在于原版的用户信息需传入的是unionId，该版本调整为传入userId，比原版需多传入corpId。 |
| 删除日程（userId版本） | 删除日程的userId版本，与原版的区别在于原版的用户信息需传入的是unionId，该版本调整为传入userId，比原版需多传入corpId。 |
| 查询日历本（userId版本） | 查询日历本的userId版本，与原版的区别在于原版的用户信息需传入的是unionId，该版本调整为传入userId，比原版需多传入corpId。 |
| 添加日程参与者（userId版本） | 添加日程参与者的userId版本，与原版的区别在于原版的用户信息需传入的是unionId，该版本调整为传入userId，比原版需多传入corpId。 |

## **相关链接**

- [新人入职自动发送培训日程](https://open.dingtalk.com/document/dingstart/new-recruits-automatically-send-training-schedule)
