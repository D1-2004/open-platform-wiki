---
title: "AI 藏头诗"
source_url: "https://open.dingtalk.com/document/connection/ai-tibetan-poems"
namespace: "connection"
slug: "ai-tibetan-poems"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "群聊自动化 > 模板教学 > AI 藏头诗"
doc_id: "yCE0jdFXb7"
updated_at: "2026-08-03 09:13:28"
---

> Source: https://open.dingtalk.com/document/connection/ai-tibetan-poems
> Path: 连接平台 / 连接平台自动化 / 群聊自动化 > 模板教学 > AI 藏头诗
> Updated: 2026-08-03 09:13:28

# AI 藏头诗

## **场景介绍**

在新人入群欢迎时，你是否觉得传统的欢迎方式有些单调？

- ❌ **千篇一律**：每次都是"欢迎 XXX 加入群聊"，缺乏新意和温度。
- ❌ **人工耗时**：需要手动编辑欢迎语，人多时容易遗漏或延迟。
- ❌ **互动感弱**：纯文字欢迎难以留下深刻印象，新人融入感不强。

AI 藏头诗自动化流程可以让每一次欢迎都独一无二！

## **预期效果**

当有新成员加入群聊时，自动化流程会自动完成以下工作：

- **实时触发**：检测到新人入群事件，自动获取新成员的姓名信息。
- **AI 创作**：调用 AI 能力，为新人的名字量身定制一首藏头诗，每句首字连起来正是新人的名字
- **即时发送**：将生成的藏头诗作为欢迎消息发送到群内，让新人在入群的第一时间感受到专属的仪式感

通过这一流程，你可以实现：

- ✅ **全自动处理，零人力投入**：无需人工干预，7×24 小时自动响应；
- ✅ **个性化体验**：每位新人都能收到独一无二的藏头诗欢迎；
- ✅ **文化温度**：用诗词传递团队文化，增强归属感和认同感
- ✅ **社交破冰**：独特的欢迎方式引发群内互动，帮助新人快速融入

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7030645871/p755044.png)

## **操作步骤**

1. 在**流程新建**Tab下，选择**新人入群**，然后选择模板**AI藏头诗**并点击**立即使用**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8069175871/p754865.png)
2. 设置**新人入群时**触发条件，该步骤无需配置。

   > **[!NOTE]**
   >
   > 该节点表示，每当有新人入群时，流程就会被触发。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8069175871/p754867.png)
3. 为**向 AI 提问**，你可以根据需要修改问题内容**，**如图所示。

   > **[!NOTE]**
   >
   > 模板内容表示，需要AI为人名写一首藏头诗，这个人名就是上一步「新人入群」的输出数据[入群成员名单]。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8069175871/p754869.png)
4. **发送消息到该群组**，你可以根据需要修改发送内容，如图所示。

   > **[!NOTE]**
   >
   > 模板内容表示，消息内容中包含了藏头诗内容，即**引用**了上一步**向AI提问时**的**返回内容。**

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8069175871/p754870.png)
5. 若需修改流程名称，可点击左上角编辑流程（图示中①），然后点击右上角**保存**（图示中②），最后点击**发布**（图示中③）即可。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8069175871/p754871.png)
