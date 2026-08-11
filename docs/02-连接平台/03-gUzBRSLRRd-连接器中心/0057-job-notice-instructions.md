---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/job-notice-instructions"
namespace: "connection"
slug: "job-notice-instructions"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 工作通知 > 参数说明"
doc_id: "sKGz4SRX0b"
updated_at: "2025-09-23 19:21:16"
---

> Source: https://open.dingtalk.com/document/connection/job-notice-instructions
> Path: 连接平台 / 连接器中心 / 官方连接器 > 工作通知 > 参数说明
> Updated: 2025-09-23 19:21:16

# 参数说明

## **发送工作通知[文本消息]**

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| agentId | Number | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| content | String | 是 | 需要发送的文本消息。 |
| toAllUser | Boolean | 否 | 是否@所有人：   - **true**：@所有人 - **false**：不@所有人   **[!NOTE]**  默认为false，当设置为false时必须指定「接收者的部门Id列表」或者「接收者的用户Id列表」中一个参数值。 |
| deptIdList | Array  <Number> | 否 | 输入[部门Id（deptId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#18304350ffsh5)，发送消息给部门下的所有员工。 |
| useridList | Array  <String> | 否 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，发送消息给对应的员工。 |

## 发送工作通知[图片消息]

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| agentId | Number | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| mediaId | String | 是 | 可以通过调用[上传媒体文件](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)接口获取mediaId参数值。 |
| toAllUser | Boolean | 否 | 是否@所有人：   - **true**：@所有人 - **false**：不@所有人   **[!NOTE]**  默认为false，当设置为false时必须指定「接收者的部门Id列表」或者「接收者的用户Id列表」中一个参数值。 |
| deptIdList | Array  <Number> | 否 | 输入[部门Id（deptId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#18304350ffsh5)，发送消息给部门下的所有员工。 |
| useridList | Array  <String> | 否 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，发送消息给对应的员工。 |

## 发送工作通知[markdown消息]

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| agentId | Number | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| text | String | 是 | markdown格式的消息。 |
| title | String | 是 | 首屏会话透出的展示内容，在没有进入消息详情时看到的消息内容。 |
| toAllUser | Boolean | 否 | 是否@所有人：   - **true**：@所有人 - **false**：不@所有人   **[!NOTE]**  默认为false，当设置为false时必须指定「接收者的部门Id列表」或者「接收者的用户Id列表」中一个参数值。 |
| deptIdList | Array  <Number> | 否 | 输入[部门Id（deptId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#18304350ffsh5)，发送消息给部门下的所有员工。 |
| useridList | Array  <String> | 否 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，发送消息给对应的员工。 |

## **发送工作通知[整体跳转卡片消息]**

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| agentId | Number | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| toAllUser | Boolean | 否 | 是否@所有人：   - **true**：@所有人 - **false**：不@所有人   **[!NOTE]**  默认为false，当设置为false时必须指定「接收者的部门Id列表」或者「接收者的用户Id列表」中一个参数值。 |
| deptIdList | Array  <Number> | 否 | 输入[部门Id（deptId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#18304350ffsh5)，发送消息给部门下的所有员工。 |
| useridList | Array  <String> | 否 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，发送消息给对应的员工。 |
| btnTitle | String | 是 | 消息底部按钮的标题。 |
| btnUrl | String | 是 | 按钮触发跳转url。  **[!NOTE]**  消息底部按钮触发跳转url，需要以http://或者https://开头，内容以半屏的方式打开。 |
| text | String | 是 | markdown格式的消息。 |
| title | String | 是 | 首屏会话透出的展示内容，在没有进入消息详情时看到的消息内容。 |

## **发送工作通知[横排多按钮ActionCard消息]**

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| agentId | Number | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| toAllUser | Boolean | 否 | 是否@所有人：   - true：@所有人 - false：不@所有人   **[!NOTE]**  默认为false，当设置为false时必须指定「接收者的部门Id列表」或者「接收者的用户Id列表」中一个参数值。 |
| deptIdList | Array  <Number> | 否 | 输入[部门Id（deptId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#18304350ffsh5)，发送消息给部门下的所有员工。 |
| useridList | Array  <String> | 否 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，发送消息给对应的员工。 |
| btns | Array  <Object> | 否 | 横排多个按钮信息。 |
| title | String | 是 | 按钮的标题。 |
| actionUrl | String | 是 | 按钮触发跳转url。  **[!NOTE]**  需要以http://或者https://开头，内容以半屏的方式打开。 |
| text | String | 是 | markdown格式的消息。 |
| title | String | 是 | 首屏会话透出的展示内容，在没有进入消息详情时看到的消息内容。 |

## 发送工作通知[竖排多按钮ActionCard消息]

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| agentId | Number | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| toAllUser | Boolean | 否 | 是否@所有人：   - true：@所有人 - false：不@所有人   **[!NOTE]**  默认为false，当设置为false时必须指定「接收者的部门Id列表」或者「接收者的用户Id列表」中一个参数值。 |
| deptIdList | Array  <Number> | 否 | 输入[部门Id（deptId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#18304350ffsh5)，发送消息给部门下的所有员工。 |
| useridList | Array  <String> | 否 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，发送消息给对应的员工。 |
| btns | Array  <Object> | 否 | 竖排多个按钮信息。 |
| title | String | 是 | 按钮的标题。 |
| actionUrl | String | 是 | 按钮触发跳转url。  **[!NOTE]**  需要以http://或者https://开头，内容以半屏的方式打开。 |
| text | String | 是 | markdown格式的消息。 |
| title | String | 是 | 首屏会话透出的展示内容，在没有进入消息详情时看到的消息内容。 |

## 发送工作通知[OA消息]

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| agentId | Number | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| toAllUser | Boolean | 否 | 是否@所有人：   - true：@所有人 - false：不@所有人   **[!NOTE]**  默认为false，当设置为false时必须指定「接收者的部门Id列表」或者「接收者的用户Id列表」中一个参数值。 |
| deptIdList | Array  <Number> | 否 | 输入[部门Id（deptId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#18304350ffsh5)，发送消息给部门下的所有员工。 |
| useridList | Array  <String> | 否 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，发送消息给对应的员工。 |
| messageUrl | String | 是 | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接。链接格式参考[消息链接说明](../../01-应用开发/02-4a8AMF6u2A-服务端API/0774-message-link-description.md)。 |
| pcMessageUrl | String | 是 | PC端点击消息时跳转到的地址。  **[!NOTE]**  以http://或https://开头。 |
| statusBar | String | 否 | 消息状态栏。  **[!NOTE]**  只支持接收者的userid列表，userid最多不能超过5个人。不支持部门id列表，并且to\_all\_user不能传true。 |
| statusValue | String | 是 | 状态栏文案，例如：进行中。 |
| statusBg | String | 是 | 状态栏背景色，默认为黑色，推荐0xFF加六位颜色值。例如：0xFFF65E5E。 |
| head | Object | 是 | 消息头部内容，消息的头部标题为当前应用名称。 |
| bgcolor | String | 是 | 长度限制为8个英文字符，其中前2为表示透明度，后6位表示颜色值。不要添加0x。 |
| body | Object | 是 | OA消息体。 |
| image | String | 否 | 消息体中的图片，支持图片资源@mediaId。建议宽600像素 x 400像素，宽高比3 : 2。 |
| author | String | 否 | 自定义的作者名字，例如：李四。 |
| title | String | 否 | 消息体的标题，建议50个字符以内。 |
| fileCount | String | 否 | 此数字仅供显示，钉钉不作验证，例如3。 |
| content | String | 否 | 消息体的内容，最多显示3行。 |
| rich | Object | 否 | 单行富文本信息。 |
| unit | String | 否 | 单行富文本信息的单位，例如：元。 |
| num | String | 否 | 单行富文本信息的数目，例如：15.6。 |
| form | Array  <Object> | 否 | 消息体的表单，最多显示6个，超过会被隐藏。 |
| key | String | 否 | 消息体的关键字，例如：姓名。 |
| value | String | 否 | 消息体的关键字对应的值，例如：张三。 |

## 发送工作通知[链接消息]

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| agentId | Number | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| toAllUser | Boolean | 否 | 是否@所有人：   - true：@所有人 - false：不@所有人   **[!NOTE]**  默认为false，当设置为false时必须指定「接收者的部门Id列表」或者「接收者的用户Id列表」中一个参数值。 |
| deptIdList | Array  <Number> | 否 | 输入[部门Id（deptId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#18304350ffsh5)，发送消息给部门下的所有员工。 |
| useridList | Array  <String> | 否 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，发送消息给对应的员工。 |
| picUrl | String | 是 | 图片地址，mediaId格式，可以通过调用[上传媒体文件](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)接口获取mediaId参数值。 |
| messageUrl | String | 是 | 消息点击链接地址。  **[!NOTE]**  以http://或https://开头。 |
| text | String | 是 | 消息描述，建议500字符以内。 |
| title | String | 是 | 整个链接消息头部标题。 |

## 发送工作通知[文件消息]

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| agentId | Number | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| toAllUser | Boolean | 否 | 是否@所有人：   - true：@所有人 - false：不@所有人   **[!NOTE]**  默认为false，当设置为false时必须指定「接收者的部门Id列表」或者「接收者的用户Id列表」中一个参数值。 |
| deptIdList | Array  <Number> | 否 | 输入[部门Id（deptId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#18304350ffsh5)，发送消息给部门下的所有员工。 |
| useridList | Array  <String> | 否 | 输入[用户ID（userId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#17072210ff2rq)，发送消息给对应的员工。 |
|  |  |  |  |
| mediaId  图片地址 | String | 是 | 文件地址，mediaId格式，可以通过调用[上传媒体文件](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md)接口获取mediaId参数值。 |

## **撤回工作通知消息**

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| agentId | Number | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| taskId | Number | 是 | 发送消息时钉钉返回的任务id。  **[!NOTE]**  仅支持撤回24小时内发送的工作通知消息。 |

## **获取工作通知消息的发送结果**

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| agentId | Number | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| taskId | Number | 是 | 发送消息时钉钉返回的任务id。  **[!NOTE]**  仅支持查询24小时内工作通知消息的发送结果。 |

## **获取工作通知消息的发送进度**

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| agentId | Number | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| taskId | Number | 是 | 发送消息时钉钉返回的任务id。  **[!NOTE]**  仅支持查询24小时内工作通知消息的发送进度。 |

## **更新工作通知状态栏**

> **[!NOTE]**
>
> 仅针对更新OA消息状态栏。

| **入参** | **类型** | **必填** | **详细说明** |
| --- | --- | --- | --- |
| agentId | Number | 是 | 微应用在企业的[应用Id（agentId）](../02-iO2mVD3wB2-开发指南/0018-official-connector-generic-field-acquisition-1.md#7c21daa0ffp70)。 |
| statusValue | String | 是 | 状态栏值。 |
| statusBg | String | 否 | 状态栏背景色。  **[!NOTE]**  推荐0xFF加六位颜色值。 |
| taskId | Number | 是 | 发送消息时钉钉返回的任务id。  **[!NOTE]**  仅支持更新24小时内发出的OA工作通知状态栏。 |
