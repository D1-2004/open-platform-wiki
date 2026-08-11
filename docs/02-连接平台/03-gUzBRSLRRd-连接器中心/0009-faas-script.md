---
title: "FaaS 脚本"
source_url: "https://open.dingtalk.com/document/connection/faas-script"
namespace: "connection"
slug: "faas-script"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "内置工具 > FaaS 脚本 > FaaS 脚本"
doc_id: "2X1qAX1QMm"
updated_at: "2026-01-22 20:46:45"
---

> Source: https://open.dingtalk.com/document/connection/faas-script
> Path: 连接平台 / 连接器中心 / 内置工具 > FaaS 脚本 > FaaS 脚本
> Updated: 2026-01-22 20:46:45

# FaaS 脚本

## **简介**

当需要处理前置节点生成的复杂数据时，可通过FaaS脚本实现自定义业务逻辑并输出结果。

该功能适用于在流程中嵌入灵活的数据处理能力，支持JavaScript和Python语言，满足多样化的业务场景需求。

## **能力说明**

FaaS（Function as a Service）脚本是钉钉流程自动化中的高级能力，允许开发者在流程节点中运行自定义代码，完成数据转换、条件判断、聚合计算等复杂逻辑处理。

脚本执行上下文包含以下关键元素：

- `event`：接收来自前置节点的输入数据，格式为JSON对象。
- `callback`：用于返回处理结果，必须调用以传递数据至下一节点。
- 支持异步操作（需在超时时间内完成）。

目前提供两种运行环境供选择：

- **Node.js**：基于V8引擎，支持ES6+语法，适合轻量级数据处理。
- **Python**：支持标准Python 3语法，便于进行数学运算或调用内置库。

> 注意：脚本仅支持同步返回结果，不支持长期后台任务或外部网络请求。

## 使用指引

### 执行限制

| **项目** | **限制** |
| --- | --- |
| 超时时间 | 5秒（超过将被强制终止） |
| 内存限制 | 128MB |
| 代码大小 | 不超过5KB |
| 支持语法 | JavaScript（Node.js）、Python 3基础语法 |
| 禁止行为 | 网络请求、文件系统访问、进程调用 |

### 权限角色要求

- 必须具备“应用开发管理员”权限才能配置和保存脚本。
- 普通成员仅可触发流程执行，无法查看或修改脚本内容。

### 上下文变量说明

- `event`：传入的输入参数，来源于前一个节点的输出数据。

  - `error`：错误信息，无错误时设为`null`。
  - `result`：输出数据，将作为下一个节点的输入。

## **相关文档**

- [使用FaaS脚本处理企业部门信息](https://open.dingtalk.com/document/dingstart/enterprise-department-information)
