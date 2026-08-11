---
title: "getOperateAuthCode"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-operate-auth-code"
namespace: "development"
slug: "jsapi-get-operate-auth-code"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "获取凭证 > getOperateAuthCode"
doc_id: "W74JUsfTgo"
updated_at: "2024-12-04"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-operate-auth-code
> Path: 应用开发 / 客户端JSAPI / 获取凭证 > getOperateAuthCode
> Updated: 2024-12-04

# getOperateAuthCode

调用getOperateAuthCode，获取微应用反馈式操作的临时授权码。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11658) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11658) |

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
dd.getOperateAuthCode({
  corpId: 'ding1234xxxx',
  agentId: '2179124000',
  success: (res) => {
    const { code } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "code": "hYLK98jkf0m" }
```
