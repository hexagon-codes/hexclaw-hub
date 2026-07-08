#!/usr/bin/env python3
"""
从 skills/*.md 的 YAML frontmatter 生成 index.json —— 单一真相源（堵住 frontmatter 与 index 双维护漂移）。

改进点（对应架构评审 P1-5）：
- index 由 frontmatter 生成，不手维护；
- 每条带 sha256 + size + min_engine_version + trust（完整性 + 兼容 + 信任分层）；
- downloads/rating 不再凭空编造：从旧 index 按 name 携带（保留市场既有展示），新条目默认 0；
- 兼容后端手写解析器：frontmatter 用 `key: value` / `key: [a, b]` 内联列表 / `- item` 多行列表。

用法：python3 scripts/generate-index.py   （在 hexclaw-hub 根目录）
"""
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")
INDEX_PATH = os.path.join(ROOT, "index.json")

# 进入 index 的 frontmatter 字段（正文不进 index，激活时才加载——渐进披露）
SCALAR_FIELDS = [
    "name", "display_name", "description", "version", "author",
    "category", "icon", "trust", "min_engine_version", "license",
    "schema_version", "eval", "acceptance",  # 契约字段（供后端 eval 卡门 P0-2 + 客户端展示）
]
LIST_FIELDS = ["tags", "requires", "outputs"]  # 依赖 + 输出契约（installer 解析 / 闭环打通）


def parse_frontmatter(text):
    """解析 --- ... --- 之间的 frontmatter。返回 dict（scalar=str, list=list[str]）。"""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return None
    body = m.group(1)
    meta = {}
    cur_list_key = None
    for raw in body.split("\n"):
        line = raw.rstrip()
        if not line.strip():
            continue
        # 多行列表项： "  - item"
        m_item = re.match(r"^\s*-\s+(.*)$", line)
        if m_item and cur_list_key:
            meta.setdefault(cur_list_key, []).append(m_item.group(1).strip().strip("\"'"))
            continue
        # key: value
        m_kv = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if not m_kv:
            continue
        key, val = m_kv.group(1), m_kv.group(2).strip()
        cur_list_key = None
        if val == "":
            # 后续可能是多行列表
            cur_list_key = key
            meta[key] = []
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            meta[key] = [x.strip().strip("\"'") for x in inner.split(",") if x.strip()] if inner else []
        else:
            meta[key] = val.strip("\"'")
    return meta


def main():
    # 非破坏性：以旧 index 条目为基底（保留 display_name/category/downloads/rating 等历史手维护字段），
    # 再用 frontmatter 覆盖它声明的字段，最后加完整性字段。避免"整表重生成降级现有条目"。
    prev_entry = {}
    if os.path.exists(INDEX_PATH):
        try:
            old = json.load(open(INDEX_PATH, encoding="utf-8"))
            for s in old.get("skills", []):
                prev_entry[s.get("name")] = s
        except Exception:
            pass

    entries = []
    errors = []
    for fn in sorted(os.listdir(SKILLS_DIR)):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(SKILLS_DIR, fn)
        content = open(path, "rb").read()
        meta = parse_frontmatter(content.decode("utf-8"))
        if not meta or not meta.get("name"):
            errors.append(f"{fn}: 缺 frontmatter/name")
            continue
        base = dict(prev_entry.get(meta["name"], {}))  # 历史字段基底
        for f in SCALAR_FIELDS:
            if meta.get(f):
                base[f] = meta[f]  # frontmatter 覆盖（新字段的真相源）
        for f in LIST_FIELDS:
            if meta.get(f):
                base[f] = meta[f]
        base["file"] = f"skills/{fn}"
        base["sha256"] = hashlib.sha256(content).hexdigest()
        base["size"] = len(content)
        base.setdefault("downloads", 0)  # 新条目诚实为 0，不编造
        base.setdefault("rating", 0)
        entries.append(base)

    if errors:
        print("⚠️  跳过（frontmatter 有问题）:", *errors, sep="\n  ", file=sys.stderr)

    entries.sort(key=lambda e: e["name"])
    # updated_at 必须是 RFC3339（后端 Catalog.UpdatedAt 是 time.Time，纯日期会 unmarshal 崩）
    now_rfc3339 = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    index = {
        "version": "2.0.0",
        "updated_at": now_rfc3339,
        "generated_by": "scripts/generate-index.py",
        "count": len(entries),
        "skills": entries,
    }
    with open(INDEX_PATH, "w", encoding="utf-8") as fp:
        json.dump(index, fp, ensure_ascii=False, indent=2)
        fp.write("\n")
    print(f"✅ index.json 已生成：{len(entries)} skills（含 sha256/size）")


if __name__ == "__main__":
    main()
