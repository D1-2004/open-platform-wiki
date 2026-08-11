---
title: "摄像头反向二维码接入"
source_url: "https://open.dingtalk.com/document/development/xvdsha"
namespace: "development"
slug: "xvdsha"
group: "硬件开发"
tab: "智能硬件"
breadcrumb: "Android设备接入SDK > 摄像头反向二维码接入"
doc_id: "EGWnc2jg9J"
updated_at: "2026-03-06 09:16:03"
---

> Source: https://open.dingtalk.com/document/development/xvdsha
> Path: 硬件开发 / 智能硬件 / Android设备接入SDK > 摄像头反向二维码接入
> Updated: 2026-03-06 09:16:03

# 摄像头反向二维码接入

本文档介绍了摄像头反向二维码功能的SDK接入方式，包括启动与停止绑定流程。

## 引入SDK依赖类

请确保项目中已引入以下类：

```
import com.alibaba.dingtalk.inside.bind.DingTalkInsideSdk;
```

## 启动摄像头反向二维码绑定

**场景**：使用摄像头反向二维码绑定. 当设备扫描到二维码后调用此api启动摄像头反向二维码绑定。

**函数**：

```
public static void cameraBindStart(String qrcode);
```

## 停止摄像头反向二维码绑定

**场景**：停止摄像头反向二维码绑定。

**函数**：

```
public static void cameraBindStop();
```

## **示例代码**

```
// 初始化并启动摄像头反向二维码绑定
public void startBinding() {
  String scannedQrCode = qrScanner.scan(); // 获取扫描结果
  if (scannedQrCode != null && !scannedQrCode.isEmpty()) {
    DingTalkInsideSdk.cameraBindStart(scannedQrCode); // 启动绑定
    System.out.println("摄像头反向二维码绑定成功");
  }
}

// 停止绑定流程（例如绑定成功或取消操作）
public void stopBinding() {
  DingTalkInsideSdk.cameraBindStop();
  System.out.println("摄像头反向二维码绑定已停止");
}
```
