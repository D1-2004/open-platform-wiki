---
title: "MapContext.showRoute"
source_url: "https://open.dingtalk.com/document/development/jsapi-map-context-show-route"
namespace: "development"
slug: "jsapi-map-context-show-route"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 地图 > MapContext.showRoute"
doc_id: "oeU6yEBHWS"
updated_at: "2023-08-08"
---

> Source: https://open.dingtalk.com/document/development/jsapi-map-context-show-route
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 地图 > MapContext.showRoute
> Updated: 2023-08-08

# MapContext.showRoute

使用MapContext.showRoute规划默认步行路线，只能显示一条。

钉钉客户端 5.1.2 版本及以上支持规划步行、公交、骑行和驾车四种路线。

### 重要

IDE 模拟器无法获得返回值，需真机预览获得返回值。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10130) |

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
const mapContext = dd.createMapContext();

mapContext.showRoute({
  city: 'hangzhou',
  mode: 0,
  endLat: 30.256718,
  endLng: 120.059985,
  zIndex: 4,
  iconPath: `iconPath示例值`,
  startLat: 30.257839,
  startLng: 120.062726,
  iconWidth: 10,
  routeColor: '#FFB90F',
  routeWidth: 10,
  searchType: 'walk',
  throughPoints: [
    { lat: 39.866958, lng: 116.494231 },
    { lat: 39.9357, lng: 116.581092 },
  ],
  destinationCity: 'hangzhou',
  success: (res) => {
    const { success, distance, duration } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "success": true, "distance": 328, "duration": 262 }
```
