---
title: "getBLEDeviceCharacteristics"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-ble-device-characteristics"
namespace: "development"
slug: "jsapi-get-ble-device-characteristics"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 蓝牙 > 低功耗蓝牙 > getBLEDeviceCharacteristics"
doc_id: "PjXMe4BJtt"
updated_at: "2024-12-04"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-ble-device-characteristics
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 蓝牙 > 低功耗蓝牙 > getBLEDeviceCharacteristics
> Updated: 2024-12-04

# getBLEDeviceCharacteristics

调用getBLEDeviceCharacteristics，获取蓝牙设备所有特征值。

> 建立连接后先执行`dd.getBLEDeviceServices`与`dd.getBLEDeviceCharacteristics`后再进行与蓝牙设备的数据交互。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10168) |

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
dd.getBLEDeviceCharacteristics({
  deviceId: '0D9C82AD-1CC0-414D-9526-119E08D28124',
  serviceId: '00001800-0000-1000-8000-00805f9b34fb',
  success: (res) => {
    const { characteristics } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "characteristics": [
    {
      "value": "0x26FF",
      "serviceId": "00001800-0000-1000-8000-00805f9b34fb",
      "properties": {
        "read": true,
        "write": true,
        "notify": true,
        "indicate": true
      },
      "characteristicId": "9fa480e0-4967-4542-9390-d343dc5d04ae"
    }
  ]
}
```
