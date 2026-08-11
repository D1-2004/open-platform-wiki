---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/yl-parameter-description"
namespace: "connection"
slug: "yl-parameter-description"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "三方连接器 > 1688 > 参数说明"
doc_id: "HEG90Lfjeq"
updated_at: "2025-09-23 19:21:33"
---

> Source: https://open.dingtalk.com/document/connection/yl-parameter-description
> Path: 连接平台 / 连接器中心 / 三方连接器 > 1688 > 参数说明
> Updated: 2025-09-23 19:21:33

# 参数说明

## **执行动作说明**

## **根据关键词搜索类目**

| **入参** | **类型** | **是否必填** | **详细说明** |
| --- | --- | --- | --- |
| appkey | String | 是 | 企业入驻1688平台创建应用时产生的应用鉴权标识。 |
| keyword | String | 是 | 关键词。 |

## **采购商品比价**

| **入参** | **类型** | **是否必填** | **详细说明** |
| --- | --- | --- | --- |
| appkey | String | 是 | 企业入驻1688平台创建应用时产生的应用鉴权标识。 |
| scenario | String | 是 | 场景，默认填all。 |
| param | Object | 是 | 跨境关键词搜索参数。 |
| keywords | String | 是 | 关键词，示例值：帐篷。 |
| categoryIds | Array<String> | 是 | 限定类目ID列表，示例值：["201901404"]。 |
| quantityBegin | Long | 是 | 起批量，示例值：2。 |
| priceStart | String | 是 | 价格区间过滤，起始价格，示例值：10。 |
| priceEnd | String | 是 | 价格区间过滤，终止价格，示例值：100。 |
| sortType | String | 是 | 排序字段，price 价格排序，va\_rmdarkgmv30rt 30天成交额排序。 |
| sortOrder | String | 是 | 降序desc还是升序asc，默认不传算法排序。 |
| filter | Array<String> | 是 | 过滤参数，shipIn48Hours（48小时发货），freeExchange7days（7天包换），powerMerchant（实力商家），crossPotential(跨境潜力商品)，ttpft(批发团商品)，jxhy(精选货源商品)。 |
| pageSize | Long | 是 | 翻页大小，最大支持100，示例值：20。 |
| pageNum | Long | 是 | 当前页，示例值：1。 |
