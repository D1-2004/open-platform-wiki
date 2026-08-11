---
title: "getCloudCallList"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-cloud-call-list"
namespace: "development"
slug: "jsapi-get-cloud-call-list"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "办公电话 > getCloudCallList"
doc_id: "SeI0Ii5w6W"
updated_at: "2023-08-22"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-cloud-call-list
> Path: 应用开发 / 客户端JSAPI / 办公电话 > getCloudCallList
> Updated: 2023-08-22

# getCloudCallList

调用getCloudCallList，查询话单列表。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 6.0.9 | 6.0.9 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11648) |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.9 | 6.0.9 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11648) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

参数占位区域

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

参数占位区域

## **示例****代码**

### 默认出入参

```
dd.getCloudCallList({
  index: 0,
  corpId: 'ding1234',
  endTime: '2022-02-01 00:00:00',
  pageSize: 100,
  bizNumber: '711xxxxx',
  direction: 1,
  sessionId: '798xxxxx',
  startTime: '2022-01-01 00:00:00',
  staffIdList: ['userId1', 'userId2'],
  success: (res) => {
    const { code, cause, total, hasMore, callList, currentIndex } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "code": 200,
  "cause": "内部异常",
  "total": 10,
  "hasMore": true,
  "callList": ["711xxxxx", "711xxxxx"],
  "currentIndex": 2
}
```
