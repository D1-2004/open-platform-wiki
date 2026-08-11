---
title: "AI 表格参数说明"
source_url: "https://open.dingtalk.com/document/connection/multidimensional-parameter-description"
namespace: "connection"
slug: "multidimensional-parameter-description"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > AI 表格 > AI 表格参数说明"
doc_id: "x0PWgAgeUk"
updated_at: "2026-06-15 17:01:29"
---

> Source: https://open.dingtalk.com/document/connection/multidimensional-parameter-description
> Path: 连接平台 / 连接器中心 / 官方连接器 > AI 表格 > AI 表格参数说明
> Updated: 2026-06-15 17:01:29

# AI 表格参数说明

## **数据结构**

### 多维表ID

多维表id唯一标识了一篇文档。可以通过 url 获取，也可以通过文档信息面板获取。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7102910371/p864137.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7102910371/p864142.png)

### **数据表ID**

数据表 id 唯一标识了一篇AI表格文档。可以通过 url 获取，也可以通过文档信息面板获取。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7102910371/p864135.png)

### **记录ID**

数据表中的每一行即是一个记录。一个数据表中通常有多个记录。

记录 id 仅保证在文档中唯一，不保证全局唯一。可以通过`新增多行记录``获取多行记录`获取。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7102910371/p864129.png)

## **字段格式配置**

| **类型** | **设置值（新增/更新记录时使用的格式）** |
| --- | --- |
| 文本 | ``` "TextString" // 字符串 ``` |
| 数字 | ``` 123 // 支持整数/浮点数/字符串 ``` |
| 单选 | ``` "optionName1" // 单选选项名 ``` |
| 多选 | ``` ["optionName1", "optionName2"] // 多选选项名 ``` |
| 日期 | ``` "2023-12-20 03:00" // ISO 8601字符串 ``` |
| 人员 | ``` [   {     "unionId": "xxxxxxxxx"  // 可以通过获取多行记录等接口获取   } ] ```  ``` [   {     "staffId": "xxxxxxxxx"   } ] ``` |
| 部门 | ``` [   {     "deptId": "xxx"   } ] ``` |
| 附件 | 暂不支持 |
| 单向关联 | ``` {   "linkedRecordIds": [     "xxx",     "yyy"   ] } ``` |
| 双向关联 | ``` {   "linkedRecordIds": [     "xxx",     "yyy"   ] } ``` |
| 链接 | ``` {   "text": "Dingtalk",   "link": "https://dingtalk.com" } ``` |

## **条件查询配置**

| **字段类型** | **可用操作符** | **value** |
| --- | --- | --- |
| 文本 | equal | notEqual | contain | notContain | empty | notEmpty | 示例：`["abc"]`  operator 是 empty/notEmpty 时不需要传 |
| 数字 | equal | notEqual | greater | greaterEqual | less | lessEqual | empty | notEmpty | 示例：`["123"]`  operator 是 empty/notEmpty 时不需要传 |
| 单选 | equal | notEqual | contain | notContain | empty | notEmpty | 示例: `["option1", "optionId2"]`  operator 是 contain 时，包含 value 中的任何一个选项即满足条件  operator 是 notContain 时，不包含 value 中的所有选项即满足条件  operator 是 empty/notEmpty 时不需要传 |
| 多选 | 同「单选」 | 同「单选」 |
| 日期 | equal | greater | less | empty | notEmpty | 示例: `["2024-09-27" | timestamp]`  operator 是 empty/notEmpty 时不需要传  operator 是 equal 时，可以传相对日期，如下所示   ``` {   type: 'today' | 'tomorrow' | 'yesterday' | 'thisWeek' | 'lastWeek' | 'thisMonth' | 'lastMonth' | 'next7Days' | 'last7Days' | 'next30Days' | 'last30Days'; } ```   当 operator 是 greater/less 时，可以传相对日期，如下所示   ``` {   type: 'today' | 'tomorrow' | 'yesterday' | 'thisWeek' | 'lastWeek' | 'thisMonth' | 'lastMonth' | 'next7Days' | 'last7Days' | 'next30Days' | 'last30Days'; } ```   日期的筛选只精确到「日」。例如，{ operator: 'equal', value: ['2024-09-27 10:00']} 这一条件会匹配 '2024-09-27 12:00' 这条记录。 |
| 人员 | equal | notEqual | contain | notContain | empty | notEmpty | 示例: `[{"uid": "xxx"}, {"uid": "yyy"}]`  operator 是 contain 时，包含 value 中的任何一个选项即满足条件  operator 是 notContain 时，不包含 value 中的所有选项即满足条件  operator 是 empty/notEmpty 时不需要传 |

## **执行动作**

## **创建/删除/获取数据表**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| 多维表id | String | 是 | 文档id(具体获取方式在上方文档中)。 |
| 数据表名 | String | 是 | 要创建/删除/获取的数据表名称(此处也可使用数据表id，具体获取方式在上方文档中)。 |

## **更新数据表**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| 多维表id | String | 是 | 多维表id(具体获取方式在上方文档中)。 |
| 原数据表名 | String | 是 | 要修改的原数据表名称。 |
| 新数据表名 | String | 是 | 要修改的新数据表名称。 |

## **获取所有数据表**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| 多维表id | String | 是 | 多维表id(具体获取方式在上方文档中)。 |

## **获取数据表多行记录**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| 多维表id | String | 是 | 多维表id(具体获取方式在上方文档中)。 |
| 数据表名 | String | 是 | 要获取记录的数据表名称(此处也可使用数据表id，具体获取方式在上方文档中)。 |
| 每次获取记录数 | Number | 否 | 表中记录每次拉取展示的数量，不填默认 20 行。 |
| 查询条件 | Object | 否 | 通过不同字段操作符，实现对记录的条件查询(具体条件查询配置在上方文档中)。 |
| 分页游标 | String | 否 | 数据拉取的起始位置。首次调用时不传，后续调用时，若表中还有更多行记录，返回结果中会带有nextToken参数，下次请求时需带上此参数。 |

### **条件查询示例**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7102910371/p864220.png)

### **出参示例**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7102910371/p864160.png)

## **获取数据表单行记录**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| 多维表id | String | 是 | 多维表id(具体获取方式在上方文档中)。 |
| 数据表名 | String | 是 | 要获取记录的数据表名称(此处也可使用数据表id，具体获取方式在上方文档中)。 |
| 记录id | String | 是 | 记录id(具体获取方式在上方文档中)。 |

## **新增数据表多行记录**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| 多维表id | String | 是 | 多维表id(具体获取方式在上方文档中)。 |
| 数据表名 | String | 是 | 要新增记录的数据表名称(此处也可使用数据表id，具体获取方式在上方文档中)。 |
| 新增的记录 | Array | 是 | 新增的记录参考上文不同字段格式配置，具体格式如下图所示（注意在 FaaS 脚本中必须添加 fields 字段）。 |

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2484013371/p880445.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2484013371/p880442.png)

## **更新数据表多行记录**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| 多维表id | String | 是 | 多维表id(具体获取方式在上方文档中)。 |
| 数据表名 | String | 是 | 要更新记录的数据表名称(此处也可使用数据表id，具体获取方式在上方文档中)。 |
| 更新的记录 | Array | 是 | 更新的记录参考上文不同字段格式配置，具体格式如下图所示（注意在 FaaS 脚本中必须添加 id、fields 字段）。 |

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2484013371/p880447.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2484013371/p880446.png)

## **删除数据表多行记录**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| 多维表id | String | 是 | 多维表id(具体获取方式在上方文档中)。 |
| 数据表名 | String | 是 | 要删除记录的数据表名称(此处也可使用数据表id，具体获取方式在上方文档中)。 |
| 删除记录id | Array | 是 | 要删除的记录id的列表(具体获取方式在上方文档中)。 |
