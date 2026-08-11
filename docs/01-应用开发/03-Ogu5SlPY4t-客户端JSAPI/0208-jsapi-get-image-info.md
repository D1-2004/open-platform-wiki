---
title: "getImageInfo"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-image-info"
namespace: "development"
slug: "jsapi-get-image-info"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 图片 > getImageInfo"
doc_id: "Qo4D5i1xCI"
updated_at: "2024-12-13"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-image-info
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 图片 > getImageInfo
> Updated: 2024-12-13

# getImageInfo

调用getImageInfo，获取图片信息。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10196) |

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
dd.getImageInfo({
  src: 'https://img.alicdn.com/tps/TB1sXGYIFXXXXc5XpXXXXXXXXXX.jpg',
  success: (res) => {
    const { path, width, height } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "path": "https://resource/a94dc111aaae9d6cc6e0bd8cbd2a34ca.file",
  "width": 200,
  "height": 200
}
```
