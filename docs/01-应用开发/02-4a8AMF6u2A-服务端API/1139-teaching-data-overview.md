---
title: "课堂数据概述"
source_url: "https://open.dingtalk.com/document/development/teaching-data-overview"
namespace: "development"
slug: "teaching-data-overview"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 在线课堂 > 课堂数据概述"
doc_id: "0wt8AB0OGU"
updated_at: "2025-09-23 19:22:58"
---

> Source: https://open.dingtalk.com/document/development/teaching-data-overview
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 在线课堂 > 课堂数据概述
> Updated: 2025-09-23 19:22:58

# 课堂数据概述

## 数据类别

授课的数据读取需要依托前置定义的数据类别及因子，当前已支持的授课数据类别如下：

| 名称 | **编码category\_code** | 包含因子 | 说明 |
| --- | --- | --- | --- |
| 课堂基础数据 | BASIC\_INFO | - 课堂开始时间 - 课堂结束时间 - 课堂参与人数 - 课堂消息数 - 进入课堂时间 - 退出课堂时间 | 授课课堂的基础类别数据 |
| 课堂举手数据 | RAISE\_HAND | - 开始举手时间 - 取消举手时间 | 授课课堂的举手类别数据 |
| 课堂连麦数据 | CONVERSE | - 邀请连麦时间 - 同意连麦时间 - 结束连麦时间 - 踢出连麦时间 | 授课课堂的连麦类别数据 |
| 课堂点名签到数据 | SIGN\_IN | - 点名轮次id - 点名开始时间 - 点名结束时间 - 点名参与总人数 - 实际签到人数 - 点名发起时间 - 是否签到 - 签到具体时间 | 授课课堂的点名签到数据 |

## 数据因子

| 名称 | 编码 | 类别 | 说明 |
| --- | --- | --- | --- |
| 课堂开始时间 | classroomStartTime | 概要数据 | 授课课堂的开始时间 |
| 课堂结束时间 | classroomEndTime | 概要数据 | 授课课堂的结束时间 |
| 课堂参与人数 | classroomMemberCount | 概要数据 | 授课课堂的参与人数，多少人听课 |
| 课堂消息数 | classroomMessageCount | 概要数据 | 授课课堂的整体消息数 |
| 进入课堂时间 | joinClassroomTime | 明细数据 | 授课课堂参与方进入课堂时间 |
| 退出课堂时间 | leaveClassroomTime | 明细数据 | 授课课堂参与方退出课堂时间 |
| 开始举手时间 | raiseTime | 明细数据 | 授课课堂学生举手时间 |
| 取消举手时间 | raiseCancelTime | 明细数据 | 授课课堂学生取消举手时间 |
| 邀请连麦时间 | inviteConverseTime | 明细数据 | 授课课堂老师邀请学生连麦时间 |
| 同意连麦时间 | acceptConverseTime | 明细数据 | 授课课堂学生同意连麦时间 |
| 结束连麦时间 | leaveConverseTime | 明细数据 | 授课课堂学生主动结束连麦时间 |
| 踢出连麦时间 | kickConverseTime | 明细数据 | 授课课堂老师踢出学生连麦时间 |
| 点名轮次id | signInId | 概要数据 | 本点名轮次id |
| 点名开始时间 | signInStartTime | 概要数据 | 本点名轮次开始时间 |
| 点名结束时间 | signInEndTime | 概要数据 | 本点名轮次结束时间 |
| 点名参与总人数 | signInTotalCount | 概要数据 | 本点名轮次实际参与总数 |
| 实际签到人数 | signedInCount | 概要数据 | 本点名轮次实际签到人数 |
| 点名发起时间 | signInCreateTime | 明细数据 | 授课课堂老师发起点名时间 |
| 是否签到 | isSignedIn | 明细数据 | 授课课堂学生是否签到 |
| 签到具体时间 | signedInTime | 明细数据 | 授课课堂学生签到具体时间 |
