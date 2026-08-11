---
title: "上架连接器"
source_url: "https://open.dingtalk.com/document/connection/connector-shelf-specification-1"
namespace: "connection"
slug: "connector-shelf-specification-1"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发连接器 > 上架连接器"
doc_id: "HqyODTtiSw"
updated_at: "2025-09-23 19:20:09"
---

> Source: https://open.dingtalk.com/document/connection/connector-shelf-specification-1
> Path: 连接平台 / 开发指南 / 开发连接器 > 上架连接器
> Updated: 2025-09-23 19:20:09

# 上架连接器

连接器发布完成后，如果你需要上架连接器，可以参考本文档操作步骤。

## **前提条件**

- 入驻成为[产品方案商](../../01-应用开发/07-TjCzIgfQs3-平台服务/0028-become-an-application-service-provider.md)。
- 完成[使用连接器](0016-using-connectors-1.md)的流程。

## **操作步骤**

### **上架前自检**

1. 检查基本信息填写：

   | **检查项** | **说明** |
   | --- | --- |
   | 连接器名称 | 非特殊情况外，不应带有客户信息或组织信息，即不应该有为某某组织专属的含义。 |
   | 连接器描述 | 应注明执行动作的使用场景，涉及的系统功能。 |
   | 连接器图标 | 不存在敏感信息或其他容易引发争议的元素。 |

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9794786071/p766350.png)
2. 检查出入参配置：

   - 字段key值：驼峰写法首字母小写。例如：

     - 正确：greenApple。
     - 不推荐：green\_apple。
     - 错误：green-apple，如无特殊原因不应该包含特殊符号。
   - 字段名称：简单描述字段对应显示的名称即可，不需要将描述信息直接填写。
   - 字段描述：

     - ID类字段：描述清楚ID获取的途径方式，来源系统等。
     - 枚举类字段：描述清楚枚举的全部值及其对应含义，或给出可以获取这些信息的地方。
     - 时间或日期类字段：描述清楚时间的具体格式，如果是数字时间戳描述清楚单位是毫秒还是秒，如果是字符按照yyyyMMdd HH:mm:ss（年月日 时:分:秒）给出时间格式模板。
   - 字段是否必须：应该严格按照实际要求来，如果出现使用过程中，因非必须字段传值出现调用问题，应在备注里说明，否则应该要求改正。

     > **[!NOTE]**
     >
     > 时间类型、ID类型、枚举值参数需要在备注中说明清楚。

### **上架**

1. 登录[开发者后台](https://open-dev.dingtalk.com)，单击**开放能力** > **连接平台** > **服务商** > **上架连接器**。
2. 单击需要上架的连接器，进入对应连接器的上架页面。
3. 单击上架，按照提示完成连接器上架操作。

   > **[!NOTE]**
   >
   > - 注明新增或修改哪些执行动作、触发事件，修改需要注明是否有调整参数的情况。
   > - 无须备注连接器的使用场景，这些应该调整放到连接器、执行动作、触发事件的描述里。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9794786071/p766359.png)
