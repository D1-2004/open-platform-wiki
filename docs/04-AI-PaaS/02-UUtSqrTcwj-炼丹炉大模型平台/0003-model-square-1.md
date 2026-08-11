---
title: "操作指南"
source_url: "https://open.dingtalk.com/document/aipass/model-square-1"
namespace: "aipass"
slug: "model-square-1"
group: "AI PaaS"
tab: "炼丹炉大模型平台"
breadcrumb: "操作指南"
doc_id: "hlV0uqVr76"
updated_at: "2026-05-22 18:12:48"
---

> Source: https://open.dingtalk.com/document/aipass/model-square-1
> Path: AI PaaS / 炼丹炉大模型平台 / 操作指南
> Updated: 2026-05-22 18:12:48

# 操作指南

## **模型广场**

### **前提条件**

- 操作人必须是当前企业的子管理员并且拥有开发者权限。

### **操作步骤**

1. 登录企业[开发者后台](https://open-dev.dingtalk.com/)。
2. 进入模型广场页面。
3. 该页面以大模型所属厂商为单位作为展示，鼠标悬停其中一个卡片的体验按钮，可选择某个模型进行在线体验。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6026129171/p813588.png)

## **体验中心.**

### **前提条件**

- 操作人必须是当前企业的子管理员并且拥有开发者权限。

### **操作步骤**

1. 登录企业[开发者后台](https://open-dev.dingtalk.com/)。
2. 进入体验中心页面。
3. 选择1-3个大模型，点击授权后，勾选并点击确定。

   > **[!NOTE]**
   >
   > 如果在炼丹炉内已训练了企业专属模型，也可在“我的专属模型”中进行勾选。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9126129171/p813604.png)
4. 输入任意问题，即可体验不同模型的效果。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9126129171/p813609.png)
5. 可查看每个模型的答案耗时时长、输入tokens数量和输出tokens数量。

## **我的模型**

### **模型类型**

我的模型界面内，目前共包含以下模型类型：

| **模型类型** | **含义** | **相关操作** |
| --- | --- | --- |
| 公共模型 | 在体验中心授权之后的公共大模型 | API调用&钉钉AI助理内使用 |
| 专属模型 | 在炼丹炉内训练得到的专属模型 | API调用&钉钉AI助理内使用 |
| 多模态 | 暂未上线 | —— |

### **操作步骤**

1. 点击AIP文档，可按照API文档调用相关模型服务。
2. 点击使用范围，设置该模型服务的使用范围，被选中的员工，可以在创建AI助理时，切换该大模型用于智能回复和知识库问答。详情步骤参考[快速入门](0002-switch-the-model-of-the-ai-assistant-1.md)。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3326129171/p813619.png)
3. 点击关闭使用，在体验中心内，该大模型不能在线体验，需要重新授权。

## **模型训练**

### **知识问答**

知识问答的目的是根据用户的自然语言输入，使大模型完成针对性的内容输出。通常可用于智能问答和智能写作场景。

通常要实现良好的知识创作效果，需要经过Pretrain、SFT和RLHF训练三个流程。

#### **前提条件**

- Pretrain训练，需要已完成泛文本数据集的创建。
- SFT训练，需要已完成文本对话无排序数据集的创建。

  > **[!NOTE]**
  >
  > SFT训练的文本对话无排序数据集，需要来自Pretrain训练时使用的泛文本产生的QA问答对
- RLHF训练，需要已完成文本对话包含排序数据集的创建。

#### **操作步骤**

1. 进入炼丹炉平台的模型训练-知识问答页面​。
2. Pretrain训练。

   - 填写基础信息，包含自定义模型ID、模型名称、选择基础模型、选择泛文本数据集

     > **[!NOTE]**
     >
     > - 自定义模型ID只能由小写字母、数字和 - 组成且开头必须使用小写字母，不能出现连续的 -，结尾不能使用 -，不超过20个字符
     > - Pretrain训练阶段，只支持泛文本类型数据集

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3276129171/p813653.png)
   - 点击左下角**开始训练**

     > **[!NOTE]**
     >
     > Pretrain训练完成后，点击发布上线，可在线试用效果，如果达不到预期效果，可继续使用SFT训练。
3. SFT训练。

   - 完成Pretrain训练后，在模型管理中，点击修改按钮，进入Pretrain训练信息查看页面![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3276129171/p813761.png)
   - 查看Pretrain训练信息，点击下一步，进入SFT训练![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3276129171/p813762.png)
   - 选择相应的SFT训练数据集，该训练集内容需要是来自Pretrain训练时使用的泛文本产生的QA问答对

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3276129171/p813764.png)
   - 点击开始训练，可在我的模型-专属模型页面中查看进度![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3276129171/p813765.png)

     > **[!NOTE]**
     >
     > SFT训练完成后，点击发布上线，可在线试用效果，如果达不到预期效果，可继续使用RLHF训练。
4. RLHF训练。

   - SFT训练完成后，点击修改按钮![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3276129171/p813807.png)
   - 此处点击下一步，进入RLHF训练![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3276129171/p813810.png)
   - 选择文本对话含排序数据集，点击开始训练![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3276129171/p813811.png)

### **数据查询**

数据查询的目的是将用户的自然语句转为可以执行的 SQL 语句，例如：

输入：查询一下三班的平均分。

回复：SELECT AVG(score) FROM table\_name WHERE class = 3;

#### **操作步骤**

1. 进入炼丹炉平台的模型训练-数据查询页面​。
2. 填写基础配置，模型ID和模型名称。

   > **[!NOTE]**
   >
   > 自定义模型ID只能由小写字母、数字和 - 组成且开头必须使用小写字母，不能出现连续的 -，结尾不能使用 -，不超过20个字符

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0476129171/p813738.png)
3. 填写知识样例配置，可参考下方表格中的说明。

   | **配置项** | **说明** | **是否必填** | **示例** |
   | --- | --- | --- | --- |
   | 配置数据表名称 | 业务数据表的表名。 | 是 | user\_info |
   | 配置表结构 | 录入表格的字段名称（英文名称）、字段别名（中文名称）、字段类型、字段描述等信息。 | 是 | image.png |
   | 录入领域知识 | 领域知识是指业务场景下的特定知识，比如专有词汇等，可单条逐个录入也可通过文件批量上传录入。 | 否 | image.png |
   | 上传样例数据 | 样例是一些问答对，用于模型的训练和后续的参考样例库的构建。 | 是 | image.png |
   | 添加约束维度 | 添加指定的约束。  - 条件约束，规定操作的条件范围。 - 数量约束，规定操作的数量范围。 | 否 | image.png |
4. 选择训练方式。

   > 数据模型训练的底模型是钉钉开放平台提供的​NL2SQL专用模型，该模型是使用SQL能力数据基于开源MPT-7B底座模型通过指令微调得到的专属领域模型，基于NL2SQL能力模型继续进行微调要比直接基于开源通用模型效果要好。**​**

   | **训练方式** | **是否消耗训练token** | **是否消耗算力单元** |
   | --- | --- | --- |
   | 仅Prompt学习 | 是 | 否 |
   | Prompt学习+模型训练 | 是 | 是 |
5. 点击左下角**开始训练**。​

#### **后续步骤**

智能用数模型开始训练后，会跳转到“我的模型”-“专属模型”页面，查看模型训练的进度。

### **自动填表**

自动填表的目的是根据用户的自然语言输入，抽取其中的内容，并填充到规定的Json结构中返回。通常用于连接用户和应用系统，作为用户自然语言输入指导应用系统工作的中间桥梁。

#### **操作步骤**

1. 进入炼丹炉平台的模型训练-自动填表页面​。
2. 填写基础配置。

   > **[!NOTE]**
   >
   > 自定义模型ID只能由小写字母、数字和 - 组成且开头必须使用小写字母，不能出现连续的 -，结尾不能使用 -，不超过20个字符

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0540565071/p759653.png)
3. 填写指令集配置**。**

   - **指令集通用知识。**填写指令集中所有指令通用的描述，作用是提升大模型路由的准确性。每条知识可填写不超过200个字符。例如：宜搭是阿里巴巴钉钉的低代码平台。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7576129171/p813757.png)
   - **单次调用是否有上下文配置。**

     - **是：**需要填写上下文内容，作用是针对某次调用，可在本次调用时，添加上下文信息。例如，当前的应用结构为${app\_struct}。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7576129171/p813758.png)
     - **否：**无需填写。
   - **指令集配置**。设置指令的名称，配置指令的参数定义，并上传样例。  
     ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3270159961/p731658.png)​

     - 指令名称一般规定为具有语义的单词短语（中英均可），避免使用语义较泛的单词短语，避免使用领域内、口语化的单词。
     - 指令的定义需填写该指令下的参数名称、字段名称、字段类型、字段描述和字段值。

       - 【必填】参数名称建议用具有语义的英文单词，避免使用语义较泛的单词短语，避免使用领域内、口语化的单词。
       - 【必填】字段名称为简短的参数名称翻译，中英文均可。
       - 【必填】字段类型可以选择为string、number、array、object、boolean。目前对于单层JSON的支持效果较好，建议尽量少用object类型的字段配置，可将其中的内容提出到外层配置。
       - 【可选】字段描述为参数的简单语义解释。
       - 【可选】字段值主要用于填写枚举范围，用英文逗号分隔
   - **添加样例**。手动输入样例，每条样例包含输入和输出两个部分内容。样例将作为训练样本实际训练模型。

     - 输入是当前指令下具有代表性的用户输入。
     - 输出是用户输入在当前指令的配置下的预期输出。必须包含所有定义的参数字段，若某个字段在当前输入中没有对应取值，则字段值为null。  
       ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3270159961/p731657.png)
4. 选择训练方式。  
   指令模型训练的底模型是钉钉开放平台提供的​NL2Frame专用模型，该模型是使用​NL2Frame能力数据基于开源MPT-7B底座模型通过指令微调得到的专属领域模型，基于​NL2Frame能力模型继续进行微调要比直接基于开源通用模型效果要好。**​**

   | **训练方式** | **是否消耗训练token** | **是否消耗算力单元** |
   | --- | --- | --- |
   | 仅Prompt学习 | 是 | 否 |
   | Prompt学习+模型训练 | 是 | 是 |
5. 点击左下角**开始训练**。​

#### **后续步骤**

智能指令模型开始训练后，可跳转到“我的模型”-“专属模型”页面，查看模型训练的进度。
