---
title: "API Secret鉴权"
source_url: "https://open.dingtalk.com/document/connection/apissecret-authentication"
namespace: "connection"
slug: "apissecret-authentication"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发参考 > 鉴权设置 > API Secret鉴权"
doc_id: "MDJeI4fnWL"
updated_at: "2026-07-27 17:25:38"
---

> Source: https://open.dingtalk.com/document/connection/apissecret-authentication
> Path: 连接平台 / 我的连接 / 开发参考 > 鉴权设置 > API Secret鉴权
> Updated: 2026-07-27 17:25:38

# API Secret鉴权

本文档主要介绍连接器API Secret鉴权方式的设置步骤。

## **基本介绍**

APISecret：指用户在请求接口时，通过ApiSecret和时间戳对请求进行签名，实现对用户身份的验证。其中apiSecret是Api的私钥。

> **[!NOTE]**
>
> 使用ApiSecret进行签名，在请求时将签名信息添加到消息头，从而通过身份认证。

APISecret鉴权根据请求接口的ApiSecret以及当前的时间戳进行鉴权，在连接平台您需要进行如下几步操作：

- **选择鉴权方式**为APISecret**。**
- **设置APISecret字段**，固定使用Api的私钥（apiSecret）
- **鉴权验证**

  1. **设置鉴权验证接口**，支持自定义域名和连接器域名。
  2. **设置鉴权验证参数**（可选），根据实际接口选择对应的传参方式和需要的参数。
  3. 进行**鉴权验证**，测试鉴权是否通过，如果Api的私钥正确，服务器则根据请求，将所请求资源发送给客户端。

## **鉴权示例**

1. **选择鉴权方式，****选择鉴权方式**为APISecret**。**

   ![APISecret鉴权-选择鉴权方式](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0438980761/p534101.png)
2. **设置APISecret字段**，固定使用Api的私钥（apiSecret），填写APISecret值。

   ![APISecret鉴权-设置鉴权字段](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0438980761/p534102.png)
3. 鉴权验证，包括**设置鉴权验证接口**、**设置鉴权验证参数**（可选）、进行**鉴权验证****。**

   ![APISecret鉴权-鉴权验证总览](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0438980761/p534103.png)
4. **设置鉴权验证接口**，选择**GET**请求方式，并输入接口地址。

   > **[!NOTE]**
   >
   > - 支持使用自定义域名和连接器域名，如果连接器没有设置接口域名变量，仅支持使用固定域名。
   > - 接口请求方式支持**GET**、**POST**、**PATCH**、**PUT**四种请求方式，请根据真实接口选择相应的请求方式和地址。

   ![APISecret鉴权-设置鉴权验证接口](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0438980761/p534104.png)
5. **设置鉴权验证参数**（可选），选择**URL查询参数**类型，填写参数字段，选择**固定值**，并填写参数的值。

   > **[!NOTE]**
   >
   > 此项为可选项，如果请求接口需要携带额外参数，支持**HTTP Header**、**URL查询参数**、**HTTP Body**三种传参方式，请根据真实接口选择对应的方式进行参数设置

   ![APISecret鉴权-设置鉴权验证参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0438980761/p534105.png)

   鉴权验证参数值支持以下两种方式设置：

   - **固定值：**填写已知的固定值作为传参的值。
   - **表达式**：通过表达式进行参数加密或者字符串转换等来设置值，表达式如何使用，详情请参考[表达式](0008-expression-overview.md)。
6. **进行鉴权验证，**单击**鉴权验证**，查看返回结果是否符合预期，最后单击**完成**。

   ![APISecret鉴权-进行鉴权验证](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0438980761/p534106.png)

   - 返回结果，如果鉴权通过，成功返回请求接口的信息*。*

     ![APISecret鉴权-成功返回结果](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0438980761/p534107.png)
   - 返回结果，如果鉴权失败，需要查看以下请求入参信息是否设置正确：![APISecret鉴权-失败请求入参](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0438980761/p534109.png)

     - 请求地址**url**中接口地址和需要携带**URL查询参数**是否正确。
     - 请求方式**method**是否设置正确。
     - 请求头**headers**中自动生成的**x-ddpaas-signature**是否加密正确，请参考如下[API Secret鉴权](#)。

## **签名算法**

如注册时提供了apiSecret，则收到的HTTP请求Header中包含签名相关Header：

- x-ddpaas-signature-timestamp：<签名时时间戳>
- x-ddpaas-signature：<签名串>

> **[!NOTE]**
>
> 其中 <签名串> = calcSignature(apiSecret, <签名时时间戳>)，apiSecret是注册时指定的签名密钥。

接口提供方，应使用如下方法计算签名并验证签名串是否正确以防未授权的调用：

```
public static String calcSignature(String apiSecret, long ts) {
    try {
        Mac mac = Mac.getInstance("HmacSHA256");
        SecretKeySpec key = new SecretKeySpec(apiSecret.getBytes(), "HmacSHA256");
        mac.init(key);
        return Base64.getEncoder()
            .encodeToString(mac.doFinal(Long.toString(ts).getBytes()));
    } catch (NoSuchAlgorithmException | InvalidKeyException e) {
        log.error("sign api secret failed", e);
    }
}
```
