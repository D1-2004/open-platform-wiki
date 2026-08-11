---
title: "钉钉开放接口鉴权"
source_url: "https://open.dingtalk.com/document/connection/dingtalk-open-interface-authentication-1"
namespace: "connection"
slug: "dingtalk-open-interface-authentication-1"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发参考 > 鉴权设置 > 钉钉开放接口鉴权"
doc_id: "UhfbFdUx9Y"
updated_at: "2025-09-23 19:20:23"
---

> Source: https://open.dingtalk.com/document/connection/dingtalk-open-interface-authentication-1
> Path: 连接平台 / 开发指南 / 开发参考 > 鉴权设置 > 钉钉开放接口鉴权
> Updated: 2025-09-23 19:20:23

# 钉钉开放接口鉴权

## **简介**

钉钉开放接口鉴权，企业或开发者可以根据特定需要，对钉钉开放接口实现自定义的鉴权操作，进一步提高连接器的灵活性、可控性和易用性，真正实现了连接器个性化和定制化的服务能力。

## **鉴权示例**

因钉钉开放接口获取 Token 的方式存在新版和旧版的区别。本示例将提供钉钉新旧版 Token 的鉴权示例。

钉钉开放接口新旧版差异，详情参见[旧版服务端API、新版服务端API的区别](https://open.dingtalk.com/document/development/how-to-call-apis#section-8lr-id4-rbz)。

## **准备工作**

1. 拥有所在钉钉组织开发者后台的[成为钉钉开发者](https://open.dingtalk.com/document/dingstart/dingtalk-developer)。
2. 拥有一个所在钉钉组织开发者后台的[企业内部应用](../../01-应用开发/01-XOnnmGCTbn-开发指南/0002-application-type-introduction.md#b85664702cyp7)。
3. 拥有一个所在钉钉组织连接平台的[创建连接器](0013-create-connector.md)。

## **示例一：**新版服务端接口鉴权

> **[!IMPORTANT]**
>
> - **$.Query：**获取授权重定向后链接上的参数。
> - **$.Body：**获取 Token 接口返回的 Body 参数。
> - **$.Header**：获取 Token 接口返回的 Header 参数。

1. 单击鉴权设置：

   **选择鉴权方式**：TOKEN鉴权。

   ![旧版TOKEN选择](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629453.png)
2. 设置鉴权字段。

   ![新版设置appKey](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629640.png)
3. 设置 token 请求接口：

   - 设置 Token 获取接口**：**

     - **请求方式：**`POST`。
     - **请求路径：**`https://api.dingtalk.com/v1.0/oauth2/accessToken`。

       ![新版设置Token获取接口](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629642.png)
   - 设置参数位置**：**

     ![新版设置请求参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629661.png)
   - Token 失效判断：

     ![新版Token失效..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p645833.png)
4. 设置鉴权请求参数。

   ![新版设置鉴权请求参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629668.png)
5. 鉴权验证：

   - 设置鉴权验证接口：

     - **请求方式：**`GET`。
     - **请求路径：**`https://api.dingtalk.com/v1.0/microApp/allInnerApps`。

       ![新版设置验证接口](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629769.png)
   - 鉴权验证：

     1. 添加账户。

        > **[!NOTE]**
        >
        > 可通过准备工作第2点的企业内部应用中获取。

        ![旧版账户添加](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629510.png)
     2. 鉴权验证。

        ![旧版鉴权验证](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629515.png)
     3. 验证返回结果：

        - 正确结果：

          ![新版返回结果正确](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p630442.png)
        - 错误结果，如果鉴权失败或者接口调用失败，需要查看以下信息是否正确：

          - 请求入参：

            - 请求地址 **url** 中接口地址是否正确。
            - 请求方式 **method** 是否设置正确。
            - 请求头 **headers** 中自动生成的 **x-acs-dingtalk-access-token** 是否正确。

              ![新版请求入参](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p630471.png)
          - 返回结果：

            提示接口没有权限，需申请接口权限后重新鉴权验证即可，详情参见[权限管理](https://open.dingtalk.com/document/orgapp/permission-management)。

            ![新版权限未申请](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p630713.png)
     4. 单击**完成**保存鉴权配置。

## **示例二：旧版服务端接口鉴权**

> **[!IMPORTANT]**
>
> - **$.Query：**获取授权重定向后链接上的参数。
> - **$.Body：**获取 Token 接口返回的 Body 参数。
> - **$.Header**：获取 Token 接口返回的 Header 参数。

1. 单击鉴权设置：

   - **选择鉴权方式**：TOKEN鉴权。

     ![旧版TOKEN选择](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629453.png)
2. 设置鉴权字段。

   ![设置旧版appkey](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629461.png)
3. 设置 token 请求接口：

   - 设置 Token 获取接口**：**

     - **请求方式：**`GET`。
     - **请求路径：**`https://oapi.dingtalk.com/gettoken`。

       ![旧版设置获取token](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629469.png)
   - 设置参数位置**：**

     ![旧版设置参数位置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629473.png)
   - Token 失效判断：

     ![旧版token失效..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0518337861/p671329.png)
4. 设置鉴权请求参数。

   ![旧版设置鉴权请求参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629479.png)
5. 鉴权验证：

   - 设置鉴权验证接口：

     - **请求方式：**`POST`。
     - **请求路径：**`https://oapi.dingtalk.com/topapi/user/count`。

       ![设置鉴权验证接口](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629487.png)
   - 设置鉴权验证参数：

     ![旧版设置鉴权验证参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629496.png)
   - 鉴权验证：

     1. 添加账户。

        > **[!NOTE]**
        >
        > 可通过准备工作第2点的企业内部应用中获取。

        ![旧版账户添加](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629510.png)
     2. 鉴权验证。

        ![旧版鉴权验证](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629515.png)
     3. 验证返回结果：

        - 正确结果：

          ![旧版返回结果](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629523.png)
        - 错误结果，如果鉴权失败或者接口调用失败，需要查看以下信息是否正确：

          - 请求入参：

            - 请求地址 **url** 中接口地址和需要携带 **URL查询参数** 是否正确。
            - 请求方式 **method** 是否设置正确。
            - 请求体 **body** 中的请求体参数是否正确。

              ![验证请求入参](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629581.png)
          - 返回结果：

            提示接口没有权限，需申请接口权限后重新鉴权验证即可，详情参见[添加接口调用权限](../../01-应用开发/02-4a8AMF6u2A-服务端API/0003-add-api-permission.md)。

            ![旧版权限申请](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3902852861/p629584.png)
     4. 单击**完成**保存鉴权配置。
