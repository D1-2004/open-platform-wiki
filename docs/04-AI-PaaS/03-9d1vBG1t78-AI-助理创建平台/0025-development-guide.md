---
title: "开发指南"
source_url: "https://open.dingtalk.com/document/aipass/development-guide"
namespace: "aipass"
slug: "development-guide"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 能力 > 自定义能力 > 开发指南"
doc_id: "LyD24x1OFN"
updated_at: "2025-09-23 19:19:26"
---

> Source: https://open.dingtalk.com/document/aipass/development-guide
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 能力 > 自定义能力 > 开发指南
> Updated: 2025-09-23 19:19:26

# 开发指南

如果你需要开发 OpenAPI 的 AI 能力，你可以参考本文档操作步骤完成开发。

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理/助理市场创建的 AI 助理**

## **背景信息**

本文以官方**天气查询**功能为例，详细介绍如何通过 OpenAPI 的方式开发 AI 能力。

**天气查询**是钉钉 AI 助理提供的官方示例能力，当你询问 AI 助理的时候， AI 助理可以识别出你想要查询的地点和时间，然后通过调用我们提供的天气查询接口获取天气情况，并将天气情况通过卡片展示给你。

## **步骤一：**开发 RESTful API

首先你需要开发一个查询天气的接口， 接口的风格需要符合 RESTful API 规范，我们以 Java 代码为例：

```
@RestController
@RequestMapping("/v1/actions/example/weather")
public class WeatherExampleController {
  
  @GetMapping("/get")
  public WeatherResponse get(@RequestParam(value = "location") String location,
                             @RequestParam(value = "date", defaultValue= "杭州") String dateStr) {
        WeatherResponse response = WeatherResponse();
        response.setLocation(location);
        response.setDateStr(dateStr);
        response.setText("晴天");
        response.setTemperature(22);
        response.setHumidity(65);
        response.setWindDirection("东南风");
        return response;
    }
}
```

## **步骤二：**编写接口的 OpenAPI 描述文件

> **[!NOTE]**
>
> 编写符合 OpenAPI 3.0 规范的描述文件描述上述接口（语法规范参考标准 [OpenAPI Specification](https://swagger.io/specification/), 格式校验使用 [Swagger Editor](https://editor.swagger.io)）。

以天气查询为例，根据你定义的 RESTful 接口出入参和 URL 信息，OpenAPI 描述文件如下所示：

> **[!IMPORTANT]**
>
> - 接口描述的字段中，**summary**，**description**，**operationId** 为必填字段：
>
>   - **summary**：简短的动宾结构的短语，例如：**查询天气**。
>   - **description**：接口的详细描述信息。
>   - **operationId**：接口的唯一标识符，建议驼峰式的英文命名。
> - 同一个接口中请勿声名重名的参数。
> - **POST** 接口的请求和响应当前仅支持 **application/json** 格式
> - **POST** 接口参数支持 **object** 类型，且只能支持**一层参数**结构（更多能力，敬请期待！）
> - **servers** 字段填写接口对应的公网域名，支持HTTP和HTTPS协议

```
openapi: 3.0.1
info:
  title: 天气查询
  description: 按地区和日期来查看天气信息，了解气温、湿度、风向等信息。非真实天气数据，仅用于演示，请勿在生产中使用。
  version: 1.0.0
servers:
  - url: https://action-example.dingtalk.com ##此处填写接口对应的域名
paths:
  /v1/actions/example/weather/get:
    get:
      description: 查询特定地区的天气信息
      summary: 查询天气
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
          required: false
          schema: 
            type: string
      responses:
        200:
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

## **步骤三：**上传 OpenAPI 描述文件

描述文件上传支持 URL 链接导入或文本框编辑，上传完成后，单击保存，即可完成自定义 OpenAPI 能力的创建。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3941824071/p753753.png)

## **相关文档**

- [高级设置](0026-advanced-settings.md)
- [鉴权方式](0027-authentication-method.md)

## **参考资料**

- [OpenAPI 英文规范](https://swagger.io/specification/)
- [OpenAPI 中文规范](https://openapi.apifox.cn/)
- [OpenAPI 在线编辑器](https://editor.swagger.io/)
- [JSON Schema介绍](https://json-schema.org/learn/getting-started-step-by-step)

## **技术支持**

如果以上文档无法解决您的问题，可以通过[**自定义 AI 助理技术支持**](https://opensource.dingtalk.com/developerpedia/docs/explore/support/?via=moon-group)渠道寻求帮助。
