---
title: "quickCallList"
source_url: "https://open.dingtalk.com/document/development/jsapi-quick-call-list"
namespace: "development"
slug: "jsapi-quick-call-list"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "办公电话 > quickCallList"
doc_id: "nKejTRvvUl"
updated_at: "2023-08-08"
---

> Source: https://open.dingtalk.com/document/development/jsapi-quick-call-list
> Path: 应用开发 / 客户端JSAPI / 办公电话 > quickCallList
> Updated: 2023-08-08

# quickCallList

调用quickCallList，拨打单人电话选项。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 不支持 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11652) |
| 小程序 | 6.0.0 | 不支持 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11652) |

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
dd.quickCallList({
  title: '测试电话',
  corpId: 'ding1234xxxx',
  content: '推荐使用办公电话',
  staffId: '03432',
  typeList: [1, 2],
  phoneNumber: '155xxxxxxxx',
  success: (res) => {
    const { callId, callType, callTypeList } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "callId": "xijdnxxxxx", "callType": -1, "callTypeList": [1, 2] }
```
