---
title: "获取开发者权限"
source_url: "https://open.dingtalk.com/document/dingstart/get-developer-permissions"
namespace: "dingstart"
slug: "get-developer-permissions"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发指南 > 获取开发者权限"
doc_id: "svc3DQClP8"
updated_at: "2026-06-30 09:00:21"
---

> Source: https://open.dingtalk.com/document/dingstart/get-developer-permissions
> Path: 应用开发 / 开发指南 / 开发指南 > 获取开发者权限
> Updated: 2026-06-30 09:00:21

# 获取开发者权限

在钉钉开放平台中，获取开发者权限是进行应用开发、调试和发布的关键前提。本文档详细说明了管理员为成员配置开发者权限以及普通成员主动申请开发者权限的操作流程，帮助用户快速完成权限获取。

## **前提条件**

- 您已登录企业管理员账号或具备相应子管理员权限。
- 企业已完成组织架构搭建，需授权的成员已在组织内，详情参考[如何加入团队](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/yZvMRzlLwOAWr0nwgeGNJnjY02pBqGox)。
- 若涉及第三方服务商开发支持，需提前获取对方的 CorpId 或相关身份标识。

加入企业/团队，打开钉钉客户端，选择组织架构 > 创建或加入企业/团队，

在实际使用过程中，存在两种主要方式获取开发者权限：

- **由管理员代为添加**：适用于企业统一管理开发者角色、集中分配权限的场景。管理员可直接为指定成员配置开发者权限，无需用户发起申请。
- **由开发者主动申请**：适用于成员自行参与开发项目、临时需要调试权限的场景。成员可通过提交审批单的方式向管理员申请权限，经审批通过后自动生效。

以下将分别介绍两种模式的具体操作步骤。

## **管理员添加开发者权限**

1. 登录[钉钉管理后台](https://oa.dingtalk.com/#/welcome)。
2. 单击**安全与权限** > **权限管理** > **子管理员** > **添加子管理员。**

   ![添加子管理员权限.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1221872871/p723059.png)
3. 配置权限。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1221872871/p1084291.png)
4. 配置完成后，在添加子管理员页面，单击**保存。**

## **开发者主动申请开发者权限**

当用户没有开发者权限，登录[开发者后台](https://open-dev.dingtalk.com/)，需要进行应用开发时，会显示没有开发者权限，你需要提交子管理员的审批单，申请开发者权限，如下图所示：

![提交审批单申请.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6223096961/p724206.png)

## **后续步骤**

开发者权限添加完成后，你可以进行[应用创建与配置](0007-create-application.md)。
