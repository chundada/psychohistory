# 🔄 给 AI 代理的接手指南 (Continue for AI Agents)

> 此文件专门为后续 AI 代理（Claude Code、Cursor Agent 等）设计。
> 阅读此文件 + 查看最新 Git 提交 + 浏览仓库文件 = 可继续工作。

---

## 📋 项目概要

**项目**：Psychohistory（心理史学）— 把 @PredictiveHistory YouTube 频道的知识蒸馏为 AI Skill 体系
**仓库**：`github.com/chundada/psychohistory`
**方法论版本**：v3.0 — 检索式提取（Retrieval-based Extraction）

---

## 🏗️ 仓库结构

```
Psychohistory/
├── .obsidian/                        # Obsidian 库配置（可直接在 Obsidian 中打开）
├── SPEC.md                           # ⭐ 设计规范 — 先读这个
├── PROGRESS.md                       # ⭐ 进度板 — 看当前在做什么
├── README.md                         # 项目简介
├── CONTINUE_FOR_AI.md                # ← 你现在正在读的
├── _打开库.ps1                        # 用 Obsidian 打开此库的快捷脚本
│
├── methodology/                      # 蒸馏流水线 SOP（按阶段编号）
│   ├── 00-overview.md
│   ├── 01-stage0-series-understand.md
│   ├── 02-stage1-retrieval-extract.md    # ⭐ 核心：检索式提取
│   ├── 03-stage1.5-quadruple-verify.md
│   ├── 04-stage2-ria-plus.md
│   ├── 05-stage3-cross-series-link.md
│   ├── 06-stage4-pressure-test.md
│   └── 07-stage5-deliver.md
│
├── extractors/                       # 7 路检索式提取器 Prompt
│   ├── 01-game-theory-extractor.md
│   ├── 02-geopolitics-extractor.md
│   ├── 03-civilization-extractor.md
│   ├── 04-religion-extractor.md
│   ├── 05-predictive-extractor.md
│   ├── 06-failure-extractor.md
│   └── 07-glossary-extractor.md
│
├── templates/                        # 输出模板
│
├── series/                           # 各系列源数据
│   └── game-theory/                  # 当前 Pilot
│       ├── transcripts/              # VTT + Markdown 格式字幕
│       ├── candidates/               # 检索式提取结果存放处
│       ├── rejected/                 # 四重验证淘汰
│       └── skills/                   # RIA++ 构建后的 Skill 产出
│
├── skills/                           # 已发布的跨系列 Skills
│
├── MOC-心理史学总览.md                # Obsidian 图谱入口
├── MOC-系列目录.md                    # 系列索引
├── MOC-核心方法论.md                   # 方法论索引
└── MOC-Game-Theory.md                # Pilot 入口
```

---

## ✅ Game Theory Pilot — 全部完成

```
状态: ✅ 全部完成（共 6 个阶段）
      耗时: 1 天（2026-07-13）
      产出: 52 个可调用的 Skill
```

### 最终产出

| 交付物 | 说明 |
|---|---|
| `skills/` | 52 个 RIA++ 格式 SKILL.md（含 R/I/A1/A2/E/B 六段） |
| `INDEX.md` | 按触发场景索引 + 技能总览 + 术语表 |
| `DIGEST.md` | 精华长文（10,000 字，必读） |
| `QUICK_START.md` | 场景→技能速查表（遇到问题查这个） |
| `_install_skills.ps1` | 一键安装到 `~/.claude/skills/Psychohistory/` |

### 经验总结（对后续系列）

| 学到的教训 | 后续改进 |
|---|---|
| 两阶段摘要提取→信息丢失 | 直接检索式提取（已用） |
| 压力测试不可行（416 测试无人执行） | 跳过，改用 QUICK_START 替代 |
| Zettelkasten Mermaid 图好看无用 | 跳过，INDEX 场景索引更有用 |
| E5 预测模型最丰富（12 个 HIGH） | 后续系列优先投给预测信号 |

---

## ✅ 已完成的工作

| Git 提交 | 内容 |
|----------|------|
| `d824bb2` | 📝 Stage 2: 52 个 RIA++ Skill 文件 |
| `fa70e42` | ✅ Stage 1.5: 四重验证完成 |
| `461c508` | 🔬 Stage 1: 7 路检索式提取 → 81+ 候选 |
| `7f8d8a1` | 📦 Obsidian 库 + AI 接手文档 |
| `e0aeafe` | 🎯 v3.0 检索式提取方法论 |

---

## 🔜 下一步（新系列启动）

### 优先级

1. **📜 Civilization 系列**（59 集，~60h）— 最高优先，需要先下载字幕
2. **🔮 Secret History**（27 集，~25h）
3. 其余系列见 `PROGRESS.md`

### 执行流程

```bash
# 1. 下载 Civilization 系列字幕
python -m yt_dlp --write-auto-subs --sub-langs "en" --skip-download \
  -o "series/civilization/transcripts/%(title)s.%(ext)s" \
  "https://www.youtube.com/playlist?list=..."

# 2. 依次执行 Stage 0 → 1 → 1.5 → 2 → 交付
# 3. 与已有 skills/ 做 Zettelkasten 链接
# 4. 更新 INDEX.md + DIGEST.md + 推送
```

### 启动命令

对 AI 说：
```
继续 Psychohistory，处理 Civilization 系列。下载字幕并开始 Stage 0 系列理解。
```

---

## 📝 工作规范（对 AI 代理）

### Git 提交规范

每次阶段性完成任务后执行：

```bash
git add -A
git commit -m "<emoji> <阶段名>: <做了什么>

- 具体变更条目 1
- 具体变更条目 2
- 当前状态: 下一步该做什么"
git push
```

提交信息用中文，前缀 emoji 规范：
- 🎉 初始/里程碑
- 📥 下载/数据获取
- 🔬 提取/分析
- 🎯 方法论设计/更新
- ✅ 验证/测试
- 📝 文档/模板
- 🔗 链接/体系整合

### 更新 PROGRESS.md

每次提交前更新 PROGRESS.md 中的状态标记：
- `✅` = 完成
- `🔵` = 进行中
- `⏳` = 待处理

### 先读再写

接手工作前，依次阅读：
1. `CONTINUE_FOR_AI.md`（当前文件）— 知道上下文
2. `PROGRESS.md` — 知道进度
3. `SPEC.md` — 知道设计
4. 对应阶段的 `methodology/*.md` — 知道怎么做
