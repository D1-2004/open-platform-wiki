---
title: "应用场景"
source_url: "https://open.dingtalk.com/document/connection/application-scenarios"
namespace: "connection"
slug: "application-scenarios"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > OA审批 > 应用场景"
doc_id: "qHjLsWSIwv"
updated_at: "2026-01-22 20:38:39"
---

> Source: https://open.dingtalk.com/document/connection/application-scenarios
> Path: 连接平台 / 连接器中心 / 官方连接器 > OA审批 > 应用场景
> Updated: 2026-01-22 20:38:39

# 应用场景

## 场景介绍

借助钉钉连接平台，企业可以打通钉钉审批与钉钉其他官方场景、SaaS应用以及企业内部应用，目前钉钉连接平台包含共40+官方场景和SaaS应用。

> **[!NOTE]**
>
> OA审批场景的接入目前仅支持钉钉专业版，详情请参考[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)。

## 应用场景

### 场景一：表单加载外部数据源

- **场景痛点**

  企业内部往往存在多个IT系统，如ERP、CRM等，当员工在钉钉提交表单时，往往需要从外部系统加载数据，如提交订单时从CRM加载客户列表、从ERP加载价目表等。在使用系统集成之前，员工往往需要在系统间手动拷贝数据，这不光降低了办公效率，同时带来了业务数据不一致的风险。
- **解决方案**

  企业可以在表单上配置表单组件的数据映射规则，表单在加载时可以基于集成器的规则进行数据自动填充，这样既提高了表单输入效率，也降低了由于误输入导致的业务数据不一致的风险。

  ![表单自动填充](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1639771461/p380896.png)

### 场景二：表单提交时校验

- **场景痛点**

  当员工提交预算、订单类审批单时，往往需要在财务系统查询预算或者在供应链系统查询库存，在使用系统集成之前，管理员需要将第一个审批人设置成财务或者仓库管理员，这无疑给员工增加了负担，并降低了流程执行效率。
- **解决方案**

  企业可以配置表单提交时的数据校验规则，员工在提交表单时，集成器会连接外部系统进行预算、库存类校验，并可以定制化提示文案。

  ![表单提交校验](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1639771461/p380897.png)

### 场景三：表单数据同步到外部系统

- **场景痛点**

  当员工在钉钉完成审批后，有时需要将审批单同步到外部系统，比如在出库审批单通过以后在ERP系统生成出库单。在使用系统集成之前，企业有两种方式实现数据同步：

  - 通过开放接口接收审批数据回调，通过自定义开发将审批单数据转换成ERP表单数据。
  - 手动同步。

  其中开放接口方案开发成本较高，且审批单数据变更以后，相关代码需要同步变更。手动同步的方式效率较低，且存在人为失误的风险。
- **解决方案**

  企业可以在审批流添加集成器节点，并通过配置化方式自定义需要同步到外部系统的数据，当审批流执行到该节点时，可以按照映射规则向外部系统同步数据。

  ![数据同步](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1639771461/p380899.png)

### **场景四：OA审批接入子流程**

- **场景痛点**

  OA审批场景下不支持编排和表达式，无法对官方和三方连接器的返回结果进行改造，使得返回结果不是所需要的内容。如获取智能人事员工花名册中岗位职级信息，返回结果是["P7"]。

  ![OA审批场景接入集成流痛点 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576616661/p506067.png)
- **解决方案**

  在连接平台通过子流程方式，对官方或三方连接器的执行动作出参进行改造，OA审批场景下直接引用发布后的子流程。如获取智能人事员工花名册中岗位职级信息，返回结果是P7。

  ![OA审批场景接入集成流解决方案 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576616661/p506068.png)
