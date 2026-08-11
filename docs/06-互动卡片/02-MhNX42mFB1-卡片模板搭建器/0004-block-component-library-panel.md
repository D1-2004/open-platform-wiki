---
title: "区块组件库面板"
source_url: "https://open.dingtalk.com/document/development/block-component-library-panel"
namespace: "development"
slug: "block-component-library-panel"
group: "互动卡片"
tab: "卡片模板搭建器"
breadcrumb: "面板介绍 > 区块组件库面板"
doc_id: "pKFpb0AaEq"
updated_at: "2025-09-23 19:18:25"
---

> Source: https://open.dingtalk.com/document/development/block-component-library-panel
> Path: 互动卡片 / 卡片模板搭建器 / 面板介绍 > 区块组件库面板
> Updated: 2025-09-23 19:18:25

# 区块组件库面板

通过本文你将了解到如何向模拟器中添加区块组件以及搭建器中有哪些区块组件。

## **内容介绍**

区块组件库面板直观地罗列出了所有区块组件，其入口如下图所示。同样地，你可以通过拖拽的方式将区块组件拖入「模拟器画布」中的某个位置上。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3882293761/p515000.png)

## **基础组件与**区块组件的区别

区块组件一般由基础组件组合而成，一般一个组件单独占用一行空间。

> **[!NOTE]**
>
> - 基础组件：[组件库面板](0003-component-library-panel.md)中的组件
> - 区块组件：区块组件库面板中的组件

|  | **基础组件** | **区块组件** |
| --- | --- | --- |
| **配置性** | 可配置组件的内容和样式 | 统一了 UI 规范，不支持样式上的配置，只能配置内容 |
| **是否原子化** | 是 | 否，区块组件中具有复合组件 |
| **是否支持响应式布局** | 否 | 复合的区块组件支持响应式布局 |
| **是否能与其他布局嵌套使用** | 可以 | 只能作为卡片顶层的组件，无法嵌套在其他布局中使用 |

## **复合组件的响应式功能**

复合组件是由文本和另一部分组合而成的区块组件，它们的排列方式可能是左右排列，也有可能是上下排列。在某种条件下，复合组件的排列方式会进行改变，这就是它的响应式。下面以一个「双列文本」组件为例，帮助你更轻松地理解响应式。

| **条件（或）** | ① 在 PC 端且卡片宽度大于 440px | ① 在移动端  ② 在 PC 端且卡片宽度小于 440px |
| --- | --- | --- |
| **排列方式** | 左右排列 | 上下排列 |
| **示例** | image | image |

### **开启响应式功能**

想要开启响应式，需要在卡片创建时为卡片的公有数据添加`config`对象，并配置`config.autoLayout`为`true`，下面分别介绍[卡片平台创建卡片实例](../01-N4KJ5HbqnQ-开发指南/0003-create-a-card-instance-from-the-card-platform.md)和[开放接口创建卡片实例](../01-N4KJ5HbqnQ-开发指南/0004-open-the-interface-to-create-a-card-instance.md)两种方式如何配置：

#### **通过卡片平台创建时**

1. 为了在创建实例时能为`autoLayout`配置值，我们需要定义该变量，如图，需要作为`config`对象的一个字段。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3882293761/p549913.png)
2. 搭建完成后「发布」卡片，进入卡片实例管理页面。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3882293761/p538065.png)
3. 为`config`配置静态数据，如图所示，其中`autoLayout`为`true`。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3882293761/p538066.png)
4. 实现[卡片平台投放卡片实例](../01-N4KJ5HbqnQ-开发指南/0005-card-delivery-instance-for-card-platform.md)即可。

#### **通过开放接口创建时**

由于`config`的值是非字符串类型，因此我们在创建卡片实例时，需要在内置的`cardParamMap.sys_full_json_obj`字段中添加相关变量，[开放接口投放卡片实例](../01-N4KJ5HbqnQ-开发指南/0006-open-interface-card-delivery-instance.md)后即可看到响应式效果。

```
{
  "cardData" : {
    "cardParamMap" : {
      "sys_full_json_obj" : "{\"config\":{\"autoLayout\":true}}"
    }
  },
}
```

#### **实际效果**

此处使用了「文本+下拉框」和「文本+按钮」复合组件进行演示。

![autolayout](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3882293761/p538071.gif)
