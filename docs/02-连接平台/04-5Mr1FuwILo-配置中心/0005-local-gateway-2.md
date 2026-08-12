---
title: "本地网关配置"
source_url: "https://open.dingtalk.com/document/connection/local-gateway-2"
namespace: "connection"
slug: "local-gateway-2"
group: "连接平台"
tab: "配置中心"
breadcrumb: "本地网关 > 本地网关配置"
doc_id: "zgIFkbwtrJ"
updated_at: "2026-07-30 09:18:35"
---

> Source: https://open.dingtalk.com/document/connection/local-gateway-2
> Path: 连接平台 / 配置中心 / 本地网关 > 本地网关配置
> Updated: 2026-07-30 09:18:35

# 本地网关配置

## **背景信息**

为保障企业数据安全，部分应用部署在企业内网中，无法从公网直接访问。这些内网应用也无法通过连接平台直接访问，需借助本地网关实现访问。

本地网关采用轻量级反向代理机制，解决内外网服务互通问题。针对内网部署的应用，无需调整企业现有网络安全策略，即可通过本地网关在连接平台与企业内网之间建立安全通道，使连接平台能够访问对应服务的 HTTP 地址，实现跨网络环境的系统集成。

本地网关客户端是基于[钉钉开放平台 Stream](https://open-dingtalk.github.io/developerpedia/docs/learn/stream/overview/) 能力开发的开源软件，如需获取相关代码，请前往[Github代码仓库](https://github.com/open-dingtalk/ipaas-agent)。

## **前提条件**

- 本地网关仅面向钉钉专业版、专属版用户开放。
- 企业内本地网关的增删操作，仅企业主管理员或连接平台管理员可见。
- 目前本地网关处于公测阶段，如有问题可通过[AI 客服自助答疑或提交需求 / BUG](../../01-应用开发/07-TjCzIgfQs3-平台服务/0044-ngliko.md)获取支持。
- 已经申请了连接平台管理权限，添加路径如下：

  1. 登录[OA管理后台](https://oa.dingtalk.com/#/welcome)，单击侧边栏**安全与权限** > **权限管理。**
  2. 切换顶部为**子管理员**，单击增加子管理员 > 钉钉官方应用权限。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5134735871/p921627.png)

## **配置本地网关**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 单击**开放能力** > **连接平台** > **配置中心**，选择**本地网关。**
3. **在**本地网关页面**，**你可以选择在指定项目下，然后单击**添加本地网关。**

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5134735871/p745490.png)
4. 选择操作系统，设置网关名称，根据操作系统，选择自己的使用场景，最后单击**下一步**。

   > **[!NOTE]**
   >
   > 场景仅用于配置记录，目前一经设置不可更改。但并不代表网关仅可用于该场景，如果网关选择了 Windows 场景，其依然可以用于 Mac 系统和 Linux 系统。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5134735871/p745491.png)
5. 勾选服务条款后，单击**下一步**。

   > **[!IMPORTANT]**
   >
   > 请仔细并充分阅读服务条款，并同意钉钉相关许可及服务协议。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5134735871/p745492.png)
6. 下载Agent，下载安装包，并根据提示解压。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5134735871/p745493.png)

   - 文档更新可能滞后，获取最新的客户端请前往[Github发布页](https://github.com/open-dingtalk/ipaas-agent/releases/latest)。
   - 对于 Windows 系统：单击**下载安装程序**按钮，下载客户端程序 **ding-ipaas-agent**，双击即可运行。
   - 对于 Mac 系统：

     - 如果你使用浏览器：单击**下载安装程序**按钮，下载客户端程序 **ding-ipaas-agent，**双击即可运行
     - 如果你使用命令行，选择任意目录作为安装目录，例如 `~/ipaas-agent`，并进入该目录；如果安装目录不存在，请使用 `mkdir ~/ipaas-agent`创建，使用使用 curl 命令下载客户端程序：

       - Apple Silicon 版本：

         ```
         curl -L -o ding-ipaas-agent https://github.com/open-dingtalk/ipaas-agent/releases/download/v0.9.5/ipaas-agent-v0.9.5-darwin-arm64
         ```
       - Intel 处理器版本：

         ```
         curl -L -o ding-ipaas-agent https://github.com/open-dingtalk/ipaas-agent/releases/download/v0.9.5/ipaas-agent-v0.9.5-darwin-amd64
         ```
   - 对于 Linux 系统，选择任意目录作为安装目录，例如 `~/ipaas-agent`，并进入该目录；如果安装目录不存在，请使用 `mkdir ~/ipaas-agent`创建。

     - 使用使用 curl 命令下载客户端程序：

       ```
       curl -L -o ding-ipaas-agent https://github.com/open-dingtalk/ipaas-agent/releases/download/v0.9.5/ipaas-agent-v0.9.5-linux-amd64
       ```
     - 使用 wget 命令下载客户端程序：

       ```
       wget -O ding-ipaas-agent https://github.com/open-dingtalk/ipaas-agent/releases/download/v0.9.5/ipaas-agent-v0.9.5-linux-amd64
       ```
   - 获取更多版本，如果你希望获取最新的客户端版本（可能处于测试状态），或想寻找旧版本。亦或者你的使用场景不限于上述系统，获取最新的客户端请前往[Github发布页](https://github.com/open-dingtalk/ipaas-agent/releases/latest)。
7. 下载应用密钥，选择企业内部应用，根据应用会生成应用密钥。

   > **[!NOTE]**
   >
   > 1. 应用仅仅用于鉴权，你可以选择任意一个拥有权限的应用，可以在本地网关详情中下载对应的应用key，也可以直接登录[开发者后台](https://open-dev.dingtalk.com/fe/app#/corp/app)进行查询。
   > 2. 每个应用仅限绑定一个本地网关。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5134735871/p745494.png)

   配置文件的存放位置，为了确保ipaas-agent应用程序能够正确运行，请将config.yml配置文件放置在ipaas-agent可执行文件的同级目录下，例如，如果你将ipaas-agent下载到以下目录：

   - 在 **Windows** 系统上：`C:\path\to\ipaas-agent`
   - 在 **macOS** 和 **Linux** 系统上：`/path/to/ipaas-agent`

     那么，你应该将 config.yml 文件放置在该目录中，使其与 ipaas-agent 应用程序处于同一目录，如下所示：
   - 在 **Windows** 系统上：`C:\path\to\ipaas-agent\config.yml`
   - 在 **macOS** 和 **Linux** 系统上：`/path/to/ipaas-agent/config.yml`

     如果 config.yml 文件没有放置在正确的位置，ipaas-agent 可能无法启动或无法按预期工作。

     > **[!NOTE]**
     >
     > 如需查看配置文件更多详细内容，可查看[配置文件介绍](0006-local-gateway-configuration-1.md)。
8. 运行网关，根据不同的使用场景，运行本地网关。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5134735871/p745496.png)

   - Windows 系统，你可以通过两种方式运行 ipaas-agent：

     - 双击 ipaas-agent 应用程序的图标，这将以普通模式启动程序。
     - 通过命令行以后台模式运行，打开命令提示符或PowerShell，然后输入以下命令以使 ipaas-agent 在后台运行（假设 ipaas-agent 位于 C:\path\to\ipaas-agent ）：

       ```
       start /b C:\path\to\ipaas-agent\ipaas-agent.exe
       ```
   - macOS 和 Linux 系统，在 **macOS** 和 **Linux** 系统中，你同样有两种方式来运行 ipaas-agent：

     - 打开终端，切换到包含ipaas-agent的目录，然后执行以下命令直接运行：

       ```
       ./ipaas-agent
       ```
     - 要在后台持续运行`ipaas-agent`，同时屏蔽输出，可以使用`nohup`命令。在终端中执行以下命令：

       ```
       nohup ./ipaas-agent >/dev/null 2>&1 &
       ```

       这将启动`ipaas-agent`，所有的输出信息会被重定向到`/dev/null`，即不会显示任何输出信息。`&`符号表示`ipaas-agent`将在后台运行。

       > **[!NOTE]**
       >
       > 1. 确保`ipaas-agent`有执行权限。在Linux和macOS上，你可能需要通过`chmod +x ipaas-agent`命令来给予执行权限。
       > 2. 如果连接成功你将看见你的设备在活跃终端中显示在线。
       >
       >    ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5134735871/p747681.png)
       >
       >    ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5134735871/p747683.png)
9. 本地启动客户端后，应该看到如图所示的界面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5134735871/p880939.png)

   看到“成功连接到服务器”和“初始化成功”代表启动成功。

## **使用本地网关**

### **自建连接器**

自建连接器仅支持HTTP代理：

1. 假设有一个仅在内网可以访问的 HTTP GET 服务 ：`http://127.0.0.1:8000/test/Untitled-2.json`。
2. 新建连接器，在**连接器 > 鉴权设置**，启用**本地网关**。然后选择鉴权方式为`零信任网关`。

   ![零信任网关鉴权方式](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5134735871/p1090968.png)
3. 在**执行动作**中，新建自建HTTP执行动作，然后点击**下一步**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5134735871/p750337.png)
4. 接口路径中输入内网地址，并完成执行动作的调试，如何配置和调试可参考[添加执行动作](../02-XdgyZifJkr-我的连接/0012-add-execution-action-1.md)。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5134735871/p750339.png)

   鉴权调试成功后，会提示**调试成功**，**状态码200**的成功提示。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5134735871/p1090978.png)
5. 在**连接凭证**中，选择**是否使用本地网关**，如果使用，则可以选择已有本地网关。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5134735871/p750344.png)

### **本地MySQL连接器**

从市场中选择MySQL连接器使用。

MySQL连接器需要在 Agent 进行额外的配置，参见下方配置文件说明章节。
