---
title: "域名变量"
source_url: "https://open.dingtalk.com/document/connection/domain-name-variable-1"
namespace: "connection"
slug: "domain-name-variable-1"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发参考 > 高级功能 > 域名变量"
doc_id: "50PzZdRuzo"
updated_at: "2025-09-23 19:20:30"
---

> Source: https://open.dingtalk.com/document/connection/domain-name-variable-1
> Path: 连接平台 / 我的连接 / 开发参考 > 高级功能 > 域名变量
> Updated: 2025-09-23 19:20:30

# 域名变量

## **什么是域名变量**

域名变量是钉钉连接平台为了使连接器的使用更具有通用性、易用性而新推出的一种参数设置方式。

你可以在创建连接器后开启域名变量，用户可以在安装使用你提供的连接器模板时填写这个域名变量的值，从而使流模板更加通用化。

## **适用场景**

产品方案商在开发三方连接器时，如果要为不同用户提供服务的域名不相同时，则将域名变量交给需要使用的用户去填写，就可以将**高级设置—域名变量**开启。

## **开启域名变量**

1. 创建完连接器后，可以在**基本信息**中**高级设置**，开启域名变量。根据提示，点击**确定**，开启域名变量。

   > **[!NOTE]**
   >
   > 若开启后在「环境变量-接口域名」中配置了具体域名信息，将无法关闭。

   ![域名变量..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4393155861/p676316.png)
2. 开启域名变量后，需要到我的连接主界面中，设置环境变量的值。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4393155861/p676318.png)
3. 设置完成后，即可在执行动作中使用连接器域名。

   ![设置环境变量..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4393155861/p676323.png)
4. 连接器上架到连接器市场后，订阅该连接器，就需要用户自行填写接口域名。

   ![接口域名..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3393155861/p676340.png)
