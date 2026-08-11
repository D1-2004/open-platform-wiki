---
title: "complexChoose"
source_url: "https://open.dingtalk.com/document/development/jsapi-complex-choose"
namespace: "development"
slug: "jsapi-complex-choose"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "通讯录 > complexChoose"
doc_id: "CucGIH88i7"
updated_at: "2025-06-12"
---

> Source: https://open.dingtalk.com/document/development/jsapi-complex-choose
> Path: 应用开发 / 客户端JSAPI / 通讯录 > complexChoose
> Updated: 2025-06-12

# complexChoose

调用complexChoose，选择人和部门。

![](https://gw.alicdn.com/imgextra/i1/O1CN01kfcX9r24hmoE66zrS_!!6000000007423-0-tps-536-1020.jpg)

支持选择企业关联的上下游组织

![](https://gw.alicdn.com/imgextra/i2/O1CN01POFp0q1yNjmI18vRD_!!6000000006567-0-tps-1164-1032.jpg)

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10309) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10309) |

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
dd.complexChoose({
  appId: '013324',
  title: '选择员工',
  corpId: 'ding1234xxxxx',
  deptId: '0987',
  maxUsers: 100,
  multiple: true,
  rootPage: `rootPage示例值`,
  limitTips: '选择人数不能超过20个',
  pickedUsers: ['userId0', 'userId2'],
  disabledUsers: ['userId0', 'userId2'],
  requiredUsers: ['userId0', 'userId2'],
  showLabelPick: true,
  responseUserOnly: true,
  pickedDepartments: ['deptId0', 'deptId1'],
  showOrgEcological: false,
  disabledDepartments: ['deptId0', 'deptId1'],
  filterOrgEcological: false,
  requiredDepartments: ['deptId0', 'deptId1'],
  startWithDepartmentId: '0332',
  success: (res) => {
    const { users, departments, selectedCount } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "users": [
    {
      "name": "钉小二",
      "avatar": "https://static.dingtalk.com/media/lADPDiCpu12oVqvNApTNApQ_660_660.jpg",
      "emplId": "22055215283702319x"
    }
  ],
  "departments": [{ "id": "68094649x", "name": "人事部", "number": 10 }],
  "selectedCount": 4
}
```
