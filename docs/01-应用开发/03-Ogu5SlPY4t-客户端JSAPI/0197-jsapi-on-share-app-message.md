---
title: "onShareAppMessage"
source_url: "https://open.dingtalk.com/document/development/jsapi-on-share-app-message"
namespace: "development"
slug: "jsapi-on-share-app-message"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 分享 > onShareAppMessage"
doc_id: "RJXuSrJiv7"
updated_at: "2023-11-13"
---

> Source: https://open.dingtalk.com/document/development/jsapi-on-share-app-message
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 分享 > onShareAppMessage
> Updated: 2023-11-13

# onShareAppMessage

在Page中定义onShareAppMessage函数，用来自定义该页面的分享内容。此时该页面右上角菜单中会显示分享按钮，反之不显示。

用户点击分享按钮时才会调用此事件。
此事件需要return一个Object，用于自定义分享内容。

扫码体验
![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3654199951/p163583.png)
分享卡片规范
![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8162814361/p338530.png)

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| H5 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10021) |

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
Page({
  onShareAppMessage() {
    return {
      title: '小程序示例',
      desc: '小程序官方示例Demo，展示已支持的接口能力及组件。',
      path: 'page/component/component-pages/view/view?param=123',
    };
  },
});
```
