---
title: "chooseVideo"
source_url: "https://open.dingtalk.com/document/development/jsapi-choose-video"
namespace: "development"
slug: "jsapi-choose-video"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 视频 > chooseVideo"
doc_id: "BFB8eml1Zu"
updated_at: "2024-11-08"
---

> Source: https://open.dingtalk.com/document/development/jsapi-choose-video
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 视频 > chooseVideo
> Updated: 2024-11-08

# chooseVideo

调用chooseVideo，拍摄视频或从手机相册中选视频。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 7.0.55 | 7.0.55 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10208) |

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
dd.chooseVideo({
  sourceType: ['album', 'camera'],
  maxDuration: 60,
  compressed: true,
  success: (res) => {
    console.log(res);
  },
  fail: (err) => {
    console.log(err);
  },
});
```

`success`返回对象示例：

```
{
  "size": 12334,
  "width": 200,
  "height": 200,
  "duration": 40,
  "filePath": "https://resource/apml31fc26337c885be15b4fd1c0abefee8f.video"
}
```
