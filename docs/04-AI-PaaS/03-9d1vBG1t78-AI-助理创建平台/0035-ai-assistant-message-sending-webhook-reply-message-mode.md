---
title: "AI 助理发消息 - Webhook 回复消息模式"
source_url: "https://open.dingtalk.com/document/aipass/ai-assistant-message-sending-webhook-reply-message-mode"
namespace: "aipass"
slug: "ai-assistant-message-sending-webhook-reply-message-mode"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 能力 > 配置 AI 卡片 > AI 助理发消息 - Webhook 回复消息模式"
doc_id: "GlhStnD09S"
updated_at: "2025-12-08 16:13:45"
---

> Source: https://open.dingtalk.com/document/aipass/ai-assistant-message-sending-webhook-reply-message-mode
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 能力 > 配置 AI 卡片 > AI 助理发消息 - Webhook 回复消息模式
> Updated: 2025-12-08 16:13:45

# AI 助理发消息 - Webhook 回复消息模式

如果你需要实现 AI 助理回复消息，可依据本文档操作步骤实现通过 Webhook 方式发送消息。

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理/助理市场创建的 AI 助理**

## 前提条件

- 完成[创建组织内使用的 AI 助理](0005-create-a-dingtalk-ai-assistant-1.md)/[创建市场 AI 助理](0006-share-dingtalk-ai-assistant.md)的流程。

## **功能简介**

用户与聊天对象（比如 AI 助理）进行交互，开发者可通过高级自定义能力获取到钉钉平台的推送信息，然后开发者根据推送信息中 Webhook 地址发送卡片，完成消息回复。

## **概览**

开发者需要完成以下四个步骤：

1. 在卡片平台中创建 [AI 卡片模板](../../06-互动卡片/01-N4KJ5HbqnQ-开发指南/0002-ai-card-template.md)。
2. 配置 AI 助理的**高级自定义能力**。
3. 与 AI 助理对话，通过配置获取会话的 Webhook Url 地址。
4. HTTP POST 请求 Webhook Url。

## 步骤一：搭建自定义卡片模板

1. 登录钉钉[卡片平台](https://open-dev.dingtalk.com/fe/card)。
2. 创建AI 卡片模板，可参考 [AI 卡片模板](../../06-互动卡片/01-N4KJ5HbqnQ-开发指南/0002-ai-card-template.md)。

   > **[!IMPORTANT]**
   >
   > 创建卡片模板时，卡片类型选择**消息卡片**；卡片模板场景请选择**AI卡片**。
   >
   > ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4406531171/p783288.png)
3. 获取卡片模板ID备用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7685531171/p783289.png)

## **步骤二：****配置 AI 助理的高级自定义能力**

1. 了解 AI 助理高级自定义能力，可参考[高级自定义能力开发指南](0025-development-guide.md)。
2. 在 YAML 文件中添加以下配置：

   - 获取卡片相关的运行上下文（Webhook 地址，用户后续发送卡片消息）：

     ```
     x-dingtalk-context:
       property: currentConversation
       format: sessionWebhook
     ```
   - 如果你只想发送自己的卡片，不想让钉钉官方的聊天消息，可以进行如下配置，关闭官方卡片：

     ```
     x-dingtalk-display-result: disabled
     ```
   - 完成配置后，以天气查询为例，高级自定义能力的 YAML 文件如下所示：

     ```
     openapi: 3.0.1
     info:
       title: 天气查询
       description: 按地区和日期来查看天气信息，了解气温、湿度、风向等信息。非真实天气数据，仅用于演示，请勿在生产中使用。
       version: 1.0.0
     servers:
       - url: https://action-example.dingtalk.com
     paths:
       /v1/actions/example/weather/get:
         get:
           description: 查询特定地区的天气信息
           summary: 查询天气
           operationId: GetCurrentWeather
           x-dingtalk-display-result: disabled  ## 关闭钉钉官方卡片，可选
           parameters:
            - name: sessionWebhook
               in: query
               description: 会话凭证
               schema:
                 type: string
                 x-dingtalk-context:  ## 获取卡片相关的运行上下文
                     property: currentConversation
                     format: sessionWebhook
             - name: location
               in: query
               description: 地区
               required: true
               schema: 
                 type: string
             - name: date
               in: query
               description: 日期
               required: false
               schema: 
                 type: string
           responses:
             200:
               description: OK
               content:
                 application/json:
                   schema:
                     $ref: '#/components/schemas/GetWeatherResponse'
     components:
       schemas:
         GetWeatherResponse:
           type: object
           properties:
             location:
               type: string
               description: 查询天气结果对应的城市和地区
             date:
               type: string
               description: 查询天气结果对应的日期
             text:
               type: string
               description: 天气现象，晴天、多云等
             temperature:
               type: number
               description: 气温，单位：摄氏度
             humidity:
               type: number
               description: 湿度
             wind_direction:
               type: string
               description: 风向
     ```

     上面的示例中只有一个高级自定义能力，你可以按照同样的方式创建多个高级自定义能力。

## 步骤三：与 AI 助理对话，获取 Webhook 地址

在成功完成 AI 助理的配置后，你可以开始与其对话，触发你配置的高级自定义能力，如下图。

![截屏2024-03-13 下午3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9601230171/p778344.png)

**此时，你会在你的服务中收到钉钉颁发的会话凭证 Webhook 地址。**

示例：HTTP 的 body 中收到 sessionWebhook：

```
{
    "date": "2024-03-13",
    "location": "杭州",
    "sessionWebhook": "https://api.dingtalk.com/agent/send?session=aswh_xxxxxxxx"
}
```

> **[!NOTE]**
>
> 如果用户和 AI 助理的对话没有命中高级自定义能力，则 AI 助理会发出正常的官方聊天消息。

## 步骤四：通过 Webhook URL 调用

```
POST /agent/send?session=aswh_xxxx
HTTP/1.1
Host:api.dingtalk.com
Content-Type:application/json

{
    "contentType": "ai_card",
    "content": {
        "templateId": "卡片模版ID",
        "cardData": {
            "param1": "参数1",
            "param2": "参数2"
        }
    }
}
```

## 服务支持

如果你在使用过程中有任何疑问，可通过以下两种方式入群咨询：

- 钉钉搜索“96330019657”群号，加入AI助理共创群。
- 通过扫描下方二维码，加入群聊：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6245361671/p1019720.png)
