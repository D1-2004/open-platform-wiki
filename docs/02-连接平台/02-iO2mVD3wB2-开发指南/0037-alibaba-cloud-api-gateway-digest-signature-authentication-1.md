---
title: "阿里云API网关摘要签名鉴权"
source_url: "https://open.dingtalk.com/document/connection/alibaba-cloud-api-gateway-digest-signature-authentication-1"
namespace: "connection"
slug: "alibaba-cloud-api-gateway-digest-signature-authentication-1"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发参考 > 鉴权设置 > 阿里云API网关摘要签名鉴权"
doc_id: "eO9dNUw7i8"
updated_at: "2025-09-23 19:20:25"
---

> Source: https://open.dingtalk.com/document/connection/alibaba-cloud-api-gateway-digest-signature-authentication-1
> Path: 连接平台 / 开发指南 / 开发参考 > 鉴权设置 > 阿里云API网关摘要签名鉴权
> Updated: 2025-09-23 19:20:25

# 阿里云API网关摘要签名鉴权

> **[!IMPORTANT]**
>
> 本文鉴权使用摘要签名认证方式调用阿里云API网关，详细可参考[阿里云使用摘要签名认证方式调用API](https://help.aliyun.com/document_detail/29475.html?spm=a2c4g.29464.0.0.2fe2b752P79zSm)官方文档。

## **简介**

API网关摘要签名认证，需要使用签名密钥对请求内容进行签名计算，并将签名同步传输给服务器端进行签名验证。API网关提供的SDK内置了签名实现，只需要将签名密钥配置在SDK中，即可实现发起携带正确签名的请求。

## **准备工作**

- 拥有所在钉钉组织开发者后台的[开发者权限](https://open.dingtalk.com/document/dingstart/dingtalk-developer)。
- 拥有一个所在钉钉组织连接平台的[连接器](0013-create-connector.md)。
- 拥有一个[阿里云API网关应用](https://apigateway.console.aliyun.com/?spm=5176.8465980.top-nav.22.432e1450nEHDnz&accounttraceid=59d7a2cdbc244dce96d55203fa295c49mgvw#/cn-hangzhou/apps/list?AppName=)并查询应用AppKey和AppSecret。

  ![应用Appkey..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7951065861/p677224.png)

## **鉴权设置**

1. 单击鉴权设置：

   **选择鉴权方式：**自定义签名鉴权。

   ![鉴权方式选择- API网关..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9751065861/p676816.png)
2. **设置鉴权字段，**并单击**下一步**：

   ![设置鉴权字段-摘要签名..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7951065861/p677225.png)
3. **设置鉴权请求参数，**并单击**保存配置并调试**。

   **HTTP请求头：**

   - **x-ca-key：**阿里云API网关鉴权的AppKey，会作为鉴权字段传入，因此这里类型选择“鉴权字段”并选中“阿里云API网关的appKey”。

     ![key..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7951065861/p677230.png)
   - **x-ca-timestamp：**时间戳，这里类型选择“表达式”，进行获取当前时间戳的表达式配置。

     ![时间戳设置..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7951065861/p677227.png)
   - **x-ca-nonce**：主要用于防止重放攻击，这里类型选择“表达式”，进行UUID的表达式配置。

     ![uuid..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7951065861/p677228.png)
   - **x-ca-signature-method**：鉴权使用的加密算法，因为我们使用HmacSHA256的加密算法，所以这里类型选择“固定值”，值写入：`HmacSHA256`。

     ![menthod..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7951065861/p677229.png)
   - **x-ca-signature**：由于签名需要对包括运行时的入参进行排序等操作后再进行加密计算，因此这里使用Python脚本去实现。类型选择“Python脚本”。

     ![Python-参数鉴权..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7951065861/p677231.png)

     ```
     import datetime
     import uuid
     import hashlib
     import hmac
     import base64
     import urllib.parse
     from urllib.parse import urlparse, parse_qsl , unquote, unquote_plus

     def generate_x_ca_signature(appKey, appSecret):
         parsed_url = urlparse(url)
         path = parsed_url.path
         query = parsed_url.query
         header_keys = list(headers.keys())
         header_keys.sort()
         header_values = []
         for key in header_keys:
             header_values.append(headers[key])
         sign_message = '\n'.join([method.upper(), accept, '', contentType, '']) + '\n'
         headers_str = ""
         for key in header_keys:
             if key in ['x-ca-timestamp','x-ca-nonce','x-ca-key','x-ca-signature-method']:
                 headers_str = f"{headers_str}{key}:{headers[key]}\n"
         sign_message = f"{sign_message}{headers_str}"
         # query是经过urlencode过的，这里需要进行urldecode的处理，并且处理过程中+会变为空格，最后还需要进行一次替换处理
         sorted_query = ""
         if query:
             decoded_query = unquote(query)
             parse_query = parse_qsl(decoded_query)
             params = {}
             for key, value in parse_query:
                 if key not in params:
                     params[key] = value
             for key, value in params.items():
                 params[key] = value
             # 按照字典排序
             sorted_dict = sorted(params.items())
             sorted_query = '&'.join([f"{k}={v}" for k, v in sorted_dict])
         path_and_parameters = path + ("" if sorted_query == "" else ("?" + sorted_query.replace(' ', '+')))
         sign_message = f"{sign_message}{path_and_parameters}"
         signature = hmac.new(appSecret.encode(), sign_message.encode(), hashlib.sha256).digest()
         signature = base64.b64encode(signature).decode()
         return signature

     signature = generate_x_ca_signature(authFields.get('appKey'), authFields.get('appSecret'))
     return signature
     ```
4. 鉴权调试：

   1. 设置鉴权调试接口：

      ![设置调试接口..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8851065861/p677132.png)
   2. 设置鉴权调试参数：

      ![设置调试参数..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8851065861/p677135.png)
   3. 添加账户：

      ![添加账户..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8851065861/p677137.png)
   4. 单击**鉴权调试，**查看调试结果：

      ![单击调试..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7951065861/p677233.png)
   5. 单击**完成调试**，实现保存。

      ![完成调试并保存-1..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7951065861/p677234.png)
