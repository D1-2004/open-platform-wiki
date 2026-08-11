---
title: "使用互动卡片"
source_url: "https://open.dingtalk.com/document/download/using-interactive-cards"
namespace: "download"
slug: "using-interactive-cards"
group: "互动卡片"
tab: "互动卡片搭建平台"
breadcrumb: "互动卡片高级版搭建平台 > 使用互动卡片"
doc_id: "BnD42Z1qcy"
updated_at: "2026-01-29 14:37:14"
---

> Source: https://open.dingtalk.com/document/download/using-interactive-cards
> Path: 互动卡片 / 互动卡片搭建平台 / 互动卡片高级版搭建平台 > 使用互动卡片
> Updated: 2026-01-29 14:37:14

# 使用互动卡片

本功能适用于企业内部自建应用或第三方企业应用开发者，用于在群聊中发送可交互的卡片消息。

## **适用对象**

- 企业内部自建应用开发者
- 第三方ISV应用开发者

## 步骤一：准备互动卡片模板

在准备互动卡片模板这个环节上，您有两种选择：

- 使用钉钉提供的轻量级卡片模板
- 通过钉钉的卡片模板编辑器开发自定义模板

### 使用轻量级卡片模板

为了进一步降低您开发互动卡片的成本，我们针对一些常用的卡片使用场景，封装了一套轻量级卡片模板，通过使用轻量级卡片模板，您无需开发卡片模板即可在群里发送钉钉的互动卡片。

轻量级卡片模板具体使用方法，以及所适用的场景可以在上查阅。如果轻量级卡片模板满足不了您的需求，您可以通过卡片模板编辑器开发自定义的卡片模板。

### 使用卡片模板高级版编辑器开发自定义模板

互动卡片模板的创建可以在钉钉的卡片模板管理页上进行操作：

（首次打开卡片模板管理页面会检查当前的登录态，如果您未登录的话，会提示您进行登录后再操作）![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5782662461/p389802.png)

卡片管理页面会列出当前组织下所创建的模板，点击右上角的“新增模板”即可创建新的卡片模板。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5782662461/p389803.png)

创建新模板时需要指定所创建的模板类型，目前有：

- IM 卡片
- 吊顶卡片

您可根据自身需求选择对应的类型来创建卡片模板。模板创建完后会生成新的卡片模板 ID ，在首页的卡片模板列表上会展示，该 ID 会在发送卡片的时候用到：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6782662461/p389805.png)

点击卡片模板的“编辑”按钮即可进入卡片模板编辑器：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6782662461/p389806.png)

在卡片模板编辑器上您可以通过不同的组件组合来实现您的业务需求。具体的卡片模板编辑器使用方法请移步：。当卡片搭建完成之后，点击保存或发布后即可使用该卡片。

## 步骤二：发送互动卡片

互动卡片需要通过钉钉机器人来发送，因此在发送互动卡片之前，您需要先准备钉钉机器人。具体可以查阅钉钉机器人的文档：

针对于不同的模板类型，您可使用不同的接口来发送钉钉的互动卡片：

### 发送轻量级卡片模板

轻量级卡片模板的发送可以直接参考对应的[发送轻量级互动卡片](../../01-应用开发/02-4a8AMF6u2A-服务端API/1457-send-lightweight-interactive-cards.md)接口。

### 发送卡片模板高级版编辑器开发的自定义模板

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6782662461/p389807.png)

对应的发送卡片接口数据：

```
POST /v1.0/im/interactiveCards/send HTTP/1.1
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "cardTemplateId" : "String",
  "openConversationId" : "String",
  "receiverUserIdList" : [ "String" ],
  "outTrackId" : "String",
  "robotCode" : "String",
  "conversationType" : Integer,
  "callbackRouteKey" : "String",
  "cardData" : {
    "cardParamMap" : {
      "title" : "设计中心周会",
      "date": "3月24日 周五 18:00-17:00",
      "location": "湖畔 大梅沙"
    }
  },
  "chatBotId" : "String",
  "userIdType" : Integer
}
```

## 步骤三：响应用户的卡片操作

钉钉的互动卡片允许用户与卡片进行简单的交互，目前可用的交互类型有：

1. **跳转交互**

   在卡片模板编辑器上您可以为可交互的组件（如按钮、链接组件等）配置点击事件类型为“链接跳转”，同时配置具体的链接值，这时候当用户点击这个按钮时就能打开该链接：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6782662461/p389808.png)
2. **回传请求交互**

   除了链接跳转之外，卡片上也可以让用户进行回传请求，比如在日程卡片上点击“接受”，即可发送接口请求到开发者服务端进行业务逻辑处理。

   在可交互的组件上设置点击事件类型为“回传请求”即可完成设置，同时您也可以配置回传到服务端的参数：

   ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6782662461/p389809.png)

   当配置好按钮之后，用户在钉钉上点击该按钮，卡片会向您注册好的互动卡片回调地址发送一个 POST 请求，请求内容为：

   ```
   {
       "corpId": "dingXXXXXX",
       "outTrackId": "XXXXXX",
       "userId": "XXXXXX",
       "content": "{\"cardPrivateData\":{\"actionIds\":[\"1\"]},\"params\":{\"action\":\"accept\"}}"
   }
   ```

   其中 content 字段包含了按钮的相关信息，如 cardPrivateData.actionIds 表示当前点击的按钮 ID ，如果您给按钮配置了额外的参数的话，这些参数会放在 cardPrivateData.params 里面。

   如果您需要在用户请求接口后同步更新卡片的内容，那么您可以在接收到回调请求后，在该请求里面返回新的卡片数据回去，这样就能实现用户点击按钮之后，执行业务逻辑，然后更新卡片。

   具体返回的卡片数据格式为：

   ```
   {
    "cardTemplateId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx(见消息模板后台模板ID)",
    "outTrackId": "XXXXXX(用于更新卡片的唯一ID)",
    "cardOptions": {
     "updateCardDataByKey": true,
     "updatePrivateDataByKey": true
    },
    "cardData": {
     "cardParamMap": {
      "key1": "value1",
      "key2": "value2",
      "变量N": "变量值N"
     },
     "cardMediaIdParamMap": {
      "image1": "mediaIdXXXXX1",
      "image2": "mediaIdXXXXX2"
     }
    },
    "userPrivateData": {
     "cardParamMap": {
      "key1": "value1",
      "key2": "value2",
      "变量N": "变量值N"
     },
     "cardMediaIdParamMap": {
      "image1": "mediaIdXXXXX1",
      "image2": "mediaIdXXXXX2"
     }
    }
   }
   ```

## 步骤四：更新卡片内容

更新卡片内容有两种方式，一种就是当用户在操作卡片时同步更新卡片内容，这部分已经在上个章节有介绍。另外一种就是开发者主动发起卡片内容更新请求。

当需要主动更新卡片内容时，您只需要调用卡片的更新接口，传递最新的数据即可完成卡片的更新，详情请参考服务端API-[更新钉钉互动卡片](../../01-应用开发/02-4a8AMF6u2A-服务端API/1454-update-dingtalk-interactive-cards.md)接口。
