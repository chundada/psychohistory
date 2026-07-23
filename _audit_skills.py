# -*- coding: utf-8 -*-
"""机械审计 skills/ 目录下全部蒸馏技能文件"""
import os, re, sys, json, hashlib
from collections import Counter, defaultdict

io = sys.stdout
io.reconfigure(encoding="utf-8")

ROOT = r"C:\Users\周春宇\Desktop\Psychohistory\skills"
files = sorted(f for f in os.listdir(ROOT) if f.endswith(".md"))

PLACEHOLDER_PAT = re.compile(r"<技能名称>|<一句话>|<系列>|___|TODO|TBD|待补|占位|placeholder", re.I)
TS_PAT = re.compile(r"\[\d{1,2}:\d{2}(:\d{2})?\s*-\s*\d{1,2}:\d{2}(:\d{2})?\]")
QUOTE_PAT = re.compile(r'^>\s*"', re.M)

stats = []
hash_map = defaultdict(list)
quote_map = defaultdict(list)   # 完全相同的引文块 -> 文件
name_map = defaultdict(list)    # frontmatter name 重复

for fn in files:
    p = os.path.join(ROOT, fn)
    text = open(p, encoding="utf-8").read()
    lines = text.splitlines()
    size = len(text.encode("utf-8"))

    # frontmatter
    fm = {}
    if text.startswith("---"):
        end = text.find("---", 3)
        fm_raw = text[3:end]
        for line in fm_raw.splitlines():
            m = re.match(r"^(\w[\w_]*):\s*(.*)$", line)
            if m:
                fm[m.group(1)] = m.group(2).strip().strip('"')

    sec_r = bool(re.search(r"## R —", text))
    sec_i = bool(re.search(r"## I —", text))
    sec_a = bool(re.search(r"## A —", text) or re.search(r"### A1", text))
    sec_b = bool(re.search(r"## B —", text))
    has_ts = bool(TS_PAT.search(text))
    has_quote = bool(QUOTE_PAT.search(text))
    placeholders = PLACEHOLDER_PAT.findall(text)
    body = re.sub(r"\s+", " ", text)
    h = hashlib.md5(body.encode()).hexdigest()
    hash_map[h].append(fn)
    name_map[fm.get("name", "")].append(fn)

    # 引文块内容（R 段引号文本）
    quotes = QUOTE_PAT.findall(text)
    qtexts = re.findall(r'^>\s*"(.*?)"\s*$', text, re.M)
    for q in qtexts:
        key = re.sub(r"\s+", " ", q.strip())[:120]
        quote_map[key].append(fn)

    stats.append(dict(
        fn=fn, size=size, lines=len(lines),
        name=fm.get("name", ""), desc_len=len(fm.get("description", "")),
        episodes=fm.get("source_episodes", ""),
        created=fm.get("created", ""), verified=fm.get("verified", ""),
        fm_fields=sorted(fm.keys()),
        sec_r=sec_r, sec_i=sec_i, sec_a=sec_a, sec_b=sec_b,
        has_ts=has_ts, has_quote=has_quote, placeholders=placeholders,
    ))

# ---------- 汇总 ----------
print(f"== 总文件数: {len(stats)}")
sizes = sorted(s["size"] for s in stats)
print(f"== 大小(bytes): min={sizes[0]} p25={sizes[len(sizes)//4]} median={sizes[len(sizes)//2]} p75={sizes[3*len(sizes)//4]} max={sizes[-1]}")

missing_fm = [s["fn"] for s in stats if not s["name"] or not s["created"]]
print(f"\n== 缺 frontmatter 关键字段(name/created)的文件数: {len(missing_fm)}")
for f in missing_fm[:20]: print("   -", f)

no_ts = [s["fn"] for s in stats if not s["has_ts"]]
print(f"\n== 无时间戳 [HH:MM-HH:MM] 的文件: {len(no_ts)} / {len(stats)}")
for f in no_ts[:30]: print("   -", f)

no_quote = [s["fn"] for s in stats if not s["has_quote"]]
print(f"\n== 无原文引用的文件: {len(no_quote)} / {len(stats)}")
for f in no_quote[:30]: print("   -", f)

sec_missing = [s["fn"] for s in stats if not (s["sec_r"] and s["sec_i"] and s["sec_a"] and s["sec_b"])]
print(f"\n== R/I/A/B 结构不完整的文件: {len(sec_missing)} / {len(stats)}")
for f in sec_missing[:30]:
    s = next(x for x in stats if x["fn"] == f)
    print(f"   - {f}  R={s['sec_r']} I={s['sec_i']} A={s['sec_a']} B={s['sec_b']}")

ph = [s["fn"] for s in stats if s["placeholders"]]
print(f"\n== 含模板占位符/未填内容的文件: {len(ph)}")
for f in ph: 
    s = next(x for x in stats if x["fn"] == f)
    print(f"   - {f}: {set(s['placeholders'])}")

tiny = [s for s in stats if s["size"] < 1500]
print(f"\n== 体量过小(<1500 bytes)的文件: {len(tiny)}")
for s in tiny: print(f"   - {s['fn']}  {s['size']}B {s['lines']}行")

dup_bodies = {h: fs for h, fs in hash_map.items() if len(fs) > 1}
print(f"\n== 正文完全重复的文件组: {len(dup_bodies)}")
for h, fs in dup_bodies.items(): print("   -", fs)

dup_names = {n: fs for n, fs in name_map.items() if n and len(fs) > 1}
print(f"\n== frontmatter name 重复: {len(dup_names)}")
for n, fs in dup_names.items(): print(f"   - {n}: {fs}")

dup_quotes = {q: fs for q, fs in quote_map.items() if len(set(fs)) > 1}
print(f"\n== 相同引文出现在多个文件的组数: {len(dup_quotes)}")
for q, fs in list(dup_quotes.items())[:25]:
    print(f"   - \"{q[:60]}...\" -> {sorted(set(fs))}")

# frontmatter 字段分布
field_count = Counter()
for s in stats: field_count.update(s["fm_fields"])
print("\n== frontmatter 字段出现次数:")
for k, v in field_count.most_common(): print(f"   {k}: {v}")

verified = Counter(s["verified"] or "(无)" for s in stats)
print("\n== verified 字段分布:", dict(verified))

desc_short = [s["fn"] for s in stats if s["desc_len"] < 20]
print(f"\n== description 过短(<20字符): {len(desc_short)}")
for f in desc_short[:20]: print("   -", f)

no_ep = [s["fn"] for s in stats if not s["episodes"]]
print(f"\n== 无 source_episodes: {len(no_ep)}")
for f in no_ep[:20]: print("   -", f)
