---
title: "创建数据源"
source_url: "https://open.dingtalk.com/document/dingstart/dashboard-create-data-source"
namespace: "dingstart"
slug: "dashboard-create-data-source"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > 数据源 > 创建数据源"
doc_id: "IAYNJtakWu"
updated_at: "2025-10-20 17:26:46"
---

> Source: https://open.dingtalk.com/document/dingstart/dashboard-create-data-source
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > 数据源 > 创建数据源
> Updated: 2025-10-20 17:26:46

# 创建数据源

创建数据源就是将服务接口注册在钉钉的网关上，当组件发起请求时，钉钉网关会将 corpId、userId 植入进来传递给服务端接口。

## 操作流程

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/plugin)。
2. 然后依次单击**定制服务** > **数据源管理** > **新建数据源**。

   ![数据源](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3233658161/p262557.png)
3. 在弹出的**新建数据源**页面中填写数据源基本信息。

   ![填写注册信息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1026432161/p232907.png)

   **字段说明：**

   - **apiKey**：apiKey 是这个数据源的唯一标识，可自定义，由英文大小写组成，作为系统中对数据源的唯一识别码。

     例如：组件中需要用到一个数据源，那么在`config.json`的配置信息中需要用到 apiKey。

     ```
     // config.json 中的片段
     {
         ...
         "dataSources": [{
             "apiKey": "getChartData",
             "propName": "getChartDataApi",
         }],
         ...
     }
     ```
   - **apiSecret**：apiSecret 可以填写你和服务端同学约定的任意值，作为签名密钥，在获取用户身份时，供服务端接口识别这是来自钉钉的请求。
   - **参数**：请输入接口的所有参数名，多个参数名以英文逗号分隔，例如 param1，param2。

     无需设置 userid 和 corpid 参数，接口可以自动解析得到。
4. 数据源注册完成后，单击**测试**，测试数据源。

   测试数据源时，不需要填写参数 corpId 和 userid。服务端可以接收到 corpId 和 userid，服务端接收到的 corpId 为**当前企业的 corpId**，userid 为当前企业中**当前用户的 userid**。

   ![测试数据源](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1026432161/p232928.png)
5. 注册后的数据源，可以在服务商视角的设计器的数据源选择器中选到。也可以在 config.json 中的 **dataSources** 字段中使用。

   ![使用实践？](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1026432161/p232934.png)

   > **[!NOTE]**
   >
   > 在组件中使用选中的数据源，详见[在组件内发送请求](0015-send-a-request-within-a-component.md)。
