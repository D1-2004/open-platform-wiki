---
title: "流程变量获取企业部门名称"
source_url: "https://open.dingtalk.com/document/connection/process-enterprise-department"
namespace: "connection"
slug: "process-enterprise-department"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "内置工具 > 使用教程 > 流程变量 > 流程变量获取企业部门名称"
doc_id: "qG0eZKeoxa"
updated_at: "2026-07-30 09:18:50"
---

> Source: https://open.dingtalk.com/document/connection/process-enterprise-department
> Path: 连接平台 / 连接器中心 / 内置工具 > 使用教程 > 流程变量 > 流程变量获取企业部门名称
> Updated: 2026-07-30 09:18:50

# 流程变量获取企业部门名称

## **前提条件**

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 已开通[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)。

## **操作步骤**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 单击**开放能力** > **连接平台** > **我的连接** > **我的连接流** > **创建连接流**。

   ![我的连接流  创建连接流](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9134735871/p1091131.png)
3. 配置触发事件，选择**内置工具** > **webhook** > **当接受到数据时触发，**无需配置参数。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9134735871/p1091173.png)
4. 配置执行动作（节点2），选择**官方连接器** > **通讯录**。

   ![配置执行动作（节点2）](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0234735871/p1091176.png)
5. 选择**获取部门列表**执行动作，无需配置参数。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0234735871/p1091179.png)
6. 配置执行动作（节点3），选择**内置工具** > **流程变量** > **创建基本类型变量** > **新增变量**，并配置参数：

   ![流程变量创建基本类型变量](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0334735871/p1091205.png)

   | **配置项** | **值** |
   | --- | --- |
   | 变量key | nameList |
   | 变量名称 | 部门名列表 |
   | 变量类型 | 选择**文本**类型 |
   | 默认值 | 选择输入值，填写**部门名列表** |
7. 点击**+**新增一个循环节点。

   ![配置循环执行（节点4）](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0334735871/p1091207.png)
8. 配置循环执行（节点4），配置循环内容：

   ![配置循环内容](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0334735871/p1091208.png)

   | **配置项** | **值** |
   | --- | --- |
   | 循环的数据类型 | 选择**数组**类型 |
   | 循环内容 | 选择**节点2**中的**返回结果.部门列表[\*].部门名称** |
   | 最大循环数据条数 | 填写**10**，表示只取列表中前10个部门名称 |
9. 配置执行动作（节点5），选择**内置工具** > **流程变量** > **更新基本类型变量**：

   1. 属性设置**选择部门名列表**
   2. 属性设置完成后，部门名列表，选择表达式，并设置值为`​流程变量​+"\n"+(​本次循环内容.当前循环次数​+1)+"."+​本次循环内容.本次循环数据`。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0334735871/p753304.png)
10. 配置执行动作（节点6），选择**官方连接器** > **发送机器人消息到群[文本消息]**，并配置参数：

    | **配置项** | **描述** |
    | --- | --- |
    | accessToken | 选择输入值，填写企业应用机器人的Webhook机器人的access\_token的值，可参考[机器人（access\_token）](../02-XdgyZifJkr-我的连接/0015-official-connector-generic-field-acquisition-1.md#bab98990ffdym)。 |
    | 文本消息 | 选择**节点3**的**流程变量.部门名列表**。 |
11. 单击**保存草稿** > **调试**，查看调试效果。

    1. 保存并调试：

       ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0334735871/p753313.png)
    2. 查看调试效果：

       ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0334735871/p753342.png)
12. 调试完成后，单击**发布**。​
