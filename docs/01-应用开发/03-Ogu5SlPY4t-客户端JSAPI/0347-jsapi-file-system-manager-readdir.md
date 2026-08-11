---
title: "FileSystemManager.readdir"
source_url: "https://open.dingtalk.com/document/development/jsapi-file-system-manager-readdir"
namespace: "development"
slug: "jsapi-file-system-manager-readdir"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "文件存储 > 文件 > FileSystemManager.readdir"
doc_id: "eCSOe6dDCb"
updated_at: "2023-08-11"
---

> Source: https://open.dingtalk.com/document/development/jsapi-file-system-manager-readdir
> Path: 应用开发 / 客户端JSAPI / 文件存储 > 文件 > FileSystemManager.readdir
> Updated: 2023-08-11

# FileSystemManager.readdir

调用FileSystemManager.readdir，获取本地用户文件列表。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.5.26 | 6.5.26 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10271) |

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
const fileSystemManager = dd.getFileSystemManager();

fileSystemManager.readdir({
  dirPath: '${dd.env.USER_DATA_PATH}/newDir',
  success: (res) => {
    const { files, success } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "files": ["https://resource/43fbb13460c2c917ef7d0370d9bf09f0.file"],
  "success": true
}
```
