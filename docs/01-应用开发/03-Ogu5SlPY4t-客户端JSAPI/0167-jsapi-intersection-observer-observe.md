---
title: "IntersectionObserver.observe"
source_url: "https://open.dingtalk.com/document/development/jsapi-intersection-observer-observe"
namespace: "development"
slug: "jsapi-intersection-observer-observe"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 节点查询 > IntersectionObserver.observe"
doc_id: "CZSYZwwors"
updated_at: "2023-08-11"
---

> Source: https://open.dingtalk.com/document/development/jsapi-intersection-observer-observe
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 节点查询 > IntersectionObserver.observe
> Updated: 2023-08-11

# IntersectionObserver.observe

调用IntersectionObserver.observe，指定目标节点并开始监听相交状态变化情况。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10037) |

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

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

参数占位区域

## **示例****代码**

### 默认出入参

```
const intersectionObserver = dd.IntersectionObserver();

intersectionObserver.observe('xxId', (res) => {
  const {
    time,
    relativeRect,
    intersectionRect,
    intersectionRatio,
    boundingClientRect,
  } = res;
});
```

`callback`返回对象示例：

```
{
  "time": 1677725294970,
  "relativeRect": { "top": 50, "left": 0, "right": 100, "bottom": 200 },
  "intersectionRect": { "top": 50, "left": 0, "right": 100, "bottom": 200 },
  "intersectionRatio": 0.5,
  "boundingClientRect": { "top": 50, "left": 0, "right": 100, "bottom": 200 }
}
```
