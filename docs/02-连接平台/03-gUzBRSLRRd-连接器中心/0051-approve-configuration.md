---
title: "审批配置"
source_url: "https://open.dingtalk.com/document/connection/approve-configuration"
namespace: "connection"
slug: "approve-configuration"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > OA审批 > 操作手册 > 审批配置"
doc_id: "AFpcrT98Jp"
updated_at: "2025-09-23 19:21:11"
---

> Source: https://open.dingtalk.com/document/connection/approve-configuration
> Path: 连接平台 / 连接器中心 / 官方连接器 > OA审批 > 操作手册 > 审批配置
> Updated: 2025-09-23 19:21:11

# 审批配置

## 表单设置

用户可在**OA审批**表单设计器中选择相应的触发条件，并绑定相应的接口，当前支持的触发条件如下：

- **新建表单加载时**：当打开表单时触发，可以通过接口自动给某些表单控件赋值。
- **控件值发生变化时**：当表单中某些控件值发生变化后调用接口，自动给其他表单控件赋值。
- **表单提交（含发起人重新提交）时验证**：当单击提交按钮时，通过接口对数据进行校验，如不通过则阻断用户发起审批。

在**表单设计器**界面，单击**连接器**按钮，在右侧可以看到已配置的接口，同时也可以新建、编辑、删除操作。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8751370571/p976688.png)

## 触发条件

单击**新建/编辑**后，根据自身业务需求选择触发条件。

![触发条件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6873109661/p381151.png)

## 选择执行动作

在**选择连接器**下，选择相应的连接器和执行动作。

> **[!NOTE]**
>
> 连接器和执行动作如何创建，详情请参考[创建连接器](../02-iO2mVD3wB2-开发指南/0013-create-connector.md)、[添加触发事件](../02-iO2mVD3wB2-开发指南/0014-add-trigger-event-1.md)、[添加执行动作](../02-iO2mVD3wB2-开发指南/0015-add-execution-action-1.md)。

![选择执行动作](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7873109661/p381153.png)

## 配置执行动作

在**配置执行动作**下，填写控件的值用于获取数据，并设置获取的数据填充到控件。

![配置执行动作](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7873109661/p381154.png)

- 对于触发条件为**新建****表单加载时**、**控件值发生变化时**的执行动作，可以将执行动作出参映射到表单组件，实现表单数据的自动填充。

  - **客户列表.选项列表.ID列表**：表示选项的key，类似于身份证号码，每一个选项的key唯一，不展示。
  - **客户列表.选项列表.值列表**：表示选项展示的值，可重复。
- 对于触发条件为**表单提交时验证**的执行动作，**校验结果**（Boolean类型参数）和**校验错误信息**（String类型参数）为其固定的2个出参参数，此时连接器执行引擎会根据执行动作的回参实现表单校验功能：

  - 当**校验结果=true**时执行审批流。
  - 当**校验结果=false**时阻断审批发起，并弹出**校验错误信息**进行提示。

## 流程设置

用户可在OA审批流程设计器中绑定相应的集成接口或子流程，实现表单的自定义审批人，分支条件判断，同步数据等功能。

## 节点设置

1. 单击“**+**”符号，选择添加系统集成节点。

   ![设置节点](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0377956661/p381155.png)
2. 选择相应的连接器和执行动作。

   ![选择执行动作](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9277956661/p381156.png)
3. 在连接器模块下，配置执行动作。

   ![最后一步](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4059771461/p381157.png)

   如需开启同步调用功能，请确保动态流程开已启。

   ![OA审批-OA审批配置-开启动态流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7873109661/p522077.png)

   **是否开启同步调用**：表示执行动作支持同步调用和异步调用

   - **同步**：当流程引擎执行到该节点时，将同步等到连接器执行结果，如果调用失败或超时，审批流将终止执行。但同步执行支持以下功能：

     - 执行动作出参可以作为审批流分支条件。
     - 执行动作出参可以作为审批人选择条件。
   - **异步**：当流程引擎执行到该节点时，流程引擎不等待连接器执行结果，继续后续审批流程。如果连接器节点执行失败，将进行三次重试。
