---
title: "角色授权"
source_url: "https://open.dingtalk.com/document/aipass/share-dingtalk-ai-assistant"
namespace: "aipass"
slug: "share-dingtalk-ai-assistant"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "安全与权限 > 角色授权"
doc_id: "63yp949EQP"
updated_at: "2026-07-08 15:48:56"
---

> Source: https://open.dingtalk.com/document/aipass/share-dingtalk-ai-assistant
> Path: AI PaaS / DEAP·企业AI平台 / 安全与权限 > 角色授权
> Updated: 2026-07-08 15:48:56

# 角色授权

## **概述**

企业在使用Deap时，若由各部门自行创建和使用智能体（Agent），会带来以下问题：

- 缺乏统一的管理与安全审计
- 智能体随意建设，资源浪费
- 权限混乱，部分业务数据存在泄露风险

因此需要给Deap使用者赋予不同的权限，以保障智能体的统一管理和数据安全。

## **用户角色**

目前 DEAP 提供了 4 种角色：**超管（Enterprise Admin）**、**部门管理者（Department Admin）**、**模型开发者（AI Builder）**、**智能体开发者（Model Trainer）**。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6396943871/p1085680.png)

### **超管**

- **定义：**具备DEAP全局权限，可设置用户角色与权限。
- **核心权限点：**企业内

  - 不同权限角色的授权
  - DEAP运营数据
  - 日志审计
- **核心诉求：**统一管理企业AI资产与安全策略。

### **部门管理员**

- **定义：**具备管理部门内智能体权限的用户。
- **核心权限点：**本部门内

  - 授权智能体开发者
  - DEAP运营数据
  - 审批发布
  - 创建/编辑/评测/发布智能体
  - 创建/编辑知识集
- **核心诉求：**确保部门级AI应用落地与合规。

### 智能体开发者

- **定义：**具备智能体创建权限的用户。
- **核心权限点：**

  - 创建/编辑/评测智能体
  - 创建/编辑知识集
  - 提交发布申请
- **核心诉求：**快速构建AI智能体。

### **部门管理员**

- **定义：**具备训练专属模型权限的用户。
- **核心权限点：**

  - 训练专属模型
  - 创建/编辑训练集
  - 提交发布申请
- **核心诉求：**高效训练模型。
