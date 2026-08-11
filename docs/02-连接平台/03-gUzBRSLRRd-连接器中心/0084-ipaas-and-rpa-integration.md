---
title: "连接平台与阿里云RPA集成"
source_url: "https://open.dingtalk.com/document/connection/ipaas-and-rpa-integration"
namespace: "connection"
slug: "ipaas-and-rpa-integration"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "三方连接器 > 连接平台与阿里云RPA集成"
doc_id: "P50P7GRYUF"
updated_at: "2026-05-19 19:46:17"
---

> Source: https://open.dingtalk.com/document/connection/ipaas-and-rpa-integration
> Path: 连接平台 / 连接器中心 / 三方连接器 > 连接平台与阿里云RPA集成
> Updated: 2026-05-19 19:46:17

# 连接平台与阿里云RPA集成

## **简介**

连接平台与阿里云RPA的集成能力可以模拟人类操作应用程序和系统交互，例如在使用鼠标、键盘、窗口和屏幕上模拟人类的操作。对尚未开放API，但存在参数界面，可以通过阿里云RPA的能力进行捕捉获取。再通过连接平台的基本规则、条件和逻辑来实现复杂的业务流程。将为企业提供更高效的解决方案，提高企业生产力和准确性，节约时间和资源，从而带来更高效、更智能的工作方式，使得企业更具竞争力和创新力。

## **准备工作**

在使用RPA前需要做一些准备工作：

- 阿里云RPA需要部署在Windows机器上：

  - 如果无Windows机器，可通过[无影云桌面免费体验季](https://www.aliyun.com/daily-act/ecs/eds_free?spm=5176.19598036.J_3584438920.1.35552058rJq0Le&scm=20140722.M_8110064.P_192.MO_978-ID_8110064-MID_8110064-CID_28241-ST_5348-V_1)申请3个月免费服务器。
  - 如果已有Windows机器，可直接使用。
- 开通阿里云RPA：

  - 如果无RPA，可通过[阿里云RPA免费试用](https://help.aliyun.com/document_detail/176791.html?spm=a2c4g.396266.0.0.6ff82ac5Pa7lHp)一个月，并[下载和安装](https://help.aliyun.com/document_detail/174585.html?spm=a2c4g.55920.0.0.4bb830e5Ibfh4p)对应RPA软件。
  - 如果已有RPA，可直接使用。

## 案例：**发送工作通知**

> **[!NOTE]**
>
> 工程文件**DingAppDemo.zip**可以在底部**相关链接**中下载。

工作通知接口需要应用的[agentId](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)，目前可通过用户登录开发者后台，然后搜索应用，进入应用后复制对应的agentId。

## **步骤一：搭建RPA工程**

在阿里云RPA编辑器中通过代码或者可视化方式编排UI操作流程。本示例采用基础编码工程模板的方式。

![基础编码工程..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679338.png)

#### **代码示例：**

```
# -*- coding: utf-8 -*-
from rpa.core import *
from rpa.utils import *
import rpa4 as rpa
import requests
import time

def start():
    # 打开新网页
    page = rpa.app.chrome.create('https://open-dev.dingtalk.com/')
    # 点击控件（网页）
    page.click('应用开发', index=1, simulate=True, button='left', offset_x=0, offset_y=0)
    time.sleep(3)
    app_name = rpa.project.params['app_name']
    page.input_text('应用名称搜索', app_name, index = 1, simulate=True, replace = True, sent_raw = False, wait_mili_seconds = 20)
    page.click('开始搜索', index=1, simulate=True, button='left', offset_x=0, offset_y=0)
    # 点击控件（网页）
    ctrls.variable.assign('$searchText', app_name)
    page.click('点击应用', index=1, simulate=True, button='left', offset_x=0, offset_y=0)

    # 获取文本（网页）
    agentId = page.text(element = '应用凭证信息',index = 1)
    # 获取文本（网页）
    appKey = page.text(element = '应用凭证信息',index = 2)
    # 获取文本（网页）
    appSecret = page.text(element = '应用凭证信息',index = 3)
    # 记录日志
    print([agentId, appKey, appSecret])
    callback_url = rpa.project.params['callback_url']
    result = f'''{{
        "AgentId": "{agentId}",
        "AppKey": "{appKey}",
        "AppSecret": "{appSecret}"
    }}'''
    print(callback_url)
    if callback_url is not None:
        req = requests.post(callback_url, headers={
            'Content-Type': 'application/json'
        }, json={
            'agentId': agentId,
            'appKey': appKey,
            'appSecret': appSecret
        })
        print(req.content.decode())
    else:
        rpa.console.workbench.task_result(result)
```

复制上述代码示例：

![编写RPA代码..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679340.png)

#### **组件捕捉：**

代码里引用的所有组件都需要通过[组件捕捉](https://help.aliyun.com/document_detail/346725.html?spm=a2c4g.58974.0.0.2c5929ecu7emVM)的方式捕捉并验证。

1. 单击「开始捕捉」。

   ![开始捕捉..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679354.png)
2. 捕捉控件：

   - 捕捉「应用开发」控件：

     1. 开始捕捉。

        ![应用开发捕捉..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679348.png)
     2. 设置控件名称，并单击**保存**。

        ![RPA应用开发..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679956.png)
   - 捕捉「应用名称搜索」控件：

     1. 单击**应用开发**，进入应用列表，捕捉「应用名称搜索」控件。

        ![应用名称搜索捕捉..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679373.png)
     2. 设置控件名称，并单击**保存**。

        ![应用名称搜索RPA..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679972.png)
   - 捕捉「应用名称搜索」控件：

     1. 进行搜索，捕捉「开始搜索」控件。

        > **[!NOTE]**
        >
        > 由于上述代码示例中，定义了搜索内容，这里我们直接捕捉「开始搜索」控件。

        ![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679376.png)
     2. 设置控件名称，并单击**保存**。

        ![开始搜索RPA..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679971.png)
   - 进行搜索，捕捉「点击应用」控件：

     1. 进入搜索应用，捕捉「点击应用」控件。

        ![捕捉点击应用..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679395.png)
     2. 设置控件名称，并单击保存。

        ![点击应用RPA..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679968.png)
   - 捕捉「应用凭证信息」控件。

     1. 单击进入应用，捕捉「应用凭证信息」控件。

        ![agentId获取..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679417.png)
     2. 单击捕捉相似控件。实现信息获取。

        > **[!NOTE]**
        >
        > 由于这里获取的是AgentId、AppKey和AppSecret，所以我们采用「捕捉相似控件」方式。

        ![捕捉相似控件..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679424.png)
     3. 实现多个内容捕捉。

        ![多个信息捕捉..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679425.png)
     4. 设置控件名称，并单击保存。

        ![保存捕捉..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679430.png)

        此时，我们控件就已经全部捕捉完成了。
3. 设置参数面板：

   1. 单击参数面板。

      ![设置参数面板..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679437.png)
   2. 设置参数。

      > **[!NOTE]**
      >
      > 此处`callback_url`填写仅用于测试，可随意填写。

      ![设置参数..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679445.png)
4. 调试，执行本流程。

   ![调试RPA..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679450.png)
5. 发布流程。

   ![发布RPA..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679451.png)

> **[!NOTE]**
>
> 1. 发布后可以在[RPA控制台](https://console-rpa.aliyun.com/myApp/appList)申请发布的应用，管理员[审批](https://help.aliyun.com/document_detail/444786.html?spm=a2c4g.444785.0.0.3001399fjhzSEl#p-5e1-e5v-68i)后就可以使用了，如何使用参考[RPA需求方-快速入门](https://help.aliyun.com/document_detail/444785.html?spm=a2c4g.444786.0.0.164b29abebBd28)。
> 2. 可以在**我的应用**中复制应用ID，为后续调用连接流使用。
>
>    ![应用IDRPA..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679657.png)

## **步骤二：创建连接器**

告警监控通知基于连接器的基础上实现：

- 如果无连接器，详情参见[创建连接器](../02-iO2mVD3wB2-开发指南/0013-create-connector.md)。
- 如果已有连接器，可直接使用已有连接器。

## **步骤三：创建触发事件**

1. 单击**创建触发事件**。

   ![创建触发事件..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679736.png)
2. 填写触发事件设置。

   - 获取钉钉应用信息并发送给工作通知RPA任务触发：

     1. 设置**基础信息**并单击**下一步**：

        ![RPA下一步.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0309167961/p728224.png)
     2. 模型配置：

        完成触发事件入参并单击**下一步**：

        ![参数设置RPA.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0309167961/p728232.png)

        ```
        {
          "description": "当前对象模型根容器",
          "properties": {
            "appName": {
              "description": "钉钉企业内部应用名称",
              "properties": {},
              "required": [],
              "sortedProps": [],
              "title": "应用名称",
              "type": "string",
              "version": 0
            },
            "rpaProjectId": {
              "properties": {},
              "required": [],
              "sortedProps": [],
              "title": "RPA应用ID",
              "type": "string",
              "version": 0
            }
          },
          "required": [
            "appName",
            "rpaProjectId"
          ],
          "sortedProps": [
            "appName",
            "rpaProjectId"
          ],
          "title": "入参",
          "type": "object",
          "version": 0
        }
        ```
     3. 进行调试并发布。

        ![参数设置RPA.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0309167961/p728243.png)

## **步骤四：iPaas中编排连接流**

在iPaaS中通过连接流方式将流程串联起来，这里可以配置两个连接流：

1. 触发RPA流程的连接流。
2. 当RPA流程运行完后接收运行结果执行后续业务逻辑的连接流。

### **配置触发事件**

1. 创建连接流。

   ![一阶段连接流创建..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679796.png)
2. 选择连接器。

   > **[!NOTE]**
   >
   > 此处选择连接器为步骤一、步骤二中所创建的连接器。

   ![RPA触发事件..png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679802.png)
3. 选择触发事件。

   ![选择触发事件-一阶段..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679808.png)
4. 完成配置。

   ![完成第一阶段RPA配置..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679809.png)

### **配置阿里云RPA执行动作**

1. 选择连接器。

   ![一阶段阿里云RPA执行..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679815.png)
2. 选择执行动作。

   ![一阶段执行动作..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679817.png)
3. 配置账号。

   > **[!IMPORTANT]**
   >
   > 根据准备工作内容，已经拥有使用阿里云RPA，使用**阿里云RPA**的AK信息。这里的AK信息不是阿里云控制台的AK信息。
   >
   > ![阿里云RPA的AK..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679824.png)

   ![添加账户一阶段..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679828.png)
4. 配置参数。

   1. 出入参配置：

      ![点击出参配置一阶段..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679835.png)
   2. 参数映射：

      - 应用唯一标识符：

        ![RPA对应参数设置.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0309167961/p728265.png)
      - 参数名称：

        选择**表达式**，填写并**确认。**

        ![参数名称表达式..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3404316861/p679874.png)
      - 参数值：

        选择**表达式**，填写并**确认。**

        ![RPA表达式设置.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0309167961/p728303.png)

### **配置流程暂停执行动作**

1. 单击“⊕”符号 > **请选择连接器和执行动作**。
2. 单击**内置工具** > **流程暂停** > **从当前节点暂停**。
3. 单击**测试并预览**，复制回调地址。

   ![复制回调地址.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0309167961/p728328.png)
4. 请求回调地址。

   ![请求回调地址.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0309167961/p728331.png)
5. 再次单击**测试并预览**，查看测试信息，确认回调地址正确。

   ![出参信息-rpa.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0309167961/p728367.png)

### **配置工作通知执行动作**

1. 单击“⊕”符号 > **请选择连接器和执行动作**。
2. 单击**官方连接器** > **工作通知**。
3. 单击**发送工作通知[文本消息]**。
4. 配置参数：

   - **微应用的id**：应用agentId，获取详情参见[应用Id](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。
   - **接收者的用户userid列表**：选择多种类型，通过选人组件完成成员添加。

     ![选择多种类型-userid.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0309167961/p728364.png)
   - 文本消息：

     本示例采用**表达式**，填写并**确认**。

     ![工作通知-确认.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0309167961/p728370.png)

### **发布连接流**

单击右上角发布，完成连接流的发布操作。

## **步骤五：实现通知**

1. 打开阿里云RPA机器人。

   > **[!IMPORTANT]**
   >
   > 开启允许被调用，否则无法使用。

   ![阿里云RPA机器人..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4607126861/p680497.png)
2. 使用postman构建请求。

   ![发送工作通知-RPA.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0309167961/p728375.png)

   - **请求地址：**上述步骤二、三中连接器中**发送给工作通知第一阶段RPA任务触发**的[Webhook](../02-iO2mVD3wB2-开发指南/0016-using-connectors-1.md#636e0c4a67u8r)地址
   - **rpaProjectId**：上述步骤一的RPA应用ID。
   - **appName**：钉钉应用名称。

## **相关链接**

- 发送工作通知RPA工程：[DingAppDemo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20230608/usxu/DingAppDemo.zip)。
