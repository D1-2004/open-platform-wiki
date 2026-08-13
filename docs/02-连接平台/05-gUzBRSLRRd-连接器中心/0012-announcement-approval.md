---
title: "OA审批通过后发布公告"
source_url: "https://open.dingtalk.com/document/connection/announcement-approval"
namespace: "connection"
slug: "announcement-approval"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 使用教程 > 公告 > OA审批通过后发布公告"
doc_id: "KV0bTS4PL4"
updated_at: "2026-07-30 09:19:01"
---

> Source: https://open.dingtalk.com/document/connection/announcement-approval
> Path: 连接平台 / 连接器中心 / 官方连接器 > 使用教程 > 公告 > OA审批通过后发布公告
> Updated: 2026-07-30 09:19:01

# OA审批通过后发布公告

本教程介绍了通过OA管理后台配置公告连接器后，实现OA表单审批通过后发布公告。

## **基本流程**

OA审批通过后发布公告基本流程，如下图所示：

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2586813961/p707247.png)

## **预期效果**

![预期效果-公告通知.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0908925871/p707266.png)

## **准备工作**

- 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
- 已开通[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)。（OA审批中使用连接器必备）。

## **步骤一：**创建OA审批表单

1. 登录钉钉客户端，单击**工作台** > **审批**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0908925871/p707248.png)
2. 单击**管理后台**。进入后台管理页面。

   > **[!IMPORTANT]**
   >
   > 进入OA审批管理后台，必须拥有OA审批应用管理权限，否则该按钮图标不显示。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0908925871/p707249.png)
3. 单击**创建新表单**，选择**流程表单**，填写**基础设置**信息。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0908925871/p707252.png)
4. 在**表单设计**界面添加表单控件，选择一个**单行输入框**和一个**多行输入框**，完成OA审批的界面设计。

   ![选择公告控件.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0908925871/p707262.png)

## **步骤二：**配置连接器

1. 单击**流程设计** > **审批人后的“+”号** > **连接器**。

   ![添加连接器节点.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0908925871/p707254.png)
2. 在侧边栏弹出页面：

   1. 选择连接器：公告。
   2. 选择连接器的执行动作：创建企业公告。

      ![连接器选择和执行动作选择.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0908925871/p707255.png)

      选择完成后，单击下一步。
3. 在配置执行动作页面中，填写控件的值用于获取数据：

   - 操作人的userId：选择**系统参数** > **创建人工号**。
   - 公告标题：选择**表单字段** > **公告标题**。
   - 公告内容：选择**表单字段** > **公告内容**。

     ![公告参数配置.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6617925871/p707257.png)

     配置完成后，单击**保存。**

     > **[!NOTE]**
     >
     > 更多参数详情，请参见[公告参数说明-创建企业公告](https://open.dingtalk.com/document/connection/1)。
4. 保存完成后，单击发布，即可完成审批表单全部配置。

   ![完成公告审批表单创建.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0908925871/p707258.png)

## 恭喜，你已完成全部配置！

你已完成本教程的全部内容，可以通过以下方式进行体验。

1. 进入钉钉客户端**工作台**>**审批**。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0908925871/p707259.png)
2. 选择上述发布的表单，填写信息并提交表单。

   > **[!NOTE]**
   >
   > 公告内容中可以使用HTML语言编辑内容，如：<img/>、<br/>、<b>标签，且图片标签中的路径必须是公网可访问的。

   ![发起公告审批.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0908925871/p707264.png)
