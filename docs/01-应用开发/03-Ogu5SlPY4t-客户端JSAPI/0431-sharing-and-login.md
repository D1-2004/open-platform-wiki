---
title: "分享与登录"
source_url: "https://open.dingtalk.com/document/development/sharing-and-login"
namespace: "development"
slug: "sharing-and-login"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "常见问题 > 分享与登录"
doc_id: "mq72NxOGdu"
updated_at: "2025-08-28 19:54:57"
---

> Source: https://open.dingtalk.com/document/development/sharing-and-login
> Path: 应用开发 / 客户端JSAPI / 常见问题 > 分享与登录
> Updated: 2025-08-28 19:54:57

# 分享与登录

本文介绍了分享与登录的常见问题。

## 调用Android应用授权登录接入流程报错'Caused by: android.content.pm.PackageManager$NameNotFoundException: com.alibaba.android.rimet'

答：调用[Android应用授权登录接入流程](https://open.dingtalk.com/document/orgapp/android-platform-application-authorization-login-access)出现上述错误时，需要在AndroidManifest.xml该文件内添加要查询的APP包名。

例如：<queries> <package android:name="com.instagram.android" /></queries>

> **[!IMPORTANT]**
>
> 针对Android 11：添加上<queries>标签才会判断安卓手机已安装钉钉。
