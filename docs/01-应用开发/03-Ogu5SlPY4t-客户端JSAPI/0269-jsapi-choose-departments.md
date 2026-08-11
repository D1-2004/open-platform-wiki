---
title: "chooseDepartments"
source_url: "https://open.dingtalk.com/document/development/jsapi-choose-departments"
namespace: "development"
slug: "jsapi-choose-departments"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "通讯录 > chooseDepartments"
doc_id: "TbUM4hl1mg"
updated_at: "2024-12-04"
---

> Source: https://open.dingtalk.com/document/development/jsapi-choose-departments
> Path: 应用开发 / 客户端JSAPI / 通讯录 > chooseDepartments
> Updated: 2024-12-04

# chooseDepartments

调用chooseDepartments，返回部门的信息，是以部门为纬度，不是以人为纬度。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10310) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10310) |

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
dd.chooseDepartments({
  appId: `appId示例值`,
  title: '标题',
  corpId: `corpId示例值`,
  multiple: true,
  limitTips: '选择数量不能超过20个',
  maxDepartments: 100,
  pickedDepartments: ['deptId0', 'deptId1'],
  disabledDepartments: ['deptId0', 'deptId1'],
  requiredDepartments: ['deptId0', 'deptId1'],
  success: (res) => {
    const { userCount, departments, departmentsCount } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "userCount": 5,
  "departments": [{ "id": "68094649x", "name": "人事部", "number": 10 }],
  "departmentsCount": 2
}
```
