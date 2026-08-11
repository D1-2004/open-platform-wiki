---
title: "readBLECharacteristicValue"
source_url: "https://open.dingtalk.com/document/development/jsapi-read-ble-characteristic-value"
namespace: "development"
slug: "jsapi-read-ble-characteristic-value"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 蓝牙 > 低功耗蓝牙 > readBLECharacteristicValue"
doc_id: "VfyFug0Uss"
updated_at: "2024-12-04"
---

> Source: https://open.dingtalk.com/document/development/jsapi-read-ble-characteristic-value
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 蓝牙 > 低功耗蓝牙 > readBLECharacteristicValue
> Updated: 2024-12-04

# readBLECharacteristicValue

调用readBLECharacteristicValue，读取低功耗蓝牙设备特征值中的数据。调用后在onBLECharacteristicValueChange() 事件中接收数据返回。

> - 设备的特征值必须支持read才可以成功调用，具体参照 characteristic 的 properties 属性。
> - 并行多次调用读写接口存在读写失败的可能性。
> - 如果读取超时，错误码 10015，`dd.onBLECharacteristicValueChange`接口之后可能返回数据，需要接入方酌情处理。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10165) |

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
dd.readBLECharacteristicValue({
  deviceId: '0D9C82AD-1CC0-414D-9526-119E08D28124',
  serviceId: '00001800-0000-1000-8000-00805f9b34fb',
  characteristicId: '9fa480e0-4967-4542-9390-d343dc5d04ae',
  success: (res) => {
    const { value, serviceId, characteristicId } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "value": "0x26FF",
  "serviceId": "00001800-0000-1000-8000-00805f9b34fb",
  "characteristicId": "9fa480e0-4967-4542-9390-d343dc5d04ae"
}
```
