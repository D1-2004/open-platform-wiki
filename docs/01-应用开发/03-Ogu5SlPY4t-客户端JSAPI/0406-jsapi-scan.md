---
title: "scan"
source_url: "https://open.dingtalk.com/document/development/jsapi-scan"
namespace: "development"
slug: "jsapi-scan"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 扫码 > scan"
doc_id: "NGuySAjiGl"
updated_at: "2025-08-06"
---

> Source: https://open.dingtalk.com/document/development/jsapi-scan
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 扫码 > scan
> Updated: 2025-08-06

# scan

调用dd.scan使用扫一扫功能。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10160) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10160) |

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
dd.scan({
  type: 'qr',
  source: 'camera',
  success: (res) => {
    const { text } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "text": "我是躲在二维码背后的数据" }
```
