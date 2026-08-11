---
title: "compressImage"
source_url: "https://open.dingtalk.com/document/development/jsapi-compress-image"
namespace: "development"
slug: "jsapi-compress-image"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 图片 > compressImage"
doc_id: "6AKplxmF3T"
updated_at: "2023-05-19"
---

> Source: https://open.dingtalk.com/document/development/jsapi-compress-image
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 图片 > compressImage
> Updated: 2023-05-19

# compressImage

调用dd.compressImage压缩图片。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10195) |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10195) |

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
dd.compressImage({
  filePaths: ['https://resource/apmlcc0ed184daffc5a0d8da86b2f518cf7b.image'],
  compressLevel: 3,
  success: (res) => {
    const { filePaths } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "filePaths": ["https://resource/apml31fc26337c885be15b4fd1c0abefee8f.image"] }
```
