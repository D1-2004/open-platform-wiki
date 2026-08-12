---
title: "其他JSAPI参考"
source_url: "https://open.dingtalk.com/document/dingstart/other-jsapi-references-1"
namespace: "dingstart"
slug: "other-jsapi-references-1"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > API参考 > 其他JSAPI参考"
doc_id: "USgzXTN0g3"
updated_at: "2025-09-03 15:57:14"
---

> Source: https://open.dingtalk.com/document/dingstart/other-jsapi-references-1
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > API参考 > 其他JSAPI参考
> Updated: 2025-09-03 15:57:14

# 其他JSAPI参考

本文介绍组件支持的其他参考自JSAPI的SDK。

## 查看地图位置

**openLocation**

更多参数内容。请参考[使用内置地图查看位置](../../01-应用开发/03-Ogu5SlPY4t-客户端JSAPI/0325-jsapi-open-location.md)。

```
getSdk().openLocation({
    longitude: '120.126293',
    latitude: '30.274653',
    name: '黄龙万科中心',
    address: '学院路77号',
});
```

## 扫码

**scan**

更多参数内容。请参考[扫码](../../01-应用开发/03-Ogu5SlPY4t-客户端JSAPI/0406-jsapi-scan.md)。

```
getSdk().scan({
    type: 'qr',
    success: (res) => {
       dd.alert({ title: res.code });
    },
});
```
