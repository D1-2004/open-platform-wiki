---
title: "静态二维码接入"
source_url: "https://open.dingtalk.com/document/development/gwdrtm"
namespace: "development"
slug: "gwdrtm"
group: "硬件开发"
tab: "智能硬件"
breadcrumb: "钉钉SDK(门禁/考勤机)接入 > 静态二维码接入"
doc_id: "euswLv4p6P"
updated_at: "2025-10-09 18:05:25"
---

> Source: https://open.dingtalk.com/document/development/gwdrtm
> Path: 硬件开发 / 智能硬件 / 钉钉SDK(门禁/考勤机)接入 > 静态二维码接入
> Updated: 2025-10-09 18:05:25

# 静态二维码接入

## 1.头文件

```
#include "dtiot_netconfig_bind_service.h"
```

## 2.静态二维码绑定

## 2.1 启动静态二维码绑定

**场景：**启动静态二维码绑定

**函数：**

```
  int (*static_bind_start)();
```

## 2.2 停止静态二维码绑定

**场景：**停止静态二维码绑定

**函数：**

```
  int (*static_bind_stop)(void);
```
