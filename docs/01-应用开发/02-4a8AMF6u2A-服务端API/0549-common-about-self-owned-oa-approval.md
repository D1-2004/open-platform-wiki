---
title: "自有OA审批"
source_url: "https://open.dingtalk.com/document/development/common-about-self-owned-oa-approval"
namespace: "development"
slug: "common-about-self-owned-oa-approval"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 常见问题 > 自有OA审批"
doc_id: "2egGbTG0ff"
updated_at: "2025-12-05 15:42:04"
---

> Source: https://open.dingtalk.com/document/development/common-about-self-owned-oa-approval
> Path: 应用开发 / 服务端API / OA 审批 > 常见问题 > 自有OA审批
> Updated: 2025-12-05 15:42:04

# 自有OA审批

调用钉钉服务端自有OA审批接口时的常见错误。

## errcode=15（创建或更新模板接口）

- **问题描述**

  调用【创建或者更新模板】接口，出现如下错误。

  ```
  {
     " errcode":15,
     " sub_msg":"服务不可用",
     " sub_code":isp.-1,
     " errmsg":"Remote service error"[
        subcode=isp.-1,
        "submsg=服务不可用"
     ]
  }
  ```
- **原因**

  componentName参数不能自定义，要传文档给的几个固定值。
- **解决方案**

  修改componentName参数值，请参考[创建或更新审批模板](https://open.dingtalk.com/document/development/create-or-update-approval-templates-new)。

## errcode=810002（创建或更新模板接口）

- **问题描述**

  调用【创建或者更新模板】接口，出现如下错误。

  ```
  {
     "errcode":810002,
     "errmsg":"复制的审批流已超过最大数量",
     "request_id":"xsr5qth2j075"
  }
  ```
- **原因**

  已达到创建模板上限200个。
- **解决方案**

  可删除不需要的模板再重试。

## errcode=810007 无操作审批流的权限（创建实例接口）

- **问题描述**

  调用【创建实例接口process/workrecord/create】接口，出现如下错误。

  ```
  无操作审批流的权限，请检查审批实例或者模版是否正确
  ```

  ```
  {
      "errcode": 810007,
      "errmsg": "没有操作审批流的权限",
      "request_id": "xxx"
  }
  ```
- **原因**

  processCode参数不正确。
- **解决方案**

  processCode必须使用[创建或更新审批模板](https://open.dingtalk.com/document/development/create-or-update-approval-templates-new)接口返回的processCode，并且参数**fake\_mode**必须传**true**。

## errcode=810007 无操作审批流的权限（更新实例接口）

- **问题描述**

  调用【更新实例接口process/workrecord/update】接口，出现如下错误。

  ```
  无操作审批流的权限，请检查审批实例或者模版是否正确
  ```

  ```
  {
      "errcode": 810007,
      "errmsg": "没有操作审批流的权限",
      "request_id": "xxx"
  }
  ```
- **原因**

  实例ID（process\_instance\_id）参数不正确。
- **解决方案**

  实例ID（process\_instance\_id）必须是[创建实例](0509-create-a-ticket-approval-instance.md)接口返回的process\_instance\_id值，不能使用官方审批流的实例值。

## errorcode=820008（更新实例接口）

- **问题描述**

  调用【更新实例接口process/workrecord/update】接口，出现如下错误。

  ```
  {
     "errcode":810002,
     "errmsg":"审批系统错误，原因为【审批表单已被管理员修改】",
     "request_id":"6pz3le495848"
  }
  ```
- **原因**

  没有传result参数。
- **解决方案**

  更新审批单实例时，请传入result值后，再尝试。

## errorcode=820008（创建待办接口）

- **问题描述**

  调用【创建待办process/workrecord/task/create】接口，出现如下错误。

  ```
  {
     "errcode":810002,
     "errmsg":"审批系统错误，原因为【引擎已知错误:{0}",
     "request_id":"6pz3le495848"
  }
  ```
- **原因**

  参数URL字符过长。
- **解决方案**

  请修改URL参数，再尝试。

## errorcode=820010（创建待办接口）

- **问题描述**

  调用【创建待办process/workrecord/task/create】接口，出现如下错误。

  ```
  {
     "errcode":820010,
     "request_id":"6pz3le495848"
  }
  ```
- **原因**

  实例下的待办任务超过限制。
- **解决方案**

  一个实例下，最多只能创建100个待办，请删除不需要的待办任务重试或新建实例。

## 自有OA审批接口提示“无操作审批流权限”

此问题是由于将“使用官方OA审批”和“使用自有OA审批”两种场景混用导致的。

1. 调用自有OA审批创建实例接口，参数process\_code必须来自[创建或更新审批模板](https://open.dingtalk.com/document/development/create-or-update-approval-templates-new)接口，不能使用从审批后台地址栏中截取的process\_code。
2. 调用自有OA审批的更新实例状态接口，参数process\_instance\_id必须来自[创建实例](0509-create-a-ticket-approval-instance.md)接口，不能传入官方审批流中发起审批实例接口得到的process\_instance\_id。
