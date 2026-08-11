---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/message-notification-parameter-description"
namespace: "connection"
slug: "message-notification-parameter-description"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 消息通知 > 参数说明"
doc_id: "5C7qoO5Jla"
updated_at: "2025-09-23 19:21:19"
---

> Source: https://open.dingtalk.com/document/connection/message-notification-parameter-description
> Path: 连接平台 / 连接器中心 / 官方连接器 > 消息通知 > 参数说明
> Updated: 2025-09-23 19:21:19

# 参数说明

## 执行动作说明

## **发送消息到企业群[文本消息]**

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| msg | Object | 是 | 发送消息的类型。 |
| text | Object | 是 | 文本消息。 |
| content | String | 是 | 消息内容。 |
| chatid | String | 是 | 输入[群会话ID（chatId/openConversationId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#37be9ff0ffhrb)，待发送群的会话ID。 |

## 发送消息到企业群[图片消息]

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| msg | Object | 是 | 发送消息的类型。 |
| image | Object | 是 | 图片消息。 |
| media\_id | String | 是 | 可以通过调用[上传媒体文件](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)接口获取mediaId参数值。 |
| chatid | String | 是 | 输入[群会话ID（chatId/openConversationId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#37be9ff0ffhrb)，待发送群的会话ID。 |

## 发送消息到企业群[markdown消息]

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| msg | Object | 否 | 消息类型。 |
| markdown | Object | 否 | markdown消息。 |
| text | String | 否 | markdown格式的消息。 |
| title | String | 否 | 首屏会话透出的展示内容。 |
| chatid | String | 否 | 输入[群会话ID（chatId/openConversationId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#37be9ff0ffhrb)，待发送群的会话ID。 |

## 发送消息到企业群[OA消息]

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| msg | Object | 否 | 消息类型。 |
| oa | Object | 否 | oa消息。 |
| head | Object | 否 | 消息头部内容。 |
| bgcolor | String | 否 | 消息头部的背景颜色。长度限制为8个英文字符，其中前2为表示透明度，后6位表示颜色值。不要添加0x。 |
| text | String | 否 | 消息的头部标题 。  **[!NOTE]**   - 向普通会话发送时有效，向企业会话发送时会被替换为微应用的名字 - 长度限制为最多10个字符。 |
| pc\_message\_url | String | 否 | PC端点击消息时跳转到的地址。 |
| body | Object | 否 | 消息体。 |
| file\_count | String | 否 | 自定义的附件数目。  **[!NOTE]**  此数字仅供显示，钉钉不作验证。 |
| image | String | 否 | 可以通过调用[上传媒体文件](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)接口获取mediaId参数值。 |
| form | Array of Object | 否 | 消息体的表单。例如：   ``` { 	"key": "姓名:", 	"value": "小钉" } ```   **[!NOTE]**  最多显示6个，超过会被隐藏。 |
| key | String | 否 | 消息体的关键字。 |
| value | String | 否 | 消息体的关键字对应的值。 |
| author | String | 否 | 自定义的作者名字。 |
| rich | Object | 否 | 单行富文本信息。 |
| unit | String | 否 | 单行富文本信息的单位。 |
| num | String | 否 | 单行富文本信息的数目。 |
| title | String | 否 | 消息体的标题。  **[!NOTE]**  建议50个字符以内 |
| content | String | 否 | 消息体的内容。  **[!NOTE]**  最多显示3行。 |
| message\_url | String | 否 | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接。 |
| chatid | String | 否 | 输入[群会话ID（chatId/openConversationId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#37be9ff0ffhrb)，待发送群的会话ID。 |

## 发送消息到企业群[链接消息]

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| chatid | String | 否 | 输入[群会话ID（chatId/openConversationId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#37be9ff0ffhrb)，待发送群的会话ID。 |
| msg | Object | 否 | 消息类型。 |
| link | Object | 否 | 链接消息。 |
| messageUrl | String | 否 | 消息点击链接地址。 |
| picUrl | String | 否 | 图片地址。 |
| text | String | 否 | 消息文本。 |
| title | String | 否 | 消息标题。 |

## 发送消息到企业群[voice消息]

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| msg | Object | 否 | 消息类型。 |
| voice | Object | 否 | voice消息。 |
| duration | String | 否 | 录音时长，单位s。  **[!NOTE]**  播放长度不超过60s。 |
| media\_id | String | 否 | 可以通过调用[上传媒体文件](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)接口获取mediaId参数值。  **[!NOTE]**  不超过2MB，AMR格式。 |
| chatid | String | 否 | 输入[群会话ID（chatId/openConversationId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#37be9ff0ffhrb)，待发送群的会话ID。 |

## 发送消息到企业群[文件消息]

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| msg | Object | 是 | 发送消息的类型。 |
| file | Object | 是 | 文件消息。 |
| media\_id | String | 是 | 可以通过调用[上传媒体文件](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)接口获取mediaId参数值。 |
| chatid | String | 是 | 输入[群会话ID（chatId/openConversationId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#37be9ff0ffhrb)，待发送群的会话ID。 |

## 发送消息到企业群[卡片消息]

整体跳转ActionCard样式，支持一个点击Action，必须传入参数 single\_title和 single\_url。

```
{
  "chatid": "chat****",
  "action_card": {
    "title": "是透出到会话列表和通知的文案",
    "markdown": "支持markdown格式的正文内容",
    "single_title": "查看详情",
    "single_url": "https://open.dingtalk.com"
  }
}
```

独立跳转ActionCard样式，支持多个点击Action，必须传入参数 btn\_orientation 和 btn\_json\_list。

```
{
  "chatid": "chat****",
  "action_card": {
    "title": "是透出到会话列表和通知的文案",
    "markdown": "支持markdown格式的正文内容",
    "btn_orientation": "1",
    "btn_json_list": [
      {
        "title": "一个按钮",
        "action_url": "https://www.taobao.com"
      },
      {
        "title": "两个按钮",
        "action_url": "https://www.tmall.com"
      }
    ]
  }
}
```

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| chatid | String | 否 | 输入[群会话ID（chatId/openConversationId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#37be9ff0ffhrb)，待发送群的会话ID。 |
| msg | Object | 否 | 发送消息的类型。 |
| action\_card | Object | 否 | 卡片消息。 |
| agentid | String | 否 | 应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| btn\_json\_list | Array | 否 | 使用独立跳转ActionCard样式时的按钮列表。  **[!NOTE]**  必须与btn\_orientation同时设置。 |
| action\_url | String | 否 | 使用独立跳转消息点击链接地址。 |
| title | String | 否 | 使用独立跳转ActionCard样式时的按钮的标题。  **[!NOTE]**  最长20个字符。 |
| single\_url | String | 否 | 使用整体跳转消息点击链接地址。  **[!NOTE]**  最长500个字符。 |
| btn\_orientation | String | 否 | 使用独立跳转ActionCard样式时的按钮排列方式：   - **0**：竖直排列 - **1**：横向排列   **[!NOTE]**  必须与btn\_json\_list同时设置。 |
| single\_title | String | 否 | 使用整体跳转ActionCard样式时的标题。  **[!NOTE]**   - 必须与single\_url同时设置。 - 最长20个字符。 |
| markdown | String | 否 | 消息内容。  **[!NOTE]**  建议1000个字符以内。 |
| hide\_avatar | Boolean | 否 | 是否隐藏发送者头像。 |
| title | String | 否 | 透出到会话列表和通知的文案。  **[!NOTE]**  最长64个字符。 |
