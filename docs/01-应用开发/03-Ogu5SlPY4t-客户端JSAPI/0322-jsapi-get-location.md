---
title: "getLocation"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-location"
namespace: "development"
slug: "jsapi-get-location"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "位置服务 > getLocation"
doc_id: "Sq9R155LMz"
updated_at: "2024-12-04"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-location
> Path: 应用开发 / 客户端JSAPI / 位置服务 > getLocation
> Updated: 2024-12-04

# getLocation

调用dd.getLocation获取用户当前的地理位置信息。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10256) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10256) |

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

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 11 | 请确认定位相关权限已开启 |
| 12 | 网络异常，请稍后再试 |
| 13 | 定位失败，请稍后再试 |
| 14 | 业务定位超时 |

## **示例****代码**

### 默认出入参

```
dd.getLocation({
  type: 1,
  useCache: true,
  coordinate: '1',
  cacheTimeout: 20,
  withReGeocode: true,
  targetAccuracy: '200',
  success: (res) => {
    const { city, address, accuracy, latitude, province, longitude } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "city": "杭州市",
  "address": "钱塘区二十四号大街353号",
  "accuracy": "200",
  "latitude": "38.963035",
  "province": "浙江省",
  "longitude": "117.451692"
}
```
