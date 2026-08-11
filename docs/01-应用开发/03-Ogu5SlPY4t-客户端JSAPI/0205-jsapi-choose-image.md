---
title: "chooseImage"
source_url: "https://open.dingtalk.com/document/development/jsapi-choose-image"
namespace: "development"
slug: "jsapi-choose-image"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 图片 > chooseImage"
doc_id: "IXXdEMtvrr"
updated_at: "2025-06-12"
---

> Source: https://open.dingtalk.com/document/development/jsapi-choose-image
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 图片 > chooseImage
> Updated: 2025-06-12

# chooseImage

调用chooseImage，从本地相册选择图片。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.5.35 | 6.5.35 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10194) |
| 小程序 | 6.5.35 | 6.5.35 | 7.0.0 | 6.5.35 | 6.5.35 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10194) |

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
| 11 | 在开发者后台将此域名添加到安全域名列表中。 |

## **示例****代码**

### 默认出入参

```
dd.chooseImage({
  count: 9,
  secret: false,
  position: 'back',
  sourceType: ['camera', 'album'],
  success: (res) => {
    const { files, filePaths } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "files": [
    {
      "path": "https://resource/MzNjMmEwN2FjMjg0YTBkYTI4NTdlYmJhNTI3NDhlZWU=.image",
      "size": 327622,
      "fileType": "jpg"
    },
    {
      "path": "https://resource/ZDNmODkzM2RhNWQwMWI4NzEwOGFlY2U0NzJkY2ZmZjY=.image",
      "size": 317501,
      "fileType": "jpg"
    }
  ],
  "filePaths": [
    "https://resource/MzNjMmEwN2FjMjg0YTBkYTI4NTdlYmJhNTI3NDhlZWU=.image",
    "https://resource/ZDNmODkzM2RhNWQwMWI4NzEwOGFlY2U0NzJkY2ZmZjY=.image"
  ]
}
```
