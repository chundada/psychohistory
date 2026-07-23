# -*- coding: utf-8 -*-
"""对30个错集文件做逐片段精确诊断"""
import os, re, sys, glob

sys.stdout.reconfigure(encoding="utf-8")
BASE = r"C:\Users\周春宇\Desktop\Psychohistory"
SKILLS = os.path.join(BASE, "skills")
SERIES = os.path.join(BASE, "series")

FILES = """civ-civ-003 civ-civ-005 civ-civ-011 civ-pred-004 civ-rel-002 civ-rel-007 civ-rel-008 civ-rel-009 civ-rel-010 civ-rel-013 civ-rel-015 gt-civilization-military-industrial-complex gt-predictive-005 gt-predictive-008 gt-predictive-009 gt-predictive-011 gt-predictive-013 gt-religion-kabbalistic-redemption ph-origin-elite-overproduction ph-origin-psychohistory-definition sh-fail-001 sh-fail-002 sh-game-007 sh-geo-001 sh-pre-002 sh-pre-003 sh-rel-005 sh-rel-014 sh-rel-017 sh-rel-022""".split()

def norm(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def vtt_text(path):
    raw = open(path, encoding="utf-8", errors="ignore").read()
    raw = re.sub(r"<[^>]+>", " ", raw)
    return norm(raw)

def ngrams(words, n=4):
    return set(tuple(words[i:i + n]) for i in range(len(words) - n + 1))

# 全库
all_paths = []
for series in ["civilization", "game-theory", "geo-strategy", "great-books", "secret-history", "psychohistory-origin"]:
    for p in glob.glob(os.path.join(SERIES, series, "transcripts", "*")):
        if p.endswith((".vtt", ".md")) and not p.endswith("_download_summary.json"):
            all_paths.append(p)
all_paths.append(os.path.join(SERIES, "interview-jang-letstalk", "transcript.txt"))
all_paths = list(dict.fromkeys(all_paths))

grams = {}
for p in all_paths:
    grams[p] = ngrams(vtt_text(p).split())

def frag_locate(frag):
    words = norm(frag).split()
    if len(words) < 4:
        return None
    fg = ngrams(words)
    best_r, best_p = 0.0, None
    for p, gs in grams.items():
        hits = sum(1 for g in fg if g in gs)
        r = hits / len(fg)
        if r > best_r:
            best_r, best_p = r, p
    return best_r, os.path.basename(best_p) if best_p else ""

for fn in FILES:
    text = open(os.path.join(SKILLS, fn + ".md"), encoding="utf-8").read()
    eps_m = re.findall(r'source_episodes:\s*\n((?:\s*-\s*"[^"]*"\s*\n)+)', text)
    eps = re.findall(r'-\s*"([^"]*)"', eps_m[0]) if eps_m else []
    rsec = re.search(r"## R —(.*?)(?=\n## )", text, re.S)
    quotes = re.findall(r'^>\s*"(.*?)"\s*$', rsec.group(1), re.M) if rsec else []
    print(f"\n=== {fn}  标注: {eps}")
    for i, q in enumerate(quotes, 1):
        frags = [f for f in re.split(r"\.\.\.|…", q) if len(norm(f).split()) >= 4]
        for j, f in enumerate(frags):
            r, loc = frag_locate(f)
            tag = "✓" if r >= 0.7 else ("~" if r >= 0.4 else "✗")
            print(f"  Q{i}.{j+1} {tag}[{r:.2f}] \"{f[:55].strip()}...\" -> {loc[:70]}")
