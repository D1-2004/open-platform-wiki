---
title: "管理组织内创建的 AI 助理"
source_url: "https://open.dingtalk.com/document/aipass/management-dingtalk-ai-assistant-1"
namespace: "aipass"
slug: "management-dingtalk-ai-assistant-1"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "管理 AI 助理 > 管理组织内创建的 AI 助理"
doc_id: "Eex1uuBi5z"
updated_at: "2025-09-23 19:19:09"
---

> Source: https://open.dingtalk.com/document/aipass/management-dingtalk-ai-assistant-1
> Path: AI PaaS / AI 助理创建平台 / 管理 AI 助理 > 管理组织内创建的 AI 助理
> Updated: 2025-09-23 19:19:09

# 管理组织内创建的 AI 助理

如果你需要对钉钉 AI 助理进行管理（包括在 AI 助理容器中管理和钉钉管理后台中管理），可以参考本文档内容。

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理**

## **AI 助理容器中管理 AI 助理**

### **编辑管理**

> **组织 AI 助理包括仅你自己使用的 AI 助理和组织成员使用的 AI 助理，详情参考**[创建组织内使用的 AI 助理](0005-create-a-dingtalk-ai-assistant-1.md)。

如果你需要编辑组织 AI 助理，需要在钉钉客户端中的 AI 助理容器中进行操作，具体步骤如下：

1. 登录钉钉客户端，单击右上角**“/”** > **AI 助理 ⇋**，选择目标 AI 助理。
2. 单击右上角 **“···”** > **助理详情**，进入 AI 助理详情页面，单击**编辑**，即可进行编辑操作。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4903148071/p768081.png)

### **权限管理**

如果你需要和其他成员共同编辑或转让 AI 助理，你可以：

1. AI 助理创建者，进入 AI 助理创建页面，详情参考[创建组织内使用的 AI 助理](0005-create-a-dingtalk-ai-assistant-1.md)。
2. 单击**权限**，进入助理管理权限页面。
3. 单击共同管理员输入框/转让，选择你需要协同/转让的成员，确认即可。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8095543271/p833971.png)

> **[!NOTE]**
>
> - AI 助理拥有者可转让 AI 助理，被转让用户会接收到消息提醒。
> - 共同管理员最多可添加20人，且支持编辑和发布操作，但不支持删除。
> - 企业主管理员和拥有**开发者权限** > **全局应用管理权限**的成员拥有组织内 AI 助理的最高权限，可对组织 AI 助理进行编辑和转让。
>
>   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3246526171/p802139.png)

### **数据管理**

如果你需要查看 AI 助理的使用情况和资源消耗量，你可以：

1. 进入 AI 助理创建页面，详情参考[创建组织内使用的 AI 助理](0005-create-a-dingtalk-ai-assistant-1.md)。
2. 单击**分析**，进入数据概览页面，你可以在该页面查看相关数据信息，包括活跃用户量、用户对话量、数据详情（对话明细和助理所在群）信息。

   > **[!NOTE]**
   >
   > - 对话明细数据为实时数据信息。
   > - 对话明细数据支持导出。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8369825371/p894038.png)

## 钉钉管理后台管理 AI 助理

### **配置 AI 助理管理权限**

如果你是企业管理员，你可以对已发布的 AI 助理进行管理

1. 登录[钉钉管理后台](https://oa.dingtalk.com/#/welcome)，单击**AI 助理** > **AI 助理管理**，选择对应 AI 助理。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8369825371/p894088.png)
2. 单击**设置**，即可设置 AI 助理的编辑权限、转让助理拥有者、共同管理员和 AI 助理的可使用范围。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8369825371/p894089.png)

### **配置 AI 助理功能管理权限**

如果你是企业管理员，你可以对组织 AI 助理的功能进行管理。

1. 登录[钉钉管理后台](https://oa.dingtalk.com/#/welcome)，单击**AI 助理** > **AI 助理功能管理**，进入 AI 助理功能管理页面。
2. 配置 AI 助理高级管理设置：

   | **配置项** | | | **说明** | **权益** |
   | --- | --- | --- | --- | --- |
   | 使用管理 | AI 助理创建入口 | 入口可见性 | 用于控制钉钉APP右上角的功能开关。  image | 生产力平台免费版 |
   | 入口图标自定义 | 支持将 AI 助理的入口图标替换为自定义图标。 | 生产力平台定制版 |
   | 自定义企业默认AI助理 | | 支持替换默认企业 AI 助理。 | 生产力平台定制版 |
   | 创建管理 | AI 助理创建权限 | AI 助理创建权限 | 支持设置企业成员创建 AI 助理的权限 | 生产力平台免费版 |
   |  | AI 助理发布审批设置 | 支持设置发布时的审批人  **[!NOTE]**  企业主管理员和拥有**开发者权限** > **全局应用管理权限**的成员，均可成为 AI 助理的审核成员。  image | 生产力平台免费版 |
   | 组织外发布渠道设置 | | 支持设置 AI 助理组织外发布渠道。 | 生产力平台高级版 |
   | 安装管理 | 助理市场安装设置 | | 助理市场安装管控：支持自定义助理市场的跳转链接。 | 生产力平台定制版 |

## **钉钉管理后台查看 AI 助理消耗额度**

如果你是企业管理员并且需要查看 AI 助理的额度消耗情况，需要在钉钉管理后台中进行操作，具体步骤如下：

1. 登录[钉钉管理后台](https://oa.dingtalk.com/#/welcome)，单击 **AI 助理** > **AI 算粒管理**，进入 AI 助理容量管理页面。
2. 你可以在AI 助理容量管理页面，查看算粒余额，已用算粒、算粒使用人数、算粒用量排行以及算粒使用日志信息。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8369825371/p894057.png)
