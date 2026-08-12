---
title: "使用FaaS脚本处理企业部门信息"
source_url: "https://open.dingtalk.com/document/connection/enterprise-department-information"
namespace: "connection"
slug: "enterprise-department-information"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "内置工具 > 使用教程 > FaaS脚本 > 使用FaaS脚本处理企业部门信息"
doc_id: "YMA7r9t6vl"
updated_at: "2026-07-30 09:18:40"
---

> Source: https://open.dingtalk.com/document/connection/enterprise-department-information
> Path: 连接平台 / 连接器中心 / 内置工具 > 使用教程 > FaaS脚本 > 使用FaaS脚本处理企业部门信息
> Updated: 2026-07-30 09:18:40

# 使用FaaS脚本处理企业部门信息

## **前提条件**

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 已开通[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)。

## 操作步骤

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 单击**开放能力** > **连接平台** > **我的连接** > **我的连接流** > **创建连接流**。

   ![我的连接流  创建连接流](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9134735871/p1091131.png)
3. 配置触发事件，选择**内置工具** > **webhook** > **当接受到数据时触发，**无需配置参数。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9134735871/p1091173.png)
4. 配置执行动作（节点2），选择**官方连接器** > **通讯录**。

   ![配置执行动作（节点2）](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0234735871/p1091176.png)
5. 选择**获取部门列表**执行动作，无需配置参数。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0234735871/p1091179.png)
6. 配置执行动作（节点3），选择**内置工具 > FaaS脚本 > Python脚本**，并配置参数：

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0234735871/p754334.png)

   | **配置项** | **值** |
   | --- | --- |
   | 设置脚本入参变量（deptInfos） | 选择**引用值** > **节点2：查询结果**。  image |
   | Python脚本代码 | 编写如下脚本代码，遍历通讯录查询到的部门列表，将部门名称和对应的部门 ID 拼接到字符串 result 中，最终添加到 output 输出变量中作为出参字段：   ``` # 从节点2返回的deptInfos中获取部门列表deptList deptList = input["deptInfos"].get("result")  # 遍历deptList，将部门名称开头为连接器的部门name和ID添加到result字符串中 result = "部门名称及对应ID: \n" for dept in deptList:     name = dept.get("name")     deptId = dept.get("dept_id")     if name.startswith("连接器"):         result += "    " + name + ": "+ str(deptId) +"\n"      # 将遍历结果添加到输出output中 output = {"result": result} ```   **[!NOTE]**  相同业务逻辑的Nodejs脚本如下，执行动作选择为**Nodejs脚本**时可用。   ``` var deptList = input.deptInfos.result; var result = ""; deptList   .filter((dept) => dept.name.startsWith("连接器"))   .forEach((dept) => {     result = result + "    " + dept.name + ": " + dept.dept_id + "\n";   }); output.result = result; ``` |
7. 配置执行动作（节点4），选择**官方连接器 > 机器人 > 发送机器人消息到群[文本消息]**，并配置参数：

   | **配置项** | **值** |
   | --- | --- |
   | accessToken | 选择输入值，机器人添加入群后，机器人webhook地址的access\_token的值，可参考[机器人（access\_token）](../02-XdgyZifJkr-我的连接/0015-official-connector-generic-field-acquisition-1.md#bab98990ffdym)。 |
   | 文本消息 | 选择**引用值**，设置**节点3：出参.result**。  image |
8. 单击**保存草稿** > **调试**，查看调试效果。

   1. 保存并调试：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0234735871/p754347.png)
   2. 查看调试效果：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1795864071/p754349.png)
9. 调试完成后，单击**发布**。
