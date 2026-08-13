---
title: "外勤打卡通知"
source_url: "https://open.dingtalk.com/document/connection/field-clock-in-notification"
namespace: "connection"
slug: "field-clock-in-notification"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "考勤自动化 > 模板教学 > 外勤打卡通知"
doc_id: "953LLcUmoW"
updated_at: "2026-08-03 09:13:33"
---

> Source: https://open.dingtalk.com/document/connection/field-clock-in-notification
> Path: 连接平台 / 连接平台自动化 / 考勤自动化 > 模板教学 > 外勤打卡通知
> Updated: 2026-08-03 09:13:33

# 外勤打卡通知

## **场景介绍**

在团队管理中，你是否经常遇到以下困扰：

- ❌ **外勤难追踪**：员工外出拜访客户、现场施工等场景下，无法实时确认是否按时到达指定地点。
- ❌ **信息滞后**：主管需要手动查看考勤报表或逐个询问，才能知道谁完成了外勤打卡。
- ❌ **管理盲区**：外勤人员分散在不同地点，传统坐班式考勤规则不适用，缺乏有效的过程监督手段。

考勤自动化流程可以让"外勤动态实时可见"成为现实！

## **预期效果**

当关注的考勤组员工或部门员工发生外勤打卡时，自动化流程会自动完成以下工作：

- **事件捕获**：系统检测到指定范围内的员工完成外勤打卡（含打卡时间、地点、备注等信息）。
- **精准推送**：自动向该员工的直属主管或其他指定用户发送通知消息。
- **信息透明**：消息中可引用员工身份信息、打卡位置、打卡时间等关键字段，让管理者一目了然。

通过这一流程，你可以实现：

- ✅ **全自动处理，零人力投入**：无需人工轮询考勤报表。
- ✅ **实时感知**：外勤打卡秒级触达主管，告别信息延迟。
- ✅ **精准触达**：支持按考勤组/部门/人员维度配置触发范围，避免无关打扰。
- ✅ **灵活定制**：消息内容可自由编辑，支持引用前置步骤的输出数据。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3169175871/p758040.png)

## **操作步骤**

1. 在**流程新建**Tab下，选择**打卡通知**，然后选择**外勤通知**模板并点击**立即使用**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3169175871/p758059.png)
2. 配置**员工打卡时**触发条件，选择**触发范围**、考勤组和打开类型。

   > **[!NOTE]**
   >
   > - 只能选择你有管理权限的考勤组。
   > - 考勤组只有该范围内考勤组的员工打卡时，才触发通知流程。
   > - 若触发范围选择指定部门/人员时，只有部门/人员打卡时，才触发通知流程。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3169175871/p758060.png)
3. 配置**发送消息到指定用户或群**指定执行动作，如下图所示：

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3169175871/p758063.png)
4. 若需修改流程名称，可点击左上角编辑流程（图示中①），然后点击右上角**保存**（图示中②），最后点击**发布**（图示中③）即可。![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3169175871/p758066.png)
