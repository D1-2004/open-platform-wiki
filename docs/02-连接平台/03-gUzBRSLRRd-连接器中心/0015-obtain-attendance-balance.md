---
title: "获取考勤调休余额"
source_url: "https://open.dingtalk.com/document/connection/obtain-attendance-balance"
namespace: "connection"
slug: "obtain-attendance-balance"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 考勤 > 使用教程 > 获取考勤调休余额"
doc_id: "t7Ztfx25EE"
updated_at: "2026-05-19 16:01:45"
---

> Source: https://open.dingtalk.com/document/connection/obtain-attendance-balance
> Path: 连接平台 / 连接器中心 / 官方连接器 > 考勤 > 使用教程 > 获取考勤调休余额
> Updated: 2026-05-19 16:01:45

# 获取考勤调休余额

## **简介**

本教程介绍了如何通过OA管理后台配置子流程，实现OA审批发起时自动获取提交人调休总剩余额度。

## **准备工作**

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 已开通[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)（OA审批中使用连接器必备）。

## **步骤一：配置连接流**

1. [创建连接流](../02-iO2mVD3wB2-开发指南/0002-create-a-connection-flow-1.md)，并完善连接流基本信息。
2. 配置触发事件：

   1. 选择**内置工具** > **子流程**。

      ![子流程设置-调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696369.png)
   2. 单击**设置入参，**并完善参数信息。

      ![设置userid-调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696373.png)
   3. 完成配置。

      ![完成触发事件-调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696376.png)
3. 配置执行动作：

   1. 选择官方连接器。

      ![执行动作选择-考勤规则-调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696379.png)
   2. 选择执行动作 > **查询假期规则列表**。

      ![查询假期规则-调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696381.png)

      1. 单击**点击进行配置**，实现参数配置。
      2. 测试并预览：

         1. 输入测试值。

            ![调试-调休查询.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696392.png)
         2. 完成测试。

            ![完成调试-假期规则-调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696390.png)此时，我们可以看到**调休**的唯一标识`leave_code`**。**
   3. 添加执行动作，并选择执行动作 > **查询假期规则列表**。

      ![查询假期余额-调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696403.png)

      1. 单击**点击进行配置**，实现参数配置。
      2. 测试并预览。

         1. 输入测试值。

            ![假期余额调试-调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696407.png)
         2. 完成测试。

            > **[!NOTE]**
            >
            > 需在[钉钉管理后台](https://oa.dingtalk.com/admin/portal/oa#?lang=zh_CN&nation=CN)设置假期管理，否则返回信息为空。

            ![完成调试-假期余额-调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696409.png)

            此时，我们可以看到**调休总额小时数**为40小时，**使用调休额度**为0小时。
   4. 设置出参。

      1. 设置出参字段。

         ![出参-调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696416.png)
      2. 单击**点击进行配置**，实现出参配置。

         > **[!NOTE]**
         >
         > 处理调休余额以小时为单位。
      3. 测试、预览并完成**保存**。

         ![保存出参.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696422.png)
   5. 发布连接流。

      ![发布连接流-调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696428.png)

## **步骤二：配置OA审批单**

1. 登录钉钉客户端，单击**工作台** > **审批**。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696429.png)

2. 单击管理后台。进入后台管理页面。

> **[!IMPORTANT]**
>
> 进入OA审批管理后台，必须拥有OA审批应用管理权限，否则该按钮图标不显示。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696430.png)

3. 创建新表单，选择**流程表单**。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696437.png)

4. 表单设计。

   1. 设置表单组件，选择**数字输入框**。

      ![设置调休余额（小时）OA.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696455.png)
   2. 配置连接器。

      1. 添加连接器。

         ![添加连接器-调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696458.png)
      2. 设置触发条件。

         ![设置触发条件-OA调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696460.png)
      3. 选择连接器。

         ![选择连接器-OA调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696464.png)
      4. 配置执行动作并保存。

         ![保存执行动作-OA调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696472.png)
      5. 发布流程表单。

         ![发布OA审批流程-调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696476.png)

## 恭喜，你已完成全部配置！

你已完成本教程的全部内容，可以通过以下方式进行体验。

1. 进入钉钉客户端**工作台** > **审批**。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696480.png)

2. 选择上述发布的表单，并查看调休余额。

![查看调休余额.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1206330961/p696485.png)
