---
title: "概述"
source_url: "https://open.dingtalk.com/document/connection/table-overview"
namespace: "connection"
slug: "table-overview"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 表格 > 概述"
doc_id: "i30UytGa3q"
updated_at: "2025-09-23 19:20:46"
---

> Source: https://open.dingtalk.com/document/connection/table-overview
> Path: 连接平台 / 连接器中心 / 官方连接器 > 表格 > 概述
> Updated: 2025-09-23 19:20:46

# 概述

钉钉表格是阿里巴巴集团钉钉研发的企业协同办公套件的一部分。在日常使用中，无需下载文档即可通过电脑、手机或平板直接编辑和查看文档内容，文档内容实时自动保存。在钉钉中打开表格或Excel文件时，依据企业设置和文件内容，可能使用不同的应用打开表格。

## 参数说明

### 目录项ID

目录项 id 唯一标识了一篇表格文档。可以在 url 中截取。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9308762371/p878199.png)

### **工作表名称**

每个目录项中的工作表名称是唯一的。可以在文档底部栏获取，也可以对工作表名称进行编辑修改。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9308762371/p878200.png)

### **单元格区域**

工作表中单元格区域格式为`区域内左上角单元格:区域内右下角单元格`

例如： B2:C3 表示区域如下图所示。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9308762371/p878201.png)

## 执行动作

### 工作表

| **连接器名称** | **执行动作** | **描述** |
| --- | --- | --- |
| 表格 | [创建工作表](../../01-应用开发/02-4a8AMF6u2A-服务端API/0589-create-a-worksheet.md) | 创建指定名称工作表。 |
| [删除工作表](../../01-应用开发/02-4a8AMF6u2A-服务端API/0591-delete-classic-workbooks.md) | 删除指定名称工作表。 |
| [获取工作表](../../01-应用开发/02-4a8AMF6u2A-服务端API/0592-obtain-worksheet-properties.md) | 获取指定名称工作表。 |
| [获取所有工作表](../../01-应用开发/02-4a8AMF6u2A-服务端API/0593-obtain-all-worksheets.md) | 获取目录下所有工作表。 |

### **行列**

| **连接器名称** | **执行动作** | **描述** |
| --- | --- | --- |
| 表格 | [指定行上方插入若干行](../../01-应用开发/02-4a8AMF6u2A-服务端API/0602-insert-rows-before-rows.md) | 在工作表指定行下方插入若干行。 |
| [指定列左侧插入若干列](../../01-应用开发/02-4a8AMF6u2A-服务端API/0603-insert-column-before-column.md) | 在工作表指定列右侧插入若干列。 |
| [删除行](../../01-应用开发/02-4a8AMF6u2A-服务端API/0594-delete-row.md) | 在工作表指定行下方删除若干行。 |
| [删除列](../../01-应用开发/02-4a8AMF6u2A-服务端API/0595-delete-column.md) | 在工作表指定列右侧删除若干列。 |
| [设置行隐藏或显示](../../01-应用开发/02-4a8AMF6u2A-服务端API/0600-set-row-visibility.md) | 设置行的可见性。 |
| [设置列隐藏或显示](../../01-应用开发/02-4a8AMF6u2A-服务端API/0601-set-column-visibility.md) | 设置列的可见性。 |

### **区域**

| **连接器名称** | **执行动作** | **描述** |
| --- | --- | --- |
| 表格 | [获取单元格区域](../../01-应用开发/02-4a8AMF6u2A-服务端API/0607-get-cell-properties.md) | 获取单元格指定区域内的数据。 |
| [更新单元格区域](../../01-应用开发/02-4a8AMF6u2A-服务端API/0608-update-cell-properties.md) | 更新单元格指定区域内的数据。 |
| [清除单元格区域内数据](../../01-应用开发/02-4a8AMF6u2A-服务端API/0611-clear-cell-data.md) | 清除单元格指定区域内的数据。 |
| [清除单元格区域内所有内容](../../01-应用开发/02-4a8AMF6u2A-服务端API/0612-clear-all.md) | 清除单元格指定区域内的数据和格式。 |
