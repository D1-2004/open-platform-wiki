---
title: "MapContext.translateMarker"
source_url: "https://open.dingtalk.com/document/development/jsapi-map-context-translate-marker"
namespace: "development"
slug: "jsapi-map-context-translate-marker"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 地图 > MapContext.translateMarker"
doc_id: "5Np7rY3ljD"
updated_at: "2023-08-08"
---

> Source: https://open.dingtalk.com/document/development/jsapi-map-context-translate-marker
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 地图 > MapContext.translateMarker
> Updated: 2023-08-08

# MapContext.translateMarker

MapContext.translateMarker用于平移点标记（marker）。

对同一个 markerId，在 translateMarker 没调用 animationEnd 之前再次调动无法生效，需要在调用 animationEnd 之后再调用一次动画，方才有效。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10135) |

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
const mapContext = dd.createMapContext();

mapContext.translateMarker({
  rotate: 90,
  duration: 1000,
  markerId: 0,
  autoRotate: false,
  destination: { latitude: 30, longitude: 120 },
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
