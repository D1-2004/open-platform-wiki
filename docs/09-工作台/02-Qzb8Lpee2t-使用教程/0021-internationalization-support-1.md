---
title: "国际化支持"
source_url: "https://open.dingtalk.com/document/dingstart/internationalization-support-1"
namespace: "dingstart"
slug: "internationalization-support-1"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > 场景示例 > 国际化支持"
doc_id: "IKfDLylsJI"
updated_at: "2025-09-03 15:57:10"
---

> Source: https://open.dingtalk.com/document/dingstart/internationalization-support-1
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > 场景示例 > 国际化支持
> Updated: 2025-09-03 15:57:10

# 国际化支持

**方案**

- 组件内处理国际化逻辑。
- 加载组件时，会传入变量 locale，例如 zh\_CN、en\_US 等。
- 组件需要在 didUpdate 里处理 locale 变更逻辑。

如下图中，组件需内部实现 compI18n，处理国际化：

![国际化支持](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7551987261/p300406.png)
