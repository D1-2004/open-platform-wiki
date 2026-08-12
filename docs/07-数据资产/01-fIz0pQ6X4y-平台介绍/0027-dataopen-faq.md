---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/dataopen/dataopen-faq"
namespace: "dataopen"
slug: "dataopen-faq"
group: "数据资产"
tab: "平台介绍"
breadcrumb: "常见问题"
doc_id: "fzUkRGkpg2"
updated_at: "2026-08-12 09:23:57"
---

> Source: https://open.dingtalk.com/document/dataopen/dataopen-faq
> Path: 数据资产 / 平台介绍 / 常见问题
> Updated: 2026-08-12 09:23:57

# 常见问题

本文档主要介绍数据资产平台的常见问题

- **accessToken如何获取？**

  生成accessToken的方式如下，可参考：

  [](https://cloud.video.taobao.com/play/u/null/p/1/e/6/t/1/404182532501.mp4?SBizCode=xiaoer)
- **登录时出现“暂无权限提示”，怎么办？**

  如下方图，暂无权限提示 （请联系管理员在数据资产平台-权限审批管理中添加权限）

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0743171861/p619117.png)

  数据资产平台权限设计为首次登录，组织的主管理员默认拥有权限，需由组织管理员，在资产平台权限管理页面未其他人赋予对应的权限，才能有登录权限。

  权限体系请参考：**权限审批管理**

  数据资产平台作为企业统一管理自身数据资产的平台，引入了企业数据管理体系的3类角色，角色与权限如下：

  | **角色名称** | **权限说明** |
  | --- | --- |
  | 普通权限 | 数据的使用人角色，拥有数据资产平台各项功能的使用权限，如创建数据服务接口、生成数据图表等，一般授予开发、运营等职能 |
  | 数据审批人 | 数据的审批人角色，拥有对普通权限用户创建接口或图表后的业务审批权限，对数据的业务使用具有决定权，一般授予业务负责人 |
  | 数据安全接口人 | 企业的数据安全把关人，针对业务审批后的数据服务从数据安全角度做最后的把关，一般授予专职的数据安全负责人 |

  > **[!NOTE]**
  >
  > 在数据资产平台打包数据服务之前，首先需要添加好本组织的数据审批人、数据安全接口人，只有有完整的接口人角色，才能完成数据服务的流程审批。
- **调用时，显示ip没有在白名单范围，怎么办？**

  调用的ip不在白名单内，在如上图开发管理页面添加对应ip即可。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0743171861/p619121.png)
- **没有调用该接口的权限**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0743171861/p619113.png)

  在接口调用时，需前置增加数据目录的数据资产平台数据服务接口权限。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0743171861/p619139.png)
- **调用数据资产平台的接口获取到的dataList是空的****是什么情况？**

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2219314961/p715698.png)

  当前查询条件没有查到数据的情况下，dataList会返回为空，请检查下查询条件。
- **为什么调用数据资产平台的接口没有返回全部字段****？**

  如果返回数据中有字段值为NULL的字段，开放平台网关会自动进行过滤，不返回。

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2219314961/p715714.png)
- **为什么调用数据资产平台的接口****一次最多只能返回最多50条数据****？**

  基于平台数据安全及稳定性的机制，一次最多只能返回最多50条数据，需要获取全量数据，需要分页轮询调用接口，直到dataList为空为止。注：需要注意轮询时间间隔，太快会触发限流。
