---
title: "getDingerDeviceStatus"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-dinger-device-status"
namespace: "development"
slug: "jsapi-get-dinger-device-status"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "DingTalk A1 > getDingerDeviceStatus"
doc_id: "sFlQ1KxPOl"
updated_at: "2026-02-12"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-dinger-device-status
> Path: 应用开发 / 客户端JSAPI / DingTalk A1 > getDingerDeviceStatus
> Updated: 2026-02-12

# getDingerDeviceStatus

查询 DingTalk A1 设备状态

查询 DingTalk A1 设备状态

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 8.2.15 | 8.2.15 | 8.0.28 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11939) |
| 小程序 | 8.2.15 | 8.2.15 | 8.0.28 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11939) |

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

### 默认Demo标题

```
dd.getDingerDeviceStatus({
  deviceId: '123456',
  success: (res) => {
    const {
      device_status,
      audio_status,
      fid,
      duration,
      battery_percent,
      storage_total_size,
      storage_remain,
      version,
      accountId,
      accountType,
      occupyOperation,
      deviceName,
      bleStatus,
      bleName,
      sn,
      deviceId,
    } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "sn": "xxx",
  "fid": "12345",
  "bleName": "DingTalk A1",
  "version": "xxx",
  "deviceId": "12345",
  "duration": 12345,
  "accountId": "0",
  "bleStatus": true,
  "deviceName": "DingTalk A1",
  "accountType": 0,
  "audio_status": "idle",
  "device_status": 0,
  "storage_remain": "0",
  "battery_percent": 2,
  "occupyOperation": "xxx",
  "storage_total_size": "0"
}
```
