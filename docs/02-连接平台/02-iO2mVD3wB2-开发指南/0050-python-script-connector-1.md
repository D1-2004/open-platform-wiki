---
title: "Python脚本连接器"
source_url: "https://open.dingtalk.com/document/connection/python-script-connector-1"
namespace: "connection"
slug: "python-script-connector-1"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发参考 > 创建FAAS执行动作 > Python脚本连接器"
doc_id: "NoP5lkyKQT"
updated_at: "2025-09-23 19:20:35"
---

> Source: https://open.dingtalk.com/document/connection/python-script-connector-1
> Path: 连接平台 / 开发指南 / 开发参考 > 创建FAAS执行动作 > Python脚本连接器
> Updated: 2025-09-23 19:20:35

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

### Python**示例脚本：**

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

#### **输入**

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

#### **输出**

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

### **执行动作配置**

#### **基础配置**

1. 创建执行动作。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1725395761/p558590.png)
2. 类型选择：

   1. **API类型**：FAAS

      ![FAAS中Python..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2891186861/p683001.png)
   2. **选择脚本语言：**Python

      ![选择Python..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2891186861/p683014.png)

      示例中有对应脚本语言实现的详细说明，可根据说明实现自己的脚本。

      ![python设置..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2891186861/p683021.png)

#### **脚本配置**

实现将双层数组转换为对象数组的Python脚本，并单击**下一步。**

1. 设置脚本代码并单击调试。

   ```
   array = input["array"]
   result = []
   for a in array:
     key = a[0]
     value = a[1]
     result.append({"key":key,"value":value})
   output.update({"result":result})
   ```

   ![python调试..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2891186861/p683026.png)
2. 写入调试并执行。

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

   ![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2891186861/p683030.png)
3. 单击下一步。

   ![下一步python..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2891186861/p683055.png)

#### **入参配置**

在「入参配置」中设置双层数组的入参结构，入参属性array与Python脚本中从input获取的属性名称一致。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1725395761/p558616.png)

#### **出参配置**

在「出参配置」中设置对象数组的出参结构，出参属性与Python脚本中output中设置的返回key一致。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1725395761/p558622.png)

#### **执行动作验证**

经过配置步骤后，结构转换的FAAS连接器已经配置完成，我们对此进行一下校验。

1. 选择**执行动作**的「调试」功能。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6825395761/p558701.png)
2. 请求体输入并单击调试。

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

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1725395761/p558641.png)
3. 响应体输出。

   ```
   {
     "result": [
       {
         "value": "钉钉",
         "key": "code1"
       },
       {
         "value": "让进步发生",
         "key": "code2"
       }
     ]
   }
   ```

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1725395761/p558648.png)

## 示例二：网络请求

### **执行动作配置**

#### **基础配置**

1. 创建执行动作。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1725395761/p558590.png)
2. 类型选择：

   1. **API类型**：FAAS

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1725395761/p558593.png)
   2. **选择脚本语言：**Python

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6825395761/p558676.png)

      示例中有对应脚本语言实现的详细说明，可根据说明实现自己的脚本

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6825395761/p558677.png)

#### **脚本配置**

实现将双层数组转换为对象数组的Python脚本，并单击**下一步。**

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

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6825395761/p558794.png)

#### **入参配置**

在「入参配置」中设置水果名称与申请数量的入参，入参属性**fruitName**、**applyNum**与Python脚本中从input获取的属性名称一致

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6825395761/p558818.png)

#### **出参配置**

在「出参配置」中设置对象数组的出参结构，出参属性与Python脚本中output中设置的返回key一致。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6825395761/p558816.png)

#### **执行动作验证**

经过配置步骤后，结构转换的FAAS连接器已经配置完成，我们对此进行一下校验。

1. 选择**执行动作**的「调试」功能。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6825395761/p558701.png)
2. 请求体输入并单击调试。

   ```
   {
    "fruitName":"香蕉",
    "applyNum":2
   }
   ```

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6825395761/p558849.png)
3. 响应体输出。

   ```
   {
     "oldNum": 958,
     "newNum": 956
   }
   ```

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6825395761/p558856.png)
