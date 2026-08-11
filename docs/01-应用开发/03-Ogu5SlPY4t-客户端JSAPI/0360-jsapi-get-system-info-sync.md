---
title: "getSystemInfoSync"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-system-info-sync"
namespace: "development"
slug: "jsapi-get-system-info-sync"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 系统信息 > getSystemInfoSync"
doc_id: "OXlPc1D9PA"
updated_at: "2023-08-11"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-system-info-sync
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 系统信息 > getSystemInfoSync
> Updated: 2023-08-11

# getSystemInfoSync

调用dd.getSystemInfoSync获取手机系统信息的同步接口。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10141) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

参数占位区域

## **示例****代码**

### 默认出入参

```
const res = dd.getSystemInfoSync();
const {
  app,
  brand,
  model,
  system,
  storage,
  version,
  language,
  paltform,
  pixelRatio,
  orientation,
  screenWidth,
  windowWidth,
  lowPowerMode,
  screenHeight,
  windowHeight,
  currentBattery,
  titleBarHeight,
  fontSizeSetting,
  isIphoneXSeries,
  statusBarHeight,
} = res;
```

返回对象示例：

```
{
  "app": "DingTalk",
  "brand": "iPhone",
  "model": "iPhone13,2",
  "system": "16.1.1",
  "storage": "119.09 GB",
  "version": "7.0.1",
  "language": "zh_CN",
  "paltform": "iOS",
  "pixelRatio": 3,
  "orientation": 0,
  "screenWidth": 390,
  "windowWidth": 390,
  "lowPowerMode": false,
  "screenHeight": 844,
  "windowHeight": 753,
  "currentBattery": "84%",
  "titleBarHeight": 44,
  "fontSizeSetting": 17,
  "isIphoneXSeries": true,
  "statusBarHeight": 47
}
```
