---
title: "删除知识库成员"
source_url: "https://open.dingtalk.com/document/development/delete-team-space-user-permissions"
namespace: "development"
slug: "delete-team-space-user-permissions"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 知识库 > 知识库权限管理 > 删除知识库成员"
doc_id: "70A4xfj1ja"
updated_at: "2025-09-08 19:07:04"
---

> Source: https://open.dingtalk.com/document/development/delete-team-space-user-permissions
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 知识库 > 知识库权限管理 > 删除知识库成员
> Updated: 2025-09-08 19:07:04

# 删除知识库成员

调用本接口，删除用户对知识库的权限。

> **[!IMPORTANT]**
>
> 1. 为了提升接口的使用体验, 知识库接口已升级。本文档已于2023年7月6日迁移至历史文档(不推荐)目录，接口不再支持新应用接入, 已接入的应用可继续调用。
>
>    - 如果未使用本接口，推荐使用[删除权限](https://open.dingtalk.com/document/orgapp/delete-permissions-file)接口。
>    - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。
> 2. 新老接口中的ID不兼容, 不支持混用。

![](https://img.alicdn.com/imgextra/i1/O1CN01UhT2B01URut2tG3oh_!!6000000002515-2-tps-2732-1582.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 知识库写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=doc_1.0%23DeleteWorkspaceMembers) |
| 第三方企业应用 | 支持 | 知识库写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=doc_1.0%23DeleteWorkspaceMembers) |
| 第三方个人应用 | 暂不支持 | 知识库写权限 | 暂不支持 |

## 请求方法

```
POST /v1.0/doc/workspaces/{workspaceId}/members/remove HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "operatorId" : "String",
  "members" : [ {
    "memberId" : "String",
    "memberType" : "String"
  } ]
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Path参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| workspaceId | String | 是 | 知识库ID。   - 企业内部应用，调用[新建知识库](https://open.dingtalk.com/document/orgapp/create-a-team-space)接口或者[查询用户有权限的知识库列表](https://open.dingtalk.com/document/orgapp/querying-the-list-of-user-team-spaces)接口获取的workspaceId字段值。 - 第三方企业应用，调用[新建知识库](https://open.dingtalk.com/document/isvapp/create-a-team-space)接口或者[查询用户有权限的知识库列表](https://open.dingtalk.com/document/isvapp/querying-the-list-of-user-team-spaces)接口获取的workspaceId字段值。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 发起添加权限操作用户的unionId。   - 企业内部应用，调用[查询用户详情](https://open.dingtalk.com/document/orgapp/query-user-details)接口获取unionid参数值。 - 第三方企业应用，调用[查询用户详情](https://open.dingtalk.com/document/isvapp/query-user-details)接口获取unionid参数值。 |
| members | Array | 是 | 被操作用户组。  **[!NOTE]**  可一次操作多个用户，最大数量限制50，超过数量限制会直接报错。 |
| memberId | String | 是 | 被删除的文档成员。   - memberType如果是**USER**，该参数值传员工的unionId。    - 企业内部应用，调用[查询用户详情](https://open.dingtalk.com/document/orgapp/query-user-details)接口获取unionid参数值。   - 第三方企业应用，调用[查询用户详情](https://open.dingtalk.com/document/isvapp/query-user-details)接口获取unionid参数值。 - memberType如果是**DEPT**，该参数值是传部门ID。    - 企业内部应用，调用[获取部门列表](https://open.dingtalk.com/document/orgapp/obtain-the-department-list-v2)接口获取dept\_id参数值。   - 第三方企业应用，调用[获取部门列表](https://open.dingtalk.com/document/isvapp/get-department-list)接口获取dept\_id参数值。 |
| memberType | String | 是 | 用户类型，取值：   - **USER**：用户 - **DEPT**：部门 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/doc/workspaces/YRBGxxx/members/remove HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:7dc9ec4xxx
Content-Type:application/json

{
  "operatorId" : "Q2xwPOxxx",
  "members" : [ {
    "memberId" : "Q2xwPOKixxx",
    "memberType" : "USER"
  } ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkdoc_1_0.*;
import com.aliyun.dingtalkdoc_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdoc_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdoc_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdoc_1_0.Client client = Sample.createClient();
        DeleteWorkspaceMembersHeaders deleteWorkspaceMembersHeaders = new DeleteWorkspaceMembersHeaders();
        deleteWorkspaceMembersHeaders.xAcsDingtalkAccessToken = "<your access token>";
        DeleteWorkspaceMembersRequest.DeleteWorkspaceMembersRequestMembers members0 = new DeleteWorkspaceMembersRequest.DeleteWorkspaceMembersRequestMembers()
                .setMemberId("Q2xwPOKixxx")
                .setMemberType("USER");
        DeleteWorkspaceMembersRequest deleteWorkspaceMembersRequest = new DeleteWorkspaceMembersRequest()
                .setOperatorId("Q2xwPOxxx")
                .setMembers(java.util.Arrays.asList(
                    members0
                ));
        try {
            client.deleteWorkspaceMembersWithOptions("YRBGxxx", deleteWorkspaceMembersRequest, deleteWorkspaceMembersHeaders, new RuntimeOptions());
        } catch (TeaException err) {
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        } catch (Exception _err) {
            TeaException err = new TeaException(_err.getMessage(), _err);
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        }        
    }
}
```

Python

```
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_dingtalk.doc_1_0.client import Client as dingtalkdoc_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.doc_1_0 import models as dingtalkdoc__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdoc_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdoc_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_workspace_members_headers = dingtalkdoc__1__0_models.DeleteWorkspaceMembersHeaders()
        delete_workspace_members_headers.x_acs_dingtalk_access_token = '<your access token>'
        members_0 = dingtalkdoc__1__0_models.DeleteWorkspaceMembersRequestMembers(
            member_id='Q2xwPOKixxx',
            member_type='USER'
        )
        delete_workspace_members_request = dingtalkdoc__1__0_models.DeleteWorkspaceMembersRequest(
            operator_id='Q2xwPOxxx',
            members=[
                members_0
            ]
        )
        try:
            client.delete_workspace_members_with_options('YRBGxxx', delete_workspace_members_request, delete_workspace_members_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_workspace_members_headers = dingtalkdoc__1__0_models.DeleteWorkspaceMembersHeaders()
        delete_workspace_members_headers.x_acs_dingtalk_access_token = '<your access token>'
        members_0 = dingtalkdoc__1__0_models.DeleteWorkspaceMembersRequestMembers(
            member_id='Q2xwPOKixxx',
            member_type='USER'
        )
        delete_workspace_members_request = dingtalkdoc__1__0_models.DeleteWorkspaceMembersRequest(
            operator_id='Q2xwPOxxx',
            members=[
                members_0
            ]
        )
        try:
            await client.delete_workspace_members_with_options_async('YRBGxxx', delete_workspace_members_request, delete_workspace_members_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

if __name__ == '__main__':
    Sample.main(sys.argv[1:])
```

PHP

```
<?php

// This file is auto-generated, don't edit it. Thanks.
namespace AlibabaCloud\SDK\Sample;

use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\DeleteWorkspaceMembersHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\DeleteWorkspaceMembersRequest\members;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\DeleteWorkspaceMembersRequest;
use AlibabaCloud\Tea\Utils\Utils\RuntimeOptions;

class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Dingtalk Client
     */
    public static function createClient(){
        $config = new Config([]);
        $config->protocol = "https";
        $config->regionId = "central";
        return new Dingtalk($config);
    }

    /**
     * @param string[] $args
     * @return void
     */
    public static function main($args){
        $client = self::createClient();
        $deleteWorkspaceMembersHeaders = new DeleteWorkspaceMembersHeaders([]);
        $deleteWorkspaceMembersHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $members0 = new members([
            "memberId" => "Q2xwPOKixxx",
            "memberType" => "USER"
        ]);
        $deleteWorkspaceMembersRequest = new DeleteWorkspaceMembersRequest([
            "operatorId" => "Q2xwPOxxx",
            "members" => [
                $members0
            ]
        ]);
        try {
            $client->deleteWorkspaceMembersWithOptions("YRBGxxx", $deleteWorkspaceMembersRequest, $deleteWorkspaceMembersHeaders, new RuntimeOptions([]));
        }
        catch (Exception $err) {
            if (!($err instanceof TeaError)) {
                $err = new TeaError([], $err->getMessage(), $err->getCode(), $err);
            }
            if (!Utils::empty_($err->code) && !Utils::empty_($err->message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }
        }
    }
}
$path = __DIR__ . \DIRECTORY_SEPARATOR . '..' . \DIRECTORY_SEPARATOR . 'vendor' . \DIRECTORY_SEPARATOR . 'autoload.php';
if (file_exists($path)) {
    require_once $path;
}
Sample::main(array_slice($argv, 1));
```

Go

```
// This file is auto-generated, don't edit it. Thanks.
package main

import (
  "os"
  util  "github.com/alibabacloud-go/tea-utils/service"
  dingtalkdoc_1_0  "github.com/alibabacloud-go/dingtalk/doc_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdoc_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdoc_1_0.Client{}
  _result, _err = dingtalkdoc_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  deleteWorkspaceMembersHeaders := &dingtalkdoc_1_0.DeleteWorkspaceMembersHeaders{}
  deleteWorkspaceMembersHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  members0 := &dingtalkdoc_1_0.DeleteWorkspaceMembersRequestMembers{
    MemberId: tea.String("Q2xwPOKixxx"),
    MemberType: tea.String("USER"),
  }
  deleteWorkspaceMembersRequest := &dingtalkdoc_1_0.DeleteWorkspaceMembersRequest{
    OperatorId: tea.String("Q2xwPOxxx"),
    Members: []*dingtalkdoc_1_0.DeleteWorkspaceMembersRequestMembers{members0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeleteWorkspaceMembersWithOptions(tea.String("YRBGxxx"), deleteWorkspaceMembersRequest, deleteWorkspaceMembersHeaders, &util.RuntimeOptions{})
    if _err != nil {
      return _err
    }

    return nil
  }()

  if tryErr != nil {
    var err = &tea.SDKError{}
    if _t, ok := tryErr.(*tea.SDKError); ok {
      err = _t
    } else {
      err.Message = tea.String(tryErr.Error())
    }
    if !tea.BoolValue(util.Empty(err.Code)) && !tea.BoolValue(util.Empty(err.Message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }

  }
  return _err
}

func main() {
  err := _main(tea.StringSlice(os.Args[1:]))
  if err != nil {
    panic(err)
  }
}
```

Node.js

```
// This file is auto-generated, don't edit it
import Util, * as $Util from '@alicloud/tea-util';
import dingtalkdoc_1_0, * as $dingtalkdoc_1_0 from '@alicloud/dingtalk/doc_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdoc_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdoc_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let deleteWorkspaceMembersHeaders = new $dingtalkdoc_1_0.DeleteWorkspaceMembersHeaders({ });
    deleteWorkspaceMembersHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let members0 = new $dingtalkdoc_1_0.DeleteWorkspaceMembersRequestMembers({
      memberId: "Q2xwPOKixxx",
      memberType: "USER",
    });
    let deleteWorkspaceMembersRequest = new $dingtalkdoc_1_0.DeleteWorkspaceMembersRequest({
      operatorId: "Q2xwPOxxx",
      members: [
        members0
      ],
    });
    try {
      await client.deleteWorkspaceMembersWithOptions("YRBGxxx", deleteWorkspaceMembersRequest, deleteWorkspaceMembersHeaders, new $Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.empty(err.code) && !Util.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

Client.main(process.argv.slice(2));
```

C#

```
// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

using Tea;
using Tea.Utils;

namespace AlibabaCloud.SDK.Sample
{
    public class Sample 
    {

        /**
         * 使用 Token 初始化账号Client
         * @return Client
         * @throws Exception
         */
        public static AlibabaCloud.SDK.Dingtalkdoc_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdoc_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DeleteWorkspaceMembersHeaders deleteWorkspaceMembersHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DeleteWorkspaceMembersHeaders();
            deleteWorkspaceMembersHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DeleteWorkspaceMembersRequest.DeleteWorkspaceMembersRequestMembers members0 = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DeleteWorkspaceMembersRequest.DeleteWorkspaceMembersRequestMembers
            {
                MemberId = "Q2xwPOKixxx",
                MemberType = "USER",
            };
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DeleteWorkspaceMembersRequest deleteWorkspaceMembersRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DeleteWorkspaceMembersRequest
            {
                OperatorId = "Q2xwPOxxx",
                Members = new List<AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DeleteWorkspaceMembersRequest.DeleteWorkspaceMembersRequestMembers>
                {
                    members0
                },
            };
            try
            {
                client.DeleteWorkspaceMembersWithOptions("YRBGxxx", deleteWorkspaceMembersRequest, deleteWorkspaceMembersHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
            }
            catch (TeaException err)
            {
                if (!AlibabaCloud.TeaUtil.Common.Empty(err.Code) && !AlibabaCloud.TeaUtil.Common.Empty(err.Message))
                {
                    // err 中含有 code 和 message 属性，可帮助开发定位问题
                }
            }
            catch (Exception _err)
            {
                TeaException err = new TeaException(new Dictionary<string, object>
                {
                    { "message", _err.Message }
                });
                if (!AlibabaCloud.TeaUtil.Common.Empty(err.Code) && !AlibabaCloud.TeaUtil.Common.Empty(err.Message))
                {
                    // err 中含有 code 和 message 属性，可帮助开发定位问题
                }
            }
        }

    }
}
```

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkdoc__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkdoc_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkdoc_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkdoc_1_0::Client> client = make_shared<Alibabacloud_Dingtalkdoc_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkdoc_1_0::DeleteWorkspaceMembersHeaders> deleteWorkspaceMembersHeaders = make_shared<Alibabacloud_Dingtalkdoc_1_0::DeleteWorkspaceMembersHeaders>();
  deleteWorkspaceMembersHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdoc_1_0::DeleteWorkspaceMembersRequestMembers> members0 = make_shared<Alibabacloud_Dingtalkdoc_1_0::DeleteWorkspaceMembersRequestMembers>(map<string, boost::any>({
    {"memberId", boost::any(string("Q2xwPOKixxx"))},
    {"memberType", boost::any(string("USER"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkdoc_1_0::DeleteWorkspaceMembersRequest> deleteWorkspaceMembersRequest = make_shared<Alibabacloud_Dingtalkdoc_1_0::DeleteWorkspaceMembersRequest>(map<string, boost::any>({
    {"operatorId", boost::any(string("Q2xwPOxxx"))},
    {"members", boost::any(vector<Alibabacloud_Dingtalkdoc_1_0::DeleteWorkspaceMembersRequestMembers>({
      members0
    }))}
  }));
  try {
    client->deleteWorkspaceMembersWithOptions(make_shared<string>("YRBGxxx"), deleteWorkspaceMembersRequest, deleteWorkspaceMembersHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

**返回示例**

```
HTTP/1.1 200 OK
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.inputArgs.overLimit | 批量操作数量超过限制 | 批量接口操作数量超限 |
| 400 | invalidRequest.permission.operationIllegal | 权限操作非法 | 权限操作非法，不能移除自己的权限，也不能移除所有者 |
| 400 | invalidRequest.inputArgs.invalid | 方法入参校验失败 | 方法入参校验失败，检查是否有必填参数未填，或者unionId是否合法等 |
| 403 | forbidden.user.notInOrg | 操作用户不在组织内 | 操作用户不在组织内 |
| 403 | forbidden.accessDenied | 用户无操作权限 | 用户无操作权限 |
| 404 | invalidRequest.resource.notFound | 资源找不到 | 资源找不到 |
| 404 | invalidRequest.workspace.deleted | 知识库已被删除 | 知识库已被删除 |
| 500 | internalError | 系统内部错误 | 系统内部错误 |
