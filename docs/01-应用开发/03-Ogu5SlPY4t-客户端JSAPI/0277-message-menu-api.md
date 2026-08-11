---
title: "获取消息内容"
source_url: "https://open.dingtalk.com/document/development/message-menu-api"
namespace: "development"
slug: "message-menu-api"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "酷应用 > 消息菜单 > 获取消息内容"
doc_id: "7DhuTjTPN8"
updated_at: "2025-08-27 18:09:17"
---

> Source: https://open.dingtalk.com/document/development/message-menu-api
> Path: 应用开发 / 客户端JSAPI / 酷应用 > 消息菜单 > 获取消息内容
> Updated: 2025-08-27 18:09:17

# 获取消息内容

本文档介绍了通过H5JSAPI获取消息菜单选中的消息内容。

## 效果示例

> **[!IMPORTANT]**
>
> Android端和iOS端不同系统展示结果可能会出现差别，请以最终的展示效果为准。

展示效果如下图所示：

使用本接口，获取下图步骤3中的消息内容。![11111](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2535257661/p512331.png)

## 调试

本接口暂不支持调试。

## 准备工作

> **[!NOTE]**
>
> 本文API需结合消息菜单使用，在开始开发前，需了解消息菜单相关内容。

1. 查看[消息菜单](https://open.dingtalk.com/document/orgapp/message-menu-overview#title-f9u-iik-8l5)。
2. 查看[接入消息菜单流程指南](https://open.dingtalk.com/document/orgapp/guide-to-the-process-of-accessing-message-menus)。
3. 进行[JSAPI鉴权](https://open.dingtalk.com/document/orgapp/jsapi-authentication)。
4. 获取消息内容JSAPI需依赖[dingtalk-jsapi](https://www.npmjs.com/package/dingtalk-jsapi)，请先升级到最新版本的[dingtalk-jsapi](https://www.npmjs.com/package/dingtalk-jsapi)版本。

```
npm install dingtalk-jsapi --save
```

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 6.3.20及以上 | 6.3.20及以上 | 6.5.30及以上 |

```
import getData from 'dingtalk-jsapi/api/util/openTemporary/getData';

getData({
     onSuccess : function(result) {
        console.log("成功"+ JSON.stringify(result))
     },
    onFail : function(err) {
      console.log("失败"+ JSON.stringify(err))
    }
})
```

## 返回结果

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| conversation | Array of Object | 会话模型相关信息。 |
| name | String | 会话名。 |
| openConversationId | String | 会话Id。 |
| corpId | String | 会话所属corpId。 |
| msgList | Array of Object | 所选中消息的相关信息。 |
| msgtype | String | 消息类型。有以下类型：   - **text**：普通文本 - **richtext**：富文本 - **image**：图片 - **video**: 视频 - **file**： 文件   **[!NOTE]**  当msgtype是image、video和file时，需要注意以下几点：   - 该类消息对应的文件可能存在钉盘中，获取该文件的方法为：根据content中的fileid和spaceid以及[文件下载流程](https://open.dingtalk.com/document/orgapp/file-download-process)。 - 如不存在钉盘中，可以根据content中的url字段进行获取，比如image的url可以通过img标签在钉钉端内进行获取。 |
| createAt | String | 消息的创建时间。 |
| senderName | String | 发送人名称。 |
| text | image | file | video | richtext | String | 消息内容。  **[!NOTE]**   - 当msgtype为text、image时，返回参数为text、image。 - 当msgtype为file、video或richtext时，不返回text、imagee。 |

## 返回数据示例

```
{
    conversation: {
      name: string,
      openConversationId: string,
      corpId: string,
    }
    msgList: [
      {
          msgtype: 'text' | 'image' | 'richtext' | 'video' | 'file';
          createAt: string;
          senderName: string;      //  发送人名称
          extension?: {
            // 消息扩展，可选
            [key: string]: string;
            // 扩展属性内容为字符类型 Map，例如：
            // code_language?: "TypeScript";
            // text_type?: "code_snippet";
          };
          text?: {
            // 文本内容
            content: string;
          };
          image?: {
            // 图片内容
            url: string;
            width: number;
            height: number;
            // * 原始图片大小
            picSize: number;
            // * 图片方向，1-normal,
            // 2-flip_horizontal,
            // 3-rotate_180, 4-flip_vertical, 5-transpose, 6-rotate_90, 7-transverse, 8-rotate_270
            orientation?: number;
          };
          richtext?: {
            // 富文本内容
            content: string;
          };
          file?: {
            fileid?: string;
            f_name?: string;
            f_size?: string;
            f_type?: string;
            spaceid?: string;
            url?: string;   // 当fileid与spaceid不存在时，则会返回url虚拟链接
          }
        }
    ]
  }
```

## 错误码

| 参数 | 说明 |
| --- | --- |
| -1 | 用户取消。 |
| 15001 | 当前用户无可授权项。 |
