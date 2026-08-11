---
title: "技术支持"
source_url: "https://open.dingtalk.com/document/services/ngliko"
namespace: "services"
slug: "ngliko"
group: "应用开发"
tab: "平台服务"
breadcrumb: "服务支持 > 技术支持"
doc_id: "aybLtjzeIy"
updated_at: "2026-06-10 18:31:00"
---

> Source: https://open.dingtalk.com/document/services/ngliko
> Path: 应用开发 / 平台服务 / 服务支持 > 技术支持
> Updated: 2026-06-10 18:31:00

# 技术支持

本文档旨在指导开发者如何获取钉钉开放平台的技术支持。请按照以下流程准备信息、提交问题，并与技术支持人员高效沟通，以加快问题解决速度。

> **[!IMPORTANT]**
>
> 为更好地服务客户，自 2026 年 6 月 5 日起，原开发者后台工单系统将由技术支持团队统一通过以下渠道提供服务。

## **提交前准备**

在提交工单前，建议您优先使用自助工具进行问题排查和接口调试，部分常见问题可通过以下方式快速定位：

- [服务端API调试工具](../06-JDICnQyZLF-开发工具/0005-api-explorer.md)：用于调用和测试服务端API，查看实际返回结果。
- [小程序开发工具](../06-JDICnQyZLF-开发工具/0001-miniapp-tool.md)：适用于钉钉小程序的本地开发与调试。
- [微应用调试工具—RC版](../06-JDICnQyZLF-开发工具/0007-h5-debug.md)：帮助调试H5微应用在钉钉环境中的运行情况。

若通过上述工具仍无法解决问题，请继续完成以下准备工作：

- 明确您的问题分类和归属，以便技术支持人员判断权限模型和调用上下文。
- 获取企业的 **CorpId**（企业唯一标识，可在开发者后台页面查看），用于定位调用来源。
- 若涉及接口调用问题，请记录请求的完整信息，包括接口URL、参数、返回结果及 **requestID**（请求唯一标识，用于日志追踪）。

## 获取支持

为提供更好的服务质量，减少等待时间，建议先通过自助工具解决。如果未解决问题，可以通过以下步骤进行咨询。

### **AI 客服自助答疑**

1. 打开钉钉客户端，点击头像并选择[**客服与帮助**](dingtalk://dingtalkclient/page/singleconversation?uid=5639198466)。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4090790871/p1080232.png)
2. 在新的钉钉客服聊天中，可通过以下三种方式获取相关服务：

   1. **方式一**：直接在对话框中输入相关问题进行咨询。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3090790871/p1080234.png)
   2. **方式二**：在对话框中输入`人工客服`，发送成功后，钉钉客服会在服务时间内为您服务。

      > **[!NOTE]**
      >
      > 人工客服服务时间为工作日8:00~18:00，请在该时间段内获取在线人工帮助。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3090790871/p1080235.png)
   3. **方式三**：点击右上角**热线咨询**按钮，提交需要咨询的内容，客服会根据预约时间为您服务。

      > **[!NOTE]**
      >
      > 客服服务时间为工作日9:00~18:00，请在该时间段内进行预约。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3090790871/p1080236.png)

### **提交需求 / BUG**

> **[!NOTE]**
>
> 若有需求或产品bug，可通过本方式提交产品需求或VOC。

1. 点击[提交VOC](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fwww.aliwork.com%2Fo%2F085A77422A63404EBDC4B363E10CE15D52OG%3FisRenderNav%3Dfalse&pc_slide=true&title=%E9%9C%80%E6%B1%82%E6%8F%90%E4%BA%A4)（客户自行提交）链接。
2. 在需求提交的界面，点击**提交建议**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0647801871/p1080572.png)
3. 在表单界面填写您的问题，最后单击**提交**按钮即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0647801871/p1080573.png)
4. 提交成功后，可再次点击[提交VOC](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fwww.aliwork.com%2Fo%2F085A77422A63404EBDC4B363E10CE15D52OG%3FisRenderNav%3Dfalse&pc_slide=true&title=%E9%9C%80%E6%B1%82%E6%8F%90%E4%BA%A4)链接，点击**查看进度**后，可查看提交需求后的处理进展。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0647801871/p1080574.png)

## 注意事项

**为便于快速定位排查问题，建议你在反馈时提供以下开发信息，包括但不限于：**

- 你开发的应用类型或场景

  - 企业内部应用
  - 第三方企业应用
  - 第三方个人应用
  - 工作台开发
  - 群开放等
- 问题的详细描述及相关问题截图
- 公司名称、CorpId
- 服务端接口调用问题，请提供以下内容：

  - 请求的接口URL
  - 参数信息
  - 实际返回结果
  - 期望返回结果
- 前端接口调用问题，请提供以下内容：

  - 手机机型
  - 手机系统
  - 使用钉钉版本
  - 调用的接口参数
  - 实际返回结果
  - 期望返回结果

感谢您提供的宝贵信息！我们将竭诚为您提供高效、专业的技术支持服务。
