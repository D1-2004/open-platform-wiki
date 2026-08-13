---
title: "调试数据源请求"
source_url: "https://open.dingtalk.com/document/dingstart/debugging-data-source-requests"
namespace: "dingstart"
slug: "debugging-data-source-requests"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > 数据源 > 调试数据源请求"
doc_id: "RHEysx2wRt"
updated_at: "2025-09-03 15:57:07"
---

> Source: https://open.dingtalk.com/document/dingstart/debugging-data-source-requests
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > 数据源 > 调试数据源请求
> Updated: 2025-09-03 15:57:07

# 调试数据源请求

本文介绍了如何通过断点在 IDE 或设计器中预览时进行调试。

在IDE或设计器中预览时，如果你需要通过断点进行调试，可使用以下两种方式实现：

- 方式一：使用 **getSdk().alert** 调试。

  > **[!NOTE]**
  >
  > `getSdk().alert()`只会在IDE或设计器中预览时才会生效，在线上不生效。

  ```
  getSdk().alert('标题', '内容');
  ```
- 方式二：使用 **getSdk().logger** 调试。

  `getSdk().logger`提供了 **log** 和 **error** 方法，在开发调试过程中，可实现与 **console.log**、**console.error** 相同的效果。

  你还可以通过`getSdk().logger`打印的信息配合调试工具可以实现远程真机调试的效果，如下：

  [](https://cloud.video.taobao.com/play/u/3691671841/p/1/e/6/t/1/327664641545.mp4)
