---
title: "自定义签名鉴权"
source_url: "https://open.dingtalk.com/document/connection/custom-signature-authentication-1"
namespace: "connection"
slug: "custom-signature-authentication-1"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发参考 > 鉴权设置 > 自定义签名鉴权"
doc_id: "ONQUlCxwDc"
updated_at: "2025-09-23 19:20:21"
---

> Source: https://open.dingtalk.com/document/connection/custom-signature-authentication-1
> Path: 连接平台 / 开发指南 / 开发参考 > 鉴权设置 > 自定义签名鉴权
> Updated: 2025-09-23 19:20:21

# 自定义签名鉴权

本文档主要介绍连接器自定义签名鉴权方式的设置步骤。

## **基本介绍**

自定义鉴权：指用户在请求接口时，通过填写自定义鉴权字段，然后配置鉴权参数在HTTP请求中的位置及参数值（可以通过表达式自定义加密），后续用户携带加密后的参数值请求接口，实现对用户身份的验证。

> **[!NOTE]**
>
> 使用自定义鉴权字段验证，在请求时将自定义加密后的请求参数添加到消息头，从而通过身份认证。

自定义鉴权根据自定义鉴权字段进行鉴权，在连接平台您需要进行如下几步操作：

- **选择鉴权方式**为自定义签名鉴权。
- **设置鉴权字段**，自定义鉴权字段，例如accessKeyId和accessKeySecret。
- **设置鉴权请求参数**，根据实际接口选择对应的传参方式和需要的参数。
- **鉴权验证**

  1. **设置鉴权验证接口**，支持自定义域名和连接器域名。
  2. **设置鉴权验证参数**（可选），根据实际接口选择对应的传参方式和需要的参数。
  3. 进行**鉴权验证**，测试鉴权是否通过，如果自定义鉴权字段正确，服务器则根据请求，将所请求资源发送给客户端。

## **鉴权示例**

自定义鉴权可以通过设置自定义鉴权字段以及对请求参数进行加密完成自定义鉴权设置，也可以通过此方式完成Basic Auth、APISecret、零信任网关鉴权等。本次示例通过自定义配置完成零信任网关鉴权的功能。

### **选择鉴权方式**

**选择鉴权方式**为自定义签名鉴权。

![自定义签名鉴权-选择鉴权方式](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3727980761/p534142.png)

### 设置鉴权字段

​自定义鉴权字段，填写需要的鉴权字段信息。

> **[!NOTE]**
>
> 该示例零信任网关的鉴权字段需要设置为：accessKeyId和accessKeySecret，请根据实际接口请求参数设置鉴权字段，文本类型支持密码类型，可对文本进行隐藏。

![自定义签名鉴权-设置鉴权字段](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3727980761/p534143.png)

### **设置鉴权请求参数**

​选择**HTTP Header**请求方式，添加请求接口需要的参数和设置对应的值**。**

> **[!NOTE]**
>
> 该示例中使用的是零信任网关鉴权中的请求接口，需携带x-ztna-signature-timestamp、x-ztna-accessKeyId、x-ztna-signature参数，请根据实际接口选择对应的传参方式和需要的参数。

![自定义签名鉴权-设置鉴权请求参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3727980761/p534144.png)

- **x-ztna-signature-timestamp**：签名时时间戳，通过表达式获取当前时间的时间戳。
- **x-ztna-accessKeyId**：鉴权字段accessKeyId，通过直接获取填写的鉴权字段。
- **x-ztna-signature**：加密后得到签名密钥，通过表达式完成加密，表达式如何使用，详情请参考[表达式](0011-expression-overview.md)。

  > **[!NOTE]**
  >
  > 该示例中使用的是零信任网关鉴权中的请求接口，签名密钥请参考[零信任网关鉴权](0030-zero-trust-gateway-authentication-1.md)，请根据实际接口情况设置密钥。

  ![自定义签名鉴权-设置表达鉴权请求参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3727980761/p534145.png)

### **鉴权验证**

鉴权验证，包括**设置鉴权验证接口**、**设置鉴权验证参数**（可选）、**进行鉴权验证****。**

![自定义签名鉴权-鉴权验证总览](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3727980761/p534146.png)

1. **设置鉴权验证接口**

   选择**GET**请求方式，并输入接口地址。

   > **[!NOTE]**
   >
   > 接口请求方式支持**GET**、**POST**、**PATCH**、**PUT**四种请求方式，请根据真实接口选择相应的请求方式和地址。

   ![自定义签名鉴权-设置鉴权验证接口](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3727980761/p534147.png)
2. **设置鉴权验证参数**（可选）

   选择**URL查询参数**类型，填写参数字段，选择**固定值**，并填写参数的值。

   > **[!NOTE]**
   >
   > 此项为可选项，如果请求接口需要携带额外参数，支持**HTTP Header**、**URL查询参数**、**HTTP Body**三种传参方式，请根据真实接口选择对应的方式进行参数设置。

   ![自定义签名鉴权-设置鉴权验证参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3727980761/p534148.png)

   ​鉴权验证参数值支持以下三种方式设置：

   - **固定值**：填写已知的固定值作为传参的值。
   - **鉴权字段**：引用鉴权字段中的accessKeyId或accessKeySecret。
   - **表达式**：通过表达式进行参数加密或者字符串转换等来设置值，表达式如何使用，详情请参考[表达式](0011-expression-overview.md)。
3. **进行鉴权验证**

   填写accessKeyId和accessKeySecret，单击**鉴权验证**，查看返回结果是否符合预期，最后单击**完成**。

   ![自定义签名鉴权-进行验证](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3727980761/p534149.png)

   - 返回结果，如果鉴权通过，成功返回请求接口的信息*。*

     ![自定义签名鉴权-返回结果](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3727980761/p534150.png)
   - 返回结果，如果鉴权失败，需要查看以下请求入参信息是否设置正确：

     ![自定义签名鉴权-请求入参](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3727980761/p534151.png)

     - 请求地址**url**中接口地址和需要携带**URL查询参数**是否正确。
     - 请求方式**method**是否设置正确。
     - 请求头**headers**中需要携带的参数（如：x-ztna-signature-timestamp、x-ztna-accessKeyId、x-ztna-signature）是否携带，其中x-ztna-signature是否加密正确，如何判断，请参考如下[零信任网关鉴权](0030-zero-trust-gateway-authentication-1.md)中的签名算法。

## **其他鉴权方式参考**

- **Basic Auth加密示例**：其中username的值为username，password的值为password。
  Authorization通过表达式加密使用CONCATENATE('BASIC',BASE64(CONCATENATE('username',':','password')))
- **APISecret加密示例**：其中apiSecret的值为123456789，时间戳为1670577222。
  ​x-ddpaas-signature通过表达式加密使用

  BASE64(HMACSHA256('123456789',​'1670577222'​), 'hexDecode')，它的结果是ZxG82mXCf3Z41wNXtWP159kGkeAH/GZDftu+hDbYqac=。
