#!/usr/bin/env python3
"""把抓取快照编译成「钉钉开放平台知识答疑」可用的分层语料。

用法:
    python3 tools/compile_qa_kb.py                 # 只产出 manifest + 报告（不动原文件）
    python3 tools/compile_qa_kb.py --materialize    # 额外把 T0/T1/T2 正文拷到 compiled/
    python3 tools/compile_qa_kb.py --tiers T0 T1    # 只物化指定层

分层:
    T0 core       答疑主力：开发指南 / 现行服务端API / 现行JSAPI / 现行事件订阅
    T1 adjacent   周边产品线：互动卡片、连接平台、AI PaaS、工作台组件、CLI/工具
    T2 archived   历史文档（不推荐）——仍可调用，保留但降权，仅命中「旧接口」类问题
    DROP          答疑用不到：商务协议/入驻规范、端侧插件、硬件、数据资产大屏、空壳、重复
"""
import argparse
import collections
import hashlib
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
JSONL = os.path.join(ROOT, "meta", "documents.jsonl")
OUT = os.path.join(ROOT, "meta")

HIST = "历史文档（不推荐）"

# (group, tab) -> tier。未列出的 tab 默认进 T1。
TIER_BY_TAB = {
    ("应用开发", "开发指南"): "T0",
    ("应用开发", "服务端API"): "T0",
    ("应用开发", "客户端JSAPI"): "T0",
    ("应用开发", "事件订阅"): "T0",
    ("应用开发", "开发工具"): "T1",
    ("应用开发", "钉钉CLI"): "T1",
    ("互动卡片", "开发指南"): "T1",
    ("互动卡片", "卡片模板搭建器"): "T1",
    ("互动卡片", "互动卡片搭建平台"): "T1",
    ("互动卡片", "卡片规范设计"): "T1",
    ("连接平台", "开发指南"): "T1",
    ("连接平台", "连接器中心"): "T1",
    ("连接平台", "连接平台自动化"): "T1",
    ("连接平台", "平台介绍"): "T1",
    ("AI PaaS", "AI 助理创建平台"): "T1",
    ("AI PaaS", "平台介绍"): "T1",
    ("AI PaaS", "炼丹炉大模型平台"): "T1",
    ("AI PaaS", "AI 客服助理"): "T1",
    ("工作台", "使用教程"): "T1",
}

# 整个 tab 剔除：与「开放平台开发答疑」无关的商务/端侧/垂直产品线。
DROP_TABS = {
    ("应用开发", "平台服务"): "商务规则：服务商入驻/协议/收费/合作流程，非开发问题",
    ("专属版客户端插件", "插件开发"): "专属版客户端原生插件（Android/iOS/Win），独立技术栈",
    ("专属版客户端插件", "功能介绍"): "专属版客户端原生插件，独立技术栈",
    ("硬件开发", "智能硬件"): "硬件固件/协议对接，与开放平台 API 答疑无交集",
    ("数据资产", "平台介绍"): "宜数大屏搭建，图多字少的后台操作教程",
    ("数据资产", "宜数（智能问数）"): "宜数大屏搭建，图多字少的后台操作教程",
    ("工作台", "平台介绍"): "开通方式/服务商渠道，商务类",
}

# 标题级剔除：协议、计费、入驻、考试等纯运营内容（在保留的 tab 内）
DROP_TITLE_RE = re.compile(
    r"(服务协议|隐私权政策|入驻服务协议|合作协议|入驻规范|保证金规范|运营规范|"
    r"准入要求|合作指南|合作流程|收费规则|收款帐号|保证金|营销活动|流量管理|"
    r"数字化管理师|钉钉碳中和|365会员|学习平台|大赛|榜单|招募)"
)

# breadcrumb 级剔除
DROP_CRUMB_RE = re.compile(r"(平台协议|平台基础规则|服务商准入规则|第三方个人应用发布规范)")


def strip_header(text: str) -> str:
    t = re.sub(r"^---.*?^---", "", text, count=1, flags=re.S | re.M)
    t = re.sub(r"^> (Source|Path|Updated):.*$", "", t, flags=re.M)
    return t


def body_len(text: str) -> int:
    t = strip_header(text)
    t = re.sub(r"^#\s+.*$", "", t, count=1, flags=re.M)
    return len(re.sub(r"\s", "", t))


def norm_body(text: str) -> str:
    t = strip_header(text)
    t = re.sub(r"https?://\S+", "", t)
    return re.sub(r"\s+", " ", t).strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--materialize", action="store_true", help="把正文拷贝到 compiled/")
    ap.add_argument("--tiers", nargs="*", default=["T0", "T1", "T2"], help="要物化的层")
    ap.add_argument("--check", action="store_true", help="只比对 kb_manifest 不落盘，漂移退出码 1")
    args = ap.parse_args()

    if not os.path.exists(JSONL):
        print(f"找不到 {JSONL}", file=sys.stderr)
        return 1

    docs = [json.loads(line) for line in open(JSONL, encoding="utf-8")]

    # ---- 先算重复：同正文取 local_path 排序最小的那篇为 canonical ----
    by_hash = collections.defaultdict(list)
    cache = {}
    for d in docs:
        p = os.path.join(ROOT, d["local_path"])
        if not os.path.exists(p):
            continue
        text = open(p, encoding="utf-8", errors="ignore").read()
        cache[d["local_path"]] = text
        nb = norm_body(text)
        if len(nb) >= 200:
            by_hash[hashlib.md5(nb.encode()).hexdigest()].append(d["local_path"])
    dup_of = {}
    for paths in by_hash.values():
        if len(paths) > 1:
            keep, *rest = sorted(paths)
            for r in rest:
                dup_of[r] = keep

    records = []
    for d in docs:
        lp = d["local_path"]
        crumb = d.get("breadcrumb") or []
        crumb_s = " > ".join(crumb)
        group, tab, title = d["group"], d["tab"], d["title"]
        text = cache.get(lp)

        tier, reason = None, ""
        if text is None:
            tier, reason = "DROP", "正文文件缺失"
        elif lp in dup_of:
            tier, reason = "DROP", f"正文与 {dup_of[lp]} 完全重复"
        elif body_len(text) < 120:
            tier, reason = "DROP", "空壳文档：只有标题，无正文"
        elif (group, tab) in DROP_TABS:
            tier, reason = "DROP", DROP_TABS[(group, tab)]
        elif DROP_CRUMB_RE.search(crumb_s):
            tier, reason = "DROP", "商务/运营规则类目录"
        elif DROP_TITLE_RE.search(title):
            tier, reason = "DROP", "协议/计费/入驻/运营类标题"
        elif crumb and crumb[0] == HIST:
            tier, reason = "T2", "历史文档（不推荐）：接口仍可用，降权召回"
        else:
            tier = TIER_BY_TAB.get((group, tab), "T1")

        rec = {
            "tier": tier,
            "drop_reason": reason if tier == "DROP" else "",
            "deprecated": tier == "T2",
            "title": title,
            "group": group,
            "tab": tab,
            "breadcrumb": crumb,
            "source_url": d["source_url"],
            "namespace": d["namespace"],
            "slug": d["slug"],
            "updated_at": d["updated_at"],
            "local_path": lp,
            "bytes": os.path.getsize(os.path.join(ROOT, lp)) if text is not None else 0,
            "body_chars": body_len(text) if text is not None else 0,
            "headings": d.get("headings", []),
        }
        records.append(rec)

    if args.check:
        want = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records)
        p = os.path.join(OUT, "kb_manifest.jsonl")
        have = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
        if want != have:
            print("[compile_qa_kb --check] kb_manifest.jsonl 与 docs/meta 漂移，需重跑 compile_qa_kb.py")
            return 1
        print(f"[compile_qa_kb --check] OK：kb_manifest {len(records)} 条与 docs/meta 一致")
        return 0

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "kb_manifest.jsonl"), "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # ---- 统计 ----
    agg = collections.defaultdict(lambda: [0, 0])
    for r in records:
        a = agg[r["tier"]]
        a[0] += 1
        a[1] += r["bytes"]
    total_b = sum(a[1] for a in agg.values())

    lines = ["# 编译结果\n", f"源快照 {len(records)} 篇 / {total_b/1048576:.1f} MB\n", "| 层 | 篇数 | MB | ≈k tokens | 占比 |", "| --- | --- | --- | --- | --- |"]
    for t in ["T0", "T1", "T2", "DROP"]:
        n, b = agg[t]
        lines.append(f"| {t} | {n} | {b/1048576:.1f} | {b/1600:.0f} | {b/total_b*100:.1f}% |")

    drops = collections.defaultdict(lambda: [0, 0])
    for r in records:
        if r["tier"] == "DROP":
            a = drops[r["drop_reason"]]
            a[0] += 1
            a[1] += r["bytes"]
    lines += ["\n## DROP 明细\n", "| 原因 | 篇数 | MB |", "| --- | --- | --- |"]
    for k, (n, b) in sorted(drops.items(), key=lambda x: -x[1][1]):
        lines.append(f"| {k} | {n} | {b/1048576:.2f} |")

    report = "\n".join(lines) + "\n"
    open(os.path.join(OUT, "COMPILE_REPORT.md"), "w", encoding="utf-8").write(report)
    print(report)

    # ---- 物化 ----
    if args.materialize:
        for t in args.tiers:
            tdir = os.path.join(OUT, t)
            if os.path.isdir(tdir):
                shutil.rmtree(tdir)
        copied = 0
        for r in records:
            if r["tier"] not in args.tiers:
                continue
            src = os.path.join(ROOT, r["local_path"])
            dst = os.path.join(OUT, r["tier"], os.path.relpath(r["local_path"], "docs"))
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            text = open(src, encoding="utf-8", errors="ignore").read()
            if r["deprecated"]:
                # 在正文最前面插入显式废弃标记，保证切片后每个 chunk 的上游都带上下文
                text = text.replace(
                    "\n---\n",
                    '\nstatus: "archived"\ndeprecated: true\n---\n',
                    1,
                )
                text = re.sub(
                    r"^(# .*)$",
                    r"\1\n\n> **[归档接口]** 本文属钉钉「历史文档（不推荐）」目录，接口仍可调用，"
                    r"但新接入请使用对应新版接口。",
                    text,
                    count=1,
                    flags=re.M,
                )
            open(dst, "w", encoding="utf-8").write(text)
            copied += 1
        print(f"已物化 {copied} 篇到 {OUT}/{{{','.join(args.tiers)}}}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
