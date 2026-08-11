---
title: "uploadAttachmentToDingTalk"
source_url: "https://open.dingtalk.com/document/development/jsapi-upload-attachment-to-ding-talk"
namespace: "development"
slug: "jsapi-upload-attachment-to-ding-talk"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "文件存储 > 钉盘 > uploadAttachmentToDingTalk"
doc_id: "qyKeN7qhrB"
updated_at: "2025-06-13"
---

> Source: https://open.dingtalk.com/document/development/jsapi-upload-attachment-to-ding-talk
> Path: 应用开发 / 客户端JSAPI / 文件存储 > 钉盘 > uploadAttachmentToDingTalk
> Updated: 2025-06-13

# uploadAttachmentToDingTalk

调用uploadAttachmentToDingTalk，上传附件到钉盘，或从钉盘选择文件。

## 使用说明

> 网页应用（H5微应用）使用前，先引入钉钉 js，参考[客户端SDK](https://open.dingtalk.com/document/orgapp/webapp-read-before-development)。

此接口支持照片、拍照、本地系统文件和从已有钉盘文件选择，返回值为文件在钉盘系统内的数据信息，如spaceId、fileId等。其中照片、拍照和本地系统文件将先上传到参数spaceId指定的钉盘空间再返回，上传过程对开发者透明。

存储空间/自定义空间：调用该 jsapi 前需要先创建存储空间并授予当前用户对该空间的上传操作权限，请参考[添加空间](https://open.dingtalk.com/document/orgapp/add-space)和[添加权限](https://open.dingtalk.com/document/orgapp/add-storage-permissions)。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10318) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10318) |

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

## **示例****代码**

### 默认出入参

```
dd.uploadAttachmentToDingTalk({
  file: { max: 9, spaceId: '12345', folderId: '123' },
  image: {
    max: 9,
    spaceId: '12345',
    compress: true,
    folderId: '123',
    multiple: true,
  },
  space: {
    max: 9,
    corpId: 'ding1234xxx',
    isCopy: 1,
    spaceId: '12345',
    folderId: '123',
  },
  types: ['photo', 'camera', 'file', 'space'],
  success: (res) => {
    const { data, type } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "data": {
    "fileId": "DzzzzzzNqZY",
    "spaceId": "232323",
    "fileName": "审批流程.docx",
    "fileSize": "1024",
    "fileType": "docx"
  },
  "type": "image"
}
```
