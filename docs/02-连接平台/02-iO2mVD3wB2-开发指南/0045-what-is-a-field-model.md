---
title: "概述"
source_url: "https://open.dingtalk.com/document/connection/what-is-a-field-model"
namespace: "connection"
slug: "what-is-a-field-model"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发参考 > 高级功能 > 字段模型 > 概述"
doc_id: "73kLyIvdAO"
updated_at: "2025-09-23 19:20:31"
---

> Source: https://open.dingtalk.com/document/connection/what-is-a-field-model
> Path: 连接平台 / 开发指南 / 开发参考 > 高级功能 > 字段模型 > 概述
> Updated: 2025-09-23 19:20:31

# 概述

本文主要介绍了字段模型的基本概念以及如何使用相关的字段模型

## **什么是字段模型**

字段模型是赋予连接器接口字段一定的业务含义，提升连接器的交互体验，比如字段关联了钉钉用户 ID、应用 AgentId、下拉枚举选择等模型之后，在使用该连接器的时候这些字段的赋值操作除了常规的引用、表达式之外，还能弹出对应的选人组件、应用下拉列表等模型自定义的丰富交互组件。

## **为什么使用字段模型**

- 支持丰富的渲染组件，提升使用体验
- 降低连接器的使用门槛，通过下拉、搜索等操作完成相关字段的赋值
- 快速适配宜搭等其它场域连接器的使用

## 字段模型分类

### **钉钉用户ID**

该模型主要用于选择组织内的成员，并获取其 UserId/UnionId 赋值到关联的字段

1. 为字段关联「钉钉用户ID」的内容格式，并选择想要获取的 ID 类型。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7253883961/p715056.png)

2. 搜索并选择对应的用户即可完成字段的赋值。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7253883961/p715052.png)

### **下拉选项**

下拉选项主要用于支持枚举类型的字段

1. 为字段关联**下拉选项**的内容格式，并配置好选项列表。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7253883961/p715082.png)

2. 对应的字段赋值支持下拉直接选择

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7253883961/p715085.png)

### **日期组件**

日期组件支持丰富的日期格式选择，且可支持自定义格式

1. 为字段关联「日期组件」的内容格式，并配置好时间格式

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7253883961/p715088.png)

2. 对应字段的赋值操作可弹出日期选项框

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7253883961/p715090.png)

### **SQL组件**

SQL 组件可以支持 SQL 的快速录入，并支持选择上游参数变量

1. 为字段关联 「SQL 组件」的内容格式

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7253883961/p715099.png)

2. 对应字段支持录入 SQL，且可引用上游参数，注意需要自己手工加上引号，同时只有连接流的使用测才会出现上游参数，执行动作测试不支持上游参数

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7253883961/p715117.png)

### **组织内部群**

组织内部群可通过搜索/选择的方式获取对应的 OpenConversationId

1. 为字段关联「组织内部群」的内容格式

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7253883961/p715100.png)

2. 选择内部群即可给字段赋值对应的 OpenConversationId

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7253883961/p715103.png)

### **钉钉机器人**

钉钉机器人可获取应用关联的机器人 RobotCode

1. 为字段关联「钉钉机器人」的内容格式

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7253883961/p715105.png)

2. 通过选择应用的方式获取绑定机器人的 RobotCode，如果应用没有绑定机器人那么会给出红色的提示引导

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7253883961/p715106.png)

### **企业应用**

企业应用可获取企业内部应用的 agentId，注意仅支持 Number 类型的字段

1. 为字段关联「企业应用」的内容格式

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7253883961/p715107.png)

2. 通过搜索/选择的方式即可获取企业内部应用的 agentId 并赋值给关联的字段

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7253883961/p715108.png)

## **相关文档**

- [配置字段模型](0046-configure-the-field-model.md)
