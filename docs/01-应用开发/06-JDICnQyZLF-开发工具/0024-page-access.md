---
title: "页面访问"
source_url: "https://open.dingtalk.com/document/download/page-access"
namespace: "download"
slug: "page-access"
group: "应用开发"
tab: "开发工具"
breadcrumb: "前端监控平台 > 页面访问"
doc_id: "Oz15q395Jp"
updated_at: "2025-12-19 20:26:14"
---

> Source: https://open.dingtalk.com/document/download/page-access
> Path: 应用开发 / 开发工具 / 前端监控平台 > 页面访问
> Updated: 2025-12-19 20:26:14

# 页面访问

在「页面访问」模块中，您可以查看整体的PVUV趋势、性能、异常等数据。通过图表交互可筛选分析维度，进一步下钻查看具体页面的表现情况。

本模块的核心分析维度包括：

- **PV/UV趋势**：页面浏览量（PV）和独立访客数（UV）反映页面的访问热度。数据来源于前端埋点上报，可用于评估活动效果或用户活跃变化。典型场景如大促期间监测首页流量波动。
- **页面性能指标**：包括白屏时间、首屏时间、DOM渲染完成时间等，衡量用户打开页面的响应速度。数据来自浏览器性能API采集，性能下降可能影响转化率，需结合网络环境排查。
- **JS异常统计**：记录页面运行时JavaScript错误的发生频率与类型。数据由全局error事件捕获，当异常率突增时，应检查最新发布的代码版本是否存在兼容性问题。
- **资源加载表现**：展示关键静态资源（如JS、CSS、图片）的加载耗时与失败情况，帮助定位前端性能瓶颈。

## 图表趋势对比

- 显示时间段PVUV的图表趋势。

  ![图表趋势](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2577591361/p328032.png)
- 点击时间点的图形，会作为筛选条件加至下方的结果（包括下方图形统计）。

  ![Top访问页面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2577591361/p328033.png)

## 分析具体页面情况

TOP访问页面，点击 详情 进入具体页面分析，分析维度包括 PVUV趋势、页面性能趋势、JS异常趋势、白屏趋势、资源加载异常趋势。

![分析具体页面情况](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2577591361/p328038.png)
