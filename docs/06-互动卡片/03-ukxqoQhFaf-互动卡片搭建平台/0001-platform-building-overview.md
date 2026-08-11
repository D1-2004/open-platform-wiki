---
title: "概述"
source_url: "https://open.dingtalk.com/document/download/platform-building-overview"
namespace: "download"
slug: "platform-building-overview"
group: "互动卡片"
tab: "互动卡片搭建平台"
breadcrumb: "概述"
doc_id: "Qp8CekIF0n"
updated_at: "2025-09-23 19:21:18"
---

> Source: https://open.dingtalk.com/document/download/platform-building-overview
> Path: 互动卡片 / 互动卡片搭建平台 / 概述
> Updated: 2025-09-23 19:21:18

# 概述

钉钉互动卡片搭建平台是在线可视化搭建互动卡片的平台，提供了创建互动卡片模板、编辑互动卡片模板等功能，帮助开发者更加方便、快速地接入互动卡片。

## 什么是互动卡片

钉钉互动卡片是一种新型的消息类型，它具有动态性、可交互性、多端统一等特点。它能够极大地丰富消息类型，并且促进用户的沟通互动。具有以下特点：

- **卡片内容可动态变更**

与普通的文本消息或Markdown消息相比，互动卡片能够在卡片内多端实时进行内容的变更，减少消息打扰，提升效率。

![卡片内容动态更新 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2395219361/p367447.gif)

- **在卡片内进行轻量级交互**

互动卡片能够让用户直接在卡片内进行轻量级交互，促进沟通互动，并且无需进入二级页面，能够缩短用户操作路径，提升效率。

![轻量级交互-1 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2395219361/p367461.gif)

- **四端一致、四端统一**

互动卡片只需编写一套模板，能够在不同平台（iOS、Android、Windows、macOS）展示，接入流程简单方便。

![四端统一 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2395219361/p367477.gif)

## 互动卡片版本介绍

为提升开发者使用体验，钉钉提供了互动卡片普通版和互动卡片高级版能力。

> **[!IMPORTANT]**
>
> 不同的版本，在搭建互动卡片模板、调用接口能力等方面不同。

| 说明 | 互动卡片普通版 | 互动卡片高级版 |
| --- | --- | --- |
| 使用的互动卡片模板搭建平台 | [**互动卡片普通版**](https://card.dingtalk.com/card-builder)搭建平台 | [互动卡片高级版搭建平台](0012-card-building-platform.md)搭建平台 |
| 支持的接口能力 | 互动卡片普通版支持的接口（见本文后续） | 互动卡片高级版支持的接口（见本文后续） |

## 搭建平台区别

为提升开发者使用体验，钉钉提供了互动卡片普通版和互动卡片高级版搭建平台。

| 搭建平台 | 适用场景 | 组件类型 | 布局方式 | 卡片形式 |
| --- | --- | --- | --- | --- |
| [**互动卡片普通版**](https://card.dingtalk.com/card-builder)搭建平台 | - 面向所有开发者。 - 开箱即用，开发成本低，适用于无定制化需求的场景。 - 官方提供一系列面向具体场景的模板帮助开发者更方便地接入。   **[!NOTE]**  如无特殊需求推荐使用。 | 区块组件 | - 上下布局 | JSON Schema |
| [**互动卡片高级版**](0012-card-building-platform.md)搭建平台 | - 面向进阶和有强定制化需求的开发者。 - 能力丰富强大，支持自定义布局和更精细力度的组件属性配置，有一定地上手门槛。 | 原子组件 | - 上下布局 - 左右布局 - 嵌套布局 | 模板+数据 |

## 开放的接口能力区别

> **[!NOTE]**
>
> 接口需要使用新版规范调用方式，请参考[如何调用服务端API](https://open.dingtalk.com/document/development/how-to-call-apis)和[服务端SDK下载](../../01-应用开发/02-4a8AMF6u2A-服务端API/0002-download-the-server-side-sdk.md)。

| 接口能力 | 互动卡片普通版 | 互动卡片高级版 |
| --- | --- | --- |
| 发送钉钉互动卡片 | [机器人发送互动卡片（普通版）](../../01-应用开发/02-4a8AMF6u2A-服务端API/1451-robots-send-interactive-cards.md) | [发送钉钉互动卡片（高级版）](../../01-应用开发/02-4a8AMF6u2A-服务端API/1453-send-interactive-dynamic-cards-1.md) |
| 更新钉钉互动卡片 | [更新机器人发送互动卡片（普通版）](../../01-应用开发/02-4a8AMF6u2A-服务端API/1452-update-the-robot-to-send-interactive-cards.md) | [更新钉钉互动卡片](../../01-应用开发/02-4a8AMF6u2A-服务端API/0780-interactive-card-update-interface.md) |
| 注册互动卡片回调地址 | **[!NOTE]**  无需注册互动卡片回调地址，[机器人发送互动卡片（普通版）](../../01-应用开发/02-4a8AMF6u2A-服务端API/1451-robots-send-interactive-cards.md)可设置回调地址。 | [注册互动卡片回调地址](../../01-应用开发/02-4a8AMF6u2A-服务端API/1455-registration-card-interaction-callback-address-1.md) |
| 发送轻量级互动卡片。  通过此模板将不再需要调试模板，不用关心卡片点击事件处理。在用户点击互动卡片之后，钉钉以事件订阅的形式将互动内容发送。 | 暂不支持 | [发送轻量级互动卡片](../../01-应用开发/02-4a8AMF6u2A-服务端API/1457-send-lightweight-interactive-cards.md) |
| 创建互动卡片实例 | 暂不支持 | [创建并开启互动卡片吊顶](../../01-应用开发/02-4a8AMF6u2A-服务端API/0759-send-group-helper-message.md) |
| 开启互动卡片实例置顶 | 暂不支持 | [创建并开启互动卡片吊顶](../../01-应用开发/02-4a8AMF6u2A-服务端API/0759-send-group-helper-message.md) |
| 关闭互动卡片实例置顶 | 暂不支持 | [关闭互动卡片吊顶](../../01-应用开发/02-4a8AMF6u2A-服务端API/0760-close-interactive-card-ceiling.md) |
