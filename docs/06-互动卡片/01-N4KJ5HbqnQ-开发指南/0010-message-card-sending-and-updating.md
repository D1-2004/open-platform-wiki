---
title: "消息卡片发送及更新"
source_url: "https://open.dingtalk.com/document/development/message-card-sending-and-updating"
namespace: "development"
slug: "message-card-sending-and-updating"
group: "互动卡片"
tab: "开发指南"
breadcrumb: "消息卡片发送及更新"
doc_id: "FvywjLsCVr"
updated_at: "2025-09-23 19:18:22"
---

> Source: https://open.dingtalk.com/document/development/message-card-sending-and-updating
> Path: 互动卡片 / 开发指南 / 消息卡片发送及更新
> Updated: 2025-09-23 19:18:22

# 消息卡片发送及更新

为了让使用者更加直观地了解如何使用模板编辑器来搭建模板，这里我们以一个审批卡片为例子，给大家展示卡片从 0 到 1 的开发过程。

## **步骤一：分析卡片需求并创建卡片模板**

一个典型的审批卡片样式：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3782293761/p549542.png)

用户点击整个卡片可以跳转到审批的详情页面，点击卡片底部的按钮，则可以快速地完成“同意”、“拒绝”操作，同时卡片状态发生变更，按钮切换成“已同意”或“已拒绝”的样式：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3782293761/p549543.png)

此时按钮已不能再点击，但仍可以点击整个卡片进入到详情页面。

分析完需求后，就可以在[钉钉卡片平台](https://open-dev.dingtalk.com/fe/card#/)上创建对应的卡片模板：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p525141.png)

## **步骤二：分析卡片模板布局以及搭建卡片模板**

从上面审批卡片的样式我们可以发现，卡片分为三部分：

- 卡片头部区
- 卡片内容区
- 卡片操作区

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3782293761/p549544.png)

### **1. 卡片头部区搭建**

卡片头部区的样式可以通过布局容器来实现三栏的样式。图片、文字以及标签可以分别放置在对应的布局中。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3782293761/p549545.png)

同时可以发现，最左边的审批图标是固定尺寸的，因此对应的布局宽度可以设置成固定宽度：

![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p524336.gif)

而对于中间“审批”的文字，其宽度有可能会随着不同的客户端显示出来不同的宽度，因此这里需要给文字和对应的布局设置成自适应宽度：

![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p524347.gif)

最后的标签组件则不需要太多的设置。配置完标签组件之后，再整体调整几个组件之间的间距以及垂直居中即可：

![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p524348.gif)

至此卡片头部区已搭建完成。

### **2. 卡片内容区搭建**

内容区布局相对比较简单，上下分别是由文本组件构成，唯一的不同是，上面的文本设置了加粗，下面的文本是小号字体，同时设置了灰色颜色。

而中间的内容则可以由一个布局容器，里面放置两个文本的布局来组成。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3782293761/p549546.png)

在设置中间的文本内容时，只需要留意给左边的布局和文本设置成自适应宽度即可，这样右边的文案内容就会紧贴左边的文案：

![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p524414.gif)

### **3. 卡片操作区搭建**

卡片操作区只有两个按钮，比较简单，因此这里直接使用「横排按钮」组件来搭建即可：![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p524989.gif)

至此整个卡片模板的样式已经全部搭建完成。

## **步骤三：**定义模板字段以及绑定数据

上面的步骤搭建的是一个静态的卡片模板，为了能让卡片真正在业务系统中使用，需要对卡片模板里面的内容和真正的业务数据做结合。因此这里需要对卡片模板进行字段的定义以及绑定。

### **1. 定义卡片模板变量字段**

从该审批卡片的需求来看，卡片上存在动态变化的内容有：

- 审批的二级模块
- 审批的标题
- 审批的内容项
- 审批的创建时间
- 审批的状态
- 审批的详情页链接

因此可以定义出该卡片的所有字段：

| **字段** | **变量类型** | **描述** |
| --- | --- | --- |
| brand | 字符串 | 审批二级模块的名称 |
| title | 字符串 | 审批标题 |
| contents | 对象数组 | 审批内容项。是一个对象数组，对象的结构在下方描述 |
| contents[\*].label | 字符串 | 审批内容项的标题 |
| contents[\*].text | 字符串 | 审批内容项的内容 |
| date | 字符串 | 审批单的创建时间 |
| status | 字符串 | 审批状态 |
| detailUrl | 字符串 | 审批详情页的URL |

其中为了让审批内容足够灵活，审批内容项使用对象数组来表达，而不是使用单独的字段，这样方便后续进行内容扩展。

有了上述的字段之后便可以把字段录入到卡片模板搭建器的变量面板中：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p525031.png)

在录入完模板的变量之后，为了方便在搭建的时候预览数据，也可以在这个时候配置好对应的变量 mock 数据：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p525049.png)

### **2. 绑定卡片模板变量**

#### **文本变量绑定**

对于文本的变量绑定，只需要在文本组件里面使用`${变量}`的格式即可完成绑定：

![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5826269661/p525038.gif)

在审批内容项这里需要进行特殊的处理，由于上个环节给内容项设置的字段结构是一个对象数组，因此在模板搭建这里得进行调整，需要把搭建好的内容放入到循环渲染容器中，同时给循环渲染容器绑定对应的对象数组，以及为内容项绑定对应的循环字段：

![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p525062.gif)

在循环渲染容器里面绑定文本内容时，绑定的变量格式是`${loop.变量}`，该语法用来表明当前数据是从对象数组里面取每一项的字段。

同时，在编辑卡片模板时，循环渲染容器里的元素默认只会显示一条内容，如果希望显示完整内容，可以切换到预览模式来查看。

#### **按钮变量绑定**

在当前的审批卡片中，我们希望当用户点击“同意”或“拒绝”之后，卡片能够切换到“已同意”或“已拒绝”的状态，此时按钮不再可点击，为了实现该效果，我们需要再新增两个按钮，分别是“已同意”和“已拒绝”，然后给这两个按钮分别设置成禁用的状态，让按钮不可点击：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p525066.png)

这个时候卡片会显示四个按钮，为了让按钮能根据审批的状态来显示正确的按钮，这里需要对四个按钮分别配置“是否显示”的属性，通过审批的状态字段来控制按钮的显示。当：

- status 字段值为 pending 时，表示还未进行操作，此时显示“拒绝”和“同意”两个按钮
- status 字段值为 accept 时，表示审批已通过，此时显示“已通过”的按钮，其他按钮不显示
- status 字段值为 reject 时，表示审批已拒绝，此时显示“已拒绝”的按钮，其他按钮不显示

![ezgif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p525086.gif)

#### **按钮点击事件绑定**

对于卡片上的“同意”和“拒绝”按钮，我们希望用户点击之后能够直接在卡片上发起回调请求到业务系统中执行对应的操作。因此在这里需要对这两个按钮配置点击事件：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p525091.png)

除了给按钮设置了“点击事件类型”为“回传请求”之外，还定义了回传参数，这代表当按钮被点击时，此时回传给业务系统的参数里面会携带上的额外参数（如上图的中展示的参数是`{"action": "reject"}`），用来让业务系统区分当前是什么操作。

#### **卡片链接跳转绑定**

最后需要对整个卡片配置跳转链接，我们希望用户点击除按钮之外的其他地方都能够直接跳转到当前审批的详情页面，因此在搭建器上只需要选中卡片组件，在“事件”的面板上设置“链接跳转”的事件，同时绑定对应的变量即可：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4826269661/p525088.png)

至此卡片模板的搭建和配置已经全部完成。

## **步骤四：**实现卡片创建及投放

卡片模板搭建完成并且保存之后，接下来可以通过调用服务端API-[创建并投放卡片](../../01-应用开发/02-4a8AMF6u2A-服务端API/0781-create-and-deliver-cards.md)接口实现卡片投放。以这次的审批卡片为例，具体调用 API 的请求如下：

```
POST /v1.0/card/instances/createAndDeliver HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:fake_token
Content-Type:application/json

{
  "userId": "fake_user_id",
  "cardTemplateId": "fake_card_template_id",
  "outTrackId": "custom_biz_id",
  "openSpaceId": "fake_open_conversation_id",
  "cardData" : {
  	"cardParamMap": {
      "brand": "智能财务",
      "title": "朱小志提交的财务报销",
      "contents": [
        {
          "label": "报销类型",
          "text": "差旅费"
        },
        {
          "label": "报销金额",
          "text": "1000"
        },
        {
          "label": "报销理由",
          "text": "出差费用"
        }
      ],
      "date": "2022-05-22 21:20",
      "status": "pending",
      "detailUrl": "https://dingtalk.com"
    }
  },
  "imGroupOpenSpaceModel" : {
    "supportForward" : true,
    "lastMessageI18n" : {
      "zh_CN" : "朱小志提交的财务报销"
    }
  },
  "imGroupOpenDeliverModel" : {
    "robotCode": "fake_robot_code"
  }
}
```

其中：

- `userId`：创建该卡片的用户 id
- cardTemplateId：是卡片模板的 ID ，这个在卡片编辑器创建模板时就能够获取到
- outTrackId：是卡片的唯一 ID ，这个 ID 需要业务侧来维护，在审批的场景下，可以对应为审批单的 ID；后续如果需要对卡片进行更新，则需要通过该 ID 进行更新
- openSpaceId：是所要投放的场域的 ID 。在审批这个例子中，我们需要把它投放到群聊中，因此该 ID 在这里对应的是群的 ID，即 openConversationId
- cardData：是当前卡片的数据，对应到卡片模板上的变量字段。
- imGroupOpenSpaceModel：是群聊/单聊场域的场域配置信息，这里可以设置卡片消息是否支持转发（supportForward）、以及消息的 lastMessage
- imGroupOpenDeliverModel：是群聊场域的投放配置信息，这里需要设置当前卡片是由哪一个机器人所发出来的（robotCode）

调用接口成功之后就能在群里面看到我们发送出来的卡片了。

## **步骤五：响应用户点击操作**

前面的步骤都完成之后，卡片就可以正常发送到群聊里。但此时卡片上的按钮还不具备交互能力，点击按钮会发现没有任何反应。

从上面的章节可以看到，我们为“同意”按钮和“拒绝”按钮设置了“回传请求”的事件。“回传请求”功能会在用户点击该按钮的时候主动调用卡片发送方所提供的回调地址，并且携带上相关参数。但在使用该功能之前，需要先注册卡片的回调地址，详细注册方法可以参考[注册卡片回调地址](../../01-应用开发/02-4a8AMF6u2A-服务端API/0784-register-card-callback-address.md)文档。

当卡片有配置回调地址之后，此时用户点击“同意”按钮，钉钉卡片系统会向回调地址发送一个 HTTP 请求，同时带上以下参数：

```
{
    "corpId": "dingXXXXXX",
    "outTrackId": "custom_biz_id",
    "userId": "XXXXXX",
    "value": "{\"cardPrivateData\":{\"actionIds\":[\"1\"]},\"params\":{\"action\":\"agree\"}}"
}
```

其中：

- corpId：点击该按钮的用户的组织
- outTrackId：卡片的唯一ID。与发送卡片时的 outTrackId 值是一致的
- userId：点击该按钮的用户 ID
- value：按钮的详细信息。它是一个 JSON 字符串，里面包含了 cardPrivateData 字段，cardPrivateData.actionIds 代表的是当前点击的按钮 ID 。例如在审批的这个例子里面，由于“同意”按钮的 ID 是 1 ，因此这里 actionIds 的值是 ["1"] 。如果你在卡片模板上给按钮配置了回传参数，那么这些参数会在 cardPrivateData.params 里面出现。一般来说，业务系统可以根据 actionIds 以及 params 来确定用户所点击的按钮是哪一个，需要执行什么操作。

那么这时候为了让审批卡片能够显示“已同意”的界面，在回调请求里面需要返回新的卡片数据，来让卡片界面进行更新：

```
{
  "cardUpdateOptions": {
    "updateCardDataByKey": true
  },
  "cardData": {
    "cardParamMap": {
      "status": "accept"
    }
  }
}
```

其中 cardUpdateOptions.updateCardDataByKey 代表了此次更新卡片的数据，只需要更新指定的字段，其他没有更新的字段保持原有的值。当返回了新的数据之后，钉钉的互动卡片会及时刷新为最新的状态和数据，至此就完成了卡片的状态更新的流程。

> **[!NOTE]**
>
> 需要注意的是，目前在卡片回传请求中更新 cardData 只会将公有数据下发给触发回传请求事件的用户，不会扩散给所有人。如果有需要协同更新所有卡片的需求，可以另外调用[更新卡片](../../01-应用开发/02-4a8AMF6u2A-服务端API/0780-interactive-card-update-interface.md)接口进行公有数据的更新。更多事件回调相关请参考文档：[事件回调](0007-event-callback-card.md)。

## **相关内容**

如果你需要了解更多互动卡片示例，请参考[互动卡片示例中心](https://github.com/open-dingtalk/dingtalk-card-examples)
