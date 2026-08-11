---
title: "createIntersectionObserver"
source_url: "https://open.dingtalk.com/document/development/jsapi-create-intersection-observer"
namespace: "development"
slug: "jsapi-create-intersection-observer"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 节点查询 > createIntersectionObserver"
doc_id: "FiKu8nUf08"
updated_at: "2023-08-11"
---

> Source: https://open.dingtalk.com/document/development/jsapi-create-intersection-observer
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 节点查询 > createIntersectionObserver
> Updated: 2023-08-11

# createIntersectionObserver

调用createIntersectionObserver，创建并返回一个IntersectionObserver对象实例。

> 需在page.onReady之后执行dd.createIntersectionObserver()。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10035) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

参数占位区域

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.createIntersectionObserver(true, [0], 0);
```
