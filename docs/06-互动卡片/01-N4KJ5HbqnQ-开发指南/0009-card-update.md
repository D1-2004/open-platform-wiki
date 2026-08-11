---
title: "卡片更新"
source_url: "https://open.dingtalk.com/document/development/card-update"
namespace: "development"
slug: "card-update"
group: "互动卡片"
tab: "开发指南"
breadcrumb: "卡片互动 > 卡片更新"
doc_id: "Vi22O3EV8i"
updated_at: "2025-09-23 19:18:21"
---

> Source: https://open.dingtalk.com/document/development/card-update
> Path: 互动卡片 / 开发指南 / 卡片互动 > 卡片更新
> Updated: 2025-09-23 19:18:21

# 卡片更新

通过本文，你将会了解到如何更新一个互动卡片，如何对某个人的卡片内容做变更。

> **[!NOTE]**
>
> 在投放卡片实例之前，确保你已经完成了以下的准备工作：
>
> 1. 实现完成[卡片模板搭建及发布](0001-card-template-building-and-publishing.md)过程。
> 2. 实现完成[卡片平台创建卡片实例](0003-create-a-card-instance-from-the-card-platform.md)流程和[开放接口创建卡片实例](0004-open-the-interface-to-create-a-card-instance.md)流程。
> 3. 实现完成[卡片平台投放卡片实例](0005-card-delivery-instance-for-card-platform.md)流程和[开放接口投放卡片实例](0006-open-interface-card-delivery-instance.md)流程。

## **卡片更新**

当卡片背后承载的业务发生变更的时候，系统希望对应的卡片内容也能及时反映出业务的变化。此时，我们就可以通过调用开放接口，来主动更新卡片的内容，及时给用户反馈当前业务发生的变动。

## **更新流程及效果图**

### **业务流程**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4540261761/p537538.png)

### **视觉效果**

提交审批：

| **审批人视角** | **提交人视角** |
| --- | --- |
| image | image |

审批完成：

| **审批人视角** | **提交人视角** |
| --- | --- |
| image | image |

## **实现更新**

通过调用[更新卡片](../../01-应用开发/02-4a8AMF6u2A-服务端API/0780-interactive-card-update-interface.md)进行更新，在调用更新之前，你必须已经通过之前的接口，创建了一张互动卡片的实例，并将其投放到一个或者多个特定的场域。

正如创建所示，互动卡片的数据分为公有数据跟私有数据。卡片的更新也分为公有数据更新、私有数据更新，也可以同时更新公有数据与私有数据。

### **更新的两种形式**

#### **更新公有数据**

当进行公有数据变更的时候，我们进行的变更会推送给所有该卡片的接收者。所有接收到该卡片的用户，在看到该卡片的时候，相应字段都会发生变更。

#### **更新私有数据**

当某个数据只针对部分用户进行更新的时候，我们可以进行私有数据变更，该变更会推送给对应变更数据的用户。当对应用户看到该卡片的时候，相应字段会发生变更。

## **适用场景**

主动更新适用于低频变更的场景（例如：审批单审批结果的变更），以及需要立即生效的变更，如果业务数据变动高频或者对数据刷新及时性不敏感，可使用[动态数据源](0008-dynamic-data-source.md)。

> **[!NOTE]**
>
> 本示例分两个部分：
>
> 示例1 用于展示如何调用更新接口更新卡片数据。
>
> 示例2 使用审批案例，用于展示一个完整的业务流更新。

### **示例1**

#### **更新公有数据**

下面我们通过一个具体的案例，调用服务端API-[更新卡片](../../01-应用开发/02-4a8AMF6u2A-服务端API/0780-interactive-card-update-interface.md)接口实现更新公有数据。

场景设计：

```
一个群里有：张三、李四、王五三个人；
群里有一张卡片；
通过API调用更新接口更新该卡片的公有数据；
```

代码实例：

HTTP

```
PUT /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "outTrackId" : "my-out-trarck-id",
  "userIdType" : 1,
  "cardData" : {
    "cardParamMap" : {
      "param1" : "val_changed"
    }
  },
  "cardUpdateOptions" : {
    "updateCardDataByKey" : true
  }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.dingtalkcard_1_0.Client;
import com.aliyun.teaopenapi.models.Config;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardHeaders;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardUpdateOptions;
import com.aliyun.dingtalkcard_1_0.models.PrivateDataValue;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardData;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest;
import com.aliyun.teautil.models.RuntimeOptions;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static Client createClient() throws Exception {
        Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        Client client = Sample.createClient();
        UpdateCardHeaders updateCardHeaders = new UpdateCardHeaders();
        updateCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateCardRequestCardUpdateOptions cardUpdateOptions = new UpdateCardRequestCardUpdateOptions()
                .setUpdateCardDataByKey(true);
        UpdateCardRequestCardData cardData = new UpdateCardRequestCardData();
        Map<String,String> cardDataMap = new HashMap<>();
        cardDataMap.put("param1", "val_changed");
        cardData.setCardParamMap(cardDataMap);
        UpdateCardRequest updateCardRequest = new UpdateCardRequest()
                .setOutTrackId("my-out-trarck-id")
          			.setUserIdType(1)
                .setCardData(cardData)
                .setCardUpdateOptions(cardUpdateOptions);
        try {
            client.updateCardWithOptions(updateCardRequest, updateCardHeaders, new RuntimeOptions());
        } catch (TeaException err) {
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        } catch (Exception _err) {
            TeaException err = new TeaException(_err.getMessage(), _err);
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        }        
    }
}
```

> **[!NOTE]**
>
> - updateCardDataByKey：如果该参数设置为true，则卡片公有数据的更新是按照key来进行增量更新，如果设置为false，则为全量覆盖更新。**默认为全量覆盖更新****。**
> - 卡片非 String 类型属性的填写请参考：[API 卡片数据的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端API/0787-instructions-for-filling-in-api-card-data.md)。
> - `userIdType` 字段的填写请参考：[userIdType 字段的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端API/0788-faq-card.md#8cad7f90a8mzg)。

#### **更新私有数据**

下面我们通过一个具体的案例，调用服务端API-[更新卡片](../../01-应用开发/02-4a8AMF6u2A-服务端API/0780-interactive-card-update-interface.md)接口实现更新私有数据。

场景设计：

```
一个群里有：张三、李四、王五三个人；
群里有一张卡片；
通过API调用更新接口更新该卡片的李四(user123)的私有数据；
```

代码实例：

HTTP

```
PUT /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "outTrackId" : "my-out-trarck-id",
  "userIdType" : 1,
  "privateData" : {
    "user123" : {
      "cardParamMap" : {
        "privateParam1" : "val_changed"
      }
    }
  },
  "cardUpdateOptions" : {
    "updatePrivateDataByKey" : true
  }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.dingtalkcard_1_0.Client;
import com.aliyun.teaopenapi.models.Config;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardHeaders;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardUpdateOptions;
import com.aliyun.dingtalkcard_1_0.models.PrivateDataValue;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardData;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest;
import com.aliyun.teautil.models.RuntimeOptions;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static Client createClient() throws Exception {
        Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        Client client = Sample.createClient();
        UpdateCardHeaders updateCardHeaders = new UpdateCardHeaders();
        updateCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateCardRequestCardUpdateOptions cardUpdateOptions = new UpdateCardRequestCardUpdateOptions()
                .setUpdatePrivateDataByKey(true);
        PrivateDataValue privateDataValueKey = new PrivateDataValue();
        Map<String,String> privateDataMap = new HashMap<>();
        privateDataMap.put("privateParam1", "val_changed");
        privateDataValueKey.setCardParamMap(privateDataMap);
        java.util.Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("user123", privateDataValueKey)
        );
        UpdateCardRequest updateCardRequest = new UpdateCardRequest()
                .setOutTrackId("my-out-trarck-id")
          			.setUserIdType(1)
                .setPrivateData(privateData)
                .setCardUpdateOptions(cardUpdateOptions);
        try {
            client.updateCardWithOptions(updateCardRequest, updateCardHeaders, new RuntimeOptions());
        } catch (TeaException err) {
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        } catch (Exception _err) {
            TeaException err = new TeaException(_err.getMessage(), _err);
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        }        
    }
}
```

> **[!NOTE]**
>
> - updatePrivateDataByKey：如果该参数设置为true，则卡片私有数据的更新是按照key来进行增量更新，如果设置为false，则为全量覆盖更新。**默认为全量覆盖更新****。**
> - 卡片非 String 类型属性的填写请参考：[API 卡片数据的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端API/0787-instructions-for-filling-in-api-card-data.md)。
> - `userIdType` 字段的填写请参考：[userIdType 字段的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端API/0788-faq-card.md#8cad7f90a8mzg)。

#### **同时更新公有/私有数据**

下面我们通过一个具体的案例，调用服务端API-[更新卡片](../../01-应用开发/02-4a8AMF6u2A-服务端API/0780-interactive-card-update-interface.md)接口实现更新公、私有数据。

场景设计：

```
一个群里有：张三、李四、王五三个人；
群里有一张卡片；
通过API调用更新接口更新该卡片的共有数据，同时更新该卡片的李四(user123)的私有数据；
```

代码实例：

HTTP

```
PUT /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "outTrackId" : "my-out-trarck-id",
  "userIdType" : 1,
  "cardData" : {
    "cardParamMap" : {
      "param1" : "val_changed"
    }
  },
  "privateData" : {
    "user123" : {
      "cardParamMap" : {
        "privateParam1" : "val_changed"
      }
    }
  },
  "cardUpdateOptions" : {
    "updatePrivateDataByKey" : true,
    "updateCardDataByKey" : true
  }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.dingtalkcard_1_0.Client;
import com.aliyun.teaopenapi.models.Config;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardHeaders;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardUpdateOptions;
import com.aliyun.dingtalkcard_1_0.models.PrivateDataValue;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardData;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest;
import com.aliyun.teautil.models.RuntimeOptions;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static Client createClient() throws Exception {
        Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        Client client = Sample.createClient();
        UpdateCardHeaders updateCardHeaders = new UpdateCardHeaders();
        updateCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateCardRequestCardUpdateOptions cardUpdateOptions = new UpdateCardRequestCardUpdateOptions()
                .setUpdateCardDataByKey(true)
                .setUpdatePrivateDataByKey(true);
        PrivateDataValue privateDataValueKey = new PrivateDataValue();
      	Map<String,String> privateDataMap = new HashMap<>();
        privateDataMap.put("privateParam1", "val_changed");
        privateDataValueKey.setCardParamMap(privateDataMap);
        java.util.Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("userId123", privateDataValueKey)
        );
      
        UpdateCardRequestCardData cardData = new UpdateCardRequestCardData();
        Map<String,String> cardDataMap = new HashMap<>();
        cardDataMap.put("param1", "val_changed");
        cardData.setCardParamMap(cardDataMap);
      
        UpdateCardRequest updateCardRequest = new UpdateCardRequest()
                .setOutTrackId("my-out-trarck-id")
          			.setUserIdType(1)
                .setCardData(cardData)
                .setPrivateData(privateData)
                .setCardUpdateOptions(cardUpdateOptions);
        try {
            client.updateCardWithOptions(updateCardRequest, updateCardHeaders, new RuntimeOptions());
        } catch (TeaException err) {
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        } catch (Exception _err) {
            TeaException err = new TeaException(_err.getMessage(), _err);
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        }        
    }
}
```

> **[!NOTE]**
>
> - updateCardDataByKey：如果该参数设置为true，则卡片公有数据的更新是按照key来进行增量更新，如果设置为false，则为全量覆盖更新。**默认为全量覆盖更新****。**
> - updatePrivateDataByKey：如果该参数设置为true，则卡片私有数据的更新是按照key来进行增量更新，如果设置为false，则为全量覆盖更新。**默认为全量覆盖更新****。**
> - 卡片非 String 类型属性的填写请参考：[API 卡片数据的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端API/0787-instructions-for-filling-in-api-card-data.md)。
> - `userIdType` 字段的填写请参考：[userIdType 字段的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端API/0788-faq-card.md#8cad7f90a8mzg)。

### **示例2**

> **[!NOTE]**
>
> 本示例是基于上文提到的一个审批流的更新。

#### **前置说明**

首先我们搭建了一个模板如下及模板对应的变量如下所示：

| image | image |
| --- | --- |

其中审批处理按钮只对审批人显示，审批过程中展示正常的审批按钮，审批结束后，展示禁用的审批按钮。

当我们创建卡片的时候整个数据如下：

```
{
        "cardData": {
            "cardParamMap": {
                "title": "**的差旅报销",
                "type": "差旅费",
                "reason": "出差费用",
                "amount": "100",
                "status": "未审批"
            }
        },
        "privateData": {
            "userId1": {
                "cardParamMap": {
                    "isApprover": "0"
                }
            },
             "userId2": {
                "cardParamMap": {
                    "isApprover": "1",
                		"isFinished": "0"
                }
            }
        }
}
```

卡片如下图所示

| userId1 | userId2 |
| --- | --- |
| image | image |

此时userId2点击同意后，审批系统调用服务端API-[更新卡片](../../01-应用开发/02-4a8AMF6u2A-服务端API/0780-interactive-card-update-interface.md)接口实现更新接口，如下：

HTTP

```
PUT /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
    "outTrackId":"my-out-trarck-id",
    "userIdType":1,
    "cardData":{
        "cardParamMap":{
            "status":"审批完成"
        }
    },
    "privateData": {
             "userId2": {
                "cardParamMap": {
                		"isFinished": "1"
                }
            }
        }
    "cardUpdateOptions":{
        "updateCardDataByKey":true
        "updatePrivateDataByKey":true
    }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.dingtalkcard_1_0.Client;
import com.aliyun.teaopenapi.models.Config;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardHeaders;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardUpdateOptions;
import com.aliyun.dingtalkcard_1_0.models.PrivateDataValue;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest.UpdateCardRequestCardData;
import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest;
import com.aliyun.teautil.models.RuntimeOptions;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static Client createClient() throws Exception {
        Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        Client client = Sample.createClient();
        UpdateCardHeaders updateCardHeaders = new UpdateCardHeaders();
        updateCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateCardRequestCardUpdateOptions cardUpdateOptions = new UpdateCardRequestCardUpdateOptions()
                .setUpdateCardDataByKey(true)
                .setUpdatePrivateDataByKey(true);
        PrivateDataValue privateDataValueKey = new PrivateDataValue();
        Map<String,String> privateDataMap = new HashMap<>();
      	privateDataMap.put("isFinished", "1");
        privateDataValueKey.setCardParamMap(privateDataMap);
        java.util.Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("userId123", privateDataValueKey)
        );
      
        UpdateCardRequestCardData cardData = new UpdateCardRequestCardData();
        Map<String,String> cardDataMap = new HashMap<>();
        cardDataMap.put("status", "审批完成");
        cardData.setCardParamMap(cardDataMap);
      
        UpdateCardRequest updateCardRequest = new UpdateCardRequest()
                .setOutTrackId("my-out-trarck-id")
          			.setUserIdType(1)
                .setCardData(cardData)
                .setPrivateData(privateData)
                .setCardUpdateOptions(cardUpdateOptions);
        try {
            client.updateCardWithOptions(updateCardRequest, updateCardHeaders, new RuntimeOptions());
        } catch (TeaException err) {
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        } catch (Exception _err) {
            TeaException err = new TeaException(_err.getMessage(), _err);
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        }        
    }
}
```

调用之后效果如下：

| userId1 | userId2 |
| --- | --- |
| image | image |
