---
title: "外勤打卡通知"
source_url: "https://open.dingtalk.com/document/connection/field-clock-in-notification"
namespace: "connection"
slug: "field-clock-in-notification"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "考勤自动化 > 模板教学 > 外勤打卡通知"
doc_id: "953LLcUmoW"
updated_at: "2025-09-23 19:21:44"
---

> Source: https://open.dingtalk.com/document/connection/field-clock-in-notification
> Path: 连接平台 / 连接平台自动化 / 考勤自动化 > 模板教学 > 外勤打卡通知
> Updated: 2025-09-23 19:21:44

# 外勤打卡通知

## **场景介绍**

想要实时监控员工的外勤打卡情况？

想要将考勤数据实时同步给指定用户或群组？

考勤自动化来帮你解决！

## **预期效果**

当关注的考勤组员工或部门员工发生外勤打卡时，自动发送消息通知员工的直属主管或其他指定用户。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9583735071/p758050.png)

## **操作步骤**

1. 在流程模板中单击**外勤通知**模板。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9583735071/p758059.png)
2. 配置步骤1**员工打卡时**，选择**触发范围**：

   1. 选择需要关注的考勤组，只有该范围内考勤组的员工打卡时，才会触发通知流程。

      > **[!NOTE]**
      >
      > 只能选择你有管理权限的考勤组。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9583735071/p758060.png)
   2. 或者选择需要关注的部门/人员，只有这些部门/人员打卡时，才会触发通知流程。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9583735071/p758062.png)
3. 配置步骤2**发送消息到指定用户或群**：

   1. 根据需要选择发送对象。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9583735071/p758063.png)
   2. 根据需要，在**内容**中填写消息内容。单击右侧蓝色加号 “⊕”，可以引用前置步骤的输出数据，比如员工的身份信息、打卡信息。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9583735071/p758065.png)
4. 单击**保存并启用**，即配置完成。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9583735071/p758066.png)
