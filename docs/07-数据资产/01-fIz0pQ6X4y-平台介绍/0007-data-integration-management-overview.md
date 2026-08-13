---
title: "概述"
source_url: "https://open.dingtalk.com/document/dataopen/data-integration-management-overview"
namespace: "dataopen"
slug: "data-integration-management-overview"
group: "数据资产"
tab: "平台介绍"
breadcrumb: "企业客户手册 > 数据集成管理 > 概述"
doc_id: "D2Jp0Nv5FN"
updated_at: "2026-08-12 09:23:44"
---

> Source: https://open.dingtalk.com/document/dataopen/data-integration-management-overview
> Path: 数据资产 / 平台介绍 / 企业客户手册 > 数据集成管理 > 概述
> Updated: 2026-08-12 09:23:44

# 概述

如果你需要了解数据集成管理，你可以参看本文档内容，本文档将帮助你了解什么是数据集成管理和为什么使用数据集成管理。

## 什么是数据集成管理

[数据集成管理](https://open-dev.dingtalk.com/fe/daas#/dataSet)是针对用户在数据资产平台自建的数据源、数据集进行统一管理的界面。除平台提供的官方数据外，用户可以将企业内的业务数据，通过数据集成管理的方式，上架到平台成为用户的自有数据，自有数据完全适配到平台提供的数据服务场景，如自定义仪表盘、发送数据卡片等。

## **为什么使用数据集成管理**

- **业务数据上架平台**

  在数据集成管理之前，用户可用的数据是平台提供的官方数据，基本覆盖组织日常工作的大多数场景。但随着企业业务不断发展扩大，差异化需求的不断涌现，官方数据已经无法满足所有场景，因此平台支持用户将自身业务的数据上架至平台，与官方数据结合，满足用户更多的数据使用场景。
- **支持多种集成方式**

  为满足用户业务数据的不同存储方式，平台目前提供三种集成方式，分别是：Mysql 直连、Hologres 直连、Postgres 直连、连接器触发。用户可根据自身业务存储方式，选择适合的集成方式。
- **适配数据服务**

  用户业务数据上架到平台后，会成为用户自有数据，与官方数据没有区别，可以使用平台的数据服务，如自定义仪表盘、发送数据卡片等。

## **名词解释**

### **数据源**

读取数据的来源，可以是 **Mysql**、**Hologres** 等数据库，同时也支持钉钉连接器的方式。

### 数据集

数据的集合，由字段组成。可以通过拖拽或 JOIN 数据库内的表字段，或者提前定义字段，再由连接器产出数据。

### **连接器**

阿里一站式实时数据仓库引擎，支持海量数据实时写入、实时更新、实时分析，支持标准 SQL（兼容 PostgreSQL 协议），支持 PB 级数据多维分析。

### **Hologres/Postgres**

[钉钉连接平台](https://open-dev.dingtalk.com/fe/connector#/myFlow)搭建的连接媒介，就是用简洁的方式实现应用与应用之间的连接。

> 连接平台上架了[数据资产平台](https://open-dev.dingtalk.com/fe/connector#/market/connector/G-CONN-101A840E5E84213639B7000D?corpId=ding32fff839a3e0105d&gray=1)的连接器，可以实现用户业务数据安全、快速的上架。
