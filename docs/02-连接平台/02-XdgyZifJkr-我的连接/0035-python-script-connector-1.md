---
title: "Python脚本连接器"
source_url: "https://open.dingtalk.com/document/connection/python-script-connector-1"
namespace: "connection"
slug: "python-script-connector-1"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发参考 > 创建FAAS执行动作 > Python脚本连接器"
doc_id: "NoP5lkyKQT"
updated_at: "2026-07-30 09:18:31"
---

> Source: https://open.dingtalk.com/document/connection/python-script-connector-1
> Path: 连接平台 / 我的连接 / 开发参考 > 创建FAAS执行动作 > Python脚本连接器
> Updated: 2026-07-30 09:18:31

# Python脚本连接器

## **简介**

Python脚本连接器是基于Python脚本去实现执行动作执行行为的连接器，用户可基于该连接器进行一些复杂逻辑的处理，包括数据结构转换、网络请求等。

> **[!NOTE]**
>
> 当前可限时进行免费体验。

## **配置说明**

入参配置的属性将会映射到字典input中，字典output对应的属性将会映射到出参设置中。

例如：

- 入参配置字段name，脚本中可以通过input["name"]取到字段name的值。
- 出参output.update({"age":20})，可将出参配置字段age的值设置为20后返回。

以Python示例为例，脚本如下：

```
array = input["array"] 
result = [] 
for a in array: 
  key = a[0] 
value = a[1] 
result.append({"key": key, "value":value}) 
output.update({"result": result})
```

以上Python脚本获取到名为array的双层数组参数（内部的数组为固定存储key、value的大小为2的数组），将内部数组的key、value转为对象后返回。

**输入**:

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

**输出:**

```
{
  "result":[
    {
      "key":"a",
      "value":"b"
    },
    {
      "key":"c",
      "value":"d"
    }
  ]
}
```

## 示例一：数据结构转换

执行动作配置：

1. 在连接器的基本信息界面，依次选择**执行动作>创建执行动作**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1134735871/p558590.png)
2. 在基础信息中，选择**API类型**为`FAAS`，然后点击下一步。

   ![FAAS选择..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2134735871/p682801.png)
3. 在入参配置中，选择脚本语言为`Python`，示例中有对应脚本语言实现的详细说明，可根据说明实现自己的脚本。

   ![Python示例脚本图片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1134735871/p1090829.png)
4. 实现将双层数组转换为对象数组的Python脚本为例，依次**设置脚本代码**、**测试入参**，并点击**脚本测试**，如下图所示：

   ![python调试..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1134735871/p683026.png)

   **设置脚本代码**：

   ```
   array = input["array"]
   result = []
   for a in array:
     key = a[0]
     value = a[1]
     result.append({"key":key,"value":value})
   output.update({"result":result})
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
   > 出参属性与Python脚本中output中设置的返回key一致。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1134735871/p558616.png)
6. 在「脚本出参」中设置对象数组的出参结构，然后单击**下一步**。

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

## 示例二：网络请求

执行动作配置：

1. 在连接器的基本信息界面，依次选择**执行动作>创建执行动作**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1134735871/p558590.png)
2. 在基础信息中，选择**API类型**为`FAAS`，然后点击下一步。

   ![FAAS选择..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2134735871/p682801.png)
3. 在入参配置中，选择脚本语言为`Python`，示例中有对应脚本语言实现的详细说明，可根据说明实现自己的脚本。

   > **[!NOTE]**
   >
   > 在点击下一步之前，请将右侧`测试过程是否作为下一步出入参`设置为否，否则无法进入下一步。

   ![Python示例脚本图片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1134735871/p1090829.png)
4. 实现将双层数组转换为对象数组的Python脚本，依次**设置脚本代码**、**测试入参**，并点击**脚本测试**，如下图所示：

   > **[!NOTE]**
   >
   > 以下示例仅提供参考，具体实现请结合实际使用情况。

   ```
   import requests

     fruitName = input['fruitName']
   applyNum = input['applyNum']

   res = requests.get(url='your Request-URI',headers={"your Request-Headers"})
   fruit1 = res.json()
   fruit1Result = fruit1['result']
   oldNum = None
   for f1 in fruit1Result:
   if f1['name'] == fruitName:
   oldNum = f1['remainNum']
   break

   res = requests.post(url='your Request-URI',headers={"your Request-Headers"},
                       json={"corpId":111,"fruitName":fruitName,"applyNum":applyNum})

   res = requests.get(url='your Request-URI',headers={"your Request-Headers"})
   fruit2 = res.json()
   fruit2Result = fruit2['result']
   newNum = None
   for f2 in fruit2Result:
   if f2['name'] == fruitName:
   newNum = f2['remainNum']
   break

   output.update({"oldNum":oldNum,"newNum":newNum})
   ```

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2134735871/p558794.png)
5. 在「脚本入参」中设置水果名称与申请数量的入参。

   > **[!NOTE]**
   >
   > 入参属性**fruitName**、**applyNum**与Python脚本中从input获取的属性名称一致。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1134735871/p558818.png)
6. 在「脚本出参」中设置对象数组的出参结构，然后单击**下一步**。

   > **[!NOTE]**
   >
   > 出参属性与Python脚本中output中设置的返回key一致。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1134735871/p558816.png)
7. 在调试中，输入执行动作入参参数值，并单击**立即调试。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1134735871/p558701.png)

   如果执行动作出参参数显示如下格式返回值，则结构转换的FAAS连接器已经配置完成，最后点击**发布**即可。

   ```
   {
     "oldNum": 958,
     "newNum": 956
   }
   ```
