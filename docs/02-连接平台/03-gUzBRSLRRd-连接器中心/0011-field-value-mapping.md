---
title: "字段值映射"
source_url: "https://open.dingtalk.com/document/connection/field-value-mapping"
namespace: "connection"
slug: "field-value-mapping"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "内置工具 > 字段值映射 > 字段值映射"
doc_id: "vWSz0as0Nw"
updated_at: "2025-09-23 19:20:39"
---

> Source: https://open.dingtalk.com/document/connection/field-value-mapping
> Path: 连接平台 / 连接器中心 / 内置工具 > 字段值映射 > 字段值映射
> Updated: 2025-09-23 19:20:39

# 字段值映射

## **简介**

在流程设计过程中，你可能需要将流程中的字段值转换成特定格式的数据。举个例子，当A系统与B系统进行数据集成，A系统中的城市字段为“杭州”，而B系统中则使用“杭州市”。为了实现数据集成，您需要将“A系统”的城市名称映射转换为“B系统”的对应格式，即“杭州”映射为“杭州市”。字段值映射功能正是用于支持此类转换，它使得流程中的字段适配变得简单快捷。

## **功能说明**

**字段值映射**具有一个执行动作**通过查询映射表配置映射规则**。该执行动作在进行映射时，需要预先配置映射表，映射表均为Map键值对格式。具体格式如下：

```
{
  "香蕉": "Apple",
  "苹果": "Banana",
  "梨子": "Pear"
}
```

映射表有3种来源：

- 录入映射表：自行在执行动作配置时录入即可。
- 引用变量：引用上文节点返回的键值对类型变量。
- 数据映射表：该数据源需要配合连接项目使用。可在配置中心 > 连接项目 > 数据存储中，配置当前项目所属的键值对映射数据。

## **相关文档**

- [使用字段值映射对字段进行转换](https://open.dingtalk.com/document/dingstart/transforming-value-mappings)
