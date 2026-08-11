---
title: "从模板生成"
source_url: "https://open.dingtalk.com/document/aipass/generate-from-template"
namespace: "aipass"
slug: "generate-from-template"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 工作流 > 钉钉协作 > 消息通知 > 从模板生成"
doc_id: "sOJLQVEFTK"
updated_at: "2025-10-21 14:15:39"
---

> Source: https://open.dingtalk.com/document/aipass/generate-from-template
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 工作流 > 钉钉协作 > 消息通知 > 从模板生成
> Updated: 2025-10-21 14:15:39

# 从模板生成

如果你需要使用卡片-发送互动卡片的能力，请了解如何在[创建 AI 助理工作流](0037-create-an-ai-assistant-workflow-1.md)时添加执行动作，本文档将帮助你快速了解如何配置互动卡片。

卡片模板你可以选择固有模板，也可选择自定义卡片模板。

## **搭建自定义卡片**

1. 在 AI 助理工作流搭建页面，单击**选择执行动作**，选择**钉钉协作 > 消息通知 > AI 助理回卡片给当前用户。**
2. 选择**从模板生成，**并单击**下拉框 > 新增自定义模板，**进入卡片搭建平台。

   > 在卡片平台右上角确认组织，**请确保卡片平台登录组织和工作流登录的组织一致。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4753701471/p920950.png)
3. 单击**创建卡片**，进入卡片搭建页面。
4. 在卡片搭建页面下，拖拉拽左侧的组件，搭建卡片的布局和样式。详情参考[互动卡片搭建平台](../../06-互动卡片/02-MhNX42mFB1-卡片模板搭建器/0001-card-template-overview.md)内容。

   > 以宣传文案卡片为例，我选取了 文本、按钮 组件，搭建了标题、正文内容、按钮三个模块。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4753701471/p920953.png)
5. 如果你的卡片内容是动态变化的，你需要单击左侧变量栏，新增你所需的变量信息，此处设置的变量将自动同步到工作流中。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2588311471/p924033.png)
6. 以宣传卡片为为例，我选取了 文本、按钮 组件，搭建了标题、正文内容、按钮三个模块。并添加了三个变量：

   > 请尽量填写变量的描述（支持中文），方便你在工作流配置时区分不同变量的含义。

   | **变量** | **说明** |
   | --- | --- |
   | title | 变量类型是文本，对应卡片标题模块的文字内容。 |
   | content | 变量类型是文本，对应卡片正文内容模块的文字内容。 |
   | event1 | 变量类型是**动态事件**，对应卡片按钮模块中，**点击按钮后要触发的事件。**  image |
7. 为对应组件设置动态变量，在在**编辑模式**下，选择标题模块的组件，为标题的内容绑定刚刚创建的**title**变量。输入 $ 即可引用变量。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2588311471/p924035.png)
8. 你如果要查看测试数据，你可以单击**编辑 mock 数据**，添加对应变量的测试值。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2588311471/p924037.png)
9. 单击**预览模式**，即可查看卡片效果。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2588311471/p924038.png)
10. 创建完成后，单击**保存**，即可在工作流中使用和配置自定义卡片。

    > **[!NOTE]**
    >
    > 如果单击发布后，自定义卡片将无法再次编辑，请谨慎操作。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2588311471/p924039.png)
11. 返回 AI 助理工作流搭建页面，选择搭建完成的自定义卡片。

    > 如果卡片列表没有实时拉取出来，请重新切换该节点后再重试，可删除该节点重新加入该执行动作。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4753701471/p920959.png)
12. 在工作流中配置变量内容，这些变量就是刚刚在卡片搭建工具中定义的动态变量。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4753701471/p920964.png)

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2588311471/p924041.png)

    至此，自定义卡片就已经搭建完成了。
