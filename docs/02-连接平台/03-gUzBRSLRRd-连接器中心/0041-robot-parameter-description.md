---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/robot-parameter-description"
namespace: "connection"
slug: "robot-parameter-description"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 机器人 > 参数说明"
doc_id: "K3nbp6SnUc"
updated_at: "2025-09-23 19:21:04"
---

> Source: https://open.dingtalk.com/document/connection/robot-parameter-description
> Path: 连接平台 / 连接器中心 / 官方连接器 > 机器人 > 参数说明
> Updated: 2025-09-23 19:21:04

# 参数说明

# **执行动作**

## **批量发送机器人单聊信息**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userIds | Array of String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，钉钉用户 ID列表。 |
| msgParam | String | 是 | 消息内容。  **[!NOTE]**  JSONString格式，和msgKey对应。 |
| msgKey | String | 是 | 输入[模板Key](https://open.dingtalk.com/document/dingstart/types-of-messages-sent-by-robots)，消息类型模板Key。 |
| robotCode | String | 是 | 输入[机器人编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#1bdeba70ffrtc)，机器人robotCode。 |

## **批量发送机器人单聊信息[文本消息]**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userIds | Array of String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，钉钉用户 ID列表。 |
| msgParam | Object | 是 | 消息内容。 |
| content | String | 是 | 文本消息。 |
| robotCode | String | 是 | 输入[机器人编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#1bdeba70ffrtc)，机器人robotCode。 |

## **批量发送机器人单聊信息[图片消息]**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userIds | Array of String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，钉钉用户 ID列表。 |
| msgParam | Object | 是 | 消息内容。 |
| photoURL | String | 是 | 图片url。 |
| robotCode | String | 是 | 输入[机器人编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#1bdeba70ffrtc)，机器人robotCode。 |

## **批量发送机器人单聊信息[链接消息]**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userIds | Array of String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，钉钉用户 ID列表。 |
| msgParam | Object | 是 | 消息内容。 |
| picUrl | String | 是 | 图片URL,支持MediaId。  **[!NOTE]**  可以通过调用[上传媒体文件](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7d80e380ffp3t)接口获取mediaId参数值。 |
| messageUrl | String | 是 | 消息点击跳转URL。 |
| text | String | 是 | 消息正文。 |
| title | String | 是 | 消息标题 |
| robotCode | String | 是 | 输入[机器人编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#1bdeba70ffrtc)，机器人robotCode。 |

## **批量发送机器人单聊信息[markdown消息]**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userIds | Array of String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，钉钉用户 ID列表。 |
| msgParam | Object | 是 | 消息内容。 |
| text | String | 是 | Markdown格式的文本。 |
| title | String | 是 | 消息标题 |
| robotCode | String | 是 | 输入[机器人编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#1bdeba70ffrtc)，机器人robotCode。 |

## **批量发送机器人单聊信息[单按钮消息]**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userIds | Array of String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，钉钉用户 ID列表。 |
| msgParam | Object | 是 | 消息内容。 |
| singleTitle | String | 是 | 单按钮显示标题。 |
| singleURL | String | 是 | 单按钮点击跳转URL。 |
| text | String | 是 | 消息正文。 |
| title | String | 是 | 消息标题 |
| robotCode | String | 是 | 输入[机器人编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#1bdeba70ffrtc)，机器人robotCode。 |

## **批量发送机器人单聊信息[横向多按钮消息]**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userIds | Array of String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，钉钉用户 ID列表。 |
| msgParam | Object | 是 | 消息内容。 |
| buttonTitle2 | String | 是 | 第二个按钮标题。 |
| buttonUrl2 | String | 是 | 第二个按钮点击跳转URL。 |
| buttonTitle1 | String | 是 | 第一个按钮标题。 |
| buttonUrl1 | String | 是 | 第一个按钮点击跳转URL。 |
| text | String | 是 | 消息正文。 |
| title | String | 是 | 消息标题。 |
| robotCode | String | 是 | 输入[机器人编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#1bdeba70ffrtc)，机器人robotCode。 |

## **批量发送机器人单聊信息[竖向两按钮消息]**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userIds | Array of String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，钉钉用户 ID列表。 |
| msgParam | Object | 是 | 消息内容。 |
| actionTitle1 | String | 是 | 按钮一显示标题。 |
| actionURL1 | String | 是 | 按钮一点击跳转URL。 |
| actionTitle2 | String | 是 | 按钮二显示标题。 |
| actionURL2 | String | 是 | 按钮二点击跳转URL。 |
| text | String | 是 | 消息正文。 |
| title | String | 是 | 消息标题。 |
| robotCode | String | 是 | 输入[机器人编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#1bdeba70ffrtc)，机器人robotCode。 |

## **批量发送机器人单聊信息[竖向三个按钮消息]**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userIds | Array of String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，钉钉用户 ID列表。 |
| msgParam | Object | 是 | 消息内容。 |
| actionTitle1 | String | 是 | 按钮一显示标题。 |
| actionURL1 | String | 是 | 按钮一点击跳转URL。 |
| actionTitle2 | String | 是 | 按钮二显示标题。 |
| actionURL2 | String | 是 | 按钮二点击跳转URL。 |
| actionTitle3 | String | 是 | 按钮三显示标题。 |
| actionURL3 | String | 是 | 按钮三点击跳转URL。 |
| text | String | 是 | 消息正文。 |
| title | String | 是 | 消息标题。 |
| robotCode | String | 是 | 输入[机器人编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#1bdeba70ffrtc)，机器人robotCode。 |

## 批量发送机器人单聊信息[竖向四个按钮消息]

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userIds | Array of String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，钉钉用户 ID列表。 |
| msgParam | Object | 是 | 消息内容。 |
| actionTitle1 | String | 是 | 按钮一显示标题。 |
| actionURL1 | String | 是 | 按钮一点击跳转URL。 |
| actionTitle2 | String | 是 | 按钮二显示标题。 |
| actionURL2 | String | 是 | 按钮二点击跳转URL。 |
| actionTitle3 | String | 是 | 按钮三显示标题。 |
| actionURL3 | String | 是 | 按钮三点击跳转URL。 |
| actionTitle4 | String | 是 | 按钮四显示标题 |
| actionURL4 | String | 是 | 按钮四点击跳转URL。 |
| text | String | 是 | 消息正文。 |
| title | String | 是 | 消息标题。 |
| robotCode | String | 是 | 输入[机器人编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#1bdeba70ffrtc)，机器人robotCode。 |

## 批量发送机器人单聊信息[竖向五个按钮消息]

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| userIds | Array of String | 是 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，钉钉用户ID列表。 |
| msgParam | Object | 是 | 消息内容。 |
| actionTitle1 | String | 是 | 按钮一显示标题。 |
| actionURL1 | String | 是 | 按钮一点击跳转URL。 |
| actionTitle2 | String | 是 | 按钮二显示标题。 |
| actionURL2 | String | 是 | 按钮二点击跳转URL。 |
| actionTitle3 | String | 是 | 按钮三显示标题。 |
| actionURL3 | String | 是 | 按钮三点击跳转URL。 |
| actionTitle4 | String | 是 | 按钮四显示标题 |
| actionURL4 | String | 是 | 按钮四点击跳转URL。 |
| actionTitle5 | String | 否 | 按钮五显示标题。 |
| actionURL5 | String | 否 | 按钮五点击跳转URL。 |
| text | String | 是 | 消息正文。 |
| title | String | 是 | 消息标题。 |
| robotCode | String | 是 | 输入[机器人编码](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#1bdeba70ffrtc)，机器人robotCode。 |

## **自定义机器人接入发送消息**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| at | Object | 否 | 被@人信息。 |
| isAtAll | Boolean | 否 | 是否@所有人。 |
| atUserIds | Array of String | 否 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，被@用户的ID列表。 |
| atMobiles | Array of String | 否 | 被@人的手机号。 |
| msgType | String | 是 | 消息类型。 |
| link | Object | 否 | 消息类型，此时固定为link。 |
| messageUrl | String | 否 | 点击消息跳转的URL。 |
| picUrl | String | 否 | 图片URL。 |
| text | String | 否 | 消息内容。  **[!NOTE]**  如果太长只会部分展示。 |
| title | String | 否 | 消息标题。 |
| markdown | Object | 否 | 消息类型，此时固定为markdown。 |
| text | String | 否 | markdown消息内容。 |
| title | String | 否 | 首屏会话透出的展示内容。 |
| feedCard | Object | 否 | 消息类型，此时固定为feedCard。 |
| links | Array | 否 | 链接列表。 |
| picURL | String | 否 | 单条图片URL。 |
| messageURL | String | 否 | 单条信息到跳转链接。 |
| title | String | 否 | 单条信息标题。 |
| text | Object | 否 | 消息类型，此时固定为text。 |
| content | String | 否 | 文本内容。 |
| accessToken | String | 否 | 输入[机器人token](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。  **[!NOTE]**  需要获取**access\_token=**之后的内容。 |
| actionCard | Object | 否 | 消息类型，此时固定为actionCard。 |
| hideAvatar | String | 否 | 是否隐藏头像：   - 0：不隐藏 - 1：隐藏 |
| btnOrientation | String | 否 | 按钮排列：   - 0：竖向 - 1：横向 |
| singleTitle | String | 否 | 单个按钮的标题。  **[!NOTE]**  设置此项和singleURL后，btns无效。 |
| btns | Array | 否 | 按钮的信息。 |
| actionURL | String | 否 | 按钮跳转URL |
| title | String | 否 | 按钮跳转标题。 |
| text | String | 否 | markdown消息内容。 |
| singleURL | String | 否 | 单个按钮触发的URL。 |
| title | String | 否 | 首屏会话透出的展示内容。 |

## **发送文本消息[自定义机器人]**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| isAtAll | Boolean | 否 | 是否@所有人。 |
| atUserIds | Array of String | 否 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，被@用户的ID列表。 |
| atMobiles | Array of String | 否 | 被@人的手机号。 |
| accessToken | String | 是 | 输入[机器人token](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。  **[!NOTE]**  需要获取**access\_token=**之后的内容。 |
| content | String | 是 | 文本内容。 |

## **发送链接消息[自定义机器人]**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| picUrl | String | 否 | 展示图片URL。 |
| text | String | 是 | 消息内容。  **[!NOTE]**  如果太长只会部分展示。 |
| title | String | 是 | 消息标题。 |
| accessToken | String | 是 | 输入[机器人token](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。  **[!NOTE]**  需要获取**access\_token=**之后的内容。 |
| jumpUrl | String | 是 | 跳转URL。 |

## **发送markdown消息[自定义机器人]**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| isAtAll | Boolean | 否 | 是否@所有人。 |
| atUserIds | Array of String | 否 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，被@用户的ID列表。 |
| atMobiles | Array of String | 否 | 被@人的手机号。 |
| accessToken | String | 是 | 输入[机器人token](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。  **[!NOTE]**  需要获取**access\_token=**之后的内容。 |
| text | String | 是 | markdown文本内容。 |
| title | String | 是 | 标题 |

## **发送单按钮ActionCard消息[自定义机器人]**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| isAtAll | Boolean | 否 | 是否@所有人。 |
| atUserIds | Array of String | 否 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，被@用户的ID列表。 |
| atMobiles | Array of String | 否 | 被@人的手机号。 |
| accessToken | String | 是 | 输入[机器人token](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。  **[!NOTE]**  需要获取**access\_token=**之后的内容。 |
| text | String | 是 | markdown内容。 |
| title | String | 是 | 标题。 |
| btnUrl | String | 是 | 按钮触发跳转url。 |
| btnTitle | String | 是 | 按钮标题。 |

## **发送横排多按钮ActionCard消息[自定义机器人]**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| isAtAll | Boolean | 否 | 是否@所有人。 |
| atUserIds | Array of String | 否 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，被@用户的ID列表。 |
| atMobiles | Array of String | 否 | 被@人的手机号。 |
| btns | Array | 是 | 按钮的信息。 |
| actionUrl | String | 否 | 按钮跳转url。 |
| title | String | 否 | 按钮标题。 |
| text | String | 是 | markdown内容。 |
| accessToken | String | 是 | 输入[机器人token](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。  **[!NOTE]**  需要获取**access\_token=**之后的内容。 |
| title | String | 是 | 消息标题。 |

## **发送竖排多按钮ActionCard消息[自定义机器人]**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| isAtAll | Boolean | 否 | 是否@所有人。 |
| atUserIds | Array of String | 否 | 输入[用户ID](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)，被@用户的ID列表。 |
| atMobiles | Array of String | 否 | 被@人的手机号。 |
| btns | Array of Object | 是 | 按钮的信息。 |
| actionUrl | String | 否 | 按钮跳转url。 |
| title | String | 否 | 按钮标题。 |
| text | String | 是 | markdown内容。 |
| accessToken | String | 是 | 输入[机器人token](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。  **[!NOTE]**  需要获取**access\_token=**之后的内容。 |
| title | String | 是 | 消息标题。 |

## **发送FeedCard消息[自定义机器人]**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| feedCards | Array of Object | 是 | feedCard信息列表。 |
| picUrl | String | 是 | 展示图片url。 |
| title | String | 是 | 图片标题。 |
| jumpUrl | String | 是 | 跳转链接。 |
| accessToken | String | 是 | 输入[机器人token](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)。  **[!NOTE]**  需要获取**access\_token=**之后的内容。 |
