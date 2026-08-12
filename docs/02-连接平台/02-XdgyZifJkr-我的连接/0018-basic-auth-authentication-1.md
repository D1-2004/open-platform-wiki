---
title: "Basic Auth鉴权"
source_url: "https://open.dingtalk.com/document/connection/basic-auth-authentication-1"
namespace: "connection"
slug: "basic-auth-authentication-1"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发参考 > 鉴权设置 > Basic Auth鉴权"
doc_id: "T4til4gdSc"
updated_at: "2026-07-27 17:25:40"
---

> Source: https://open.dingtalk.com/document/connection/basic-auth-authentication-1
> Path: 连接平台 / 我的连接 / 开发参考 > 鉴权设置 > Basic Auth鉴权
> Updated: 2026-07-27 17:25:40

# Basic Auth鉴权

本文档主要介绍连接器Basic Auth鉴权方式的设置步骤。

## 基本介绍

Basic Auth（基本鉴权）：指用户在请求接口时，通过用户提供用户名和密码的方式，实现对用户身份的验证。

> **[!NOTE]**
>
> 使用username和password对请求进行base64编码签名，在请求时将签名信息添加到消息头，从而通过身份认证。

Basic Auth鉴权是遵守http协议实现的基本鉴权方式，在连接平台您需要进行如下几步操作：

- **选择鉴权方式**为Basic Auth。
- **设置鉴权字段**，使用username和password。
- **鉴权验证**

  1. **设置鉴权验证接口**，支持自定义域名和连接器域名。
  2. **设置鉴权验证参数**（可选），根据实际接口选择对应的传参方式和需要的参数。
  3. 进行**鉴权验证**，测试鉴权是否通过，如用户名及密码正确，服务器则根据请求，将所请求资源发送给客户端。

## **鉴权示例**

1. **选择鉴权方式**，**选择鉴权方式**为Basic Auth。

   ![Basic Auth鉴权-选择鉴权方式](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8508980761/p534119.png)
2. **设置鉴权字段**，固定使用username和password，无需设置，直接单击**下一步**。

   ![Basic Auth鉴权-设置鉴权字段](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9508980761/p534120.png)
3. 鉴权验证，包括**设置鉴权验证接口**、**设置鉴权验证参数**（可选）、进行**鉴权验证****。**

   ![Basic Auth鉴权-鉴权验证总览](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9508980761/p534121.png)
4. **设置鉴权验证接口**，选择**GET**请求方式，并输入接口地址。

   > **[!NOTE]**
   >
   > - 支持使用自定义域名和连接器域名，如果连接器没有设置接口域名变量，仅支持使用固定域名。
   > - 接口请求方式支持**GET**、**POST**、**PATCH**、**PUT**四种请求方式，请根据真实接口选择相应的请求方式和地址。

   ![Basic Auth鉴权-设置鉴权验证接口](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9508980761/p534122.png)
5. **设置鉴权验证参数**（可选），选择**URL查询参数**类型，填写参数字段，选择**固定值**，并填写参数的值。

   > **[!NOTE]**
   >
   > 此项为可选项，如果请求接口需要携带额外参数，支持**HTTP Header**、**URL查询参数**、**HTTP Body**三种传参方式，请根据真实接口选择对应的方式进行参数设置。

   ![Basic Auth鉴权-设置鉴权验证参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9508980761/p534123.png)

   鉴权验证参数值支持以下三种方式设置：

   - **固定值**：填写已知的固定值作为传参的值。
   - **鉴权字段**：引用鉴权字段中的账号名称或账号密码的值。
   - **表达式**：通过表达式进行参数加密或者字符串转换等来设置值，表达式如何使用，详情请参考[表达式](0008-expression-overview.md)。
6. **进行鉴权验证**，填写账号名称和密码，单击**鉴权验证**，查看返回结果是否符合预期，最后单击**完成**。

   > **[!NOTE]**
   >
   > 请根据真实接口输入相应的账号名称、账号密码，服务器则根据请求，将所请求资源发送给客户端。

   ![Basic Auth鉴权-进行鉴权验证](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8508980761/p534124.png)

   - 返回结果，如果鉴权通过，成功返回请求接口的信息*。*

     ![Basic Auth鉴权-验证结果](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9508980761/p534125.png)
   - 返回结果，如果鉴权失败，需要查看以下请求入参信息是否设置正确：![Basic Auth鉴权-请求入参](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9508980761/p534126.png)

     - 请求地址**url**中接口地址和需要携带**URL查询参数**是否正确。
     - 请求方式**method**是否设置正确。
     - 请求头**headers**中Basic Auth自动生成的**Authorization**是否加密正确，请参考如下[Basic Auth鉴权](#)。

## **签名算法**

如注册时提供了username和password，则收到的HTTP请求Header中包含签名相关Header：

- Authorization： <签名串>

> **[!NOTE]**
>
> 其中 <签名串> = calcSignature(username, password)。

接口提供方，应使用如下方法计算签名并验证签名串是否正确以防未授权的调用：

```
public static String calcSignature(String username, String password) {
  String basicAuth = "Basic " + Base64.getEncoder().encodeToString(
    String.format("%s:%s",
                  username,
                  password
                ).getBytes(StandardCharsets.UTF_8)
            );
  return basicAuth;
}
```
