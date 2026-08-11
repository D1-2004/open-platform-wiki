---
title: "企业授权变更事件"
source_url: "https://open.dingtalk.com/document/development/event-org-suite-relieve"
namespace: "development"
slug: "event-org-suite-relieve"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "身份与免登 > 企业授权变更事件"
doc_id: "Jp8IHYvfwx"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-org-suite-relieve
> Path: 应用开发 / 事件订阅 / 身份与免登 > 企业授权变更事件
> Updated: 2022-01-19 19:29:22

# 企业授权变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业授权变更事件 |
| 英文名称 | org\_suite\_change |

## 功能描述

数据为企业授权应用的最新状态，企业授权变更事件表示企业变更第三方企业应用的授权范围。其中auth\_corp\_info， auth\_info和auth\_user\_info三段结构信息请参考[获取企业授权信息](https://open.dingtalk.com/document/isvapp/obtains-the-basic-information-of-an-enterprise)。auth\_scope结构信息请参考[获取通讯录权限范围](https://open.dingtalk.com/document/isvapp/obtain-corpsecret-authorization-scope)。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "org_suite_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "authCorpInfo": {
      "authChannel": "4",
      "corpid": "dingb2b068b57xxxxxx288",
      "corpType": 0,
      "fullCorpName": "测试组织",
      "corpTypeV2": 2,
      "industry": "互联网",
      "corpName": "测试组织",
      "isAuthenticated": true,
      "licenseCode": "xxx",
      "corpLogoUrl": "https://static-legacy.dingtalk.com/xxx",
      "inviteUrl": "https://wx.dingtalk.com/invite-page/xxx",
      "inviteCode": "dada2xdaflgf",
      "isEcologicalCorp": false,
      "authLevel": 2,
      "authChannelType": "STAR_ACTIVITY"
    },
    "permanentCode": "68QKuTAkgHRSMOyCxoYZyNXXXX",
    "authUserInfo": {
      "userId": "managerxxx92"
    },
    "authScope": {
      "errcode": 0,
      "authUserField": [
        "jobnumber"
      ],
      "authOrgScopes": {
        "errmsg": "ok",
        "authedDept": [
          1
        ]
      }
    },
    "authInfo": {
      "agent": [
        {
          "agentid": 2574805120,
          "adminList": [
            "182937xxx"
          ],
          "appid": "1000",
          "agentName": "测试应用",
          "logoUrl": "https://staticXXX.jpg"
        }
      ]
    }
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data中。

### **biz\_data数据示例(biz\_type=4)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 4,
  "biz_data": {
    "auth_user_info": {
      "userId": "managerxxx92"
    },
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "auth_corp_info": {
      "corp_type": 0,
      "corpid": "dingb2b068b57xxxxxx288",
      "auth_level": 2,
      "auth_channel": "4",
      "industry": "互联网",
      "full_corp_name": "测试组织",
      "corp_name": "测试组织",
      "is_ecological_corp": false,
      "invite_url": "https://wx.dingtalk.com/invite-page/xxx",
      "auth_channel_type": "STAR_ACTIVITY",
      "invite_code": "dada2xdaflgf",
      "corp_type_v2": 2,
      "is_authenticated": true,
      "license_code": "xxx",
      "corp_logo_url": "https://static-legacy.dingtalk.com/xxx"
    },
    "syncAction": "org_suite_change",
    "auth_scope": {
      "errcode": 0,
      "auth_user_field": [
        "jobnumber"
      ],
      "auth_org_scopes": {
        "authed_dept": [
          1
        ],
        "errmsg": "ok"
      }
    },
    "auth_info": {
      "agent": [
        {
          "agentid": 2574805120,
          "agent_name": "测试应用",
          "logo_url": "https://staticXXX.jpg",
          "appid": "1000",
          "admin_list": [
            "182937xxx"
          ]
        }
      ]
    },
    "permanent_code": "68QKuTAkgHRSMOyCxoYZyNXXXX"
  }
}
```
