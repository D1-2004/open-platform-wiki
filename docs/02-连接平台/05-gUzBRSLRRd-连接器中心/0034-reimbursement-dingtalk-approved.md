---
title: "差旅报销钉钉 OA 申请审批通过后同步到金蝶云星空"
source_url: "https://open.dingtalk.com/document/connection/reimbursement-dingtalk-approved"
namespace: "connection"
slug: "reimbursement-dingtalk-approved"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "三方连接器 > 使用教程 > 金蝶云星空 > 差旅报销钉钉 OA 申请审批通过后同步到金蝶云星空"
doc_id: "pe6S0e4eAi"
updated_at: "2026-05-19 19:46:24"
---

> Source: https://open.dingtalk.com/document/connection/reimbursement-dingtalk-approved
> Path: 连接平台 / 连接器中心 / 三方连接器 > 使用教程 > 金蝶云星空 > 差旅报销钉钉 OA 申请审批通过后同步到金蝶云星空
> Updated: 2026-05-19 19:46:24

# 差旅报销钉钉 OA 申请审批通过后同步到金蝶云星空

本教程介绍了如何通过钉钉连接平台配置连接流，实现钉钉OA审批和金蝶云星空的数据连通。

## **准备工作**

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 完成配置金蝶云星空环境，已经获取云星空系统的用户登录名、密码、账套Id（数据中心Id）以及系统的访问域名，支持私有云（需配置网关）和公有云两种形式。

## **配置连接流**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 单击**开放能力**>**连接平台**>**我的连接 >我的连接流**>**创建连接流**。
3. 配置触发事件：

   1. 选择**官方连接器**> **审批**。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0452622071/p745415.png)
   2. 触发事件选择**审批实例变更**。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0452622071/p745416.png)
4. 配置执行动作（节点2）:

   1. 选择**官方连接器 > 审批**，执行动作选择**获取单个审批实例详情**。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0452622071/p745422.png)
   2. 配置参数，审批实例选择上个触发事件节点中的**审批实例id。**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0452622071/p745423.png)
5. 配置执行动作（节点3）：

   1. 选择**内置工具** > **FaaS脚本**，执行动作选择**Python脚本**。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0452622071/p745426.png)
   2. 新增入参变量，选择表达式模式，内容为节点2的返回结果。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0452622071/p745430.png)
   3. 设置代码，填充以下代码：

      ```
      from collections import defaultdict

      array = input["result"]["result"]
      targetValue = array["formComponentValues"]
      result = defaultdict(list)
      for a in targetValue:
          key = a["name"]
          value = a["value"]
          result[key] = value
      output = {"result": result}
      ```
6. 配置执行动作（节点4）：

   1. 选择**三方连接器 > 金蝶云星空**，执行动作选择**采购申请暂存**。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0452622071/p745433.png)
   2. 配置账号，根据准备工作的信息，完成鉴权。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0452622071/p745435.png)
   3. 配置参数：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0452622071/p745437.png)
7. 调试并发布连接流。

## 配置OA审批表单

1. 登录钉钉客户端，单击**工作台** > **审批**。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0452622071/p745441.png)
2. 单击管理后台。进入后台管理页面。

   > **[!IMPORTANT]**
   >
   > 进入OA审批管理后台，必须拥有OA审批应用管理权限，否则该按钮图标不显示。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2371732071/p746487.png)
3. 创建表单，配置表单内容。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2371732071/p746488.png)
4. 配置完成后，发布表单**。**

## 恭喜，你已完成全部配置！

1. 你可以根据上述创建的OA审批表单，发起审批实例。
2. 查看连接流的执行情况。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2371732071/p746489.png)
3. 查看金蝶系统的数据同步情况。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0253786071/p746815.png)
