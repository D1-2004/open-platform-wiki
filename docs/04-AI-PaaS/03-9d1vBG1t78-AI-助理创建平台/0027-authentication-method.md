---
title: "鉴权方式"
source_url: "https://open.dingtalk.com/document/aipass/authentication-method"
namespace: "aipass"
slug: "authentication-method"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 能力 > 自定义能力 > 鉴权方式"
doc_id: "mY0pqUoaEm"
updated_at: "2025-09-23 19:19:28"
---

> Source: https://open.dingtalk.com/document/aipass/authentication-method
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 能力 > 自定义能力 > 鉴权方式
> Updated: 2025-09-23 19:19:28

# 鉴权方式

本文介绍了 OpenAPI 接口权限校验的能力。

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理/助理市场创建的 AI 助理**

## **背景信息**

在开发 Actions 时，如果所提供的接口需要进行权限验证，你可以在开发过程中选择合适的权限验证方法来实现接口鉴权。钉钉 AI 自定义能力开发支持三种鉴权方式：无需认证（noAuth）、API 密钥和 OAuth。以下内容将分别介绍这三种鉴权方式及其对应的 HTTP 请求格式。

## **鉴权方式**

## **方式一：NoAuth**

采用 noAuth 方式时，你所提供的接口将不进行任何权限校验。你只需在开发过程中勾选“无权限校验”选项即可实现。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0855724071/p753924.png)

## **方式二：** API 密钥鉴权

API 密钥鉴权方式允许你通过设置固定的密钥来对接口实施权限验证。在开发 Actions 时，平台提供了三种密钥鉴权方式：Basic（基本认证）、Bearer（令牌认证）以及自定义方式。开发者可根据需要选择合适的鉴权方式进行配置。

### **Basic**

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0855724071/p753927.png)

在回调 OpenAPI 时，系统会生成一个符合下述格式的Base64编码文本，并将其通过 HTTP 请求的Authorization Header 发送。

```
base64(username:password)
```

HTTP 请求示例如下所示：

```
GET /v1/actions/example/weather
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQxMjM=
```

### **Bearer**

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0855724071/p753936.png)

使用 Bearer 方式平台在请求 OpenAPI 的时候将用户填入的 API 密钥原文放在HTTP Authorization Header中，HTTP 请求示例如下所示：

```
GET /v1/actions/example/weather
Content-Type: application/json
Accept: */*
Authorization: Bearer hello1234
```

### 自定义

自定义鉴权方式为你提供了更灵活的选择：你可以自行设定 HTTP header 的名称以及对应的 API 密钥内容。通过验证收到的请求中自定义请求头里的值是否与你预先设定的 API 密钥一致，即可完成权限的判断和校验。

例如：你填写的自定义头和 API 密钥如下所示：

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0855724071/p753937.png)

对应的 HTTP 请求示例如下所示：

```
GET /v1/actions/example/weather
X-Custom-API-Key: apikey123456
Content-Type: application/json
```

## **方式三：**OAuth 鉴权

OpenAPI 自定义能力支持标准的 [OAuth2.0 协议](https://oauth.net/2/)进行鉴权，你可以选择 OAuth 鉴权机制，并进行相应的配置以实现对接口的安全访问。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0855724071/p753941.png)

默认 Post 获取 token 的请求格式如下所示：

```
POST /auth/token HTTP/1.0
Accept: application/json
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&client_id=$client_id&client_secret=$client_secret&code=$auth_code&redirect_uri=$redirect_url
```

在 Basic 鉴权模式下获取 token，不需要将 client\_id 和 client\_secret 放置在 body 中，而应将它们按照 Base64 编码规则进行编码，并将编码后的字符串放入 HTTP 请求的 Authorization header中。具体的编码格式如下所示：

```
base64(client_id:client_secret)
```

HTTP 请求示例如下所示：

```
POST /auth/token HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Accept: application/json
Authorization: Basic ZGluZ2Z3OHBva290OWxocWM2Z2s6akI5TyoqKio0N05t

grant_type=authorization_code&code=$auth_code&redirect_uri=$redirect_url
```

授权范围：

授权范围支持多个，当多个时以英文逗号分隔，例如 Contact.User.mobile,Calendar.Event.Read

## **参考资料**

- [OAuth2.0](https://oauth.net/2/)

## **技术支持**

如果以上文档无法解决您的问题，可以通过[**自定义 AI 助理技术支持**](https://opensource.dingtalk.com/developerpedia/docs/explore/support/?via=moon-group)渠道寻求帮助。
