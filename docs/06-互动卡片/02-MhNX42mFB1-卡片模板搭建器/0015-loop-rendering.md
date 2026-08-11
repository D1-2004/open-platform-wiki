---
title: "循环渲染"
source_url: "https://open.dingtalk.com/document/development/loop-rendering"
namespace: "development"
slug: "loop-rendering"
group: "互动卡片"
tab: "卡片模板搭建器"
breadcrumb: "绑定卡片变量 > 循环渲染"
doc_id: "RBDNWrZvge"
updated_at: "2025-10-09 18:05:17"
---

> Source: https://open.dingtalk.com/document/development/loop-rendering
> Path: 互动卡片 / 卡片模板搭建器 / 绑定卡片变量 > 循环渲染
> Updated: 2025-10-09 18:05:17

# 循环渲染

通过本文你将了解到如何使用循环渲染容器来展示列表内容。

## **概述**

循环渲染指通过数据来动态地展示内容项，这是一个非常典型的场景，例如报名用户列表等。下面将会借助用户列表渲染的例子来帮助你快速的了解循环渲染的使用。

## **预期效果**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p550581.png)

如图所示，卡片中展示了用户信息列表，且每个用户都有序号、头像以及昵称信息。

> **[!NOTE]**
>
> 循环渲染的结果只能在预览模式下才生效，且在编辑模式下当没有数据时「渲染渲染容器」不会展示子元素。为了更方便地进行布局的搭建调整，在循环渲染前建议先定义变量和模拟数据。

## **步骤一：创建变量**

循环渲染需要一个列表，且每位用户需要展示序列号、头像以及昵称。

因此，我们首先创建一个`userList`的对象数组来表示用户列表，且在数组中的每一项都包含以下字段：

- **index**：序列号
- **userName**：用户昵称
- **avatar**：用户头像

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p550582.png)

## **步骤二：数据模拟**

接下来为`userList`模拟相关数据并保存，如图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p550590.png)

## **步骤三：布局搭建并绑定变量**

想要利用变量进行循环渲染，就必须借助「循环渲染容器」来绑定变量进行渲染。由于布局搭建的步骤较多，此处分为**基础布局实现**、**用户序列号展示**、**用户头像展示**以及**用户昵称展示**四个部分。

### **基础布局实现**

1. 添加「循环渲染容器」组件，绑定`userLIst` 变量后设置相关样式。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p550593.png)![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p550628.png)
2. 基础的循环容器搭建好后，我们需要确定循环项的布局，分析每一项用户信息，我们可以将其切分为三个部分，分别放置用户的序列号、头像以及昵称。
3. 对于这种三段式的布局，我们可以先使用「1:1:1」的布局方式后再进行调整，将「1:1:1」组件拖入「渲染渲染容器」中。![drag_1_1_1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p537977.gif)

### **用户序列号展示**

1. 序列号的展示可以直接使用「基础文本」组件来展示，而为了卡片样式更加美观，我们修改「布局容器」的字元素位置为「左中」，这样子能保证子元素垂直居中。![loop_step2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p537978.gif)
2. 因为序号的宽度不会很长，此处为「布局」组件添加合适的固定宽度。![loop_step3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p537979.gif)
3. 最后，对于「基础文本」组件，我们绑定循环数组中的`index` 字段。![loop_step4](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p537980.gif)
4. 至此，在预览模式下已经能展示出模拟数据中的所有序列号了。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p550641.png)

### **用户头像展示**

1. 该步骤与用户序列号的展示大致相同，在中间的布局中，我们使用「头像」组件来展示头像，并绑定循环里的`avatar`变量，最后简单调整一下样式。![loop_step5](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p537989.gif)
2. 同样地，调整一下「布局」的宽度为合适值即可。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p550655.png)
3. 至此，在预览模式下也同样能展示出模拟数据中的所有头像了。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p550656.png)

### **用户昵称展示**

用户昵称的展示与用户的序列号展示一样，都是使用「基础文本」组件进行展示，如图所示：

![loop_step6](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p537994.gif)

至此，循环渲染的示例已经结束，这是最终的效果。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p550661.png)
