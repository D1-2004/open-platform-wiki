---
title: "startLocating"
source_url: "https://open.dingtalk.com/document/development/jsapi-start-locating"
namespace: "development"
slug: "jsapi-start-locating"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "位置服务 > startLocating"
doc_id: "WgHtLWQkdL"
updated_at: "2024-12-04"
---

> Source: https://open.dingtalk.com/document/development/jsapi-start-locating
> Path: 应用开发 / 客户端JSAPI / 位置服务 > startLocating
> Updated: 2024-12-04

# startLocating

调用startLocating，连续获取当前地理位置信息（持续定位）。

用于对定位精度要求较高以及需要持续更新用户位置的场景，通过持续接收callback方式，获取用户当前的位置信息。连续定位功能，由三个接口组成，开始连续定位(startLocating)、停止连续定位(stopLocating)、以及获取当前定位状态(getLocatingStatus)。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11678) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11678) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

参数占位区域

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

参数占位区域

## **示例****代码**

### 默认出入参

```
dd.startLocating({
  sceneId: '****',
  useCache: true,
  withReGeocode: fal,
  targetAccuracy: 200,
  callBackInterval: 1000,
  iOSDistanceFilter: Number,
  success: (res) => {
    const {
      city,
      road,
      address,
      netType,
      accuracy,
      district,
      latitude,
      provider,
      province,
      errorCode,
      longitude,
      isFromMock,
      errorMessage,
      isGpsEnabled,
      locationType,
      operatorType,
      isWifiEnabled,
      isMobileEnabled,
    } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{"loc":{"start":{"line":1,"column":165},"end":{"line":1,"column":168}},"codeFrame":"> 1 | {city:'北京市',road:'西大望路甲12-2号楼。',address:'如：北京市朝阳区南磨房镇北京国家广告产业园区。',netType:'wifi',accuracy:200,district:'朝阳区',latitude:119.,provider:'wifi',province:'北京市',errorCode:返回码,longitude:100,isFromMock:true,errorMessage:'返回码描述',isGpsEnabled:true,locationType:1,operatorType:'CMCC',isWifiEnabled:true,isMobileEnabled:true,}\n    |                                                                                                                                                                     ^^^"}
```
