---
title: "JS异常"
source_url: "https://open.dingtalk.com/document/download/js-exceptions"
namespace: "download"
slug: "js-exceptions"
group: "应用开发"
tab: "开发工具"
breadcrumb: "前端监控平台 > JS异常"
doc_id: "IHa8PaiZLc"
updated_at: "2026-01-22 19:53:07"
---

> Source: https://open.dingtalk.com/document/download/js-exceptions
> Path: 应用开发 / 开发工具 / 前端监控平台 > JS异常
> Updated: 2026-01-22 19:53:07

# JS异常

JS异常分析主要针对用户访问页面遇到JS异常进行实时监控。通过图表统计直观地了解页面运行的健康情况，通过JS异常堆栈智能聚合，sourcemap等功能，快速分析出导致页面使用异常的错误代码。

## **功能概述**

JS异常监控功能主要用于实时捕获和分析用户在访问页面时发生的JavaScript运行时错误。通过该功能，开发者可以全面掌握页面的运行健康状况，及时发现并定位前端代码中的潜在问题。系统会自动对异常堆栈进行智能聚合，并支持 sourcemap 映射等功能，帮助将压缩后的错误代码还原为原始源码位置，从而大幅提升问题排查效率。

本功能适用于企业内部自建应用或第三方企业应用的前端监控场景，尤其适合需要保障核心业务页面稳定性的中大型组织。使用前需确保应用已接入钉钉开放平台前端SDK，并具备相应的权限配置。

## **使用前提与权限要求**

- 适用对象：企业内部自建应用、第三方企业应用开发者
- 权限角色：需具有应用管理员权限，方可开启监控能力并查看数据
- 回调地址：如涉及异常上报回调，必须使用 HTTPS 协议地址

此外，若网络环境受限，建议提前将钉钉API上报域名加入企业网络出口IP白名单，避免因防火墙策略导致数据上报失败。

如何开启JS异常监控，请参考[接入流程](0018-monitoring-center-1.md)。

## 今日指标

可以查看当日异常次数据，异常次数PV比，影响用户以及影响用户占比。

![今日指标](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6477591361/p327948.png)

## 趋势异常对比

- 显示时间段内异常次数和异常次数PV比。

  ![异常pv](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6477591361/p327949.png)
- 点击时间点的图形，会作为筛选条件加至下方的结果（包括下方图形统计）

  ![异常详情](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6477591361/p327950.png)
- 时间段内的异常对比。

  ![异常对比](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7477591361/p327953.png)

## 查看日志

在异常列表中，点击查看日志，可以查看异常的日志详情，包括摘要信息，异常堆栈，设备信息，网络&位置等。

![查看日志](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7477591361/p327954.png)

## 添加筛选条件

点击统计图表，或者列表中的“设为筛选”按钮，可以添加条件至全局，进行分析统计。查看JS异常信息在URL、异常内容、地理、网络、运营商等维度下的分布情况。通过多重维度下去聚合分析问题，快速定位问题点。

![添加筛选条件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7477591361/p327955.png)
