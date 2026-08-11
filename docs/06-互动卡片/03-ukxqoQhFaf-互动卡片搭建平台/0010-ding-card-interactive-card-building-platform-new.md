---
title: "互动卡片普通版搭建平台"
source_url: "https://open.dingtalk.com/document/download/ding-card-interactive-card-building-platform-new"
namespace: "download"
slug: "ding-card-interactive-card-building-platform-new"
group: "互动卡片"
tab: "互动卡片搭建平台"
breadcrumb: "互动卡片普通版搭建平台 > 互动卡片普通版搭建平台"
doc_id: "bAuIHYSjv7"
updated_at: "2026-01-29 14:34:05"
---

> Source: https://open.dingtalk.com/document/download/ding-card-interactive-card-building-platform-new
> Path: 互动卡片 / 互动卡片搭建平台 / 互动卡片普通版搭建平台 > 互动卡片普通版搭建平台
> Updated: 2026-01-29 14:34:05

# 互动卡片普通版搭建平台

本文介绍了互动卡片普通版搭建平台的基本功能、卡片配置相关数据结构内容，帮助开发者系统了解该平台的设计背景、使用场景及完整接入流程。通过本指南，开发者可快速掌握如何利用可视化工具高效构建互动卡片，并通过接口实现消息发送与交互处理。

## 设计背景

随着企业数字化协作需求的不断增长，传统静态消息已难以满足复杂业务场景下的信息展示与用户交互需求。钉钉推出的**互动卡片**是一种支持动态内容展示和用户操作反馈的消息形态，广泛应用于审批、任务分配、日程提醒、数据填报等高频协作场景。

为降低开发者在卡片模板开发中的技术门槛，钉钉开放平台提供**互动卡片普通版搭建平台**，以可视化方式简化模板设计过程，无需编写代码即可完成专业级卡片布局，提升开发效率与维护便利性。

## 使用场景

- **审批流程通知**：员工提交申请后，审批人可在聊天窗口直接查看详情并点击“同意”或“拒绝”按钮。
- **任务分发与跟进**：项目负责人发送包含任务描述、执行人选择组件的任务卡片，接收方可即时确认或修改状态。
- **信息收集表单**：通过下拉选择器、时间选择器、选人组件等收集结构化数据，如会议意向调研、报名登记等。
- **数据看板推送**：定时向管理群推送关键指标卡片，支持点击跳转至完整报表页面。
- **内部公告增强交互**：发布公告时附加“已读回执”按钮或意见收集区域，提升沟通闭环能力。

## 什么是互动卡片普通版搭建平台

[**互动卡片普通版搭建平台**](https://card.dingtalk.com/card-builder)是钉钉提供的在线可视化工具，用于快速创建和编辑[互动卡片](0001-platform-building-overview.md)，平台集成了丰富的官方组件与通用模板，开发者无需从零编码即可完成卡片设计，并通过调用服务端API将模板应用于实际业务消息中。

### 适用对象

- 企业内部自研应用开发者
- 第三方ISV（独立软件供应商）开发者
- 需要快速实现高交互性消息能力的技术团队

## 主页介绍

登录[**互动卡片普通版搭建平台**](https://card.dingtalk.com/card-builder)后，模板编辑页面由三部分组成，分别是：

- 左边区域：组件和模板管理区
- 中间区域：模板搭建区
- 右边区域：代码区

![dingCard搭建平台 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7038314561/p444928.png)

## 组件和模板管理区

在组件和模板管理区，钉钉提供了一系列官方组件和模板资源，开发者可通过拖拽组件构建个性化卡片模板，也可直接选用官方推荐模板快速上线。![组件模板管理区](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7038314561/p446269.png)

### 组件区能力介绍

**基础模块**

提供基础的内容展示功能，当前支持以下7种类型：

| 模块 | 是否支持 | 描述 |
| --- | --- | --- |
| [文本模块](https://card.dingtalk.com/card-builder/docs/text) | 是 | 文本模块是钉钉卡片使用最频繁的模块，用以展示文本段落，并支持配置国际化、图标以及前缀标记。 |
| [富文本模块](https://card.dingtalk.com/card-builder/docs/markdown) | 是 | 富文本支持设置文本颜色、加粗、斜体、字号调整、链接、艾特人、钉钉表情等功能。 |
| [单图模块](https://card.dingtalk.com/card-builder/docs/image) | 是 | 单图模块用以展示图片，并支持配置宽高比、裁剪部位、预览功能等。 |
| [多图模块](https://card.dingtalk.com/card-builder/docs/imageList) | 是 | 多图模块为多张图片提供了丰富的布局。  **[!IMPORTANT]**  多图模块不支持配置宽高比和裁剪部位，默认为居中裁剪。 |
| [轮播图模块](https://card.dingtalk.com/card-builder/docs/imageCarousel) | 是 | 钉钉卡片提供了交互性更强的轮播图模块。  **[!IMPORTANT]**  轮播图图片要求不允许多于5张。 |
| [视频模块](https://card.dingtalk.com/card-builder/docs/video) | 是 | 视频模块提供一个视频播放器，用户可以在钉钉卡片上播放视频。 |
| [分割线模块](https://card.dingtalk.com/card-builder/docs/divider) | 是 | 该模块主要展示一条分割线，目前暂无配置项。 |

**交互模块**

提供可响应用户操作的表单类组件，显著提升卡片的交互能力，目前支持以下6种类型：

| 模块 | 是否支持 | 描述 |
| --- | --- | --- |
| [单选下拉选择器](https://card.dingtalk.com/card-builder/docs/select) | 是 | 单选下拉选择器是钉钉提供的一个交互组件，用以下拉单选内容。 |
| [多选下拉选择器](https://card.dingtalk.com/card-builder/docs/multiSelect) | 是 | 多选下拉选择器是钉钉提供的一个交互组件，用以下拉多选内容。 |
| [时间选择器](https://card.dingtalk.com/card-builder/docs/datePicker) | 是 | 时间选择器是钉钉提供的一个交互组件，用以选择年月日和时分秒内容。 |
| [聚合菜单](https://card.dingtalk.com/card-builder/docs/menu) | 是 | 聚合菜单是钉钉提供的一个支持跳转和回传服务端值的交互组件。 |
| [选人组件](https://card.dingtalk.com/card-builder/docs/userSelect) | 是 | 选择组件是钉钉提供的一个支持选择组织架构成员的一个交互祖组件。 |
| [按钮](https://card.dingtalk.com/card-builder/docs/button) | 是 | 按钮组件是钉钉提供的一个支持多种形式按钮的一个交互组件。支持不同的按钮样式和点击相应的事件类型。 |

**混排模块**

将文本与其他特定模块组合使用，实现更灵活的信息布局与交互表达：

| 模块 | 是否支持 |
| --- | --- |
| [双列文本](https://card.dingtalk.com/card-builder/docs/twoColumnText) | 是 |
| [文本 + 图片](https://card.dingtalk.com/card-builder/docs/textMixImage) | 是 |
| [文本 + 单选下拉选择器](https://card.dingtalk.com/card-builder/docs/textMixSelect) | 是 |
| [文本 + 多选下拉选择器](https://card.dingtalk.com/card-builder/docs/textMixMultiSelect) | 是 |
| [文本 + 时间选择器](https://card.dingtalk.com/card-builder/docs/textMixDatePicker) | 是 |
| [文本 + 聚合菜单](https://card.dingtalk.com/card-builder/docs/textMixMenu) | 是 |
| [文本 + 选人组件](https://card.dingtalk.com/card-builder/docs/textMixUserSelect) | 是 |
| [文本 + 按钮](https://card.dingtalk.com/card-builder/docs/textMixButton) | 是 |

### 官方模板区域能力介绍

在官方模板区域，钉钉提供了招聘流程、审批流程、信息收集等多种通用模板，覆盖常见办公协作场景。开发者可根据业务需求直接选用并做微调，大幅提升开发效率。![官方模板区](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7038314561/p446276.png)

### 我的模板区域能力介绍

在**我的模板**区域，开发者可以将历史编辑过的模板保存下来，便于后续复用与管理。

**模板保存前**：![模板保存前](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7038314561/p446279.png)**模板保存后**：![模板保存后](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7038314561/p446280.png)

## 模板搭建区

在模板搭建区，开发者可使用左侧的组件来搭建自己的模板，并通过发送测试卡片的按钮来实现测试已搭建的模板的效果。

在模板搭建区所搭建的模板，将自动适配桌面端和PC端，以及浅色模式和深色模式。![模板搭建区](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7038314561/p446283.png)

## 代码预览区

![代码预览区](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7038314561/p446284.png)

### 代码区卡片配置数据结构

钉钉卡片是通过 `JSON` 数据结构进行描述的，总共可将该描述划分为三个部分：**卡片属性**、**卡片头部**以及**卡片内容**。

### 卡片属性

在卡片的`JSON` 数据顶层通过`config`字段对卡片的整体属性进行配置，`config`的相关字段如下：![dingCard属性](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7038314561/p444936.png)

| 字段 | 是否必填 | 类型 | 描述 |
| --- | --- | --- | --- |
| autoLayout | 否 | Boolean | 卡片PC端是否自适应宽度：   - true：是 - false：否 |
| enableForward | 否 | Boolean | 卡片是否支持转发：   - true：支持 - false：不支持 |

示例如下：

```
{
  "config": {
    "autoLayout": true,
    "enableForward": true
  }
}
```

### 卡片头部

钉钉卡片的标题通过`JSON`描述的`header`字段进行配置，相关字段如下：![header图片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7038314561/p444973.png)

| 字段 | 是否必填 | 类型 | 描述 |
| --- | --- | --- | --- |
| title | 是 | JSON，参考[文本模块](https://card.dingtalk.com/card-builder/docs/text) | 卡片标题文案，支持配置颜色，具体颜色请查看[色值表](https://card.dingtalk.com/card-builder/docs/cardConstruction#color_table)。 |
| logo | 是 | String | 卡片 logo，支持普通链接和MediaId。 |
| darkLogo | 否 | String | 暗黑模式下的卡片logo。 |

```
{
  "header": {
    "title": {
      "type": "text",
      "text": "钉钉卡片",
      // 蓝色
      "color": "common_blue1_color"
    },
    "logo": "@lALPDfJ6V_FPDmvNAfTNAfQ"
  }
}
```

### 卡片内容

钉钉卡片的标题通过`JSON`描述的`content`字段进行配置。![卡片内容](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7038314561/p445010.png)具体数据详情参见上文**组件区能力介绍**。

## **更多信息**

了解互动卡片普通版搭建平台基础功能后，可通过[互动卡片普通版接入流程](0011-ding-card-interactive-card-operation-process.md)相关步骤，实现能力接入。
