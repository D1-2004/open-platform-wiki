---
title: "最佳实践：智能财务企业经营台账分析"
source_url: "https://open.dingtalk.com/document/aipass/best-practice-smart-finance-business-account-analysis"
namespace: "aipass"
slug: "best-practice-smart-finance-business-account-analysis"
group: "数据资产"
tab: "宜数（智能问数）"
breadcrumb: "数据工厂 > 最佳实践：智能财务企业经营台账分析"
doc_id: "OOUiTxd3An"
updated_at: "2025-09-23 19:20:55"
---

> Source: https://open.dingtalk.com/document/aipass/best-practice-smart-finance-business-account-analysis
> Path: 数据资产 / 宜数（智能问数） / 数据工厂 > 最佳实践：智能财务企业经营台账分析
> Updated: 2025-09-23 19:20:55

# 最佳实践：智能财务企业经营台账分析

## **功能使用效果**

财务业务里的有许多定制字段，可以借助数据工厂的数据集加工能力，基于明细表，关联维表及新增衍生字段加工出来，无需依赖在底层表进行开发，提高数据的利用效率。

如客户A的需求：按创建年份、负责人统计金额，最终效果图如下：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5870954371/p890674.png)

## **功能搭建流程**

## **加工数据集**

### **一、数据集导入**

1. 单击新建数据集。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4870954371/p890675.png)
2. 选择合适的数据集来源。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5870954371/p890676.png)
3. 上传表格。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4870954371/p890677.png)
4. 配置表格。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4870954371/p890678.png)
5. 数据预览。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4870954371/p890679.png)

### **二、实现多表关联**

1. 单击新建数据集。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4870954371/p890681.png)
2. 选择数据准备。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4870954371/p890682.png)
3. 实现多表关联。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4870954371/p890683.png)

### **三、加工衍生字段**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4870954371/p890686.png)

### **四、结果预览**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4870954371/p890687.png)

## **配置仪表盘**

### **一、配置明细数据**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5870954371/p890689.png)

### **二、配置过滤项**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4870954371/p890691.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4870954371/p890692.png)
