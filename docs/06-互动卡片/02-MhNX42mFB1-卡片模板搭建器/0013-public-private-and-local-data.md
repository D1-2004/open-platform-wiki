---
title: "公有数据、私有数据和本地数据"
source_url: "https://open.dingtalk.com/document/development/public-private-and-local-data"
namespace: "development"
slug: "public-private-and-local-data"
group: "互动卡片"
tab: "卡片模板搭建器"
breadcrumb: "绑定卡片变量 > 公有数据、私有数据和本地数据"
doc_id: "66rxeYtyEY"
updated_at: "2025-09-23 19:18:32"
---

> Source: https://open.dingtalk.com/document/development/public-private-and-local-data
> Path: 互动卡片 / 卡片模板搭建器 / 绑定卡片变量 > 公有数据、私有数据和本地数据
> Updated: 2025-09-23 19:18:32

# 公有数据、私有数据和本地数据

通过本文你可以了解到公有数据、私有数据、本地数据三种模拟数据类型以及它们的区别。

> **[!NOTE]**
>
> 在阅读本文档之前，确保你已经完成了以下的准备工作：
>
> - 了解数据源面板中的 Mock 数据面板的相关操作，参见[数据源面板](0006-data-source-panel.md)。

## **一、内容介绍**

在卡片模板搭建器中没有真实服务端下发的卡片数据，想要看到模板结合数据的最终结果，就需要通过变量数据模拟以及变量绑定[展示动态化内容](0011-binding-variables.md)来达成目的。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1192293761/p550495.png)

上图为 Mock 数据面板的截图，除了可以看到公有数据之外，还有私有数据和本地数据的模拟。

## **二、公有数据**

公有数据顾名思义，就是所有用户共享的数据。公有数据主要服务于正常创建的**公有**的**普通变量**。

创建公有变量及其模拟数据的说明如下：

1. 在不开启「私有化」的开关的情况下创建的变量就是一个公有变量。公有变量也是最常用的变量类型，能够服务于大多数没有“千人千面”诉求的卡片场景。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1192293761/p550503.png)
2. 在 Mock 数据面板中编写该变量的公有数据。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1192293761/p550514.png)
3. 使用组件绑定该变量，即可在模拟器中看到实时预览效果。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1192293761/p550517.png)

## **三、私有数据**

私有数据是针对用户自身定制的数据，仅用户本身可查看。它的优先级高于公有数据，渲染时，如果卡片在私有数据中获取不到变量对应的值时，会尝试去公有数据中获取。

接下来将上述的`str` 转为私有变量，并进行私有数据的模拟：

1. 如图，将`str`变量进行私有化。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1192293761/p550518.png)
2. 私有化后，可以在 Mock 数据面板中为该变量编写私有数据。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1192293761/p550522.png)
3. 如图，模拟器中的`public string`字样已经转变为`private string`。同时，可以发现在上述的 Mock 数据面板中，既编写了`str`变量的公有数据，又编写了其私有数据，但最终还是按照私有数据进行展示，这也再次说明了**私有数据的优先级高于公有数据**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1192293761/p550526.png)

## **四、本地数据**

与公有数据和私有数据不同的是，公有数据和私有数据服务的是普通变量，而本地数据则是为**本地变量**服务的。本地变量仅保存在当前的客户端会话中，卡片下发时是空的，切换会话后会重置，无法通过服务端下发本地变量默认值。

接下来以一个简单的例子展示本地变量和本地数据是如何结合组件进行运作的：

1. 创建本地变量`local` 。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1192293761/p550557.png)
2. 编写该变量的本地数据。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1192293761/p550558.png)
3. 使用**选择框**组件绑定该本地变量。

   > **[!NOTE]**
   >
   > 目前能操作本地变量的组件只有**选择框**组件

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1192293761/p550561.png)
4. 修改**选择框**组件的点击事件为更新本地变量`local` 。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1192293761/p550565.png)
5. 进入预览模式，鼠标单击**选择框**即可进行本地数据的更新（布尔值取反）。如下图，选择框的选中状态随着鼠标点击进行了切换。![local_var](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1192293761/p517529.png)

## **五、公有、私有、本地数据的区别**

| **数据类型** | **公有数据** | **私有数据** | **本地数据** |
| --- | --- | --- | --- |
| **可见范围** | 所有人可见 | 仅自己可见 | 仅自己可见 |
| **对应的变量类型** | 普通变量（公有） | 普通变量（私有） | 本地变量 |
| **优先级** | 低 | 高 | 仅对本地变量生效，没有优先级可言 |
| 在搭建器中模拟数据 | image | image | image |
| [卡片平台创建卡片实例](../01-N4KJ5HbqnQ-开发指南/0003-create-a-card-instance-from-the-card-platform.md) | ``` {   "cardData" : {     "cardParamMap" : {       "key" : "String"     }   }, } ``` | ``` {   "privateData" : {     "userId" : {       "cardParamMap" : {         "key" : "String"       }     }   } } ``` | 本地数据为卡片的临时数据，不支持通过 API 传入 |
