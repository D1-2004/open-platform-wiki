---
title: "邮件参数说明"
source_url: "https://open.dingtalk.com/document/connection/message-parameter-description"
namespace: "connection"
slug: "message-parameter-description"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 邮箱 > 邮件参数说明"
doc_id: "oGm8XXLuDx"
updated_at: "2025-09-23 19:20:48"
---

> Source: https://open.dingtalk.com/document/connection/message-parameter-description
> Path: 连接平台 / 连接器中心 / 官方连接器 > 邮箱 > 邮件参数说明
> Updated: 2025-09-23 19:20:48

# 邮件参数说明

## **鉴权凭证**

邮箱连接器使用前需要先添加凭证，即发送邮件的邮箱账号与授权码，注意此处的授权码不一定是邮箱密码，相关字段的获取方式点击链接查看详情。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2052576371/p903409.png)

## **发送邮件**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| 收件人 | Array(String) | 是 | 邮件接受人的邮箱地址（xxxxxx@xxx.xxx） |
| 标题 | String | 是 | 邮件标题 |
| 邮件正文 | String | 是 | 邮件正文内容 |
| 邮件正文类型 | String | 是 | 邮件正文类型  纯文本：邮件中所有内容以文本格式展示  HTML：邮件中若有url地址以链接方式展示 |
| 正文字符编码 | String | 是 | 目前只支持 UTF-8 |
| 附件列表 | Array(Object) |  |  |
| 附件名称 |  | 是 | 附件 |
| 附件网络地址 |  | 是 | 附件url地址需要公网能访问，部分url存在防爬等问题，需另做处理 |
| 附件类型 |  | 是 | 下拉选择支持的附件类型 |
| 附件头部 |  |  | JSON Key-Value结构 |

## **参数举例**

以 QQ 邮件为例，发送一封邮件到指定邮箱

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2052576371/p903510.png)

对应邮箱收到来自用户鉴权中配置的 QQ 邮箱的一封邮件

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2052576371/p903514.png)
