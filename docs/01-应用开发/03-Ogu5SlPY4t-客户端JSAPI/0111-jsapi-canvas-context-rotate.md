---
title: "CanvasContext.rotate"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-rotate"
namespace: "development"
slug: "jsapi-canvas-context-rotate"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.rotate"
doc_id: "zilv2salKn"
updated_at: "2023-08-08"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-rotate
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.rotate
> Updated: 2023-08-08

# CanvasContext.rotate

调用rotate，以原点为中心（原点可以用translate方法修改），顺时针旋转当前坐标轴。多次调用rotate，旋转的角度会叠加。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | - |

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
dd.CanvasContext.rotate((30 * Math.PI) / 180);
```

`success`返回对象示例：

```
{}
```
