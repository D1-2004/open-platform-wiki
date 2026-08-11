---
title: "showToast"
source_url: "https://open.dingtalk.com/document/development/jsapi-show-toast"
namespace: "development"
slug: "jsapi-show-toast"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 交互反馈 > showToast"
doc_id: "YDnBy4mwwf"
updated_at: "2024-12-04"
---

> Source: https://open.dingtalk.com/document/development/jsapi-show-toast
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 交互反馈 > showToast
> Updated: 2024-12-04

# showToast

调用dd.showToast显示一个弱提示，在到达设定的显示时间后自动消失弱提示。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 7.0.10 | 7.0.10 | 7.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10067) |
| 小程序 | 7.0.10 | 7.0.10 | 7.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10067) |

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

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 2 | 参数无效 |
| 3 | 系统异常 |

## **示例****代码**

### 默认出入参

```
dd.showToast({
  type: 'success',
  content: '恭喜你，审核完成咯',
  duration: 2000,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
