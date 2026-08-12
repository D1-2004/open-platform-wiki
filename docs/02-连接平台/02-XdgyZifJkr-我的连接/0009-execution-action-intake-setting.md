---
title: "执行动作入参设置"
source_url: "https://open.dingtalk.com/document/connection/execution-action-intake-setting"
namespace: "connection"
slug: "execution-action-intake-setting"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发连接流 > 参考 > 执行动作入参设置"
doc_id: "MQw7A9SPR7"
updated_at: "2026-07-24 09:20:38"
---

> Source: https://open.dingtalk.com/document/connection/execution-action-intake-setting
> Path: 连接平台 / 我的连接 / 开发连接流 > 参考 > 执行动作入参设置
> Updated: 2026-07-24 09:20:38

# 执行动作入参设置

本文档主要介绍连接流执行动作节点中，如何进行入参映射设置。

## **功能介绍**

入参映射功能，提供对本节点执行动作设置入参操作。可通过拖拽入参、固定值、表达式、模板变量4种方式进行入参设置。

## **使用说明**

1. 选择目标执行动作后，在**出入参配置**面板进行参数配置。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8306584871/p715114.png)
2. 在**出入参配置**面板上，把**上文节点出参**与**本节点入参**进行映射配置。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8306584871/p715118.png)

   入参设置可分为如下4种方式：

   - **引用值：**在左上角上文参数面板中选择需要映射的值。
   - **输入值：**输入文本后，可以单击⊕选择引用上文节点参数。
   - **表达式：**单击输入框进行表达式映射，函数如何使用，详情请参考[表达式](0008-expression-overview.md)。
3. **多种类型（只会对array和object类型生效）：**

   - array选择多种类型后，可分别对数组每一个元素进行赋值。
   - object选择多种类型后，可分别对object每一个元素进行赋值。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8306584871/p1089471.png)
4. **空值（只会对array生效）**

   空值表示为数组值为null，例：[ null ] , [[ null ]]。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8306584871/p715130.png)
