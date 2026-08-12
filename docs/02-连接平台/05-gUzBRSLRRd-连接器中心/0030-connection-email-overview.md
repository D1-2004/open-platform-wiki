---
title: "介绍"
source_url: "https://open.dingtalk.com/document/connection/connection-email-overview"
namespace: "connection"
slug: "connection-email-overview"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "三方连接器 > 介绍"
doc_id: "lpVeXLMXho"
updated_at: "2026-07-30 09:19:33"
---

> Source: https://open.dingtalk.com/document/connection/connection-email-overview
> Path: 连接平台 / 连接器中心 / 三方连接器 > 介绍
> Updated: 2026-07-30 09:19:33

# 介绍

## **邮箱**

连接平台提供了QQ、163、阿里云、钉钉四种邮箱连接器，用户可根据需求选取适合的邮箱连接器，发送邮件。

### **执行动作**

#### **QQ邮箱**

| **模块** | **核心能力** |
| --- | --- |
| 发送邮件 | 以用户设定的QQ邮箱发送邮件。 |

#### **163邮箱**

| **模块** | **核心能力** |
| --- | --- |
| 发送邮件 | 以用户设定的163邮箱发送邮件。 |

#### **钉邮**

| **模块** | **核心能力** |
| --- | --- |
| 发送邮件 | 以用户设定的钉钉邮箱发送邮件。 |

#### **阿里邮箱**

| **模块** | **核心能力** |
| --- | --- |
| 企业邮箱发送邮件 | 以企业管理员设定的阿里云企业邮箱发送邮件。 |
| 个人邮箱发送邮件 | 以用户设定的阿里云个人企业邮箱发送邮件。 |

### **参数说明**

#### **鉴权凭证**

邮箱连接器使用前需要先添加凭证，即发送邮件的邮箱账号与授权码，注意此处的授权码不一定是邮箱密码，相关字段的获取方式点击链接查看详情。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2052576371/p903409.png)

#### **发送邮件**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| 收件人 | Array(String) | 是 | 邮件接受人的邮箱地址（xxxxxx@xxx.xxx） |
| 标题 | String | 是 | 邮件标题 |
| 邮件正文 | String | 是 | 邮件正文内容 |
| 邮件正文类型 | String | 是 | 邮件正文类型  纯文本：邮件中所有内容以文本格式展示  HTML：邮件中若有url地址以链接方式展示 |
| 正文字符编码 | String | 是 | 目前只支持 UTF-8 |
| 附件列表 | Array(Object) |  |  |
| 附件名称 |  | 是 | 附件 |
| 附件网络地址 |  | 是 | 附件url地址需要公网能访问，部分url存在防爬等问题，需另做处理 |
| 附件类型 |  | 是 | 下拉选择支持的附件类型 |
| 附件头部 |  |  | JSON Key-Value结构 |

#### **参数举例**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2052576371/p903510.png)

对应邮箱收到来自用户鉴权中配置的 QQ 邮箱的一封邮件。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2052576371/p903514.png)

## **抖音**

抖音（国际版称为TikTok）是一款音乐创意短视频社交软件，由中国的字节跳动公司（ByteDance）孵化。它是一个面向全年龄的短视频社区平台，用户可以通过这款软件选择歌曲，拍摄音乐作品形成自己的作品。是数字文化和网络趋势的一个主要发源地，并且对流行文化有着显著的影响。抖音在中国非常受欢迎，而它的国际版本TikTok也在全球范围内赢得了大量的用户。

### **场景说明**

抖音为用户和创作者提供了一个丰富多彩、互动性强的平台，通过短视频内容的形式允许不同背景和兴趣的人们进行创作、分享和连接，提供了多样化的应用场景，主要包括：

- 娱乐消遣：用户在空闲时间浏览各种短视频来娱乐放松。视频内容涵盖舞蹈、搞笑、旅行、宠物等多种类别。
- 社交互动：用户可以通过点赞、评论、分享视频来与创作者或其他观众互动。同时，用户还可以关注感兴趣的创作者，建立自己的社交网络。
- 内容创作：创作者利用抖音发布自己的短视频作品，展现才艺，如唱歌、跳舞、演奏乐器等，以此吸引粉丝和关注。
- 个人品牌建设：当创作者拥有一定的粉丝基础后，可以构建和发展个人品牌，通过不同的内容来塑造个人形象和特色。
- 教育与学习：抖音上有许多教育性质的内容，如语言学习、科学知识、历史事实、技能教学等，用户可以通过观看相关视频来学习新知识。
- 营销推广：企业和个体商家使用抖音作为营销工具来推广产品和服务，通过创建吸引人的视频内容或与知名创作者合作来吸引潜在顾客。
- 参与挑战与话题：用户可以参与抖音平台上流行的挑战或话题标签，制作相关主题的视频，与更广泛的社区成员互动。
- 直播互动：创作者和名人进行直播，与观众实时互动，分享日常生活、进行才艺表演，甚至通过直播进行商品展销。
- 才艺展示：一些用户利用抖音展示自己的特殊才艺或兴趣爱好，比如绘画、手工制作、烹饪技巧等。
- 文化交流：因抖音用户遍布全球，人们通过这个平台分享和了解不同国家和地区的文化、风俗和生活方式。

### **执行动作**

如需查看更多信息，请前往[抖音](https://open-dev.dingtalk.com/fe/connector?spm=ding_open_doc.document.0.0.18684a70Pr7ppX&hash=%23%2Fmarket%2Fconnector%2FG-CONN-101FE4A43BB82103E8CE000F%3FcorpId%3Dding3b2e428dfde07ac7ffe93478753d9884#/market/connector/G-CONN-101FE4A43BB82103E8CE000F?corpId=ding3b2e428dfde07ac7ffe93478753d9884)连接器详情中查看。

| **模块** | **核心能力** |
| --- | --- |
| 获取用户公开信息 | 该接口获取用户的抖音公开信息，包含昵称和头像。 |
| 查询视频列表 | 该接口用于分页获取用户所有视频的数据，返回的数据是实时的。 |
| 查询评论列表 | 该接口用于获取视频评论列表。 |
| 获取直播间基础数据 | 该接口用于获取直播间房间维度基础数据。 |
| 获取直播间看播数据 | 该接口用于获取直播间看播维度数据。 |
| 获取抖音星图达人指数 | 该接口用于查询抖音星图达人相关数据。【调用接口给用户展示时必须带有【星图指数】或【星图达人榜】字样】。 |

### **参数说明**

> **[!NOTE]**
>
> 抖音开放平台的 OAuth API 与 其他功能 API，域名为`https://open.douyin.com`。

#### **获取用户公开信息**

| **入参** | **类型** | **是否必填** | **详细说明** |
| --- | --- | --- | --- |
| access\_token | string | 是 | 调用[获取 access\_token](https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/account-permission/get-access-token)获取，此 token 需要用户授权。 |
| open\_id | string | 是 | 调用[获取 access\_token](https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/account-permission/get-access-token)获取，用户唯一标识。 |

#### **查询视频列表**

| **入参** | **类型** | **是否必填** | **详细说明** |
| --- | --- | --- | --- |
| open\_id | string | 是 | 调用[获取 access\_token](https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/account-permission/get-access-token)获取，用户唯一标识。 |
| cursor | i64 | 否 | 分页游标, 第一页请求 cursor 是 0, response 中会返回下一页请求用到的 cursor , 同时 response 还会返回 has\_more 来表明是否有更多的数据。 |
| count | i32 | 是 | 每页数量。 |

#### **查询评论列表**

| **入参** | **类型** | **是否必填** | **详细说明** |
| --- | --- | --- | --- |
| open\_id | string | 是 | 调用[获取 access\_token](https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/account-permission/get-access-token)获取，用户唯一标识。 |
| cursor | i64 | 否 | 分页游标, 第一页请求 cursor 是 0, response 中会返回下一页请求用到的 cursor , 同时 response 还会返回 has\_more 来表明是否有更多的数据。 |
| count | i32 | 是 | 每页的数量，最大不超过 20，最小不低于 1。 |
| item\_id | string | 是 | 视频id。 |
| sort\_type | string | 否 | 列表排序方式，不传默认按推荐序，可选值：time(时间逆序)、time\_asc(时间顺序)。 |

#### **获取直播间基础数据/看播数据**

| **入参** | **类型** | **是否必填** | **详细说明** |
| --- | --- | --- | --- |
| open\_id | string | 是 | 调用[获取 access\_token](https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/account-permission/get-access-token)获取，用户唯一标识。 |
| live\_id | int64 | 是 | 业务线id：   - 1：抖火 - 3：西瓜头条 |
| room\_id | int64 | 是 | 房间id。 |

#### **获取抖音星图达人指数**

| **入参** | **类型** | **是否必填** | **详细说明** |
| --- | --- | --- | --- |
| open\_id | string | 是 | 调用[获取 access\_token](https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/account-permission/get-access-token)获取，用户唯一标识。 |

### **使用教程**

- [将抖音多条视频列表数据同步到多维表](0031-synchronize-multiple-dimensional.md)

## **1688**

1688 开放平台，依托 B2B 海量用户资源以及强大的平台优势，是为阿里巴巴买卖家提供开放服务的重要平台，帮助商家提升经营能力、拓宽生意渠道、提高办公效率；帮助买家提升选品、下单效率，降低采购成本等。

1688 致力于为企业构建智能经营服务网络，开放和集成企业经营生命周期所需的专业服务，解决企业经营问题。赋能生态伙伴以灵活、安全及低成本形式进行系统对接，信息互联。

### **执行动作**

| **模块** | **核心能力** |
| --- | --- |
| 根据关键词搜索类目 | 查询关键词在1688平台上对应的类目ID。 |
| 采购商品比价 | 根据商品关键词、类目、采购量、价格区间等信息获取一定范围内的供应商报价。 |

### **参数说明**

#### **根据关键词搜索类目**

| **入参** | **类型** | **是否必填** | **详细说明** |
| --- | --- | --- | --- |
| appkey | String | 是 | 企业入驻1688平台创建应用时产生的应用鉴权标识。 |
| keyword | String | 是 | 关键词。 |

#### **采购商品比价**

| **入参** | **类型** | **是否必填** | **详细说明** |
| --- | --- | --- | --- |
| appkey | String | 是 | 企业入驻1688平台创建应用时产生的应用鉴权标识。 |
| scenario | String | 是 | 场景，默认填all。 |
| param | Object | 是 | 跨境关键词搜索参数。 |
| keywords | String | 是 | 关键词，示例值：帐篷。 |
| categoryIds | Array<String> | 是 | 限定类目ID列表，示例值：["201901404"]。 |
| quantityBegin | Long | 是 | 起批量，示例值：2。 |
| priceStart | String | 是 | 价格区间过滤，起始价格，示例值：10。 |
| priceEnd | String | 是 | 价格区间过滤，终止价格，示例值：100。 |
| sortType | String | 是 | 排序字段，price 价格排序，va\_rmdarkgmv30rt 30天成交额排序。 |
| sortOrder | String | 是 | 降序desc还是升序asc，默认不传算法排序。 |
| filter | Array<String> | 是 | 过滤参数，shipIn48Hours（48小时发货），freeExchange7days（7天包换），powerMerchant（实力商家），crossPotential(跨境潜力商品)，ttpft(批发团商品)，jxhy(精选货源商品)。 |
| pageSize | Long | 是 | 翻页大小，最大支持100，示例值：20。 |
| pageNum | Long | 是 | 当前页，示例值：1。 |

### **使用教程**

- [查询指定类目价格最低的三家供应商和报价信息](0032-query-quotation-information.md)

## **金蝶云星空**

金蝶云星空融合了当代尖端的管理理念与海量国内客户的优秀应用经验，专为实行事业部制、拥有多地点和多工厂运营的协同及管控型企业和集团公司量身打造，提供一个全面的ERP服务平台。云星空涵盖了广泛的协同应用功能，包括但不限于：中心化/分散化销售、采购策略、B2B电子商务管理、B2C电商平台、供应商协同合作、多工厂生产计划、跨工厂物料配送、加工作业、工厂间的物资调转、内部交易与结算、集团财务管理，以及阿米巴经营模式等。云星空不仅提高了业务效率，还增强了企业运营的灵活性和市场响应速度，帮助企业在激烈的市场竞争中保持领先地位。

### **场景说明**

金蝶云星空作为一款企业级的云服务平台，适用于多种企业运营和管理场景，大体包括：

- **财务管理**：云星空提供一套完整的财务管理解决方案，支持会计处理、财务报表、资金管理等功能，适用于需要改善财务透明度和效率的企业。
- **人力资源管理**：云星空包含人力资源规划、员工档案管理、薪酬福利管理、考勤管理以及招聘和培训管理等模块，适用于需要优化人力资源流程的企业。
- **供应链管理**：适用于需要改进供应链效率、库存管理、采购计划、订单管理和物流跟踪的企业。
- **客户关系管理（CRM）**：适用于需要管理客户信息、销售机会、营销活动和客户服务的企业。
- **生产管理**：适用于制造业企业，支持生产计划、工艺管理、质量控制和设备维护等功能。
- **项目管理**：云星空提供项目计划、资源分配、进度跟踪和成本控制等工具，适用于需要项目管理的服务型或工程类企业。
- **电子商务**：适用于需要整合线上和线下销售渠道、管理电商平台及提升电商运营效率的企业。
- **多工厂管理**：适用于具有多个生产基地需要协同管理生产活动的制造企业。
- **跨国运营**：适用于跨国企业需要集中管理财务、运营并遵守当地法规的场景。
- **决策支持**：云星空提供数据分析和大数据处理功能，帮助企业从大量数据中提取有价值信息，为决策提供支持。

### **执行动作**

| **模块** | **核心能力** |
| --- | --- |
| 基础资料-暂存客户 | 暂存接口是统一的，不同模块内容的保存，入参中的Model对象下的字段有所不同。 |
| 基础资料-保存客户 | 保存接口是统一的，不同模块内容的保存，入参中的Model对象下的字段有所不同。 |
| 提交 | 提交接口是统一的，可适用于不同模块，比如基础管理下的客户、薪资项、会计政策、银行等，供应链下的联系人、采购合同、采购订单、采购调价表等。 |
| 审核 | 审核接口是统一的，可适用于不同模块。 |
| 反审核 | 反审核接口是统一的，可适用于不同模块。 |
| 编码操作（禁用、反禁用） | 编码操作接口是统一的，可适用于不同模块。 |
| 撤销 | 撤销接口是统一的，可适用于不同模块。 |
| 删除 | 删除接口是统一的，可适用于不同模块。 |
| 查看 | 查看接口是统一的，可适用于不同模块。 |
| 单据查询 | 单据查询接口是统一的，可适用于不同模块。 |

### **参数说明**

#### **基础资料-暂存客户、保存客户**

| **入参** | **类型** | **是否必填** | **示例值** | **详细说明** |
| --- | --- | --- | --- | --- |
| formid | String | 是 | BD\_Customer | 业务对象表单Id，字符串类型。 |
| data | Object | 是 |  | JSON格式数据（详情参考JSON格式数据）。 |
| NeedUpDateFields | Array | 否 | [] | 需要更新的字段，数组类型，格式：[key1,key2,...] 。  **[!NOTE]**  更新字段时Model数据包中必须设置内码，若更新单据体字段还需设置分录内码。 |
| NeedReturnFields | Array | 否 | [] | 需返回结果的字段集合，数组类型，格式：[key,entitykey.key,...]。  **[!NOTE]**  返回单据体字段格式：entitykey.key |
| IsDeleteEntry | bool | 否 | true | 是否删除已存在的分录，布尔类型，默认true。 |
| SubSystemId | String | 否 |  | 表单所在的子系统内码，字符串类型。 |
| IsVerifyBaseDataField | bool | 否 | false | 是否验证所有的基础资料有效性，布尔类，默认false。 |
| IsEntryBatchFill | bool | 否 | true | 是否批量填充分录，默认true。 |
| ValidateFlag | bool | 否 | true | 是否验证数据合法性标志，布尔类型，默认true。  **[!NOTE]**  设为false时不对数据合法性进行校验 |
| NumberSearch | bool | 否 | true | 是否用编码搜索基础资料，布尔类型，默认true。 |
| IsAutoAdjustField | bool | 否 | false | 是否自动调整JSON字段顺序，布尔类型，默认false。 |
| InterationFlags | String | 否 |  | 交互标志集合，字符串类型，分号分隔，格式："flag1;flag2;..."，例如：允许负库存标识：STK\_InvCheckResult。 |
| IgnoreInterationFlag | String | 否 |  | 是否允许忽略交互，布尔类型，默认true。 |
| IsControlPrecision | bool | 否 | false | 是否控制精度，为true时对金额、单价和数量字段进行精度验证，默认false。 |
| ValidateRepeatJson | bool | 否 | false | 校验Json数据包是否重复传入，一旦重复传入，接口调用失败，默认false。 |
| Model | Object | 是 | {} | 表单数据包，JSON类型。 |
| FCreateOrgId | Object | 是 | {} | 创建组织， |
| FNumber | String | 否 |  | 客户编码。 |
| FUseOrgId | Object | 否 | {} | 使用组织。 |
| FName | String | 是 |  | 客户名称。 |
| FShortName | String | 否 |  | 简称。 |
| FCOUNTRY | Object | 否 | {} | 国家。 |
| FPROVINCIAL | Object | 否 | {} | 地区。 |
| FADDRESS | String | 否 |  | 通讯地址。 |
| FZIP | String | 否 |  | 邮政编码。 |
| FWEBSITE | String | 否 |  | 公司网址。 |
| FTEL | String | 否 |  | 联系电话。 |
| FFAX | String | 否 |  | 传真。 |
| FCompanyClassify | Object | 否 | {} | 公司类别。 |
| FCompanyNature | Object | 否 | {} | 公司性质。 |
| FCompanyScale | Object | 否 | {} | 公司规模。 |
| FINVOICETITLE | String | 否 |  | 发票抬头。 |
| FTAXREGISTERCODE | String | 否 |  | 纳税登记号。 |
| FINVOICEBANKNAME | String | 否 |  | 开户银行。 |
| FINVOICETEL | String | 否 |  | 开票联系电话。 |
| FINVOICEBANKACCOUNT | String | 否 |  | 银行账号。 |
| FINVOICEADDRESS | String | 否 |  | 开票通讯地址。 |
| FSUPPLIERID | Object | 否 | {} | 对应供应商。 |
| FIsGroup | bool | 否 | false | 集团客户。 |
| FIsDefPayer | bool | 否 | false | 默认付款方。 |
| FCustTypeId | Object | 否 | {} | 客户类别。 |
| FGROUPCUSTID | Object | 否 | {} | 对应集团客户。 |
| FGroup | Object | 否 | {} | 客户分组。 |
| FTRADINGCURRID | Object | 是 | {} | 结算币别。 |
| FCorrespondOrgId | Object | 否 | {} | 对应组织。 |
| FDescription | String | 否 |  | 备注。 |
| FSALDEPTID | Object | 否 | {} | 销售部门。 |
| FSELLER | Object | 否 | {} | 销售员。 |
| FSETTLETYPEID | Object | 否 | {} | 结算方式。 |
| FRECCONDITIONID | Object | 否 | {} | 收款条件。 |
| FDISCOUNTLISTID | Object | 否 | {} | 折扣表。 |
| FPRICELISTID | Object | 否 | {} | 价目表。 |
| FTRANSLEADTIME | Integer | 否 | 0 | 运输提前期。 |
| FInvoiceType | String | 否 |  | 发票类型。 |
| FTaxType | Object | 否 | {} | 税分类。 |
| FRECEIVECURRID | Object | 否 | {} | 收款币别。 |
| FPriority | Integer | 否 | 0 | 客户优先级。 |
| FTaxRate | Object | 否 | {} | 默认税率。 |
| FISCREDITCHECK | bool | 否 | false | 启用信用管理。 |
| FIsTrade | bool | 否 | false | 是否交易客户。 |
| FUncheckExpectQty | bool | 否 | false | 不校验可发量。 |
| FLegalPerson | String | 否 |  | 法人代表。 |
| FRegisterFund | String | 否 |  | 注册资本。 |
| FFoundDate | String | 否 |  | 创立日期。 |
| FDomains | String | 否 |  | 行业。 |
| FSOCIALCRECODE | String | 否 |  | 统一社会信用代码。 |
| FRegisterAddress | String | 否 |  | 注册地址。 |
| FT\_BD\_CUSTOMEREXT | Object | 否 | {} | 商务信息。 |
| FT\_BD\_CUSTLOCATION | Array | 否 | [] | 联系人。 |
| FT\_BD\_CUSTBANK | Array | 否 | [] | 银行信息。 |
| FT\_BD\_CUSTCONTACT | Array | 否 | [] | 地址信息。 |
| FT\_BD\_CUSTORDERORG | Array | 否 | [] | 订货组织。 |
| FT\_BD\_CUSTSUBACCOUNT | Array | 否 | [] | 对应子账户信息。 |

#### **提交**

| **入参** | **类型** | **是否必填** | **示例值** | **详细说明** |
| --- | --- | --- | --- | --- |
| formid | String | 是 | BD\_Customer | 业务对象表单Id，字符串类型。 |
| data | Object | 是 |  | JSON格式数据（详情参考JSON格式数据）。 |
| CreateOrgId | Integer | 否 | 0 | 创建者组织内码（非必录） |
| Numbers | Array | 否 | [] | 单据编码集合，数组类型，格式：[No1,No2,...]。  **[!NOTE]**  使用编码时必填。 |
| Ids | String | 否 |  | 单据内码集合，字符串类型，格式："Id1,Id2,..."。  **[!NOTE]**  使用内码时必填。 |
| SelectedPostId | Integer | 否 | 0 | 工作流发起员工岗位内码，整型。  **[!NOTE]**  员工身兼多岗时不传参默认取第一个岗位 |
| NetworkCtrl | String | 否 |  | 是否启用网控，布尔类型，默认false。 |
| IgnoreInterationFlag | String | 否 |  | 是否允许忽略交互，布尔类型，默认true。 |

#### **审核**

| **入参** | **类型** | **是否必填** | **示例值** | **详细说明** |
| --- | --- | --- | --- | --- |
| formid | String | 是 | BD\_Customer | 业务对象表单Id，字符串类型。 |
| data | Object | 是 |  | JSON格式数据（详情参考JSON格式数据）。 |
| CreateOrgId | Integer | 否 | 0 | 创建者组织内码。 |
| Numbers | Array | 否 | [] | 单据编码集合，数组类型，格式：[No1,No2,...]。  **[!NOTE]**  使用编码时必填。 |
| Ids | String | 否 |  | 单据内码集合，字符串类型，格式："Id1,Id2,..."。  **[!NOTE]**  使用内码时必填。 |
| InterationFlags | String | 否 |  | 交互标志集合，字符串类型，分号分隔，格式："flag1;flag2;..."，例如，允许负库存标识：STK\_InvCheckResult。 |
| NetworkCtrl | String | 否 |  | 是否启用网控，布尔类型，默认false。 |
| IsVerifyProcInst | String | 否 |  | 是否检验单据关联运行中的工作流实例，布尔类型，默认false。 |
| IgnoreInterationFlag | String | 否 |  | 是否允许忽略交互，布尔类型，默认true。 |
| UseBatControlTimes | bool | 否 | false | 是否应用单据参数设置分批处理，默认false。 |

#### **反审核**

| **入参** | **类型** | **是否必填** | **示例值** | **详细说明** |
| --- | --- | --- | --- | --- |
| formid | String | 是 | BD\_Customer | 业务对象表单Id，字符串类型。 |
| data | Object | 是 |  | JSON格式数据（详情参考JSON格式数据）。 |
| CreateOrgId | Integer | 否 | 0 | 创建者组织内码。 |
| Numbers | Array | 否 | [] | 单据编码集合，数组类型，格式：[No1,No2,...]。  **[!NOTE]**  使用编码时必填。 |
| Ids | String | 否 |  | 单据内码集合，字符串类型，格式："Id1,Id2,..."。  **[!NOTE]**  使用内码时必填。 |
| InterationFlags | String | 否 |  | 交互标志集合，字符串类型，分号分隔，格式："flag1;flag2;..."，例如，允许负库存标识：STK\_InvCheckResult。 |
| IgnoreInterationFlag | String | 否 |  | 是否允许忽略交互，布尔类型，默认true。 |
| NetworkCtrl | String | 否 |  | 是否启用网控，布尔类型，默认false。 |
| IsVerifyProcInst | String | 否 |  | 是否检验单据关联运行中的工作流实例，布尔类型，默认false。 |

#### **编码操作-禁用（Forbid）、反禁用（enable）**

| **入参** | **类型** | **是否必填** | **示例值** | **详细说明** |
| --- | --- | --- | --- | --- |
| formid | String | 是 | BD\_Customer | 业务对象表单Id，字符串类型。 |
| opNumber | String | 是 | Forbid | 操作编码，字符串类型。 |
| data | Object | 是 |  | JSON格式数据（详情参考JSON格式数据）。 |
| CreateOrgId | Integer | 否 | 0 | 创建者组织内码， |
| Numbers | Array | 否 | [] | 单据编码集合，数组类型，格式：[No1,No2,...]。  **[!NOTE]**  使用编码时必填。 |
| Ids | String | 否 |  | 单据内码集合，字符串类型，格式："Id1,Id2,..."。  **[!NOTE]**  使用内码时必填。 |
| PkEntryIds | Array | 否 | [] | 单据内码与分录内码对应关系的集合，字符串类型，格式：[{"Id":"Id1","EntryIds":"EntryId1,EntryId2,..."}] 。  **[!NOTE]**  使用分录状态转换时必录。 |
| NetworkCtrl | String | 否 |  | 是否启用网控，布尔类型，默认false。 |
| IgnoreInterationFlag | String | 否 |  | 是否允许忽略交互，布尔类型，默认true。 |

#### **撤销**

| **入参** | **类型** | **是否必填** | **示例值** | **详细说明** |
| --- | --- | --- | --- | --- |
| formid | String | 是 | BD\_Customer | 业务对象表单Id，字符串类型。 |
| data | Object | 是 |  | JSON格式数据（详情参考JSON格式数据）。 |
| CreateOrgId | Integer | 否 | 0 | 创建者组织内码。 |
| Numbers | Array | 否 | [] | 单据编码集合，数组类型，格式：[No1,No2,...]。  **[!NOTE]**  使用编码时必填。 |
| Ids | String | 否 |  | 单据内码集合，字符串类型，格式："Id1,Id2,..."。  **[!NOTE]**  使用内码时必填。 |
| NetworkCtrl | String | 否 |  | 是否启用网控，布尔类型，默认false。 |

#### **删除**

| **入参** | **类型** | **是否必填** | **示例值** | **详细说明** |
| --- | --- | --- | --- | --- |
| formid | String | 是 | BD\_Customer | 业务对象表单Id，字符串类型。 |
| data | Object | 是 |  | JSON格式数据（详情参考JSON格式数据）。 |
| CreateOrgId | Integer | 否 | 0 | 创建者组织内码。 |
| Numbers | Array | 否 | [] | 单据编码集合，数组类型，格式：[No1,No2,...]。  **[!NOTE]**  使用编码时必填。 |
| Ids | String | 否 |  | 单据内码集合，字符串类型，格式："Id1,Id2,..."。  **[!NOTE]**  使用内码时必填。 |
| NetworkCtrl | String | 否 |  | 是否启用网控，布尔类型，默认false。 |

#### **单据查询**

| **入参** | **类型** | **是否必填** | **示例值** | **详细说明** |
| --- | --- | --- | --- | --- |
| data | Object | 是 |  | JSON格式数据（详情参考JSON格式数据）。 |
| FormId | String | 是 | BD\_Empinfo | 业务对象表单Id。 |
| FieldKeys | String | 是 |  | 需查询的字段key集合，字符串类型，格式："key1,key2,..."。  **[!NOTE]**  查询单据体内码,需加单据体Key和下划线,如：FEntryKey\_FEntryId |
| FilterString | Array | 否 | [] | 过滤条件，数组类型，如：[{"Left":"(","FieldName":"Field1","Compare":"=","Value":"111","Right":")","Logic":"AND"},{"Left":"(","FieldName":"Field2","Compare":"=","Value":"222","Right":")","Logic":""}]。 |
| OrderString | String | 否 |  | 排序字段，字符串类型。 |
| TopRowCount | Integer | 否 | 0 | 返回总行数，整型。 |
| StartRow | Integer | 否 | 0 | 开始行索引，整型。 |
| Limit | Integer | 否 | 2000 | 最大行数，整型，不能超过10000。 |
| SubSystemId | String | 否 |  | 表单所在的子系统内码，字符串类型。 |

#### **供应链采购申请单暂存**

| **入参** | **类型** | **是否必填** | **示例值** | **详细说明** |
| --- | --- | --- | --- | --- |
| formid | String | 是 | BD\_Customer | 业务对象表单Id，字符串类型。 |
| data | Object | 是 |  | JSON格式数据（详情参考JSON格式数据）。 |
| NeedUpDateFields | Array | 否 | [] | 需要更新的字段，数组类型，格式：[key1,key2,...] 。  **[!NOTE]**  更新字段时Model数据包中必须设置内码，若更新单据体字段还需设置分录内码 |
| NeedReturnFields | Array | 否 | [] | 需返回结果的字段集合，数组类型，格式：[key,entitykey.key,...]。  **[!NOTE]**  返回单据体字段格式：entitykey.key |
| IsDeleteEntry | bool | 否 | true | 是否删除已存在的分录，布尔类型，默认true。 |
| SubSystemId | String | 否 |  | 表单所在的子系统内码，字符串类型。 |
| IsVerifyBaseDataField | bool | 否 | false | 是否验证所有的基础资料有效性，布尔类，默认false。 |
| IsEntryBatchFill | bool | 否 | true | 是否批量填充分录，默认true。 |
| ValidateFlag | bool | 否 | true | 是否验证数据合法性标志，布尔类型，默认true。  **[!NOTE]**  设为false时不对数据合法性进行校验 |
| NumberSearch | bool | 否 | true | 是否用编码搜索基础资料，布尔类型，默认true。 |
| IsAutoAdjustField | bool | 否 | false | 是否自动调整JSON字段顺序，布尔类型，默认false。 |
| InterationFlags | String | 否 |  | 交互标志集合，字符串类型，分号分隔，格式："flag1;flag2;..."，例如，允许负库存标识：STK\_InvCheckResult。 |
| IgnoreInterationFlag | String | 否 |  | 是否允许忽略交互，布尔类型，默认true。 |
| IsControlPrecision | bool | 否 | false | 是否控制精度，为true时对金额、单价和数量字段进行精度验证，默认false。 |
| ValidateRepeatJson | bool | 否 | false | 校验Json数据包是否重复传入，一旦重复传入，接口调用失败，默认false。 |
| Model | Object | 是 | {} | 表单数据包，JSON类型。 |
| FBillTypeID | Object | 是 | {} | 单据类型。 |
| FNumber | String | 否 |  | 单据类型编码。 |
| FApplicationOrgId | Object | 是 | {} | 申请组织。 |
| FNumber | String | 否 |  | 申请组织编码。 |
| FApplicationDate | String | 是 |  | 申请日期。 |
| FRequestType | String | 是 |  | 申请类型。 |
| FEntity | Array | 是 | [] | 明细信息。 |
| FEntryID | Integer | 否 | 0 | 明细ID。 |
| FRequireOrgId | Object | 是 | {} | 需求组织。 |
| FMaterialId | Object | 是 | {} | 物料编码。 |
| FMaterialDesc | String | 否 |  | 物料说明。 |
| FAuxpropId | Object | 否 | {} | 辅助属性。 |
| FUnitId | Object | 是 | {} | 申请单位。 |
| FReqQty | Integer | 否 | 0 | 申请数量。 |
| FApproveQty | Integer | 否 | 0 | 批准数量。 |
| FPurchaseOrgId | Object | 是 | {} | 采购组织。 |
| FSuggestSupplierId | Object | 否 | {} | 建议供应商。 |
| FReceiveOrgId | Object | 否 | {} | 收料组织。 |
| FEvaluatePrice | Integer | 否 | 0 | 单价。 |
| FTAXPRICE | Integer | 否 | 0 | 含税单价。 |
| FTAXRATE | Integer | 否 | 0 | 税率%。 |
| FPriceUnitId | Object | 是 | {} | 计价单位。 |
| FPriceUnitQty | Integer | 否 | 0 | 计价数量。 |
| FREQSTOCKUNITID | Object | 是 | {} | 库存单位。 |
| FREQSTOCKQTY | Integer | 否 | 0 | 库存单位数量。 |
| FLeadTime | Integer | 否 | 0 | 提前期。 |
| FSrcBillTypeId | String | 否 |  | 源单类型。 |
| FSupplierId | Object | 否 | {} | 指定供应商(6.0作废)。 |
| FSrcBillNo | String | 否 |  | 源单编号。 |
| FChargeProjectID | Object | 否 | {} | 费用项目。 |
| FPurchaseDeptId | Object | 否 | {} | 采购部门。 |
| FReceiveAddress | String | 否 |  | 交货地址。 |
| FEntryNote | String | 否 |  | 备注。 |
| FPurchaserId | Object | 否 | {} | 采购员。 |
| FPurchaseGroupId | Object | 否 | {} | 采购组。 |
| FBOMNoId | Object | 否 | {} | BOM版本。 |
| FStockId | Object | 否 | {} | 仓库。 |
| FProviderId | Object | 否 | {} | 供货地点。 |
| FMtoNo | String | 否 |  | 计划跟踪号。 |
| FBaseReqQty | Integer | 否 | 0 | 申请数量(基本单位)。 |
| FReceiveDeptId | Object | 否 | {} | 收料部门。 |
| FRequireDeptId | Object | 否 | {} | 需求部门。 |
| FSalUnitID | Object | 否 | {} | 销售单位。 |
| FSalQty | Integer | 否 | 0 | 销售数量。 |
| FSalBaseQty | Integer | 否 | 0 | 销售基本数量。 |
| FIsVmiBusiness | bool | 否 | false | VMI业务。 |
| FDEMANDTYPE | String | 否 |  | 需求来源。 |
| FDEMANDBILLNO | String | 否 |  | 需求单据编号。 |
| FDEMANDBILLENTRYSEQ | Integer | 否 | 0 | 需求单据行号。 |
| FDEMANDBILLENTRYID | Integer | 否 | 0 | 需求单据分录内码。 |
| FSrcReqMergeEntryIds | String | 否 |  | 申请单合并前分录内码。 |
| FAssortBillNo | String | 否 |  | 配套单据编号。 |
| FSupMatId | String | 否 |  | 供应商物料编码。 |
| FSupMatName | String | 否 |  | 供应商物料名称。 |

#### **员工服务-费用申请单保存**

| **入参** | **类型** | **是否必填** | **示例值** | **详细说明** |
| --- | --- | --- | --- | --- |
| formid | String | 是 | BD\_Customer | 业务对象表单Id，字符串类型。 |
| data | Object | 是 |  | JSON格式数据（详情参考JSON格式数据）。 |
| NeedUpDateFields | Array | 否 | [] | 需要更新的字段，数组类型，格式：[key1,key2,...] 。  **[!NOTE]**  更新字段时Model数据包中必须设置内码，若更新单据体字段还需设置分录内码 |
| NeedReturnFields | Array | 否 | [] | 需返回结果的字段集合，数组类型，格式：[key,entitykey.key,...]。  **[!NOTE]**  返回单据体字段格式：entitykey.key |
| IsDeleteEntry | bool | 否 | true | 是否删除已存在的分录，布尔类型，默认true。 |
| SubSystemId | String | 否 |  | 表单所在的子系统内码，字符串类型。 |
| IsVerifyBaseDataField | bool | 否 | false | 是否验证所有的基础资料有效性，布尔类，默认false。 |
| IsEntryBatchFill | bool | 否 | true | 是否批量填充分录，默认true。 |
| ValidateFlag | bool | 否 | true | 是否验证数据合法性标志，布尔类型，默认true。  **[!NOTE]**  设为false时不对数据合法性进行校验 |
| NumberSearch | bool | 否 | true | 是否用编码搜索基础资料，布尔类型，默认true。 |
| IsAutoAdjustField | bool | 否 | false | 是否自动调整JSON字段顺序，布尔类型，默认false。 |
| InterationFlags | String | 否 |  | 交互标志集合，字符串类型，分号分隔，格式："flag1;flag2;..."。例如，允许负库存标识：STK\_InvCheckResult。 |
| IgnoreInterationFlag | String | 否 |  | 是否允许忽略交互，布尔类型，默认true。 |
| IsControlPrecision | bool | 否 | false | 是否控制精度，为true时对金额、单价和数量字段进行精度验证，默认false。 |
| ValidateRepeatJson | bool | 否 | false | 校验Json数据包是否重复传入，一旦重复传入，接口调用失败，默认false。 |
| Model | Object | 是 | {} | 表单数据包，JSON类型。 |
| FDate | String | 是 | 1900-01-01 | 申请日期。 |
| FStaffID | Object | 是 | {} | 申请人。 |
| FDeptID | Object | 是 | {} | 申请部门。 |
| FReason | String | 是 |  | 事由。 |
| FOrgID | Object | 是 | {} | 申请组织。 |
| FPhoneNumber | String | 否 |  | 联系电话。 |
| FCostOrgID | Object | 否 | {} | 费用承担组织。 |
| FCostDeptID | Object | 否 | {} | 费用承担部门。 |
| FCurrencyID | Object | 是 | {} | 币别。 |
| FSettleTypeID | Object | 否 | {} | 结算方式。 |
| FPayOrgID | Object | 否 | {} | 付款组织。 |
| FIsBorrow | bool | 否 | false | 申请借款。 |
| FTOCONTACTUNITTYPE | String | 是 |  | 往来单位类型。 |
| FTOCONTACTUNIT | Object | 否 | {} | 往来单位。 |
| FBankName | String | 否 |  | 开户银行。 |
| FBankAcctName | String | 否 |  | 账户名称。 |
| FBankAccount | String | 否 |  | 银行账号。 |
| FIsOnlineBankPay | bool | 否 | false | 通过网上银行支付。 |
| FProvince | Object | 否 | {} | 省（作废）。 |
| FCostProductID | Object | 否 | {} | 费用承担产品。 |
| FCITY | Object | 否 | {} | 市（作废）。 |
| FDISTRICT | Object | 否 | {} | 地区（作废）。 |
| FOrgAmountSum | Integer | 否 | 0 | 申请金额汇总。 |
| FCheckedOrgAmountSum | Integer | 否 | 0 | 核定金额汇总。 |
| FLocCurrencyID | Object | 是 | {} | 本位币。 |
| FExchangeRate | Integer | 否 | 0 | 汇率。 |
| FExchangeTypeID | Object | 是 | {} | 汇率类型。 |
| FLocAmountSum | Integer | 否 | 0 | 申请金额汇总(本位币)。 |
| FCheckedLocAmountSum | Integer | 否 | 0 | 核定金额汇总(本位币)。 |
| FCreatorId | Object | 否 | {} | 创建人。 |
| FCreateDate | String | 否 | 1900-01-01 | 创建日期。 |
| FModifierId | Object | 否 | {} | 修改人。 |
| FModifyDate | String | 否 | 1900-01-01 | 修改日期。 |
| FAPPROVERID | Object | 否 | {} | 审核人。 |
| FAPPROVEDATE | String | 否 | 1900-01-01 | 审核日期。 |
| FRefundDate | String | 否 | 1900-01-01 | 预计还款日期。 |
| FPayBankID | Object | 否 | {} | 收款银行（作废）。 |
| FBillTypeID | Object | 是 | {} | 单据类型。 |
| FShowLocInfo | bool | 否 | false | 显示本位币信息。 |
| FBankAddress | String | 否 |  | 银行地址。 |
| FBankCnaps | String | 否 |  | 联行号。 |
| FBankDetail | Object | 否 | {} | 银行网点。 |
| FCountry | String | 否 |  | 国别。 |
| FNProvince | String | 否 |  | 省。 |
| FNCity | String | 否 |  | 城市。 |
| FNDistrict | String | 否 |  | 地区。 |
| FFromTransfer | bool | 否 | false | 来自转移。 |
| FBringAccount | String | 否 |  | 银行账号携带。 |
| FEntity | Array | 是 | [] | 明细信息。 |
| FEntryID | Integer | 否 | 0 | 明细ID。 |
| FSourceBillType | String | 否 |  | 源单类型。 |
| FSourceBillNo | String | 否 |  | 源单编号。 |
| FSourceRowID | Integer | 否 | 0 | 源单分录ID。 |
| FLocAmount | Integer | 否 | 0 | 申请金额(本位币)。 |
| FCheckedLocAmount | Integer | 否 | 0 | 核定金额(本位币)。 |
| FExpenseItemID | Object | 是 | {} | 费用项目。 |
| FOrgAmount | Integer | 否 | 0 | 申请金额。 |
| FCheckedOrgAmount | Integer | 否 | 0 | 核定金额。 |
| FEntryCostDeptID | Object | 否 | {} | 费用承担部门。 |
| FRemark | String | 否 |  | 备注。 |

### **使用教程**

- [采购申请钉钉 OA 申请审批通过后同步到金蝶云星空](0033-dingtalk-application.md)
- [差旅报销钉钉 OA 申请审批通过后同步到金蝶云星空](0034-reimbursement-dingtalk-approved.md)
