---
title: "配置事件推送方式"
source_url: "https://open.dingtalk.com/document/development/configure-stream-push"
namespace: "development"
slug: "configure-stream-push"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "开发指南 > 配置事件推送方式"
doc_id: "VSoTXnLPgh"
updated_at: "2026-06-08 09:20:33"
---

> Source: https://open.dingtalk.com/document/development/configure-stream-push
> Path: 应用开发 / 事件订阅 / 开发指南 > 配置事件推送方式
> Updated: 2026-06-08 09:20:33

# 配置事件推送方式

如果你需要配置 Stream推送方式、SyncHTTP推送方式或HTTP事件推送方式，可以参考本文档操作步骤完成接入。

## **配置 Stream 推送（推荐）**

### **前提条件**

1. 拥有所在钉钉组织开发者后台的[开发者权限](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 拥有所在钉钉组织的[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

### **操作步骤**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击目标应用，进入应用详情页。
2. 单击**开发配置** > **事件订阅，**选择 **Stream 模式推送**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3361880871/p1077947.png)
3. 参照[开发 Stream 模式推送服务端（推荐）](0004-develop-stream-mode-push-server.md#7c157d52c89et)文档，完成服务端开发。
4. 服务端开发完成后，单击**已完成接入，验证连接通道**。
5. 单击**保存**。保存完成后，事件订阅列表才会展示。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7945080071/p737643.png)

## **配置 HTTP 推送（不推荐）**

### **前提条件**

1. 拥有公网可访问的请求网址。
2. 拥有所在钉钉组织开发者后台的[开发者权限](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
3. 拥有所在钉钉组织的[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

### **操作步骤**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击目标应用，进入应用详情页。
2. 单击**开发配置** > **事件订阅，**选择 **HTTP 推送**。
3. 配置 HTTP 信息：

   | **配置项** | **描述** |
   | --- | --- |
   | **加密 aes\_key** | 回调消息内容的加解密参数，是AES密钥的Base64编码。 |
   | **签名 token** | 钉钉每次向你的地址推送事件数据时都会携带`token`，用于生成签名、校验回调请求的合法性。必须为英文或数字，长度为3~32个字符 |
   | **请求网址** | 用于接收事件订阅请求的URL。当应用订阅的事件触发时，钉钉会向该网址发送相应的 HTTP POST 请求。 |
4. 配置完成后，你需要开发事件订阅服务端。详情参考[开发 HTTP 推送服务端](0004-develop-stream-mode-push-server.md#6d7a5d60ddwgj)。
5. 服务端开发完成后，需要 HTTP 推送服务端启动，你需要单击**保存**。保存完成后，事件订阅列表才会展示。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9545080071/p737446.png)

### **常见问题**

#### **页面报错“HTTP请求结果校验返回字段值失败”**

- 原因：

  - 返回给钉钉服务器的json信息中有其中一个字段值不正确。
  - 返回给钉钉服务器的信息不是json格式。
- 解决方案：

  > **[!NOTE]**
  >
  > 需校验[开发 HTTP 推送服务端](0004-develop-stream-mode-push-server.md#6d7a5d60ddwgj) 内容是否正确。

  构造main方法，使用回调地址返回的四个字段值，调用加密接口，验证得到的值是否为success字符串，例如：

  ```
  //构造加解密类，使用的参数不变
  DingTalkEncryptor dingTalkEncryptor = new DingTalkEncryptor("123456", "1234567890123456789012345678901234567890123", "dingsnotzck6pm5veliw");
  //加密方法内传你的回调地址返回给钉钉服务器的四个参数
  String result = dingTalkEncryptor.getDecryptMsg("9a95a004dd16f5c307e849b994173f76aa26e5eb", "1614767836", "A7Co0cJLMzIDtMMI", "YvkvaGe4hQxd3VxRmEty0dVlnCOAqwf56xwTRHDHoOURqhalbmBJQk5FNcRk42Gl5T0YQXZNwpwWSm1xAFJ5ZA==");
  System.out.println(result);
  ```

  此时的运行结果如下：

  - 如果得到了success字符串，说明返回的值没有问题，问题出现在回调接口返回给钉钉服务器的值参数格式不对，需要再次确认。
  - 如果运行出现报错，常见运行报错和原因如下：

    | **错误** | **原因** | **调整方式** |
    | --- | --- | --- |
    | 计算解密文字corpid不匹配 | DingTalkEncryptor中`OWNER_KEY`参数错误。 | 当前开发者后台应用上的事件订阅，`owner_key`需要传当前应用的appkey值。 |
    | 不合法的aes key | DingTalkEncryptor中`ENCODING_AES_KEY`参数错误。 | `ENCODING_AES_KEY`自定义的固定43位字符串，只支持大小写字母和数字。 |
    | 签名计算失败 | 解密方法中的参数使用有问题。 | 解密方法getEncryptedMap内的四个参数都来自钉钉服务器请求时带来的值。 |

    ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9545080071/p741380.png)

## **配置 SyncHTTP 推送（不推荐）**

### **前提条件**

1. 拥有公网可访问的请求地址。
2. 拥有所在钉钉组织开发者后台的[开发者权限](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
3. 拥有所在钉钉组织的[第三方企业应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

### **操作步骤**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击目标应用，进入应用详情页。
2. 单击**开发配置** > **事件订阅，**选择 **使用 SyncHTTP 推送**。
3. 配置 SyncHTTP 信息：

   | **配置项** | **描述** |
   | --- | --- |
   | 加密 Aes\_key | 回调消息内容的加解密参数，是AES密钥的Base64编码。 |
   | 签名 Token | 钉钉每次向你的地址推送事件数据时都会携带`token`，用于生成签名、校验回调请求的合法性。必须为英文或数字，长度为3~32个字符 |
   | 回调请求地址 | 用于接收事件订阅请求的URL。当应用订阅的事件触发时，钉钉会向该网址发送相应的 HTTP POST 请求，接收事件回调的 URL，必须是公网可以访问的 url 地址。 |
4. 配置完成后，你需要开发事件订阅服务端。详情参考[开发 SyncHTTP 推送服务端](https://open.dingtalk.com/document/isvapp/develop-synchttp-push-server)。
5. 服务端开发完成后，需要 SyncHTTP 推送服务端启动，你需要单击**保存**。保存完成后，就可以添加订阅了。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2964682071/p745892.png)
