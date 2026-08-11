---
title: "showActionSheet"
source_url: "https://open.dingtalk.com/document/development/jsapi-show-action-sheet"
namespace: "development"
slug: "jsapi-show-action-sheet"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 交互反馈 > showActionSheet"
doc_id: "P2RkXyfqAl"
updated_at: "2024-12-04"
---

> Source: https://open.dingtalk.com/document/development/jsapi-show-action-sheet
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 交互反馈 > showActionSheet
> Updated: 2024-12-04

# showActionSheet

调用dd.showActionSheet，显示操作菜单。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 7.0.10 | 7.0.10 | 7.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10071) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10071) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

参数占位区域

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

参数占位区域

## **示例****代码**

### 默认出入参

```
dd.showActionSheet({
  items: ['北京', '上海', '杭州'],
  title: '夏天去哪里玩',
  cancelButtonText: '我不去了',
  success: (res) => {
    const { index } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "index": 0 }
```
