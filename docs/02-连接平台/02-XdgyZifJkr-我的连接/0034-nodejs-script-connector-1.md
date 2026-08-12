---
title: "Nodejs脚本连接器"
source_url: "https://open.dingtalk.com/document/connection/nodejs-script-connector-1"
namespace: "connection"
slug: "nodejs-script-connector-1"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发参考 > 创建FAAS执行动作 > Nodejs脚本连接器"
doc_id: "I4bg6yMjgJ"
updated_at: "2026-07-30 09:55:32"
---

> Source: https://open.dingtalk.com/document/connection/nodejs-script-connector-1
> Path: 连接平台 / 我的连接 / 开发参考 > 创建FAAS执行动作 > Nodejs脚本连接器
> Updated: 2026-07-30 09:55:32

# Nodejs脚本连接器

## **简介**

Nodejs脚本连接器是基于Nodejs脚本去实现执行动作执行行为的连接器，用户可基于该连接器进行一些复杂逻辑的处理，包括数据结构转换、网络请求等。

> **[!NOTE]**
>
> 当前可限时进行免费体验。

## **配置说明**

入参配置的属性将会映射到对象input中，对象output对应的属性将会映射到出参设置中。

例如：

- 入参配置字段name，脚本中可以通过input.name取到字段name的值。
- 脚本output.age = 20，可将出参配置字段age的值设置为20后返回。

以node示例为例，脚本如下：

```
var array = input.array;
var result = array.map((val, index) => {
  var key = val[0];
  var value = val[1];
  return {"key":key, "value":value};
});
output.result = result;
```

以上脚本获取到名为array的双层数组参数（内部的数组为固定存储key、value的大小为2的数组），将内部数组的key、value转为对象后返回。

**输入**：

```
{
  "array":[
    [
      "a",
      "b"
    ],
    [
      "c",
      "d"
    ]
  ]
}
```

**输出**：

```
{
  "result":
  [
    {
      "value":"b",
      "key":"a"
    },
    {
      "value":"d",
      "key":"c"
    }
  ]
}
```

## 数据结构转换

执行动作配置：

1. 在连接器的基本信息界面，依次选择**执行动作>创建执行动作**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1134735871/p558590.png)
2. 在基础信息中，选择**API类型**为`FAAS`，然后点击下一步。

   ![FAAS选择..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2134735871/p682801.png)
3. 在入参配置中，选择脚本语言为`Nodejs`，示例中有对应脚本语言实现的详细说明，可根据说明实现自己的脚本。

   ![FAAS-NodeJS..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2356735871/p682804.png)
4. 实现将双层数组转换为对象数组的Nodejs脚本为例，依次**设置脚本代码**、**测试入参**，并点击**脚本测试**，如下图所示：

   ![调试nodeJs..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2356735871/p682973.png)**设置脚本代码**：

   ```
   var array = input.array;
   var result = array.map((val, index) => {
     var key = val[0];
     var value = val[1];
     return {"key":key, "value":value};
   });
   output.result = result;
   ```

   **测试入参**：

   ```
   {
     "array":[
       [
         "a",
         "b"
       ],
       [
         "c",
         "d"
       ]
     ]
   }
   ```

   **测试结果**：

   ```
   {
     "result":
     [
       {
         "value":"b",
         "key":"a"
       },
       {
         "value":"d",
         "key":"c"
       }
     ]
   }
   ```
5. 在「脚本入参」中设置双层数组的入参结构。

   > **[!NOTE]**
   >
   > 入参属性array与Nodejs脚本中从input获取的属性名称一致。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1134735871/p558616.png)
6. 在「脚本出参」中设置对象数组的出参结构，然后单击**下一步**。

   > **[!NOTE]**
   >
   > 出参属性与Nodejs脚本中output中设置的返回key一致。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1134735871/p558622.png)
7. 在调试中，点击**编码模式**，在弹窗中输入示例代码，并单击**立即调试。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1134735871/p558630.png)

   示例代码：

   ```
   {
     "array":[
       [
         "code1","钉钉"
       ],
       [
         "code2","让进步发生"
       ]
     ]
   }
   ```
8. 如果显示**调试成功**且状态码为`200`，则结构转换的FAAS连接器已经配置完成，最后点击**发布**即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1134735871/p558648.png)
