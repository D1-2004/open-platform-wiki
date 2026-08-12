---
title: "Token鉴权"
source_url: "https://open.dingtalk.com/document/connection/token-authentication-1"
namespace: "connection"
slug: "token-authentication-1"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发参考 > 鉴权设置 > Token鉴权"
doc_id: "kcZeiqkDto"
updated_at: "2026-07-27 17:25:46"
---

> Source: https://open.dingtalk.com/document/connection/token-authentication-1
> Path: 连接平台 / 我的连接 / 开发参考 > 鉴权设置 > Token鉴权
> Updated: 2026-07-27 17:25:46

# Token鉴权

本文档主要介绍连接器Token鉴权方式的设置步骤。

## **基本介绍**

Token鉴权：指用户在请求接口时，通过填写自定义鉴权字段，然后在指定接口验证成功后获取Token，后续用户携带Token信息请求接口，实现对用户身份的验证。

> **[!NOTE]**
>
> 使用自定义鉴权字段验证通过，获取Token，在请求时将Token信息添加到消息头，从而通过身份认证。

Token鉴权根据验证通过后获取的Token进行鉴权，在连接平台您需要进行如下几步操作：

- **选择鉴权方式**为TOKEN鉴权。
- **设置鉴权字段**，自定义鉴权字段，例如accessKey用户名和accessSecret密码。
- **设置Token请求接口**

  1. **设置Token获取接口**，填写获取Token的请求方式和请求接口。
  2. **设置参数位置**（可选），设置参数所在位置以及填写请求接口所需参数。
  3. **设置Token失效判断**，根据系统字段或者自定义方式判断失效。
- 设置**鉴权请求参数**，例如设置HTTP Header中请求参数为token。
- **鉴权验证**

  1. **设置鉴权验证接口**，填写鉴权验证接口的请求方式和请求验证的接口。
  2. **设置鉴权验证参数**（可选），选择请求方式，填写接口所需参数。
  3. 进行**鉴权验证**，通过填写鉴权字段请求鉴权验证接口，如果携带获取到的Token并且没有过期，服务器则根据请求，将所请求资源发送给客户端。

在鉴权中，常用的有**Basic**和**Bearer**两种类型的Token，各自使用场景不同。本示例会对两种类型都进行操作说明。

## **Basic Token鉴权示例**

1. **选择鉴权方式**为TOKEN鉴权。

   ![Toke鉴权-选择鉴权方式A](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534154.png)
2. 自定义鉴权字段，例如：accessKey和accessSecret，单击**下一步**。

   > **[!NOTE]**
   >
   > 此项为可选设置项，如果没有自定义鉴权字段则无需设置，直接进入下一步，文本类型支持密码类型，可对文本进行隐藏。

   ![Toke鉴权-选择鉴权字段A](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534155.png)
3. 设置token请求接口，包括**设置Token获取接口**、**设置参数位置**、**Token失效判断。**

   ![Toke鉴权-设置Token请求接口总览A](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534156.png)
4. **设置Token获取接口**，选择**GET**请求方式，并输入接口地址。

   > **[!NOTE]**
   >
   > 接口请求方式支持**GET**、**POST**、**PATCH**、**PUT**四种请求方式，请根据真实接口选择相应的请求方式和获取Token的地址。

   ![Toke鉴权-设置Token获取接口A](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534157.png)
5. **设置参数位置**（可选），选择**URL查询参数**类型，填写参数字段，选择**鉴权字段**，通过直接获取鉴权字段获取值。

   > **[!NOTE]**
   >
   > - **HTTP Header**为HTTP的请求头，提供客户端信息。
   > - **URL查询参数**将参数附加在请求URL的末尾，在'?'之后。
   > - **HTTP Body**为HTTP的请求体，POST请求方式中传递参数给服务器。

   ![Toke鉴权-设置参数位置A](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534158.png)

   ​参数位置支持以下三种方式设置：

   - **固定值**：填写已知的固定值作为传参的值。
   - **鉴权字段**：引用鉴权字段中的accessKey或accessSecret的值。
   - **表达式**：通过表达式进行参数加密或者字符串转换等来设置值，表达式如何使用，详情请参考[表达式](https://open.dingtalk.com/document/connector/overview-of-expressions)。
6. **Token失效判断**，选择**自定义**方式，填写$.Body.errorCode获取方法和判断值token\_not\_effective。

   > **[!IMPORTANT]**
   >
   > - 请求**Token获取接口**后返回结果，可以通过$.Body.xx或$.Header.xx格式获取，请根据实际接口中的返回结果填写获取方法和判断值。
   > - Token鉴权时，连接平台会在用户创建账户的时候缓存Token，避免频繁的Token请求。当Token失效时，连接平台会根据用户配置的Token失效判断规则，对HTTP的返回结果进行判断，如果与规则匹配，说明是Token失效导致的请求异常，连接平台会重新请求Token获取的接口并使用新的Token发起系统重试，过程中会缓存返回的新Token作为之后HTTP请求的鉴权Token。因此如果Token不是永久有效，Token失效判断必须配置，否则存在连接器运行一段时间后不可用的风险。

   ![Toke鉴权-Token失效判断A](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534159.png)

   - **系统字段**：根据Http状态码的值来判断是否失效。
   - **自定义**：根据请求**Token获取接口**后返回结果中Body的errorCode（**$.Body.errorCode**）来判断，如果返回值为token\_not\_effective则判定Token失效。
7. **设置鉴权请求参数**，选择**HTTP Header**请求方式，添加**token**，选择**固定值**，填写**Token获取接口**返回的结果值。

   > **[!NOTE]**
   >
   > - 如果鉴权请求接口需要携带额外参数，支持**HTTP Header**、**URL查询参数**两种传参方式，请根据真实接口选择对应的方式进行参数设置。
   > - **设置鉴权请求参数**需要获取到**设置token请求接口**返回的token值作为入参条件，可通过$.Body.xx或$.Header.xx格式获取，请根据实际接口返回结果选择相应的格式获取token值。

   ![Basic Token-设置鉴权请求参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534160.png)

   鉴权请求参数值支持以下三种方式设置：

   - **固定值**：支持填写固定值和$Body.result格式获取token请求接口返回结果中的字段值。
   - **鉴权字段**：引用鉴权字段中的accessKey或accessSecret。
   - **表达式**：通过表达式进行参数加密或者字符串转换等来设置值，表达式如何使用，详情请参考[表达式](0008-expression-overview.md)。
8. **设置鉴权验证接口**，选择**GET**请求方式，并输入接口地址。

   > **[!NOTE]**
   >
   > 接口请求方式支持**GET**、**POST**、**PATCH**、**PUT**四种请求方式，请根据真实接口选择相应的请求方式和地址。

   ![Basic Token-设置鉴权验证接口](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534161.png)
9. **设置鉴权验证参数**（可选），选择**URL查询参数**类型，填写参数字段，选择**固定值**，并填写参数的值。

   > **[!NOTE]**
   >
   > 此项为可选项，如果请求接口需要携带额外参数，支持**HTTP Header**、**URL查询参数**、**HTTP Body**三种传参方式，请根据真实接口选择对应的方式进行参数设置。

   ![Basic Token-设置鉴权验证参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534162.png)
10. 进行**鉴权验证**，填写accessKey和accessSecret，单击**鉴权验证**，查看返回结果是否符合预期，最后单击**完成**。

    ![Basic Token-进行鉴权验证](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534163.png)

    - 返回结果，如果鉴权通过，成功返回请求接口的信息*。*

      ![Basic Token-返回结果](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534164.png)
    - 返回结果，如果鉴权失败，需要查看以下请求入参信息是否设置正确

      ![Basic Token-请求入参](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534165.png)

      - 请求地址**url**中接口地址和需要携带**URL查询参数**是否正确。
      - 请求方式**method**是否设置正确。
      - 请求头**headers**中需要携带的参数（如：token）是否加密正确**。**

## **Bearer Token鉴权示例**

1. **选择鉴权方式**为TOKEN鉴权。

   ![Toke鉴权-选择鉴权方式B](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534166.png)
2. 设置鉴权字段（可选），自定义鉴权字段，例如：accessKey和accessSecret。

   > **[!NOTE]**
   >
   > ​此项为可选设置项，如果没有自定义鉴权字段则无需设置，直接进入下一步，文本类型支持密码类型，可对文本进行隐藏。

   ![Toke鉴权-选择鉴权字段B](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534167.png)
3. 设置token请求接口，包括**设置Token获取接口**、**设置参数位置**、**Token失效判断。**

   ![Toke鉴权-设置Token请求接口总览B](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534168.png)
4. **设置Token获取接口**，选择**GET**请求方式，并输入接口地址。

   > **[!NOTE]**
   >
   > 接口请求方式支持**GET**、**POST**、**PATCH**、**PUT**四种请求方式，请根据真实接口选择相应的请求方式和获取Token的地址。

   ![Toke鉴权-设置Token获取接口B](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534169.png)
5. **设置参数位置**（可选），选择**URL查询参数**类型，填写参数字段，选择**鉴权字段**，通过直接获取鉴权字段获取值。

   > **[!NOTE]**
   >
   > 此项为可选设置项，如果请求接口需要携带额外参数，支持**HTTP Header**、**URL查询参数**、**HTTP Body**三种传参方式，请根据真实接口选择对应的方式进行参数设置

   ![Toke鉴权-设置参数位置B](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534170.png)

   参数位置支持以下三种方式设置：

   - **固定值**：填写已知的固定值作为传参的值。
   - **鉴权字段**：引用鉴权字段中的accessKey或accessSecret的值。
   - **表达式**：通过表达式进行参数加密或者字符串转换等来设置值，表达式如何使用，详情请参考[表达式](0008-expression-overview.md)。
   - **Token失效判断**

     选择**自定义**方式，填写$.Body.errorCode获取方法和判断值token\_not\_effective。

     > **[!IMPORTANT]**
     >
     > - 请求**Token获取接口**后返回结果，可以通过$.Body.xx或$.Header.xx格式获取，请根据实际接口中的返回结果填写获取方法和判断值。
     > - Token鉴权时，连接平台会在用户创建账户的时候缓存Token，避免频繁的Token请求。当Token失效时，连接平台会根据用户配置的Token失效判断规则，对HTTP的返回结果进行判断，如果与规则匹配，说明是Token失效导致的请求异常，连接平台会重新请求Token获取的接口并使用新的Token发起系统重试，过程中会缓存返回的新Token作为之后HTTP请求的鉴权Token。因此如果Token不是永久有效，Token失效判断必须配置，否则存在连接器运行一段时间后不可用的风险。

     ![Toke鉴权-Token失效判断B](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534171.png)

     - **系统字段**：根据Http状态码的值来判断是否失效。
     - **自定义**：根据请求**Token获取接口**后返回结果中Body的errorCode（**$.Body.errorCode**）来判断，如果返回值为token\_not\_effective则判定Token失效。
6. **设置鉴权请求参数**，选择**HTTP Header**请求方式，添加携带的参数，选择**表达式**，添加携带参数的值，单击**下一步。**

   > **[!NOTE]**
   >
   > - 如果鉴权请求接口需要携带额外参数，支持**HTTP Header**、**URL查询参数**两种传参方式，请根据真实接口选择对应的方式进行参数设置。
   > - **设置鉴权请求参数**需要获取到**设置token请求接口**返回的token值作为入参条件，可通过$.Body.xx或$.Header.xx格式获取，请根据实际接口返回结果选择相应的格式获取token值。

   ![Bearer Token-设置鉴权请求参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534172.png)

   鉴权请求参数值支持以下三种方式设置：

   - **固定值**：支持填写固定值。
   - **鉴权字段**：引用鉴权字段中的accessKey或accessSecret。
   - **表达式**：Authorization值为字符串“Bearer ”与请求**Token获取接口**后返回结果中Body的result（**$.Body.result**）的值拼在一起的字符串，表达式如何使用，详情请参考[表达式](0008-expression-overview.md)。

     ![Bearer Token-鉴权请求参数表达式](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534173.png)
7. **设置鉴权验证接口**，选择**GET**请求方式，并输入接口地址

   ![Bearer Token-设置鉴权验证接口](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534174.png)
8. **设置鉴权验证参数**（可选），​选择**URL查询参数**类型，填写参数字段，选择**固定值**，并填写参数的值。

   > **[!NOTE]**
   >
   > 此项为可选项，如果请求接口需要携带额外参数，支持**HTTP Header**、**URL查询参数**、**HTTP Body**三种传参方式，请根据真实接口选择对应的方式进行参数设置。

   ![Bearer Token-设置鉴权验证参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534175.png)

   鉴权验证参数值支持以下三种方式设置：

   - **固定值**：填写已知的固定值作为传参的值。
   - **鉴权字段**：引用鉴权字段中的accessKey或accessSecret。
   - **表达式**：通过表达式进行参数加密或者字符串转换等来设置值，表达式如何使用，详情请参考[表达式](0008-expression-overview.md)。
9. 进行**鉴权验证**，填写accessKey和accessSecret，单击**鉴权验证**，查看返回结果是否符合预期，最后单击**完成**。

   ![Bearer Token-进行鉴权验证](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534176.png)

   - 返回结果，如果鉴权通过，成功返回请求接口的信息*。*

     ![Bearer Token-返回结果](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534177.png)
   - 返回结果，如果鉴权失败，需要查看以下请求入参信息是否设置正确：

     ![Bearer Token-请求入参](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825980761/p534178.png)

     - 请求地址**url**中接口地址和需要携带**URL查询参数**是否正确。
     - 请求方式**method**是否设置正确。
     - 请求头**headers**中需要携带的参数（如：token）是否加密正确**。**
