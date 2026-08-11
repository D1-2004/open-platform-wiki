---
title: "开发工具"
source_url: "https://open.dingtalk.com/document/aipass/development-tools"
namespace: "aipass"
slug: "development-tools"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 能力 > 拟人操作（RPA） > 开发工具"
doc_id: "HlRf4fnYLG"
updated_at: "2025-09-23 19:19:32"
---

> Source: https://open.dingtalk.com/document/aipass/development-tools
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 能力 > 拟人操作（RPA） > 开发工具
> Updated: 2025-09-23 19:19:32

# 开发工具

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理**

拟人操作（RPA）开发工具能帮助你快速创建拟人操作（RPA）项目，并且提供了丰富的开发调试能力，包括：钉钉身份认证、快速上手、开发调试、运行预览、生成描述文件等能力。

![x.jpg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8531323171/p791831.jpg)

## **安装开发工具**

1. 下载安装 Visual Studio Code，[下载地址](https://code.visualstudio.com/Download)
2. 安装完成后，在 Visual Studio Code 扩展市场中搜索 DingTalk Toolkit 并安装，点击左侧功能栏的钉钉 icon，即可开始使用。

## **能力介绍**

### **钉钉身份认证**

单击登录按钮，可唤起钉钉桌面端并打开登录页，点击授权登录按钮进行登录授权，登录成功后会自动跳转转回 vscode 并将个人信息和组织信息展示到 vscode 扩展中。

### **初始化**拟人操作（RPA）**项目**

单击**快速上手**功能栏中的**创建拟人操作（RPA）项目**按钮，会唤起交互对话框，按照指引填入项目基本信息，完成拟人操作（RPA）项目的创建。项目创建完成后，会自动在新窗口中打开项目文件目录。

### 拟人操作（RPA**）开发**

1. 在 automator.js|ts 文件注释中配置 @target\_url。

   > **[!NOTE]**
   >
   > 工具当前为单文件模式，因此仅支持识别名称为 automator 的文件。

   ```
   /**
    * @title 飞猪旅行预订机票
    * @description 需要预订机票时使用
    * @target_url_mobile https://market.m.taobao.com/app/trip/h5-traffic-search/pages/search/index.html
    */
   const { lifecycle, page, utils } = DDAutomator;
   const { loaded, step } = lifecycle;

   // ... 内容
   ```
2. 你需要确保手机、电脑在同一个局域网内，单击**开发调试**，打开调试页面后，使用钉钉移动端扫码或点击在桌面端打开目标页，即可在钉钉客户端页面和 vscode 扩展右侧 devtools 页面之间建立远程连接。成功建立连接后，在钉钉端内页面右上角可见调试面板，显示远程调试已连接，vscode 扩展打开的 devtools 页面中，可以看到页面元素内容。

   ![page.jpg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8531323171/p789755.jpg)

   之后便可开始进行拟人操作（RPA）开发，**开发调试**可提供如下能力：

   - 支持与钉钉客户端页面建立远程连接，对钉钉端内页面进行审查元素、查看日志等功能。在注释中配置 @target\_url，即可自动生成二维码，使用钉钉扫码或点击按钮打开目标页，即可建立远程连接。
   - 支持在控制台 Console 面板中远程调用拟人操作（RPA）框架 API，实时查看 API 调用效果。
   - 支持代码生成，点击开启代码生成后，在页面中的点击、填写表单、调用钉钉 jsapi 等操作都会实时转换成代码插入到文件中。
3. 单击**运行预览**，支持预览本地拟人操作（RPA），扫码或单击按钮在钉钉端内打开 target\_url 后，automator.js|ts 内容会自动运行在页面中。代码修改后，重新扫码打开页面即可预览最新内容。

### **生成描述文件**

单击**生成描述文件**按钮，会自动进行项目打包，并生成描述文件 ai-plugin.json。将 json 内容复制后，粘贴至拟人操作（RPA）发布页，完成拟人操作（RPA）创建。

> **[!NOTE]**
>
> 描述文件生成之前，请按照以下规则在文件内容的最上方进行描述内容的配置。

| **字段** | **是否必填** | **备注** |
| --- | --- | --- |
| title | 是 | 标题，必须为英文。 |
| description | 是 | 描述信息。 |
| target\_url\_mobile | 否 | 移动端目标页地址 |
| target\_url\_desktop | 否 | 桌面端目标页地址 |
| target\_url\_default | 否 | 默认目标页地址，优先使用 target\_url\_mobile 和 target\_url\_desktop。 |
| target\_valid\_domains | 是 | 可操作的目标页面host列表。自适应插件的target\_url页面需要打开另外的域名执行脚本时，每个页面domain都需要配置。 |
| keywords | 否 | 关键词，关键词之间以英文逗号分隔。 |
| examples | 否 | 大模型示例，input 表示给大模型的输入，output 表示大模型对输入的参数解析。input 内容实用双引号包裹，output 中对象 value 用双引号包裹。input 和 out 之间用空格分割。  此字段对实际会话中大模型理解会话信息非常重要，建议配置。 |
| headless\_mode | 否 | 设置拟人操作（RPA）运行时，有头模式（false）、无头模式（true） |
| support\_platform | 否 | 支持平台，默认为四端 android, ios, mac, win。 |
| param | 否 | 运行参数。  **[!NOTE]**  请严格按照两层参数定义：   - 即第一层为函数入参 params，名称和描述固定，类型为 object。 - 第二层为 params 下的属性，名称、类型、描述、示例内容自定义，之间以空格做分割，示例内容应为`example：${示例内容}`，默认值 `default：${默认值}`，卡片展示 `displayName：${卡片展示值}`。参数可选以中括号做标识，如`[params.clientType]`。 |

以下为描述内容的示例模板，请将此内容放置在文件内容的最上方。

```
/**
 * @title 飞猪旅行预订机票
 * @description 需要预订机票时使用
 * @target_url_mobile https://market.m.taobao.com/app/trip/h5-traffic-search/pages/search/index.html
 * @keywords 预定机票,订机票,机票,预订
 * @headless_mode false
 * @support_platform android,ios
 * @target_valid_domains market.m.taobao.com
 * @examples input: '帮我预订一张下周二的机票，出发地：成都，到达地：广州' output: { startCity: '成都', endCity: '广州', date: '下周二' }
 * @examples input: '预订一张明天的机票，从北京到杭州' output: { startCity: 北京', endCity: '杭州', date: '明天' }
 * @param {object} params 参数对象
 * @param {string} params.startCity 出发城市 displayName: 出发城市
 * @param {string} params.endCity 到达城市 displayName: 到达城市
 * @param {dingtalk.customTime} params.date 出发日期 format: yyyy-MM-dd displayName: 出发日期
 */
const { lifecycle, page, utils } = DDAutomator;
const { loaded, step } = lifecycle;

// ... 内容
```

除基本类型参数外，支持定义特殊类型参数，用以获取当前会话信息及会话中可以提取为钉钉标准信息的参数，包括

| **特殊参数类型** | **备注** |
| --- | --- |
| dingtalk.current.userId | 当前对话发送人的 userId。 |
| dingtalk.current.unionId | 当前对话发送人的 unionId。 |
| dingtalk.current.jobNum | 当前对话发送人的 jobNum。 |
| dingtalk.current.corpId | 当前对话发送人的 corpId。 |
| dingtalk.current.input | 当前对话内容。 |
| dingtalk.current.coversationId | 当前对话 id。 |
| dingtalk.userId | 对话中包含的用户的钉钉 userId |
| dingtalk.unionId | 对话中包含的用户的钉钉 unionId |
| dingtalk.time | 对话中包含的时间信息 |
| dingtalk.customTime | 对话中包含的时间信息，自定义格式。例如：yyyy-MM-dd 输出的时间为2023-12-31 |

特殊类型参数使用示例

```
/**
 * @param {object} params 参数对象
 * @param {dingtalk.current.userId} params.curUid 当前对话发送人的 userId。
 * @param {dingtalk.customTime} params.myTime 我的自定义时间 format: yyyy-MM-dd
 */
```

### **重置窗口**

此功能在 DingTalk Toolkit 运行异常时使用，用来重新初始化 vscode 窗口和 DingTalk Toolkit 运行上下文。
