---
title: "组件属性设置面板"
source_url: "https://open.dingtalk.com/document/development/component-property-settings-panel"
namespace: "development"
slug: "component-property-settings-panel"
group: "互动卡片"
tab: "卡片模板搭建器"
breadcrumb: "面板介绍 > 组件属性设置面板"
doc_id: "izCxDhxAas"
updated_at: "2025-09-23 19:18:28"
---

> Source: https://open.dingtalk.com/document/development/component-property-settings-panel
> Path: 互动卡片 / 卡片模板搭建器 / 面板介绍 > 组件属性设置面板
> Updated: 2025-09-23 19:18:28

# 组件属性设置面板

通过本文你可以了解到组件属性设置面板的功能以及常见的属性设置面板介绍。

## **内容介绍**

组件的属性面板用来修改组件属性的值。在组件属性设置面板中，你可以看到当前组件所有的属性并对它们进行配置。

当你在模拟器中选中某个组件时，组件设置面板就会同步展示对应组件的属性，如图：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1427989661/p516248.png)

## **属性分类**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p549932.png)

如上图所示，属性设置面板中的属性被分为四类：

- 内容：与组件内容相关的属性，如内容、图片地址、最大行数、是否显示等
- 样式：与组件样式相关的属性，常见的有文字颜色、文字大小、边距等
- 事件：与组件点击事件相关的属性，如链接跳转、回传请求、复制内容、弹窗提示等
- 高级：不隶属于前三类的高级属性，具体请查看组件的详细属性

## **常见功能介绍**

### **文本内容设置**

文本的内容设置经常被多个组件广泛使用到，凡是需要进行文本输入都会使用到它。它的作用是让开发者输入一段文本内容。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p549941.png)

#### **使用变量**

在文本内容属性设置中，开发者除了可以输入基础的文本内容之外，也可以在文本当中插入一些变量，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p549965.png)

在文本内容属性的设置中使用变量的方法是通过`${变量名}`的格式来实现的。如果要使用的变量是对象变量的属性，那么可以通过`${object.property}`的方式来引用。

需要注意的是，如果在循环渲染容器里面要引用循环项的字段时，需要使用 `${loop.变量名}` 的格式来引用变量。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p550031.png)

> **[!NOTE]**
>
> 使用变量之前，请确保已经创建了对应的变量。创建变量的方法请参考[数据源面板](0006-data-source-panel.md)文档。

#### **启用多语言支持**

钉钉客户端自身支持多语言，如果希望在钉钉客户端切换语言之后，卡片上的内容能够切换到对应语言的文案，那么可以在文本内容属性设置中开启“国际化”的配置。开启了国际化配置之后，开发者即可以为每一种语言配置独立的文案，在每一种语言的文案输入框里面同样可以引用变量。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p549971.png)

配置完成之后，也可以在搭建器上通过模拟器的预览功能来实现不同语言的预览：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p549975.png)

### **组件“条件显示”设置**

目前绝大多数组件均可以通过“是否显示”的属性来控制组件的显示或隐藏，而该属性对应的设置属性即是“条件显示”属性。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p549980.png)

“条件显示”设置面板有两个选项，一个是“固定值”，另一个是“条件计算”。

#### **固定值**

顾名思义，选择该选项之后，组件会按照所配置的“显示”或“隐藏”进行展示，不会进行动态展示。

#### **条件计算**

条件计算表示组件只有满足了一定的条件之后才会显示，否则不显示。目前有两种条件类型：运行环境和变量。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p549982.png)

| **条件类型** | **解释** |
| --- | --- |
| 运行环境 | 运行环境是指当客户端的版本号满足一定的条件时显示该组件。在选择客户端时，可以选择多个客户端，如桌面端、安卓客户端等。  需要注意的是，所填写的版本号必须是一个合法的版本号，否则功能不生效。  image |
| 变量 | 变量是指当卡片的变量数据值满足一定条件时显示该组件。在选择变量时，可以选择不同类型的变量，同时不同类型的变量对应的条件选项也会有所不同，例如对于布尔值类型的变量，它的条件只能是“为true”或“为false”。  image |

除了创建单个条件之外，也可以创建多个不同类型的条件，同时可以控制多个条件的满足条件，当配置了“且”的选项，那么表示只有所有的条件都满足了才会显示该组件。而当配置了“或”选项，表示只要有一个条件满足了，组件就会显示。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p550000.png)
