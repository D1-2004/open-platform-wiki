---
title: "基础控件"
source_url: "https://open.dingtalk.com/document/connection/basic-controls"
namespace: "connection"
slug: "basic-controls"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > OA审批 > 控件库 > 基础控件"
doc_id: "7zFmVwCdqA"
updated_at: "2025-09-23 19:21:08"
---

> Source: https://open.dingtalk.com/document/connection/basic-controls
> Path: 连接平台 / 连接器中心 / 官方连接器 > OA审批 > 控件库 > 基础控件
> Updated: 2025-09-23 19:21:08

# 基础控件

本文介绍了OA审批常用的基础控件。

## **单行输入框**

填写以下控件的值获取数据，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p561993.png)

获取的数据填充到以下控件，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p561996.png)

## **多行输入框**

填写以下控件的值获取数据，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p561999.png)

获取的数据填充到以下控件，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562000.png)

## **数字输入框**

填写以下控件的值获取数据，数据格式为：number类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562010.png)

获取的数据填充到以下控件，数据格式为：number类型或只包含数字的String类型，如（123或“123”）。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562015.png)

## **单选框**

> **[!IMPORTANT]**
>
> 选项最多200项，每项最多50个字。

### **连接平台**

单选框作为输入到连接器时，填写以下控件的值获取数据中入参设置，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562072.png)

单选框作为连接器输出时，获取的数据填充到以下控件时出参设置，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562075.png)

### **OA审批管理后台**

填写以下控件的值获取数据：

- 「单选框.值」数据格式为：String类型。
- 「单选框.选项列表.值列表」数据格式为：array类型。
- 「单选框.选项列表.ID列表」数据格式为：array类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562029.png)

> **[!NOTE]**
>
> - 「单选框.值」为展示值。
> - 「单选框.选项列表.值列表」为下拉框选项列表。
> - 「单选框.选项列表.ID列表」为对应选项的ID列表。
>
> 根据实际需求选择所需值获取，并不是所有值必填。

获取的数据填充到以下控件：

- 「单选框.值」数据格式为：String类型。
- 「单选框.选项列表.值列表」数据格式为：array类型。
- 「单选框.选项列表.ID列表」数据格式为：array类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562056.png)

> **[!NOTE]**
>
> 根据实际需求选择所需值填充，并不是所有值必填。

## **多选框**

> **[!IMPORTANT]**
>
> 选项最多200项，每项最多50个字。

### **连接平台**

多选框内容作为输入到连接器时，填写以下控件的值获取数据中入参设置，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562107.png)

多选框内容作为连接器输出时，获取的数据填充到以下控件中出参设置，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562117.png)

### **OA审批管理后台**

填写以下控件的值获取数据：

- 「多选框.值」数据格式为：Array<String>类型。
- 「多选框.选项列表.值列表」数据格式为：array类型。
- 「多选框.选项列表.ID列表」数据格式为：array类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562095.png)

> **[!NOTE]**
>
> - 「多选框.值」为展示值。
> - 「多选框.选项列表.值列表」为下拉框选项列表。
> - 「多选框.选项列表.ID列表」为对应选项的ID列表。
>
> 根据实际需求选择所需值获取，并不是所有值必填。

获取的数据填充到以下控件：

- 「多选框.值」数据格式为：Array<String>类型。
- 「多选框.选项列表.值列表」数据格式为：array类型。
- 「多选框.选项列表.ID列表」数据格式为：array类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562105.png)

> **[!NOTE]**
>
> 根据实际需求选择所需值填充，并不是所有值必填。

## **日期**

填写以下控件的值获取数据，数据格式为：String类型。

> **[!NOTE]**
>
> - 如果日期控件类型选择为：「年-月-日」则参数数据格式为「2023-02-02」。
> - 如果日期控件类型选择为「年-月-日 时：分」则参数为「2023-02-02 11:11」。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562142.png)

获取的数据填充到以下控件，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562153.png)

## **日期区间**

### **连接平台**

日期区间作为输入到连接器时，填写以下控件的值获取数据中入参设置，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562190.png)

日期区间作为连接器输出时，获取的数据填充到以下控件中出参设置，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562191.png)

### **OA审批管理后台**

填写以下控件的值获取数据，数据格式为：Array<String, String>或Array<String, String, number>类型。

> **[!NOTE]**
>
> - 如果日期区间控件类型设置为「年-月-日」，则参数数据格式为「2023-02-02」。
> - 如果日期控件类型选择为「年-月-日 时：分」，则参数为「2023-02-02 11:11」。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562172.png)

获取的数据填充到以下控件，数据格式为：Array<String, String>或Array<String, String, number>类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1467256761/p562639.png)

## **身份证**

填写以下控件的值获取数据，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562267.png)

获取的数据填充到以下控件，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562272.png)

## **电话**

填写以下控件的值获取数据，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562275.png)

获取的数据填充到以下控件，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562277.png)
