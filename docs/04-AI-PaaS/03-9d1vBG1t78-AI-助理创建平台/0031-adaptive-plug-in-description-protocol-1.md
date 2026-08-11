---
title: "描述协议"
source_url: "https://open.dingtalk.com/document/aipass/adaptive-plug-in-description-protocol-1"
namespace: "aipass"
slug: "adaptive-plug-in-description-protocol-1"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 能力 > 拟人操作（RPA） > 描述协议"
doc_id: "v1S0KUZS7v"
updated_at: "2025-09-23 19:19:31"
---

> Source: https://open.dingtalk.com/document/aipass/adaptive-plug-in-description-protocol-1
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 能力 > 拟人操作（RPA） > 描述协议
> Updated: 2025-09-23 19:19:31

# 描述协议

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理**

每个拟人操作（RPA）必须包含一个名为`ai-plugin.json`的文件。你可以使用钉钉提供的[拟人操作（RPA）开发工具](0032-development-tools.md)来生成这个文件，或者手动编写。该文件详细说明了插件具有的功能以及所需的参数信息。

## **基础配置**

请确保你的插件遵守我们的协议标准，并且满足以下字段的字符限制要求。未按规范设计的插件将无法被录入。以下是所需`ai-plugin.json`文件的最简定义：

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| adaptive\_schema\_version | String | 是 | 协议版本，不同的协议版本对应的解析规则不相同，当前协议版本：1.0.0。 |
| title | String | 是 | 插件的名称，要求，不允许空格，最多 50 个字符。 |
| description | String | 是 | 插件的描述，用于模型识别。标记上下文，用于改进插件提示的关键词使用，最多 2000 个字符。 |
| version | String | 否 | 业务定义的插件版本。 |
| actions | Object | 是 | 插件能力项。 |
| summary | String | 是 | action 名称。 |
| description | String | 是 | action 描述，用于模型识别。 |
| keywords | Array of String | 否 | 插件关键词，用户 action 路由匹配，详情参考下方高级配置。 |
| target\_url\_by\_platform | Object | 是 | action 运行的目标页面。 |
| default | String | 否 | 默认地址。 |
| mobile | String | 否 | 移动端地址。  action运行的目标页面,目标页面分平台时使用，优先使用mobile。 |
| desktop | String | 否 | 桌面端地址。  desktop不填时默认用default。 |
| script\_url | String | 是 | action 运行的脚本。 |
| examples | Array | 否 | 用于大模型更准确地理解 action 意图。 |
| input | String | 是 | input 表示用户输入。 |
| output | Object | 是 | output 表示大模型需要返回的结构及内容，结构与 input\_param 保持一致。 |
| input\_param | Object | 是 | action脚本接收的入参。 |
| type | String | 是 | 字段类型：   - string：字符串类型 - number：数值类型 - array：数组类型 - object：对象类型 - boolean：布尔类型 |
| description | String | 是 | 字段描述。 |
| properties | Object | 是 | 属性对象。 |
| <key> | Object | 否 | 自定义属性 Key。 |
| type | String | 否 | 自定义属性类型。 |
| description | String | 否 | 描述。 |
| items | Object | 否 | 属性 type 是 array 时，需要约定item的类型 。 |
| type | String | 否 | 字段类型：   - string：字符串类型 - number：数值类型 - array：数组类型 - object：对象类型 - boolean：布尔类型 |
| x-dingtalk-default | String | 否 | 属性默认值，详细见高级配置。 |
| x-dingtalk-entity | String | 否 | 业务实体，目前提供 name 和 time。  name 格式示例如下：   ``` {   "category":"name",   "format":"unionId" } ``` |
| x-dingtalk-context | String | 否 | 系统字段，目前提供 currentUser 和 input。  currentUser 格式示例如下：   ``` { "property": "currentUser", "format": "staffId" } ``` |
| required | Array of String | 否 | 必填属性。 |
| output\_param | Object | 否 | action 脚本出参。 |
| type | String | 否 | 字段类型：   - string：字符串类型 - number：数值类型 - array：数组类型 - object：对象类型 - boolean：布尔类型 |
| description | String | 否 | 描述。 |
| properties | Object | 否 | 属性对象。 |
| <key> | Object | 否 | 自定义属性 Key。 |
| type | String | 否 | 字段类型：   - string：字符串类型 - number：数值类型 - array：数组类型 - object：对象类型 - boolean：布尔类型 |
| description | String | 否 | 描述。 |
| items | Object | 否 | 属性 type 是 array 时，需要约定 item 的类型 。 |
| type | String | 否 | 字段类型：   - string：字符串类型 - number：数值类型 - array：数组类型 - object：对象类型 - boolean：布尔类型 |
| x-dingtalk-default | String | 否 | 属性默认值，详细见高级配置。 |
| x-dingtalk-entity | String | 否 | 业务实体，目前提供 name 和 time。  name 格式示例如下：   ``` {   "category":"name",   "format":"unionId" } ``` |
| x-dingtalk-context | String | 否 | 系统字段，目前提供 currentUser 和 input。  currentUser 格式示例如下：   ``` { "property": "currentUser", "format": "staffId" } ``` |
| required | Array of String | 否 | 必填属性。 |
| headless\_mode | Boolean | 是 | 是否启用无头模式：   - true：启用 - false：关闭   默认 false。 |
| support\_platform | Array of String | 否 | 支持的平台：   - android - ios - mac - win |
| target\_valid\_domains | Array of String | 是 | 可操作的目标页面 host 列表。  自适应插件的 target\_url\_by\_platform 页面需要打开另外的域名执行脚本时，每个页面 domain 都需要配置。 |

## **高级设置**

## **使用 examples 提高参数提取准确性**

对于复杂的应用场景，如果大型模型在提取参数时的准确度无法达到预期，你可以通过增加示例性问题的方法来提升参数提取的效果。你可以通过补充 examples 配置中的示例问题来实现，具体的配置格式如下所示：

```
{
  examples: [
    {
      "input":原始的输入示例1,
      "output": {
        "filed1":示例参数1,
        "filed2":示例参数2
      }
    }
  ]
}
```

在 input 字段中填写用户可能提出的问题方式，在 output 字段中填写你希望得到的参数提取结果。举个例子，对于天气查询功能，具体的查询动作（Action）的示例配置如下：

```
{
  "examples": [
    {
      "input": "搜索杭州天气",
      "output": {
        "keyword": "杭州天气"
      }
    }
  ]
}
```

## **使用 keywords 提高 action 识别的准确性**

在配置文件包含多个动作（Action）的复杂场景下，如果大型模型无法根据输入信息理想地选择相应的接口，您可以使用 keywords 字段来辅助模型更准确地理解和识别接口。关键词的配置格式示例如下：

```
{
  "keywords":["关键词1","关键词2","关键词3"]
}
```

以**百度搜索**为例，关键词配置如下所示：

```
"baiduSearch": {
  "examples": [
    {
      "input": "搜索杭州天气",
      "output": {
        "keyword": "杭州天气"
      }
    }
  ],
  "keywords": [
    "搜索",
    "百度搜索",
    "搜一下"
  ],
  "input_param": {
    "type": "object",
    "description": "",
    "properties": {
      "keyword": {
        "type": "string",
        "example": "",
        "description": "搜索关键词",
      }
    }
  }
}
```

## **参数设定默认值**

动作（Action）支持配置输入参数 input\_param。在大多数场景下，input\_param 是由大型模型通过泛化处理得到的。对于特殊情况，input\_param 支持设置默认值。如需配置默认值，请使用扩展字段  x-dingtalk-default 进行设置：

```
{
  "x-dingtalk-default": "<your default value>"
}
```

以百度搜索为例，如果我们想要指定搜索关键词为“钉钉”：

```
{
  "baiduSearch": {
    "examples": [
      {
        "input": "搜索杭州天气",
        "output": {
          "keyword": "杭州天气"
        }
      }
    ],
    "keywords": [
      "搜索",
      "百度搜索",
      "搜一下"
    ],
    "input_param": {
      "type": "object",
      "description": "",
      "properties": {
        "keyword": {
          "type": "string",
          "example": "",
          "x-dingtalk-default": "钉钉"
        }
      }
    }
  }
}
```

## **获取运行上下文**

在开发 Actions 时，开发者可能需要获取一些在执行过程中的上下文信息，例如消息发送者的信息、发送者所在组织的信息等。这些上下文信息可以通过扩展字段  x-dingtalk-context 来获取。获取上下文信息的基本格式如下：

```
{
  "x-dingtalk-context": {
    "property":'属性值',
    "format":'属性格式'
  }
}
```

以百度搜索为例，如果你想要获取查询者的信息，你可以进行如下配置：

```
{
  "baiduSearch": {
    "examples": [
      {
        "input": "搜索杭州天气",
        "output": {
          "keyword": "杭州天气"
        }
      }
    ],
    "keywords": [
      "搜索",
      "百度搜索",
      "搜一下"
    ],
    "input_param": {
      "type": "object",
      "description": "",
      "properties": {
        "uid": {
          "type": "string",
          "description": "搜索人Id",
          "x-dingtalk-context": {
            "property": "currentUser",
            "format": "userId"
          }
        },
        "keyword": {
          "type": "string",
          "example": "",
          "description": "搜索关键词",
        }
      }
    }
  }
}
```

> **[!NOTE]**
>
> 当你在开发中需要利用上下文字段时，平台会自动为这些字段填充相应的值。在配置示例问法时，无需指示大模型去获取这些字段。

在上述你所使用的描述文件中，以 uid 字段为例，平台会自动将其填充为消息发送者的 userId 信息。另外，上下文字段支持数组，示例如下：

```
{
  "baiduSearch": {
    "input_param": {
      "type": "object",
      "description": "",
      "properties": {
        "uid": {
          "type": "array",
          "description": "参会人",
          "example": ["张三","李四"],
          "items": {
             "type": "string"
          },
          "x-dingtalk-context": {
            "property": "currentUser",
            "format": "userId"
          }
        },
      }
    }
  }
}
```

目前，官方支持的上下文枚举信息列举如下：

| **属性（property）** | **格式（format）** | **说明** |
| --- | --- | --- |
| currentUser | userId | 发送人的 userId。 |
| unionId | 发送人的 unionId。 |
| jobNum | 发送人的工号信息。 |
| currentOrg | corpId | 发送人的组织 corpId。 |
| currentInput | raw | 用户与数字助理对话的原始信息。 |

## **实体识别**

钉钉拥有多样化的业务系统和丰富的业务实体信息。除了基础的自然语言理解功能外，它还支持把相关实体映射到对应的业务模型中。例如，当你询问 AI 助理“给张三发邮件”时，AI 助理可能无法直接识别“张三”的具体身份。在钉钉平台上，可以通过实体识别技术，将“张三”识别为具体的用户 userId，进而查询到其邮箱、手机号等。钉钉通过 x-dingtalk-entity 这一扩展字段，辅助完成业务实体到用户信息的映射。具体的配置格式如下：

```
{
  "x-dingtalk-entity": {
    "category": "实体类型",
    "format": "格式"
  }
}
```

| **类型（category）** | **格式（format）** | **说明** |
| --- | --- | --- |
| name | unionId | 将人名转为unionId。 |
| userId | 将人名转为userId。 |
| time | iso8601 | yyyy-MM-dd:mm:ss.sssZ。  例如：2023-03-15T14:45:30+02:00 |
| strftime:自定义格式 | strftime: 自定义时间格式  例如 strftime: yyyy-MM-dd 输出的时间为2023-12-31 |

以查询天气的功能为例，如果你需要将大模型提取的日期信息转换为“yyyy-MM-dd”这种自定义的日期格式，你可以按照以下内容进行配置：

```
{
  "baiduSearch": {
    "examples": [
      {
        "input": "搜索明天杭州天气",
        "output": {
          "keyword": "杭州天气",
          "date": "2023-01-03"
        }
      }
    ],
    "keywords": [
      "搜索",
      "百度搜索",
      "搜一下"
    ],
    "input_param": {
      "type": "object",
      "description": "",
      "properties": {
        "uid": {
          "type": "string",
          "description": "搜索人Id",
          "x-dingtalk-context": {
            "property": "currentUser",
            "format": "userId"
          }
        },
        "keyword": {
          "type": "string",
          "example": "",
          "description": "搜索关键词",
        },
        "date": {
          "type": "string",
          "description": "查询时间",
          "x-dingtalk-entity": {
            "category": "time",
            "format": "strftime:yyyy-MM-dd"
          }
        }
      }
    }
  }
}
```

## **示例展示**

通过百度搜索，查询天气状态，示例如下：

```
{
    "adaptive_schema_version": "1.0.0",
    "title": "百度搜索",
    "description": "通过百度搜索信息，可提取搜索时间及关键词",
    "version": "1.0.1",
    "keywords": [
        "搜索",
        "search"
    ],
    "actions": {
        "baiduSearch": {
            "description":"百度搜索天气",
            "examples":[{
              "input":"搜索明天杭州天气",
              "output":{
                "keyword":"杭州天气",
                "date":"2023-01-03"
              }
            }],
            "keywords":["搜索","百度搜索","搜一下"],
            "input_param":{
              "type": "object",
              "description": "",
              "properties": {
                  "uid": {
                      "type": "string",
                      "description": "搜索人Id",
                      "x-dingtalk-context":{
                        "property":"currentUser",
                        "format":"userId"
                      }
                  },
                  "keyword": {
                      "type": "string",
                      "example": "",
                      "description": "搜索关键词",
                  },
                 "date":{
                   "type":"string",
                   "description": "查询时间",
                   "x-dingtalk-entity":{
                      "category":"time",
                      "format":"strftime:yyyy-MM-dd"
                    }
                 }
              }
            }
            "target_url": "http://www.baidu.com",
            "script_url": "${cdn_url}",
            "headless_mode": true,
            "support_platform": [
                "android",
                "ios",
                "mac",
                "win"
            ]
      }
  }
}
```
