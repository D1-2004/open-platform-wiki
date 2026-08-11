---
title: "数据存储"
source_url: "https://open.dingtalk.com/document/connection/data-storage"
namespace: "connection"
slug: "data-storage"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "内置工具 > 数据存储 > 数据存储"
doc_id: "ddN7yHeZTm"
updated_at: "2025-09-23 19:20:37"
---

> Source: https://open.dingtalk.com/document/connection/data-storage
> Path: 连接平台 / 连接器中心 / 内置工具 > 数据存储 > 数据存储
> Updated: 2025-09-23 19:20:37

# 数据存储

## **简介**

如果你在连接项目中建立了数据存储，用于各流程间共享数据，在设置连接流程时若需读取或改动数据存储内容，可使用**数据存储**内置工具，即可轻松进行数据的管理与查询，确保项目中的数据流转高效顺畅。

> **[!NOTE]**
>
> 在使用**数据存储**内置工具前，首先要在当前流程所属的**连接项目**下，创建一个**数据存储项**。

## **能力说明**

数据存储内置工具能够对当前流程所属连接项目中的数据存储项目进行查询和管理。

### **新增键值对**

往键值对类型存储中新增数据。

#### **入参配置**

| **配置项** | **类型** | **描述** |
| --- | --- | --- |
| 选择需要操作的数据存储（storeId） | String | 数据存储ID。 |
| 键（key） | String | 待新增键名。 |
| 值（value） | String | 值。 |

#### **出参配置**

| **配置项** | **类型** | **描述** |
| --- | --- | --- |
| success | Boolean | 新增是否成功：   - true：成功 - false：失败 |

### **更新键值对**

更新键值对类型存储中的数据。

#### **入参配置**

| **配置项** | **类型** | **描述** |
| --- | --- | --- |
| 选择需要操作的数据存储（storeId） | String | 数据存储ID。 |
| 键（key） | String | 待更新键名。 |
| 值（value） | String | 值。 |

#### **出参配置**

| **配置项** | **类型** | **描述** |
| --- | --- | --- |
| success | Boolean | 更新是否成功：   - true：成功 - false：失败 |

### **删除键值对**

删除键值对类型存储中的数据。

#### **入参配置**

| **配置项** | **类型** | **描述** |
| --- | --- | --- |
| 选择需要操作的数据存储（storeId） | String | 数据存储ID。 |
| 键（key） | String | 待删除键名。 |
| 值（value） | String | 值。 |

#### **出参配置**

| **配置项** | **类型** | **描述** |
| --- | --- | --- |
| result | String | 删除的行数。 |
| success | Boolean | 删除是否成功：   - true：成功 - false：失败 |

### **查询键值对**

数据存在则执行更新，数据不存在则执行创建。

#### **入参配置**

| **配置项** | **类型** | **描述** |
| --- | --- | --- |
| 选择需要操作的数据存储（storeId） | String | 数据存储ID。 |
| 键（key） | String | 待查询键名。 |

#### **出参配置**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| result | Object | 查询结果。 |
| key | String | 查询输入键。 |
| value | String | 键对应的值。 |
| valueFrom | String | 值来源：   - **SYSTEM**：系统写入 - **USER**：用户录入 |
| gmtCreate | String | 创建时间。 |
| gmtModified | String | 修改时间。 |
| success | Boolean | 查询是否成功：   - true：成功 - false：失败 |

### **新增或更新键值对**

数据存在则执行更新，数据不存在则执行创建。

#### **入参配置**

| **配置项** | **类型** | **描述** |
| --- | --- | --- |
| 选择需要操作的数据存储（storeId） | String | 数据存储ID。 |
| 键（key） | String | 待操作键名。 |
| 值（value） | String | 值。 |

#### **出参配置**

| **配置项** | **类型** | **描述** |
| --- | --- | --- |
| success | Boolean | 操作是否成功：   - true：成功 - false：失败 |

## **相关文档**

- [使用数据存储更新连接项目数据](https://open.dingtalk.com/document/dingstart/updating-connection-store)+
