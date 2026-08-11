---
title: "事件链"
source_url: "https://open.dingtalk.com/document/development/chain-of-events"
namespace: "development"
slug: "chain-of-events"
group: "互动卡片"
tab: "卡片模板搭建器"
breadcrumb: "添加卡片交互 > 事件链"
doc_id: "uozu6spWyw"
updated_at: "2025-09-23 19:18:35"
---

> Source: https://open.dingtalk.com/document/development/chain-of-events
> Path: 互动卡片 / 卡片模板搭建器 / 添加卡片交互 > 事件链
> Updated: 2025-09-23 19:18:35

# 事件链

本文将介绍什么是事件链以及如何配置使用事件链。

## **事件链**

针对单次事件，允许配置并编排多个异步事件，同时支持配置这些异步事件的成功、失败回调的事件类型就是事件链。

## **为什么使用事件链**

用户可以为单次事件配置多个事件。在事件链中，这些事件将异步执行。例如，在按钮点击事件中需要同时更新本地变量、调用回传请求这种场景就可以使用事件链来完成。此外，事件链支持为部分事件设置成功、失败回调，例如可以在回传请求成功或失败时进行不同的弹窗内容提示。

## **配置事件链**

1. 选中需要配置事件链的组件，单击**事件** > **事件类型**，选择**事件链**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6799089071/p772723.png)
2. 单击**编辑事件链**，打开编辑事件链弹窗。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6799089071/p772749.png)
3. 在编辑事件链弹窗中，你可以进行事件链的配置了，通过单击**新增事件**来添加需要调用的事件类型。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7799089071/p772753.png)
4. 以回传请求为例，根据业务需求，在下方表单中填入回传参数：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7799089071/p775454.png)

到这里，你就已经完成基础的事件链配置了。

## **事件链的执行顺序**

在事件链中，所有配置的事件会按照定义的顺序异步执行。每个事件可以独立执行，互不阻塞。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6799089071/p772762.png)

事件链的几个主要步骤：

1. 触发事件链：当一个触发条件（如按钮点击、容器点击）满足时，事件链启动。
2. 顺序执行事件：事件链中的事件按照配置顺序依次执行，但每个事件是异步的，不会等待前一个事件完成。
3. 回调处理：每个事件可以配置成功和失败回调，事件链会根据事件的执行结果，调用相应的回调处理事件。

## **事件链的回调配置**

如果需要在事件执行后进行一些后续操作，可以通过事件链的回调来实现。目前支持回调的事件有：回传请求、动作面板等。回传请求的具体配置可以参考文档[事件回调](../01-N4KJ5HbqnQ-开发指南/0007-event-callback-card.md)。

事件的回调分为成功回调和失败回调，每个事件回调可以配置以下内容：

| 事件回调类型 | 成功回调 | 失败回调 |
| --- | --- | --- |
| 定义 | 当事件成功执行后，要进行的操作。 | 当事件执行失败后，要进行的操作。 |
| 配置方法 | 在事件链事件的事件回调里选择**添加事件执行成功回调**。 | 在事件链事件的事件回调里选择**添加事件执行失败回调**。 |
| 例子 | 回传请求调用成功后，弹窗提示成功信息。 | 回传请求调用失败后，弹窗提示失败信息。 |

### **配置事件回调**

在支持配置回调的事件中单击**添加回调**，就可以选择对应的事件执行结果的回调配置：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6443889171/p815923.png)

这里的事件回调配置与上面的事件链配置类似，不同的是这里的事件执行成功回调配置可以使用事件返回值。

### **使用事件返回值**

如果你需要使用事件的返回值进行配置，你可以参考下方内容：

- 如果当前字段类型已经确定为事件返回值，对应的事件链返回值变量格式应为：`cardData/cardPrivateData.****`。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6443889171/p815921.png)
- 如果是固定值类型，使用事件返回值的格式应为：`${event.cardData/cardPrivateData.****}`。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6443889171/p815920.png)

  具体是使用 cardData 还是 cardPrivateData 请根据服务端事件回调返回的数据结构来确定，这里填写的参数层级需与服务端下发的数据结构保持一致。
- 如果希望根据条件（运行环境、变量、事件返回值）来配置不同执行的事件，还可以通过单击**条件**按钮来配置附加的执行条件，使得仅当事件的返回结果与配置的条件相匹配时，才会触发设定的回调。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6443889171/p815922.png)

  > **[!IMPORTANT]**
  >
  > 回传请求成功：指的是回传的网络请求发送成功。
  >
  > 回传请求失败：指的是回传的网络请求发送失败。

## **常见用法**

### **回传请求后弹窗提示回调结果**

1. 添加**回传请求**事件，并配置相关参数：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7799089071/p775456.png)
2. 添加事件的成功和失败回调，事件回调类型选择**弹窗提示**，并配置需要提示的内容：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6799089071/p775458.png)

   假设业务服务端[事件回调](../01-N4KJ5HbqnQ-开发指南/0007-event-callback-card.md)返回的数据为：

   ```
   {
     "cardData": {
       "cardParamMap": {
         "result": "https://open-dev.dingtalk.com/fe/card"
       }
     },
     "userPrivateData": {
       "cardParamMap": {}
     },
     "cardUpdateOptions": {
       "updateCardDataByKey": true,
       "updatePrivateDataByKey": true
     }
   }
   ```

   实现效果应为：

   ![image.gif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7799089071/p772165.gif)

### **点击按钮后禁用按钮并回传请求，请求返回后按钮恢复可点击状态**

1. 添加**更新本地变量**事件，将控制按钮状态的变量`buttonStatus`更新为`disabled`：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6799089071/p775460.png)
2. 添加**回传请求**事件并配置相关参数：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5799089071/p775463.png)
3. 添加**事件成功回调**和**事件失败回调**，并在其中将`buttonStatus`更新为`normal`：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6799089071/p775466.png)

   > **[!NOTE]**
   >
   > 由于这里需要将按钮的初始值设为`normal`，但是本地变量的初始值为空，所以需要将按钮的状态绑定一个[表达式变量](0012-variable-type.md#d5f7b6e08c31r)，参考如下实现：
   >
   > ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5799089071/p772173.png)

   实现效果应为：

   ![image.gif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6799089071/p772171.gif)

## **相关内容**

事件链使用的代码示例：[事件链配置演示](https://github.com/open-dingtalk/dingtalk-card-examples/tree/main/examples/事件链配置演示)。

如果你需要了解更多互动卡片示例，请参考[互动卡片示例中心](https://github.com/open-dingtalk/dingtalk-card-examples)。
