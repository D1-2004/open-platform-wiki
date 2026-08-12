---
title: "概述"
source_url: "https://open.dingtalk.com/document/connection/connection-overview"
namespace: "connection"
slug: "connection-overview"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发参考 > 鉴权设置 > 概述"
doc_id: "Tr3Ri2VEdA"
updated_at: "2025-10-20 18:33:50"
---

> Source: https://open.dingtalk.com/document/connection/connection-overview
> Path: 连接平台 / 我的连接 / 开发参考 > 鉴权设置 > 概述
> Updated: 2025-10-20 18:33:50

# 概述

本文将为您介绍简述连接器目前支持的鉴权方式。

## **什么是连接器鉴权**

连接器鉴权指的是使用连接器的执行动作向某个业务接口发起请求时，需要携带特定的身份标识信息，业务系统根据该信息来验证用户是否具备接口的访问权限，如果鉴权通过则能够正常访问请求的接口，否则访问失败。

## **连接器鉴权类型**

连接平台为用户提供了多种接口鉴权方式，包括：

| **鉴权方式** | **鉴权说明** |
| --- | --- |
| [Basic Auth鉴权](0018-basic-auth-authentication-1.md) | 用户在请求接口时，通过用户提供用户名和密码的方式，实现对用户身份的验证。 |
| [API Secret鉴权](0017-apissecret-authentication.md) | 用户在请求接口时，通过ApiSecret和时间戳对请求进行签名，实现对用户身份的验证。 |
| [零信任网关鉴权](0019-zero-trust-gateway-authentication-1.md) | 用户在请求接口时，通过accessKeyId和accessKeySecret对请求进行签名，实现对用户身份的验证。 |
| [自定义签名鉴权](0020-custom-signature-authentication-1.md) | 若以上鉴权方式不满足接口系统鉴权方式，可采用自定义鉴权。  用户在请求接口时，通过填写自定义鉴权字段，并根据字段进行自定义处理后生成新的鉴权参数，添加到HTTP请求参数中。后续用户携带加密后的参数值请求接口，实现对用户身份的验证。 |
| [Token鉴权](0021-token-authentication-1.md) | 用户在请求接口时，通过填写自定义鉴权字段，然后在指定接口验证成功后获取Token。后续用户携带Token信息请求接口，实现对用户身份的验证。 |
| [OAuth2.0鉴权](0022-oauth2-0-authentication.md) | 用户在请求接口时，通过填写自定义鉴权字段，然后访问OAuth2.0授权页面，通过后获取token。后续用户携带token请求用户授权访问受保护的资源，实现对用户身份的验证 |

除此之外，平台还提供了多种官方鉴权模板，包括：

- [钉钉开放接口鉴权](0023-dingtalk-open-interface-authentication-1.md)
- [阿里云OSS签名鉴权](0024-alibaba-cloud-oss-signature-authentication-1.md)
- [阿里云API网关AppCode鉴权](0025-apcode-authentication-for-alibaba-cloud-api-gateway-1.md)
- [阿里云API网关摘要签名鉴权](0026-alibaba-cloud-api-gateway-digest-signature-authentication-1.md)
