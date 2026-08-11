#!/usr/bin/env python3
"""扫描 docs/ 全部 Markdown 的站内相对链接，重建文档间关系边。

产出（生成物，勿手改）：
  graph/links.jsonl   有向边一行一条：{"from": docs/..., "to": docs/..., "text": 锚文本, "n": 次数}
  graph/hubs.md       被引用最多的文档 Top 100（事实上的核心页/枢纽页）

用途：
  - 答疑时从一篇文档扩展到关联文档（正向查 from，反向查 to）
  - 变更处理时做「关系级重编译」：某文档更新/下线后，反查谁引用它（见 ops/INGEST.md）

用法:
  python3 ops/scripts/build_links.py           # 重建
  python3 ops/scripts/build_links.py --check   # 只比对不落盘，漂移则退出码 1
"""
import argparse
import collections
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOCS = os.path.join(ROOT, "docs")
GRAPH = os.path.join(ROOT, "graph")
RE_LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")


def collect():
    edges = collections.Counter()
    texts = {}
    broken = []
    for dirpath, _, files in os.walk(DOCS):
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            fp = os.path.join(dirpath, fn)
            src = os.path.relpath(fp, ROOT)
            body = open(fp, encoding="utf-8", errors="ignore").read()
            for text, target in RE_LINK.findall(body):
                if target.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                target = target.split("#")[0]
                if not target.endswith(".md"):
                    continue
                dst_abs = os.path.normpath(os.path.join(dirpath, target))
                dst = os.path.relpath(dst_abs, ROOT)
                if not dst.startswith("docs/"):
                    continue
                if not os.path.exists(dst_abs):
                    broken.append((src, dst))
                    continue
                key = (src, dst)
                edges[key] += 1
                texts.setdefault(key, text.strip())
    return edges, texts, broken


def render(edges, texts, titles):
    lines = []
    for (src, dst), n in sorted(edges.items()):
        lines.append(json.dumps({"from": src, "to": dst, "text": texts[(src, dst)], "n": n}, ensure_ascii=False))
    links_jsonl = "\n".join(lines) + "\n" if lines else ""

    indeg = collections.Counter()
    for (src, dst), n in edges.items():
        indeg[dst] += 1  # 按引用方数量计，不按重复次数
    hub = ["# 枢纽文档：被引用最多的 Top 100", ""]
    hub.append("> 站内被其他文档引用最多的页面，即事实上的核心概念/核心流程页。答疑吃不准从哪读起时，从这里进。")
    hub.append("> 生成物（ops/scripts/build_links.py），勿手改。")
    hub.append("")
    for dst, n in sorted(indeg.items(), key=lambda kv: (-kv[1], kv[0]))[:100]:
        t = titles.get(dst, {})
        title = t.get("title", os.path.basename(dst))
        tab = t.get("tab", "")
        rel = os.path.relpath(dst, "graph")
        hub.append(f"- {n} ← [{title}]({rel})（{tab}）")
    hubs_md = "\n".join(hub) + "\n"
    return {"links.jsonl": links_jsonl, "hubs.md": hubs_md}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    titles = {}
    with open(os.path.join(ROOT, "meta", "documents.jsonl"), encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            titles[d["local_path"]] = d

    edges, texts, broken = collect()
    out = render(edges, texts, titles)

    if args.check:
        drift = []
        for name, content in out.items():
            fp = os.path.join(GRAPH, name)
            if not os.path.exists(fp) or open(fp, encoding="utf-8").read() != content:
                drift.append(name)
        if drift:
            print(f"[build_links --check] 漂移，需重跑 build_links.py: {drift}")
            return 1
        print(f"[build_links --check] OK：{len(edges)} 条边与 docs/ 一致（站内断链 {len(broken)} 条为源快照固有）")
        return 0

    os.makedirs(GRAPH, exist_ok=True)
    for name, content in out.items():
        with open(os.path.join(GRAPH, name), "w", encoding="utf-8") as f:
            f.write(content)
    print(f"[build_links] {len(edges)} 条 doc→doc 边；断链 {len(broken)} 条（快照转换时未纳入目录树的链接）")
    if broken:
        for s, d in broken[:10]:
            print(f"  断链示例: {s} -> {d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
