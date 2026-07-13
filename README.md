# 🧠 心理史学 | Psychohistory

> **"把 YouTube 上的博弈论、地缘政治、文明规律蒸馏成 AI 可调用的知识体系"**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()
[![Pilot: Game Theory](https://img.shields.io/badge/Pilot-Game%20Theory%20%2329-blue)]()

---

## 📜 起源

> *"心理史学（Psychohistory）是一门介于心理学和历史学之间的学科，它使用数学公式来预测整个人类社会的未来行为。"*
> — Isaac Asimov，《基地》系列

本项目受 Asimov 的启发，但实践路径不同。我们不建模数学公式，而是从 **`@PredictiveHistory`** YouTube 频道——一个融合了博弈论、地缘政治、文明分析和未来预测的顶级频道——中**蒸馏出 AI 可直接调用的方法论 Skill**。

每一条 Skill 都是一个**可执行的思维框架**：当你在分析时局、理解冲突、预测趋势时，AI 会自动调用它来帮助你想得更深。

---

## 🏗️ 整体架构

```
YouTube @PredictiveHistory (7大系列, ~160集)
        │
        ▼
┌─────────────────────────────────────┐
│        Psychohistory 蒸馏流水线       │
│                                     │
│  逐集精提 → 7路并行提取 → 四重验证     │
│  → RIA++ 构造 → 跨系列链接 → 交付     │
└─────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────┐
│  可调用的 AI Skill 体系              │
│  └ 博弈论 / 地缘法则 / 文明规律       │
│  └ 宗教叙事 / 预测模型 / 思维陷阱     │
│  └ 概念词典                          │
└─────────────────────────────────────┘
```

## 📊 知识来源

| 系列 | 集数 | 覆盖话题 | 状态 |
|---|---|---|---|
| 🎯 **Game Theory** | 29集 | 博弈论·地缘政治·时局·AI未来 | **🔵 Pilot进行中** |
| 📜 Civilization | 59集 | 文明演进·社会规律·宗教历史 | ⏳ 待处理 |
| 🔮 Secret History | 27集 | 宗教哲学·权力分析·历史深层逻辑 | ⏳ 待处理 |
| 🗺️ Geo-Strategy | 19集 | 地缘战略·时局分析·预测 | ⏳ 待处理 |
| 📚 Great Books | 13集 | 经典文本·思想史 | ⏳ 待处理 |
| 🔥 Dante | 12集 | 宗教哲学·文学 | ⏳ 待处理 |

---

## 🧩 核心：7 路自定义提取器

针对心理史学的知识类型，我们设计了 **7 个并行提取器**（比 cangjie-skill 多 2 个）：

| 编号 | 提取器 | 提取什么 |
|---|---|---|
| 🎯 E1 | **博弈模型提取器** | 囚徒困境、胆小鬼博弈、信号博弈、承诺机制等 |
| 🌍 E2 | **地缘法则提取器** | 心脏地带理论、修昔底德陷阱、海权vs陆权 |
| 🏛️ E3 | **文明规律提取器** | 精英过剩、人口转型、体制僵化、兴衰周期 |
| ✝️ E4 | **宗教叙事提取器** | 弥赛亚叙事、千禧年主义、一神教革命 |
| 🔮 E5 | **预测模型提取器** ⭐ | 信号→推演→结果链、条件预测、拐点识别 |
| ⚠️ E6 | **反例陷阱提取器** | 归因错误、确认偏误、类比滥用 |
| 📖 E7 | **术语词典提取器** | 核心概念、作者独创术语 |

---

## 🔬 质量保障：四重验证

| 验证 | 核心问题 | 通过标准 |
|---|---|---|
| ✅ V1 **跨域验证** | 至少 2 集有佐证？ | 不同剧集独立确认 |
| ✅ V2 **预测力验证** | 能推导出未明说的结论？ | 产出非平庸推断 |
| ✅ V3 **独特性验证** | 不是常识？ | 作者独特的反直觉见解 |
| ✅ V4 **体系兼容** | 与其他体系不矛盾？ | 融入 Psychohistory 整体框架 |

---

## 📈 项目进度

详见 [PROGRESS.md](./PROGRESS.md)

| 里程碑 | 状态 | 产出 |
|---|---|---|
| 架构设计 | ✅ 完成 | `SPEC.md` / `methodology/` / `extractors/` / `templates/` |
| Pilot: Game Theory 转录 | 🔵 进行中 | `series/game-theory/transcripts/` |
| Pilot: Game Theory 蒸馏 | ⏳ 待开始 | Skills (预计 15-25 个) |
| Civilization 系列 | ⏳ 待处理 | |
| Secret History 系列 | ⏳ 待处理 | |
| 跨系列链接整合 | ⏳ 待处理 | |

---

## 🚀 使用方法

### 作为 AI Skill 调用

当安装后，你可以对 AI 说：

```
"用我的 Psychohistory 体系来分析当前的国际局势"
"这个场景触发了哪条博弈法则？"
"根据@PredictiveHistory 的预测模型，推演下一步"
```

### 开发者

```bash
# Clone 仓库
git clone https://github.com/chundada/psychohistory.git

# 目录结构
psychohistory/
├── methodology/          # 蒸馏流水线 SOP
├── extractors/           # 7 个提取器 Prompt
├── templates/            # 输出模板
├── series/               # 各系列的处理数据
│   └── game-theory/      # 当前 Pilot
│       ├── transcripts/  # 转录文本
│       ├── candidates/   # 提取候选池
│       ├── rejected/     # 淘汰单元
│       └── skills/       # 最终 Skill 产出
└── SPEC.md               # 完整设计规范
```

---

## 🤝 生态关系

本项目是袋鼠帝 `cangjie-skill` 蒸馏流水线的定制化实现：

```
cangjie-skill (通用知识蒸馏)
    └── psychohistory (心理史学定制版) ← 当前项目
            └── darwin-skill (未来：自动进化)
```

---

## 📄 许可证

MIT License

<h6 align="center">Built with ❤️ for the love of knowledge distillation</h6>
