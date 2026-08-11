---
title: "知识向量存储私有化"
source_url: "https://open.dingtalk.com/document/aipass/privatization-of-knowledge-vector-storage-1"
namespace: "aipass"
slug: "privatization-of-knowledge-vector-storage-1"
group: "AI PaaS"
tab: "AI 助理创建平台"
breadcrumb: "AI 技能 > 知识 > 知识维护 > 知识向量存储私有化"
doc_id: "V6XnCXnYYV"
updated_at: "2025-09-23 19:20:13"
---

> Source: https://open.dingtalk.com/document/aipass/privatization-of-knowledge-vector-storage-1
> Path: AI PaaS / AI 助理创建平台 / AI 技能 > 知识 > 知识维护 > 知识向量存储私有化
> Updated: 2025-09-23 19:20:13

# 知识向量存储私有化

本文档将帮助你掌握配置知识向量存储私有化的流程。

**适用人群**：**开发者** ；**适用范围**：**组织内创建的 AI 助理**

## **方案简介**

该方案将通过阿里云原生数据库 AnalyticDB 实现。

## **前提条件**

1. 已开通钉钉 **AI 生产力平台定制版**。
2. 了解[云原生数据库 AnalyticDB](https://help.aliyun.com/zh/analyticdb-for-postgresql/getting-started/overview-getting-started?spm=a2c4g.11186623.0.0.33804993o6gRXi)。

## **操作步骤**

1. 登录[云原生数据仓库 PostgreSQL版](https://common-buy.aliyun.com/?commodityCode=GreenplumPre&regionId=cn-zhangjiakou&spm=5176.13690186.commonbuy2container.GreenplumPost_ZjqTabLinks_0.710e778bLPXR3J#/buy)购买页面。
2. 选择购买配置：

   | **配置项** | | **说明** |
   | --- | --- | --- |
   | 商品类型 | | 按需选择。 |
   | 商品规格 | 地域和可用区 | 选择：中国 > 华北3（张家口）。 |
   | 实例资源类型 | 选择：存储弹性模式。 |
   | 引擎版本 | 选择：6.0标准版。 |
   | 产品类型 | 默认标准版。 |
   | 实例系列 | 选择：高可用版。 |
   | 向量引擎优化 | 选择：开启。 |
   | master资源 | 选择：8 CU。 |
   | 节点规格 | 选择：8 核 32 GB 及以上。 |
   | 节点数量 | 选择：2及以上。 |
   | 磁盘存储类型 | 选择：ESSD云盘 PL1。 |
   | 加密类型 | 选择：不加密。 |
   | 节点存储容量 | 建议 500 G 以上。  后续可扩容。 |
   | 网络类型 | 默认专有网络。 |
   | 专有网络 | 创建新的专有网络：  1. 单击  **如需创建新的专有网络，您可点击创建>**  image 2. 填写专有网络名称和交换机名称，点击确定即可。  image |
   | 专有网络交换机 | 选择上述完成创建的专有网络交换机。 |
   | 资源组 | 选择：默认资源组。 |
   | SSL加密 | 选择：关闭 SSL 加密。 |
   | 样本数据 | 选择：不加载 |
   | 服务关联角色 | 按需配置。 |
   | 购买时长 | | 按需选择。 |
3. 购买完成后，进入数据库实例页面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0124157371/p908209.png)
4. 确认引擎版本，引擎内核版本需为v6.6.2.2及以上，v7.x.x.x以下。
5. 在实例详情页申请数据库公网连接地址，单击左侧"数据安全性"选项，将钉钉生产网络配置到白名单，详情参考[设置白名单](https://help.aliyun.com/zh/analyticdb/analyticdb-for-postgresql/user-guide/configure-an-ip-address-whitelist-user-guide?spm=a2c4g.11186623.0.0.659627c3BgUCNq)。

   ```
   42.120.75.160/27,42.120.72.0/24,42.120.74.128/25,42.120.74.80/29,140.205.11.224/27,42.120.74.0/24,42.120.74.88/29,42.120.74.64/28,42.120.74.0/26,42.120.75.192/28,42.120.75.0/26,140.205.11.0/27,42.120.74.96/27
   ```
6. 创建用户账号，详情参考[创建和管理用户](https://help.aliyun.com/zh/analyticdb-for-postgresql/user-guide/create-a-database-account-user-guide?spm=a2c4g.11186623.0.0.94b677baSZtWKz#task-bhh-2mr-52b)。
7. 通过 DMS 的方式登录数据库，详情参考[客户端连接](https://help.aliyun.com/zh/analyticdb/analyticdb-for-postgresql/user-guide/client-connection/?spm=a2c4g.11186623.0.0.94b677baMGmWQG#concept-ncj-gmr-52b)：

   | **图例** | **说明** |
   | --- | --- |
   | image | - gp-8vb67q30f73609834：实例ID - doc2bot\_no1：数据库名 - public：schema - chunk\_index/chunk\_detail：表 |
8. 创建表和索引：

   > **[!NOTE]**
   >
   > - 数据库名可自定义。
   > - schema 保持为 public。
   > - 表名 chunk\_index 和 chunk\_detail 也不要更改

   | **表** | **说明** |
   | --- | --- |
   | content\_index 表 | - 建表语句：     ```   CREATE TABLE "public"."content_index"   (    "id" bigint NOT NULL ,    "content" text DEFAULT ''::character varying ,    "content_text_search" tsvector ,    "dentry_id" bigint ,    "space_id" bigint ,    "chunk_id" integer ,    "extension" text ,    "eam_path" varchar(1024)[] ,    "eam_full_path" varchar(1024)[] ,    "biz_id" varchar(255) ,    "time_stamp" bigint ,    "tenant_id" varchar(255) ,    "biz_type" varchar(255) ,    "knowledge_base_dentry_id" varchar(255) ,    "is_public" integer ,    "is_eam" integer ,    "title" text ,    "embedding_vec1" real[] ,    "embedding_sparse_vec1" svector ,    "parent_ids" tsvector ,   CONSTRAINT "pk_public_content_index" PRIMARY KEY ("id")    )   WITH (       FILLFACTOR = 100,       OIDS = FALSE   )   ;    COMMENT ON COLUMN "public"."content_index"."id" IS '主键';   COMMENT ON COLUMN "public"."content_index"."content" IS '原文';   COMMENT ON COLUMN "public"."content_index"."content_text_search" IS '文本分词';   COMMENT ON COLUMN "public"."content_index"."dentry_id" IS '文档唯一id';   COMMENT ON COLUMN "public"."content_index"."space_id" IS '知识库id';   COMMENT ON COLUMN "public"."content_index"."chunk_id" IS '切片id';   COMMENT ON COLUMN "public"."content_index"."extension" IS '扩展字段';   COMMENT ON COLUMN "public"."content_index"."eam_path" IS '跟 eam 索引表 join 的资源路径';   COMMENT ON COLUMN "public"."content_index"."eam_full_path" IS '跟 eam 索引表 join 的资源全路径';   COMMENT ON COLUMN "public"."content_index"."biz_id" IS 'instanceId';   COMMENT ON COLUMN "public"."content_index"."time_stamp" IS '时间戳';   COMMENT ON COLUMN "public"."content_index"."tenant_id" IS 'org_id';   COMMENT ON COLUMN "public"."content_index"."biz_type" IS '文本类型，local|doc|qp';   COMMENT ON COLUMN "public"."content_index"."knowledge_base_dentry_id" IS '文件所属知识库dentry_id';   COMMENT ON COLUMN "public"."content_index"."is_public" IS '是否为公开知识库';   COMMENT ON COLUMN "public"."content_index"."is_eam" IS '权限是否走eam';   COMMENT ON COLUMN "public"."content_index"."title" IS '标题';   COMMENT ON COLUMN "public"."content_index"."embedding_vec1" IS '向量编码';   COMMENT ON COLUMN "public"."content_index"."parent_ids" IS '资源路径';   ``` - 建索引语句：     ```   "CREATE UNIQUE INDEX pk_public_content_index ON public.content_index USING btree (id)"   "CREATE INDEX content_index_dentry_id_idx ON public.content_index USING btree (dentry_id)"   "CREATE INDEX content_index_space_id_idx ON public.content_index USING btree (space_id)"   "CREATE INDEX content_index_title_idx ON public.content_index USING btree (title)"   "CREATE INDEX content_index_tenant_id_idx ON public.content_index USING btree (tenant_id)"   "CREATE INDEX content_index_timestamp_idx ON public.content_index USING btree (time_stamp)"   "CREATE INDEX content_index_is_eam_idx ON public.content_index USING btree (is_eam)"   "CREATE INDEX content_index_is_public_idx ON public.content_index USING btree (is_public)"   "CREATE INDEX content_index_biz_type_idx ON public.content_index USING btree (biz_type)"   "CREATE INDEX content_index_biz_id_idx ON public.content_index USING btree (biz_id)"   "CREATE INDEX idx_content_text_search ON public.content_index USING gin (content_text_search)"   "CREATE INDEX idx_embedding_sparse_vec1_ip ON public.content_index USING ann (embedding_sparse_vec1) WITH (distancemeasure=ip, hnsw_m='64')"   "CREATE INDEX idx_embedding_vec1 ON public.content_index USING ann (embedding_vec1) WITH (dim='1024', distancemeasure=cosine, hnsw_m='64', pq_enable='1')"   "CREATE INDEX content_index_content_idx ON public.content_index USING btree (content)"   "CREATE INDEX idx_eam_path ON public.content_index USING gin (eam_path)"   "CREATE INDEX idx_eam_full_path ON public.content_index USING gin (eam_full_path)"   "CREATE INDEX idx_parent_ids ON public.content_index USING gin (parent_ids)"   "CREATE INDEX idx_time_stmp ON public.content_index USING btree (time_stamp)"   ``` |
   | chunk\_detail 表 | - 建表语句：     ```   CREATE TABLE "public"."chunk_detail"   (    "instance_id" varchar(255) NOT NULL ,    "dentry_id" varchar(255) NOT NULL ,    "chunk_id" integer NOT NULL ,    "part_id" integer NOT NULL ,    "content" text ,    "org_id" varchar(255) ,    "extension" text ,   CONSTRAINT "pk_public_chunk_detail" PRIMARY KEY ("instance_id","dentry_id","chunk_id","part_id")    )   WITH (       FILLFACTOR = 100,       OIDS = FALSE   )   ;   ``` |

## **联系我们**

配置完成后，你需要提供给我们对应信息，请填写[表单](https://alidocs.dingtalk.com/notable/share/form/v01eYVOLXVZVxQLOpz2_2NPKTUr_K9ghbub?dontjump=true)。
