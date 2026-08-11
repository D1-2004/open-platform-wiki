---
title: "绑定变量"
source_url: "https://open.dingtalk.com/document/development/binding-variables"
namespace: "development"
slug: "binding-variables"
group: "互动卡片"
tab: "卡片模板搭建器"
breadcrumb: "绑定卡片变量 > 绑定变量"
doc_id: "nNCQDkzXi1"
updated_at: "2025-09-23 19:18:30"
---

> Source: https://open.dingtalk.com/document/development/binding-variables
> Path: 互动卡片 / 卡片模板搭建器 / 绑定卡片变量 > 绑定变量
> Updated: 2025-09-23 19:18:30

# 绑定变量

本文将介绍什么是绑定变量以及如何绑定变量。

## 绑定变量

对于在数据源面板中定义的变量，想要让其展示在卡片上，就要在[组件属性设置面板](0008-component-property-settings-panel.md)上将组件的属性与对应的变量进行绑定，这就是绑定变量。

## **绑定变量的作用**

对组件的属性进行绑定变量后，当卡片在渲染时就能使用变量的值来进行展示，这是绑定变量最基础的作用。不仅如此，我们还可以结合变量的值来控制组件的显示与隐藏（即[条件渲染](0014-conditional-rendering-card.md)），也可以结合数组变量和「循环渲染容器」组件来循环渲染数组项（即[循环渲染](0015-loop-rendering.md)）。

## **如何绑定变量**

在组件属性设置面板上，绑定变量有两种方式：

1. 使用下拉框绑定变量
2. 使用`${}`语法绑定变量

### **使用下拉框绑定变量**

当我们在组件属性设置面板中看到如下图类似的具有「绑定变量」字样的设置器时，就可以在选中「绑定变量」后对变量进行快速绑定了。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2092293761/p550045.png)

> **[!IMPORTANT]**
>
> 需要注意的是，**不同的属性所能绑定的**[变量类型](0012-variable-type.md)**可能不一样**。例如，「图片圆角」这个属性就只能绑定数字类型的变量。当发现在绑定变量的变量列表中没有想要的变量时，那很有可能就是类型不匹配。

如下图，是「单张图片」组件的属性设置面板截图，可以看到其中的图片高度、图片宽度和图片圆角三个属性就都支持绑定变量。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3092293761/p550050.png)

### **使用 ${} 语法绑定变量**

以上下拉框的方式对于绑定变量的入口均比较明显，但目前还有其他的设置器是可以通过输入`${}`来对变量进行绑定的，较为常见的就如下具有帮助图标的文本输入框。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3092293761/p550082.png)

这种方式绑定变量的方式目前是字符串的输入，通过这种方式我们可以对字符串和变量较为自由的进行拼接。

当我们在输入`$`时，搭建器会自动弹出可使用的变量列表，选中后将会自动补充`{variable}`的内容。当然，也可以通过手动输入`${变量名}`来绑定变量。

> **[!IMPORTANT]**
>
> 需要注意的是，如果要使用的变量是对象变量的属性，那么需要通过`${object.property}`的方式来引用；如果在循环渲染容器里面要引用循环项的字段时，需要使用 `${loop.变量名}` 的格式来引用。
