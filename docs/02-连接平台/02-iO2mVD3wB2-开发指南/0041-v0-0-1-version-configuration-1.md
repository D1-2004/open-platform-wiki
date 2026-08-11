---
title: "v0.0.1 版本配置"
source_url: "https://open.dingtalk.com/document/connection/v0-0-1-version-configuration-1"
namespace: "connection"
slug: "v0-0-1-version-configuration-1"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发参考 > 本地网关 > v0.0.1 版本配置"
doc_id: "9NE5jAI7ll"
updated_at: "2025-09-23 19:20:28"
---

> Source: https://open.dingtalk.com/document/connection/v0-0-1-version-configuration-1
> Path: 连接平台 / 开发指南 / 开发参考 > 本地网关 > v0.0.1 版本配置
> Updated: 2025-09-23 19:20:28

# v0.0.1 版本配置

v0.0.1 为过时版本，不推荐使用。获取最新的客户端请前往[Github发布页](https://github.com/open-dingtalk/ipaas-agent/releases/latest)。

## **配置文件说明**

ipaas-agent 使用 YAML 格式的配置文件。下面是配置文件各字段的详细说明：

### **client 配置**

- **client\_id**: 你的钉钉开放平台应用的ID（Client ID），可以登录钉钉[开发者后台](https://open-dev.dingtalk.com/fe/app#/corp/app)，进入应用详情页获取。
- client\_secret: 该应用的客户端密钥（Client Secret），可以登录钉钉[开发者后台](https://open-dev.dingtalk.com/fe/app#/corp/app)，进入应用详情页获取。

### mysql 配置

配置文件中 mysql 部分是用来定义数据库连接的，它可以包含多个数据库配置，但不是必须的。每个数据库配置包括以下字段：

- host：数据库服务器的主机名或IP地址。
- addr：数据库服务器的地址和端口，通常格式为 hostname:port。
- username：用于连接数据库的用户名称。
- password：用于连接数据库的密码。
- database：要连接的数据库名。
- config：额外的数据库连接配置，如：

  - max\_open\_conns：数据库连接池允许的最大打开连接数。
  - max\_idle\_conns：数据库连接池允许的最大空闲连接数。
- config\_key：此数据库配置的引用键名，用于在连接平台鉴权配置中引用特定数据库配置。

> **[!NOTE]**
>
> agent 的 mysql 代理只对 sql 做转发，没有审计功能，请使用者注意误操作或其他因素可能带来的数据安全问题，建议为 agent 单独分配一个权限合理的数据库账户，使用 mysql 账户体系限制 agent 执行高危操作，例如删除表、删除库等。

## **使用示例**

1. 在你的项目目录中添加一个名为 config.yml 的配置文件，根据上述字段填写对应的信息。例如：

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

   确保 client 部分包含有效的 client\_id 和 client\_secret，mysql 部分包含正确的数据库连接信息。
2. 新建一条连接流：

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9911362071/p747710.png)
3. 选择三方 MySQL 连接器，并添加和使用连接凭证。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9911362071/p747712.png)
4. 编写查询语句：

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9911362071/p747713.png)

   测试预览后可以在连接平台获取到本地数据库的数据。
