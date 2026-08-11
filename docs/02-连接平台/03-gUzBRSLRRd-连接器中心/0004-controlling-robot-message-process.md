---
title: "使用流程暂停控制机器人发送消息"
source_url: "https://open.dingtalk.com/document/connection/controlling-robot-message-process"
namespace: "connection"
slug: "controlling-robot-message-process"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "内置工具 > 流程暂停 > 使用流程暂停控制机器人发送消息"
doc_id: "8j50L7QxL5"
updated_at: "2026-05-19 16:01:36"
---

> Source: https://open.dingtalk.com/document/connection/controlling-robot-message-process
> Path: 连接平台 / 连接器中心 / 内置工具 > 流程暂停 > 使用流程暂停控制机器人发送消息
> Updated: 2026-05-19 16:01:36

# 使用流程暂停控制机器人发送消息

## **前提条件**

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 已开通[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)。

## **操作步骤**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 单击**开放能力** > **连接平台** > **我的连接** > **我的连接流** > **创建连接流**。
3. 配置触发事件，选择**内置工具** > **webhook** > **当接受到数据时触发。**
4. 配置执行动作（节点2），选择**官方连接器** > **机器人** >**发送机器人消息到群[文本消息]，**并配置参数：

   | **配置项** | **值** |
   | --- | --- |
   | accessToken | 选择输入值，机器人添加入群后，机器人webhook地址的access\_token的值，可参考[机器人（access\_token）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#bab98990ffdym)。 |
   | 文本消息 | 选择表达式，设置表达式为 **DATEFORMAT(NOW(),'HH:mm:ss')+" 流程暂停提示"**  image.png |
5. 配置执行动作（节点3），选择**内置工具** > **流程暂停** > **从当前节点暂停**，无需配置参数，当流程暂停后，可通过回调URL来恢复其运行（回调URL可在流程调试时获取）。
6. 配置执行动作（节点4），选择**官方连接器 > 机器人 > 发送机器人消息到群[文本消息]**，并配置参数：

   | **配置项** | **值** |
   | --- | --- |
   | accessToken | 选择输入值，机器人添加入群后，机器人webhook地址的access\_token的值，可参考[机器人（access\_token）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#bab98990ffdym)。 |
   | 文本消息 | 选择表达式，设置表达式为 **DATEFORMAT(NOW(),'HH:mm:ss')+" 流程恢复提示"**  image.png |
7. 单击**保存** > **调试**，查看调试效果。

   1. 保存并调试：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9695864071/p754286.png)
   2. 查看调试效果：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9695864071/p754288.png)
8. 调试完成后，单击**执行记录 > 对应执行记录 > 复制回调 URL**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9695864071/p754298.png)
9. 接下来在浏览器或接口调试工具中直接发送该请求（无需设置入参，Get/Post类型均可），恢复流程运行。可在群聊中收到机器人发送的**流程恢复提示**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9695864071/p754305.png)​
