---
title: "阿里云OSS签名鉴权"
source_url: "https://open.dingtalk.com/document/connection/alibaba-cloud-oss-signature-authentication-1"
namespace: "connection"
slug: "alibaba-cloud-oss-signature-authentication-1"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发参考 > 鉴权设置 > 官方模板鉴权 > 阿里云OSS签名鉴权"
doc_id: "RilYFQ2e7Y"
updated_at: "2026-07-27 17:25:52"
---

> Source: https://open.dingtalk.com/document/connection/alibaba-cloud-oss-signature-authentication-1
> Path: 连接平台 / 我的连接 / 开发参考 > 鉴权设置 > 官方模板鉴权 > 阿里云OSS签名鉴权
> Updated: 2026-07-27 17:25:52

# 阿里云OSS签名鉴权

> **[!IMPORTANT]**
>
> 本文鉴权使用Header中包含签名的方式调用阿里云OSS REST API，详情参见[使用阿里云OSS REST API发起请求](https://help.aliyun.com/document_detail/375247.html?spm=a2c4g.31951.0.0.15933a285vpYob)和[在Header中包含签名](https://help.aliyun.com/document_detail/31951.html?spm=a2c4g.375247.0.0.127c7d22b71pco)的官方文档。

## **简介**

REST API发起请求适用于对程序自定义要求较高的场景。需要手动编写代码计算签名并将签名添加到REST API请求中。OSS仅支持虚拟托管（Virtual Hosted）风格的REST API请求。

## **准备工作**

- 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
- 拥有一个所在钉钉组织连接平台的[连接器](0010-create-connector.md)。

## **鉴权设置**

> **[!NOTE]**
>
> 鉴权字段**accessKeyId**和**accessKeySecret**需登录[阿里云RAM访问控制](https://ram.console.aliyun.com/manage/ak?spm=5176.2020520153.top-nav.dak.48b1336aNUXAbI)查看。

1. 单击鉴权设置，选择**自定义签名鉴权**方式。

   ![鉴权方式选择- API网关..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2534415871/p676816.png)
2. **设置鉴权字段，**并单击**下一步**：

   ![设置鉴权字段..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2534415871/p677182.png)
3. **设置鉴权请求参数，**并单击**保存配置并调试**。

   **HTTP请求头：**

   - **Date：表达式 >** `FORMATDATE(NOW(),'E, dd MMM yyyy HH:mm:ss z','GMT')`。

     ![表达式设置-oss..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2534415871/p677217.png)
   - **Authorization：Python。**

     ![python-oss..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2534415871/p677218.png)

     ```
     import json
     import base64
     import hmac
     import hashlib
     import datetime
     import os
     import requests
     from urllib.parse import urlparse

     VERB = method
     accessKeyId = authFields.get('accessKeyId')
     accessKeySecret = authFields.get('accessKeySecret')
     DATE = headers.get('Date')
     bucketName = urlparse(url).hostname.split('.')[0]
     objectName = '/' if path == '' else path
     # 以下为CANONICALIZED_RESOURCE的生成规则
     # 如果既有BucketName也有ObjectName，则则CanonicalizedResource格式为/BucketName/ObjectName
     # 如果仅有BucketName而没有ObjectName，则CanonicalizedResource格式为/BucketName/。
     # 如果既没有BucketName也没有ObjectName，则CanonicalizedResource为正斜线（/）。
     # 如果请求的资源包括子资源（SubResource），则所有的子资源需按照字典序升序排列，并以&为分隔符生成子资源字符串。在CanonicalizedResource字符串尾添加?和子资源字符串。此时的CanonicalizedResource为/BucketName/ObjectName?acl&uploadId=UploadId
     # 前缀如果是endpoint，说明是OSS维度的查询，这时候CANONICALIZED_RESOURCE直接设置为/
     if bucketName in ['oss-cn-hangzhou','oss-cn-shanghai','oss-cn-qingdao','oss-cn-beijing','oss-cn-zhangjiakou','oss-cn-huhehaote','oss-cn-shenzhen','oss-cn-heyuan','oss-cn-chengdu','oss-cn-hongkong','oss-us-west-1','oss-us-east-1','oss-ap-southeast-1','oss-ap-southeast-2','oss-ap-southeast-3','oss-ap-southeast-5','oss-ap-northeast-1','oss-ap-south-1','oss-eu-central-1','oss-eu-west-1','oss-me-east-1']:
         CANONICALIZED_RESOURCE = "/"
     else:
         CANONICALIZED_RESOURCE = "/" + bucketName + objectName

     canonicalized_oss_headers_str = ""
     CANONICALIZED_OSS_HEADERS = headers
     for key in sorted(CANONICALIZED_OSS_HEADERS):
         if key.lower().startswith("x-oss-"):
             value = CANONICALIZED_OSS_HEADERS[key]
             canonicalized_oss_headers_str += f"{key.lower()}:{value}\n"

     string_to_sign = '\n'.join([VERB, "", contentType, DATE, canonicalized_oss_headers_str + CANONICALIZED_RESOURCE])
     signature = base64.b64encode(hmac.new(accessKeySecret.encode('utf-8'), string_to_sign.encode('utf-8'), hashlib.sha1).digest()).decode('utf-8')
     authorization = 'OSS ' + accessKeyId + ':' + signature
     return authorization
     ```
4. 鉴权调试：

   1. 设置鉴权调试接口：

      ![设置入参-调试-oss..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2534415871/p677219.png)
   2. 单击**添加账户。**

      ![添加账户-oss..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2534415871/p677221.png)
   3. **完成账户添加。**

      ![完成账户添加..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2534415871/p677220.png)
   4. 单击**鉴权调试**，查看调试结果。

      ![调试结果-oss..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2534415871/p677222.png)
   5. 单击**完成调试**，实现保存。

      > **[!NOTE]**
      >
      > 由于OSS REST API返回的都是XML格式的内容，需要自行处理。

      ![完成调试并保存-oss..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2534415871/p677223.png)
