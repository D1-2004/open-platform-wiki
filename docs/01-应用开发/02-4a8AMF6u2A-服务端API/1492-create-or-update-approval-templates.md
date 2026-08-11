---
title: "创建或更新审批模板"
source_url: "https://open.dingtalk.com/document/development/create-or-update-approval-templates"
namespace: "development"
slug: "create-or-update-approval-templates"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 创建或更新审批模板"
doc_id: "8rW99C2sc9"
updated_at: "2025-09-08 19:04:29"
---

> Source: https://open.dingtalk.com/document/development/create-or-update-approval-templates
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 创建或更新审批模板
> Updated: 2025-09-08 19:04:29

# 创建或更新审批模板

调用本接口创建或更新审批模板。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对OA审批相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2022年10月8日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[创建或更新审批表单模板](https://open.dingtalk.com/document/orgapp/create-an-approval-form-template)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

> **[!IMPORTANT]**
>
> - 每个企业最多创建200个官方审批模板，超过最大数量后调用接口会报错。
> - 钉钉客户端展示OA审批列表时，仅展示模板表单的前三个选项。
> - 官方OA审批模板仅支持文档下方所展示的审批组件，其他组件均不支持。
> - 更新审批模板时更新的组件在流程设计中设置为分支条件，则该模板表单不支持修改。

调用接口创建模板后，可以在[钉钉管理后台](https://oa.dingtalk.com/)-工作台-OA审批找到对应的审批模板。![审批模板](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8107796361/p352510.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/save`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 - 第三方企业应用可通[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential) |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| saveProcessRequest | SaveProcessRequest | 是 |  | 审批模板信息。 |
| agentid | Number | 是 | 123 | 应用标识。可在开发者后台的应用详情页获取。AgentId |
| process\_code | String | 否 | PROC-EF6YJL35P2xxxx | 审批流的唯一码。   - **未填写该参数，**表示新建一个模板。 - **填写该参数，**表示更新所传值对应的审批模板。   **如何获取process\_code**：在[钉钉管理后台](https://oa.dingtalk.com/#/login)-审批模板查看。  **新版钉钉管理后台**：在审批模板编辑页-基础设置-页面底部查看。审批-名词解释-processcode新版获取方法  **旧版钉钉管理后台**：在审批模板编辑页的URL中查看。 processCode |
| name | String | 是 | 请假 | 审批模板名称。 |
| description | String | 是 | 特殊请假流程 | 审批模板描述。 |
| form\_component\_list | FormComponentVo[] | 是 |  | 表单列表，最大列表长度20。 |
| component\_name | String | 是 | TextField | 表单名称。每种表单组件的component\_name是固定的。表单组件的props里的id，必须在模板里唯一，可以有两段字符串组成，第一段为表单的component\_name；第二段为8位随机字符串。  **[!NOTE]**  只支持下表中的表单，不支持其他值。 |
| props | FormComponentPropVo | 是 |  | 表单属性。 |
| id | String | 是 | TextField-78Fxxxx | 表单ID，最大不能超过22个字符。 |
| label | String | 是 | 单行输入框 | 表单名称。 |
| required | Boolean | 否 | true | 是否必填：   - **true**：是 - **false**：否。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 5av7ifh2atw0 | 请求ID。 |
| errmsg | String | 成功 | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| result | ProcessTopVo |  | 创建接口。 |
| process\_code | String | PROC-CODE | 审批模板唯一码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/save?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "saveProcessRequest": {
    "name": "审批模版测试",
    "process_code": "PROC-37801FB3-xxxx-xxxx-xxxx-6C6ADB87CD9A",  //创建模版时无该字段
    "agentid": "115xxxxxx211",
    "description": "审批模版测试",
    "form_component_list": [
      {
        "component_name": "TextField",
        "props": {
          "id": "TextField-J78F056R",
          "label": "单行输入框",
          "placeholder": "请输入"
        }
      },
      {
        "component_name": "TextareaField",
        "props": {
          "id": "TextareaField-J78F056S",
          "label": "多行输入框",
          "placeholder": "请输入",
          "required": true
        }
      },
      {
        "component_name": "MoneyField",
        "props": {
          "id": "MoneyField-J78F0571",
          "label": "金额（元）大写",
          "placeholder": "请输入金额",
          "not_upper": "0",
          "required": true
        }
      },
      {
        "component_name": "NumberField",
        "props": {
          "id": "NumberField-J78F057N",
          "label": "数字输入框",
          "placeholder": "请输入",
          "unit": "元",
          "required": true
        }
      },
      {
        "component_name": "CalculateField",
        "props": {
          "id": "CalculateField-JF85Z4ZP",
          "label": "合计",
          "placeholder": "自动计算数值",
          "formula": [
            {
              "id": "MoneyField-J78F0571"
            },
            "*",
            {
              "id": "NumberField-J78F057N"
            }
          ],
          "required": false
        }
      },
      {
        "component_name": "DDSelectField",
        "props": {
          "id": "DDSelectField-J78F056U",
          "label": "单选框",
          "placeholder": "请选择",
          "options": [
            "a",
            "b",
            "c"
          ],
          "required": true
        }
      },
      {
        "component_name": "DDMultiSelectField",
        "props": {
          "id": "DDMultiSelectField-J78F056V",
          "label": "多选框",
          "placeholder": "请选择",
          "options": [
            "a",
            "b",
            "c"
          ],
          "required": true
        }
      },
      {
        "component_name": "DDDateField",
        "props": {
          "id": "DDDateField-J8MTJZVE",
          "label": "日期",
          "placeholder": "请选择",
          "unit": "天",
          "required": true
        }
      },
      {
        "component_name": "DDDateRangeField",
        "props": {
          "id": "DDDateRangeField-J78F057Q",
          "label": [
            "开始时间",
            "结束时间"
          ],
          "placeholder": "请选择",
          "unit": "天",
          "required": true
        }
      },
      {
        "component_name": "RelateField",
        "props": {
          "id": "RelateField-JF85Z4ZO",
          "label": "关联审批单",
          "placeholder": "请选择",
          "not_print": "1",
          "required": true
        }
      },
      {
        "component_name": "DDPhotoField",
        "props": {
          "id": "DDPhotoField-J78F056Y",
          "label": "图片",
          "required": true
        }
      },
      {
        "component_name": "DDAttachment",
        "props": {
          "id": "DDAttachment-J78F0572",
          "label": "附件",
          "required": true
        }
      },
      {
        "component_name": "InnerContactField",
        "props": {
          "id": "InnerContactField-J78F0574",
          "label": "联系人",
          "choice": "0",
          "required": true
        }
      },
      {
        "component_name": "TableField",
        "props": {
          "id": "TableField-JT435H4C",
          "label": "明细",
          "action_name": "增加明细",
          "stat_field": [
            {
              "id": "NumberField-JT435KJO",
              "label": "数字",
              "upper": false
            }
          ]
        },
        "children": [
          {
            "component_name": "TextField",
            "props": {
              "id": "TextField-JT435KJN",
              "label": "单行输入框",
              "placeholder": "请输入",
              "required": true
            }
          },
          {
            "component_name": "NumberField",
            "props": {
              "id": "NumberField-JT435KJO",
              "label": "数字输入框",
              "placeholder": "请输入数字",
              "required": true
            }
          }
        ]
      }
    ]
  }
}
```

**请求示例（JAVA SDK）**

```
   DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/save");
        OapiProcessSaveRequest request = new OapiProcessSaveRequest();
        OapiProcessSaveRequest.SaveProcessRequest saveProcessRequest = new OapiProcessSaveRequest.SaveProcessRequest();
        saveProcessRequest.setName("审批模版测试");
        saveProcessRequest.setProcessCode("PROC-37801FB3-xxxx-xxxx-xxxx-6C6ADB87CD9A");
        saveProcessRequest.setAgentid(115xxxx211L);
        saveProcessRequest.setDescription("审批模版测试");

        // 注意，每种表单组件，对应的componentName是固定的，参照以下示例代码
        List<OapiProcessSaveRequest.FormComponentVo> formComponentList = new ArrayList<>();

        // 单行文本框
        OapiProcessSaveRequest.FormComponentVo singleInput = new OapiProcessSaveRequest.FormComponentVo();
        singleInput.setComponentName("TextField");
        OapiProcessSaveRequest.FormComponentPropVo singleInputProp = new OapiProcessSaveRequest.FormComponentPropVo();
        singleInputProp.setRequired(true);
        singleInputProp.setLabel("单行输入框");
        singleInputProp.setPlaceholder("请输入");
        singleInputProp.setId("TextField-J78F056R");
        singleInput.setProps(singleInputProp);
        formComponentList.add(singleInput);

        // 多行文本框
        OapiProcessSaveRequest.FormComponentVo multipleInput = new OapiProcessSaveRequest.FormComponentVo();
        multipleInput.setComponentName("TextareaField");
        OapiProcessSaveRequest.FormComponentPropVo multipleInputProp = new OapiProcessSaveRequest.FormComponentPropVo();
        multipleInputProp.setRequired(true);
        multipleInputProp.setLabel("多行输入框");
        multipleInputProp.setPlaceholder("请输入");
        multipleInputProp.setId("TextareaField-J78F056S");
        multipleInput.setProps(multipleInputProp);
        formComponentList.add(multipleInput);

        // 金额组件
        OapiProcessSaveRequest.FormComponentVo moneyComponent = new OapiProcessSaveRequest.FormComponentVo();
        moneyComponent.setComponentName("MoneyField");
        OapiProcessSaveRequest.FormComponentPropVo moneyComponentProp = new OapiProcessSaveRequest.FormComponentPropVo();
        moneyComponentProp.setRequired(true);
        moneyComponentProp.setLabel("金额（元）大写");
        moneyComponentProp.setPlaceholder("请输入");
        moneyComponentProp.setId("MoneyField-J78F0571");
        // 是否禁用大写
        moneyComponentProp.setNotUpper("0"); 
        moneyComponent.setProps(moneyComponentProp);
        formComponentList.add(moneyComponent);

        // 数字输入框
        OapiProcessSaveRequest.FormComponentVo numberComponent = new OapiProcessSaveRequest.FormComponentVo();
        numberComponent.setComponentName("NumberField");
        OapiProcessSaveRequest.FormComponentPropVo numberComponentProp = new OapiProcessSaveRequest.FormComponentPropVo();
        numberComponentProp.setRequired(true);
        numberComponentProp.setLabel("数字输入框");
        numberComponentProp.setPlaceholder("请输入");
        numberComponentProp.setId("NumberField-J78F057N");
        numberComponentProp.setUnit("元");
        numberComponent.setProps(numberComponentProp);
        formComponentList.add(numberComponent);

        // 计算公式
        OapiProcessSaveRequest.FormComponentVo calculateComponent = new OapiProcessSaveRequest.FormComponentVo();
        calculateComponent.setComponentName("CalculateField");
        OapiProcessSaveRequest.FormComponentPropVo calculateComponentProp = new OapiProcessSaveRequest.FormComponentPropVo();
        calculateComponentProp.setRequired(false);
        calculateComponentProp.setLabel("合计");
        JSONObject jsonObject1 = new JSONObject();
        jsonObject1.put("id", "MoneyField-J78F0571");
        String s = "*";
        JSONObject jsonObject2 = new JSONObject();
        jsonObject2.put("id", "NumberField-J78F057N");
        Object objects[] = new Object[]{jsonObject1, s, jsonObject2};
        calculateComponentProp.setFormula(JSON.toJSONString(objects));
        calculateComponentProp.setPlaceholder("自动计算数值");
        calculateComponentProp.setId("CalculateField-JF85Z4ZP");
        calculateComponent.setProps(calculateComponentProp);
        formComponentList.add(calculateComponent);

        // 单选框
        OapiProcessSaveRequest.FormComponentVo selectComponent = new OapiProcessSaveRequest.FormComponentVo();
        selectComponent.setComponentName("DDSelectField");
        OapiProcessSaveRequest.FormComponentPropVo selectComponentProp = new OapiProcessSaveRequest.FormComponentPropVo();
        selectComponentProp.setRequired(true);
        selectComponentProp.setLabel("单选框");
        selectComponentProp.setPlaceholder("请输入");
        selectComponentProp.setId("DDSelectField-J78F056U");
        // 选项最多200项，每项最多50个字
        selectComponentProp.setOptions(Arrays.asList("a", "b", "c")); 
        selectComponent.setProps(selectComponentProp);
        formComponentList.add(selectComponent);

        // 多选框
        OapiProcessSaveRequest.FormComponentVo multiSelectComponent = new OapiProcessSaveRequest.FormComponentVo();
        multiSelectComponent.setComponentName("DDMultiSelectField");
        OapiProcessSaveRequest.FormComponentPropVo multiSelectComponentProp = new OapiProcessSaveRequest.FormComponentPropVo();
        multiSelectComponentProp.setRequired(true);
        multiSelectComponentProp.setLabel("多选框");
        multiSelectComponentProp.setPlaceholder("请输入");
        multiSelectComponentProp.setId("DDMultiSelectField-J78F056V");
        multiSelectComponentProp.setOptions(Arrays.asList("a", "b", "c"));
        multiSelectComponent.setProps(multiSelectComponentProp);
        formComponentList.add(multiSelectComponent);

        // 日期
        OapiProcessSaveRequest.FormComponentVo dateComponent = new OapiProcessSaveRequest.FormComponentVo();
        dateComponent.setComponentName("DDDateField");
        OapiProcessSaveRequest.FormComponentPropVo dateComponentProp = new OapiProcessSaveRequest.FormComponentPropVo();
        dateComponentProp.setRequired(true);
        dateComponentProp.setLabel("日期");
        dateComponentProp.setPlaceholder("请选择");
        // 小时或天
        dateComponentProp.setUnit("天"); 
        dateComponentProp.setId("DDDateField-J8MTJZVE");
        dateComponent.setProps(dateComponentProp);
        formComponentList.add(dateComponent);

        // 日期区间
        OapiProcessSaveRequest.FormComponentVo dateRangeComponent = new OapiProcessSaveRequest.FormComponentVo();
        dateRangeComponent.setComponentName("DDDateRangeField");
        OapiProcessSaveRequest.FormComponentPropVo dateRangeComponentProp = new OapiProcessSaveRequest.FormComponentPropVo();
        dateRangeComponentProp.setRequired(true);
        dateRangeComponentProp.setLabel(JSON.toJSONString(Arrays.asList("开始时间", "结束时间")));
        dateRangeComponentProp.setPlaceholder("请选择");
         // 小时或天
        dateRangeComponentProp.setUnit("天");
        dateRangeComponentProp.setId("DDDateRangeField-J78F057Q");
        dateRangeComponent.setProps(dateRangeComponentProp);
        formComponentList.add(dateRangeComponent);

        // 关联组件
        OapiProcessSaveRequest.FormComponentVo relateComponent = new OapiProcessSaveRequest.FormComponentVo();
        relateComponent.setComponentName("RelateField");
        OapiProcessSaveRequest.FormComponentPropVo relateComponentProp = new OapiProcessSaveRequest.FormComponentPropVo();
        relateComponentProp.setRequired(true);
        relateComponentProp.setLabel("关联审批单");
        relateComponentProp.setPlaceholder("请选择");
        relateComponentProp.setId("RelateField-JF85Z4ZO");
        //是否打印，1表示不打印, 0表示打印
        relateComponentProp.setNotPrint("1");
        relateComponent.setProps(relateComponentProp);
        formComponentList.add(relateComponent);

        // 图片
        OapiProcessSaveRequest.FormComponentVo photoComponent = new OapiProcessSaveRequest.FormComponentVo();
        photoComponent.setComponentName("DDPhotoField");
        OapiProcessSaveRequest.FormComponentPropVo photoComponentProp = new OapiProcessSaveRequest.FormComponentPropVo();
        photoComponentProp.setRequired(true);
        photoComponentProp.setLabel("图片");
        photoComponentProp.setId("DDPhotoField-J78F056Y");
        photoComponent.setProps(photoComponentProp);
        formComponentList.add(photoComponent);

        // 附件
        OapiProcessSaveRequest.FormComponentVo attachmentComponent = new OapiProcessSaveRequest.FormComponentVo();
        attachmentComponent.setComponentName("DDAttachment");
        OapiProcessSaveRequest.FormComponentPropVo attachmentComponentProp = new OapiProcessSaveRequest.FormComponentPropVo();
        attachmentComponentProp.setRequired(true);
        attachmentComponentProp.setLabel("附件");
        attachmentComponentProp.setId("DDAttachment-J78F0572");
        attachmentComponent.setProps(attachmentComponentProp);
        formComponentList.add(attachmentComponent);

        // 内部联系人
        OapiProcessSaveRequest.FormComponentVo innerContactComponent = new OapiProcessSaveRequest.FormComponentVo();
        innerContactComponent.setComponentName("InnerContactField");
        OapiProcessSaveRequest.FormComponentPropVo innerContactComponentProp = new OapiProcessSaveRequest.FormComponentPropVo();
        innerContactComponentProp.setRequired(true);
        innerContactComponentProp.setLabel("联系人");
        // 是否支持多选 "1" or "0"，1表示多选
        innerContactComponentProp.setChoice(0L);
        innerContactComponentProp.setId("InnerContactField-J78F0574");
        innerContactComponent.setProps(innerContactComponentProp);
        formComponentList.add(innerContactComponent);

        // 明细组件
        OapiProcessSaveRequest.FormComponentVo formComponentVo = new OapiProcessSaveRequest.FormComponentVo();
        // 设置组件名称
        formComponentVo.setComponentName("TableField");
        // 设置组件属性
        OapiProcessSaveRequest.FormComponentPropVo prop = new OapiProcessSaveRequest.FormComponentPropVo();
        prop.setActionName("增加明细");
        prop.setLabel("明细");
        prop.setId("TableField-JT435H4C");
        // 明细里需要计算的组件列表
        List<OapiProcessSaveRequest.FormComponentStatVo> statFieldList = new ArrayList<>();
        OapiProcessSaveRequest.FormComponentStatVo statField = new OapiProcessSaveRequest.FormComponentStatVo();
        statField.setId("NumberField-JT435KJO");
        statField.setLabel("数字");
        statField.setUpper(false);
        statFieldList.add(statField);
        prop.setStatField(statFieldList);
        // 明细组件的子组件
        List<OapiProcessSaveRequest.FormComponentVo2> children = new ArrayList<>();
        OapiProcessSaveRequest.FormComponentVo2 form1 = new OapiProcessSaveRequest.FormComponentVo2();
        form1.setComponentName("TextField");
        OapiProcessSaveRequest.FormComponentPropVo2 prop1 = new OapiProcessSaveRequest.FormComponentPropVo2();
        prop1.setPlaceholder("请输入");
        prop1.setLabel("单行输入框");
        prop1.setId("TextField-JT435KJN");
        form1.setProps(prop1);

        OapiProcessSaveRequest.FormComponentVo2 form2 = new OapiProcessSaveRequest.FormComponentVo2();
        form2.setComponentName("NumberField");
        OapiProcessSaveRequest.FormComponentPropVo2 prop2 = new OapiProcessSaveRequest.FormComponentPropVo2();
        prop2.setRequired(true);
        prop2.setLabel("数字输入框");
        prop2.setId("NumberField-JT435KJO");
        prop2.setPlaceholder("请输入数字");
        form2.setProps(prop2);
        children.add(form1);
        children.add(form2);
        formComponentVo.setChildren(children);
        formComponentVo.setProps(prop);
        formComponentList.add(formComponentVo);
        saveProcessRequest.setFormComponentList(formComponentList);
        request.setSaveProcessRequest(saveProcessRequest);

        OapiProcessSaveResponse response = client.execute(request, AccessToken);
        System.out.println(JSON.toJSONString(response));
```

**返回示例**

```
{
    "errcode": 0,
    "result": {
        "process_code": "PROC-7C8BB7AE-E758-4A96-9375-27CFD376B19C"
    },
    "request_id": "5av7ifh2atw0"
}
```

## 支持的表单组件（component\_name）

- 单行文本-TextField

  ```
  {
    "component_name": "TextField",
    "props": {
      "required": true,
      "placeholder": "请输入1",
      "label": "单行输入框",
      "id": "TextField-J78F056R"
    }
  }
  ```
- 多行文本-TextareaField

  ```
  {
    "component_name": "TextareaField",
    "props": {
      "required": true,
      "placeholder": "请输入2",
      "label": "多行输入框",
      "id": "TextareaField-J78F056S"
    }
  }
  ```
- 金额-MoneyField

  ```
  {
    "component_name": "MoneyField",
    "props": {
      "required": true,
      "placeholder": "请输入6",
      "label": "金额（元）大写",
      "id": "MoneyField-J78F0571",
      "not_upper": "1" // 是否禁用大写
    }
  }
  ```
- 数字输入框-NumberField

  ```
  {
    "component_name": "NumberField",
    "props": {
      "required": true,
      "placeholder": "请输入4",
      "label": "数字输入框带单位",
      "unit": "元",
      "id": "NumberField-J78F057N"
    }
  ```
- 计算公式-CalculateField

  ```
  {
    "component_name": "CalculateField",
    "props": {
      "required": true,
      "placeholder": "自动计算数值",
      "label": "计算公式",
      "id": "CalculateField-JF85Z4ZP"
    }
  }
  ```
- 单选框-DDSelectField

  > **[!IMPORTANT]**
  >
  > 选项最多200项，每项最多50个字。

  ```
  {
    "component_name": "DDSelectField",
    "props": {
      "required": true,
      "placeholder": "请选择7",
      "options": [
        "选项1",
        "选项2",
        "选项3"
      ],
      "label": "单选框",
      "id": "DDSelectField-J78F056U"
    }
  }
  ```
- 多选框-DDMultiSelectField

  ```
  {
    "component_name": "DDMultiSelectField",
    "props": {
      "required": true,
      "placeholder": "请选择",
      "options": [
        "选项1",
        "选项2",
        "选项3"
      ],
      "label": "多选框",
      "id": "DDMultiSelectField-J78F056V"
    }
  }
  ```

  > **[!IMPORTANT]**
  >
  > 选项最多200项，每项最多50个字。

  ```
  {
      value: Array<string>; // 如 ["选项1"，"选项2"]
  }
  ```
- 日期-DDDateField

  ```
  {
    "component_name": "DDDateField",
    "props": {
      "required": true,
      "placeholder": "请选择",
      "label": "日期时分",
      "unit": "小时",    // 小时或天
      "id": "DDDateField-J8MTJZVE"
    }
  }
  ```
- 日期区间-DDDateRangeField

  ```
  {
    "component_name": "DDDateRangeField",
    "props": {
      "required": true,
      "placeholder": "请选择888",
      "unit": "小时", // 小时或天
      "label": [
        "开始时间小时",
        "结束时间小时"
      ],
      "id": "DDDateRangeField-J78F057Q"
    }
  }
  ```
- 关联组件-RelateField

  ```
  {
    "component_name": "RelateField",
    "props": {
      "required": true,
      "label": "关联审批单",
      "placeholder": "请选择",
      "not_print": "1",
      "id": "RelateField-JF85Z4ZO"
    }
  }
  ```
- 图片-DDPhotoField

  ```
  {
    "component_name": "DDPhotoField",
    "props": {
      "required": true,
      "label": "图片",
      "id": "DDPhotoField-J78F056Y"
    }
  }
  ```
- 附件-DDAttachment

  ```
  {
    "component_name": "DDAttachment",
    "props": {
      "required": true,
      "label": "附件",
      "id": "DDAttachment-J78F0572"
    }
  }
  ```
- 内部联系人-InnerContactField

  ```
  {
    "component_name": "InnerContactField",
    "props": {
      "required": true,
      "placeholder": "请选择",
      "label": "联系人多选",
      "choice": "1", // 是否支持多选 "1" or "0"
      "id": "InnerContactField-J78F0574"
    }
  }
  ```
- 明细-TableField

  ```
  {
    "component_name": "TableField",
    "props": {
      "action_name": "增加明细", //明细按钮显示文案
      "stat_field": [ //统计总和的组件
        {
          "id": "NumberField-JT435KJO",
          "label": "数字输入框",
          "upper": false //统计总和是否大写
        }
      ],
      "label": "明细",
      "id": "TableField-JT435H4C"
    },
    "children": [ //明细内组件(不支持明细嵌套)
      {
        "component_name": "TextField",
        "props": {
          "placeholder": "请输入",
          "label": "单行输入框",
          "id": "TextField-JT435KJN"
        }
      },
      {
        "component_name": "NumberField",
        "props": {
          "placeholder": "请输入数字",
          "label": "数字输入框",
          "required": true,
          "id": "NumberField-JT435KJO"
        }
      }
    ]
  }
  ```

## 常见问题

1. **需要创建哪些模板？模板名称是否可以重复？**

   企业内部应用接入官方OA审批能力，所有的官方OA审批模板，均需要调用钉钉接口初始化创建对应的模板。创建模板的时候，需确保模板名称（即name字段）的全局唯一性。
2. **该怎么设计表单？用什么类型的表单组件**

   钉钉审批、待办页面，展示审批单时，只会展示概要数据，即展示表单的前三个组件。因此，在设计模板时，前三个组件可根据业务场景设计，确保展示核心数据。

   表单类型可以使用本文已列支持的表单组件，包括单行文本框、金额、数字输入框等。
3. **创建的模板，是否会在钉钉审批管理后台出现？**

   调用接口的时候，fake\_mode参数必须传true，创建的模板不会在钉钉审批管理后台出现。
4. **调用接口返回错误码810002，错误信息是复制的审批流已超过最大数量**

   目前一个企业最多可创建200个官方审批模板，超过最大数量后调用接口会报错。
