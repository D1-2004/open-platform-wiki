---
title: "表达式"
source_url: "https://open.dingtalk.com/document/connection/expression-overview"
namespace: "connection"
slug: "expression-overview"
group: "连接平台"
tab: "开发指南"
breadcrumb: "开发连接流 > 开发参考 > 表达式"
doc_id: "XO4W01t05k"
updated_at: "2025-09-23 19:20:05"
---

> Source: https://open.dingtalk.com/document/connection/expression-overview
> Path: 连接平台 / 开发指南 / 开发连接流 > 开发参考 > 表达式
> Updated: 2025-09-23 19:20:05

# 表达式

本文介绍什么是表达式以及表达式的基础语法。

## 什么是表达式

表达式是一组简单的函数，开发者可以使用表达式编写公式按照想要的方式获取数据。

例如，在连接流的节点之间传递数据时，可以通过简单的连线直接传递数据。但是在大多数情况下，可能需要更复杂的操作来处理节点数据。对节点数据进行MD5计算、多个节点数据进行合成、转换和比较等，如果有这些操作需求，可以使用表达式实现。

## 如何使用表达式

**连接流 > 入参映射 > 表达式**，进入表达式编辑框。

> **[!NOTE]**
>
> 表达式使用教程，可参考[审批表单数据同步至宜搭](https://open.dingtalk.com/document/dingstart/approval-form-appropriate)。

![iShot2022-03-23 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2136808461/p421969.png)

![iShot2022-03-23 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2136808461/p421972.png)

## 表达式基本语法

### 基础运算符

- +
- -
- \*
- /
- %
- ==
- !=
- &&
- ||
- !

### 原生支持 Json 语法

可以在表达式中直接构造 Json，并且可以在value中编写任意的表达式，例如

```
{
  "key": a+2
}
```

### 取值

- 下标取值：假设arr为`["a", "b", "c", "d"]`

  - `arr[0]`: 获取第一个元素a。
  - `arr[-1]`: 获取倒数第一个元素d。
  - `arr[1:3]`：获取数组内下标从1到3的元素，结果为`[b, c]`。语法为arr[起始下标(包含):结束下标(不包含)]。
- 属性取值：`a.b.c`
- 数组属性取值：假设arr为`[{"key":1},{"key":2}]`

  - `arr.*key`获取的结果为`[1,2]`

### 函数调用

语法为`函数名(参数列表)`，支持的函数参考本文档函数介绍。

## 集合函数

### IN

IN(ele,collection) 用于判断元素是否位于集合中。

示例：IN('选项 1', LIST('选项 1','选项 2')) 的结果为true。

### INTER

INTER(collection1,collection2) 用于计算两个集合的交集。

示例：INTER(LIST(1,2,3),LIST(2,3,5,6)) 的结果是 LIST(2,3)。

### SUPPLE

SUPPLE(collection1,collection2) 用于计算两个集合的补集。

示例：SUPPLE(LIST(1,2,3,4),LIST(3,4)) 的结果是 LIST(1,2)。

### LIST

LIST(ele1, ele2, ...) 用于生成一个由 ele1、ele2 ... 组成的集合。

示例：LIST('选项1','选项2')。

### UNION

UNION(collection1,collection2) 用于计算两个集合的并集。

示例：UNION(LIST(1,2),LIST(3,4)) 的结果是 LIST(1,2,3,4)。

### COALESCE

COALESCE(ele1,ele2,...) 用于返回第一个不为空的元素。

示例：COALESCE(null,null,1,null,2) 的结果是1。

### LISTITEM

LISTITEM(list,index) 用于获取list内，index位置的元素，下标从1开始。

示例：LISTITEM(LIST(1,2,3),2) 的结果为2。

### SIZE

SIZE(list) 用于返回集合的大小。

示例：SIZE(LIST(1,2,3)) 的结果为3。

### REPEAT

REPEAT(number,item) 用于构建一个将item重复number次的列表。

示例：REPEAT(3,'a') 的结果为 LIST('a','a','a')。

### FOREACH

FOREACH(list, func(\_)) 用于对list中每个元素应用第2个参数中的运算，得到一个新的list；第二个参数用 \_ 代表list中的单个元素。

示例1：FOREACH(LIST(1,2,3),\_\*2) 表示对list中的每个元素乘2，结果是 LIST(2,4,6)。

示例2：FOREACH(LIST('aaa','bb','c'),LEN(\_)) 表示对list中每个元素求长度，结果是 LIST(3,2,1)。

### **REPEAT**

REPEAT(number,item) 构建一个将 item 重复 number 次的列表。

示例：REPEAT(3,'a') 的结果为 LIST('a','a','a')。

## 日期函数

### DATEDELTA

DATEDELTA(date, deltadays) 用于将指定日期加或减指定天数，正数为增加，负数为减少。

示例1：DATEDELTA(date, 1) date的日期加一天。

示例2：DATEDELTA(date, - 1) date日期减一天。

### DATEDIF

DATEDIF(startDate, endDate, [unit]) 用于计算两个时间的差值。startDate和endDate为必填参数，Unit可选。

> **[!NOTE]**
>
> Unit可取值：
>
> - "y"：表示年数。
> - "M"：表示月数。
> - "d"：表示天数，默认值。
> - "h"：表示小时数。
> - "m"：表示分钟数。
> - "s"：表示秒数。

示例：DATEDIF('2020-01-01','2020-01-02','d') 结果是1天。

### DATE

DATE(string) 用于获得给定字符串代表的日期。

> **[!NOTE]**
>
> DATE(string)函数内的参数字符串支持以下格式：
>
> - yyyy-MM-dd HH:mm:ss
> - yyyy-MM-dd HH:mm
> - yyyy-MM-dd HH
> - yyyy-MM-dd

示例：DATE('2020-12-28 11:11:00') 返回该字符串代表的日期。

DATE(number) 用于获得给定时间戳（毫秒单位）代表的日期。

示例：DATE(1647592883824) 返回该时间戳（毫秒单位）代表的日期。

### YEAR

YEAR(date) 用于获取某日期内的年份信息。

示例：YEAR('2020-12-09') 的结果是2020。

### MONTH

MONTH(date)用于获取某日期内的月份信息，月份是介于1到12之间的整数。

示例：MONTH('2020-12-09 11:03:04') 的结果是12。

### DAY

DAY(date) 用于获取某个日期内的天数信息，获取的天数是介于1到31之间的整数。

示例：DAY('2020-01-02') 的结果是2。

### HOUR

HOUR(date) 用于获取某日期内的小时数信息。

示例：HOUR('2020-12-09 11:03:04') 的结果是11。

### MINUTE

MINUTE(date) 用于获取某日期内的分钟数信息。

示例：MINUTE('2020-12-09 12:03:04') 的结果是3。

### SECOND

SECOND(date) 用于返回某日期内的秒数信息。

示例：SECOND('2021-01-12 12:23:32') 返回32。

### NETWORKDAYS

NETWORKDAYS(startDate,endDate,[holidays]) 用于获取参数start\_date和end\_date之间完整的工作日数值，工作日不包括周末和参数holidays指定的假期。

示例：NETWORKDAYS('2020-12-26', '2021-01-01'， '2020-01-01') 的结果是4。

### NOW

NOW() 用于返回当前时间。

示例：NOW()。

### TIMESTAMP

TIMESTAMP(date) 用于将日期对象转换成时间戳，单位毫秒。

示例：TIMESTAMP('2020-12-23 12:23:34') 返回1608697414000。

### DATEFORMAT

DATEFORMAT(date,format) 用于将日期格式化为指定类型。

示例：DATEFORMAT(NOW(),'yyyy/MM/dd HH:mm:ss') 的结果是2020/01/02 17:02:30（依据当前时间）。

## 逻辑函数

### AND

AND(logic1, logic2..) 表示只要有一个参数是false就返回false，所有参数都为true才返回true；集合参数会被自动展开成多个参数，遇到`false`会自动短路。

示例：AND(true,false,true) 的结果是 false；AND(LIST(true,false,true)) 的结果也是false。

### EQ

EQ(value1, value2)表示如果value1和value2的值相等，则为true，否则为false。

示例：EQ('aa', 'aa')和EQ(1,1) 的结果为true。

### TRUE

TRUE() 返回true。

示例：TRUE()。

### FALSE

FALSE() 返回false。

示例：FALSE()。

### GE

GE(value1, value2) 表示如果value1大于等于value2返回true，反之则返回false。

示例：GE(2, 1)和GE(1, 1)的结果都是true。

### GT

GT(value1,value2) 表示如果value1大于value2则返回true，反之返回false。

示例：GT(2,1)的结果为true。

### IF

IF(logic, value1, value2) 表示如果logic为true，则返回value1， 否则返回value2。

示例：IF(70>=60, '及格', '不及格') 的结果是及格。

### ISEMPTY

ISEMPTY(param) 表示参数如果为空，则返回为true，反之则返回false。

示例：ISEMPTY(' ') 的结果为true。

### LE

LE(value1, value2) 表示如果value1小于等于value2则返回true，反之返回false。

示例：LE(1,2) 和LE(1,1)的结果都为true。

### LT

LT(value1,value2) 表示如果value1小于value2则返回true，反之返回false。

示例：LT(1,2) 的结果为true。

### NE

NE(value1, value2) 表示如果value1和value2的值不相等，则返回为true，否则返回false。

示例：NE(1,2) 的结果为false。

### NOT

NOT(logic) 表示获取参数的取反，如果参数是true,则返回false ，如果参数是false，则返回true。

示例：NOT(true) 的结果为false。

### OR

OR(logic1, logic2..) 表示只要有一个参数是true就返回true，所有参数都为false才返回false；集合参数会被自动展开成多个参数，遇到`true`会自动短路。

示例：OR(true,false) 的结果是true；OR(LIST(true,false)) 的结果是true。

### XOR

XOR(logic1, logic2) 表示异或运算，如果两个参数不一样则返回true，如果两个参数一样则返回false。

示例：XOR(true, true) 的结果为false。

## 数学函数

### ABS

ABS(number) 返回数字的绝对值。

示例：ABS(-123.456) 的结果为123.456。

### AVERAGE

AVERAGE(number1, number2, ...) 求数字的平均值。

示例：AVERAGE(1,2) 的结果为1.5。

### CEILING

CEILING(number, significance) 返回将参数number向上舍入（沿绝对值增大的方向）为最接近的指定基数的倍数。

示例：CEILING(22.43, 2) 向上取整到2的倍数，所以返回24。

### FIXED

FIXED(number) 将数字向下舍入到指定的小数位数。

示例：FIXED(10.8963, 2) 返回的结果是10.89。

### INT

INT(number)将数字向下舍入到最接近的整数。

示例：INT(3.45) 返回3；INT(-3.45) 返回-4。

### MAX

MAX(number1, number2, ...) 获取这组数字中的最大值。

示例：MAX(1, 4, 6.7, 10, 2) 返回10。

### MIN

MIN(number1, number2, ...) 返回数组中的最小值。

示例：MIN(1, 3, 5, 7, 2, 4) 返回1。

### MOD

MOD(number, divisor) 返回两数相除的余数。

示例：MOD(37, 6) 返回值为1。

### PI

PI() 返回圆周率3.14159265358979323846。

示例：计算半径长为r的圆的面积 PI() \* POWER(r, 2) 如果r=1，那么返回3.14159265358979323846。

### POWER

POWER(number, power) 返回数字乘幂的结果。

示例：POWER(2, 2) 的结果是4。

### PRODUCT

PRODUCT(number1, number2...) 函数将所有参数相乘并返回乘积。

示例：PRODUCT(2, 3) 的结果是6。

### RAND

RAND() 返回大于等于 0 且小于 1 的均匀分布随机实数。每一次触发计算都会变化。

示例：RAND() 的结果是0.601931207820683。

### ROUND

ROUND(number, numDigits) 将数字四舍五入到指定的位数。

示例：ROUND(1.2345, 2) 返回1.23；ROUND(12345, 2) 返回12345。

### SUM

SUM(number1, number2...) 函数将所有参数求和并返回，集合参数会被自动展开成多个参数。

示例：SUM(1.23, 1.45, 100) 返回102.68；SUM(LIST(1,2,3,4,5)) 的结果是15。

### NUMRANGE

NUMRANGE(number,start,end,[mode]) 判断number是否在区间中，mode表示区间模式。

> **[!NOTE]**
>
> 参数mode有以下取值：
>
> - "closed"：表示两侧闭区间，默认值。
> - "open"：表示两侧开区间。
> - "leftOpen"：表示左侧开区间，右侧闭区间。
> - "rightOpen"：表示左侧闭区间，右侧开区间。

示例：NUMRANGE(2,2,3) 的结果为true；NUMRANGE(2,2,3,'leftOpen') 的结果为false。

## 字符串函数

### CONCATENATE

CONCATENATE(text1, text2, text3...) 用于将多个字符串类型的参数拼接后返回新的字符串。

示例：CONCATENATE('A', 'B') 的结果为'AB'。

### CONTAIN

CONTAIN(text1, text2) 用于判断text1是否包含text2。

示例：CONTAIN('text1', 'text') 的结果为true。

### EXACT

EXACT(text1, text2) 用于判断字符串是否完全相等，如果相等则返回true；如果不相等则返回false，区分大小写。

示例：EXACT('abc', 'Abc') 返回false。

### LEFT

LEFT(text, number)表示从一个文本字符串的第一个字符开始返回指定个数的字符，如果字符个数不足，则抛出异常。

示例：LEFT('abcd', 2) 返回'ab'。

### LEN

LEN(text) 用于返回字符串长度。

示例：LEN('abc') 的结果为3。

### LOWER

LOWER(text) 用于将参数中的所有字母转换成小写字母并返回。

示例：LOWER('AbCd') 的结果是'abcd'。

### MID

MID(text, start, length) 用于返回文本字符串中从指定位置开始的特定数目的字符。

示例：MID('abcdefgh', 2, 3) 从位置2的地方返回3个字符，结果是'bcd'。

### REPLACE

REPLACE(oldText, startNum, numChars, newText) 用于将oldText的从startNum开始的numChars个字符替换成newText，startNum从1开始。

示例：REPLACE('12345678', 2, 3, 'ABCD') 结果是1ABCD5678。

### REPT

REPT(text, numberTimes) 用于将text重复numberTimes次数后返回。

示例：REPT('ABC', 2) 的结果是 'ABCABC'。

### RIGHT

RIGHT(text, numChar) 返回文本值中最右边的numChar个字符。

示例：RIGHT('12345', 2) 的结果为'45'。

### SPLIT

SPLIT(text, textSeparator) 用于将字符串分割。

示例：SPLIT('ABABAB', 'B') 的结果为 LIST('A','A','A')。

### STARTWITH

STARTWITH(text1, text2) 用于判断文本字符串是否以特定字符串开始。

示例：STARTWITH('ABCDEF', 'ABC') 返回true。

### TEXT

TEXT(number) 用于将其他类型数据转换为文本。TEXT(null) 的结果是空字符串。TEXT(number,string)将时间戳转换为对应日期格式的文本;TEXT(Date,string)将日期格式转换为对应日期格式的文本。

示例：TEXT(12) 的结果是'12'。TEXT(1608697414000,'yyyy') 的结果是 '2020'。TEXT(DATE('2020-12-28 11:11:00'),'yyyy')的结果是 '2020'。

### TRIM

TRIM(text) 用于删除字符串首尾的空格。

示例：TRIM(' ABCD ') 返回的结果是'ABCD'。

### UPPER

UPPER(text) 用于将文本字符串中的所有小写字母转换成大写字母。

示例：UPPER('AbCd') 返回结果是'ABCD'。

### VALUE

VALUE(text) 用于将文本转化成数字。

示例：VALUE('123') 的结果为123。

### GETUUID

GETUUID() 用于生成一个唯一的字符串。

示例：GETUUID() 的结果是1d6b3482-c9c3-41ef-a4c4-a7e634bfd205 （每次结果不一样）。

### MD5

MD5(text) 对一段文本进行MD5摘要，结果是一个128位散列值的16进制小写字符串。

示例：MD5('test') 的结果是098f6bcd4621d373cade4e832627b4f6。如果想要大写16进制的话可以使用UPPER(MD5('test'))，将结果转换为大小，得到的是098F6BCD4621D373CADE4E832627B4F6。

> **[!NOTE]**
>
> 使用MD5(text)方法时，如果参数传入的是null，返回的结果为空字符串。

### **JOIN**

JOIN(list, delimiter) 将数组列表转换为由delimiter分割的字符串。

示例：GET(LIST(1,2,3), ',') 返回的结果是 '1,2,3'。

### **TEXTREPLACE**

TEXTREPLACE(string, string, string) 将参数1里与参数2相匹配的字符替换成参数3。

示例：TEXTREPLACE('ABBC','B','b') 返回的结果是 'AbbC'

### **UNESCAPEHTML**

UNESCAPEHTML(string), 根据org.apache.commons.lang3.StringEscapeUtils.unescapeHtml4对HTML编码后的字符串进行解码。

示例：UNESCAPEHTML('{&quot;AgentId&quot;:23452345345&quot;'),结果为{'AgentId':23452345345}

## JSON函数

### JSONPARSE

JSONPARSE(jsonString) 用于转换json字符串为json对象。

示例：JSONPARSE(\" { 'key' : 'value' } \") 的结果是 {'key' : 'value'}。

### GET

GET(key, jsonObj) 用于获取jsonObj对应的value值，key为特殊字符时使用，key如果不是特殊字符可直接使用`.`获取对应的value值。

示例： GET('key-1', {'key-1':'value'}) 返回的结果是 'value'。

### **JACKSONJSONPATHEVAL**

JACKSONJSONPATHEVAL(object,jsonpath), 根据依赖jackson包的jsonpath从对象中取值,jsonpath参考<https://jsonpath.com/>。

示例：JACKSONJSONPATHEVAL(LIST(1,2,3), '$[0]')结果为第1个元素。

### **JSONTOSTRING**

JSONTOSTRING(object), 根据fastjson包的JSON.toJSONString将JSON对象转换为字符串。

示例：JSONTOSTRING({'a':'b'}),结果为'{'a':'b'}'。

## **加密函数**

### **BASE64**

BASE64(text,byteTransferWay,charSet) 对一段文本进行 BASE64 加密，默认结果是基于64个可打印字符来表示。其中byteTransferWay为：hexDecode、newString，若byteTransferWay为newString则charSet可填写为：UTF-8、UTF-16、ISO-8859-1等。BASE64(text) 与BASE64(text,'newString','UTF-8') 的结果相同。

示例：

- BASE64('test') 的结果是 dGVzdA==。

  如果想要大写16进制的话可以使用 UPPER(BASE64('test')), 它的结果是 DGVZDA==。
- BASE64('test','newString','UTF-8') 的结果是 dGVzdA==。

### **ENCRYPT**

ENCRYPT(key,iv,text) 对一段文本进行 AES 加密(CBC模式)。其中密钥key支持16/24/32bytes，偏移量iv支持16bytes，最后结果编码采用Hex。

示例：ENCRYPT('1234567890abcdef1234567890abcdef','1234567890abcdef','test') 的结果是 0168039dabbd88f5c9ebed1eed501465。

### **DECRYPT**

DECRYPT(key,iv,text) 对一段文本进行 AES 解密 (CBC模式)。其中密钥key支持16/24/32bytes,偏移量iv支持16bytes，最后结果编码采用Hex。

示例：DECRYPT('1234567890abcdef1234567890abcdef,'1234567890abcdef','0168039dabbd88f5c9ebed1eed501465') 的结果是 test。

### **SHA256**

SHA256(text) 对一段文本进行SHA256加密

示例：SHA256('test') 的结果是 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08。

### **URLENCODE**

URLENCODE(url) 对URL传递地址进行加密

示例：URLENCODE('https://test.com')的结果是 https%3A%2F%2Ftest.com。

### **HMACSHA256**

HMACSHA256( key, text, byteTransferWay, charSet) 对一段文本进行HMACSHA256加密，默认采用16进制（HexEncoder）对最终的byte结果进行字符串转换后返回，其中byteTransferWay为：hexEncode、newString,若byteTransferWay为newString则charSet可填写为：UTF-8、UTF-16、ISO-8859-1等。

示例：

- HMACSHA256('1234','test') 的结果是 24c4f0295e1bea74f9a5cb5bc40525c8889d11c78c4255808be00defe666671f
- HMACSHA256('1234','test','hexEncode') 的结果是 24c4f0295e1bea74f9a5cb5bc40525c8889d11c78c4255808be00defe666671f。

## **系统函数**

### **USERID2UNIONID**

USERID2UNIONID(corpId, userId) 通过corpId与userId获取unionId。

示例：USERID2UNIONID('dingxxxxxx', 'manager922') 返回的结果是unionId。

### **UNIONID2USERID**

UNIONID2USERID(corpId, unionId) 通过corpId与unionId获取userId。

示例：UNIONID2USERID('dingxxxxxx', 'w0PUiPIbZBR8904NbXtLG7wiEiE') 返回的结果是userId。

### **BATCHUSERID2UNIONID**

BATCHUSERID2UNIONID(corpId, userIdList) 通过corpId与userId列表批量获取unionId列表。

示例：BATCHUSERID2UNIONID('dingxxxxxx', ['manager922', 'manager923']) 返回的结果是unionId列表。

### **BATCHUNIONID2USERID**

BATCHUNIONID2USERID(corpId, unionIdList) 通过corpId与unionId列表批量获取userId列表。

示例：BATCHUNIONID2USERID('dingxxxxxx', ['w0PUiPIbZBR8904NbXtLG7wiEiE', 'w0PUiPIbZBR8904NbXtLG7wiEiF']) 返回的结果是userId列表。
