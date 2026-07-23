# -*- coding: utf-8 -*-
"""引文真实性验证：skill 的 R 段引文是否能在对应分集转录中找到"""
import os, re, sys, glob, difflib

sys.stdout.reconfigure(encoding="utf-8")
BASE = r"C:\Users\周春宇\Desktop\Psychohistory"
SKILLS = os.path.join(BASE, "skills")
SERIES = os.path.join(BASE, "series")

def norm(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def vtt_text(path):
    raw = open(path, encoding="utf-8", errors="ignore").read()
    raw = re.sub(r"WEBVTT.*?\n\n", "", raw, flags=re.S)
    raw = re.sub(r"\d{2}:\d{2}:\d{2}[\.,]\d+ --> .*?\n", " ", raw)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return norm(raw)

# ---------- 转录索引 ----------
def collect(pattern, series):
    out = {}
    for p in glob.glob(os.path.join(SERIES, series, "transcripts", "*")):
        if p.endswith((".vtt", ".md", ".txt")) and not p.endswith("_download_summary.json"):
            out[os.path.basename(p)] = p
    return out

transcripts = {
    "civ": collect("*", "civilization"),
    "gt": collect("*", "game-theory"),
    "gs": collect("*", "geo-strategy"),
    "gb": collect("*", "great-books"),
    "sh": collect("*", "secret-history"),
    "origin": collect("*", "psychohistory-origin"),
    "interview": {"transcript.txt": os.path.join(SERIES, "interview-jang-letstalk", "transcript.txt")},
}

_text_cache = {}
def get_text(path):
    if path not in _text_cache:
        _text_cache[path] = vtt_text(path)
    return _text_cache[path]

def map_episode(ep):
    """返回候选转录路径列表"""
    ep = ep.strip().strip('"')
    if "Let's Talk" in ep:
        return list(transcripts["interview"].values())
    if "WW3 Analysis" in ep:
        # WW3 分析视频，在 geo-strategy 中按标题关键词找
        kws = {"Catalyst": "catalyst", "Grand Strategy": "grand", "Shadow Fleet": "shadow"}
        hits = []
        for name, p in {**transcripts["gs"], **transcripts["gt"]}.items():
            nl = name.lower()
            for k, kw in kws.items():
                if k in ep and kw in nl:
                    hits.append(p)
        return hits
    m = re.match(r"(C|GB|GT|GS|GU|SH)#?(\d+|END)", ep, re.I)
    if not m:
        return []
    prefix = m.group(1).upper()
    # 支持 "C#14/17" 这类多分集写法
    nums = [m.group(2)] + re.findall(r"/(\d+|END)", ep)
    hits = []
    for num in nums:
        if prefix == "C":
            pats = [os.path.join(SERIES, "civilization", "transcripts", f"Civilization #{num}：*")]
        elif prefix == "GB":
            pats = [os.path.join(SERIES, "great-books", "transcripts", f"Great Books #{num}：*")]
        elif prefix == "GT":
            pats = [os.path.join(SERIES, "game-theory", "transcripts", f"GT{num}-*")]
        elif prefix == "GU":
            pats = [os.path.join(SERIES, "geo-strategy", "transcripts", f"GU{num}-*")]
        elif prefix == "GS":
            if num == "END":
                pats = [os.path.join(SERIES, "geo-strategy", "transcripts", "GSEND*"),
                        os.path.join(SERIES, "psychohistory-origin", "transcripts", "GSEND*")]
            else:
                pats = [os.path.join(SERIES, "geo-strategy", "transcripts", f"GS{num}-*")]
        elif prefix == "SH":
            # skill 里的 SH## 是"Secret History #N"的集号，文件名是 SH## 顺序号，需按标题内 #N 匹配
            pats = [os.path.join(SERIES, "secret-history", "transcripts", f"SH*-Secret History #{num} *"),
                    os.path.join(SERIES, "secret-history", "transcripts", f"SH{num}-*")]
        for pat in pats:
            hits.extend(g for g in glob.glob(pat) if not g.endswith("_download_summary.json"))
    return hits

def ngrams(words, n=4):
    return set(tuple(words[i:i + n]) for i in range(len(words) - n + 1))

_gram_cache = {}
def get_grams(path):
    if path not in _gram_cache:
        _gram_cache[path] = ngrams(get_text(path).split())
    return _gram_cache[path]

def best_ratio(frag, grams_list):
    """引文片段的 4-gram 在转录中出现的比例"""
    words = norm(frag).split()
    if len(words) < 4:
        return 1.0
    fg = ngrams(words)
    hits = 0
    for g in fg:
        if any(g in gs for gs in grams_list):
            hits += 1
    return hits / len(fg)

# ---------- 主循环 ----------
files = sorted(f for f in os.listdir(SKILLS) if f.endswith(".md"))
results = []
for fn in files:
    text = open(os.path.join(SKILLS, fn), encoding="utf-8").read()
    # episodes
    eps = re.findall(r'source_episodes:\s*\n((?:\s*-\s*"[^"]*"\s*\n)+)', text)
    ep_list = re.findall(r'-\s*"([^"]*)"', eps[0]) if eps else []
    # R 段引文
    rsec = re.search(r"## R —(.*?)(?=\n## )", text, re.S)
    quotes = re.findall(r'^>\s*"(.*?)"\s*$', rsec.group(1), re.M) if rsec else []
    tpaths = []
    for ep in ep_list:
        tpaths.extend(map_episode(ep))
    tpaths = list(dict.fromkeys(tpaths))

    if not quotes:
        results.append((fn, "无引文", []))
        continue
    if not tpaths:
        results.append((fn, f"找不到转录(ep={ep_list})", [("ALL", 0.0, "no-transcript")] * len(quotes)))
        continue

    combined = " ".join(get_text(p) for p in tpaths)
    grams_list = [get_grams(p) for p in tpaths]
    # 全库兜底：区分"标错集"与"编造"
    all_paths = []
    for group in transcripts.values():
        all_paths.extend(group.values())
    all_paths = list(dict.fromkeys(all_paths))
    all_grams = [(p, get_grams(p)) for p in all_paths]
    qres = []
    for q in quotes:
        frags = [f for f in re.split(r"\.\.\.|…", q) if len(norm(f).split()) >= 4]
        if not frags:
            continue
        scores = [best_ratio(f, grams_list) for f in frags]
        worst = min(scores)
        status = "ok" if worst >= 0.7 else ("partial" if worst >= 0.4 else "MISS")
        found_elsewhere = ""
        if worst < 0.4:
            # 在全库中找最好的匹配
            best_g, best_p = 0.0, ""
            for f in frags:
                words = norm(f).split()
                if len(words) < 4:
                    continue
                fg = ngrams(words)
                for pth, gs in all_grams:
                    hits = sum(1 for g in fg if g in gs)
                    r = hits / len(fg)
                    if r > best_g:
                        best_g, best_p = r, os.path.basename(pth)
            found_elsewhere = f"全库最佳[{best_g:.2f}] {best_p[:60]}"
        qres.append((q[:50], worst, status, found_elsewhere))
    results.append((fn, f"eps={ep_list}", qres))

# ---------- 汇总 ----------
bad, partial, ok, notr = [], [], 0, []
for fn, info, qres in results:
    if "找不到转录" in info:
        notr.append((fn, info))
        continue
    if not qres:
        continue
    worst = min(r for _, r, _, _ in qres)
    if worst < 0.4:
        bad.append((fn, info, qres))
    elif worst < 0.7:
        partial.append((fn, info, qres))
    else:
        ok += 1

print(f"总文件: {len(files)}")
print(f"全部引文验证通过(>=0.7): {ok}")
print(f"部分引文弱匹配(0.4-0.7, 可能改写/拼接): {len(partial)}")
print(f"存在引文无法匹配(<0.4, 疑似编造或错集): {len(bad)}")
print(f"找不到对应转录: {len(notr)}")

print("\n===== 疑似问题文件（引文匹配 <0.4）=====")
for fn, info, qres in bad:
    print(f"\n--- {fn}  {info}")
    for q, r, st, fe in qres:
        mark = "✗" if st == "MISS" else ("~" if st == "partial" else "✓")
        print(f"  {mark} [{r:.2f}] \"{q}...\" {fe}")

print("\n===== 弱匹配文件（0.4-0.7）=====")
for fn, info, qres in partial:
    print(f"\n--- {fn}  {info}")
    for q, r, st, fe in qres:
        if r < 0.7:
            print(f"  ~ [{r:.2f}] \"{q}...\"")

print("\n===== 找不到转录的文件 =====")
for fn, info in notr:
    print(f"  - {fn}  {info}")
