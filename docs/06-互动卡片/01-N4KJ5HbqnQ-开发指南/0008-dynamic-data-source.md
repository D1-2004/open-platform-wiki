---
title: "动态数据源"
source_url: "https://open.dingtalk.com/document/development/dynamic-data-source"
namespace: "development"
slug: "dynamic-data-source"
group: "互动卡片"
tab: "开发指南"
breadcrumb: "卡片互动 > 动态数据源"
doc_id: "qx7bw2uLgN"
updated_at: "2025-09-23 19:18:20"
---

> Source: https://open.dingtalk.com/document/development/dynamic-data-source
> Path: 互动卡片 / 开发指南 / 卡片互动 > 动态数据源
> Updated: 2025-09-23 19:18:20

# 动态数据源

通过本文你可以了解到卡片动态数据源的使用和常见问题

> **[!NOTE]**
>
> 在使用动态数据源之前，建议您已经完成了以下的准备工作:
>
> 1. 了解[卡片模板搭建及发布](0001-card-template-building-and-publishing.md)过程。
> 2. 了解[卡片平台创建卡片实例](0003-create-a-card-instance-from-the-card-platform.md)流程和[开放接口创建卡片实例](0004-open-the-interface-to-create-a-card-instance.md)流程。
> 3. 了解[卡片平台投放卡片实例](0005-card-delivery-instance-for-card-platform.md)流程和[开放接口投放卡片实例](0006-open-interface-card-delivery-instance.md)流程。
> 4. **确保客户端的版本高于 6.5.40**

## **卡片中的数据来源**

用户看到一张互动卡片的时候，卡片中的数据来源可以分为如下几类:

|  | 获取时机 | 更新方式 |
| --- | --- | --- |
| 卡片公有数据(卡片所有接收人可见) | 卡片实例创建时 | 调用更新接口变更 |
| 卡片私有数据(卡片某个接收人可见) | 卡片实例创建时 | 调用更新接口变更 |
| 动态数据源数据 | 卡片在客户端渲染时 | 回调动态数据源提供方拉取时变更 |

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Wmeona76ZaXQOXxj/img/2dec4410-7201-4516-b688-477d8ce8d416.png)

## **动态数据源的适用场景**

动态数据源主要在以下场景中使用:

- 部分卡片数据比较敏感，不能托管到卡片服务端(如发票金额、抬头等)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4682293761/p549417.png)

- 部分卡片数据需要根据场景千人千面, 私有数据不能满足诉求 (如查看员工OKR时根据权限隐藏等场景)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5682293761/p549534.png)

- 部分卡片数据需要定时拉取，如一些需要定期更新的报表(如每日销售额、业务趋势图等)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5682293761/p549535.png)

## **数据源交互流程**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6590282761/p537800.png)

## **动态数据源接入方式**

动态数据源的接入方式有两种，一种可以通过卡片搭建平台，在后台创建卡片实例时绑定数据源，一种可以通过开放接口接入的方式完成。

### **卡片搭建平台接入**

如果卡片的创建是[卡片平台创建卡片实例](0003-create-a-card-instance-from-the-card-platform.md)的方式完成，可以在[卡片平台创建卡片实例 > 步骤二：创建卡片实例 > 完成数据配置](0001-card-template-building-and-publishing.md)实现动态数据源接入。

### **开放接口接入**

我们以一张最简单的发票金额动态拉取为例，通过接口接入需要如下几个步骤:

1. 调用服务端API-[注册卡片回调地址](../../01-应用开发/02-4a8AMF6u2A-服务端API/0784-register-card-callback-address.md)，注册动态数据源的回调地址。
2. 调用服务端API-[创建卡片](../../01-应用开发/02-4a8AMF6u2A-服务端API/0778-interface-for-creating-a-card-instance.md)接口，实现动态数据源`openDynamicDataConfig`参数的配置。

   在[开放接口创建卡片实例](0004-open-the-interface-to-create-a-card-instance.md)中，动态数据源相关配置参数`openDynamicDataConfig`，通过简单实例，解释对应参数的含义：

   > **[!NOTE]**
   >
   > 针对`openDynamicDataConfig`参数的说明:
   >
   > - `dynamicDataSourceConfigs`: 动态数据源配置列表，一个卡片实例中可以包含多个动态数据源配置
   >
   >   - `dynamicDataSourceId`: 动态数据源的 ID，要和下文介绍的动态数据响应一一对应
   >   - `pullConfig`: 动态数据源获取配置，分为拉取策略和根据拉取策略的不同配置参数：
   >
   >     - `pullStrategy`: 拉取策略
   >
   >       - `ONCE`：仅获取一次
   >       - `INTERVAL`：定时获取，见「高级功能-定时拉取」
   >       - `RENDER`：每次用户看到卡片时

   HTTP

   ```
   POST /v1.0/card/instances HTTP/1.1
   Host:api.dingtalk.com
   x-acs-dingtalk-access-token:String
   Content-Type:application/json

   {
     "userId" : "user123",
     "userIdType": 1,
     "cardTemplateId" : "abcd-1234",
     "outTrackId" : "my-out-trarck-id",
     "cardData" : {
       "cardParamMap" : {
       "title": "张三提交的报销单",
       "type": "差旅费",
       "reason": "出差费用",
       "status": "未审批",
       "amount": "" 			  //需要通过动态数据源获取的数据的字段，可以为空
       }
     },
   	"openDynamicDataConfig":{
     	"dynamicDataSourceConfigs":[
       	{
         	"dynamicDataSourceId":"example_ds_1", //数据源id
           "pullConfig": {													
           	"pullStrategy": "ONCE"   //只需要获取一次											
         	}
         }
       ]  
     }
   }
   ```

   Java

   ```
   package com.aliyun.sample;

   import java.util.ArrayList;
   import java.util.List;

   import com.aliyun.dingtalkcard_1_0.models.*;
   import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfig;
   import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs;
   import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig;
   import com.aliyun.tea.*;

   public class Sample {

       public static com.aliyun.dingtalkcard_1_0.Client createClient() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           return new com.aliyun.dingtalkcard_1_0.Client(config);
       }

       public static void main(String[] args_) throws Exception {
           java.util.List<String> args = java.util.Arrays.asList(args_);
           com.aliyun.dingtalkcard_1_0.Client client = Sample.createClient();
           CreateCardHeaders createCardHeaders
               = new CreateCardHeaders();
           createCardHeaders.xAcsDingtalkAccessToken = "<your access token>";

           PrivateDataValue privateDataValueKey
               = new PrivateDataValue();
           java.util.Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
               new TeaPair("privateDataValueKey", privateDataValueKey)
           );
           CreateCardRequest.CreateCardRequestCardData cardData
               = new CreateCardRequest.CreateCardRequestCardData();

           //组装动态数据源配置
           CreateCardRequestOpenDynamicDataConfig openDynamicDataConfig = new CreateCardRequestOpenDynamicDataConfig();

           //数据源配置列表
           List<CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs> configs = new ArrayList<>();
           CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs configs1 = new CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs();
           //数据源id
           configs1.dynamicDataSourceId = "example_ds_1";

           //数据源拉取策略
           CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig pullConfig = new CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig();
           pullConfig.pullStrategy = "ONCE";
           configs1.setPullConfig(pullConfig);
         
           configs.add(configs1);
           openDynamicDataConfig.dynamicDataSourceConfigs = configs;

           CreateCardRequest createCardRequest
               = new CreateCardRequest()
               .setUserId("my-user-id")
               .setUserIdType(1)
               .setOutTrackId("out-track-id")
               .setCardTemplateId("card-template-id")
               .setCardData(cardData)
               .setPrivateData(privateData);
           try {
               client.createCardWithOptions(createCardRequest, createCardHeaders,
                   new com.aliyun.teautil.models.RuntimeOptions());
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
3. 实现动态数据拉取回调接口。

   **回调模式**

   目前钉钉提供了如下几个回调接入的模式：基于HTTP服务的回调和基于Stream模式的回调

   - HTTP模式，需要开发者提供一个公网可访问的域名，钉钉会通过http请求将回调信息发送到开发者应用程序。
   - Stream模式，开发者可以做到"五零接入"——零公网IP，零域名，零证书，零网关，零内网穿透工具，开发者通过钉钉SDK建立到钉钉的TCP持久连接，钉钉通过TCP连接推送回调信息到开发者应用程序。

   **HTTP模式：**

   **安全性校验：**

   为了提升回调接口的安全性，从钉钉侧发起的HTTP回调请求，支持开发者进行来源校验。

   如[注册卡片回调地址](../../01-应用开发/02-4a8AMF6u2A-服务端API/0784-register-card-callback-address.md)时提供了“卡片数据回调apiSecret”，则收到的HTTP请求Header中包含签名相关Header:

   • x-ddpaas-signature-timestamp：签名时间戳

   • x-ddpaas-signature：签名串

   其中 <签名串> = calcSignature(apiSecret, <签名时间戳>)，apiSecret是配置时指定的“卡片数据回调Secret”

   接口提供方应使用如下方法计算签名并验证签名串是否正确以防未授权的调用：

   ```
   public static String calcSignature(String apiSecret, long ts) {
       try {
           Mac mac = Mac.getInstance("HmacSHA256");
           SecretKeySpec key = new SecretKeySpec(apiSecret.getBytes(), "HmacSHA256");
           mac.init(key);
           return Base64.getEncoder()
               .encodeToString(mac.doFinal(Long.toString(ts).getBytes()));
       } catch (NoSuchAlgorithmException | InvalidKeyException e) {
           throw new GatewayException(ErrorCodeConstant.SYSTEM_ERROR,
                                      "sign api secret failed", e);
       }
   }
   ```

   **请求格式示例：**

   当卡片进行动态数据源回调时，会向注册的 URL 地址发送一个 POST 请求，请求内容示例如下所示：

   ```
   {
     "type": "dynamicDataCallback",						// 标识回调类型为动态数据源
     "corpId": "corp1234",											// 触发人的企业 ID
     "userId": "user0",												// 触发人的 userId
     "outTrackId": "testOutTrackId",					  // 卡片 ID
     "content": "{\"dynamicDataSourceQueryRequests\": [{\"dynamicDataSourceId\": \"example_ds_1\"}}"
   }
   ```

   > **[!NOTE]**
   >
   > content：这是一个 Json String，解析后为如下样式：
   >
   > ```
   > "content": {
   >     "dynamicDataSourceQueryRequests": [
   >         {
   >             "dynamicDataSourceId": "example_ds_1" // 请求动态数据源 ID
   >         }
   >     ]
   > }
   > ```

   **HTTP 返回格式示例：**

   在处理完动态数据源回调请求后，需要返回回调响应，来更新卡片上的动态数据。响应内容示例如下所示：

   ```
   {
     "dataSourceQueryResponses": [
       {
         "data": "{\"amount\":\"1000元\"}",						    // 返回的动态数据，端上直接覆盖并渲染
         "dynamicDataSourceId": "example_ds_1",					// 动态数据源 ID
         "dynamicDataValueType": "OBJECT"								// 动态数据的类型，支持 STRING、ARRAY、OBJECT 等
       }
     ]
   }
   ```

至此，一个简单的拉取一次动态数据的动态卡片就已经创建并加载完成了。

| 动态数据拉取前 | 动态数据拉取后 |
| --- | --- |
| image | image |

## **高级功能**

### **定时拉取**

在前面动态数据源的介绍和示例中，我们将 pullStrategy 设置为了 ONCE，这代表着卡片只会在第一次被用户查看的时候触发拉取动态数据源。

互动卡片支持对动态数据源的定时拉取策略。如果打算让卡片每 30 秒拉取 amount 的值，可以进行调用服务端API-[创建卡片](../../01-应用开发/02-4a8AMF6u2A-服务端API/0778-interface-for-creating-a-card-instance.md)接口进行如下的配置：

HTTP

```
POST /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "userId" : "user123",
  "userIdType": 1,
  "cardTemplateId" : "abcd-1234",
  "outTrackId" : "my-out-trarck-id",
  "cardData" : {
    "cardParamMap" : {
    "title": "张三提交的报销单",
    "type": "差旅费",
    "reason": "出差费用",
    "status": "未审批",
    "amount": "" 			  //需要通过动态数据源获取的数据的字段，可以为空
    }
  },
	"openDynamicDataConfig":{
  	"dynamicDataSourceConfigs":[
    	{
      	"dynamicDataSourceId":"example_ds_1",      			// 动态数据源 ID
        "pullConfig": {		
        	"pullStrategy": "INTERVAL",										// 间隔拉取
        	"timeUnit": "SECONDS",			   								// 拉取间隔时间的单位
        	"interval": "30"														  // 拉取间隔时间
      	}
      }
    ]
  }
}
```

Java

```
package com.aliyun.sample;

import java.util.ArrayList;
import java.util.List;

import com.aliyun.dingtalkcard_1_0.models.*;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfig;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig;
import com.aliyun.tea.*;

public class Sample {

    public static com.aliyun.dingtalkcard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcard_1_0.Client client = Sample.createClient();
        CreateCardHeaders createCardHeaders
            = new CreateCardHeaders();
        createCardHeaders.xAcsDingtalkAccessToken = "<your access token>";

        PrivateDataValue privateDataValueKey
            = new PrivateDataValue();
        java.util.Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("privateDataValueKey", privateDataValueKey)
        );
        CreateCardRequest.CreateCardRequestCardData cardData
            = new CreateCardRequest.CreateCardRequestCardData();

        //组装动态数据源配置
        CreateCardRequestOpenDynamicDataConfig openDynamicDataConfig = new CreateCardRequestOpenDynamicDataConfig();
        //字段映射类型默认填写REPLACE_WITHOUT_MAPPING
        openDynamicDataConfig.dynamicDataMappingMethod = "REPLACE_WITHOUT_MAPPING";

        //数据源配置列表
        List<CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs> configs = new ArrayList<>();
        CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs configs1 = new CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs();
        //数据源id
        configs1.dynamicDataSourceId = "example_ds_1";

        //数据源拉取策略
        CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig pullConfig = new CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig();
        pullConfig.pullStrategy = "INTERVAL";
      	pullConfig.interval=30;
        pullConfig.timeUnit="SECONDS";
        configs1.setPullConfig(pullConfig);

        configs.add(configs1);

        openDynamicDataConfig.dynamicDataSourceConfigs = configs;

        CreateCardRequest createCardRequest
            = new CreateCardRequest()
            .setUserId("my-user-id")
            .setUserIdType(1)
            .setOutTrackId("out-track-id")
            .setCardTemplateId("card-template-id")
            .setCardData(cardData)
            .setPrivateData(privateData);
        try {
            client.createCardWithOptions(createCardRequest, createCardHeaders,
                new com.aliyun.teautil.models.RuntimeOptions());
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
> - **timeUnit**：拉取间隔时间的单位，支持 SECONDS、MINUTES、HOURS、DAYS
> - **interval**：拉取间隔，如果 timeUnit 为 SECONDS 时，interval 最小值为 6，即拉取间隔最小为 6 秒

### **渲染时拉取**

前面我们介绍了动态数据源的两种拉取策略：ONCE和INTERVAL，除此之外，我们还支持渲染时拉取（即卡片上屏时拉取）策略。如果想设置卡片渲染时拉取，可以进行调用服务端API-[创建卡片](../../01-应用开发/02-4a8AMF6u2A-服务端API/0778-interface-for-creating-a-card-instance.md)接口进行如下的配置：

HTTP

```
POST /v1.0/card/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
    "userId": "user123",
    "userIdType": 1,
    "cardTemplateId": "abcd-1234",
    "outTrackId": "my-out-trarck-id",
    "cardData": {
        "cardParamMap": {
            "title": "张三提交的报销单",
            "type": "差旅费",
            "reason": "出差费用",
            "status": "未审批",
            "amount": ""       //需要通过动态数据源获取的数据的字段，可以为空
        }
    },
    "openDynamicDataConfig": {
        "dynamicDataSourceConfigs": [
            {
                "dynamicDataSourceId": "example_ds_1",          // 动态数据源 ID
                "pullConfig": {
                    "pullStrategy": "RENDER"                   // 拉取策略
                }
            }
        ]
    }
}
```

Java

```
package com.aliyun.sample;

import java.util.ArrayList;
import java.util.List;

import com.aliyun.dingtalkcard_1_0.models.*;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfig;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs;
import com.aliyun.dingtalkcard_1_0.models.CreateCardRequest.CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig;
import com.aliyun.tea.*;

public class Sample {

    public static com.aliyun.dingtalkcard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcard_1_0.Client client = Sample.createClient();
        CreateCardHeaders createCardHeaders
            = new CreateCardHeaders();
        createCardHeaders.xAcsDingtalkAccessToken = "<your access token>";

        PrivateDataValue privateDataValueKey
            = new PrivateDataValue();
        java.util.Map<String, PrivateDataValue> privateData = TeaConverter.buildMap(
            new TeaPair("privateDataValueKey", privateDataValueKey)
        );
        CreateCardRequest.CreateCardRequestCardData cardData
            = new CreateCardRequest.CreateCardRequestCardData();

        //组装动态数据源配置
        CreateCardRequestOpenDynamicDataConfig openDynamicDataConfig = new CreateCardRequestOpenDynamicDataConfig();
        //字段映射类型默认填写REPLACE_WITHOUT_MAPPING
        openDynamicDataConfig.dynamicDataMappingMethod = "REPLACE_WITHOUT_MAPPING";

        //数据源配置列表
        List<CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs> configs = new ArrayList<>();
        CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs configs1 = new CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigs();
        //数据源id
        configs1.dynamicDataSourceId = "example_ds_1";

        //数据源拉取策略
        CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig pullConfig = new CreateCardRequestOpenDynamicDataConfigDynamicDataSourceConfigsPullConfig();
        pullConfig.pullStrategy = "RENDER";
        configs1.setPullConfig(pullConfig);

        configs.add(configs1);

        openDynamicDataConfig.dynamicDataSourceConfigs = configs;

        CreateCardRequest createCardRequest
            = new CreateCardRequest()
            .setUserId("my-user-id")
            .setUserIdType(1)
            .setOutTrackId("out-track-id")
            .setCardTemplateId("card-template-id")
            .setCardData(cardData)
            .setPrivateData(privateData);
        try {
            client.createCardWithOptions(createCardRequest, createCardHeaders,
                new com.aliyun.teautil.models.RuntimeOptions());
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

## **注意事项**

- 动态数据源回调有超时（TIMEOUT）限制，请在 2 秒内完成业务处理并响应。如果有比较耗时的业务逻辑处理（比如调用大模型），考虑异步调用[更新卡片](../../01-应用开发/02-4a8AMF6u2A-服务端API/0780-interactive-card-update-interface.md)的方式来更新卡片。
- 请勿在回调过程中调用更新接口。
