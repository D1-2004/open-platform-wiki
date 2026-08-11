---
title: "获取智能人事员工花名册信息并填充到OA表单"
source_url: "https://open.dingtalk.com/document/connection/obtain-roster-information"
namespace: "connection"
slug: "obtain-roster-information"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 智能人事 > 使用教程 > 获取智能人事员工花名册信息并填充到OA表单"
doc_id: "k47TZJ4qo8"
updated_at: "2026-05-19 19:46:16"
---

> Source: https://open.dingtalk.com/document/connection/obtain-roster-information
> Path: 连接平台 / 连接器中心 / 官方连接器 > 智能人事 > 使用教程 > 获取智能人事员工花名册信息并填充到OA表单
> Updated: 2026-05-19 19:46:16

# 获取智能人事员工花名册信息并填充到OA表单

## **准备工作**

1. 已经完成了钉钉开发者的注册与激活并拥有了子管理员和开发者权限。
2. 已开通钉钉专业版（OA审批中使用连接器必备）。若尚未完成，请参考[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)。
3. 已经了解并熟悉[什么是连接平台](../01-6Ar2XD4H6b-平台介绍/0001-what-is-a-connected-platform.md)。

## **预期效果**

在发起OA审批单的时候，无需手动输入即可自动将智能人事花名册手机号信息填充到OA表单中。

![花名册字段](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6908968761/p582480.png)

## **视频展示**

[](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20230310/hqzx/获取智能人事花名册字段信息.mp4)

## **步骤一：安装集成连接流**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com)。
2. 单击**开放能力 > 连接平台。**

   ![登录连接平台](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719348761/p581363.png)
3. 单击**连接流市场，**搜索「获取智能人事花名册指定字段信息」。

   ![搜索「获取智能人事花名册指定字段信息」](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719348761/p581370.png)
4. 单击**安装**，打开**安装连接流模板**页面。

   ![安装「获取智能人事花名册指定字段信息」集成流](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719348761/p581373.png)
5. 在**安装连接流模板**页面**，**完成安装。

   ![完成安装](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719348761/p581375.png)
6. 完成安装后，跳转到连接流页面，显示安装成功。

   ![安装成功](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719348761/p581379.png)
7. 开发者可通过**我的连接 > 连接流 > 已安装连接流**查看已安装连接流。

   ![查看已安装连接流](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719348761/p581392.png)

## **步骤二：创建OA审批单**

1. 完成OA基础设置。

   ![OA基础设置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719348761/p581419.gif)

   > **[!IMPORTANT]**
   >
   > 进入OA审批管理后台，必须拥有OA审批应用管理权限，否则该按钮图标不显示。
2. 单击**表单设计，进入连接器配置。**

   ![连接器配置1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719348761/p581483.gif)
3. 选择**连接器**和**执行动作**。

   ![选择连接器和执行动作](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719348761/p581494.png)
4. 配置执行动作并保存。

   1. 数据映射：

      - 填写以下控件的值获取数据：

        - 员工ID：

          ![创建人工号](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719348761/p581499.png)
        - 花名册字段名称：

          ![自定义字段](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719348761/p581513.gif)

          > **[!IMPORTANT]**
          >
          > 输入名称必须与智能人事花名册中的字段名称保持一致，且智能人事花名册中该字段有值。
      - 获取的数据填充到以下控件：

        ![填充数据](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719348761/p581517.png)
   2. 完成保存。

      ![完成保存](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719348761/p581522.png)
5. 发布表单。

   ![发布表单](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719348761/p581524.png)

## **步骤三：功能**体验

当表单发布完成后，可直接使用手机二维码扫码体验即可。

![扫码体验](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719348761/p581529.png)
