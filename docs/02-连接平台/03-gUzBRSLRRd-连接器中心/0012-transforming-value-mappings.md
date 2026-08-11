---
title: "使用字段值映射对字段进行转换"
source_url: "https://open.dingtalk.com/document/connection/transforming-value-mappings"
namespace: "connection"
slug: "transforming-value-mappings"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "内置工具 > 字段值映射 > 使用字段值映射对字段进行转换"
doc_id: "fpPGZ1LTW4"
updated_at: "2026-05-19 16:01:42"
---

> Source: https://open.dingtalk.com/document/connection/transforming-value-mappings
> Path: 连接平台 / 连接器中心 / 内置工具 > 字段值映射 > 使用字段值映射对字段进行转换
> Updated: 2026-05-19 16:01:42

# 使用字段值映射对字段进行转换

## **前提条件**

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 已开通[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)。

## **操作步骤**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 单击**开放能力** > **连接平台** > **我的连接** > **我的连接流** > **创建连接流**。
3. 配置触发事件，选择**内置工具** > **webhook** > **当接受到数据时触发。**
4. 配置执行动作（节点2），选择**内置工具** > **字段值映射** > **通过查询映射表配置映射规则**，并配置参数：

   | **配置项** | **值** |
   | --- | --- |
   | 被映射的输入 | 填写**apple** |
   | 映射类型 | 选择**录入映射表** |
   | 录入映射表 | banana -> 香蕉 |
   | apple -> 苹果 |
   | pear -> 梨子 |
   | 查询无结果时返回值 | 未知水果 |

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8795864071/p754519.png)
5. 配置执行动作（节点3），选择**内置工具** > **字段值映射** > **通过查询映射表配置映射规则**，并配置参数：

   | **配置项** | **值** |
   | --- | --- |
   | 被映射的输入 | 张三 |
   | 映射类型 | 选择**引用变量** |
   | 引用变量 | {"张三":"zhangsan","李四":"lisi","王五":"wangwu"} |
   | 查询无结果时返回值 | 未知用户 |

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7795864071/p754521.png)
6. 配置执行动作（节点4），选择**内置工具** > **字段值映射** > **通过查询映射表配置映射规则**，并配置参数：

   | **配置项** | **值** |
   | --- | --- |
   | 被映射的输入 | 1 |
   | 映射类型 | 选择**数据映射表** |
   | 字段值映射表 | 选择数字映射  **[!NOTE]**  数据存储表在连接平台 > 配置中心 > 连接项目 > 数据存储中进行配置。  1. 先创建一个名为“数字映射”的存储表，存储类型设置为键值对  image.png 2. 在存储表中插入如下记录，内容为阿拉伯数字到英文数字的映射  image.png 3. 在执行动作配置页，设置“字段映射表”为我们刚才创建的“**数字映射**” |
   | 查询无结果时返回值 | 未找到映射值 |

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7795864071/p754525.png)
7. 配置执行动作（节点5），选择**官方连接器** > **机器人** >**发送机器人消息到群[文本消息]，**并配置参数：

   | **配置项** | **值** |
   | --- | --- |
   | accessToken | 选择输入值，机器人添加入群后，机器人webhook地址的access\_token的值，详情参考[机器人（access\_token）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#bab98990ffdym)。 |
   | 文本消息 | 选择表达式，设置表达式为:  image.png |
8. 单击**保存** > **调试**，查看调试效果。

   1. 保存并调试：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8795864071/p754535.png)
   2. 查看调试效果：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7795864071/p754536.png)
