---
title: "参数说明"
source_url: "https://open.dingtalk.com/document/connection/kingdee-parameter-description"
namespace: "connection"
slug: "kingdee-parameter-description"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "三方连接器 > 金蝶云星空 > 参数说明"
doc_id: "uebxPlrStt"
updated_at: "2025-09-23 19:21:35"
---

> Source: https://open.dingtalk.com/document/connection/kingdee-parameter-description
> Path: 连接平台 / 连接器中心 / 三方连接器 > 金蝶云星空 > 参数说明
> Updated: 2025-09-23 19:21:35

# 参数说明

## **执行动作说明**

## **基础资料-暂存客户、保存客户**

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

## **提交**

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

## **审核**

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

## **反审核**

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

## **编码操作-禁用（Forbid）、反禁用（enable）**

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

### 撤销

| **入参** | **类型** | **是否必填** | **示例值** | **详细说明** |
| --- | --- | --- | --- | --- |
| formid | String | 是 | BD\_Customer | 业务对象表单Id，字符串类型。 |
| data | Object | 是 |  | JSON格式数据（详情参考JSON格式数据）。 |
| CreateOrgId | Integer | 否 | 0 | 创建者组织内码。 |
| Numbers | Array | 否 | [] | 单据编码集合，数组类型，格式：[No1,No2,...]。  **[!NOTE]**  使用编码时必填。 |
| Ids | String | 否 |  | 单据内码集合，字符串类型，格式："Id1,Id2,..."。  **[!NOTE]**  使用内码时必填。 |
| NetworkCtrl | String | 否 |  | 是否启用网控，布尔类型，默认false。 |

### 删除

| **入参** | **类型** | **是否必填** | **示例值** | **详细说明** |
| --- | --- | --- | --- | --- |
| formid | String | 是 | BD\_Customer | 业务对象表单Id，字符串类型。 |
| data | Object | 是 |  | JSON格式数据（详情参考JSON格式数据）。 |
| CreateOrgId | Integer | 否 | 0 | 创建者组织内码。 |
| Numbers | Array | 否 | [] | 单据编码集合，数组类型，格式：[No1,No2,...]。  **[!NOTE]**  使用编码时必填。 |
| Ids | String | 否 |  | 单据内码集合，字符串类型，格式："Id1,Id2,..."。  **[!NOTE]**  使用内码时必填。 |
| NetworkCtrl | String | 否 |  | 是否启用网控，布尔类型，默认false。 |

### 单据查询

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

### 供应链采购申请单暂存

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

### 员工服务-费用申请单保存

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
