---
title: "版本对比与迁移"
source_url: "https://open.dingtalk.com/document/development/comparison--client-apis"
namespace: "development"
slug: "comparison--client-apis"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "版本对比与迁移"
doc_id: "iqQUVizgyp"
updated_at: "2026-05-22 17:53:58"
---

> Source: https://open.dingtalk.com/document/development/comparison--client-apis
> Path: 应用开发 / 客户端JSAPI / 版本对比与迁移
> Updated: 2026-05-22 17:53:58

# 版本对比与迁移

本文档详细说明钉钉客户端API的新旧版本差异、SDK引入方式、迁移操作指南，帮助开发者平滑过渡到新版API。

## **客户端SDK**

### SDK简介

`dingtalk-jsapi` 是钉钉官方提供的客户端JavaScript SDK，用于在H5微应用和小程序中调用钉钉原生能力。

### 引入方式

#### 方式一：使用npm引入（推荐）

```
npm install dingtalk-jsapi --save
```

> *dingtalk-jsapi 3.0.27 版本后支持一段式，例如：chooseChat，同时也支持三段式，例如：biz.contact.choose。*

在代码中引入：

```
import * as dd from 'dingtalk-jsapi'; // 此方式为整体加载，也可按需进行加载
```

优势：

- 支持按需加载，减少包体积
- 易于版本管理和更新
- 获得底层依赖模块的快速修复支持

#### 方式二：使用CDN引入（不推荐）

在HTML中直接引入：

```
<script src="https://g.alicdn.com/dingding/dingtalk-jsapi/3.1.0/dingtalk.open.js"></script>
```

局限性：

- 无法按需加载，包体积较大
- 难以获得底层依赖模块的快速修复支持
- 仅建议在简单场景或快速原型开发中使用

## 新旧版API对比

### **背景优势**

钉钉开放平台将客户端 API 调用方式由“三段式”统一升级为“一段式”，旨在简化调用逻辑、提升开发效率并增强跨端一致性。

- **三段式调用（旧版）**：格式为 `namespace.function.action`，如 `biz.util.chooseImage`
- **一段式调用（新版）**：格式为单一函数名，如 `chooseImage`。

**升级优势**：

- 接口命名更简洁直观
- 函数语义更清晰，易于记忆和使用
- 支持更灵活的参数结构和返回值设计
- 更好地支持 TypeScript 类型推导

**参考文档**：

- 新版客户端 API，详情参考新版[JSAPI 总览](0002-jsapi-overview.md)。
- 旧版客户端 API，分为小程序和H5微应用：

  - 小程序详情参考旧版[小程序JSAPI总览](0433-mini-program-jsapi-overview.md)。
  - H5微应用详情参考旧版[H5微应用JSAPI总览](0749-jsapi-overview-1.md)。

### 核心区别

| 特性 | 旧版API（三段式） | 新版API（一段式） |
| --- | --- | --- |
| 调用方式 | `dd.biz.contact.choose` | `dd.chooseChat` |
| 命名规范 | 按功能模块分层（biz/device/ui等） | 扁平化命名，语义更清晰 |
| 兼容性 | 所有版本均支持 | 需要 3.0.27+ 版本 |
| 推荐程度 | 兼容保留，不推荐新项目使用 | 推荐使用 |
| 参数结构 | 部分API参数复杂 | 参数更统一、简洁 |
| 返回值 | 部分API返回结构不一致 | 返回值更规范 |

### 调用示例对比

以"选择会话"为例：

- 旧版（三段式）

  ```
  dd.biz.chat.choose({
    corpId: 'dingxxxxxxxx',
    isAllowCreateGroup: true,
    onSuccess: (result) => {
      console.log('选择的会话ID:', result.cid);
    },
    onFail: (err) => {
      console.error('选择失败', err);
    }
  });
  ```
- 新版（一段式）

  ```
  dd.chooseChat({
    corpId: 'dingxxxxxxxx',
    isAllowCreateGroup: true,
    onSuccess: (result) => {
      console.log('选择的会话ID:', result.cid);
    },
    onFail: (err) => {
      console.error('选择失败', err);
    }
  });
  ```

### **API对照表**

#### **界面**

用于控制页面导航、弹窗反馈、日期选择等用户界面交互行为。

| **类目** | **新版客户端API** | **旧版客户端API** |
| --- | --- | --- |
| **地图** | [chooseDistrict](https://open.dingtalk.com/document/orgapp/jsapi-choose-district) | biz.util.chooseRegion |
| **导航栏** | [setNavigationTitle](https://open.dingtalk.com/document/orgapp/jsapi-set-navigation-title) | biz.navigation.setTitle |
| [setNavigationIcon](https://open.dingtalk.com/document/orgapp/jsapi-set-navigation-icon) | biz.navigation.setIcon |
| [setNavigationLeft](https://open.dingtalk.com/document/orgapp/jsapi-set-navigation-left) | biz.navigation.setLeft |
| [goBackPage](https://open.dingtalk.com/document/orgapp/jsapi-go-back-page) | biz.navigation.goBack |
| [replacePage](https://open.dingtalk.com/document/orgapp/jsapi-replace-page) | biz.navigation.replace |
| [closePage](https://open.dingtalk.com/document/orgapp/jsapi-close-page) | biz.navigation.close |
| [quitPage](https://open.dingtalk.com/document/orgapp/jsapi-quit-page) | biz.navigation.quit |
| **交互反馈** | [alert](https://open.dingtalk.com/document/orgapp/jsapi-alert) | device.notification.alert |
| [confirm](https://open.dingtalk.com/document/orgapp/jsapi-confirm) | device.notification.confirm |
| [showToast](https://open.dingtalk.com/document/orgapp/jsapi-show-toast) | device.notification.toast |
| [hideLoading](https://open.dingtalk.com/document/orgapp/jsapi-hide-loading) | device.notification.hidePreloader |
| [hideToast](https://open.dingtalk.com/document/orgapp/jsapi-hide-toast) | device.notification.hideToast |
| [showLoading](https://open.dingtalk.com/document/orgapp/jsapi-show-loading) | device.notification.showPreloader |
| [showActionSheet](https://open.dingtalk.com/document/orgapp/jsapi-show-action-sheet) | device.notification.actionSheet |
| [showModal](https://open.dingtalk.com/document/orgapp/jsapi-show-modal) | device.notification.extendModal |
| [prompt](https://open.dingtalk.com/document/orgapp/jsapi-prompt) | device.notification.prompt |
| **选择日期** | [datePicker](https://open.dingtalk.com/document/orgapp/jsapi-date-picker) | biz.util.datetimepicker |
| [dateRangePicker](https://open.dingtalk.com/document/orgapp/jsapi-date-range-picker) | biz.calendar.chooseInterval |
| [timePicker](https://open.dingtalk.com/document/orgapp/jsapi-time-picker) | biz.util.timepicker |
| [chooseDateTime](https://open.dingtalk.com/document/orgapp/jsapi-choose-date-time) | biz.calendar.chooseDateTime |
| [chooseOneDayInCalendar](https://open.dingtalk.com/document/orgapp/jsapi-choose-one-day-in-calendar) | biz.calendar.chooseOneDay |
| [chooseHalfDayInCalendar](https://open.dingtalk.com/document/orgapp/jsapi-choose-half-day-in-calendar) | biz.calendar.chooseHalfDay |
| **下拉刷新** | [enablePullDownRefresh](https://open.dingtalk.com/document/orgapp/jsapi-enable-pull-down-refresh) | ui.pullToRefresh.enable |
| [disablePullDownRefresh](https://open.dingtalk.com/document/orgapp/jsapi-disable-pull-down-refresh) | ui.pullToRefresh.disable |
| **选项选择器** | [singleSelect](https://open.dingtalk.com/document/orgapp/jsapi-single-select) | biz.util.chosen |
| [multiSelect](https://open.dingtalk.com/document/orgapp/jsapi-multi-select) | biz.util.multiSelect |

#### **设备**

提供对手机硬件功能的访问能力，如 NFC、振动、剪贴板等。

| **类目** | **新版客户端API** | **旧版客户端API** |
| --- | --- | --- |
| **UUID** | [getDeviceUUID](https://open.dingtalk.com/document/orgapp/jsapi-get-device-uuid) | device.base.getUUID |
| **NFC** | [writeNFC](https://open.dingtalk.com/document/orgapp/jsapi-write-nfc) | device.nfc.nfcWrite |
| [readNFC](https://open.dingtalk.com/document/orgapp/jsapi-read-nfc) | device.nfc.nfcRead |
| **振动** | [vibrate](https://open.dingtalk.com/document/orgapp/jsapi-vibrate) | device.notification.vibrate |
| **扫码** | [scanCard](https://open.dingtalk.com/document/orgapp/jsapi-scan-card) | biz.util.scanCard |
| **摇一摇** | [clearShake](https://open.dingtalk.com/document/orgapp/jsapi-clear-shake) | device.accelerometer.clearShake |
| [watchShake](https://open.dingtalk.com/document/orgapp/jsapi-watch-shake) | device.accelerometer.watchShake |
| **剪贴板** | [setClipboard](https://open.dingtalk.com/document/orgapp/jsapi-set-clipboard) | biz.clipboardData.setData |
| **Wi-Fi** | [getWifiStatus](https://open.dingtalk.com/document/orgapp/jsapi-get-wifi-status) | device.base.getWifiStatus |
| **屏幕亮度** | [setKeepScreenOn](https://open.dingtalk.com/document/orgapp/jsapi-set-keep-screen-on) | biz.util.setScreenKeepOn |
| [setScreenBrightness](https://open.dingtalk.com/document/orgapp/jsapi-set-screen-brightness) | device.screen.setScreenBrightness |
| **拨打电话** | [addPhoneContact](https://open.dingtalk.com/document/orgapp/jsapi-add-phone-contact) | biz.phoneContact.add |
| **设备电量** | [getBatteryInfo](https://open.dingtalk.com/document/orgapp/jsapi-get-battery-info) | device.base.getBatteryInfo |
| **网络状态** | [getNetworkType](https://open.dingtalk.com/document/orgapp/jsapi-get-network-type) | device.connection.getNetworkType |
| [getWifiHotspotStatus](https://open.dingtalk.com/document/orgapp/jsapi-get-wifi-hotspot-status) | device.base.getInterface |
| **系统信息** | [getSystemInfo](https://open.dingtalk.com/document/orgapp/jsapi-get-system-info) | device.base.getPhoneInfo |
| [rsa](https://open.dingtalk.com/document/orgapp/jsapi-rsa) | biz.data.rsa |
| [showAuthGuide](https://open.dingtalk.com/document/orgapp/jsapi-show-auth-guide) | biz.util.showAuthGuide |
| [checkAuth](https://open.dingtalk.com/document/orgapp/jsapi-check-auth) | biz.util.checkAuth |
| [isScreenReaderEnabled](https://open.dingtalk.com/document/orgapp/jsapi-is-screen-reader-enabled) | device.screen.isScreenReaderEnabled |
| [getSystemSettings](https://open.dingtalk.com/document/orgapp/jsapi-get-system-settings) | device.base.openSystemSetting |
| **设备方向** | [resetScreenView](https://open.dingtalk.com/document/orgapp/jsapi-reset-screen-view) | device.screen.resetView |
| [rotateScreenView](https://open.dingtalk.com/document/orgapp/jsapi-rotate-screen-view) | device.screen.rotateView |

#### **跳转**

用于实现页面跳转、本地缓存等通用功能。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [openLink](https://open.dingtalk.com/document/orgapp/jsapi-open-link) | biz.util.openLink |
| [isInTabWindow](https://open.dingtalk.com/document/orgapp/jsapi-is-in-tab-window) | biz.tabwindow.isTab |
| [getStorage](https://open.dingtalk.com/document/orgapp/jsapi-get-storage) | util.domainStorage.getItem |
| [removeStorage](https://open.dingtalk.com/document/orgapp/jsapi-remove-storage) | util.domainStorage.removeItem |
| [navigateBackPage](https://open.dingtalk.com/document/orgapp/jsapi-navigate-back-page) | biz.navigation.navigateBackPage |
| [navigateToPage](https://open.dingtalk.com/document/orgapp/jsapi-navigate-to-page) | biz.navigation.navigateToPage |
| [openMicroApp](https://open.dingtalk.com/document/orgapp/jsapi-open-micro-app) | biz.microApp.openApp |
| [openPageInMicroApp](https://open.dingtalk.com/document/orgapp/jsapi-open-page-in-micro-app) | biz.util.open |
| [openPageInWorkBenchForPC](https://open.dingtalk.com/document/orgapp/jsapi-open-page-in-work-bench-for-pc) | biz.util.invokeWorkbench |
| [openPageInSlidePanelForPC](https://open.dingtalk.com/document/orgapp/jsapi-open-page-in-slide-panel-for-pc) | biz.util.openSlidePanel |

#### **多媒体**

支持图像、音频的采集与播放控制。

| **类目** | **新版客户端API** | **旧版客户端API** |
| --- | --- | --- |
| **图片** | [chooseImage](https://open.dingtalk.com/document/orgapp/jsapi-choose-image) | biz.util.chooseImage |
| [previewImage](https://open.dingtalk.com/document/orgapp/jsapi-preview-image) | biz.util.previewImage |
| **录音** | [translateVoice](https://open.dingtalk.com/document/orgapp/jsapi-translate-voice) | device.audio.translateVoice |
| [onPlayAudioEnd](https://open.dingtalk.com/document/orgapp/jsapi-on-play-audio-end) | device.audio.onPlayEnd |
| [onRecordEnd](https://open.dingtalk.com/document/orgapp/jsapi-on-record-end) | device.audio.onRecordEnd |
| [downloadAudio](https://open.dingtalk.com/document/orgapp/jsapi-download-audio) | device.audio.download |
| [resumeAudio](https://open.dingtalk.com/document/orgapp/jsapi-resume-audio) | device.audio.resume |
| [pauseAudio](https://open.dingtalk.com/document/orgapp/jsapi-pause-audio) | device.audio.pause |
| [stopAudio](https://open.dingtalk.com/document/orgapp/jsapi-stop-audio) | device.audio.stop |
| [playAudio](https://open.dingtalk.com/document/orgapp/jsapi-play-audio) | device.audio.play |
| [stopRecord](https://open.dingtalk.com/document/orgapp/jsapi-stop-record) | device.audio.stopRecord |
| [startRecord](https://open.dingtalk.com/document/orgapp/jsapi-start-record) | device.audio.startRecord |

#### **缓存**

用于在客户端进行数据持久化存储。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [setStorage](https://open.dingtalk.com/document/orgapp/jsapi-set-storage) | util.domainStorage.setItem |
| [getStorage](https://open.dingtalk.com/document/orgapp/jsapi-get-storage) | util.domainStorage.getItem |
| [removeStorage](https://open.dingtalk.com/document/orgapp/jsapi-remove-storage) | util.domainStorage.removeItem |

#### **位置**

提供定位、地图展示、搜索等功能。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [getLocation](https://open.dingtalk.com/document/orgapp/jsapi-get-location) | device.geolocation.get |
| [openLocation](https://open.dingtalk.com/document/orgapp/jsapi-open-location) | biz.map.view |
| [searchMap](https://open.dingtalk.com/document/orgapp/jsapi-search-map) | biz.map.search |
| [locateInMap](https://open.dingtalk.com/document/orgapp/jsapi-locate-in-map) | biz.map.locate |
| [getLocatingStatus](https://open.dingtalk.com/document/orgapp/jsapi-get-locating-status) | device.geolocation.status |
| [stopLocating](https://open.dingtalk.com/document/orgapp/jsapi-stop-locating) | device.geolocation.stop |
| [startLocating](https://open.dingtalk.com/document/orgapp/jsapi-start-locating) | device.geolocation.start |

#### **网络**

支持文件下载等网络操作。

| **类目** | **新版客户端API** | **旧版客户端API** |
| --- | --- | --- |
| **上传下载** | [downloadFile](https://open.dingtalk.com/document/orgapp/jsapi-download-file) | biz.file.downloadFile |

#### **分享**

实现内容分享至会话或其他渠道。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [share](https://open.dingtalk.com/document/orgapp/jsapi-share) | biz.util.share |
| [showSharePanel](https://open.dingtalk.com/document/orgapp/jsapi-show-share-panel) | biz.util.showSharePanel |

#### **获取凭证**

用于获取用户身份凭证。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [getAuthCode](https://open.dingtalk.com/document/orgapp/jsapi-get-auth-code) | runtime.permission.requestAuthCode |
| [getOperateAuthCode](https://open.dingtalk.com/document/orgapp/jsapi-get-operate-auth-code) | runtime.permission.requestOperateAuthCode |

#### **会话管理**

用于打开或选择聊天窗口。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [chooseChat](https://open.dingtalk.com/document/orgapp/jsapi-choose-chat) | biz.chat.chooseConversationByCorpId |
| [openChatByChatId](https://open.dingtalk.com/document/orgapp/jsapi-open-chat-by-chat-id) | biz.chat.toConversation |
| [openChatByUserId](https://open.dingtalk.com/document/orgapp/jsapi-open-chat-by-user-id) | biz.chat.openSingleChat |
| [openChatByConversationId](https://open.dingtalk.com/document/orgapp/jsapi-open-chat-by-conversation-id) | biz.chat.toConversationByOpenConversationId |

#### **通讯录**

用于从组织架构中选择人员或部门。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [choosePhonebook](https://open.dingtalk.com/document/orgapp/jsapi-choose-phonebook) | biz.contact.chooseMobileContacts |
| [complexChoose](https://open.dingtalk.com/document/orgapp/jsapi-complex-choose) | biz.contact.complexPicker |
| [chooseDepartments](https://open.dingtalk.com/document/orgapp/jsapi-choose-departments) | biz.contact.departmentsPicker |
| [chooseExternalUsers](https://open.dingtalk.com/document/orgapp/jsapi-choose-external-users) | biz.contact.externalComplexPicker |
| [editExternalUser](https://open.dingtalk.com/document/orgapp/jsapi-edit-external-user) | biz.contact.externalEditForm |
| [chooseUserFromList](https://open.dingtalk.com/document/orgapp/jsapi-choose-user-from-list) | chooseUserFromList |
| [chooseStaffForPC](https://open.dingtalk.com/document/orgapp/jsapi-choose-staff-for-pc) | biz.contact.choose |

#### **DING**

用于创建和发送 DING 消息。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [createDing](https://open.dingtalk.com/document/orgapp/jsapi-create-ding) | biz.ding.create |
| [createDingForPC](https://open.dingtalk.com/document/orgapp/jsapi-create-ding-for-pc) | biz.ding.post |

#### **办公电话**

支持云呼叫、快速拨号等功能。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [callUsers](https://open.dingtalk.com/document/orgapp/jsapi-call-users) | biz.telephone.call |
| [checkBizCall](https://open.dingtalk.com/document/orgapp/jsapi-check-biz-call) | biz.telephone.checkBizCall |
| [getCloudCallList](https://open.dingtalk.com/document/orgapp/jsapi-get-cloud-call-list) | biz.conference.getCloudCallList |
| [makeCloudCall](https://open.dingtalk.com/document/orgapp/jsapi-make-cloud-call) | biz.conference.createCloudCall |
| [getCloudCallInfo](https://open.dingtalk.com/document/orgapp/jsapi-get-cloud-call-info) | biz.conference.getCloudCallInfo |
| [quickCallList](https://open.dingtalk.com/document/orgapp/jsapi-quick-call-list) | biz.telephone.quickCallList |

#### **钉盘**

用于文件保存、预览和上传。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [saveFileToDingTalk](https://open.dingtalk.com/document/orgapp/jsapi-save-file-to-ding-talk) | biz.cspace.saveFile |
| [previewFileInDingTalk](https://open.dingtalk.com/document/orgapp/jsapi-preview-file-in-ding-talk) | biz.cspace.preview |
| [uploadAttachmentToDingTalk](https://open.dingtalk.com/document/orgapp/jsapi-upload-attachment-to-ding-talk) | biz.util.uploadAttachment |
| [chooseDingTalkDir](https://open.dingtalk.com/document/orgapp/jsapi-choose-ding-talk-dir) | biz.cspace.chooseSpaceDir |
| [previewImagesInDingTalkBatch](https://open.dingtalk.com/document/orgapp/jsapi-preview-images-in-ding-talk-batch) | biz.cspace.previewDentryImages |

#### **文件**

操作设备本地文件。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [openLocalFile](https://open.dingtalk.com/document/orgapp/jsapi-open-local-file) | biz.util.openLocalFile |
| [isLocalFileExist](https://open.dingtalk.com/document/orgapp/jsapi-is-local-file-exist) | biz.util.isLocalFileExist |

#### **视频**

发起视频会议呼叫。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [makeVideoConfCall](https://open.dingtalk.com/document/orgapp/jsapi-make-video-conf-call) | biz.conference.videoConfCall |

#### **专属开放**

面向特定客户开放的能力。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [getUserExclusiveInfo](https://open.dingtalk.com/document/orgapp/jsapi-get-user-exclusive-info) | biz.realm.getUserExclusiveInfo |

## 迁移操作指南

### 迁移策略

#### 1. 新项目（直接使用）

直接使用新版API（一段式）：

- 确保 `dingtalk-jsapi` 版本 >= 3.0.27
- 优先使用一段式调用方式
- 参考官方文档中的最新示例代码

#### 1. 已有项目（渐进式迁移）

**阶段一：评估现状**

- 统计项目中使用的三段式API数量
- 识别哪些API有对应的一段式版本
- 评估迁移工作量

**阶段二：逐步替换**

- 从非核心功能开始替换（如UI组件、工具类API）
- 逐个模块迁移，每完成一个模块进行测试
- 保持向后兼容，确保旧代码仍能正常工作

**阶段三：全面验证**

- 完成所有可迁移API的替换
- 进行全面的回归测试
- 更新文档和代码注释

### 迁移示例

以下是一个完整的迁移示例，展示如何将旧版代码升级为新版：

**迁移前（旧版）**：

```
import dd from 'dingtalk-jsapi';

// 选择人员
dd.biz.contact.choose({
  startWithDepartmentId: -1,
  multiple: true,
  onSuccess: (result) => {
    console.log('选择的人员:', result.users);
  },
  onFail: (err) => {
    console.error('选择失败', err);
  }
});

// 获取位置
dd.device.geolocation.get({
  targetAccuracy: 200,
  coordinate: 1,
  withReGeocode: false,
  useCache: true,
  onSuccess: (result) => {
    console.log('位置信息:', result);
  },
  onFail: (err) => {
    console.error('获取位置失败', err);
  }
});
```

迁移后（新版）：

```
import dd from 'dingtalk-jsapi';

// 选择人员
dd.chooseContact({
  startWithDepartmentId: -1,
  multiple: true,
  onSuccess: (result) => {
    console.log('选择的人员:', result.users);
  },
  onFail: (err) => {
    console.error('选择失败', err);
  }
});

// 获取位置
dd.getLocation({
  targetAccuracy: 200,
  coordinate: 1,
  withReGeocode: false,
  useCache: true,
  onSuccess: (result) => {
    console.log('位置信息:', result);
  },
  onFail: (err) => {
    console.error('获取位置失败', err);
  }
});
```

### 注意事项

1. **兼容性测试**：迁移后务必在不同版本的钉钉客户端上进行测试
2. **参数一致性**：大部分API的参数保持不变，但建议重新核对官方文档
3. **回调函数**：`onSuccess` 和 `onFail`的使用方式保持一致
4. **鉴权配置**：H5应用的鉴权流程不受影响，无需修改
5. **错误处理**：新版的错误码和错误信息可能有所优化，建议更新错误处理逻辑

## **常见问题**

- **Q1：我的项目必须使用旧版API吗？**

  答：不是必须的。新版SDK（3.0.27+）同时支持一段式和三段式调用，你可以根据实际情况选择：

  - 新项目：推荐使用一段式
  - 老项目：可以继续使用三段式，或逐步迁移到一段式
- **Q2：一段式API是否在所有钉钉版本中都可用？**

  答：一段式API需要满足以下条件：

  - `dingtalk-jsapi` 版本 >= 3.0.27
  - 钉钉客户端版本较新（建议升级到最新版本）

    如果在不支持的环境中调用一段式API，会返回错误。建议在调用前进行能力检测：

    ```
    <javascript>

      if (typeof dd.chooseChat === 'function') {  // 支持一段式API  dd.chooseChat({...});} else {  // 降级使用三段式API  dd.biz.chat.choose({...});}
    ```
- **Q3: 迁移后是否需要重新发布应用？**

  答：是的。任何代码变更都需要重新构建并发布应用。建议在低峰期发布，并做好回滚准备。
- **Q4: 旧版API会被废弃吗？**

  答：目前钉钉官方尚未宣布废弃三段式API的计划，但推荐新项目使用一段式API。三段式API将继续保持兼容，以确保存量应用的稳定运行。
- **Q5: 如何确认当前使用的SDK版本？**

  答：可以通过以下方式查看：

  ```
  <javascript>

  console.log(dd.version); // 输出SDK版本号
  ```

  或在 `package.json` 中查看：

  ```
  <json>

  {  
    "dependencies": {
      "dingtalk-jsapi": "^3.0.27"  
    }
  }
  ```
