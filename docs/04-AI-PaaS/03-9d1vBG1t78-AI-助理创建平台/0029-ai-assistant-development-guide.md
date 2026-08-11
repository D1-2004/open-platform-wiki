---
title: "开发指南"
source_url: "https://open.dingtalk.com/document/aipass/ai-assistant-development-guide"
namespace: "aipass"
slug: "ai-assistant-development-guide"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 能力 > 拟人操作（RPA） > 开发指南"
doc_id: "wByuJXAqam"
updated_at: "2025-12-08 16:00:33"
---

> Source: https://open.dingtalk.com/document/aipass/ai-assistant-development-guide
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 能力 > 拟人操作（RPA） > 开发指南
> Updated: 2025-12-08 16:00:33

# 开发指南

如果你需要开发拟人操作（RPA）脚本的 AI 能力，你可以参考本文档操作步骤完成开发。拟人操作要求钉钉APP v6.5.30 及以上版本。

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理**

## **背景信息**

本文将以官方**飞猪旅行预订机票**功能为例，描述如何通过拟人操作（RPA）脚本的方式开发 AI 能力。

**飞猪旅行预订机票**是钉钉 AI 助理的官方示例能力，当你向 AI 助理提出预订机票请求时，它能够识别出你希望查出发地、目的地和出发时间。接着，AI 助理将执行你预设的拟人操作（RPA）脚本，模仿用户浏览飞猪旅行站点，执行机票预订流程。最后，AI 助理会完成机票选择，最终到订单确认页面返回给提问者继续操作。

## **步骤一： 开发**拟人操作（RPA）**脚本**

首先你需要开发一个飞猪旅行预订机票的拟人操作（RPA）脚本， 我们以 JavaScript 代码为例。

```
const { lifecycle, page, utils } = DDAutomator;
const { loaded, step } = lifecycle;

(async () => {
  loaded(async (params, done) => {
    await utils.waitForMilliseconds(4000);
    if (await page.getByText("登录", { exact: true }).exists()) {
      await utils.waitForPage(
        "https://market.m.taobao.com/app/trip/h5-traffic-search/pages/search/index.html"
      );
      await utils.waitForMilliseconds(3000);
    }
    await step("第1步：选择出发地", async () => {
      await page.locator(".stop.from").click();
      await utils.waitForMilliseconds(2000);
      await page.getByText(params.startCity, { exact: true }).click();
    });
    await utils.waitForMilliseconds(2000);
    await step("第2步：选择到达地", async () => {
      await page.locator(".stop.to").click();
      await utils.waitForMilliseconds(2000);
      await page.getByText(params.endCity, { exact: true }).click();
    });
    await utils.waitForMilliseconds(2000);
    await step("第3步：选择日期", async () => {
      await page.getByClass("date-wrapper").click();
      await utils.waitForMilliseconds(2000);
      const year = params.date.split("-")[0].trim();
      const month = params.date.split("-")[1].replace(/^0/, "").trim();
      const day = params.date.split("-")[2].replace(/^0/, "").trim();
      await page
        .setRoot(`[data-month-str="${year}年${month}月"]`)
        .getByText(day, { exact: true })
        .click();
    });
    await utils.waitForMilliseconds(2000);
    await step("第4步：搜索机票", async () => {
      await page.getByText("搜索机票", { exact: true }).click();
    });
    await utils.waitForMilliseconds(6000);
    await step("第5步：选择机票", async () => {
      await page.locator(".rax-view-v2.flight-card-info-main-right").click();
    });
    await utils.waitForMilliseconds(6000);
    await step("第6步：确认预订", async () => {
      await page.getByText("订", { exact: true }).click();
    });
    done({
      title: "运行完成",
      message: "点击去支付",
    });
  });
})();
```

开发钉钉拟人操作（RPA）脚本依赖 DDAutomator 框架，详情参见 [DDAutomator 框架](0030-the-ddautomator-framework.md)。

## **步骤二: 编写拟人操作（RPA）描述文件**

以飞猪旅行预订机票为例，根据拟人操作（RPA）协议规范配置出入参和 URL 信息，描述协议详情参考[描述协议](0031-adaptive-plug-in-description-protocol-1.md)。

- 如果你已经有现成的脚本 CDN 地址，可手动配置描述文件：

```
{
    "title": "飞猪旅行预订机票",
    "description": "需要预订机票时使用",
    "keywords":
    [
        "预定机票",
        "订机票",
        "机票",
        "预订"
    ],
    "actions":
    {
        "飞猪旅行预订机票":
        {
            "summary": "飞猪旅行预订机票",
            "description": "机票预订，飞猪旅行，预订机票，需要预订机票时使用",
            "input_param":
            {
                "type": "object",
                "description": "",
                "properties":
                {
                    "startCity":
                    {
                        "type": "string",
                        "description": "出发城市",
                        "x-dingtalk-display-name": "出发城市"
                    },
                    "endCity":
                    {
                        "type": "string",
                        "description": "到达城市",
                        "x-dingtalk-display-name": "到达城市"
                    },
                    "date":
                    {
                        "type": "string",
                        "description": "出发日期",
                        "x-dingtalk-default": "2023-11-29",
                        "x-dingtalk-display-name": "出发日期",
                        "x-dingtalk-entity":
                        {
                            "category": "time",
                            "format": "strftime: yyyy-MM-dd"
                        }
                    }
                },
                "required":
                [
                    "startCity",
                    "endCity",
                    "date"
                ]
            },
            "target_url_by_platform":
            {
                "default": "https://market.m.taobao.com/app/trip/h5-traffic-search/pages/search/index.html"
            },
            "script_url": "https://opencdn.dingtalk.net/vscode/457116/595734833/bdbca7da-e441-4c9a-ab06-205ef217eb49_automator.js",
            "keywords":
            [
                "预定机票",
                "订机票",
                "机票",
                "预订"
            ],
            "examples":
            [
                {
                    "input": "帮我预订一张下周二的机票，出发地：成都，到达地：广州",
                    "output":
                    {
                        "startCity": "成都",
                        "endCity": "广州",
                        "date": "下周二"
                    }
                },
                {
                    "input": "预订一张明天的机票，从北京到杭州",
                    "output":
                    {
                        "endCity": "杭州",
                        "date": "明天"
                    }
                }
            ],
            "headless_mode": false,
            "target_valid_domains":["market.m.taobao.com"],
            "support_platform":
            [
                "android",
                "ios"
            ]
        }
    }
}
```

- 你也可通过工具快速生成拟人操作（RPA）描述文件，详情参见[开发工具](0032-development-tools.md)。

## **步骤三: 填写拟人操作（RPA）描述文件**

将上述描述文件内容拷贝粘贴到文本框编辑，单击保存即可完成自定义能力的创建。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2663716171/p800998.png)

## **相关文档**

- [DDAutomator 框架](0030-the-ddautomator-framework.md)
- [描述协议](0031-adaptive-plug-in-description-protocol-1.md)
- [开发工具](0032-development-tools.md)
