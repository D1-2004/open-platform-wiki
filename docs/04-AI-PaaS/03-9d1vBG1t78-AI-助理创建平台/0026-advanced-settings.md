---
title: "高级设置"
source_url: "https://open.dingtalk.com/document/aipass/advanced-settings"
namespace: "aipass"
slug: "advanced-settings"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 能力 > 自定义能力 > 高级设置"
doc_id: "UlR8peIObA"
updated_at: "2025-09-23 19:19:27"
---

> Source: https://open.dingtalk.com/document/aipass/advanced-settings
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 能力 > 自定义能力 > 高级设置
> Updated: 2025-09-23 19:19:27

# 高级设置

本文介绍了 OpenAPI 方式自定义能力开发过程中的一些高级功能，通过这些功能开发者可以更灵活的控制自定义能力的执行效果。

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理/助理市场创建的 AI 助理**

## **提高参数提取准确性**

在处理复杂的应用场景时，如果发现大型模型在参数提取方面的准确度未达到预期效果，你可以通过添加示例问法的方式帮助大模型更好的理解你的提问方法，提升参数提取的准确性。为此，你可以使用 x-dingtalk-examples 字段来添加这些示例问法。请按照以下格式进行配置：

```
x-dingtalk-examples:
	- input: 原始的输入示例1
  	output: 
    	filed1: 示例参数1
      filed2: 示例参数2
  - input: 原始的输入示例2
  	output:
    	filed1: 示例参数1
      filed2: 示例参数2
```

在配置示例问法时，你应在 input 字段中填入用户可能会提出的问题，而在 output 字段中则填写你希望模型根据输入的信息所能提取出的参数结果。以天气查询功能为例，配置示例问法的方法如下所示：

```
 /v1/actions/example/weather:
    get:
      x-dingtalk-examples:
        - input: 查询一下今天北京的天气
          output:
            location: 北京
            date: 今天
      parameters:
        - name: location
          in: query
          description: 要查询天气的城市和地区
          required: true
          schema:
            type: string
        - name: date
          in: query
          description: 要查询日期，默认今天，格式为 yyyy-MM-dd
          schema: 
            type: string
```

> **[!IMPORTANT]**
>
> output 中的参数名必须和接口定义的参数名称保持一致，并且参数值必须是一个可以从提问者输入的信息中可以直接理解或推断出的信息，不能是业务转换之后的参数。

我们以查询假期的为例，如下为一种典型的错误写法：

```
openapi: 3.0.1
info:
  title: 剩余假期查询
  description: 根据员工工号查询剩余假期
  version: 1.0.0
servers:
  - url: http://action.dingtalk.com
paths:
  /vacation/get:
    get:
      description: 根据工号和假期类型查询员工的剩余假期额度。假期类型有：0年假、1调休、2全薪病假
      summary: 查询剩余假期额度
      operationId: queryVacation
      x-dingtalk-params-confirm: true
      x-dingtalk-examples:
        - input: 查询一下我的调休假期
          output:
            name: "107807"
            type: "1"
      parameters:
        - name: jobNum
          in: query
          description: 工号
          required: true
          schema:
            type: string
        - name: type
          in: query
          description: 假期类型，有三种类型，分别为："0"为年假、"1"为调休、"2"为全薪病假
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Response'
components:
  schemas:
    Response:
      type: object
      properties:
        result:
          type: number
          description: 返回剩余假期数量
```

大模型无法从**查询一下我的调休假期**的这段描述中推理出工号 107807 和类型 1，正确的实例写法为：

```
openapi: 3.0.1
info:
  title: 剩余假期查询
  description: 根据员工工号查询剩余假期
  version: 1.0.0
servers:
  - url: http://action.dingtalk.com
paths:
  /vacation/get:
    get:
      description: 根据工号和假期类型查询员工的剩余假期额度。假期类型有：0年假、1调休、2全薪病假
      summary: 查询剩余假期额度
      operationId: queryVacation
      x-dingtalk-params-confirm: true
      x-dingtalk-examples:
        - input: 查询一下我的调休假期
          output:
            name: 我
            type: 调休
      parameters:
        - name: jobNum
          in: query
          description: 工号
          required: true
          schema:
            type: string
        - name: type
          in: query
          description: 假期类型，有三种类型，分别为："0"为年假、"1"为调休、"2"为全薪病假
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Response'
components:
  schemas:
    Response:
      type: object
      properties:
        result:
          type: number
          description: 返回剩余假期数量
```

## **提高API识别的准确性**

在配置文件中涉及多个接口的复杂应用场景里，如果大型模型无法根据用户输入准确选择相应的接口，你可以使用 x-dingtalk-keywords 扩展字段来增强模型对接口的理解和识别。你应按照以下格式来配置关键词：

```
x-dingtalk-keywords:
  - 关键词1
  - 关键词2
  - 关键词3
```

以天气查询为例，关键词配置如下所示：

```
  /v1/actions/example/weather:
    get: 
      operationId: GetWeather
      summary: 查询天气
      description: 查询特定地区的天气信息
      x-dingtalk-examples:
        - input: 查询一下今天北京的天气
          output:
            location: 北京
            date: 今天
      x-dingtalk-keywords:
        - 天气
        - 查看
      parameters:
        - name: location
          schema: 
            type: string
          in: query
          description: 地点
        - name: date
          schema: 
            type: string
          in: query
          description: 时间
      responses:
        200:
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetWeatherResponse'
```

## **获取运行上下文**

在开发Actions（动作）的过程中，你可能会需要访问执行过程中的上下文信息，例如消息发送者的个人信息、其所属组织的信息等。这些上下文信息可以通过特定的扩展字段 x-dingtalk-context 来获取。运行上下文获取请遵循以下的基本格式：

```
x-dingtalk-context:
  property: 属性值
  format: 属性格式
```

以查询天气为例，如果你想要获取查询者的信息，你可以进行以下配置：

```
/v1/actions/example/weather/get:
    get: 
      operationId: GetWeather
      summary: 查询天气
      description: 查询特定地区特定时间的天气信息
      x-dingtalk-examples:
        - input: 查询一下今天北京的天气
          output:
            location: 北京
            date: 今天
      x-dingtalk-keywords:
        - 天气
        - 查看
      parameters:
        - name: sender 
          schema:
            type: string
            x-dingtalk-context:
            	property: currentUser
            	format: unionId
          in: query
          description: 查询人
        - name: location 
          in: query
          schema: 
            type: string
          description: 地区
        - name: date
          in: query
          schema:
            type: string
          description: 日期
```

> **[!IMPORTANT]**
>
> - x-dingtalk-context 必须配置在与参数类型 type 字段同一级。
> - 当你在开发中需要利用上下文字段时，平台会自动为这些字段填充相应的值；在配置示例问法时，无需指示大模型去获取这些字段。

在上述你所使用的描述文件中，对于 sender 字段，平台会自动将其填充为消息发送者的 unionId 信息。目前，官方支持的上下文枚举信息列举如下：

| **属性（property）** | **格式（format）** | **说明** |
| --- | --- | --- |
| currentUser | userId | 发送人的 userId。 |
| unionId | 发送人的 unionId。 |
| jobNum | 发送人的工号信息。 |
| oauthAuthCode | 发送人的 OAuth 授权码，参考[鉴权方式](0027-authentication-method.md)。 |
| currentOrg | corpId | 发送人的组织 corpId。 |
| currentInput | raw | 用户与 AI 助理对话的原始信息。 |
| currentInput | attribute | 描述了用户输入信息的属性信息，内容为一个JSON字符串，格式如下所示   ``` {   "msgType" : "text/picture/file" } ```   msgType表示输入信息的类型。  text: 文本信息  picture: 图片信息  file: 文件信息 |
| currentConversation | openConversationId | 当前 IM 单聊/群聊的 id，其他场景下该字段为空。  **[!NOTE]**  预览调试框使用 AI 助理，不返回该字段。 |
| threadId | 用户和助理之间的会话 id，用于承载用户和助理之间的聊过的消息内容，每次“开启新话题”后，threadId 值会发生变化，且助理不再记得之前聊过的消息内容。  **[!NOTE]**  该字段与 [Assistant API 调用流程](../../01-应用开发/02-4a8AMF6u2A-服务端API/1691-assistantapi-call-process.md)中的 threadId 是同一个字段，含义相同。 |
| runId | 用户每次给助理发送消息，助理就会开始运行、推理、并给出响应，这个运行过程对应了一个 runId，即一个 runId 表示了一次助理的运行。  **[!NOTE]**  该字段与 [Assistant API 调用流程](../../01-应用开发/02-4a8AMF6u2A-服务端API/1691-assistantapi-call-process.md)中的 runId 是同一个字段，含义相同。 |
| conversationToken | 会话凭证，可以用于AI助理调用API发送消息。凭证中保存了会话的上下文信息，包括：聊天场景（如单聊、群聊等）、聊天对象（如 AI 助理、机器人等）、会话发起人信息等。  **[!NOTE]**  使用凭证回复消息的开发流程可以参考文档[AI 助理发消息 - 回复消息模式](0034-the-ai-assistant-sends-a-card-to-reply-to-the.md)。 |
| sessionWebhook | 可直接用来通过 AI 助理回复消息。  **[!NOTE]**  使用 sessionWebhook 回复消息的开发流程可以参考文档 [AI 助理发消息 - Webhook 回复消息模式](https://open.dingtalk.com/document/aipass/the-ai-assistant-sends-a-card-to-reply-to-the-1)。 |

## **实体识别**

钉钉拥有多样化的业务系统和丰富的业务实体信息。除了基础的自然语言理解功能外，它还支持把相关实体映射到对应的业务模型中。例如，当你询问 AI 助理“给张三发邮件”时，AI 助理可能无法直接识别“张三”的具体身份。在钉钉平台上，可以通过实体识别技术，将“张三”识别为具体的用户 userId，进而查询到其邮箱、手机号等。钉钉通过 x-dingtalk-entity 这一扩展字段，辅助完成业务实体到用户信息的映射。具体的配置格式如下：

```
x-dingtalk-entity:
	category: 实体类型
  format: 格式
```

| **类型（category）** | **格式（format）** | **说明** |
| --- | --- | --- |
| name | unionId | 将人名转为unionId。 |
| userId | 将人名转为userId。 |
| time | iso8601 | yyyy-MM-dd:mm:ss.sssZ。  例如：2023-03-15T14:45:30+02:00 |
| 自定义格式 | strftime: 自定义时间格式  例如 strftime: yyyy-MM-dd 输出的时间为2023-12-31 |

以查询天气的功能为例，如果你需要将大模型提取的日期信息转换为“yyyy-MM-dd”这种自定义的日期格式，你可以按照以下内容进行配置：

```
  /v1/actions/example/weather/get:
    get:
      operationId: GetWeather
      summary: 查询天气
      description: 查询特定地区特定时间的天气信息
      x-dingtalk-examples:
        - input: 查询一下今天北京的天气
          output:
            location: 北京
            date: 今天
      x-dingtalk-keywords:
        - 天气
        - 查看
      parameters:
        - name: date
          schema: 
            type: string
            x-dingtalk-entity:
            	category: time
            	format: strftime:yyyy-MM-dd
          in: query
          description: 日期
        - name: location
          schema: 
            type: string
          in: query
          description: 地点
```

> **[!IMPORTANT]**
>
> x-dingtalk-entity 必须配置在与参数类型 type 字段同一级。

## **设置确认卡片**

每当用户与 AI 助理进行对话时，在大模型完成参数提取后，你可以指定 AI 助理发送一张参数确认卡片。这张卡片上会显示大模型提取出的业务参数，用户可以依据卡片上的信息来核查这些参数是否达到了预期的正确性。如果参数与预期不符，用户可以直接在卡片上进行编辑修改。编辑完成后，单击卡片上的**确认**按钮即可触发相应的 OpenAPI 操作，该能力可以通过设置 x-dingtalk-params-confirm 扩展字段来开启。

```
x-dingtalk-params-confirm: true
```

以查询天气为例：

```
 /v1/actions/example/weather/get:
    get:
      operationId: GetWeather
      summary: 查询天气
      description: 查询特定地区特定时间的天气信息
      x-dingtalk-params-confirm: true  ## 开启参确认卡片
      x-dingtalk-examples:
        - input: 查询一下今天北京的天气
          output:
            location: 北京
            date: 今天
      x-dingtalk-keywords:
        - 天气
        - 查看
      parameters:
        - name: sender
          schema:
            type: string
            x-dingtalk-context:
            	property: currentUser
            	format: unionId
          in: query
          description: 查询人
        - name: location
          in: query
          schema: 
            type: string
          description: 地区
        - name: date
          schema: 
            type: string
            x-dingtalk-entity:
            	category: time
            	format: iso8601
          in: query
          description: 日期
```

## **设置结果卡片**

在 OpenAPI 操作执行完毕后，AI 助理通常会默认使用 Markdown 格式，发送一张展示执行结果的卡片。如果你不需要显示这张结果卡片或是希望展示自定义的内容格式，可以通过设置 x-dingtalk-display-result 这一扩展字段来进行控制。具体的配置方式如下：

```
x-dingtalk-display-result: auto
```

选项值如下所示：

| **选项值** | **说明** |
| --- | --- |
| auto | 平台侧自动将 API 返回的结果转成易于阅读的消息卡片展示给用户。例如将 json 转成措辞和排版友好的 Markdown 形式的卡片消息。 |
| disabled | 平台侧不会自动返回 API 调用结果，通常用于 API 服务端自定义发送结果卡片。 |
| markdown | 如果你想自定义结果展示，而不是大模型自动生成，也不用学习卡片搭建的技术，那么可以使用 markdown 模式， 该模式下用户可以自定义需要展示的 Markdown 信息， 平台侧将会把 API 返回的 Markdown 信息展示在结果卡片上， 该模式下 API 返回的结果必须是一个符合如下规范的JSON数据，   ``` {   "content" : "需要展示的 Markdown 文本" } ```   ，例如：   ``` {   "content" : "## 天气信息\n * 日期: 2024年1月10日\n * 温度: 20摄氏度" } ``` |

以天气查询为例，如果你不想在 OpenAPI 执行之后展示结果卡片，可以做如下配置：

```
 /v1/actions/example/weather/get: 
    get:
      operationId: GetWeather
      summary: 查询天气
      description: 查询特定地区特定时间的天气信息
      x-dingtalk-display-result: disabled  ## 关闭结果卡片
      x-dingtalk-examples:
        - input: 查询一下今天北京的天气
          output:
            location: 北京
            date: 今天
      x-dingtalk-keywords:
        - 天气
        - 查看
      parameters:
        - name: sender
          schema: 
            type: string
            x-dingtalk-context:
            	property: currentUser
            	format: unionId
          in: query
          description: 查询人
        - name: location
          schema: 
            type: string
          in: query
          description: 地区
        - name: date
          in: query
          schema: 
            type: string
            x-dingtalk-entity:
            	category: time
            	format: iso8601
          description: 日期
```

## **设置参数默认值**

Actions 支持扩展字段 x-dingtalk-default 来设置参数的默认值，当你希望大模型在提取对应参数失败时使用某个默认值，可以使用 x-dingtalk-default 来设置，配置的格式如下所示:

```
x-dingtalk-default: 默认值
```

> **[!IMPORTANT]**
>
> - 在使用 x-dingtalk-default 配置时，一定要将参数的 required 设置为 false。
> - x-dingtalk-default 必须配置在与参数类型 type 字段同一级。

以天气查询为例，如果你想设置默认的地点为北京，你可以按照如下设置

```
 /v1/actions/example/weather/get: 
    get:
      operationId: GetWeather
      summary: 查询天气
      description: 查询特定地区特定时间的天气信息
      x-dingtalk-display-result: disabled  ## 关闭结果卡片
      x-dingtalk-examples:
        - input: 查询一下今天北京的天气
          output:
            location: 北京
            date: 今天
      x-dingtalk-keywords:
        - 天气
        - 查看
      parameters:
        - name: location
          schema: 
            type: string
            x-dingtalk-default: 北京 ## 设置默认值
          required: false ## 设置参数为非必填
          in: query
          description: 地区
        - name: date
          in: query
          required: true
          schema: 
            type: string
            x-dingtalk-entity:
            	category: time
            	format: iso8601
          description: 日期
```

## **启用 Stream 模式回调**

高级自定义能力默认使用 HTTP 协议回调开发者的服务，HTTP 协议的回调要求开发者在 servers 字段中填写一个公网的回调域名，当开发者基于安全或是资源的限制无法提供公网回调域名的时候，可以使用 [服务端Stream模式](https://open.dingtalk.com/document/development/introduction-to-stream-mode)来进行回调，使用 Stream 模式开发者无需提供公网域名。 开发者可以通过扩展字段 x-dingtalk-protocol 来启用 Stream 模式，配置的格式如下所示:

```
x-dingtalk-protocol: stream
```

x-dingtalk-protocol当前支持的协议枚举类型有http、stream。

> **[!IMPORTANT]**
>
> 1. 在 x-dingtalk-protocol 配置为 stream 时，OpenAPI 配置文件中的 servers 字段可以填写任意域名。
> 2. 使用 Stream 模式，Stream 客户端订阅的topic固定为：/v1.0/graph/api/invoke。
> 3. 使用 Stream 模式可以通过 AI 助理的开发页面获取应用的身份信息。
>
> ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9978251171/p783926.png)
>
> 4. 详细的代码开发方式可以参考[高级自定义能力Stream模式发手册](https://opensource.dingtalk.com/developerpedia/docs/explore/tutorials/stream/advanced_ability/java)。

以天气查询为例，可以参考如下方式编写配置文件

```
openapi: 3.0.1
info:
  title: 天气查询
  description: 按地区和日期来查看天气信息，了解气温、湿度、风向等信息。非真实天气数据，仅用于演示，请勿在生产中使用。
  version: v1.0.0
servers:
  - url: https://action-example.dingtalk.com
x-dingtalk-protocol: stream
paths:
  /v1/actions/example/weather/get:
    get:
      description: 查询特定地区的天气信息
      summary: 查看天气
      operationId: GetCurrentWeather
      parameters:
        - name: location
          in: query
          description: 地区
          required: true
          schema:
            type: string
        - name: date
          in: query
          description: 日期
          required: true
          schema:
            type: string
            x-dingtalk-entity:
                category: time
                format: strftime:yyyy-MM-dd
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetWeatherResponse'
components:
  schemas:
    GetWeatherResponse:
      type: object
      properties:
        location:
          type: string
          description: 查询天气结果对应的城市和地区
        date:
          type: string
          description: 查询天气结果对应的日期
        text:
          type: string
          description: 天气现象，晴天、多云等
        temperature:
          type: number
          description: 气温，单位：摄氏度
        humidity:
          type: number
          description: 湿度
        wind_direction:
          type: string
          description: 风向
```

接口的定义方式和 HTTP 协议的方式完全相同，只需要配置 x-dingtalk-protocol 字段开启即可。

### **数据格式**

**请求数据格式**

stream 模式下收到的请求是一个类似 HTTP 请求的 JSON 结构的数据，格式如下所示

```
{
  "requestLine" : {
    "method" : "GET",
    "uri" : "/v1/actions/example/weather/get?date=2021-10-1&location=%E6%9D%AD%E5%B7%9E"
  },
  "headers" : {
    "content-type" : "application/json"
  },
  "body" : "{}"
}
```

**响应数据格式**

处理完成响应之后，开发者需要返回一个如下结构的响应

```
{
  "statusLine" : {
    "code" : 200,
    "reasonPhrase" : "OK"
  },
  "headers" : {
    "content-type" : "application/json"
  },
  "body" : "{\"dateStr\" : \"2024-03-26\",\"temperature\" : 22, \"humidity\" : 65,\"location\" : \"杭州\", \"wind_direction\" : \"东南风\", \"text\" : \"晴天\"}"
}
```

### **Stream协议 转 HTTP**

除了上述通过监听 topic=/v1.0/graph/api/invoke的方式来处理 AI 助理回调的请求之外，开发者也可以通过 SDK 将请求直接转发到本地的 HTTP 服务端口，开发者只需要和使用 HTTP 协议一样开发业务代码即可, 我们继续以天气查询为例，在本地配置 Stream 客户端，填写需要转发的目标 HTTP 服务端口。

Java

```
@Configuration
public class StreamClientConfigure {

    @Value("${dingtalk.app.client-id}")
    private String clientId;

    @Value("${dingtalk.app.client-secret}")
    private String clientSecret;
  
    @Value("${server.port}")
    private int port;

    @Bean(initMethod = "start")
    public OpenDingTalkClient configure() {
        return OpenDingTalkStreamClientBuilder.custom()
                .credential(new AuthClientCredential(clientId, clientSecret))
                .forwardGraphRequestToHTTP(port)
                .build();
    }
}
```

业务代码编写如下

Java

```
@RestController
@RequestMapping("/v1/actions/example/weather")
public class WeatherController {
    @GetMapping("/get")
    @ResponseBody
    public Map<String, Object> get(@RequestParam(value = "location", required = false) String location,
                                   @RequestParam(value = "date", required = false) String date) {
        Map<String, Object> result = new HashMap<>();
        if (location == null || location.isEmpty()) {
            location = "杭州";
        }
        if (date == null || date.isEmpty()) {
            date = (new SimpleDateFormat("yyyy-MM-dd")).format(new Date());
        }
        result.put("location", location);
        result.put("dateStr", date);
        result.put("text", "晴天");
        result.put("temperature", 22);
        result.put("humidity", 65);
        result.put("wind_direction", "东南风");
        return result;
    }
}
```

Stream SDK 会将 AI 助理请求转成 HTTP 请求，详细的代码实现可以参考[示例工程](https://github.com/open-dingtalk/dingtalk-tutorial-java/blob/main/ai-actions-stream/src/main/java/org/example/ai/actions/StreamActionsDispatcher.java)。

## **开启直通模式**

如果当前您希望直接获取 AI 助理的对话信息并且跳过平台的大模型能力，可以使用 AI 助理的直通模式，使用直通模式之后，平台将不再执行任何与大模型相关的处理，直接将 AI 助理的上下文传递给开发者的Action，开启直通模式可以参考如下步骤：

### **步骤一：编写接口 Yaml 配置文件**

> **[!IMPORTANT]**
>
> 1. 所有的参数都必须是从上下文中获取，即必须使用 x-dingtalk-context 来映射接口参数。
> 2. 配置文件中必须只能定义一个接口。

以天气查询为例，可以参考如下方式编写配置文件

```
openapi: 3.0.1
info:
  title: 天气查询
  description: 按地区和日期来查看天气信息，了解气温、湿度、风向等信息。非真实天气数据，仅用于演示，请勿在生产中使用。
  version: v1.0.0
x-dingtalk-protocol: stream
paths:
  /v1/actions/example/weather/get:
    get:
      description: 查询特定地区的天气信息
      summary: 查看天气
      operationId: GetCurrentWeather
      parameters:
        - name: input
          in: query
          description: 输入信息
          required: true
          schema:
            type: string
            x-dingtalk-context:
              property: currentInput
              format: raw
        - name: sender
          in: query
          description: 请求人
          required: true
          schema:
            type: string
            x-dingtalk-context:
              property: currentUser
              format: userId
        - name: inputAttribute
          in: query
          description: 输入信息属性
          required: true
          schema:
            type: string
            x-dingtalk-context:
              property: currentInput
              format: attribute
        - name: corpId
          in: query
          description: 组织信息
          required: true
          schema:
            type: string
            x-dingtalk-context:
              property: currentOrg
              format: corpId
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetWeatherResponse'
components:
  schemas:
    GetWeatherResponse:
      type: object
      properties:
        location:
          type: string
          description: 查询天气结果对应的城市和地区
        date:
          type: string
          description: 查询天气结果对应的日期
        text:
          type: string
          description: 天气现象，晴天、多云等
        temperature:
          type: number
          description: 气温，单位：摄氏度
        humidity:
          type: number
          description: 湿度
        wind_direction:
          type: string
          description: 风向
```

### **步骤二：关闭 AI 助理的智能对话**

在 AI 助理的能力选项关闭智能对话选项。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4183172171/p789981.png)

完成上述步骤即开通了直通模式，AI 助理的消息将会跳过平台的大模型直接转发到开发者注册的接口上，详细的开发细节可以参考[直通模式开发教程](https://opensource.dingtalk.com/developerpedia/docs/explore/tutorials/assistant_ability/passthrough_mode)。

## **常见问题**

## **开启【规划】-【推理增强】后，如何使用直通模式**

答：

1. 可以采用指定技能方式，单击**规划** > **推理规则**，进入设置规则页面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4855817471/p954620.png)
2. 设置技能规则，执行指定技能。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4855817471/p954621.png)

## **技术支持**

如果以上文档无法解决您的问题，可以通过[**自定义 AI 助理技术支持**](https://opensource.dingtalk.com/developerpedia/docs/explore/support/?via=moon-group)渠道寻求帮助。
