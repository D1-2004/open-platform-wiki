---
title: "v0.0.1 版本配置"
source_url: "https://open.dingtalk.com/document/connection/v0-0-1-version-configuration-1"
namespace: "connection"
slug: "v0-0-1-version-configuration-1"
group: "连接平台"
tab: "配置中心"
breadcrumb: "本地网关 > v0.0.1 版本配置"
doc_id: "9NE5jAI7ll"
updated_at: "2026-07-30 09:18:37"
---

> Source: https://open.dingtalk.com/document/connection/v0-0-1-version-configuration-1
> Path: 连接平台 / 配置中心 / 本地网关 > v0.0.1 版本配置
> Updated: 2026-07-30 09:18:37

# v0.0.1 版本配置

> **[!NOTE]**
>
> v0.0.1 为过时版本，不推荐使用。获取最新的客户端请前往[Github发布页](https://github.com/open-dingtalk/ipaas-agent/releases/latest)。

## **配置文件说明**

ipaas-agent 使用 YAML 格式的配置文件。下面是配置文件各字段的详细说明：

### **client 配置**

- **client\_id**: 你的钉钉开放平台应用的ID（Client ID），可登录[开发者后台](https://open-dev.dingtalk.com/fe/app#/corp/app)获取。
- **client\_secret**: 该应用的客户端密钥（Client Secret），同样可在钉钉开发者后台获取。

### mysql 配置

配置文件中的 `mysql` 部分用于定义数据库连接，支持多个数据库配置，但非必须。每个数据库配置包含以下字段：

| **字段** | **说明** |
| --- | --- |
| host | 数据库服务器的主机名或IP地址。 |
| addr | 数据库服务器的地址和端口，通常格式为 `hostname:port`。 |
| username | 用于连接数据库的用户名称。 |
| password | 用于连接数据库的密码。 |
| database | 要连接的数据库名。 |
| config | 额外的数据库连接配置，如：   - **max\_open\_conns**：数据库连接池允许的最大打开连接数。 - **max\_idle\_conns**：数据库连接池允许的最大空闲连接数。 |
| config\_key | 此数据库配置的引用键名，用于在连接平台鉴权配置中引用特定数据库配置。 |

> **[!IMPORTANT]**
>
> Agent 的 MySQL 代理仅对 SQL 语句做透明转发，不提供审计功能。为避免误操作或其他因素导致的数据安全风险，建议为 Agent 单独分配权限受限的数据库账户，通过 MySQL 账户体系限制其执行高危操作（如删除表、删除库等）。

## **使用示例**

1. 在项目目录中添加名为 `config.yml` 配置文件，根据上述字段填写对应的信息。例如：

   > **[!NOTE]**
   >
   > 确保 `client` 部分包含有效的 `client_id` 和 `client_secret`，`mysql` 部分包含正确的数据库连接信息。

   ```
   client:
     client_id: dingeypapfxxx
     client_secret: 3YZT7mQjlIxxx
   mysql:
     - host: localhost
       addr: localhost:3306
       username: root
       password: root
       database: example
       config:
         max_open_conns: 10
         max_idle_conns: 5
       config_key: default
   ```
2. 新建一条连接流，如下图所示：

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7134735871/p747710.png)
3. 选择三方 MySQL 连接器，并添加和使用连接凭证。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7134735871/p747712.png)
4. 编写查询语句：

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9911362071/p747713.png)

   测试预览后可以在连接平台获取到本地数据库的数据。
