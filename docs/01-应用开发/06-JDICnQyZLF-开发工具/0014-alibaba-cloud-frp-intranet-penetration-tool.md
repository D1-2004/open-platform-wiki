---
title: "frp内网穿透工具"
source_url: "https://open.dingtalk.com/document/download/alibaba-cloud-frp-intranet-penetration-tool"
namespace: "download"
slug: "alibaba-cloud-frp-intranet-penetration-tool"
group: "应用开发"
tab: "开发工具"
breadcrumb: "内网穿透工具 > frp内网穿透工具"
doc_id: "SPNZCe5kGx"
updated_at: "2026-01-22 19:53:06"
---

> Source: https://open.dingtalk.com/document/download/alibaba-cloud-frp-intranet-penetration-tool
> Path: 应用开发 / 开发工具 / 内网穿透工具 > frp内网穿透工具
> Updated: 2026-01-22 19:53:06

# frp内网穿透工具

本文档介绍了如何配置和使用frp内网穿透工具，实现将内网服务安全、便捷地暴露到公网。frp（Fast Reverse Proxy）是一款高性能的反向代理应用，广泛应用于开发调试、远程访问、本地服务共享等场景。

> **[!IMPORTANT]**
>
> - frp内网穿透工具是一款三方开源工具，具体使用方式请参考[frp Github](https://github.com/fatedier/frp)。
> - 本文档提供基础的frp使用步骤仅供参考，可网络搜索frp内网穿透工具配置教程。

## 前置条件

- ✅ 拥有一台具备公网 IP 的服务器（如云主机 ECS），用于部署 frp 服务端（frps）。
- ✅ 已注册域名，并完成 DNS 解析：将主域名（如 `frps.com`）的 A 记录指向公网服务器 IP。
- ✅ 内网设备可正常运行待暴露的服务（如 Web 服务运行在 `localhost:8000`）。
- ✅ 确保公网服务器的安全组或防火墙已放行以下端口：

  - `7000`：frp 客户端通信端口（`bind_port`）
  - `80`：HTTP 流量访问端口（`vhost_http_port`）
  - `6000`（可选）：SSH 穿透端口

## 什么是frp

frp（Fast Reverse Proxy）是一个专注于内网穿透的高性能反向代理工具，支持 TCP、UDP、HTTP、HTTPS 等多种协议。它通过在具有公网 IP 的节点上部署服务端（frps），在内网节点上部署客户端（frpc），建立安全隧道，将内网服务以反向代理的方式暴露至公网。

## 步骤一：服务端安装

1. 执行以下命令，下载frp工具压缩包。

   ```
   wget https://github.com/fatedier/frp/releases/download/v0.38.0/frp_0.38.0_linux_amd64.tar.gz
   ```
2. 执行以下命令，解压frp工具包。

   ```
   tar -xvf frp_0.38.0_linux_amd64.tar.gz
   ```
3. 执行以下命令，移动至`/usr/local`目录。

   ```
   mkdir /usr/local/frp
   mv frp_0.38.0_linux_amd64/* /usr/local/frp/
   ```
4. （可选）删除frpc.ini和frpc文件，frpc相关的文件属于客户端配置。

## 步骤二：服务端配置

1. 执行以下命令进入frp文件夹。

   ```
   cd /usr/local/frp
   ```
2. 执行以下命令编辑frps服务端配置文件。

   ```
   vi frps.ini
   ```
3. frps服务端配置文件内写入以下信息。

   ```
   [common] # 必须设置
   bind_port = 7000 # frp服务端端口，默认7000
   vhost_http_port = 80 # 自定义设置的http访问端口

   [ssh] # ssh反向代理(不是必须设置)
   listen_port = 6000 #设定的ssh访问端口

   [web] 
   type = http # 为服务类型，可以设为http,https
   custom_domains = frps.com # 为要映射的域名，记得域名的A记录要解析到外网主机的IP。
   ```
4. 执行以下命令启动frps。

   ```
   ./frps -c ./frps.ini
   ```

   **预期输出示例**：

   ```
   2023/04/01 12:00:00 [I] [service.go:192] frps tcp listen on 0.0.0.0:7000
   2023/04/01 12:00:00 [I] [service.go:207] http service listen on 0.0.0.0:80
   2023/04/01 12:00:00 [I] [root.go:204] Start frps success
   ```

   > **风险提示：**请确保公网服务器的安全组/防火墙已放行 `bind_port`（7000）和 `vhost_http_port`（80），否则客户端无法连接，外部也无法访问服务。

## **步骤三：客户端安装**

1. 执行以下命令，下载frp工具压缩包。

   ```
   wget https://github.com/fatedier/frp/releases/download/v0.38.0/frp_0.38.0_linux_amd64.tar.gz
   ```
2. 执行以下命令，解压frp工具包。

   ```
   tar -xvf frp_0.38.0_linux_amd64.tar.gz
   ```
3. 执行以下命令，根据自己的偏好，移动至目标文件夹。

   ```
   mkdir /usr/local/frp
   mv frp_0.38.0_linux_amd64/* /usr/local/frp/
   ```
4. （可选）删除frps.ini和frps文件，frps相关的文件属于服务端配置。

## **步骤四：客户端配置**

1. 执行以下命令进入frp文件夹。

   ```
   cd /usr/local/frp
   ```
2. 执行以下命令编辑frpc客户端配置文件。

   ```
   vi frpc.ini
   ```
3. frpc客户端配置文件内写入以下信息。

   ```
   [common]
   server_addr = x.x.x.x    # frps所在主机的IP
   server_port = 7000       # frps与frpc客户端通信的端口

   [web-compute1]           # 内网多台web服务器，此名称不能重复
   type = http              # 通信协议类型   
   local_port = 8000        # 本地开放的web端口
   subdomain = compute1     # 子域名
   ```
4. 执行以下命令启动frpc。

   ```
   ./frpc -c ./frpc.ini
   ```

   **预期输出示例**：

   ```
   2023/04/01 12:05:00 [I] [service.go:308] [client: xxx] login to server success, get run id xxx
   2023/04/01 12:05:00 [I] [proxy_manager.go:144] [client: xxx] proxy added: [web-compute1]
   2023/04/01 12:05:00 [I] [control.go:180] [web-compute1] start proxy success
   ```

## 验证与使用

完成上述配置后，您可以通过以下方式验证服务是否生效：

1. 打开浏览器，访问：`compute1.frps.com:8080`
2. 若配置正确且服务端运行正常，您将看到内网 `localhost:8000` 上运行的应用界面。
