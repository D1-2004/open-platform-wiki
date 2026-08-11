---
title: "创建群聊会话（场景群）"
source_url: "https://open.dingtalk.com/document/development/create-a-group-chat-session"
namespace: "development"
slug: "create-a-group-chat-session"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 使用教程 > 创建群聊会话（场景群）"
doc_id: "jWAQRIo8Jf"
updated_at: "2025-12-08 10:00:37"
---

> Source: https://open.dingtalk.com/document/development/create-a-group-chat-session
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 使用教程 > 创建群聊会话（场景群）
> Updated: 2025-12-08 10:00:37

# 创建群聊会话（场景群）

本操作流程指导你如何实现创建群聊会话且存量群升级为群聊会话。

## 步骤一：创建钉钉应用

1. 登录[开发者后台](https://open-dev.dingtalk.com)。

   > **[!IMPORTANT]**
   >
   > 如果你无法使用企业组织登录开发者后台，请参考[成为钉钉开发者](https://open.dingtalk.com/document/dingstart/dingtalk-developer)文档，确保已有**开发者权限**。
2. 单击**应用开发**，创建一个企业内部应用或第三方企业应用，应用类型可以选择小程序或H5微应用。以创建企业内部应用为例。

> **[!NOTE]**
>
> 使用群聊会话相关能力，必须先创建企业内部应用或第三方企业应用，获取相关的访问凭证。

![p208247](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0510180261/p261582.png)

3. 以创建企业内部应用为例，创建应用后，可以获取AppKey和AppSecret。

> **[!NOTE]**
>
> 用于后续获取接口调用的访问凭证，详见本文第5步使用。

![群开放-创建场景群-步骤一-创建应用图1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4377760461/p377475.png)

4. 添加接口调用权限。搜索“场景群”，申请场景群接口对应的权限。

> **[!NOTE]**
>
> 用于后续步骤正常调用群聊会话相关接口，未申请接口权限，调用接口时会提示“没有调用该接口的权限”。

![群开放-创建场景群-步骤一-添加接口调用权限](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4377760461/p377484.png)5. 获取应用访问凭证。以企业内部应用为例，调用[获取企业内部应用的access\_token](1420-obtain-orgapp-token.md)。调用群聊会话相关接口时，通过accessToken鉴权调用者身份。

> **[!NOTE]**
>
> 访问凭证用于在调用群聊会话开放相关接口时使用。

## **步骤二：创建群模板**

1. 在[开发者后台](https://open-dev.dingtalk.com)，单击**场景群**，然后选择**群模板**，单击**创建群模板**。

   ![群开放-创建场景群-步骤二-创建群模板1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1477760461/p377499.png)
2. 选择应用类型，然后选择一个已创建的钉钉应用，单击**下一步**。

   ![群开放-创建场景群-步骤二-选择模板1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5993060461/p377309.png)
3. 配置群模板信息，然后单击保存编辑。

   | 群模板信息项 | 是否必填 | 填写说明 |
   | --- | --- | --- |
   | 群模板名称 | 必填 | 输入群模板的名称。 |
   | 图标 | 必填 | 选择群模板的图标。 |
   | 描述 | 必填 | 输入该模板的描述信息。 |
   | 群设置 | 非必填 | 设置群相关内容。 |

   ![群开放-创建场景群-步骤二-图2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5993060461/p377311.png)

4. 在群模板列表页面，单击新创建的群模板。

![群开放-创建场景群-步骤二-提交审核图1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5993060461/p377316.png)

5. 点击提交审核。

> **[!NOTE]**
>
> 提交审核后，审批自动通过。

![群开放-创建场景群-步骤二-提交审核图2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5993060461/p377315.png)

6. 点击发布。![群开放-创建场景群-步骤二-发布图2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5993060461/p377319.png)

7. 发布成功后，查看群模板ID。![群开放-创建场景群-步骤二-发布完后图1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5993060461/p377320.png)

## **步骤三：创建群聊会话**

### **通过接口创建群聊会话**

1. 调用[创建群](1461-create-a-scene-group-v2.md)接口创建**群聊会话**。

   > **[!IMPORTANT]**
   >
   > 第三方企业应用[创建群](1461-create-a-scene-group-v2.md)接口前，需要设置灰度企业。![企业灰度](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9564899361/p368591.png)

   ```
   DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/im/chat/scenegroup/create");
   OapiImChatScenegroupCreateRequest req = new OapiImChatScenegroupCreateRequest();
   req.setOwnerUserId("manager4220");
   req.setUserIds("user01,user02");
   req.setIcon("@asdf12zcv");
   req.setMentionAllAuthority(0L);
   req.setShowHistoryType(0L);
   req.setValidationType(0L);
   req.setSearchable(0L);
   req.setChatBannedType(0L);
   req.setManagementType(0L);
   req.setTitle("测试群");
   req.setTemplateId("template123");
   OapiImChatScenegroupCreateResponse rsp = client.execute(req, access_token);
   System.out.println(rsp.getBody());
   ```

### **存量群升级群聊会话**

存量群升级**群聊会话**有2种方式：

方式一：钉钉群里，在群设置中启动群模板

方式二：调用启用群模板API升级。

#### **哪些群可以升级成群聊会话**

目前群聊会话主要服务具有企业归属群，**企业内部群**、**服务群**是具有企业归属的，目前这两类群可以通过API升级为群聊会话。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7504092761/p543755.png)

#### **升级条件**

在将**企业内部群**、**服务群**升级为群聊会话前，确保满足以下条件：

1. 该群模板已经灰度到对应群的企业。
2. 群模板需要群主或群管理员身份才可以启用/停用。
3. 第三方企业应用群模板还需要效验目标群对应的企业是否有安装群模板对应的应用。

#### **方式一：**在群设置中启动群模板

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7504092761/p543766.png)

#### **方式二：**通过调用API启用群模板

调用[启用群模板](0757-enable-a-group-template.md)接口，实现群升级为群聊会话。

> **[!IMPORTANT]**
>
> 调用[启用群模板](0757-enable-a-group-template.md)接口前，需要设置灰度企业。![企业灰度](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9564899361/p368591.png)
