---
title: "概述"
source_url: "https://open.dingtalk.com/document/connection/application-management-overview"
namespace: "connection"
slug: "application-management-overview"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 应用管理 > 概述"
doc_id: "CTpLjk09S9"
updated_at: "2025-09-23 19:21:24"
---

> Source: https://open.dingtalk.com/document/connection/application-management-overview
> Path: 连接平台 / 连接器中心 / 官方连接器 > 应用管理 > 概述
> Updated: 2025-09-23 19:21:24

# 概述

本文详细介绍了应用管理的执行动作。

## **简介**

应用管理是钉钉提供的开放能力之一，用于获取企业内部应用的基础信息、对企业内部应用-网页应用的管理，例如创建应用、删除应用、设置应用的可使用范围等。

## **执行动作**

| **执行动作** | **描述** |
| --- | --- |
| 获取应用列表 | 获取企业所有应用的信息，包括应用名称、应用描述、应用图标、应用访问地址等。  **[!NOTE]**   - 如果是企业主管理员，在企业管理后台-应用管理列表页，可以查看到所有的应用信息。 - 如果是企业子管理员，必须同时拥有全部应用管理权限，在企业管理后台-应用管理列表页，可以查看所有应用的信息。 |
| 设置应用的可见范围 | 设置指定应用的可见范围。  **[!NOTE]**  企业内部应用-网页应用：   - 当前网页应用是开发版本，调用本接口可指定网页应用开发版本的可见范围。 - 当前网页应用是线上版本，调用本接口可指定网页应用线上版本的可见范围。   企业内部应用-小程序应用：   - 仅在小程序线上版本适用。 |
| 获取应用的可见范围 | 根据应用agentId参数，获取应用的可见范围。 |
| 获取员工可见的应用列表 | 根据用户ID，查询用户可见的应用列表。 |
