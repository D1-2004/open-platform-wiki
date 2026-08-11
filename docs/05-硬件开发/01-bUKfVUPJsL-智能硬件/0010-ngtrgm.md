---
title: "动态二维码接入"
source_url: "https://open.dingtalk.com/document/development/ngtrgm"
namespace: "development"
slug: "ngtrgm"
group: "硬件开发"
tab: "智能硬件"
breadcrumb: "钉钉SDK(门禁/考勤机)接入 > 动态二维码接入"
doc_id: "ZZ2KgtoENz"
updated_at: "2025-10-09 18:05:25"
---

> Source: https://open.dingtalk.com/document/development/ngtrgm
> Path: 硬件开发 / 智能硬件 / 钉钉SDK(门禁/考勤机)接入 > 动态二维码接入
> Updated: 2025-10-09 18:05:25

# 动态二维码接入

## 1.头文件

```
#include "dtiot_netconfig_bind_service.h"
```

## 2.动态二维码绑定

## 2.1 启动动态二维码绑定

**场景：**启动动态二维码绑定

**函数：**

```
 int (*dynamic_bind_start)(void (*on_qrcode_update)(int length, char* qrcode));
```

需要传入一个函数指针用于接收动态二维码的更新，用于显示绑定。

## 2.2 停止动态二维码绑定

**场景：**停止动态二维码绑定

**函数：**

```
int (*dynamic_bind_stop)(void);
```
