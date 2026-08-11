---
title: "使用连接器"
source_url: "https://open.dingtalk.com/document/connection/using-connectors-1"
namespace: "connection"
slug: "using-connectors-1"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发连接器 > 使用连接器"
doc_id: "t8xLeOm72W"
updated_at: "2025-09-23 19:20:09"
---

> Source: https://open.dingtalk.com/document/connection/using-connectors-1
> Path: 连接平台 / 开发指南 / 开发连接器 > 使用连接器
> Updated: 2025-09-23 19:20:09

# 使用连接器

本文将介绍如何在连接流中使用自建连接器的触发事件和执行动作。

## **前提条件**

- 完成[添加触发事件](0014-add-trigger-event-1.md)/[添加执行动作](0015-add-execution-action-1.md)的流程。

## **操作步骤**

### **使用触发事件**

> **[!NOTE]**
>
> 连接器的触发事件可作为连接流的首节点，用于触发流程运行。如果你已经发布过触发事件，可以在流程中[配置触发事件](0004-configure-trigger-events-1.md)。

当连接器事件被触发后会发送到钉钉连接器服务中，钉钉会将这些事件再广播转发给订阅了此事件的其它业务系统，触发方式主要有以下两种方式：

- #### **方式一（推荐）：通过Webhook地址触发事件**

  1. 在触发事件列表，选择创建好的触发事件，依次单击**更多>查看Webhook**。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5743786071/p758158.png)
  2. 复制Webhook地址。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6743786071/p758162.png)
  3. 打开接口请求工具，将获取的Webhook地址放到**request URL**中，并将请求类型设置为**POST**。

     > **[!NOTE]**
     >
     > 能请求钉钉接口的系统或工具，此处以postman工具作为演示。

     ![postman-webhook..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6554055861/p675075.png)
  4. 选择**Body**，然后选择**JSON**数据类型。![postman-body..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6554055861/p675085.png)
  5. 构建请求参数，并单击**Send**发起请求。

     ![postman-send..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6554055861/p675088.png)
- #### **方式二：通过接口触发事件**

  通过调用[发送连接器事件](0048-dingtalk-connector-data-synchronization-interface.md)接口，触发连接器事件。

### **使用执行动作**

连接器的执行动作可作为连接流的执行节点，能够在流程被触发后，完成一些具体的业务操作。如果你已经发布过执行动作，可以在流程中[配置执行动作](0005-configure-execution-actions-1.md)。

## **后续步骤**

如果你需要上架连接器，可以参考[上架连接器](0017-connector-shelf-specification-1.md)。

> 上架连接器需要成为钉钉的[产品方案商](../../01-应用开发/07-TjCzIgfQs3-平台服务/0028-become-an-application-service-provider.md)。
