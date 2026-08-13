---
title: "概述"
source_url: "https://open.dingtalk.com/document/connection/master-connection-overview"
namespace: "connection"
slug: "master-connection-overview"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发参考 > 高级功能 > 概述"
doc_id: "RdEq83ul5L"
updated_at: "2025-10-20 18:35:53"
---

> Source: https://open.dingtalk.com/document/connection/master-connection-overview
> Path: 连接平台 / 我的连接 / 开发参考 > 高级功能 > 概述
> Updated: 2025-10-20 18:35:53

# 概述

本文将为您简单介绍连接器配置中的高级功能。

## **概览**

| **高级功能** | **说明** |
| --- | --- |
| [主数据](0028-tips-for-using-the-master-data-model.md) | 开启后可以选择主数据模型进行映射 |
| **集成网关** | 开启后在连接器中可以配置集成网关类型的触发事件和执行动作，解决没有固定输入输出模型场景 |
| **动态出参** | 支持执行动作动态出参结构，不必配置出参Schema。  注意：动态出参的执行动作不支持非HTTP接口及连接平台以外的场景 |
| [字段模型](0030-what-is-a-field-model.md) | 支持执行动作绑定字段模型 |
| **场景模型** | 支持执行动作关联场景模型，从而可以在钉钉工作台、卡片平台等使用 |
| **私有动作** | 设置执行动作是否对用户可见 |
| [域名变量](0029-domain-name-variable-1.md) | 设置接口域名为环境变量。若为不同客户提供服务的域名不相同时，可开启本开关，开启后域名由客户自行配置。 |
