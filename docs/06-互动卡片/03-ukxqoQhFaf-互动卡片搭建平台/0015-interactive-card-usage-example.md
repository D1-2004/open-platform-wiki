---
title: "搭建互动卡片高级版模板示例"
source_url: "https://open.dingtalk.com/document/download/interactive-card-usage-example"
namespace: "download"
slug: "interactive-card-usage-example"
group: "互动卡片"
tab: "互动卡片搭建平台"
breadcrumb: "互动卡片高级版搭建平台 > 搭建互动卡片高级版模板示例"
doc_id: "RMkJN3vKgN"
updated_at: "2026-01-29 14:36:39"
---

> Source: https://open.dingtalk.com/document/download/interactive-card-usage-example
> Path: 互动卡片 / 互动卡片搭建平台 / 互动卡片高级版搭建平台 > 搭建互动卡片高级版模板示例
> Updated: 2026-01-29 14:36:39

# 搭建互动卡片高级版模板示例

为了让使用者更加直观地了解如何使用模板编辑器来搭建互动卡片，本文以审批卡片为例，完整展示从 0 到 1 的开发流程。通过本指南，开发者可快速掌握互动卡片的设计、数据绑定、发送与交互更新等核心能力。

## 适用对象

本文档适用于企业内部自建应用或第三方企业应用的开发者，用于在钉钉群聊中实现可交互的消息卡片（如审批、任务处理等场景）。

## 术语说明

- **互动卡片**：钉钉提供的一种支持动态数据渲染与用户交互的消息模板，可在群聊或单聊中使用，支持按钮点击、状态更新等功能。
- **sys\_full\_json\_obj**：系统保留字段，用于传递复杂结构的数据（如对象或数组），需将 JSON 对象序列化为字符串后填入`cardData.cardParamMap` 中。
- **回传请求**：当用户点击卡片上的按钮时，钉钉服务端会向开发者服务器发起的 HTTP 回调请求，包含用户操作信息及上下文数据。
- **outTrackId**：业务唯一标识符，在发送与后续更新卡片时必须保持一致，通常对应审批单 ID 或业务单据编号。
- **corpId**：企业的唯一标识，每个接入钉钉的企业都有一个独立的 corpId。
- **cardPrivateData**：卡片私有数据字段，包含按钮 ID（actionIds）和自定义回传参数（params），用于识别用户具体操作。

在开始开发前，请确保已完成以下准备工作：

1. 已创建**企业内部应用**或**第三方企业应用**，并在钉钉开发者后台完成注册；
2. 已获取应用的`AppKey`和`AppSecret`，用于调用 API 获取访问令牌；
3. 已申请并正确配置机器人`robotCode`，用于消息发送。

## 流程简介

步骤一：分析卡片需求。

步骤二：分析布局以及搭建样式。

步骤三：定义字段以及绑定数据。

步骤四：调用服务端API发送互动卡片。

步骤五：调用服务端API更新互动卡片。

## 步骤一：分析卡片需求

一个典型的审批卡片应具备以下交互功能：

- 用户点击整个卡片可跳转至审批详情页面；
- 卡片底部提供“同意”、“拒绝”按钮，支持一键操作；
- 操作完成后，按钮状态变更为“已同意”或“已拒绝”，且不可再次点击；
- 卡片数据根据审批结果实时更新，保持状态同步。

示意图如下：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6782662461/p389810.png)

操作后状态变化：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6782662461/p389811.png)

即使按钮已禁用，用户仍可通过点击卡片整体跳转至详情页。

## 步骤二：分析布局以及搭建样式

根据设计图，卡片整体可分为三部分：**卡片头部**、**卡片内容区**、**卡片底部按钮区**。其中内容区包含标题和列表项，每项由标签（加粗）和值（普通字体）组成。

1. 使用“卡片头部”组件设置主标题区域；
2. 添加“标题”组件展示审批事项名称；
3. 使用“横排按钮”组件添加“同意”、“拒绝”按钮；
4. 内容区使用“布局组件”实现两列对齐效果：

   - 插入一个 **1:1 布局组件**；
   - 左侧放置标签文本，右侧放置内容文本；
   - 开启左侧布局组件的 **“自适应宽度”** 属性；
   - 同时设置左侧文本组件也为“自适应宽度”；
   - 调整间距使两列紧邻显示。

我们先把简单的内容实现了，卡片头部、标题以及按钮这三部分先通过三个组件：“卡片头部”、“标题”、“横排按钮”组件来实现：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6782662461/p389812.png)

对于列表项内容，由于列表标题是加粗的字体，而列表内容是普通字体，因此没办法直接用单个文本组件来实现，这里就得使用布局组件来实现。

通过将一行文本内容，拆分成两部分，分别放置不同的文本组件，就可以实现设计稿的效果。首先，在卡片上放入布局组件，并调整好间距。可以先使用 1:1 的布局组件：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7782662461/p389813.png)

然后在左右两个布局上分别放置两个文本组件，调整文本组件的间距以及设置加粗样式：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7782662461/p389814.png)

此时，左右两边的文本是并排显示，但是我们希望两个文本是能够挨着显示，中间不要留空白。要实现这样的效果，必须让左边的布局宽度是自适应的，右边的布局宽度能够直接撑满剩下的空间。因此可以开启左边布局组件的“自适应宽度”属性，同时给左边的文本组件也设置成“自适应宽度”：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7782662461/p389815.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7782662461/p389816.png)

设置完两个属性之后，可以发现左右两边的文本组件已经挨在一起了，这时候我们修改一下文案内容，就能展示成最终效果了：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7782662461/p389817.png)

至此我们就完成了卡片的样式搭建。

## 步骤三：定义字段以及绑定数据

样式开发好了之后，我们需要开始定义卡片上的变量字段以及与卡片模板做绑定。根据卡片的需求，我们可以列出几个需要动态变更的内容：

- 审批标题
- 审批内容项
- 审批的状态
- 审批的详情页链接

有了这些内容定义之后，我们可以在卡片编辑器上开始创建变量，在数据源面板，点击“编辑普通变量”，然后在弹出来的页面里面把这几个数据录入进去：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7782662461/p389818.png)

其中，为了让内容足够灵活，审批内容项我通过对象数组的方式来表达，而不是使用单独的字段。同时，在创建变量的时候也可以同步设置变量的 mock 数据，这样方便在搭建的时候预览数据的效果：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7782662461/p389819.png)

编辑完保存之后，就可以在模板上对这些变量进行绑定。首先，选中整个卡片组件，给卡片配置卡片的点击跳转链接：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7782662461/p389820.png)

然后设置审批标题：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7782662461/p389821.png)

接着设置审批内容项。由于审批内容项是一个对象数组，在渲染对象数组时需要使用“循环渲染容器”组件，在卡片上放置“循环渲染容器”，同时设置组件的对象数组为审批内容项：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8782662461/p389822.png)

这时候放置在“循环渲染容器”里面的组件就能读取到对象数组里面每一项的内容了。因此我们只需要把前面搭建好的内容项组件放置到“循环渲染容器”里面，同时修改文本内容为变量就行：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8782662461/p389823.png)

由于是要读取对象数组里面的每一项的内容，因此文本内容绑定的变量需要加个 "loop." 的前缀，用来表示读取循环里面每一项的内容。

当绑定好变量之后，即可点击编辑器右上角的“预览模式”来查看最终的效果：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8782662461/p389824.png)

在没有开启预览模式时，循环渲染容器最多只会显示第一条内容，即使当前对象数组所配置的 mock 数据有多条记录。只有开启了预览模式才会使用真正的列表内容去展示。

至此我们完成了卡片变量的定义以及模板变量的绑定。

## 步骤四：发送互动卡片高级版内容

完成模板搭建后，以审批卡片为例，调用钉钉开放平台提供的[发送钉钉互动卡片](https://open.dingtalk.com/document/group/send-interactive-dynamic-cards#topic-2043166)接口发送卡片。

示例代码：

```
POST /v1.0/im/interactiveCards/send HTTP/1.1
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "cardTemplateId" : "templateid",
  "openConversationId" : "opencid",
  "outTrackId" : "uniqueid",
  "robotCode" : "robotcode",
  "conversationType" : 1,
  "cardData" : {
    "cardParamMap" : {
      "title": "朱小志提交的财务报销",
      "detailUrl": "https://dingtalk.com",
      "status": "pending",
      "sys_full_json_obj": "{\\"contents\\":[{\\"label\\":\\"报销类型\\",\\"text\\":\\"差旅费\\"},{\\"label\\":\\"报销金额\\",\\"text\\":\\"1000元\\"},{\\"label\\":\\"报销理由\\",\\"text\\":\\"出差费用\\"}]}"
    }
  }
}
```

参数说明：

| 参数 | 是否必填 | 描述 |
| --- | --- | --- |
| cardTemplateId | 是 | 卡片模板 ID，可在卡片编辑器中获取。 |
| openConversationId | 是 | 接收方会话 ID及群ID。 |
| outTrackId | 是 | 业务唯一标识，在审批的场景下，建议使用审批单 ID。 |
| robotCode | 是 | 应用对应的机器人 ID 。 |
| conversationType | 是 | 会话类型：   - **1**：表示群聊 - **0**：表示单聊 |
| cardData.cardParamMap | 是 | 卡片数据映射表。 |
| sys\_full\_json\_obj | 否 | 复杂对象需序列化为 JSON 字符串后填入此字段。 |

调用接口成功之后就能在群里面看到我们发送出来的卡片了。

## 步骤五：更新互动卡片高级版状态

为了实现用户点击按钮后的状态更新，需完成以下流程：

1. 在钉钉的开放平台上注册卡片的回调地址，点击卡片上“同意”或“拒绝”操作后，会通知到审批系统。
2. 对卡片模板做调整，在原来的按钮基础上新增两个按钮：“已同意”、“已拒绝”：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8782662461/p389825.png)
3. 我们希望在未审批时显示“同意”和“拒绝”按钮，审批通过后显示“已通过”，审批拒绝显示“已拒绝”。

在前面的字段定义环节，我们定义了一个 status 字段，用来表示当前的审批状态，我们假定它的值有以下几种：

- pending：未审批
- accept：审批通过
- reject：审批不通过

那么这时候我们可以给这四个按钮分别配置“是否显示”的属性，通过条件计算的方式来控制按钮的显示与否：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8782662461/p389826.png)

配置完之后，我们可以打开“预览模式”查看效果，同时也可以动态地修改 mock 数据来观察不同的 status 值所表现出来的样式是否符合期望。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8782662461/p389827.png)

当按钮的动态显示配置完之后，我们还需要配置按钮的点击事件，让审批系统知道当前按钮是要执行什么操作。

对于“已同意”和“已拒绝”按钮来说，由于该按钮不可点击，因此在搭建时可以给这两个按钮的“按钮状态”属性设置为“禁用”，这时候按钮就不能被点击了。

而在“同意”、“拒绝”按钮上，配置“按钮点击事件类型”为“回传请求”，这代表当用户点击该按钮后，会向你注册好的回调地址中发送请求。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8782662461/p389828.png)

比如对于“同意”按钮而言，配置了“回传请求”后，用户点击该按钮后，审批系统会接收到一个 HTTP 请求，请求内容为：

```
{
    "corpId": "dingXXXXXX",
    "outTrackId": "XXXXXX",
    "userId": "XXXXXX",
    "content": "{\"cardPrivateData\":{\"actionIds\":[\"1\"]},\"params\":{\"action\":\"accept\"}}"
}
```

其中：

- corpId：点击该按钮的用户的组织
- outTrackId：卡片的唯一ID。与发送卡片时的 outTrackId 值是一致的
- userId：点击该按钮的用户 ID
- content：按钮的详细信息。它是一个 JSON 字符串，里面包含了 cardPrivateData 字段，cardPrivateData.actionIds 代表的是当前点击的按钮 ID 。例如在审批的这个例子里面，由于“同意”按钮的 ID 是 1 ，因此这里 actionIds 的值是 ["1"] 。如果你在卡片模板上给按钮配置了回传参数，那么这些参数会在 cardPrivateData.params 里面出现。一般来说，业务系统可以根据 actionIds 以及 params 来确定用户所点击的按钮是哪一个，需要执行什么作。

当审批系统接收到该回调请求后，识别出当前是要执行“同意”操作，这时候审批系统处理完内部的业务逻辑后，需要把最新的卡片数据在当前的回调请求中返回，对于审批卡片而言，这时候需要更新卡片的 status 字段为 accept ，因此该回调请求需要返回的内容为：

```
{
  "cardTemplateId": "templateid",
  "outTrackId": "uqniueid",
  "cardOptions": {
    "updateCardDataByKey": true
  },
  "cardData": {
    "cardParamMap": {
      "status": "accept"
    }
  }
}
```

其中 cardOptions.updateCardDataByKey 代表了此次更新卡片的数据，只需要更新指定的字段，其他没有更新的字段保持原有的值。当返回了新的数据之后，钉钉的互动卡片会及时刷新为最新的状态和数据，至此就完成了卡片的状态更新的流程，详情参见[更新钉钉互动卡片](https://open.dingtalk.com/document/group/update-dingtalk-interactive-cards#doc-api-dingtalk-UpdateInteractiveCard)。
