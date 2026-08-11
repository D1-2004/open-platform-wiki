---
title: "datePicker"
source_url: "https://open.dingtalk.com/document/development/jsapi-date-picker"
namespace: "development"
slug: "jsapi-date-picker"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 选择日期 > datePicker"
doc_id: "VDaxXACBCk"
updated_at: "2023-08-08"
---

> Source: https://open.dingtalk.com/document/development/jsapi-date-picker
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 选择日期 > datePicker
> Updated: 2023-08-08

# datePicker

调用dd.datePicker打开日期选择列表。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10077) |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10077) |

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
dd.datePicker({
  format: 'yyyy-MM-dd',
  currentDate: '2012-12-12',
  success: (res) => {
    const { date } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "date": "2012-12-12" }
```
