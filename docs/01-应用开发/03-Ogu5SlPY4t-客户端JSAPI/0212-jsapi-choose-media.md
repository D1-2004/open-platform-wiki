---
title: "chooseMedia"
source_url: "https://open.dingtalk.com/document/development/jsapi-choose-media"
namespace: "development"
slug: "jsapi-choose-media"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 图片 > chooseMedia"
doc_id: "3hkZgbkAue"
updated_at: "2025-10-16"
---

> Source: https://open.dingtalk.com/document/development/jsapi-choose-media
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 图片 > chooseMedia
> Updated: 2025-10-16

# chooseMedia

媒体选择

拍摄或从手机相册中选择图片或视频。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 7.5.2 | 7.5.2 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11741) |
| 小程序 | 7.5.2 | 7.5.2 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11741) |

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

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 2 | 参数无效 |
| 3 | 系统异常 |
| -1 | 用户取消 |

## **示例****代码**

### 默认出入参

```
dd.chooseMedia({
  count: 9,
  camera: 'back',
  sizeType: 'original',
  mediaType: 'mix',
  sourceType: ['album', 'camera'],
  maxDuration: 60,
  success: (res) => {
    const { tempFiles } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "tempFiles": [
    {
      "size": 100,
      "width": 1920,
      "height": 1080,
      "duration": 60,
      "fileType": "image",
      "tempFilePath": "https://resource/29663b835195928c6aaf36d8b1ad6.image"
    }
  ]
}
```
