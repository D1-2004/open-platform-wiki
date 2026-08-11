---
title: "运维工具dmaasctl使用步骤"
source_url: "https://open.dingtalk.com/document/aipass/operation-and-maintenance-tool-dmaasctl-use-steps-1"
namespace: "aipass"
slug: "operation-and-maintenance-tool-dmaasctl-use-steps-1"
group: "AI PaaS"
tab: "平台介绍"
breadcrumb: "运维工具dmaasctl使用步骤"
doc_id: "Kr5cZX28ch"
updated_at: "2025-09-23 19:18:54"
---

> Source: https://open.dingtalk.com/document/aipass/operation-and-maintenance-tool-dmaasctl-use-steps-1
> Path: AI PaaS / 平台介绍 / 运维工具dmaasctl使用步骤
> Updated: 2025-09-23 19:18:54

# 运维工具dmaasctl使用步骤

本文档介绍模型调优的运维工具dmaasctl使用步骤。

## 安装**工具**

```
pip install https://dingding-archive.oss-cn-shanghai.aliyuncs.com/maas/release/dingtalk-maas-pysdk/dingtalk_maas_pysdk-0.1.4-py3-none-any.whl
```

## **查看模型调优日志**

```
export DINGTALK_MAAS_GATEWAY=https://maas.dingtalk.com;
export DINGTALK_API_KEY=xxxxxxxxxxxxx;
dmaasctl logs adapter new_grpo_repo/34
```

支持参数`-o output 可选` 输出到文件

## **停止一个模型调优任务**

```
export DINGTALK_MAAS_GATEWAY=https://maas.dingtalk.com;
export DINGTALK_API_KEY=xxxxxxxxxxxxx;
dmaasctl delete adapter new_grpo_repo/34
```

## **获取一个 adapter 详情**

```
export DINGTALK_MAAS_GATEWAY=https://maas.dingtalk.com;
export DINGTALK_API_KEY=xxxxxxxxxxxxx;
dmaasctl get adapter new_grpo_repo/34
```

## **获取一个 adapter 详情并监控调优进度，添加 -w 或 --watch 参数**

```
export DINGTALK_MAAS_GATEWAY=https://maas.dingtalk.com;
export DINGTALK_API_KEY=xxxxxxxxxxxxx;
dmaasctl get adapter new_grpo_repo/34 -w
```

支持参数 `-w/--watch 可选`
