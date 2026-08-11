---
title: "步骤七：服务商导出工作台列表"
source_url: "https://open.dingtalk.com/document/services/step-7-export-console-list-from-service-providers-1"
namespace: "services"
slug: "step-7-export-console-list-from-service-providers-1"
group: "应用开发"
tab: "平台服务"
breadcrumb: "合作指南 > 产品方案商 > 定制业务的合作指引 > 自定义工作台开发流程 > 步骤七：服务商导出工作台列表"
doc_id: "Mlic76Gx03"
updated_at: "2025-09-23 19:22:13"
---

> Source: https://open.dingtalk.com/document/services/step-7-export-console-list-from-service-providers-1
> Path: 应用开发 / 平台服务 / 合作指南 > 产品方案商 > 定制业务的合作指引 > 自定义工作台开发流程 > 步骤七：服务商导出工作台列表
> Updated: 2025-09-23 19:22:13

# 步骤七：服务商导出工作台列表

本文介绍服务商如何根据时间区间获取工作台列表。

1. 服务商登录[开发者后台](https://open-dev.dingtalk.com/)，选择**定制服务> 工作台定制 > 自定义工作台**，然后在页面右上角单击**导出工作台列表**，如下图所示：

   ![导出工作台列表 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7936275261/p230916.png)
2. 选择需要导出的时间区间，然后单击**导出**。

   ![导出时间区间列表](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7816432161/p230920.png)

   工作台列表中包括如下字段：

   - **订单号**：包括正式订单和试用订单，订单号为空，则表示客户仅完成了委托（即“客户已委托”状态），但服务商未下订单。
   - **工作台名称**：工作台名称。
   - **工作台类型**：包括定制版、专业版、专属定制，“专属定制”类型为只下意向单但未下订单时候的默认类型。
   - **客户名称**：客户名称。
   - **工作台创建时间**：即客户完成委托单确认时创建工作台的时间。
   - **工作台状态**：包括客户已委托、开发中、待客户确认、已发布、无效商机，几个状态相互互斥。
   - **下单时间**：服务商下订单时间。
   - **支付状态**：包括待支付和已支付，为空则表示没有对应需要支付的订单。
   - **支付时间**。：支付时间。
   - **支付金额**：试用订单金额为0.0。
   - **到期时间**：从支付完成订单生效后开始计算的到期时间。
   - **服务商小二名称**：当前为服务商入驻时默认登记的小二名称。
