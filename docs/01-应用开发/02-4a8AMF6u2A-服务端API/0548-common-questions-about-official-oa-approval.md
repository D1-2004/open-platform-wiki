---
title: "官方OA审批"
source_url: "https://open.dingtalk.com/document/development/common-questions-about-official-oa-approval"
namespace: "development"
slug: "common-questions-about-official-oa-approval"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 常见问题 > 官方OA审批"
doc_id: "rrjHdUvwHr"
updated_at: "2025-12-05 15:34:51"
---

> Source: https://open.dingtalk.com/document/development/common-questions-about-official-oa-approval
> Path: 应用开发 / 服务端API / OA 审批 > 常见问题 > 官方OA审批
> Updated: 2025-12-05 15:34:51

# 官方OA审批

调用钉钉服务端官方OA审批接口时出现的常见错误。

## 调用第三方企业应用获取表单schema报错“code: 500，未知错误”

答：调用[获取表单 schema](0488-obtain-the-form-schema.md)接口报错“code: 500, 未知错误”，可能为权限问题：可以获取的表单是经过用户授权的，获取不到的表单没有经过用户授权的。授权获取审批实例数据文档参见[唤起授权弹窗](../03-Ogu5SlPY4t-客户端JSAPI/0008-jsapi-request-auth-info.md)。

## 如何在审批中添加附件

答：审批附件的实现需要配合服务端API和前端API实现，详细流程可参考[审批附件的操作流程](0483-new-version-of-attachment-approval-process.md)使用案例。

> **[!NOTE]**
>
> 目前尚未支持通过调用服务端API添加审批附件。

1. 调用[获取审批钉盘空间信息](0498-obtains-the-information-about-approval-nail-disk.md)接口，得到审批附件专属钉盘空间spaceId。
2. 调用，从本地选择资源上传到审批附件钉盘获取spaceId、fileId、fileName、fileSize和fileType参数。
3. 使用步骤2得到的参数，传递给发起审批接口中的附件组件。

## 如何获取审批中的附件

答：审批附件的实现需要配合服务端API和前端API实现，详细流程可参考[审批附件的操作流程](0483-new-version-of-attachment-approval-process.md)使使用案例。

1. 调用[授权预览审批附件](https://open.dingtalk.com/document/development/preview-authorization-attachment-pop)接口。注意此接口会进行授权，只有传递的userid对应的用户才可以成功预览附件。
2. 使用参数space\_id，调用[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端JSAPI/0333-jsapi-upload-attachment-to-ding-talk.md)，获取钉盘附件的信息。

## 审批接口调用失败

答：当调用审批接口出错时，请参考以下信息进行排查：

1. 在OA后台的审批应用中构造审批模板时，选择的组件类型必须是[发起审批实例](0493-create-an-approval-instance.md)中列举的类型，否则发起审批接口会报错。
2. 构造的审批模板中明细组件内只支持输入框类型和图片组件类型，其他组件类型暂不支持。
3. 构造的审批模板中最多支持20个组件。

## 调用发起OA审批实例的明细组件内可传入的控件格式有哪些？

答：调用[发起审批实例](0493-create-an-approval-instance.md)接口中明细组件内可传入的控件格式有:单行输入框、多行输入框、数字输入框、图片控件。
