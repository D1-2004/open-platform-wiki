---
title: "支持 PC 工作台"
source_url: "https://open.dingtalk.com/document/dingstart/support-pc-workbench-1"
namespace: "dingstart"
slug: "support-pc-workbench-1"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > 场景示例 > 支持 PC 工作台"
doc_id: "rV8q3mXpG7"
updated_at: "2025-10-21 14:10:53"
---

> Source: https://open.dingtalk.com/document/dingstart/support-pc-workbench-1
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > 场景示例 > 支持 PC 工作台
> Updated: 2025-10-21 14:10:53

# 支持 PC 工作台

标准工作台组件目前支持移动端和 PC 端工作台的功能、数据和体验统一对齐，平台具备将移动端组件在PC端使用的能力。存量组件请对组件编码规范做一次排查优化，以便平台能统一识别组件代码，实现组件在移动端和 PC 端的复用。

PC 端示意图：

![PC端示意图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3580858261/p300407.png)

### 代码规范

- **AXML**

  - 语法要符合小程序标准，例如属性定义不能使用中文冒号（：）。
- **JS**

  - JSAPI需使用： `import 'dingtalk-jsapi/entry/union'`。
  - 语法要符合小程序标准，例如主入口文件不能使用 export。
  - 不能对原型链 props 修改。
  - 不能动态创建函数 new function。
  - 不能使用 eval。
  - 不能使用 dd 方式调用 jsapi。
  - 如果支持 PC，请参照本文中 JSAPI 改造部分的说明，选择同时支持移动和 PC 的 API 使用。
  - PC 或移动环境，取值组件的`props.config.platform = 'pc' / 'android' / 'ios'`。
  - 线上使用 JSAPI 前找@悦铭开通一下 JSAPI 权限。
- **acss**

  - 字号、尺寸等单位需要使用相对单位 rpx。
- **config.json&pc.config.json**

  - 支持 PC 需单独提供一个配置文件，命名：pc.config.json。

    如设计规范升级，工作台会统一修改组件外框等样式，减少组件未来的维护成本。配置说明如下：

    ```
    {
        "pluginComponentName": "project-select-view",
        "name": "对应下图中的title",
        "icon": "对应下图中的icon",
        "previewUrl": "https://img.alicdn.com/tfs/TB1KcAWdrj1gK0jSZFOXXc7GpXa-750-100.jpg",
        "previewHeight": 200,        
      // 工作台组件的快速设置选项   
        "quickSetting": {
            "useStandardHead": true,     // 使用工作台组件标准标题栏，请所有组件升级到此设置
            "useStandardContainer": true,   // 使用工作台组件标准样式，请所有组件升级到此设置
            "containerType": "standard",    // 组件是标准高度的组件值设置为standard，2倍高度的组件值为doubleHeight
        },
        "props": {

        }
    }
    ```

    ![quickSetting ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3580858261/p300389.png)

    标题栏配置说明：

    - **icon**：组件的 config.json 里的 icon（图示中①）。
    - **name**：组件的 config.json 里的 name（图示中②）。
    - **link**：点击标题跳转链接，组件上架时提交给验收人员（图示中③）。
    - **manage**：右侧管理，自动注入，开发者无需提供（图示中④）。
- **静态资源**

  - 不支持打包静态资源，可以对图片做 CDN 处理，使用图片链接。
- **openApp 兼容 PC 端使用参数说明**

  组件内链接在 PC 端和移动端的打开方式具有差异，可做兼容处理：

  ```
  export enum OpenType {
   // 使用侧边栏直接打开链接
   OPEN_SLIDE_PANEL = 'open_slide_panel',
    // 将链接转为二维码后在侧边栏显示
   OPEN_SLIDE_PANEL_QRCODE = 'open_slide_panel_qrcode',
    // 将链接转为短链二维码后在侧边栏显示
    // 注：小程序链接使用短链二维码可能会出现打不开的问题，
    // 建议使用'open_slide_panel_qrcode'方式
    OPEN_SLIDE_PANEL_SHORT_URL_QRCODE = 'open_slide_panel_short_url_qrcode', 
   // 将链接使用工作台新建选项卡打开
    OPEN_PC_APP = 'open_dd_tab',
   // 将链接使用端外浏览器打开
    OPEN_EXTERNAL_BROWSER = 'open_external_browser', 
  }
  interface opt extends IAppDetailModel {
   url: string;
    name?: string; // 如果侧边栏打开则需要提供一个title
    openType?: string;
    // pc端必传，pc端若不传默认为'open_slide_panel_qrcode'方式打开链接
  }
  openApp({
   url,
    name,
    openType,
  })
  ```
- **JSAPI 改造**

  如组件中都是使用的工作台的，则不需要做处理。如单独使用的 JSAPI，请关注下面内容。

  同时支持移动端和 PC 端的 JSAPI 如下，共 26 个，分别如下：

  ```
  [
    'alert',
    'confirm',
    'showToast',
    'showActionSheet',
    'setStorageSync',
    'getStorageSync',
    'removeStorageSync',
    'setClipboard',
    'createDing',
    'chooseUserFromList',
    'complexChoose',
    'chooseDepartments',
    'chooseExternalUsers',
    'createGroupChat',
    'checkBizCall',
    'chooseChatForNormalMsg',
    'chooseChat',
    'previewFileInDingTalk',
    'uploadAttachmentToDingTalk',
    'chooseDingTalkDir',
    'getAuthCode',
    'inquiryPrice',
    'createOrder',
    'getPayInfo',
    'cancelOrder',
    'openLink'
  ]
  ```

  如果之前组件中通过 dd.XXX 的方式使用了列表中的 JSAPI，需要转换成三段式，通过 npm 包 dingtalk-jsapi 来引入对应的 JSAPI，例如 alert 的引入方式如下：

  ```
  import alert from 'dingtalk-jsapi/api/device/notification/alert';
  ```

  PC 端和移动端可用的 JSAPI 与 dingtalk-jsapi 的引用路径的映射关系如下：

  ```
  alert --> import alert from 'dingtalk-jsapi/api/device/notification/alert'
  confirm --> import confirm from 'dingtalk-jsapi/api/device/notification/confirm'
  showToast --> import showToast from 'dingtalk-jsapi/api/device/notification/toast'
  showActionSheet --> import showActionSheet from 'dingtalk-jsapi/api/device/notification/actionSheet'
  setStorageSync --> import setStorageSync from 'dingtalk-jsapi/api/util/domainStorage/setItem'
  getStorageSync --> import getStorageSync from 'dingtalk-jsapi/api/util/domainStorage/getItem'
  removeStorageSync --> import removeStorageSync from 'dingtalk-jsapi/api/util/domainStorage/removeItem'
  getNetworkType --> import getNetworkType from 'dingtalk-jsapi/api/device/connection/getNetworkType'
  createDing --> import createDing from 'dingtalk-jsapi/api/biz/ding/create'
  chooseUserFromList --> import chooseUserFromList from 'dingtalk-jsapi/api/biz/customContact/choose'
  complexChoose --> import complexChoose from 'dingtalk-jsapi/api/biz/contact/complexPicker'
  chooseDepartments --> import chooseDepartments from 'dingtalk-jsapi/api/biz/contact/departmentsPicker'
  chooseExternalUsers --> import chooseExternalUsers from 'dingtalk-jsapi/api/biz/contact/externalComplexPicker'
  createGroupChat --> import createGroupChat from 'dingtalk-jsapi/api/biz/contact/createGroup'
  checkBizCall --> import checkBizCall from 'dingtalk-jsapi/api/biz/telephone/checkBizCall'
  chooseChatForNormalMsg --> import chooseChatForNormalMsg from 'dingtalk-jsapi/api/biz/chat/pickConversation'
  chooseChat --> import chooseChat from 'dingtalk-jsapi/api/biz/chat/chooseConversationByCorpId'
  previewFileInDingTalk --> import previewFileInDingTalk from 'dingtalk-jsapi/api/biz/cspace/preview'
  uploadAttachmentToDingTalk --> import uploadAttachmentToDingTalk from 'dingtalk-jsapi/api/biz/util/uploadAttachment'
  chooseDingTalkDir --> import chooseDingTalkDir from 'dingtalk-jsapi/api/biz/cspace/chooseSpaceDir'
  getAuthCode --> import getAuthCode from 'dingtalk-jsapi/api/runtime/permission/requestAuthCode'
  inquiryPrice --> import inquiryPrice from 'dingtalk-jsapi/api/biz/store/inquiry'
  createOrder --> import createOrder from 'dingtalk-jsapi/api/biz/store/createOrder'
  getPayInfo --> import getPayInfo from 'dingtalk-jsapi/api/biz/store/getPayUrl'
  cancelOrder --> import cancelOrder from 'dingtalk-jsapi/api/biz/store/closeUnpayOrder'
  openLink --> import openLink from 'dingtalk-jsapi/api/biz/util/openLink'
  ```

  JSAPI 使用文档：[客户端API总览](../../01-应用开发/03-Ogu5SlPY4t-客户端JSAPI/0002-jsapi-overview.md)。

  > **[!NOTE]**
  >
  > 如果之前自建组件使用了上述列表之外的 JSAPI，PC端将无法正常调用，目前尚未有其它的替代方案。具体诉求可通过[联系我们](https://open.dingtalk.com/document/dingstart/dashboard-model-overview2)加入**标准工作台组件/解决方案接入群**，在群内咨询服务小蜜。
