---
title: "自动化流程使用指南"
source_url: "https://open.dingtalk.com/document/connection/automated-process-usage-guide"
namespace: "connection"
slug: "automated-process-usage-guide"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "自动化流程使用指南"
doc_id: "xKVD6wtVhk"
updated_at: "2025-09-23 19:21:37"
---

> Source: https://open.dingtalk.com/document/connection/automated-process-usage-guide
> Path: 连接平台 / 连接平台自动化 / 自动化流程使用指南
> Updated: 2025-09-23 19:21:37

# 自动化流程使用指南

## **创建自动化流程**

### **场域说明**

#### **群聊自动化**

**创建权限**

在自动化小助手内，不同群成员可以创建多条不同的自动化流程，不同群成员的创建权限如下：

| **群主和群管理员** | **普通群成员** |
| --- | --- |
| 可以创建自动化流程 | 群设置 > 群管理 > **仅群主和群管理员可管理**的开关关闭时（如下图），才可以创建自动化流程image.png |

### **创建方式**

创建自动化流程的方式有以下两种：

- 从模板创建流程：适合新手用户，模板内提供预置的触发条件和执行动作，可在此基础上进行修改编辑
- 从空白创建流程：适合有经验的用户，自定义选择触发条件和执行动作，并自定义配置其具体内

### **从模板创建流程**

1. 顶部 TAB 切换至**流程模板**，选择一款模板，单击**使用模板**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1953786071/p754742.png)
2. 模板提供了预置的触发条件和执行动作，可在此基础上，根据自己的需求配置**触发条件**和**执行动作**的具体内容。

   1. 配置触发条件：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2953786071/p754745.png)
   2. 配置执行动作：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1953786071/p754747.png)
3. 当所有节点由橙色标识的 **!** 转变为绿色标识 **✓** 时，代表触发条件和执行动作配置成功，单击右上角流程名称，可以**修改流程名称**。单击右上角**保存并启用**按钮，即可保存并启动流程。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1953786071/p754751.png)

### **从空白创建流程**

1. 在流程管理页单击**从空白创建**，或在流程模板页单击**从空白创建：**

   1. 流程管理页创建：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0953786071/p754754.png)
   2. 流程模板页创建：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0953786071/p754755.png)
2. 选择**触发条件**，并配置其具体内容：

   1. 选择触发条件

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0953786071/p754757.png)
   2. 配置触发条件：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1953786071/p754759.png)
3. 选择**执行动作**，并配置其具体内容：

   1. 选择执行动作：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0953786071/p754760.png)
   2. 配置执行动作：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1953786071/p754761.png)
4. 根据需要，向上/向下**增加新的执行动作**；或者根据需要，**删除执行动作**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1953786071/p754766.png)
5. 当所有节点由橙色标识的 **!** 转变为绿色标识 **✓** 时，代表触发条件和执行动作配置成功，单击右上角流程名称，可以**修改流程名称**。单击右上角**保存并启用**按钮，即可保存并启动流程。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2953786071/p754771.png)

## **管理自动化流程**

### **全局管理**

顶部TAB切换至**流程管理**，可以对流程进行全局管理。

1. 在**最近运行**模块中，可以查看最近运行的流程名称和对应的运行时间；
2. 在**下方流程列表**中，可以看见创建的**全部流程、运行中的流程、未启用的流程**。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2953786071/p754775.png)

### **具体流程管理**

除了管理员外，**普通成员只能管理（查看/编辑/删除）自己创建的流程**，而不能管理他人创建的流程。

1. 在流程列表中，可通过**开关按钮**控制流程的状态：**按钮打开时流程运行**，**按钮关闭时流程禁用**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0953786071/p754776.png)
2. 选择其中一个流程，**点击更多**，可对流程进行**编辑**或**删除**。单击流程的**空白区域**，也可**进入流程编辑页面**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1953786071/p754777.png)
3. 在**流程编辑页面**，点击左上角**执行记录**，可查看流程的**累计执行次数、执行成功次数、执行失败次数**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0953786071/p754778.png)
4. 单击某次执行记录的**详情**，可以**一键复制错误信息**，进行原因排查。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2953786071/p754779.png)

## **移除自动化流程**

### **群聊自动化**

#### **移除权限**

只有**群主、群管理群、自动化小助手的创建者**，才有移除权限。

#### **操作步骤**

1. 单击右上角**更多**图标，然后再单击**移除机器人**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0953786071/p754785.png)
2. 单击**移除**，即可移除自动化小助手。

   > **[!IMPORTANT]**
   >
   > 移除后，所有群成员创建的自动化流程都将失效。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2953786071/p754786.png)
