---
title: "零信任网关鉴权"
source_url: "https://open.dingtalk.com/document/connection/zero-trust-gateway-authentication-1"
namespace: "connection"
slug: "zero-trust-gateway-authentication-1"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发参考 > 鉴权设置 > 零信任网关鉴权"
doc_id: "l1nASqmdxN"
updated_at: "2025-09-23 19:20:21"
---

> Source: https://open.dingtalk.com/document/connection/zero-trust-gateway-authentication-1
> Path: 连接平台 / 开发指南 / 开发参考 > 鉴权设置 > 零信任网关鉴权
> Updated: 2025-09-23 19:20:21

# 零信任网关鉴权

本文档主要介绍连接器零信任网关鉴权方式的设置步骤。

> **[!IMPORTANT]**
>
> 零信任网关鉴权使用，需购买[钉钉企业应用网关](https://pages.dingtalk.com/wow/z/tianyuan/default/opportunity_detail?articleCode=DDQYYYWG&channel=aggregation&spm=a2q49.26303778)产品。

## **基本介绍**

零信任网关鉴权：指用户在请求接口时，通过accessKeyId和accessKeySecret对请求进行签名，实现对用户身份的验证。其中accessKeyId是访问密钥ID，accessKeySecret是密钥。

> **[!NOTE]**
>
> 使用accessKeyId和accessKeySecret进行签名，在请求时将签名信息添加到消息头，从而通过身份认证。

零信任网关鉴权根据accessKeyId和accessKeySecret进行鉴权，在连接平台您需要进行如下几步操作：

- **选择鉴权方式**为零信任网关。
- **设置鉴权字段**，固定使用accessKeyId和accessKeySecret。
- **鉴权验证**

  - **设置鉴权验证接口**，支持自定义域名和连接器域名。
  - **设置鉴权验证参数**（可选），根据实际接口选择对应的传参方式和需要的参数。
  - 进行**鉴权验证**，测试鉴权是否通过，如果访问密钥ID和密钥正确，服务器则根据请求，将所请求资源发送给客户端。

## **鉴权示例**

### **选择鉴权方式**

**选择鉴权方式**为零信任网关。

![零信任网关鉴权-选择鉴权方式](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0277980761/p534127.png)

### **设置鉴权字段**

固定使用accessKeyId和accessKeySecret，无需设置，直接单击**下一步**。

![零信任网关鉴权-设置鉴权字段](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0277980761/p534128.png)

### **鉴权验证**

鉴权验证，包括**设置鉴权验证接口**、**设置鉴权验证参数**（可选）、进行**鉴权验证****。**

![零信任网关鉴权-鉴权验证总览](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0277980761/p534129.png)

1. **设置鉴权验证接口**

   选择**GET**请求方式，并输入接口地址。

   > **[!NOTE]**
   >
   > - 支持使用自定义域名和连接器域名，如果连接器没有设置接口域名变量，仅支持使用固定域名。
   > - 接口请求方式支持**GET**、**POST**、**PATCH**、**PUT**四种请求方式，请根据真实接口选择相应的请求方式和地址。

   ![零信任网关鉴权-设置鉴权验证接口](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0277980761/p534130.png)
2. **设置鉴权验证参数**（可选）

   选择**URL查询参数**类型，填写参数字段，选择**固定值**，并填写参数的值。

   > **[!NOTE]**
   >
   > 此项为可选项，如果请求接口需要携带额外参数，支持**HTTP Header**、**URL查询参数**、**HTTP Body**三种传参方式，请根据真实接口选择对应的方式进行参数设置。

   ![零信任网关鉴权-设置鉴权验证参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0277980761/p534131.png)

   鉴权验证参数值支持以下三种方式设置：

   - **固定值**：填写已知的固定值作为传参的值。
   - **鉴权字段**：引用鉴权字段中的accessKeyId或accessKeySecret。
   - **表达式**：通过表达式进行参数加密或者字符串转换等来设置值，表达式如何使用，详情请参考[表达式](0011-expression-overview.md)。
3. **进行鉴权验证**

   填写accessKeyId和accessKeySecret，单击**鉴权验证**，查看返回结果是否符合预期，最后单击**完成**。

   ![零信任网关鉴权-进行鉴权验证](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0277980761/p534132.png)

   - 返回结果，如果鉴权通过，成功返回请求接口的信息*。*

     ![零信任网关鉴权-返回结果](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0277980761/p534133.png)
   - 返回结果，如果鉴权失败，需要查看以下请求入参信息是否设置正确：

     ![零信任网关-请求入参](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0277980761/p534134.png)

     - 请求地址**url**中接口地址和需要携带**URL查询参数**是否正确。
     - 请求方式**method**是否设置正确。
     - 请求头**headers**中**x-ztna-accessKeyId**是否设置正确，以及自动生成的**x-ztna-signature**是否加密正确，请参考如下[零信任网关鉴权](#)。

## **签名算法**

如注册时提供了accessKeyId和accessKeySecret，则收到的HTTP请求Header中包含签名相关Header：

- x-ztna-signature-timestamp：<签名时时间戳>，毫秒值 如：1646744443533
- x-ztna-userId：<用户在当前企业的userId>，不同于uid。非必传，零信任网关用于做审计，后续可能会用此字段做安全策略校验
- x-ztna-signature： <签名串>

  > **[!NOTE]**
  >
  > 其中 <签名串> = sign(accessKeyId, accessKeySecret, host, userId, <签名时时间戳>)，accessKeyId是注册时指定的访问密钥Id，accessKeySecret是注册时指定的签名密钥。

接口提供方，应使用如下方法计算签名并验证签名串是否正确以防未鉴权的调用：

```
import org.apache.commons.lang3.StringUtils;

import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

public class SignUtils {

    /**
     * 计算签名
     *
     * @param accessKeyId
     * @param accessKeySecret
     * @param host，如果有端口也要带上
     * @param userId 用户在当前企业的userid，不同于uid
     * @param timestamp，生成签名的时间戳，重试要重新生成
     * @return 签名值
     */
    public static String sign(String accessKeyId, String accessKeySecret, String host, String userId,
        long timestamp) {
        try {
            Charset charset = StandardCharsets.UTF_8;
            Mac mac = Mac.getInstance("HmacSHA256");
            SecretKeySpec key = new SecretKeySpec(accessKeySecret.getBytes(charset), "HmacSHA256");
            mac.init(key);
            return Base64.getEncoder().encodeToString(
                    mac.doFinal((accessKeyId + host + StringUtils.defaultIfBlank(userId, "") + timestamp).getBytes(charset)));
        } catch (NoSuchAlgorithmException | InvalidKeyException e) {
            logger.warn("sign fail. " + e.getMessage(), e);
            return null;
        }
    }

    public static void main(String[] args) {
        long ts = System.currentTimeMillis();
        String userId = "145213";
        String accessKeyId = "<accesskeyid>";
        String sign = SignUtils.sign("<accesskeyid>", "<accesskeysecret>", "127-0-0-18000-6z7yucaoh14w.pregw.ztna-dingtalk.com", userId, ts);
        System.out.println("x-ztna-signature-timestamp: " + ts);
        System.out.println("x-ztna-userId: " + userId);
        System.out.println("x-ztna-accessKeyId: " + accessKeyId);
        System.out.println("x-ztna-signature: " + sign);
    }
}
```

输出结果：

```
x-ztna-signature-timestamp: 1647486145840
x-ztna-userId: 145213
x-ztna-accessKeyId: <accesskeyid>
x-ztna-signature: NWX2zBghUy8M5lUN3Z599uQcI6Vmo61+dCZAOsCZdO0=
```
