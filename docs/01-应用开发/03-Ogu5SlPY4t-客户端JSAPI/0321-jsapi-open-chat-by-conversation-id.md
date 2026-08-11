---
title: "openChatByConversationId"
source_url: "https://open.dingtalk.com/document/development/jsapi-open-chat-by-conversation-id"
namespace: "development"
slug: "jsapi-open-chat-by-conversation-id"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "会话管理 > openChatByConversationId"
doc_id: "Kcc8ugdj4E"
updated_at: "2024-12-04"
---

> Source: https://open.dingtalk.com/document/development/jsapi-open-chat-by-conversation-id
> Path: 应用开发 / 客户端JSAPI / 会话管理 > openChatByConversationId
> Updated: 2024-12-04

# openChatByConversationId

根据openChatByConversationId，跳转到对应会话。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11654) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11654) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

参数占位区域

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.openChatByConversationId({
  openConversationId: 'ddds333',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
