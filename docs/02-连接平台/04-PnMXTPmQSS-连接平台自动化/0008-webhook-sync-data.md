---
title: "Webhook同步数据"
source_url: "https://open.dingtalk.com/document/connection/webhook-sync-data"
namespace: "connection"
slug: "webhook-sync-data"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "群聊自动化 > 模板教学 > Webhook同步数据"
doc_id: "mkJ2QC78TL"
updated_at: "2025-09-23 19:21:41"
---

> Source: https://open.dingtalk.com/document/connection/webhook-sync-data
> Path: 连接平台 / 连接平台自动化 / 群聊自动化 > 模板教学 > Webhook同步数据
> Updated: 2025-09-23 19:21:41

# Webhook同步数据

## **背景信息**

Webhook是一个面向开发者的高级功能，请在开发者的帮助下使用此功能。

> **[!IMPORTANT]**
>
> 请保管好webhook地址，不要公布在外部网站，一旦产生泄露，可能会引发大量的危害信息传入，耗尽组织的开发资源，为组织带来资源损失和安全风险。

## **场景介绍**

- **内部系统数据同步**：在 ERP、CRM 等内部系统设置 Webhook，可实现系统之间的数据同步，免去人工手动同步。
- **网站内容更新通知**：在你关注的网站设置 Webhook，有新内容时就会主动通知你，不需要你反复打开网站查看。
- **监控和报警通知**：在监控系统或报警平台设置 Webhook，可以实时监控系统的健康状况，帮助你尽快处理问题。

| image.png | image.png |
| --- | --- |

## **操作步骤（手动配置）**

1. 在**流程模板**中选择模板**数据订阅**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5853786071/p754946.png)
2. 步骤1为**接收到数据时：**

   1. **设置触发关键词**。只有接收到包含关键词的数据时，才会触发流程。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5853786071/p754947.png)
   2. 在参数示例中，**手动填入将要接收到的参数示例**，以便在后续步骤中**引用这些参数。**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5853786071/p754948.png)
3. 步骤2为**发送消息到该群组**，单击 ⊕ 就能**引用**步骤1**输出的参数。**

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5853786071/p754949.png)
4. 单击左上角，用户可以更改流程的标题名称。单击右上角**保存并启用**即可发布流程。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5853786071/p754950.png)

## **操作步骤（源数据解析）**

源数据解析，可以将**符合固定格式的JSON体**自动解析为**消息体**发送。如果Webhook接收到的数据**符合固定格式（见文末）**，或者**你之前在群聊内使用过「自定义机器人」**，那么你可以使用源数据解析进行发消息。

1. 在**流程模板**中选择模板**数据预警**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4853786071/p754951.png)
2. 步骤1为**接收到数据时**，**设置触发关键词**。只有接收到包含关键词的数据时，才会触发流程。参数格式选择「**Text」**，表示将原封不动地将接收到的数据传给后续步骤。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5853786071/p754952.png)
3. 步骤2为**发送消息到该群组**。如图所示，模板的配置中，消息来源为**源数据解析**，源数据为步骤1的输出数据，即可**将接收到的数据自动解析为消息体发送出去**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5853786071/p754953.png)
4. 单击左上角，用户可以更改流程的标题名称。单击右上角**保存并启用**即可发布流程。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4853786071/p754954.png)

### **机器人支持的消息结构**

钉钉机器人支持**text、link、markdown、actionCard、feedCard**这几种消息类型，具体数据结构如下

- #### **text类型：**

  ```
  {
      "at": {
          "atMobiles":[
              "180xxxxxx"
          ],
          "atUserIds":[
              "user123"
          ],
          "isAtAll": false
      },
      "text": {
          "content":"我就是我, @XXX 是不一样的烟火"
      },
      "msgtype":"text"
  }
  ```

  | **参数** | **参数类型** | **是否必填** | **说明** |
  | --- | --- | --- | --- |
  | msgtype | String | 是 | 消息类型，此时固定为：text。 |
  | content | String | 是 | 消息内容。 |
  | atMobiles | Array | 否 | 在content里添加被@人的手机号。  提示：**只有在群内的成员才可被@**，非群内成员手机号会被脱敏 |
  | atUserIds | Array | 否 | 在content里添加被@人的用户userid。 |
  | isAtAll | Boolean | 否 | 是否@所有人。 |

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038074071/p755615.png)
- #### **link类型：**

  ```
  {
      "msgtype": "link", 
      "link": {
          "text": "这个即将发布的新版本，创始人xx称它为红树林。而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是红树林", 
          "title": "时代的火车向前开", 
          "picUrl": "", 
          "messageUrl": "https://www.dingtalk.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI"
      }
  }
  ```

  | **参数** | **参数类型** | **是否必填** | **说明** |
  | --- | --- | --- | --- |
  | msgtype | String | 是 | 消息类型，此时固定为：link。 |
  | title | String | 是 | 消息标题。 |
  | text | String | 是 | 消息内容。如果太长只会部分展示。 |
  | messageUrl | String | 是 | 点击消息跳转的URL，打开方式如下：  - 移动端，在钉钉客户端内打开 - PC端    - 默认侧边栏打开   - 希望在外部浏览器打开，详情可参考[消息链接说明](../../01-应用开发/02-4a8AMF6u2A-服务端API/0774-message-link-description.md)。 |
  | picUrl | String | 否 | 图片URL。 |

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038074071/p755616.png)
- #### **markdown类型：**

  ```
  {
       "msgtype": "markdown",
       "markdown": {
           "title":"杭州天气",
           "text": "#### 杭州天气 @150XXXXXXXX \n > 9度，西北风1级，空气良89，相对温度73%\n > ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n > ###### 10点20分发布 [天气](https://www.dingtalk.com) \n"
       },
        "at": {
            "atMobiles": [
                "150XXXXXXXX"
            ],
            "atUserIds": [
                "user123"
            ],
            "isAtAll": false
        }
   }
  ```

  | **参数** | **参数类型** | **是否必填** | **说明** |
  | --- | --- | --- | --- |
  | msgtype | String | 是 | 消息类型，此时固定为：markdown。 |
  | title | String | 是 | 首屏会话透出的展示内容。 |
  | text | String | 是 | markdown格式的消息。 |
  | atMobiles | Array | 否 | 在content里添加被@人的手机号。  提示：**只有在群内的成员才可被@**，非群内成员手机号会被脱敏 |
  | atUserIds | Array | 否 | 在content里添加被@人的用户userid。 |
  | isAtAll | Boolean | 否 | 是否@所有人。 |

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038074071/p755618.png)目前只支持markdown语法的子集，具体支持的元素如下：

  ```
  标题
  # 一级标题
  ## 二级标题
  ### 三级标题
  #### 四级标题
  ##### 五级标题
  ###### 六级标题

  引用
  > A man who stands for nothing will fall for anything.

  文字加粗、斜体
  **bold**
  *italic*

  链接
  [this is a link](http://name.com)

  图片（建议不要超过20张）
  ![](http://name.com/pic.jpg)

  无序列表
  - item1
  - item2

  有序列表
  1. item1
  2. item2
  ```
- #### **整体跳转ActionCard类型：**

  ```
  {
      "actionCard": {
          "title": "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身", 
          "text": "![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png) 
   ### 乔布斯 20 年前想打造的苹果咖啡厅 
   Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划", 
          "btnOrientation": "0", 
          "singleTitle" : "阅读全文",
          "singleURL" : "https://www.dingtalk.com/"
      }, 
      "msgtype": "actionCard"
  }
  ```

  | **参数** | **参数类型** | **是否必填** | **说明** |
  | --- | --- | --- | --- |
  | msgtype | String | 是 | 消息类型，此时固定为：actionCard。 |
  | title | String | 是 | 首屏会话透出的展示内容。 |
  | text | String | 是 | markdown格式的消息。 |
  | singleTitle | String | 是 | 单个按钮的标题。  **提示：**设置此项和singleURL后，btns无效。 |
  | singleURL | String | 是 | 点击消息跳转的URL，打开方式如下：  - 移动端，在钉钉客户端内打开 - PC端    - 默认侧边栏打开   - 希望在外部浏览器打开，详情可参考[消息链接说明](../../01-应用开发/02-4a8AMF6u2A-服务端API/0774-message-link-description.md)。 |
  | btnOrientation | String | 否 | 0：按钮竖直排列  1：按钮横向排列 |

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038074071/p755617.png)
- #### **独立跳转ActionCard类型：**

  ```
  {
      "msgtype": "actionCard",
      "actionCard": {
          "title": "我 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身", 
          "text": "![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png) \n\n #### 乔布斯 20 年前想打造的苹果咖啡厅 \n\n Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划", 
          "btnOrientation": "0", 
          "btns": [
              {
                  "title": "内容不错", 
                  "actionURL": "https://www.dingtalk.com/"
              }, 
              {
                  "title": "不感兴趣", 
                  "actionURL": "https://www.dingtalk.com/"
              }
          ]
      }
  }
  ```

  | **参数** | **参数类型** | **是否必填** | **说明** |
  | --- | --- | --- | --- |
  | msgtype | String | 是 | 消息类型，此时固定为：actionCard。 |
  | title | String | 是 | 首屏会话透出的展示内容。 |
  | text | String | 是 | markdown格式的消息。 |
  | singleTitle | String | 是 | 单个按钮的标题。  **提示：**设置此项和singleURL后，btns无效。 |
  | singleURL | String | 是 | 点击消息跳转的URL，打开方式如下：  - 移动端，在钉钉客户端内打开 - PC端    - 默认侧边栏打开   - 希望在外部浏览器打开，详情可参考[消息链接说明](../../01-应用开发/02-4a8AMF6u2A-服务端API/0774-message-link-description.md)。 |
  | btnOrientation | String | 否 | 0：按钮竖直排列  1：按钮横向排列 |

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038074071/p755619.png)
- #### **FeedCard类型：**

  ```
  {
      "msgtype":"feedCard",
      "feedCard": {
          "links": [
              {
                  "title": "时代的火车向前开1", 
                  "messageURL": "https://www.dingtalk.com/", 
                  "picURL": "https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png"
              },
              {
                  "title": "时代的火车向前开2", 
                  "messageURL": "https://www.dingtalk.com/", 
                  "picURL": "https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png"
              }
          ]
      }
  }
  ```

  | **参数** | **参数类型** | **是否必填** | **说明** |
  | --- | --- | --- | --- |
  | msgtype | String | 是 | 此消息类型为固定feedCard。 |
  | title | String | 是 | 单条信息文本。 |
  | messageURL | String | 是 | 点击单条信息到跳转链接。    **说明**  PC端跳转目标页面的方式，详情可参考[消息链接在PC端侧边栏或者外部浏览器打开](../../01-应用开发/02-4a8AMF6u2A-服务端API/0774-message-link-description.md)。 |
  | picURL | String | 是 | 单条信息后面图片的URL。 |

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038074071/p755622.png)
