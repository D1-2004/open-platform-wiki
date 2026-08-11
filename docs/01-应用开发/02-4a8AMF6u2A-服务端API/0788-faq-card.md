---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/faq-card"
namespace: "development"
slug: "faq-card"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 互动卡片 > 常见问题"
doc_id: "72TN94vPuR"
updated_at: "2025-10-21 18:13:11"
---

> Source: https://open.dingtalk.com/document/development/faq-card
> Path: 应用开发 / 服务端API / 即时通信 > 互动卡片 > 常见问题
> Updated: 2025-10-21 18:13:11

# 常见问题

本文介绍了互动卡片常见问题。

## **发出来的卡片不符合预期**

可以使用[卡片调试工具](0777-card-debugging-tool.md)查看下发的卡片数据是否正确。

## **设置卡片数据中非String类型的参数如何处理**

如果你使用的是**新版接口**，包括[创建卡片](0778-interface-for-creating-a-card-instance.md)、[创建并投放卡片](0781-create-and-deliver-cards.md)和[更新卡片](0780-interactive-card-update-interface.md)，则需要依照[API 卡片数据的填写说明](0787-instructions-for-filling-in-api-card-data.md)填写卡片数据。

相反，如果你使用的是上述三个以外的**旧版接口**，例如机器人[发送钉钉互动卡片（高级版）](1453-send-interactive-dynamic-cards-1.md)，则需要考虑使用 sys\_full\_json\_obj 字段，具体用法如下：

创建、更新卡片的接口中，都是使用 `Map<String, String>` 来传递卡片数据的，其中 Key 为参数名、Value 为参数值。这种方式的缺点是参数值只能传递 String 类型。

sys\_full\_json\_obj 是**旧版****接口**的解决方案，是卡片数据中内置的一个参数，对应的参数值格式是 JSONString。此时，如果需要设置卡片的非 String 参数值，步骤如下：

1. 将所有非 String 参数构建成一个 JSONObject

   ```
   {
     "intParam": 1,
     "floatParam": 1.2345,
     "boolParam": true,
     "strArr": ["str1", "str2"],
     "objParam": {
       "objField1": 3,
       "objField2": 3.14
     }
   }
   ```
2. 之后将这个 JSONObject 转成 JSONString，填写到卡片数据中的 sys\_full\_json\_obj 参数处

   ```
   {
     "outTrackId": "testId"
     "cardData": {
       "cardParamMap": {
          "sys_full_json_obj": "{\"strArr\":[\"str1\",\"str2\"],\"floatParam\":1.2345,\"boolParam\":true,\"objParam\":{\"objField1\":3,\"objField2\":3.14},\"intParam\":1}"
       }
     },
     ...
   }
   ```

## **创建/更新卡片后，参数值没有正常显示**

1. 如果卡片数据中包含非 String 类型参数，确保依照上面“设置卡片数据时，如何处理非 String 类型的参数”小节中的内容，正确设置卡片数据。
2. 注意核对卡片模板搭建器中所配置的变量类型与传入的属性值的类型是否匹配。

## **卡片模板或数据更新后，发送的卡片没有更新**

注意检查是否没有更换 outTrackId。一般情况下，如果使用了新的 cardTemplateId 或 cardData 等参数，则需要生成一个全新的 outTrackId，否则更改不会生效。

## **发送互动卡片时，cardData中包含Markdown如何入参**

答：cardData中包含Markdown入参方式如下：

示例：`"cardData" : "{\"field_1\":\"**钉钉平台<font color=common_blue1_color>已发起</font>**\"}"`

## 修改模板后，发送的卡片没有更新

卡片模板有缓存，可以重启钉钉后再重试，可以重发一张新的卡片后重进会话试试。

## **卡片回传请求事件返回的私有数据没生效**

回传请求返回的私有数据要设置在 userPrivateData 字段下面，且不需要以 userId 为 key。示例如下：

```
{
  "userPrivateData": {
    "cardParamMap": {
      "key": "String"
    }
  }
}
```

## 发送卡片时定义了privateData，但卡片没有更新

答：需进入[卡片搭建平台](https://h5.dingtalk.com/interactive-card-builder/index.html#/) **> 数据源 > 编辑**，选择对应的字段开启**私有**变量即可正常更新。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8933897661/p514623.png)

## **如何给不支持点击事件的元素绑定点击事件**

一些基础组件与元素，比如文本组件等，不支持绑定点击事件。如果希望实现点击效果，则可以使用“单个容器”组件来包裹目标元素，然后在“单个容器”组件上，绑定点击事件，即可实现目标效果。

## **卡片发布与不发布有什么区别**

未发布的卡片可以多次修改，每次针对卡片模板的修改都会直接影响线上使用的所有卡片，在多人协作开发的过程中，极易因为某些意外的报错操作导致线上故障。因此，我们建议在业务卡片正式发布上线后，要及时发布模板，防止模板被意外修改。

## **机器人发送互动卡片中高级版与普通版的区别**

答：高级版与普通版的区别如下表所示：

| **操作能力** | **互动卡片普通版** | **互动卡片高级版** |
| --- | --- | --- |
| **搭建平台提取操作代码** | 支持 | 不支持 |
| **搭建平台可导出JSON** | 可一键复制导出 | 可一键导出 |
| **互动卡片回调** | 不支持 | 支持 |
| **是否支持删除** | 支持 | 支持 |
| **私有数据** | 不支持 | 支持 |
| **机器人发送互动卡片** | 支持 | 支持 |
| **更新机器人发送互动卡片** | 支持 | 支持 |
| **组件 | 区块组件库** | 支持 | 支持 |
| **一键推送测试卡片** | 支持 | 不支持 |
| **表情** | 支持 | 支持 |

## **userIdType** 字段的填写说明

`userIdType` 字段控制着整个请求中用户 ID 的类型，包括卡片创建人的 ID、私有数据归属人的 ID 等。目前，`userIdType` 有两个可选值：

- 1，默认值，代表 userId 模式（可通过调用[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)获取）
- 2，代表 unionId 模式（可以通过调用[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)获取）

`userIdType`的选取可以参考下述规则：

- 如果是企业内部创建的卡片，并且仅供企业内部使用，使用 userId 模式
- 如果是企业内部创建的卡片，但是也提供给外部人员使用（例如服务群场景），使用 unionId 模式
- 如果是 ISV 创建的卡片，使用 unionId 模式

## **如何关闭吊顶卡片**

实现关闭吊顶卡片分两步：

**第一步：搭建关闭按钮 UI。**

需要进入[卡片搭建平台](https://h5.dingtalk.com/interactive-card-builder/index.html#/)创建吊顶卡片，若已经创建吊顶卡片可忽略。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1570683171/p792089.png)

- 方式一：使用吊顶卡片模板，模板已经包含关闭按钮。

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1570683171/p792088.png)
- 方式二：使用图片直接搭建，布局参考方式 一 的模板布局。

**第二步：通过调用服务端API-**[关闭互动卡片吊顶](0760-close-interactive-card-ceiling.md)**实现关闭。**

> **[!IMPORTANT]**
>
> 设置回传请求需调用[注册卡片回调地址](0784-register-card-callback-address.md)。

选择“X”图片组件所在的布局 > 点击“X” > 点击事件类型选择“回传请求” > 设置回传参数。

群成员关闭卡片后所有人不可见，建议设置关闭按钮仅对管理员可见。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1570683171/p792090.png)

## **卡片是否可以设置组件动态可见**

答：可以实现，以横排按钮组件为例：

设置**数据源>编辑变量**> 按钮的点击事件类型选择**回传请求** > **设置回传参数 >** 设置是否显示选择**条件计算** **> 创建新条件**。isShow为**true**时，则该按钮**展示**到卡片，isShow为**false**时，则该按钮**不展示**到卡片。

![编辑普通变量isShow](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/0QvjnA2jY7V8qXo5/img/e8ba3b65-d5e3-400c-bfd5-d0f4580ecb1a.png)![设置动态可见](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/0QvjnA2jY7V8qXo5/img/f4765065-1b98-4785-bdf3-4854745b76fb.png)

## 添加多个按钮，提示不能添加多个

答：横排或者竖排按钮的添加在按钮设置最下方添加新按钮。![添加按钮](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4740957561/p464020.png)

## 竖排按钮不支持显示隐藏，竖排按钮没有是否显示配置

答：区块库组件按钮暂不支持，请使用普通组件实现。

## 卡片多媒体资源绑定变量方式怎么上传和拿到这些资源

多媒体资源支持 http 协议，可以直接使用业务可用的 http 资源。

## Windows和安卓卡片显示 [Object Object]

答：卡片测试期间因数据和模板更新，可能出现不兼容老版本模板的情况，重启下钉钉即可重新拉取模板。
