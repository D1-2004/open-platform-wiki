---
title: "DDAutomator 框架"
source_url: "https://open.dingtalk.com/document/aipass/the-ddautomator-framework"
namespace: "aipass"
slug: "the-ddautomator-framework"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 能力 > 拟人操作（RPA） > DDAutomator 框架"
doc_id: "hKT5WyvptF"
updated_at: "2025-09-23 19:19:31"
---

> Source: https://open.dingtalk.com/document/aipass/the-ddautomator-framework
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 能力 > 拟人操作（RPA） > DDAutomator 框架
> Updated: 2025-09-23 19:19:31

# DDAutomator 框架

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理**

拟人操作（RPA）框架，是一个用于在钉钉端内模拟操作页面的框架，属于钉钉 AI 插件体系的一员。通过拟人操作（RPA）框架，你只需要按照 API 的使用规范，即可完成脚本的开发。

## **快速开始**

```
const { lifecycle, page, utils } = DDAutomator;
const { loaded, step } = lifecycle;

loaded(async (params, done) => {
  await step('1/2 自动点击酒店', async () => {
    await utils.waitForMilliseconds(500);
    await page.getByText('酒店').click();
    done({
      buttonText: 'complete',
    });
  });
});
```

其中， DDAutomator 对象，由钉钉客户端运行时提供，因此开发者编写脚本代码时，不需要引入额外的 SDK。

目前，推荐使用[开发工具](0032-development-tools.md)进行自适应插件脚本的开发。

## **框架生命周期**

| **方法** | **说明** | **示例** |
| --- | --- | --- |
| loaded | 脚本的执行入口，可通过 params 获取注入到脚本内的参数 | ``` const { lifecycle } = DDAutomator;  const { loaded } = lifecycle;  loaded(async (params, done) => {   //    done({     title: '执行完毕',     message: '本次执行结果',   }); }); ``` |
| step | 标记定义脚本的每一步操作，框架会在每一步的时候自动处理日志和捕获异常。 | ``` const { lifecycle } = DDAutomator; const { loaded, step} = lifecycle;  loaded(async (params, done) => {    await step('第一步', async () => {     // ...   });    await step('第二步', async () => {     // ...   });    done({}); }); ``` |
| done | 目前支持两种模式：标准模式和自定义模式。    标准模式仅需要在第一个参数中传入`title`和`message`字段，用于展示标准的卡片信息。 | ``` const { lifecycle } = DDAutomator; const { loaded, step} = lifecycle;  loaded(async (params, done) => {    await step('第一步', async () => {     // ...   });    await step('第二步', async () => {     // ...   });    done({     title: '',     message: '',   }); }); ``` |
| 自定义模式支持传入第二个`options`参数，目前支持通过参数发送自定义卡片。  其中，`templateId`和`miniAppId`需先在卡片平台配置后获取。 | ``` const { lifecycle } = DDAutomator; const { loaded, step} = lifecycle;  loaded(async (params, done) => {   await step('第一步', async () => {     // ...   });    await step('第二步', async () => {     // ...   });    done({     title: '',     message: '',   }, {     custom: true,     templateId: 'abc',     miniAppId: '123'   }); }); ``` |

## **框架方法**

### **元素获取**

| **API** | **说明** | **格式和示例** |
| --- | --- | --- |
| getByRole | 通过 ARIA role 和可见 name 获取元素 | ``` await page.getByRole('button', { name: 'Sign In' }).click(); ``` |
| getByPlaceholder | 通过 input 或 textarea的 Placeholder 获取元素 | 格式：   ``` await page.getByPlaceholder(text:string, options?: {exact?: boolean }); ```  - text：定位元素所需要的文字内容 - options：是否完全匹配，默认 false   示例：   ``` await page.getByPlaceholder(text:string, options?: {exact?: boolean }); ``` |
| getByText | 通过元素的文字内容获取该元素 | 格式：   ``` await page.getByText(text: string, options) ```  - text：文字内容 - options：    - exact：是否完全匹配，默认 false   - classNames: 对应需要匹配的 classNames 数组   示例：   ``` await page.getByText('Hello', { exact: true, classNames: ['foo', 'bar'] }) ``` |
| getByClass | 通过 class 获取元素 | 格式：   ``` await page.getByClass(text: string, options?:{exact?:boolean}) ```  - text：class名称（备注：​class 名称前面无需加 `.`） - options：    - exact：是否完全匹配，默认false   示例：   ``` await page.getByClass(text: string, options?:{exact?:boolean}) ``` |
| getByAltText | 通过 alt 获取元素 | 格式：   ``` await page.getByAltText(text: string, options?:{exact?:boolean}) ```  - text：元素 altText 的内容 - options：    - exact：是否完全匹配，默认false   示例：   ``` await page.getByAltText(text: string, options?:{exact?:boolean}) ``` |
| getByLabel | - 通过 label 获取对应的 input 元素 - getByLabel 获取的不是 label 元素本身，而是其对应的 input 元素。 | 格式：   ``` await page.getByLabel(text: string, options?:{exact?:boolean}) ```  - text：label 元素的 for 值，也是其对应 input 元素的 id 值 - options：    - exact：是否完全匹配，默认 false   示例：   ``` await page.getByLabel(text: string, options?:{exact?:boolean}) ``` |
| getByTitle | 通过 title 属性获取元素 | 格式：   ``` await page.getByLabel(text: string, options?:{exact?:boolean}) ```  - text：title 的值 - options：    - exact：是否完全匹配，默认 false   示例：   ``` await page.getByLabel(text: string, options?:{exact?:boolean}) ``` |
| getByAttribute | 通过属性对应的 Key Value 获取元素 | 格式：   ```   await page.getByAttribute(key: string, value: string); ```  - key: 属性 Key 值； - value： 属性 Value；   示例：   ``` await page.getByLabel(text: string, options?:{exact?:boolean}) ``` |
| nth | 获取对应 Locator 下指定 Index 的元素 | 示例：   ``` await page.getByText('名称').nth(2); ``` |
| locator | 通用的 locator 方法，可以使用 CSS 选择器，例如 id 或者 class 选择器等获取对应元素 | ``` await page.locator('#id').click();  await page.locator('.foo').click(); ``` |
| all | 同步获取对应 locator 的所有元素，并可以对每个元素进行操作。 | ``` const items = await page.getByClass('class_name').all();  items.forEach(async (item) => {   await item.click(); }); ``` |
| setRoot | 用于指定根节点的元素，可以传入一个 selector，并在此基础上继续执行 locator | ``` await page.setRoot('#id').getByText('text').click(); ``` |
| getAncestorLocator | 根据层级来获取某个 locator 的祖先 locator | ``` await page.getAncestorLocator(page.getByClass('foo'), 2).getByClass('bar').click(); ``` |

### 执行动作

| **API** | **说明** | **格式和示例** |
| --- | --- | --- |
| click | 点击事件 | ``` await page.getByClass('foo').click(); ``` |
| fill | 填充 input 内容 | ``` await page.getByPlaceholder('Email address')           .fill('zy123@gmail.com'); ``` |
| focus | 获取元素并聚焦 | ``` await page.getByPlaceholder('请输入').focus(); ``` |

### 获取内容

| **API** | **说明** | **格式和示例** |
| --- | --- | --- |
| textContent | 获取文字内容，同 HTML 元素的 textContent，返回一个 string | ``` await page.getByRole('div').textContent(); ``` |
| innerHTML | 获取元素内部 HTML，同 HTML 的原生 innerHTML，返回一个 string | ``` await page.getByRole('foo').innerHTML(); ``` |
| innerText | 获取元素内部的文本内容，同 HTML 原生的 innerText，返回一个 string | ``` await page.getByRole('foo').innerText(); ``` |
| getAttribute | 通过属性的 key，获取元素对应的某个属性的值 | 示例：   ``` <img id="img" src="http://cdn.com/path/to/image" /> ```  ``` const imageUrl = await page.locator('#img').getAttribute('src'); ``` |

### 工具函数 Utils

| **API** | **说明** | **格式和示例** |
| --- | --- | --- |
| waitForMilliseconds | 等待指定的毫秒数 | ``` const { utils } = DDAutomator;  await utils.waitForMillisecond(500); ``` |
| waitForPage | 等待指定页面加载，支持字符串部分匹配、完全匹配以及正则表达式匹配 | ``` const { utils } = DDAutomator;  // 字符串，部分匹配 await utils.waitForPage('dingtalk.com'); // 字符串，完全匹配 await utils.waitForPage('dingtalk.com', { exact: true }); // 正则匹配 await utils.waitForPage(/^dingtal\.com/); ``` |
| hookOnce | 用于让插件跳过本身页面调用的 Native 交互 JSAPI，直接返回数据 | ``` const { utils } = DDAutomator; const { hookOnce } = utils;  await step('1/1 选择会话测试', async () => {   await hookOnce('biz.chat.chooseConversation', [     {       "id": "54289124794",       "isEnterpriseGroup": 1,       "title": "追求卓越（钉钉技术大群）",     },   ]);      // 调用JSAPI biz.chat.chooseConversation   await page.locator('#chooseConversationBtn').click(); }); ```   参数格式：   - apiName    - 类型：string   - 说明：需要跳过 Native 执行的 JSAPI 名称   - 示例：`biz.contact.complexPicker` - data    - 对应直接返回的 JSAPI 的结果数据 |
| getSystemInfo | 获取当前执行环境的操作系统信息 | ``` const { os } = await utils.getSystemInfo(); ```   返回值   - os：wind / mac / ios / android |

## **完整示例**

```
const { lifecycle, page, utils } = DDAutomator;
const { loaded, step } = lifecycle;

loaded(async (params, done) => {
  const { name } = params;

  await step('1. 输入搜索内容', async () => {
    await page.locator('#kw').fill(name);
  });
  await step('2. 点击搜索', async () => {
    await page.locator('#su').click();
  });

  await step('3. 获取第一条结果的标题', async () => {
    await utils.waitForMilliseconds(2000);
    const content = await page.getByClass('c-title').textContent();

    done({
      title: '搜索结束',
      message: content,
    });
  });
});
```
