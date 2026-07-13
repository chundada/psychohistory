---
tags: [psychohistory, core]
type: "readme"
---
# 🧠 心理史学 | Psychohistory

> **"把 YouTube 上的博弈论、地缘政治、文明规律蒸馏成 AI 可调用的知识体系"**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()
[![Pilot: Game Theory](https://img.shields.io/badge/Pilot-Game%20Theory-blue)]()

---

## 📜 起源

> *"心理史学（Psychohistory）是一门介于心理学和历史学之间的学科，它使用数学公式来预测整个人类社会的未来行为。"*
> — Isaac Asimov，《基地》系列

本项目受 Asimov 的启发，但实践路径不同。我们不建模数学公式，而是从 **`@PredictiveHistory`** YouTube 频道——一个融合了博弈论、地缘政治、文明分析和未来预测的顶级频道（160+ 集，涵盖 7 大系列）——中**检索式提取可复用的思维框架**，蒸馏为 AI 可直接调用的方法论 Skill。

每一条 Skill 都是一个**可执行的思维框架**：当你分析时局、理解冲突、预测趋势时，AI 会自动调用它来帮你思考更深。

---

## 🏗️ 整体架构

### 旧方案 vs 新方案

```
❌ 旧方案（两阶段摘要提取）：
   29集字幕 → 每集500字摘要(1000:1压缩) → 提取器读摘要 → 质量损失严重

✅ 新方案（检索式提取 Retrieval-based Extraction）：
   29集原始字幕（零压缩） → 7路提取器以检索信号定位原文段落
                           → 在完整上下文中直接剪裁方法论
                           → 每个候选含精确原文引用 [source]
```

### 完整流程图

```
YouTube @PredictiveHistory
7 大系列 · ~160 集
       │
       ▼
┌─────────────────────────────────────────────────────────┐
│  Stage 0: 系列理解                                       │
│  列出剧集 → 分组主题弧 → 识别核心论点 → SERIES_OVERVIEW.md │
└────────────────────────┬────────────────────────────────┘
                         ▼
┌─────────────────────────────────────────────────────────┐
│  Stage 1: ⭐ 检索式提取（核心创新）                        │
│                                                         │
│  保留 29 集完整 VTT 字幕原文（零压缩）                     │
│  每个提取器以专属 检索信号 定位高价值方法论段落              │
│  找到信号命中后，在完整上下文中直接阅读并剪裁                │
│  每个提取结果含 [source] = 文件名 + 时间戳 → 可追溯原文     │
│                                                         │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │ E1 博弈  │ │ E2 地缘  │ │ E3 文明  │ │ E4 宗教  │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                │
│  │E5 预测⭐ │ │E6 陷阱   │ │E7 术语   │                │
│  └──────────┘ └──────────┘ └──────────┘                │
└────────────────────────┬────────────────────────────────┘
                         ▼
┌─────────────────────────────────────────────────────────┐
│  Stage 1.5: 四重验证                                     │
│  V1 跨剧集一致性 → V2 预测力 → V3 独特性 → V4 体系兼容    │
└────────────────────────┬────────────────────────────────┘
                         ▼
┌─────────────────────────────────────────────────────────┐
│  Stage 2: RIA++ 构造                                     │
│  R(原文) → I(方法论) → A1(案例) → A2(触发) → E(步骤) → B(边界) │
└────────────────────────┬────────────────────────────────┘
                         ▼
┌─────────────────────────────────────────────────────────┐
│  Stage 3-5: 跨系列链接 → 压力测试 → 交付到 skills 目录     │
└─────────────────────────────────────────────────────────┘
                         ▼
              ┌──────────────────────┐
              │  可调用的 AI Skill 体系 │
              │  博弈论 / 地缘法则     │
              │  文明规律 / 宗教叙事   │
              │  预测模型 / 思维陷阱   │
              │  概念词典              │
              └──────────────────────┘
```

---

## 📊 知识来源：7 大系列

| 系列 | 集数 | 时长 | 话题覆盖 | 状态 |
|---|---|---|---|---|
| 🎯 **Game Theory** | **29** | ~15h | 🎲 博弈论 · 🌍 地缘政治 · 🤖 AI · 🔮 预测 | **🔵 进行中** |
| 📜 **Civilization** | **59** | ~60h | 🏛️ 文明演进 · 👥 社会规律 · ✝️ 宗教 | ⏳ 待处理 |
| 🔮 **Secret History** | **27** | ~25h | 📖 宗教哲学 · ⚔️ 权力 · 🔍 历史深层逻辑 | ⏳ 待处理 |
| 🗺️ **Geo-Strategy** | **11+8** | ~8h | 🌏 地缘战略 · 📡 时局 · 🔮 预测 | ⏳ 待处理 |
| 📚 **Great Books** | **13** | ~5h | 📕 经典文本 · 💭 思想史 | ⏳ 待处理 |
| 🔥 **Dante** | **12** | ~50h | ✝️ 宗教哲学 · 📜 文学 | ⏳ 待处理 |
| 🌐 **Geo-Strategy Updates** | **8** | ~3h | 📰 短期时局分析 | ⏳ 待处理 |

---

## 🔬 核心：7 路检索式提取器

每个提取器以**检索信号（Search Signals）** 直接定位原文，不经过中间摘要。

| 编号 | 提取器 | 检索信号示例 | 命中预期 |
|---|---|---|---|
| 🎯 | **E1 博弈模型提取器** | `prisoner dilemma`, `escalation`, `asymmetry`, `MAD`, `signaling` | 博弈论框架 |
| 🌍 | **E2 地缘法则提取器** | `heartland`, `Thucydides trap`, `sea power`, `buffer state` | 地缘政治规律 |
| 🏛️ | **E3 文明规律提取器** | `elite overproduction`, `asabiyyah`, `institutional sclerosis` | 文明兴衰模式 |
| 📖 | **E4 宗教叙事提取器** | `messianic`, `eschatology`, `monotheism`, `Dante` | 宗教/神话结构 |
| 🔮 | **E5 预测模型提取器** ⭐ | `if...then`, `predict`, `future`, `scenario`, `tipping point` | 预测推理链 |
| ⚠️ | **E6 反例陷阱提取器** | `mistake`, `fallacy`, `bias`, `oversimplification` | 思维错误识别 |
| 📖 | **E7 术语词典提取器** | `defined as`, `coined`, `by this I mean` | 核心概念词典 |

> **检索式提取的核心优势**：不压缩、不摘要、每一条方法论候选都带有可追溯的原文引用。29 集原始字幕就是源数据库，提取器在上面做"检索—定位—剪裁"。

---

## ✅ 四重验证质量保障

| 验证 | 核心问题 | 通过率预期 |
|---|---|---|
| ✅ **V1 跨剧集一致性** | 该方法论至少出现在 2 集以上？ | 通过后保留 |
| ✅ **V2 预测力** | 能产生可 falsifiable 的预测？ | 通过后保留，无预测力降级 |
| ✅ **V3 独特性** | 不是任何人都知道的常识？ | 通过后保留 |
| ✅ **V4 体系兼容性** | 与已有 Skills 体系不矛盾？ | 冲突时优先修改新技能 |

**预期通过率**：原始提取池 ~100-200 个候选 → 四重验证后 ~25-50 个 → 最终 Skill ~15-30 个。

---

## 🚀 使用方法

### 作为 AI Skill 调用

当安装后，你可以对 AI 直接说：

```
"用 Psychohistory 的博弈模型分析当前的国际局势"
"这个地缘政治场景触发了哪条法则？"
"根据@PredictiveHistory 的预测模型，推演下一步可能走向"
"当前局势有哪些常见的分析陷阱需要注意？"
```

### 开发者

```bash
# 克隆仓库
git clone https://github.com/chundada/psychohistory.git
cd psychohistory

# 项目结构
psychohistory/
├── SPEC.md                          # 完整设计规范
├── PROGRESS.md                      # 进度追踪板
├── INSPIRATION-*.vtt                # 灵感来源视频字幕
├── methodology/                     # 蒸馏流水线 SOP（8篇）
│   ├── 00-overview.md               #   全景概览
│   ├── 01-stage0-series-understand.md
│   ├── 02-stage1-retrieval-extract.md  # ⭐ 检索式提取
│   ├── 03-stage1.5-quadruple-verify.md
│   ├── 04-stage2-ria-plus.md
│   ├── 05-stage3-cross-series-link.md
│   ├── 06-stage4-pressure-test.md
│   └── 07-stage5-deliver.md
├── extractors/                      # 7 个检索式提取器 Prompt
│   ├── 01-game-theory-extractor.md
│   ├── 02-geopolitics-extractor.md
│   ├── 03-civilization-extractor.md
│   ├── 04-religion-extractor.md
│   ├── 05-predictive-extractor.md   # ⭐ 最高优先级
│   ├── 06-failure-extractor.md
│   └── 07-glossary-extractor.md
├── templates/                       # 输出模板（4个）
├── series/                          # 各系列源数据
│   └── game-theory/                 # 当前 Pilot
│       ├── transcripts/             #   VTT 原始字幕（检索源）
│       ├── candidates/              #   检索式提取候选
│       ├── rejected/                #   四重验证淘汰
│       └── skills/                  #   RIA++ 后的 Skill 产出
└── skills/                          # 已发布的跨系列 Skills
```

---

## 🧩 方法论进化

| 版本 | 日期 | 变更 |
|------|------|------|
| **v3.0** | 2026-07-13 | ⭐ **检索式提取**：删除两阶段摘要提取，改为检索信号+上下文剪裁 |
| v2.0 | 2026-07-13 | 初始：两阶段摘要提取架构 |

---

## 📈 项目进度

| 里程碑 | 状态 | 产出 |
|---|---|---|
| 方法论设计（v3.0） | ✅ 完成 | `SPEC.md` · 8 篇 methodology · 7 个 extractors · 4 个 templates |
| Game Theory 字幕下载 | ✅ 完成 | 29 集 VTT 字幕（~12.5MB，零压缩） |
| **检索式提取 Phase 2** | **🔵 进行中** | 7 路提取器并行运行 |
| Civilization 系列 | ⏳ 待处理 | |
| Secret History 系列 | ⏳ 待处理 | |
| 跨系列链接整合 | ⏳ 待处理 | |

> 🔗 详细进度追踪见 [PROGRESS.md](./PROGRESS.md)

---

## 🤝 生态关系

本项目基于袋鼠帝 `cangjie-skill` 的 RIA-TV++ 蒸馏流水线，针对 YouTube 视频系列场景进行了深度定制：

```
cangjie-skill（通用知识蒸馏）
  └── psychohistory（心理史学 · 检索式提取定制版）
        └── darwin-skill（未来接入：自动进化）
```

---

## 📄 许可证

MIT License

<h6 align="center">📡 "The future is what you imagine, not what happens to you."</h6>
<h6 align="center">— Geo-Strategy END: Psychohistory</h6>
