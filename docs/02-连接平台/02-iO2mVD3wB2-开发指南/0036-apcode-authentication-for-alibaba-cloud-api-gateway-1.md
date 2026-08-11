---
title: "阿里云API网关AppCode鉴权"
source_url: "https://open.dingtalk.com/document/connection/apcode-authentication-for-alibaba-cloud-api-gateway-1"
namespace: "connection"
slug: "apcode-authentication-for-alibaba-cloud-api-gateway-1"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发参考 > 鉴权设置 > 阿里云API网关AppCode鉴权"
doc_id: "Hrh5iEnsMC"
updated_at: "2025-09-23 19:20:25"
---

> Source: https://open.dingtalk.com/document/connection/apcode-authentication-for-alibaba-cloud-api-gateway-1
> Path: 连接平台 / 开发指南 / 开发参考 > 鉴权设置 > 阿里云API网关AppCode鉴权
> Updated: 2025-09-23 19:20:25

# 阿里云API网关AppCode鉴权

> **[!IMPORTANT]**
>
> 本文鉴权使用简单认证（AppCode）方式调用阿里云API网关，详细可参考[阿里云使用简单认证（AppCode）方式调用API](https://help.aliyun.com/document_detail/115437.html?spm=a2c4g.29475.0.0.290247f0rbIsPw)官方文档。

## **简介**

API网关AppCode鉴权简单认证，省去了复杂的生成签名的过程。简单认证方式直接使用API网关颁发的AppCode进行身份认证，调用者将AppCode放到请求头中，或者放到请求的Query参数中进行身份认证，实现快速调用API的能力。

## **准备工作**

- 拥有所在钉钉组织开发者后台的[开发者权限](https://open.dingtalk.com/document/dingstart/dingtalk-developer)。
- 拥有一个所在钉钉组织连接平台的[连接器](0013-create-connector.md)。
- 拥有一个[阿里云API网关应用](https://apigateway.console.aliyun.com/?spm=5176.8465980.top-nav.22.432e1450nEHDnz&accounttraceid=59d7a2cdbc244dce96d55203fa295c49mgvw#/cn-hangzhou/apps/list?AppName=)并查询应用AppCode。

  ![appCode获取..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8851065861/p676807.png)

## **鉴权设置**

1. 单击鉴权设置：

   **选择鉴权方式：**自定义签名鉴权。

   ![鉴权方式选择- API网关..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9751065861/p676816.png)
2. **设置鉴权字段，**并单击**下一步**：

   - **字段key**：appCode
   - **字段标题**：阿里云API网关AppCode
   - **是否必填**：是
   - **展示类型**：文本
   - **字段说明**：阿里云API网关AppCode，从[阿里云控制台](https://apigateway.console.aliyun.com/?spm=5176.8465980.top-nav.22.432e1450nEHDnz&accounttraceid=59d7a2cdbc244dce96d55203fa295c49mgvw#/cn-hangzhou/apps/list?AppName=)获取

     ![设置鉴权字段-API网关..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8851065861/p676819.png)
3. **设置鉴权请求参数，**并单击**保存配置并调试**。

   **HTTP请求头：**

   - **Key：**Authorization

     ![Key-API请求参数..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8851065861/p676831.png)
   - **Value：使用表达式**

     阿里云API网关鉴权的AppCode，会作为鉴权字段传入，这里由于使用的值是：Authorization是AppCode值，因此选择表达式。

     1. 单击**请点击进行设置：**

        ![表达式设置..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8851065861/p676983.png)
     2. 编辑表达式，并单击**确认**：

        ![AppCode..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8851065861/p676999.png)
4. 鉴权调试：

   1. 设置鉴权调试接口：

      ![设置调试接口..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8851065861/p677132.png)
   2. 设置鉴权调试参数：

      ![设置调试参数..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8851065861/p677135.png)
   3. 添加账户：

      ![添加账户..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8851065861/p677137.png)
   4. 单击**鉴权调试，**查看调试结果：

      ![鉴权完成..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8851065861/p677140.png)
   5. 单击**完成调试**，实现保存。

      ![完成调试并保存..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8851065861/p677143.png)
