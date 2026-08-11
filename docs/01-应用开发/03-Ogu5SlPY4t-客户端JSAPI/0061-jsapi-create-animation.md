---
title: "createAnimation"
source_url: "https://open.dingtalk.com/document/development/jsapi-create-animation"
namespace: "development"
slug: "jsapi-create-animation"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 动画 > createAnimation"
doc_id: "AQjXHqfkcz"
updated_at: "2023-08-08"
---

> Source: https://open.dingtalk.com/document/development/jsapi-create-animation
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 动画 > createAnimation
> Updated: 2023-08-08

# createAnimation

调用createAnimation，创建动画实例。调用实例的方法来描述动画，最后通过动画实例的export方法将动画数据导出并传递给组件的animation属性。

### 动画实例方法

动画实例可以调用以下方法来描述动画，调用结束后会返回实例本身，支持链式调用的写法。

#### 样式

| 方法 | 参数 | 说明 |
| --- | --- | --- |
| opacity | value | 透明度，参数范围 0~1。 |
| backgroundColor | color | 颜色值。 |
| width | length | 长度值，如果传入数字则默认单位为 px ，可传入其他自定义单位的长度值。 |
| height | length | 同上。 |
| top | length | 同上。 |
| left | length | 同上。 |
| bottom | length | 同上。 |
| right | length | 同上。 |

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10079) |

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
dd.createAnimation({
  delay: 69,
  duration: 87,
  timeFunction: `timeFunction示例值`,
  transformOrigin: `transformOrigin示例值`,
});
```
