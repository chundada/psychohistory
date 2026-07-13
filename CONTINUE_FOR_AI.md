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

## 🔵 当前阶段

### Game Theory 系列 Pilot — Stage 1 检索式提取

```
状态: ✅ Stage 0 完成（系列理解）
      ✅ 字幕下载完成（29集 VTT + Markdown）
      ⏳ Stage 1 检索式提取 — 未开始
      ⏳ Stage 1.5 四重验证 — 未开始
      ⏳ Stage 2 RIA++ — 未开始
      ⏳ Stage 3-5 链接/测试/交付 — 未开始
```

### 下一步工作

执行 Stage 1 检索式提取：

1. 读 `methodology/02-stage1-retrieval-extract.md` 了解检索式提取的完整流程
2. 7 个提取器并行运行，每个提取器以检索信号扫描 29 集全文
3. 每次命中检索信号 → 在完整上下文中阅读 → 剪裁方法论候选
4. 候选写入 `series/game-theory/candidates/`，按提取器分目录
5. 每个候选必须包含 `[source]` = 文件名 + 时间戳（可追溯原文）

---

## ✅ 已完成的工作

| Git 提交 | 内容 |
|----------|------|
| `e0aeafe` | 🎯 v3.0 方法论升级：检索式提取替代两阶段摘要 |
| `05b97e6` | 🔬 29 集逐集精提完成 |
| `282f869` | 📥 Game Theory 29 集字幕下载 |
| `e67d800` | 🎉 初始提交：架构文档 + 提取器 + 模板 |

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
