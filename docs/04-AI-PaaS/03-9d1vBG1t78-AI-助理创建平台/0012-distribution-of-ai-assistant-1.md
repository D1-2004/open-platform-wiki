---
title: "分发 AI 助理"
source_url: "https://open.dingtalk.com/document/aipass/distribution-of-ai-assistant-1"
namespace: "aipass"
slug: "distribution-of-ai-assistant-1"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "分发 AI 助理 > 分发 AI 助理"
doc_id: "oe8QVy8Y35"
updated_at: "2025-09-23 19:19:13"
---

> Source: https://open.dingtalk.com/document/aipass/distribution-of-ai-assistant-1
> Path: AI PaaS / AI 助理创建平台 / 分发 AI 助理 > 分发 AI 助理
> Updated: 2025-09-23 19:19:13

# 分发 AI 助理

本文介绍了如何将在钉钉中搭建的 AI 助理发布到网页、微信公众号（服务号）、微信公众号（订阅号）和微信小程序（H5嵌入）。

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理**

## **前提条件**

- 已经完成配置 AI 助理，详情参考[创建组织内使用的 AI 助理](0005-create-a-dingtalk-ai-assistant-1.md)。
- 如需要发布到微信服务号，需要提前创建微信服务号，且**已经完成了认证**。未认证和认证中的微信服务号无法接收消息。
- 如需发布到微信订阅号，需要提前创建微信订阅号。
- 如需发布到微信小程序，已经注册了微信小程序号，并完成了以下操作：

  - 登记主体信息，主体类型为**个人****以外**的其他类型。
  - 填写微信小程序基本信息（名字、头像、描述等）。
  - 设置微信小程序服务类目。
  > 详细说明可参考[微信开放平台文档](https://developers.weixin.qq.com/miniprogram/introduction/)。

  - 已完成了微信小程序备案，备案流程可参考[微信开放平台文档](https://developers.weixin.qq.com/miniprogram/product/record/record_guidelines.html)。

## **发布成网页**

### **使用限制**

- 部分功能可能受限（如语音播报等），我们正在筹备中。

### **在钉钉客户端中配置并发布 AI 助理**

1. [AI 助理配置](0005-create-a-dingtalk-ai-assistant-1.md)完成后，单击右上角**发布**按钮，进入 AI 助理发布页面。
2. 在 AI 助理发布页面，打开网页公开访问开关，
3. 选择嵌入方式。目前支持2种嵌入方式，按需选择适合的方式：

   1. **网页内嵌。**
   2. **悬浮球嵌入。**
4. 选择登录方式。目前支持3种登录方式，按需选择适合的方式。

   1. **无需登录，直接使用**。
   2. **手机验证码登录**。
   3. **外部账号登录。**
5. 直接将代码粘贴到网页的 <body> 区域中。你也可以按需调整样式。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7814216271/p845451.png)
6. 发布成功后，你可以在自己的系统中的网页中和钉钉AI助理对话。

> **[!NOTE]**
>
> 你的网页需要支持https协议，否则无法使用。

### **投放链接参数**

投放链接格式：https://agent.dingtalk.com/copilot?code=\*\*\*&channel=${请输入channel}&accountToken=${请输入accountToken}

| **参数** | **类型** | **描述** |
| --- | --- | --- |
| code | string | 助理投放标识。 |
| channel | string | 来源标识。   - 非必填。 - 长度不超过10个字符，若存在特殊字符，需要进行URL Encoding。 - 此值为开发者自定义，用于标识在哪个场景使用AI助理。 |
| accountToken | string | 账号token：   - 当登录方式为“外部账号登录”时，此参数必传；其他登录方式不需要传此值。 - 若存在特殊字符，需要进行URL Encoding。 - 该字段的值需要由用户自定义，以便后续在 Stream 服务中接收并解析。 |

### **JSSDK参数配置**

| **参数** | **类型** | **描述** |
| --- | --- | --- |
| code | string | 助理投放标识。 |
| channel | string | 来源标识：   - 非必填。 - 长度不超过10个字符，若存在特殊字符，需要进行URL Encoding。 - 此值为开发者自定义，用于标识在哪个场景使用AI助理。 |
| accountToken | string | 账号token：   - 当登录方式为“外部账号登录”时，此参数必传；其他登录方式不需要传此值。 - 若存在特殊字符，需要进行URL Encoding。 - 该字段的值需要由用户自定义，以便后续在 Stream 服务中接收并解析。 |
| orbIcon | string | 悬浮球图标cdn地址：   - 非必填 - 若需要自定义悬浮球图标，则需要传入此参数。 |

### **外部账号登录接入流程**

**运行时流程图**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7814216271/p844956.png)

**接入步骤**

1. 发布AI助理时选择“外部账号登录”方式。
2. 提供stream回调接口，用于在运行时基于accountToken校验并解析外部用户账号。

   - stream回调接口接入流程可参考：[服务端Stream模式](https://open.dingtalk.com/document/development/introduction-to-stream-mode)
   - 示例代码：

     > **[!NOTE]**
     >
     > stream回调所需的clientId、clientSecret参数，请参考[AI 助理常见问题](0097-faq-2.md)。

     ```
     public static void main(String[] args) throws Exception {
             OpenDingTalkStreamClientBuilder
                     .custom()
                     .credential(new AuthClientCredential("${clientId}", "${clientSecret}"))
                     //注册“外部账号token解析回调”监听器
                     .registerCallbackListener("/v1.0/aiAssistant/delivery/externalAccount/callback", new OpenDingTalkCallbackListener<JSONObject, JSONObject>() {
                         @Override
                         public JSONObject execute(JSONObject params) {
                             String agentCode = params.getString("agentCode");
                             String accountToken = params.getString("accountToken");
                             // 进行业务逻辑处理，校验accountToken是否合法，并解析出对应的账号 
                             // ...
                             JSONObject result = new JSONObject();
                             result.put("resultCode", "200");
                             result.put("account", "${请输入account}");
                             result.put("message", "${请输入提示信息}");
                             return result;
                         }

                     })
                     .build().start();
     }
     ```

     接口入参
   - | **参数** | **类型** | **描述** |
     | --- | --- | --- |
     | agentCode | string | AI助理唯一标识。 |
     | accountToken | string | stream 接收的用户自定义 accountToken。 |

     接口返回值
   - | **参数** | **类型** | **描述** |
     | --- | --- | --- |
     | resultCode | string | 结果状态码。  - 成功（token合法，允许访问）：此值为200。 - 不合法/异常：此值由开发者自定义。 |
     | account | string | 账号。  - accountToken对应的用户账号，长度不超过20个字符。 - 仅当resultCode=200时，需要返回此值。 |
     | message | string | 提示信息。  - token不合法/异常的情况下，需要返回此值，用于展示给用户。 - 长度不超过16个字。 |
3. 集成AI助理的链接/代码中，增加accountToken参数。

   1. 示例：https://agent.dingtalk.com/copilot?code=\*\*\*&channel=${请输入channel}&accountToken=${请输入accountToken，由用户自定义，以便后续在 Stream 服务中接收并解析}

### **常见问题**

#### **1. 页面打不开**

解决方案：请确认AI助理是否完成审批发布。

#### **2. 外部账号登录不成功**

解决方案：请确认回调服务是否接收到回调请求，并按格式要求返回结果。

## **发布到微信服务号**

### **使用限制**

- 一个微信服务号只能和一个 AI 助理绑定。

### **步骤一：获取微信服务号的开发者 ID**

1. 访问[微信服务号平台](https://mp.weixin.qq.com/)并登录你的服务号。
2. 在**设置与开发 > 开发接口管理**页面，获取**开发者ID(AppID)**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1974002371/p874747.png)

### **步骤二：在钉钉客户端中配置并发布 AI 助理**

1. [创建组织内使用的 AI 助理](0005-create-a-dingtalk-ai-assistant-1.md)完成后，单击右上角**发布**按钮，进入 AI 助理发布页面。
2. 在 AI 助理发布页面，单击**微信公众号（服务号）**> **授权配置**，进入授权配置页面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8737613271/p832152.png)
3. 在授权配置页面，在**AppID** 输入框内，填写你步骤一获取的开发者 ID。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8737613271/p832153.png)
4. 填写完成后，单击**确认**，跳转到**公众平台账号授权**页面，使用公众平台绑定的管理员个人微信号扫描二维码。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8737613271/p832156.png)
5. 在微信移动端，根据页面提示选择服务号并确认授权。授权成功的页面提示如下：

   ![b10d407300487a2753a3f61e1cabe9da](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8737613271/p832065.png)
6. 授权成功后，返回 AI 助理发布页面，确认是否已经授权，然后单击**发布助理**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8737613271/p832157.png)
7. 发布成功后，你可以前往微信服务号与钉钉 AI 助理对话。

### **常见问题**

#### **1. 在扫码授权时，出现错误提示，如何解决？**

- **错误提示：请确认并选择正确的微信服务号类型（订阅号或服务号）**

解决方案：请确认是否在订阅号渠道绑定了服务号，或者在服务号渠道绑定了订阅号。

![截屏2024-08-07 下午4](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8737613271/p832069.png)

- **错误提示：未授权**

解决方案：请确认是否已完成“扫描二维码并确认授权”。

![截屏2024-08-07 下午4](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8737613271/p832080.png)

#### **2. 在配置时，出现错误提示，如何解决？**

- **错误提示：当前 App ID 已经和其他 AI 助理绑定**

解决方案：一个服务号只能和一个 AI 助理绑定。请确认该 App ID 是否已经和其他 AI 助理绑定。

![error1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8737613271/p832089.jpeg)

## **发布到微信订阅号**

### **使用限制**

- 一个微信订阅号只能和一个 AI 助理绑定。

### **步骤一：获取微信订阅号的开发者 ID**

1. 访问[微信公众平台](https://mp.weixin.qq.com/)并登录你的订阅号。
2. 在**设置与开发 > 开发接口管理**页面，获取**开发者ID(AppID)**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3084002371/p874751.png)

### **步骤二：在钉钉客户端中配置并发布 AI 助理**

1. [创建组织内使用的 AI 助理](0005-create-a-dingtalk-ai-assistant-1.md)完成后，单击右上角**发布**按钮，进入 AI 助理发布页面。
2. 在 AI 助理发布页面，单击**微信公众号（订阅号）**> **授权配置**，进入授权配置页面。![截屏2024-08-28 下午2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2400384271/p840821.png)
3. 在授权配置页面，在**AppID** 输入框内，填写你步骤一获取的开发者 ID。

   ![截屏2024-08-28 下午2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2400384271/p840822.png)
4. 填写完成后，单击**确认**，跳转到**公众平台账号授权**页面，使用公众平台绑定的管理员个人微信号扫描二维码。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2400384271/p840830.png)
5. 在微信移动端，根据页面提示选择订阅号并确认授权。授权成功的页面提示如下：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2400384271/p840834.png)

7. 授权成功后，返回 AI 助理发布页面，确认是否已经授权，然后单击**发布助理**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8737613271/p832157.png)
8. 发布成功后，你可以前往微信订阅号与钉钉 AI 助理对话。

## **发布到微信小程序**

### **使用限制**

- 一个微信小程序只能和一个 AI 助理绑定。
- 不支持**主体类型**为**个人**的微信小程序。

### **配置发布到微信小程序**

1. [创建组织内使用的 AI 助理](0005-create-a-dingtalk-ai-assistant-1.md)完成后，单击右上角**发布**按钮，进入 AI 助理发布页面。
2. 在 AI 助理发布页面，开启**微信小程序（H5嵌入）**能力，进入嵌入微信小程序页面。
3. 配置嵌入微信小程序：

   1. 选择登录方式：

      - 无需登录，直接使用
      - 手机验证码登录使用
      - 外部账号登录使用

        > 选择登录方式后，即可查看后续步骤。

        ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8986247271/p854621.png)
   2. 选择登录方式后，进入微信小程序后台进行微信端的配置。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8986247271/p854611.png)
   3. 复制钉钉域名完成业务域名配置后下载安全校验文件。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8986247271/p854612.png)
4. 上传授权文件，填写表单。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8986247271/p854623.png)
5. 填写 AI 助理链接并填写微信安全校验文件内容上传即完成微信小程序配置。之后待微信侧审核通过后即可使用。
