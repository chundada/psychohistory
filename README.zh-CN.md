# Psychohistory — 心理史学 · 知识蒸馏框架

> 将高维度的历史分析智慧蒸馏为 AI 可调用的结构化方法论

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills: 142](https://img.shields.io/badge/技能-142-brightgreen)]()
[![Series: 4](https://img.shields.io/badge/系列-4-blue)]()
[![Status: Active](https://img.shields.io/badge/状态-进行中-ff6600)]()

---

## 概览

本项目将 [@PredictiveHistory](https://www.youtube.com/@PredictiveHistory) YouTube 频道的**160+ 小时授课内容**——涵盖博弈论、地缘政治、文明规律、宗教叙事四大领域——蒸馏为 **142 个结构化、可复用的 Skill 文件**，供 AI 直接调用。

核心前提：历史预测不是占卜。它是一种**多框架交叉验证方法**，基于可识别的结构模式、明确的边界条件和可证伪的逻辑链条。

---

## 项目产出

| 交付物 | 说明 |
|---|---|
| **142 个 Skill 文件** | 结构化分析框架，遵循 RIA/RIA++ 格式，包含原文阅读、方法论解读、应用场景和边界条件 |
| **PSYCHOHISTORY_SYSTEM_PROMPT.md** | 完整角色激活提示——粘贴到任意 AI 中，即刻激活心理史学家身份 |
| **QUICK_START.md** | 场景→技能速查表（22 个场景映射到推荐技能组合） |
| **INDEX.md** | Zettelkasten 风格技能索引，含触发场景关键词 |
| **DIGEST.md** | Game Theory 系列精华长文阅读 |

---

## 方法论：检索式蒸馏

传统知识蒸馏遵循"压缩→摘要"的路线，存在不可逆的信息损失。本项目采用**检索式提取**方案：

1. **零压缩保留源数据**：原始授课字幕完整保留
2. **7 路并行提取器**：每路提取器针对特定分析领域，搭载定制检索信号
3. **从完整上下文中直接提取**：方法论直接从完整转录文本中剪裁，附带原文时间戳，可追溯验证
4. **四重验证**：每个候选经过四道独立筛选后方可入库

### 提取器架构

| 提取器 | 检索信号 | 产出类型 |
|---|---|---|
| **博弈模型** | 囚徒困境、非对称、升级、MAD | 博弈论框架 |
| **地缘法则** | 心脏地带、修昔底德陷阱、咽喉要道 | 地缘规律 |
| **文明规律** | 精英过剩、阿萨比亚、崩溃 | 文明周期模型 |
| **宗教叙事** | 弥赛亚、末世论、一神教 | 叙事解码 |
| **预测模型** | 如果…那么、预测、场景、临界点 | 预测推理链 |
| **经济金融** | 债务、泡沫、通胀、美元、信贷危机 | 经济框架 |
| **术语词典** | 定义为、我是说、创造 | 核心概念 |

---

## 当前进度

**已完成 4 个系列 · 142 个 Skill 文件 · 约 75% 的课程内容已处理**

| 系列 | 集数 | 技能数 | 格式 | 位置 |
|---|---|---|---|---|
| Game Theory | 29 | 52 | RIA++（R/I/A1/A2/E/B 六段） | `skills/gt-*.md` |
| Secret History | 27 | 45 | RIA（R/I/A/B 四段） | `skills/sh-*.md` |
| Geo-Strategy | 19 | 35 | RIA（R/I/A/B 四段） | `skills/gs-*.md` |
| Interview | — | 10 | RIA | `skills/interview-*.md` |
| **待处理** | | | | |
| Civilization | 59 | 预计 35-45 | — | — |
| Great Books | 13 | — | — | — |
| Dante | 12 | — | — | — |

---

## 分析能力覆盖

技能库覆盖七大领域：

| 领域 | 核心框架 |
|---|---|
| **博弈论** | 非对称法则、升级校准、邻近法则、移民陷阱、精英过剩动力学 |
| **地缘政治** | 地缘三定律、咽喉要道控制、货币战争、美元瘾症模型 |
| **文明周期** | 阿萨比亚、EOC 模型、制度硬化、生育率先行指标、雇佣兵反噬 |
| **宗教叙事** | 末世论汇聚、弥赛亚加速主义、卡巴拉救赎、AI 宗教化 |
| **预测模型** | 多重框架汇聚、帝国衰退三指标、内战投射、因果链分析 |
| **思维陷阱** | 伟人迷思、AI 意识幻觉、相关即因果、虚假二分法 |
| **术语词典** | 马赛克防御、精英过剩、现实幻觉、技术统治国 |

每个 Skill 遵循一致的结构：**原文阅读 → 方法论解读 → 作者应用 → 触发条件 → 执行步骤 → 边界条件**，使系统化的交叉验证成为可能。

---

## 快速开始

### 方式 A：克隆并安装

```powershell
git clone https://github.com/chundada/psychohistory.git
cd psychohistory
PowerShell -ExecutionPolicy Bypass .\_install_skills.ps1
```

### 方式 B：配合任意 AI 使用

将 `PSYCHOHISTORY_SYSTEM_PROMPT.md` 粘贴为系统提示。AI 将自动：

1. 激活心理史学家身份
2. 从技能库中选取 2-4 个相关技能
3. 执行**多重框架汇聚验证**
4. 使用思维陷阱清单进行自我校准
5. 输出**条件式预测**，附带明确的边界条件

---

## 仓库结构

```
Psychohistory/
├── PSYCHOHISTORY_SYSTEM_PROMPT.md   ⬅ 角色激活提示
├── skills/                            ⬅ 142 个结构化 Skill 文件
│   ├── gt-*.md                        Game Theory 系列
│   ├── sh-*.md                        Secret History 系列
│   ├── gs-*.md                        Geo-Strategy 系列
│   └── interview-*.md                 Interview 系列
├── cases/                             ⬅ 实战分析案例
├── QUICK_START.md                     ⬅ 场景→技能速查表
├── DIGEST.md                          ⬅ 精华阅读
├── INDEX.md                           ⬅ Zettelkasten 索引
├── PROGRESS.md                        ⬅ 项目进度追踪
├── CLAUDE.md                          ⬅ AI 工作区配置
├── extractors/                        ⬅ 7 路检索式提取器
├── methodology/                       ⬅ 蒸馏流水线 SOP
├── series/                            ⬅ 各系列源数据
│   ├── psychohistory-origin/
│   ├── game-theory/
│   ├── geo-strategy/
│   ├── secret-history/
│   └── interview-jang-letstalk/
└── SPEC.md                            ⬅ 设计规范
```

---

## 许可

本项目采用 MIT 许可协议——详见 [LICENSE](LICENSE) 文件。

---

<p align="center">
  142 个心理史学模型 · 4 个系列 · 持续扩张中<br/>
  <em>"预测的目的不是为了预见未来——而是让未来变得更好。"</em>
</p>
