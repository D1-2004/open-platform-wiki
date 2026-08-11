---
title: "getSystemSettings"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-system-settings"
namespace: "development"
slug: "jsapi-get-system-settings"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 系统信息 > getSystemSettings"
doc_id: "rbk6wZ0nO0"
updated_at: "2024-12-04"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-system-settings
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 系统信息 > getSystemSettings
> Updated: 2024-12-04

# getSystemSettings

调用getSystemSettings，打开系统设置。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 4.6.36 | 6.3.15 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11671) |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |

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
dd.getSystemSettings({
  data: 'data param',
  param: '"extended data',
  action: 'android.settings.BLUETOOTH_SETTINGS',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
