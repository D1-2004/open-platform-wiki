---
title: "AI 助理发消息 - 主动发送模式"
source_url: "https://open.dingtalk.com/document/aipass/ai-assistant-sends-messages-active-sending-mode"
namespace: "aipass"
slug: "ai-assistant-sends-messages-active-sending-mode"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 能力 > 配置 AI 卡片 > AI 助理发消息 - 主动发送模式"
doc_id: "WyR0LARulc"
updated_at: "2025-10-28 15:10:26"
---

> Source: https://open.dingtalk.com/document/aipass/ai-assistant-sends-messages-active-sending-mode
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 能力 > 配置 AI 卡片 > AI 助理发消息 - 主动发送模式
> Updated: 2025-10-28 15:10:26

# AI 助理发消息 - 主动发送模式

本文介绍了如何用钉钉 AI 助理主动通过 OpenAPI 的方式发送自定义卡片消息。

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理**

## **前提条件**

- 当创建组织内使用的AI助理时，即通过以下入口创建，按照正常流程操作即可。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6685531171/p783290.png)
- 当创建可跨组织使用的AI助理（可上架）时，即通过以下入口创建，需要先提交[AI助理上架运营前置审批](https://www.aliwork.com/APP_RCGBV8H51P7I5BYY77JZ/submission/FORM-29BA0C4277204F85BB3F0028DD1CF7EBC4RT?processCode=TPROC--4W8667D1R3QJUGB5AYJ779NNKDCT3T7TO9CULB&corpid=ding77a7af8924a84af0)，审批完成后才可获取AK、SK信息。

## **功能简介**

开发者可以通过钉钉 AI 助理主动给用户发送自定义智能消息。主动发送的步骤可以分为：预备、更新和结束三步。

## **概览**

开发者需要完成以下三个步骤：

1. 搭建自定义卡片模板。
2. 获取 AI 助理应用凭证。
3. 开通权限点，调用 OpenAPI。

## **步骤一：搭建自定义卡片模板**

1. 登录钉钉[卡片平台](https://open-dev.dingtalk.com/fe/card)。
2. 创建 AI 卡片模板，可参考[AI 卡片模板](../../06-互动卡片/01-N4KJ5HbqnQ-开发指南/0002-ai-card-template.md)。

   > **[!IMPORTANT]**
   >
   > 创建卡片模板时，卡片类型选择**消息卡片**；卡片模板场景请选择**AI卡片**。
3. 获取卡片模板 ID 备用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7685531171/p783289.png)

## **步骤二：****获取 AI 助理应用凭证**

1. 在 AI 助理编辑页面，单击**技能** > **添加** > **自定义能力。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4542301271/p820696.png)
2. 在新建自定义能力页面，单击**获取我的应用信息**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4542301271/p820697.png)
3. 获取该 AI 助理的 Client ID 和 Client Secret，用于获取 Access Token 凭证。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6685531171/p783284.png)

## **步骤三：开通接口权限点，调用 OpenAPI**

为了给用户提供良好的交互体验，你可以通过“预备 > 更新 > 结束”三段式的方式发送卡片。

| **OpenAPI** | **功能** | **效果** |
| --- | --- | --- |
| [AI 助理预备发消息（主动发送模式）](../../01-应用开发/02-4a8AMF6u2A-服务端API/1592-api-prepare.md) | 给用户发送一个状态为“准备中”的消息框，然后开发者在响应中获取到钉钉颁发的会话凭证。 | 截屏2024-03-25 下午2 |
| [AI 助理更新消息（主动发送模式）](https://open.dingtalk.com/document/development/api-update) | 开发者使用会话凭证更新消息框中的内容，可以多次更新。支持普通更新，也支持流式更新。 | 截屏2024-05-29 下午2  截屏2024-05-29 下午2 |
| [AI 助理结束发消息（主动发送模式）](../../01-应用开发/02-4a8AMF6u2A-服务端API/1594-api-finish.md) | 结束消息框输入。 | 截屏2024-05-29 下午2 |

## **服务支持**

如果你在使用过程中有任何疑问，可通过以下两种方式入群咨询：

- 钉钉搜索“96330019657”群号，加入AI助理共创群。
- 通过扫描下方二维码，加入群聊：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6245361671/p1019720.png)
