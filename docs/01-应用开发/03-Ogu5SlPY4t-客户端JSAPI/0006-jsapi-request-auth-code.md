---
title: "requestAuthCode"
source_url: "https://open.dingtalk.com/document/development/jsapi-request-auth-code"
namespace: "development"
slug: "jsapi-request-auth-code"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "获取凭证 > requestAuthCode"
doc_id: "KwA4BOphrD"
updated_at: "2025-06-13"
---

> Source: https://open.dingtalk.com/document/development/jsapi-request-auth-code
> Path: 应用开发 / 客户端JSAPI / 获取凭证 > requestAuthCode
> Updated: 2025-06-13

# requestAuthCode

获取微应用免登授权码

调用 requestAuthCode 获取网页应用（原 H5 微应用）免登授权码。

> - 免登是指用户进入应用后，无需输入钉钉用户名和密码，应用程序可自动获取当前用户登录系统的流程。在免登流程中需要向钉钉获取免登授权码，即是通过调用该api获取。
> - 获取的免登授权码有效期 5 分钟，且只能使用一次。

具体免登流程如下：

1. 调用本接口获取免登授权码。
2. 调用[获取应用的 Access Token](https://open.dingtalk.com/document/orgapp/api-gettoken)接口，获取应用访问凭证。
3. 调用[通过免登码获取用户信息](https://open.dingtalk.com/document/orgapp/obtain-the-userid-of-a-user-by-using-the-log-free)接口，获取用户userid。
4. 调用[查询用户详情](https://open.dingtalk.com/document/orgapp/query-user-details)接口，获取用户信息。

> 网页应用免登具体操作内容，可参考[网页应用（H5微应用）免登流程](https://open.dingtalk.com/document/orgapp/enterprise-internal-application-logon-free)，包含Demo 示例。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 7.0.45 | 7.0.45 | 7.0.0 | 7.0.50 | 7.0.50 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11723) |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 否 |

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
dd.requestAuthCode({
  corpId: 'corpid',
  clientId: 'clientid',
  onSuccess: function (result) {
    /*{
        code: 'hYLK98jkf0m' //string authCode
    }*/
  },
  onFail: function (err) {},
});
```

`success`返回对象示例：

```
{ "code": "hYLK98jkf0m" }
```
