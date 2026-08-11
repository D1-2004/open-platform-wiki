---
title: "数据源面板"
source_url: "https://open.dingtalk.com/document/development/data-source-panel"
namespace: "development"
slug: "data-source-panel"
group: "互动卡片"
tab: "卡片模板搭建器"
breadcrumb: "面板介绍 > 数据源面板"
doc_id: "SN9X9VBm0R"
updated_at: "2025-09-23 19:18:27"
---

> Source: https://open.dingtalk.com/document/development/data-source-panel
> Path: 互动卡片 / 卡片模板搭建器 / 面板介绍 > 数据源面板
> Updated: 2025-09-23 19:18:27

# 数据源面板

通过本文你可以了解到如何使用数据源面板，包括在数据源面板添加、编辑变量以及进行卡片模拟数据的修改。

## **内容介绍**

数据源包含了多种变量，这些变量对于卡片而言即是一个个的占位符，通过占位符即可让卡片实现内容的动态变化。

在数据源面板中，你可以直观的看到当前在卡片模板中创建的所有变量，并对它们进行管理，同时可以对创建的变量配置模拟数据；简而言之，数据源面板就是管理卡片变量和编辑模拟数据的模块，它的入口如下：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5018797661/p515205.png)

## **新增变量**

1. 如图所示，点击「新增」并在下拉框中选择新增的变量类型（此处以大部分场景下使用的**普通变量**为例，关于普通变量、表达式变量、新增本地变量的区别，参见文档[变量类型](0012-variable-type.md)）。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4018797661/p515293.png)
2. 在弹出的变量管理面板中，点击「新增变量」按钮新增变量。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4018797661/p515319.png)
3. 完善新增变量的**变量名**、[变量类型](0012-variable-type.md)、**变量描述、是否是私有变量**等信息后点击保存即可添加。

   > **[!NOTE]**
   >
   > 变量勾选了私有之后，表示当前变量支持私有变量模式，此时卡片在渲染时将优先从卡片的私有数据上获取对应的变量数据来进行展示。如果私有数据没有值，则使用公有数据进行展示。通过私有数据的模式，可以做到卡片内容千人千面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3914908661/p516105.png)

## **查看变量信息**

在数据源面板中会展示所有的变量列表。鼠标单击某一个变量即可打开变量的基础信息，如变量名、变量类型、是否私有是私有变量、描述等信息：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5286989661/p517453.png)

## **编辑变量**

变量的编辑包含变量的排序、复制、删除等功能，点击数据源面板中对应数据源的「编辑」按钮即可打开变量编辑面板。

打开的变量编辑面板与上文添加变量时打开的变量编辑面板是一样的，因此与「信息完善」和「新增变量」相关的功能不再进行赘述。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3914908661/p516100.png)

> **[!NOTE]**
>
> 不同的变量类型（普通变量、表达式变量等）有属于自己的「编辑」按钮以及变量编辑面板，不会互相影响。如图所示，这是表达式变量的编辑面板：
>
> ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3914908661/p516101.png)

下面将一一介绍变量编辑的相关功能。

### **变量排序**

通过长按对应变量前面的拖动图标，即可对变量进行上、下顺序的调整。

![drag_variable](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8882293761/p532232.gif)

### **变量复制**

变量的复制可以**快速地在同级目录下创建一个与目标配置相同的变量**，用好变量的复制有助于提高你的开发效率。

如图所示，高亮区域的图标即为变量复制的按钮，点击后即可在同级目录下对变量进行复制。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3914908661/p516106.png)

如下图所示，对名为`appNamePage`的变量进行了复制后可以看到同级目录下有新的变量名为`appNamePage_copy` 的变量。

![copy_variable](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8882293761/p532236.gif)

### **变量删除**

如图所示，高亮区域的图标即为变量删除的按钮，点击确认后即可对变量进行删除。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3914908661/p516102.png)

## **模拟数据编辑**

模拟数据即 Mock 数据，是对卡片变量值的模拟。

发送卡片需要结合真实的卡片数据，而我们可以在搭建器中通过变量数据的模拟来预览卡片在不同环境下的样子，有助你对卡片的布局等内容及时进行调整。

模拟数据的编辑，在数据源面板中共有两种方式：

1. 单个变量 Mock 数据编辑
2. 卡片整体 Mock 数据编辑

### **单个变量 Mock 数据编辑**

如图所示，高亮区域的图标即为变量模拟数据编辑入口，点击后即可进入该变量的模拟数据编辑页面。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3914908661/p516114.png)

#### **示例：**

1. 点击`title`变量的编辑 Mock 数据图标，进入 Mock 数据编辑面板。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3914908661/p516138.png)
2. 进入 Mock 数据编辑面板后，并填写数据为「钉钉，让进步发生」，点击「保存」对模拟数据的修改进行暂存。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3914908661/p516117.png)
3. 此时回到变量编辑面板，还需要点击「保存」更新暂存的 Mock 数据修改。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3914908661/p516139.png)
4. 此时可以看到模拟器中的卡片标题已经进行了修改。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3914908661/p516140.png)

   > **[!NOTE]**
   >
   > 这里修改了模拟数据后，卡片内容之所以能响应是因为卡片的标题中绑定了相关的变量，关于如何通过变量展示动态化的内容，参见[绑定变量](0011-binding-variables.md)。

### **卡片整体 Mock 数据编辑**

卡片整体 Mock 数据的编辑可以一次性对多种变量的多个变量进行 Mock 数据的编辑，提升 Mock 数据编辑的效率。

如图，在数据源面板中点击「Mock」按钮即可打开 Mock 数据编辑面板：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5286989661/p516141.png)

在此面板中你可以直接通过编辑`JSON`的形式去编辑卡片的[公有数据、私有数据和本地数据](0013-public-private-and-local-data.md)。
