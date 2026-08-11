---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/multidimensional-table-overview"
namespace: "connection"
slug: "multidimensional-table-overview"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > AI能力 > 参数说明"
doc_id: "omQ1TooIYP"
updated_at: "2025-09-23 19:20:58"
---

> Source: https://open.dingtalk.com/document/connection/multidimensional-table-overview
> Path: 连接平台 / 连接器中心 / 官方连接器 > AI能力 > 参数说明
> Updated: 2025-09-23 19:20:58

# 参数说明

## **执行动作**

## **文本翻译**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| query | String | 翻译源文字符串。 |
| source\_language | String | 翻译源语言类型。 |
| target\_language | String | 翻译目标语言类型。 |

## **OCR文字识别**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| image\_url | String | 识别图片地址，最大长度1000。 |
| type | String | 识别图片类型：   - **idcard**：身份证 - **invoice**：营业执照增值税发票 - **blicense**：营业执照 - **bank\_card**：银行卡 - **car\_no**：车牌 - **car\_invoice**：机动车发票 - **driving\_license**：驾驶证 - **vehicle\_license**：行驶证 - **train\_ticket**：火车票 - **quota\_invoice**：定额发票 - **taxi\_ticket**：出租车发票 - **air\_itinerary**：机票行程单 - **approval\_table**：审批表单 - **roster**：花名册 |
