---
title: "CRM客户群操作流程"
source_url: "https://open.dingtalk.com/document/development/crm-customer-group-operation-process"
namespace: "development"
slug: "crm-customer-group-operation-process"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 使用教程 > CRM客户群操作流程"
doc_id: "eXcenZ0ww1"
updated_at: "2025-09-23 19:25:44"
---

> Source: https://open.dingtalk.com/document/development/crm-customer-group-operation-process
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 使用教程 > CRM客户群操作流程
> Updated: 2025-09-23 19:25:44

# CRM客户群操作流程

本文档介绍了CRM客户群操作流程。

> **[!NOTE]**
>
> 本文档以企业内部应用实现为例，第三方企业应用实现流程与本文档流程一致。

## 流程简介

本文档介绍了如何调用客户管理接口创建CRM客户群等流程。首先创建一个企业内部应用，再使用客户管理提供的API，实现创建客户群组、更新客户群组、获取单个客户群组详情、查询客户群组列表、创建客户群、获取单个客户群详情、批量查询客户群、查询客户群列表流程。

步骤一：登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](https://open.dingtalk.com/document/orgapp/create-orgapp)。

步骤二：获取AppKey和AppSecret。

步骤三：[申请客户管理接口权限](https://open.dingtalk.com/document/orgapp/apply-for-crm-api-permission)。搜索“CRM”，申请相应的权限。

步骤四：获取应用访问凭证[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)。

步骤五：调用服务端客户群组、客户群相关API。

客户群组相关API：

1. 调用服务端API-[创建客户群组](https://open.dingtalk.com/document/orgapp/crm-create-group)接口，进行创建客户群组，获取客户群组`openGroupSetId`。
2. 根据客户群组`openGroupSetId`进行客户群组管理操作。

   - 根据客户群组`openGroupSetId`，调用服务端API-[更新客户群组](https://open.dingtalk.com/document/orgapp/crm-update-group)接口，进行更新客户群组。
   - 根据客户群组`openGroupSetId`，调用服务端API-[获取单个客户群组详情](https://open.dingtalk.com/document/orgapp/queries-the-details-of-a-single-customer-group)接口，进行查询单个客户群组详情。
3. 调用服务端API-[查询客户群组列表](https://open.dingtalk.com/document/orgapp/query-groups)接口，进行查询客户群组列表。

客户群相关API：

1. 调用服务端API-[创建客户群](https://open.dingtalk.com/document/orgapp/create-a-customer-group)接口，进行创建客户群。
2. 根据客户群`openConversationId`进行客户群管理操作。

   - 根据客户群`openConversationId`，调用服务端API-[获取单个客户群详情](https://open.dingtalk.com/document/orgapp/obtain-a-single-customer-group)接口，进行获取单个客户群详情。
   - 根据客户群`openConversationId`，调用服务端API-[批量查询客户群](https://open.dingtalk.com/document/orgapp/query-customer-groups-in-batches)接口，进行批量批量查询客户群详情。
3. 调用服务端API-[查询客户群列表](https://open.dingtalk.com/document/orgapp/query-the-list-of-customer-groups)接口，进行查询客户群列表。

## 步骤一：创建企业内部应用

> **[!NOTE]**
>
> 如果已有企业内部应用，可直接使用已有应用，可忽略此步骤。

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](https://open.dingtalk.com/document/orgapp/create-orgapp)。

   ![0815创建企业内部应用 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5513450661/p477411.png)
2. 填写应用的基本信息，然后单击**确定创建**。

   - 应用类型：选择**H5微应用**
   - 开发方式：选择**企业自主开发**![2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8613109661/p522029.png)

## 步骤二：获取AppKey和AppSecret

获取AppKey和AppSecret。![0815获取Appkey值 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5513450661/p477413.png)

## 步骤三：添加接口权限

[申请客户管理接口权限](https://open.dingtalk.com/document/orgapp/apply-for-crm-api-permission)。搜索“CRM”，申请相应的权限。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9544125661/p499403.png)

## 步骤四：获取应用访问凭证accessToken

根据步骤二中的AppKey和AppSecret，获取应用访问凭证[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)。

> **[!NOTE]**
>
> 服务端API差异详情参见[新旧版规范服务端API区别](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。
>
> - 服务端API接口SDK下载，详情参见[服务端SDK下载](https://open.dingtalk.com/document/orgapp/download-the-server-side-sdk)。
> - 新版服务端API接口SDK下载，详情参见[新版服务端SDK下载](https://open.dingtalk.com/document/orgapp/sdk-download)。
>
> 以下接口均使用新版服务端API接口，SDK下载详情参见[新版服务端SDK下载](https://open.dingtalk.com/document/orgapp/sdk-download)。

```
public void getAccessToken() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        com.aliyun.dingtalkoauth2_1_0.Client client = new com.aliyun.dingtalkoauth2_1_0.Client(config);
        GetAccessTokenRequest accessTokenRequest = new GetAccessTokenRequest()
                .setAppKey("din*********hgn")
                .setAppSecret("9G_O************mBkhgGIO");
        GetAccessTokenResponse accessToken = client.getAccessToken(accessTokenRequest);
        System.out.println(JSON.toJSONString(accessToken.getBody()));
    }
```

## 步骤五：调用服务端客户群组、客户群相关API

### **客户群组相关API：**

1. 调用服务端API-[创建客户群组](https://open.dingtalk.com/document/orgapp/crm-create-group)接口，进行创建客户群组，获取客户群组openGroupSetId。

   ```
   public void createCustomerGroupSet() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           CreateGroupSetHeaders createGroupSetHeaders = new CreateGroupSetHeaders();
           createGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
           CreateGroupSetRequest createGroupSetRequest = new CreateGroupSetRequest()
                   .setName("群组名")
                   .setOwnerUserId("301227837930")
                   .setCreatorUserId("301227837930")
                   .setMemberQuota(100)
                   .setManagerUserIds("301227837930,301227837935")
                   .setNotice("公告")
                   .setNoticeToped(1)
                   .setRelationType("crm_customer_personal")
                   .setWelcome("欢迎加入");
           try {
               CreateGroupSetResponse groupSetWithOptions = client.createGroupSetWithOptions(createGroupSetRequest, createGroupSetHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(groupSetWithOptions.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```
2. 根据客户群组`openGroupSetId`进行客户群组管理操作。

   - 根据客户群组openGroupSetId，调用服务端API-[更新客户群组](https://open.dingtalk.com/document/orgapp/crm-update-group)接口，进行更新客户群组。

     ```
      public void updateCustomerGroupSet() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             UpdateGroupSetHeaders updateGroupSetHeaders = new UpdateGroupSetHeaders();
             updateGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
             UpdateGroupSetRequest updateGroupSetRequest = new UpdateGroupSetRequest()
                     .setOpenGroupSetId("dfgfghfghdsfdsf")
                     .setName("营销群")
                     .setMemberQuota(200)
                     .setOwnerUserId("301227837938")
                     .setManagerUserIds("301227837938")
                     .setNotice("公告")
                     .setNoticeToped(1)
                     .setWelcome("欢迎入群");
             try {
                 UpdateGroupSetResponse updateGroupSetResponse = client.updateGroupSetWithOptions(updateGroupSetRequest, updateGroupSetHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(updateGroupSetResponse.getBody()));
             } catch (TeaException err) {
                 if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                     // err 中含有 code 和 message 属性，可帮助开发定位问题
                     System.out.println(err.code);
                     System.out.println(err.message);
                 }
             } catch (Exception _err) {
                 TeaException err = new TeaException(_err.getMessage(), _err);
                 if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                     // err 中含有 code 和 message 属性，可帮助开发定位问题
                     System.out.println(err.code);
                     System.out.println(err.message);
                 }
             }
         }
     ```
   - 根据客户群组`openGroupSetId`，调用服务端API-[获取单个客户群组详情](https://open.dingtalk.com/document/orgapp/queries-the-details-of-a-single-customer-group)接口，进行查询单个客户群组详情。

     ```
      public void getCustomerGroupSet() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             GetGroupSetHeaders getGroupSetHeaders = new GetGroupSetHeaders();
             getGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
             GetGroupSetRequest getGroupSetRequest = new GetGroupSetRequest()
                     .setOpenGroupSetId("OkldZxxxx");
             try {
                 GetGroupSetResponse groupSetWithOptions = client.getGroupSetWithOptions(getGroupSetRequest, getGroupSetHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(groupSetWithOptions.getBody()));
             } catch (TeaException err) {
                 if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                     // err 中含有 code 和 message 属性，可帮助开发定位问题
                     System.out.println(err.code);
                     System.out.println(err.message);
                 }
             } catch (Exception _err) {
                 TeaException err = new TeaException(_err.getMessage(), _err);
                 if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                     // err 中含有 code 和 message 属性，可帮助开发定位问题
                     System.out.println(err.code);
                     System.out.println(err.message);
                 }
             }
         }
     ```
3. 调用服务端API-[查询客户群组列表](https://open.dingtalk.com/document/orgapp/query-groups)接口，进行查询客户群组列表。

   ```
   public void queryCustomerGroupSets() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           ListGroupSetHeaders listGroupSetHeaders = new ListGroupSetHeaders();
           listGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
           ListGroupSetRequest listGroupSetRequest = new ListGroupSetRequest()
                   .setNextToken("fasafsafsd")
                   .setMaxResults(10)
                   .setQueryDsl("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"filterType\":\"SEARCH\",\"value\":\"XX\",\"fieldId\":\"name\"}]}]}")
                   .setRelationType("crm_customer_personal");
           try {
               ListGroupSetResponse listGroupSetResponse = client.listGroupSetWithOptions(listGroupSetRequest, listGroupSetHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(listGroupSetResponse.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```

### **客户群相关API：**

1. 调用服务端API-[创建客户群](https://open.dingtalk.com/document/orgapp/create-a-customer-group)接口，进行创建客户群。

   ```
   public void createCustomerGroup() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           CreateGroupHeaders createGroupHeaders = new CreateGroupHeaders();
           createGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
           CreateGroupRequest createGroupRequest = new CreateGroupRequest()
                   .setGroupName("abc")
                   .setOwnerUserId("abc123")
                   .setMemberUserIds("a,b,c")
                   .setRelationType("abc");
           try {
               CreateGroupResponse groupWithOptions = client.createGroupWithOptions(createGroupRequest, createGroupHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(groupWithOptions.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```
2. 根据客户群`openConversationId`进行客户群管理操作。

   - 根据客户群openConversationId，调用服务端API-[获取单个客户群详情](https://open.dingtalk.com/document/orgapp/obtain-a-single-customer-group)接口，进行获取单个客户群详情。

     ```
        public void getCustomerGroup() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             GetCrmGroupChatSingleHeaders getCrmGroupChatSingleHeaders = new GetCrmGroupChatSingleHeaders();
             getCrmGroupChatSingleHeaders.xAcsDingtalkAccessToken = "<your access token>";
             GetCrmGroupChatSingleRequest getCrmGroupChatSingleRequest = new GetCrmGroupChatSingleRequest()
                     .setOpenConversationId("afasd1321");
             try {
                 GetCrmGroupChatSingleResponse crmGroupChatSingleWithOptions = client.getCrmGroupChatSingleWithOptions(getCrmGroupChatSingleRequest, getCrmGroupChatSingleHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(crmGroupChatSingleWithOptions.getBody()));
             } catch (TeaException err) {
                 if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                     // err 中含有 code 和 message 属性，可帮助开发定位问题
                     System.out.println(err.code);
                     System.out.println(err.message);
                 }
             } catch (Exception _err) {
                 TeaException err = new TeaException(_err.getMessage(), _err);
                 if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                     // err 中含有 code 和 message 属性，可帮助开发定位问题
                     System.out.println(err.code);
                     System.out.println(err.message);
                 }
             }
         }
     ```
   - 根据客户群`openConversationId`，调用服务端API-[批量查询客户群](https://open.dingtalk.com/document/orgapp/query-customer-groups-in-batches)接口，进行批量批量查询客户群详情。

     ```
       public void batchGetCustomerGroups() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             GetCrmGroupChatMultiHeaders getCrmGroupChatMultiHeaders = new GetCrmGroupChatMultiHeaders();
             getCrmGroupChatMultiHeaders.xAcsDingtalkAccessToken = "<your access token>";
             GetCrmGroupChatMultiRequest getCrmGroupChatMultiRequest = new GetCrmGroupChatMultiRequest()
                     .setOpenConversationIds(java.util.Arrays.asList(
                             "cidQJKDN****=="
                     ));
             try {
                 GetCrmGroupChatMultiResponse crmGroupChatMultiWithOptions = client.getCrmGroupChatMultiWithOptions(getCrmGroupChatMultiRequest, getCrmGroupChatMultiHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(crmGroupChatMultiWithOptions.getBody()));
             } catch (TeaException err) {
                 if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                     // err 中含有 code 和 message 属性，可帮助开发定位问题
                     System.out.println(err.code);
                     System.out.println(err.message);
                 }
             } catch (Exception _err) {
                 TeaException err = new TeaException(_err.getMessage(), _err);
                 if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                     // err 中含有 code 和 message 属性，可帮助开发定位问题
                     System.out.println(err.code);
                     System.out.println(err.message);
                 }
             }
         }
     ```
3. 调用服务端API-[查询客户群列表](https://open.dingtalk.com/document/orgapp/query-the-list-of-customer-groups)接口，进行查询客户群列表。

   ```
    public void queryCustomerGroups() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           QueryCrmGroupChatsHeaders queryCrmGroupChatsHeaders = new QueryCrmGroupChatsHeaders();
           queryCrmGroupChatsHeaders.xAcsDingtalkAccessToken = "<your access token>";
           QueryCrmGroupChatsRequest queryCrmGroupChatsRequest = new QueryCrmGroupChatsRequest()
                   .setRelationType("crm_customer_personal")
                   .setNextToken("fasdfs1")
                   .setMaxResults(10)
                   .setQueryDsl("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"filterType\":\"SEARCH\",\"value\":\"测试客户群\",\"fieldId\":\"name\"},{\"filterType\":\"LT\",\"value\":\"2640002249001\",\"fieldId\":\"gmtCreate\"}]}],\"orderByFields\":[{\"orderByFieldId\":\"gmtCreate\",\"orderByDirection\":\"ASC\"}]}");
           try {
               QueryCrmGroupChatsResponse queryCrmGroupChatsResponse = client.queryCrmGroupChatsWithOptions(queryCrmGroupChatsRequest, queryCrmGroupChatsHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(queryCrmGroupChatsResponse.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```
