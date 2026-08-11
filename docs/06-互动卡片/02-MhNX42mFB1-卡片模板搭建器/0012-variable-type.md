---
title: "变量类型"
source_url: "https://open.dingtalk.com/document/development/variable-type"
namespace: "development"
slug: "variable-type"
group: "互动卡片"
tab: "卡片模板搭建器"
breadcrumb: "绑定卡片变量 > 变量类型"
doc_id: "0b70J0DXRY"
updated_at: "2025-09-23 19:18:31"
---

> Source: https://open.dingtalk.com/document/development/variable-type
> Path: 互动卡片 / 卡片模板搭建器 / 绑定卡片变量 > 变量类型
> Updated: 2025-09-23 19:18:31

# 变量类型

通过本文你将会了解到卡片变量的所有类型以及它们的适用场景。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p550138.png)

卡片的变量共有三种类型，分别是：普通变量、表达式变量以及本地变量，以下将分别进行详细的介绍。

## **一、普通变量**

普通变量是较为常用的变量类型，与开发者在发送卡片时所配置的 cardData 里的字段一一对应。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p532278.png)

如图，普通变量的变量配置如下：

- **变量名**：唯一的变量名称
- **变量类型**：普通变量的变量类型，如数字、字符串、布尔值等等
- **变量描述**：该变量的描述，非必填
- **是否为私有变量**：详见下文**公有变量与私有变量的区别**

### **1. 普通变量的类型**

| **变量类型** | **描述** | **示例** |
| --- | --- | --- |
| 字符串 | 字符串内容 | ``` "string" ``` |
| 字符串数组 | 由字符串组成的数组 | ``` ["str_1", "str_2"] ``` |
| 布尔值 | 布尔值内容，`true`或者`false` | ``` true ``` |
| 布尔数组 | 由布尔值组成的数组 | ``` [true, false] ``` |
| 数字 | 数字内容 | ``` 1688 ``` |
| 数字数组 | 由数字组成的数组 | ``` [1688, 1111] ``` |
| 对象 | 具有多个属性和对应值的结构体 | ``` {   "title": "标题",   "desc": "描述" } ``` |
| 对象数组 | 由多个对象构成的数组 | ``` [   {     "title": "标题_1",     "desc": "描述_1"   },   {     "title": "标题_2",     "desc": "描述_2"   } ] ``` |
| Markdown 内容 | 供「Markdown 内容」组件使用的数据类型，支持展示彩色文本、加粗、斜体、不同字号、链接、艾特人、钉钉表情展示等功能，语法规范请参考[Markdown 变量](0019-markdown-variable-new.md) | ``` "## 二级标题" ``` |
| 图表 | 供「图表」组件使用的数据类型，相关协议请参考[图表变量](0020-chart-variable.md) | ``` {   "data": [     {       "x": "N0",       "type": "line",       "y": 48     },     {       "x": "N1",       "type": "line",       "y": 74     }   ],   "type": "lineChart",   "config": {} } ``` |
| 用户信息 | 展示用户信息的数据类型，相关协议请参考[用户信息变量](0021-user-information-variables.md) | ``` {   "avatar": "",   "nick": "",   "uid": "" } ``` |
| 表格 | 供「表格」组件使用的数据类型，相关协议请参考[表格变量](0022-table-variables.md) | 参考[表格变量](0022-table-variables.md) |
| 表单 | 供「表单」组件使用的数据类型，相关协议请参考[表单变量](0023-form-variables.md) | 参考[表单变量](0023-form-variables.md) |

### **2. 公有变量和私有变量**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p550149.png)

根据变量定义时是否选中私有选项，可以将变量分为公有变量和私有变量，定义为私有变量后，**卡片将会从卡片的私有数据中获取该变量对应的数据，如果私有数据中获取不到则从公有数据中获取**。

公有、私有变量的区别如下：

| **数据类型** | **公有变量** | **私有变量** |
| --- | --- | --- |
| **对应的数据类型** | 公有数据（cardData） | 私有数据（cardPrivateData） |
| 可见范围 | 数据对所有人可见 | 只针对自己可见 |

简单来说，通过私有变量和私有数据的结合，服务端可以以一个相同的模板为不同的用户推送不同的数据，实现不同的卡片接收者看到的卡片不一样的效果。

> **[!NOTE]**
>
> 关于公有数据和私有数据具体的差异，请参考[公有数据、私有数据和本地数据](0013-public-private-and-local-data.md)。

## **二、表达式变量**

表达式变量是对多个变量进行引用和组合计算得到的变量，具有强大的能力，支持数字基础运算、大小判断、字符串拼接截取、类型转换、数组和对象的值获取、时间格式化等功能。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p550157.png)

其变量配置如下：

- **变量名**：唯一的变量名称
- **表达式**：表达式内容，如`variable_1 + variable_2`
- **变量描述**：该变量的描述，非必填

### **1. 表达式文档**

点击表达式变量旁边的帮助图标即可打开表达式文档，可以查看所有的表达式以及具体的用法示例。

![exp_variable_doc](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p532552.gif)

### **2. 表达式变量使用示例**

假设目前已有一个展示文章列表的卡片：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p550158.png)其中卡片变量中有一个叫`content`的对象数组，用来循环渲染并展示文章列表，`content`的每个数组项中都有一个`id`字段，代表文章的`id`，想要实现在卡片中点击每一篇文章时能够自动打开一个拼接好的最终链接，如

```
"https://www.dingtalk.com/?id=${id}"
```

其中的`${id}`代表`content`数组项中的`id`字段。

为此我们可以创建一个表达式变量，来表示数组中每一项的最终链接：

1. 首先点击新增表达式变量，并输入变量的名称，变量名称即绑定变量时使用的变量名。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p550160.png)
2. 接下来是输入表达式，想要拼接字符串我们可以使用`concat`方法，该方法的参数既可以是变量，也可以是字符串，因此我们可以先简单的把链接前缀写进该表达式中。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p550183.png)
3. 拼接的第二个参数就是`content`数组中的每项的`id`，此处我们需要使用另外一个表达式方法`subdata`，当我们输入`subdata()`时，变量的配置中会出现「循环数组」的选项，代表`subdata`是从哪个数组中取值。因此我们选中`content`数组，并输入`subdata("id")`，代表从`content` 数组中取出每一项的`id`与链接进行拼接。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p550189.png)
4. 最终该表达式变量的表达式即为。

   ```
   concat("https://www.dingtalk.com/?id=", subdata("id"))
   ```
5. 最后一步，我们需要在循环数组中的容器设置点击事件，并绑定该变量。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p550196.png)
6. 进入预览模式后我们发现点击不同的文章会跳转到不同的链接，达到最终目的。

## **三、本地变量**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p550205.png)

本地变量是一种特殊的私有变量，它是卡片的临时状态，值的修改不会发送请求到服务端，但可以通过其他组件（如按钮）的回传请求事件将本地变量的值进行回传，可以用于表单收集等场景。

### **1. 本地变量使用示例**

实现一个简单的表单，询问小伙伴们是否参加某项活动，其中包含一个选择框和一个提交按钮，用户可以在选择框进行勾选，提交时携带是否参加的值。这种场景就非常适合使用本地变量来存储「是否参加」的值，等到点击提交的时候再一并对临时的值进行收集。

> **[!NOTE]**
>
> 由于示例较为简单，此处略过卡片搭建的过程，从事件和变量的处理开始讲解。

1. 首先创建一个名`join`的本地变量，来代表接收者是否参加。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p550224.png)
2. 为选择框绑定`join`变量，从而实时展示参加的状态。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p550227.png)
3. 为了实现接受者点击选择框后可以对是否参加的值进行切换，我们需要为选择框添加事件，点击后更新本地变量`join`。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p550231.png)
4. 对于选择框展示与更新本地变量值的处理已经完毕，接下来为提交按钮添加回传请求事件，点击后将本地变量`join`提交回服务端。如图，回传参数中我们配置了参数类型为变量，并选择参数值为`join`变量。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p550239.png)
5. 至此，卡片的设计已经完毕。在实际发出的卡片中点击提交即可将`join`变量值进行提交。

   ```
   {
       "actionType": "0",
       "cardInstanceId": "String",
       "actionId": "1",
       "actionData": "{\"cardPrivateData\":{\"params\":{\"join\":true},\"actionIds\":[\"1\"]}}",
       "requestEventId": "String",
       "requestStatusKey": "String"
   }
   ```
