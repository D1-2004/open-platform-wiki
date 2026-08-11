---
title: "条件渲染"
source_url: "https://open.dingtalk.com/document/development/conditional-rendering-card"
namespace: "development"
slug: "conditional-rendering-card"
group: "互动卡片"
tab: "卡片模板搭建器"
breadcrumb: "绑定卡片变量 > 条件渲染"
doc_id: "e71H0TEQC6"
updated_at: "2025-10-09 18:05:17"
---

> Source: https://open.dingtalk.com/document/development/conditional-rendering-card
> Path: 互动卡片 / 卡片模板搭建器 / 绑定卡片变量 > 条件渲染
> Updated: 2025-10-09 18:05:17

# 条件渲染

通过本文你将了解到什么是条件渲染以及它的使用场景。

## **内容介绍**

组件的条件渲染指的是组件只有在满足一定的条件（可以是钉钉的环境版本号、变量的值判断等条件）下才显示组件。

## **适用场景**

当需要根据不同的变量值来展示不同的效果时，可以考虑使用条件渲染。如审批卡片中对未处理、已接受、已拒绝三种不同状态的处理等等。

## **预期效果**

![compare](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3192293761/p534080.png)

假设想要实现一个简单的告警卡片，并满足：

- 当业务的反馈数**小于** 10 时，我们展示橙色的**告警**字样标签
- 当反馈数量**大于等于** 10 时，我们展示红色的**危险**字样标签

## **步骤一：布局搭建**

由于布局较为简单，此处从大纲树进行布局描述。如图：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3192293761/p550569.png)

1. 使用 **1:1** 布局容器简单地做内容分割。
2. 对于左边的布局容器，我们填充**基础文本**组件，用来展示反馈数文本。
3. 对于右边的布局容器，我们填充了两个标签，分别用来展示**警告**和**危险**。
4. 进行适当的布局调整。

## **步骤二：创建与绑定变量**

1. 在此例子中，需要设置的变量只有反馈数一个，因此我们创建一个`count`数字变量用来代表反馈数。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3192293761/p550571.png)
2. 为左边的布局容器中的「基础文本」组件绑定反馈数变量，展示反馈数。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3192293761/p550573.png)

## **步骤三：设置条件**

1. 为**警告**字样的标签设置显示条件：当变量`count`小于`10`时展示。。![set_tag_show_1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3192293761/p534091.gif)
2. 为**危险**字样的标签设置显示条件：当变量`count`大于等于`10`时展示。![set_tag_show_2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3192293761/p534092.gif)
3. 进入预览模式后，即可感受当反馈数不同时带来的不同效果。
