---
title: "汇总统计"
source_url: "https://open.dingtalk.com/document/connection/summary-statistics"
namespace: "connection"
slug: "summary-statistics"
group: "连接平台"
tab: "开发指南"
breadcrumb: "管理连接 > 监控中心 > 汇总统计"
doc_id: "1rSwRiwVJr"
updated_at: "2025-09-23 19:20:16"
---

> Source: https://open.dingtalk.com/document/connection/summary-statistics
> Path: 连接平台 / 开发指南 / 管理连接 > 监控中心 > 汇总统计
> Updated: 2025-09-23 19:20:16

# 汇总统计

## **汇总统计**

汇总统计提供了对某月连接流执行情况的汇总，可以查看连接流**实时用量统计**、**消耗趋势**、**连接流执行明细**以及**执行次数最好的10个连接流**。

1. 选择需要统计的月份

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0541736761/p557395.png)
2. 查看汇总统计结果

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1541736761/p557400.png)

- **实际用量统计：**主要统计了本月使用额度，本月总额度以及本月剩余额度。

> **[!NOTE]**
>
> 钉钉专业版额度为300000次/月，专业版到期后总额度将恢复8000次/月。

- **消耗趋势：**可以查看当日流执行次数。

> **[!NOTE]**
>
> 汇总统计采用的是T+1累计指标，需要第二天才能看到前一天的数据。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1541736761/p557403.png)

- **连接流执行明细**

  - 支持查看连接流调用来源，执行总次数，失败总次数，成功率，以及查看详情。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1541736761/p557407.png)
  - 针对成功率较低的流，可以点击查看详情，查看连接流的执行详情。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1541736761/p557408.png)

    连接流执行详情包括查看状态、触发时间、耗时、失败原因、以及操作（查看详情、复制ID以及重试）。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1541736761/p557409.png)
