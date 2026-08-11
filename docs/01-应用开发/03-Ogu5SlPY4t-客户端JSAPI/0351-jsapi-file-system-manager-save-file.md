---
title: "FileSystemManager.saveFile"
source_url: "https://open.dingtalk.com/document/development/jsapi-file-system-manager-save-file"
namespace: "development"
slug: "jsapi-file-system-manager-save-file"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "文件存储 > 文件 > FileSystemManager.saveFile"
doc_id: "bFKx8jMFbA"
updated_at: "2023-08-08"
---

> Source: https://open.dingtalk.com/document/development/jsapi-file-system-manager-save-file
> Path: 应用开发 / 客户端JSAPI / 文件存储 > 文件 > FileSystemManager.saveFile
> Updated: 2023-08-08

# FileSystemManager.saveFile

调用FileSystemManager.saveFile，将本地临时文件保存为本地缓存文件或本地用户文件。

> 本接口会移动临时文件，因此调用成功后，本地临时路径的tempFilePath将不可用。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.5.26 | 6.5.26 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10275) |

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
| 10022 | filePath指定的文件路径错误。 |
| 3 | 文件读取未知错误。 |

## **示例****代码**

### 默认出入参

```
const fileSystemManager = dd.getFileSystemManager();

fileSystemManager.saveFile({
  filePath: '${dd.env.USER_DATA_PATH}/newDir/img.png',
  tempFilePath: '**',
  success: (res) => {
    const { savedFilePath } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "savedFilePath": "***" }
```
