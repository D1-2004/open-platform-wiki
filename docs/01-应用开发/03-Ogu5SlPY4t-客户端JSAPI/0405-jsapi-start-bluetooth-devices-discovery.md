---
title: "startBluetoothDevicesDiscovery"
source_url: "https://open.dingtalk.com/document/development/jsapi-start-bluetooth-devices-discovery"
namespace: "development"
slug: "jsapi-start-bluetooth-devices-discovery"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 蓝牙 > 传统蓝牙 > startBluetoothDevicesDiscovery"
doc_id: "KUVtc8EvvM"
updated_at: "2024-12-04"
---

> Source: https://open.dingtalk.com/document/development/jsapi-start-bluetooth-devices-discovery
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 蓝牙 > 传统蓝牙 > startBluetoothDevicesDiscovery
> Updated: 2024-12-04

# startBluetoothDevicesDiscovery

调用startBluetoothDevicesDiscovery，开始搜寻附近的蓝牙外围设备。搜索结果将在onBluetoothDeviceFound事件中返回。

> 该操作比较耗费系统资源，请在搜索并连接到设备后调用stop方法停止搜索。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10176) |

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
dd.startBluetoothDevicesDiscovery({
  interval: 1000,
  services: ['00001800-0000-1000-8000-00805f9b34fb'],
  allowDuplicatesKey: true,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
