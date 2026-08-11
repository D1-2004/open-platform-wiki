---
title: "如何使用代码模式"
source_url: "https://open.dingtalk.com/document/aipass/how-to-use-code-patterns"
namespace: "aipass"
slug: "how-to-use-code-patterns"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 工作流 > 执行动作 > 公式编辑 > 如何使用代码模式"
doc_id: "40E12RSsNJ"
updated_at: "2025-09-23 19:20:09"
---

> Source: https://open.dingtalk.com/document/aipass/how-to-use-code-patterns
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 工作流 > 执行动作 > 公式编辑 > 如何使用代码模式
> Updated: 2025-09-23 19:20:09

# 如何使用代码模式

如果你是第一次使用公式编辑的代码模式，请了解如何在[创建组织内使用的 AI 助理](0005-create-a-dingtalk-ai-assistant-1.md)时进入 AI 技能添加页面，本文档内容将帮助你快速体验代码模式能力。

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理/助理市场创建的 AI 助理**

## 明确需求

利用工作流查询商品，并计算出商品去掉最高价和最低价之后的平均值。

## **操作步骤**

1. 在技能市场中，单击**商品采购**，选择 1688 商品搜索，并完成添加操作。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4965329171/p813972.png)
2. 添加**发送消息**执行动作：

   1. 添加技能成功后，进入新建工作流页面，单击“⊕”，新增执行动作节点。
   2. 在步骤 4 中，选择选择**卡片** > **发送消息**执行动作。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4965329171/p813973.png)
   3. 在发送消息的自定义消息内容中，单击 “⊕” > 使用公式编辑。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4965329171/p813974.png)
   4. 选择代码模式，你必须使用`main`函数作为脚本的主函数，工作流在运行过程中会使用该函数的返回值作为结果填入参数。

      在输入框中键入如下代码：

      ```
      def main():
          # 1. 将价格文字转为数字
          prices = [float(x) for x in _ctx_node_['''$.dingtalk_flow_d39f_0771.payload[*].price''']]
          # 2. 价格从低到高排序
          prices = sorted(prices)
          # 3. 去除最低价
          if prices: prices.pop(0)
          # 4. 去除最高价
          if prices: prices.pop()
          # 5. 计算均价
          return sum(prices) / len(prices)
      ```

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4965329171/p813975.png)

      设置完成后，单击右下角确认。
3. 设置完成后，单击保存并启用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4965329171/p813976.png)
4. 此时，你已经返回到 AI 助理创建页面，你可以单击右上角保存按钮，在调试区在与 AI 助理对话：为我查询100-300区间的耳机。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4965329171/p813977.png)

   此时，你可以得到商品的均价结果。

## **版本参考**

### **所采用的库版本概览**

#### **Core Dependencies**

- **BeautifulSoup4**: 版本号4.12.3
- **Jsonpath-ng**: 版本1.6.1
- **Lxml**: 版本5.2.2
- **Soupsieve**: 版本2.5
- **Cryptography**: 版本42.0.8
- **Pandas**: 版本2.2.1
- **numpy**==1.23.2
