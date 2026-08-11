---
title: "ding.config.json配置说明"
source_url: "https://open.dingtalk.com/document/download/configuration-description"
namespace: "download"
slug: "configuration-description"
group: "应用开发"
tab: "开发工具"
breadcrumb: "开发者工具 > DingTalk Design CLI > ding.config.json配置说明"
doc_id: "5GTJ26ESaa"
updated_at: "2026-01-22 19:53:05"
---

> Source: https://open.dingtalk.com/document/download/configuration-description
> Path: 应用开发 / 开发工具 / 开发者工具 > DingTalk Design CLI > ding.config.json配置说明
> Updated: 2026-01-22 19:53:05

# ding.config.json配置说明

本文档详细介绍了 `ding.config.json` 配置文件的结构、字段含义及使用方法。该配置文件在使用 DingTalk Design CLI 初始化项目后自动生成，位于项目根目录下，用于管理项目的构建行为和关联钉钉应用的元信息，是本地开发、预览、构建和发布流程中的核心配置文件。

## 使用指引

本配置文件适用于以下类型的应用开发场景：

- 企业内部应用（如工作台组件、H5微应用）
- 第三方小程序
- 工作台插件（Plugin）

开发者需根据实际应用类型正确填写 `type` 字段，并确保 `miniAppId` 和 `token` 的准确性。这些信息可在 **钉钉开发者后台 > 应用详情页** 中获取：

1. 登录 [钉钉开放平台](https://open.dingtalk.com/)。
2. 进入目标应用的详情页面。
3. 在“基础信息 > 凭证与基础信息”区域查看 `miniAppId`。
4. `token` 可在“开发配置”模块中生成或复制。

   > **[!IMPORTANT]**
   >
   > `token` 属于敏感凭证，请勿提交至 Git 等版本控制系统。建议将其通过环境变量注入或加入 `.gitignore` 文件进行保护。

## 配置字段说明

`ding.config.json` 包含以下关键字段，具体如下表所示：

| 参数 | 说明 |
| --- | --- |
| type | 应用类型：   - **plugin**：工作台组件 - **mp**：小程序 - **h5**：H5微应用 |
| typescript | 是否为一个TypeScript项目。 |
| base | 源代码目录。 |
| outDir | 产出代码目录。  **[!NOTE]**  一般情况下，JavaScript项目中填`outDir: './'`即可，TypeScript项目中填入构建后的产出目录。 |
| miniAppId | 小程序或工作台插件的应用id，在本地构建、预览、上传、lint时需要用到。 |
| token | 在本地构建、预览、上传、lint时需要用到。 |
