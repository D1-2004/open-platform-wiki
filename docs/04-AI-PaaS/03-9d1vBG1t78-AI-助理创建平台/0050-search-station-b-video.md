---
title: "搜索B站视频"
source_url: "https://open.dingtalk.com/document/aipass/search-station-b-video"
namespace: "aipass"
slug: "search-station-b-video"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 工作流 > 执行动作 > 咨询搜索 > 搜索B站视频"
doc_id: "C9kkzcy9Cb"
updated_at: "2025-09-23 19:20:01"
---

> Source: https://open.dingtalk.com/document/aipass/search-station-b-video
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 工作流 > 执行动作 > 咨询搜索 > 搜索B站视频
> Updated: 2025-09-23 19:20:01

# 搜索B站视频

如果你需要使用搜索B站视频的执行动作，请了解如何在[创建 AI 助理工作流](0037-create-an-ai-assistant-workflow-1.md)时添加执行动作。

**适用人群**：**所有人** ；**适用范围**：**组织内创建的 AI 助理/助理市场创建的 AI 助理**

## **操作步骤**

1. 单击**选择执行动作**，选择**资讯搜索** > **搜索B站视频**。

   1. 配置内容：

      | **配置项** | **说明** |
      | --- | --- |
      | 关键词 | 输入想要搜索的关键词，比如视频名称、UP主名称等。 |
      | 排序方式 | 选择排序方式，包括：  - 最多播放 - 最新发布 - 最多弹幕 - 最多收藏 |

## **示例**

以搜索小猫视频为例，配置内容如下：

1. 搜索B站视频：

   | **配置项** | **说明** |
   | --- | --- |
   | 关键词 | 输入：小猫。 |
   | 排序方式 | 选择：最多播放 |
2. 此时，你可以在后续步骤引用搜索到的视频列表。如需在卡片中输出每个视频信息，推荐选择AI助理回复互动卡片 > 从模板生成 > 图文列表。

   | **配置项** | | **说明** |
   | --- | --- | --- |
   | 生成方式 | | 选择：从模板生成 |
   | 选择模板 | | 选择：图文列表 |
   | 卡片字段内容 | 图文列表 | 选择：动态条数。其余变量配置如下：  - 图片URL：引用“视频封面” - 文章标题：引用“视频标题” - 文章链接：引用“视频地址” - 描述（选填）：引用“视频作者” - 标签（选填）：引用“视频播放量” |

此时，你已完成B站视频搜索，并在卡片中展示。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9366625371/p831970.png)
