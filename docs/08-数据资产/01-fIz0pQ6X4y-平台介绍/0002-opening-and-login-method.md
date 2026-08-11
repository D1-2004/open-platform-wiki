---
title: "开通及登录方式"
source_url: "https://open.dingtalk.com/document/dataopen/opening-and-login-method"
namespace: "dataopen"
slug: "opening-and-login-method"
group: "数据资产"
tab: "平台介绍"
breadcrumb: "开通及登录方式"
doc_id: "ullolD7V3B"
updated_at: "2025-09-23 19:20:34"
---

> Source: https://open.dingtalk.com/document/dataopen/opening-and-login-method
> Path: 数据资产 / 平台介绍 / 开通及登录方式
> Updated: 2025-09-23 19:20:34

# 开通及登录方式

本文档介绍钉钉数据资产平台的开通方式。

## 登录数据资产平台

在完成开发者权限开通之后，由企业主管理员登录[钉钉开发者后台](https://open-dev.dingtalk.com)，开发能力内选择**数据资产平台**即可。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9603171861/p619130.png)

## **权限审批管理**

数据资产平台作为企业统一管理自身数据资产的平台，引入了企业数据管理体系的3类角色，角色与权限如下：

| **角色名称** | **权限说明** |
| --- | --- |
| 普通权限 | 数据的使用人角色，拥有数据资产平台各项功能的使用权限，如创建数据服务接口、生成数据图表等，一般授予开发、运营等职能 |
| 数据审批人 | 数据的审批人角色，拥有对普通权限用户创建接口或图表后的业务审批权限，对数据的业务使用具有决定权，一般授予业务负责人 |
| 数据安全接口人 | 企业的数据安全把关人，针对业务审批后的数据服务从数据安全角度做最后的把关，一般授予专职的数据安全负责人 |

> **[!NOTE]**
>
> 在数据资产平台打包数据服务之前，首先需要添加好本组织的数据审批人、数据安全接口人，只有有完整的接口人角色，才能完成数据服务的流程审批。

#### **1、新增权限**

点击新增后，选择好对应的角色即可为用户赋权。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9603171861/p619108.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9603171861/p619105.png)

#### **2、删除权限**

需要删除权限时，在权限审批管理页面针对相应的记录选择删除即可。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8603171861/p619104.png)

## 基础概念

| **概念** | **说明** |
| --- | --- |
| 企业身份 | 以企业组织身份登录数据资产平台。 |
| ISV身份 | 以ISV生态伙伴组织的身份登录数据资产平台，只有入驻为钉钉应用服务商的企业才有该入口。 |
| 服务ID | 创建数据服务后生成的服务ID，可使用该ID调用接口。 |
| 服务名称 | 创建数据服务时填写的名称。 |
| 应用类型 | 创建数据服务时选择的应用类型，包括打包数据API接口、生成数据图表、授权数据到钉钉生态应用使用、数据批量同步服务。 |
