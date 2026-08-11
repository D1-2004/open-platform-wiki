---
title: "图片自动比对校验判断--包装批次码与出库编码智能比对"
source_url: "https://open.dingtalk.com/document/connection/automatic-verification-comparison"
namespace: "connection"
slug: "automatic-verification-comparison"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "多维表自动化 > 图片自动比对校验判断--包装批次码与出库编码智能比对"
doc_id: "V8acjP8c3L"
updated_at: "2025-09-23 19:21:46"
---

> Source: https://open.dingtalk.com/document/connection/automatic-verification-comparison
> Path: 连接平台 / 连接平台自动化 / 多维表自动化 > 图片自动比对校验判断--包装批次码与出库编码智能比对
> Updated: 2025-09-23 19:21:46

# 图片自动比对校验判断--包装批次码与出库编码智能比对

本文档介绍AI表格自动化模板的最佳实践步骤。

## **简介**

本文档以**包装批次码与出库编码智能比对**场景为例，利用AI能力大幅度提升比对效率

## **预期效果**

**提交指令单和产品照片**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2678994571/p996369.png)

**对比信息推送**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2678994571/p996372.png)

**对比信息沉淀表**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2678994571/p996389.png)

## **准备工作**

- 创建一个钉钉 AI 表格，并设置该表格的字段，表格字段名称和类型示例如下。

  表格字段可以按照实际情况设置，本文档内容仅为示例

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2678994571/p996417.png)
- 创建的AI表格，创建表单视图，用于员工上传行令单和产品图片，进行提交。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2678994571/p996422.png)

## **操作步骤**

1. 启动创建的AI表格中，预设的自动化模板。

   ![iShot_2025-08-12_17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2678994571/p996429.gif)
2. 配置自动化模板节点

   | 节点 | 配置 | 截图 |
   | --- | --- | --- |
   | 创建记录时 | 选择记录所在的数据表：  选择刚创建的AI表格 | image |
   | 指令图片识别 | 图片链接：  配置变量为指令单照片的临时链接 | image |
   | 问题：  这里填写需要从指令单照片中提取的内容，类似于大模型的prompt，需要根据实际情况进行改写 | image |
   | 指令单信息提取后写入AI表格 | 配置需要写入到AI表格的字段信息 | image |
   | 产品照片识别 | 图片链接：  配置变量为产品照片的临时链接 | image |
   | 问题：  这里填写需要从产品照片中提取的内容，类似于大模型的prompt，需要根据实际情况进行改写 | image |
   | 产品信息提取后写入AI表格 | 配置需要写入到AI表格的字段信息 | image |
   | 向AI提问 | 使用大模型能力，比对两张照片提取的内容，进行对比 | image |
   | 更新记录 | 把内容对比的结果，写入到AI表格 | image |
   | 发送钉钉消息 | 构造发送对比结果的消息内容 | image |
3. 点击保存和发布

## **恭喜，你已完成全部配置！**

你已完成本教程的全部内容，可以开始测试。

将此AI表格的表单分享链接，发送给员工。员工点击表单提交链接，输入行令单照片和产品照片，即可收到对比结果，并且对比记录自动沉淀到AI表格中。

提交的记录信息，也可以借助AI表格强大的数据分析能力，生成各种数据看板。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2678994571/p996458.png)
