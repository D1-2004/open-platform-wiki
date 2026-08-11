---
title: "CanvasContext.rect"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-rect"
namespace: "development"
slug: "jsapi-canvas-context-rect"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.rect"
doc_id: "qUP5gy4LSi"
updated_at: "2023-08-08"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-rect
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.rect
> Updated: 2023-08-08

# CanvasContext.rect

调用CanvasContext.rect，创建一个矩形。

> 用 fill() 或者 stroke() 方法将矩形画到 canvas 中。

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.rect(20, 20, 250, 80);
ctx.setFillStyle('blue');
ctx.fill();
ctx.draw();
```

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10100) |

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

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.rect({
  x: '0',
  y: '0',
  width: '10',
  height: '20',
});
```
