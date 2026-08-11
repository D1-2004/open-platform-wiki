---
title: "Nodejs脚本连接器"
source_url: "https://open.dingtalk.com/document/connection/nodejs-script-connector-1"
namespace: "connection"
slug: "nodejs-script-connector-1"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发参考 > 创建FAAS执行动作 > Nodejs脚本连接器"
doc_id: "I4bg6yMjgJ"
updated_at: "2025-09-23 19:20:34"
---

> Source: https://open.dingtalk.com/document/connection/nodejs-script-connector-1
> Path: 连接平台 / 开发指南 / 开发参考 > 创建FAAS执行动作 > Nodejs脚本连接器
> Updated: 2025-09-23 19:20:34

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

### **Nodejs示例脚本：**

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

## 数据结构转换

### **执行动作配置**

#### **基础配置**

1. 创建执行动作。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1725395761/p558590.png)
2. 类型选择：

   1. **API类型**：FAAS

      ![FAAS选择..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9012186861/p682801.png)
   2. **选择脚本语言：**Nodejs

      ![FAAS-NodeJS..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9012186861/p682804.png)

      示例中有对应脚本语言实现的详细说明，可根据说明实现自己的脚本。

      ![nodeJs脚本说明..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9012186861/p682812.png)

#### **脚本配置**

实现将双层数组转换为对象数组的Nodejs脚本，并点击下一步

1. 设置脚本代码并单击调试。

   ```
   var array = input.array;
   var result = array.map((val, index) => {
     var key = val[0];
     var value = val[1];
     return {"key":key, "value":value};
   });
   output.result = result;
   ```

   ![调试nodeJs..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9012186861/p682973.png)
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

   ![调试执行nodeJs..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9012186861/p682981.png)
3. 单击下一步。

   ![下一步nodeJs..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9012186861/p682986.png)

#### **入参配置**

在「入参配置」中设置双层数组的入参结构，入参属性array与Nodejs脚本中从input获取的属性名称一致。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1725395761/p558616.png)

#### **出参配置**

在「出参配置」中设置对象数组的出参结构，出参属性与Nodejs脚本中output中设置的返回key一致。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1725395761/p558622.png)

#### **执行动作验证**

经过配置步骤后，结构转换的FAAS连接器已经配置完成，我们对此进行一下校验。

1. 选择**执行动作**的「调试」功能。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1725395761/p558630.png)
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
