---
title: "配置文件介绍"
source_url: "https://open.dingtalk.com/document/connection/local-gateway-configuration-1"
namespace: "connection"
slug: "local-gateway-configuration-1"
group: "连接平台"
tab: "配置中心"
breadcrumb: "本地网关 > 配置文件介绍"
doc_id: "ZvQ5lkSN2N"
updated_at: "2026-07-30 09:18:36"
---

> Source: https://open.dingtalk.com/document/connection/local-gateway-configuration-1
> Path: 连接平台 / 配置中心 / 本地网关 > 配置文件介绍
> Updated: 2026-07-30 09:18:36

# 配置文件介绍

本地网关客户端使用 YAML 格式的配置文件来配置代理的行为。配置文件中包含以下部分：

## **Client 配置**

以下两个字段为**必填项**，用于身份验证和与钉钉开放平台的通信：

- `client_id`: 你的钉钉开放平台应用的客户端ID（AppKey），可登录[开发者后台](https://open-dev.dingtalk.com/fe/app#/corp/app)获取。
- `client_secret`: 该应用的客户端密钥（AppSecret），同样可在钉钉开发者后台获取。

## **插件配置**

### **MySQL 配置**

配置文件中 `plugin.mysql`部分用于定义数据库连接，支持多个数据库配置（列表格式）。每个数据库配置包含以下字段：

| **字段** | **说明** |
| --- | --- |
| host | 数据库服务器的主机名或IP地址。 |
| port | 数据库服务器的端口号。 |
| username | 用于连接数据库的用户名称。 |
| password | 用于连接数据库的密码。 |
| database | 要连接的数据库名。 |
| config\_key | 此数据库配置的引用键名，用于在代码中引用特定数据库配置。 |

**鉴权配置**：

- `auth.mysql.allow_remote`: 是否允许远程配置。设置为 `true`时允许连接平台传入临时配置；设置为 `false`时只允许本地配置文件的设置。

### **PostgreSQL 配置**

配置文件中的`plugin.pgsql`部分用于定义 PostgreSQL 数据库连接，每个数据库配置包含以下字段：

| **字段** | **说明** |
| --- | --- |
| host | 数据库服务器的主机名或IP地址。 |
| port | 数据库服务器的端口号。 |
| username | 用于连接数据库的用户名称。 |
| password | 用于连接数据库的密码。 |
| database | 要连接的数据库名。 |
| config\_key | 此数据库配置的引用键名，用于在代码中引用特定数据库配置。 |

**鉴权配置**：

- `auth.pgsql.allow_remote`: 是否允许远程配置。设置为 `true`时允许连接平台传入临时配置；设置为 `false`时只允许本地配置文件的设置。

### **MS SQL Server 配置**

配置文件中的 `plugin.mssql` 部分用于定义微软 SQL Server 数据库连接，支持多个数据库配置（列表格式）。每个数据库配置包含以下字段：

| **字段** | **说明** |
| --- | --- |
| host | 数据库服务器的主机名或IP地址。 |
| port | 数据库服务器的端口号。 |
| user | 用于连接数据库的用户名称。 |
| password | 用于连接数据库的密码。 |
| database | 要连接的数据库名。 |
| config\_key | 此数据库配置的引用键名，用于在代码中引用特定数据库配置。 |

**鉴权配置**：

- `auth.mssql.allow_remote`: 是否允许远程配置。设置为 `true`时允许连接平台传入临时配置；设置为 `false`时只允许本地配置文件的设置。

### **Oracle DB 配置**

配置文件中的 `plugin.oracledb` 部分用于定义 Oracle 数据库连接，支持多个数据库配置（列表格式）。每个数据库配置包含以下字段：

| **字段** | **说明** |
| --- | --- |
| host | 数据库服务器的主机名或IP地址。 |
| port | 数据库服务器的端口号。 |
| user | 用于连接数据库的用户名称。 |
| password | 用于连接数据库的密码。 |
| sid | 要连接的数据库实例的SID。 |
| service\_name | 数据库的Service Name，和SID二选一。 |
| config\_key | 此数据库配置的引用键名，用于在代码中引用特定数据库配置。 |

**鉴权配置**：

- `auth.oracledb.allow_remote`: 是否允许远程配置。设置为 `true`时允许连接平台传入临时配置；设置为 `false`时只允许本地配置文件的设置。

## **示例**

一个完整的配置文件可能如下所示。

```
client:
  client_id: dingeypapxxxxxxxxxxx
  client_secret: xxxxxxxxxx7mQjlIF7q6YiFitxxxxxxxxxxxxxxxxxxxx
plugins:
  mssql:
    - host: localhost
      port: 1433
      address: localhost:1433
      user: sa
      password: sa123456A
      database: TestDB
      config_key: sqlServer
  mysql:
    - host: localhost
      port: 3306
      address: localhost:1433
      user: root
      password: root
      database: example
      config_key: default
  oracledb:
    - host: localhost
      port: 1521
      address: localhost:1521
      user: system
      password: example
      sid: FREE
      config_key: oracaldb
auth:
  mssql:
    allow_remote: true
  mysql:
    allow_remote: true
  pgsql:
    allow_remote: true
```
