---
title: "组件三种状态支持"
source_url: "https://open.dingtalk.com/document/dingstart/component-three-state-support-1"
namespace: "dingstart"
slug: "component-three-state-support-1"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > 场景示例 > 组件三种状态支持"
doc_id: "UcZchOfnaL"
updated_at: "2025-09-03 15:57:10"
---

> Source: https://open.dingtalk.com/document/dingstart/component-three-state-support-1
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > 场景示例 > 组件三种状态支持
> Updated: 2025-09-03 15:57:10

# 组件三种状态支持

在使用`sdk.request`时，需要`try catch`包裹，接口错误的情况下，需要展示组件的异常态。

> **[!NOTE]**
>
> 目前code为10002表示网关黑名单异常，其它code是接口本身异常。

代码示例：![组件三种状态支持](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7551987261/p300403.png)

- 当组件关联的应用未被安装，但组件被投放到工作台时，组件状态为营销态。
- 当组件所属的解决方案未被安装，但组件被投放到工作台时，组件状态为营销态。

```
// 营销态判断条件
this.props.componentProps.promotionState === 'STANDARD_WORKTAB'
```

**注意**：

- 营销态请按照营销态的设计稿来开发。
- 营销态时，组件不能请求`sdk.request`（强行请求会发生非预期情况）。
- 营销态时，组件被点击不能跳转自己的应用内地址（此时应用未开通，如果跳转会报错），需要跳转到 tryoutAddress（工作台自动注入给组件），代码示例如下：

  ```
  // 营销态时打开试用地址的示例代码
  if (this.props.componentProps.promotionState === 'STANDARD_WORKTAB') {
   getSdk().openApp({
     url: this.props.componentProps.tryoutAddress,
    });
  }
  ```

  非营销态和接口正常的情况下，按照设计规范展示正常态。
