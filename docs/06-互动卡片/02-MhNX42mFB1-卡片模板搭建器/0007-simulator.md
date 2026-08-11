---
title: "模拟器"
source_url: "https://open.dingtalk.com/document/development/simulator"
namespace: "development"
slug: "simulator"
group: "互动卡片"
tab: "卡片模板搭建器"
breadcrumb: "面板介绍 > 模拟器"
doc_id: "VOchx7f0yr"
updated_at: "2025-09-23 19:18:27"
---

> Source: https://open.dingtalk.com/document/development/simulator
> Path: 互动卡片 / 卡片模板搭建器 / 面板介绍 > 模拟器
> Updated: 2025-09-23 19:18:27

# 模拟器

通过本文你可以了解到如何利用模拟器对卡片渲染的环境进行模拟以及如何快速地对组件进行调整、复制、删除等操作。

## **内容介绍**

模拟器位于卡片模板搭建器的中心区域。它主要负责卡片模板的环境模拟与实时预览，同时你还能在模拟器上快速地对组件进行布局调整等操作。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7143318661/p516144.png)

## **组件快速编辑**

在**编辑模式**下，我们可以对组件快速的进行拖拽调整、祖先组件快速选择、组件复制、删除等操作，能够有效地提高你编辑卡片的效率。

### **组件拖拽**

与添加组件相同，长按模拟器中的某个组件也可以进入拖拽模式，对组件的位置进行调整，如图所示：

![simulator_drag_component](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3982293761/p537997.gif)

在调整组件位置的同时，大纲树面板中的组件树也会同步组件位置信息，可以让你更加确定组件的所在位置。

### **祖先组件快速选择**

1. **选中目标组件**，当你在模拟器中点击**选中**某个组件时，你就可以发现组件在高亮的同时还出现了一个组件的操作栏，如图所示，操作栏从左到右分别是：**组件名**、**组件复制按钮**与**组件删除按钮**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6147989661/p516203.png)
2. 鼠标悬浮到**组件名**上，即可查看当前组件的所有祖先组件列表：![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6147989661/p516207.png)
3. 在组件名下方出现的祖先组件列表，点击其中一个组件后即可对其进行选中高亮并做相关的操作。![simulator_select_parent](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3982293761/p537998.gif)

### **组件复制**

选中目标组件，点击组件复制按钮，即可复制该组件到其所在组件树位置的兄弟节点处![simulator_com_copy](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3982293761/p537999.gif)

### **组件删除**

选中目标组件，点击组件删除按钮即可删除按钮![simulator_com_del](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3982293761/p538000.gif)

> **[!IMPORTANT]**
>
> 如果误删了某个组件也不用担心，可以通过撤销操作进行回退。在模拟器的配置栏中，可以发现「撤销」与「恢复」按钮，点击撤销即可。
>
> ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6147989661/p516219.png)
>
> 也可以通过以下快捷键进行撤回：
>
> - Windows 系统：`Ctrl` + `Z`
> - Mac 系统：`Command` + `Z`

## **预览模式**

如图所示，模拟器中支持编辑模式与预览模式的切换。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6147989661/p516190.png)

当卡片处于**预览模式**时，搭建器将会做以下处理：

- 卡片模板不可编辑
- 依据当前 Mock 的数据对卡片进行渲染
- 激活组件的**条件渲染**
- 激活组件的**循环渲染生效**
- 激活组件的**点击事件**

> **[!NOTE]**
>
> 对于条件渲染、循环渲染以及点击事件，详情参见[组件属性设置面板](0008-component-property-settings-panel.md)。

## **模拟器配置**

如图所示，模拟器的上半部分是模拟器的配置区域，支持渲染环境、黑夜模式、客户端版本号以及国际化等配置。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7143318661/p516158.png)

### **渲染环境配置**

渲染环境模拟了卡片在**桌面端、iOS、Android** 下渲染时的样子，默认为 iOS 环境。如图所示，点击「iOS」按钮打开下拉框后即可选择更换渲染环境。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6143318661/p516164.png)

其中，针对于「**桌面端**」环境下还支持**宽屏、窄屏模式**的切换，入口如下

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6143318661/p516166.png)

以下是宽屏、窄屏的区别：

| **窄屏** | **宽屏** |
| --- | --- |
| image | image |

### **黑夜模式切换**

卡片模板搭建器已默认为所有组件支持了黑夜模式，想要查看当前卡片在钉钉黑夜模式下的样子，点击模拟器配置栏中的「黑夜」按钮即可，如下为示例卡片黑夜模式下的截图：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6143318661/p516171.png)

### **客户端版本号与**国际化**配置**

如图所示，点击「更多」可以打开版本号以及国际化的配置面板，可以模拟真实客户端的版本号以及语言环境。

> **[!NOTE]**
>
> 想要支持国际化，需要在为卡片组件配置属性的时候填写国际化的相关配置，组件属性的配置参见[组件属性设置面板](0008-component-property-settings-panel.md)。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6143318661/p516172.png)
