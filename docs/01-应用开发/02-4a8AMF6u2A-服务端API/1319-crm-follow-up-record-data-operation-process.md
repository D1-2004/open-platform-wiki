---
title: "CRM跟进记录数据操作流程"
source_url: "https://open.dingtalk.com/document/development/crm-follow-up-record-data-operation-process"
namespace: "development"
slug: "crm-follow-up-record-data-operation-process"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 使用教程 > CRM跟进记录数据操作流程"
doc_id: "d3t5nVXO1X"
updated_at: "2025-09-23 19:25:42"
---

> Source: https://open.dingtalk.com/document/development/crm-follow-up-record-data-operation-process
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 使用教程 > CRM跟进记录数据操作流程
> Updated: 2025-09-23 19:25:42

# CRM跟进记录数据操作流程

本文档介绍了CRM跟进记录数据操作流程。

## 流程简介

本文档介绍了如何调用客户管理接口查询CRM跟进记录数据等流程。首先创建一个企业内部应用，再使用客户管理提供的API，实现获取跟进记录对象的元数据、根据指定条件查询跟进记录数据、批量获取跟进记录数据流程。

步骤一：登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](https://open.dingtalk.com/document/orgapp/create-orgapp)。

步骤二：获取AppKey和AppSecret。

步骤三：[申请客户管理接口权限](https://open.dingtalk.com/document/orgapp/apply-for-crm-api-permission)。搜索“CRM”，申请相应的权限。

步骤四：获取应用访问凭证[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)。

步骤五：调用服务端跟进记录相关API。

1. 调用服务端API-[获取跟进记录对象的元数据](https://open.dingtalk.com/document/orgapp/obtains-the-metadata-description-of-the-crm-follow-up-record-object)接口，获取客户管理跟进记录元数据信息。
2. 调用服务端API-[根据指定条件查询跟进记录数据](https://open.dingtalk.com/document/orgapp/query-and-dingtalk-data-of-track-records-in-apsara-stack)接口，查询符合指定条件的跟进记录数据。
3. 调用服务端API-[根据ID列表批量获取跟进记录数据](https://open.dingtalk.com/document/orgapp/dingtalk-the-primary-data-of-apsara-stack-agility-paas-allows-you)接口，查询多个跟进记录数据。

## 步骤一：创建企业内部应用

> **[!NOTE]**
>
> 如果已有企业内部应用，可直接使用已有应用，可忽略此步骤。

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](https://open.dingtalk.com/document/orgapp/create-orgapp)。

   ![0815创建企业内部应用 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5513450661/p477411.png)
2. 填写应用的基本信息，然后单击**确定创建**。

   - 应用类型：选择**H5微应用**
   - 开发方式：选择**企业自主开发**

   ![2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5882109661/p522021.png)

## 步骤二：获取AppKey和AppSecret

获取AppKey和AppSecret。![0815获取Appkey值 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5513450661/p477413.png)

## 步骤三：添加接口权限

[申请客户管理接口权限](https://open.dingtalk.com/document/orgapp/apply-for-crm-api-permission)。搜索“CRM”，申请相应的权限。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9544125661/p499403.png)

## 步骤四：获取应用访问凭证accessToken

根据步骤二中的AppKey和AppSecret，获取应用访问凭证[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)。

> **[!NOTE]**
>
> 服务端API差异详情参见[新旧版规范服务端API区别](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。
>
> - 服务端API接口SDK下载，详情参见[服务端SDK下载](https://open.dingtalk.com/document/orgapp/download-the-server-side-sdk)。
> - 新版服务端API接口SDK下载，详情参见[新版服务端SDK下载](https://open.dingtalk.com/document/orgapp/sdk-download)。
>
> 以下接口均使用服务端API接口，SDK下载详情参见[服务端SDK下载](https://open.dingtalk.com/document/orgapp/download-the-server-side-sdk)。

```
public void  getAccessToken() throws ApiException {
        DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/gettoken");
        OapiGettokenRequest request = new OapiGettokenRequest();
        request.setAppkey("dingmp*****lxhgn");
        request.setAppsecret("9G_O44ATuwq9jrz3o********0t1JDf0Qq3neNDLmxamBkhgGIO");
        request.setHttpMethod("GET");
        OapiGettokenResponse response = client.execute(request);
        System.out.println(response.getBody());
    }
```

## 步骤五：调用服务端跟进记录相关API

1. 调用服务端API-[获取跟进记录对象的元数据](https://open.dingtalk.com/document/orgapp/obtains-the-metadata-description-of-the-crm-follow-up-record-object)接口，获取客户管理跟进记录元数据信息。

   ```
   public void customerFollowRecordObjectMeta() throws Exception {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectmeta/followrecord/describe");
           OapiCrmObjectmetaFollowrecordDescribeRequest req = new OapiCrmObjectmetaFollowrecordDescribeRequest();
           OapiCrmObjectmetaFollowrecordDescribeResponse rsp = client.execute(req, access_token);
           System.out.println(rsp.getBody());
   }
   ```
2. 调用服务端API-[根据指定条件查询跟进记录数据](https://open.dingtalk.com/document/orgapp/query-and-dingtalk-data-of-track-records-in-apsara-stack)接口，查询符合指定条件的跟进记录数据。

   ```
   public void queryCustomerFollowRecord() throws Exception {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/followrecord/query");
           OapiCrmObjectdataFollowrecordQueryRequest req = new OapiCrmObjectdataFollowrecordQueryRequest();
           req.setCurrentOperatorUserid("user01");
           req.setCursor("0");
           req.setPageSize(100L);
           OapiCrmObjectdataFollowrecordQueryResponse rsp = client.execute(req, access_token);
           System.out.println(rsp.getBody());
   }
   ```
3. 调用服务端API-[根据ID列表批量获取跟进记录数据](https://open.dingtalk.com/document/orgapp/dingtalk-the-primary-data-of-apsara-stack-agility-paas-allows-you)接口，查询多个跟进记录数据。

   ```
   public void getCustomerFollowRecordByInstanceIds() throws Exception {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/followrecord/list");
           OapiCrmObjectdataFollowrecordListRequest req = new OapiCrmObjectdataFollowrecordListRequest();
           req.setCurrentOperatorUserid("user01");
           req.setDataIdList("INST_XX1,INST_XX2");
           OapiCrmObjectdataFollowrecordListResponse rsp = client.execute(req, access_token);
           System.out.println(rsp.getBody());
   }
   ```
