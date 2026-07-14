# 心理史学 · Psychohistory — 知识蒸馏框架

> 将 [@PredictiveHistory](https://www.youtube.com/@PredictiveHistory) YouTube 频道的博弈论、地缘政治、文明规律与宗教叙事知识蒸馏为 AI 可调用的结构化方法论体系。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills: 149](https://img.shields.io/badge/技能-149-brightgreen)]()
[![Series: 5](https://img.shields.io/badge/系列-5-blue)]()
[![Status: Active](https://img.shields.io/badge/状态-进行中-ff6600)]()

---

## 概念

心理史学（Psychohistory）是 Isaac Asimov 在《基地》系列中提出的虚构科学，揉合历史学、数学、社会心理学、社会学与统计学，用于预测巨大人口的未来活动。Asimov 借鉴热力学原理：单个粒子运动不可描述，但大量粒子的运动可以精确描述——当人口以百兆计时，人类社会动向可通过统计科学预知。

本项目以 Asimov 的理念为灵感，但实践路径不同：不建模数学公式，而是将 [@PredictiveHistory](https://www.youtube.com/@PredictiveHistory) 频道 160+ 小时的授课内容——涵盖博弈论、地缘政治、文明规律、宗教叙事四大领域——蒸馏为 **149 个结构化、可复用的 AI Skill 文件**。每个 Skill 遵循 RIA/RIA++ 格式，包含原文引用、方法论解读、应用场景与边界条件，供 AI 直接调用。

核心前提：历史预测不是占卜。它是一种**多框架交叉验证方法**，基于可识别的结构模式、明确的边界条件和可证伪的逻辑链条。

---

## 方法论

### 检索式蒸馏

传统知识蒸馏遵循"压缩→摘要"路线，存在不可逆的信息损失。本项目采用**检索式提取（Retrieval-based Extraction）**方案：

1. **零压缩保留源数据**：原始授课字幕完整保留，不经过任何中间摘要压缩
2. **7 路并行提取器**：每路提取器针对特定分析领域，搭载定制检索信号（Search Signals），直接在完整上下文中定位方法论
3. **从完整上下文中直接提取**：方法论直接从完整转录文本中剪裁，附带原文时间戳，可追溯验证
4. **四重验证**：每个候选经过跨域验证（V1）、预测力验证（V2）、独特性验证（V3）、体系兼容验证（V4）四道独立筛选后方可入库
5. **内嵌式验证**：验证不单独成阶段，写 Skill 时自然完成，避免验证阶段空转

### 7 路提取器架构

| 提取器 | 检索信号 | 产出类型 |
|---|---|---|
| **博弈模型** | 囚徒困境、非对称、升级、MAD、承诺、均衡 | 博弈论框架 |
| **地缘法则** | 心脏地带、修昔底德陷阱、咽喉要道、缓冲区、帝国 | 地缘规律 |
| **文明规律** | 精英过剩、Asabiyyah、制度硬化、崩溃、兴衰 | 文明周期模型 |
| **宗教叙事** | 弥赛亚、末世论、一神教、神圣文本、预言 | 叙事解码 |
| **预测模型** | 如果…那么、预测、场景推演、临界点、拐点 | 预测推理链 |
| **经济金融** | 债务、泡沫、通胀、美元霸权、信贷危机、货币政策 | 经济框架 |
| **术语词典** | 作者自创术语、反复出现的核心概念、关键定义 | 核心概念 |

各提取器独立扫描全文，检索信号命中时读取前后至少 5 行上下文（或到自然段落结束），提取结果包含 `[source] = 文件名 + 时间戳范围` 作为引文锚点。

---

## 系列分布

**当前已完成 5 个系列 · 149 个 Skill 文件 · 约 75% 的课程内容已处理**

| 系列 | 来源集数 | 技能数 | 格式 | 位置 |
|---|---|---|---|---|
| Psychohistory Origin | — | 6 | RIA 四段（R/I/A/B） | `skills/ph-origin-*.md` |
| Game Theory | 29 | 52 | RIA++ 六段（R/I/A1/A2/E/B） | `skills/gt-*.md` |
| Secret History | 28 | 46 | RIA 四段（R/I/A/B） | `skills/sh-*.md` |
| Geo-Strategy | 19 | 35 | RIA 四段（R/I/A/B） | `skills/gs-*.md` |
| Interview (Jang Let's Talk) | — | 10 | RIA 四段 | `skills/interview-*.md` |
| **合计** | **~76** | **149** | | |

**待处理系列：**

| 系列 | 集数 | 预计技能数 | 优先级 |
|---|---|---|---|
| Civilization | 59 | 25-35 | ⭐⭐⭐ 最高 |
| Great Books | 13 | 8-12 | ⭐⭐ |
| Dante | 12 | 8-10 | ⭐ |

---

## 分析能力覆盖

技能库覆盖七大领域：

| 领域 | 核心框架 |
|---|---|
| **博弈论** | 非对称法则、升级校准、邻近法则、移民陷阱、精英过剩动力学 |
| **地缘政治** | 地缘三定律、咽喉要道控制、货币战争、美元瘾症模型 |
| **文明周期** | Asabiyyah、EOC 三维模型、制度硬化、生育率先行指标、雇佣兵反噬 |
| **宗教叙事** | 末世论汇聚、弥赛亚加速主义、卡巴拉救赎、AI 宗教化、末世论作为地缘政治编码 |
| **预测模型** | 多重框架汇聚验证、帝国衰退三指标、内战投射、因果链分析、历史类比预测 |
| **思维陷阱** | 伟人迷思、AI 意识幻觉、相关即因果谬误、虚假二分法、优势即劣势悖论、民族国家幻觉 |
| **术语词典** | 马赛克防御、精英过剩、现实幻觉、技术统治国、三大超结构、EOC 模型 |

每个 Skill 遵循一致的结构：**原文引用 → 方法论解读 → 作者应用案例 → 触发条件 → 执行步骤 → 边界条件**，使系统化的交叉验证成为可能。

---

## 核心交付物

| 交付物 | 说明 |
|---|---|
| **149 个 Skill 文件** | 结构化分析框架，分布于 `skills/` 目录，含 RIA/RIA++ 格式 |
| **PSYCHOHISTORY_SYSTEM_PROMPT.md** | 完整角色激活提示——粘贴到任意 AI 中即刻激活心理史学家身份 |
| **QUICK_START.md** | 场景→技能速查表（22 个场景映射到推荐技能组合） |
| **INDEX.md** | Zettelkasten 风格技能索引，含触发场景关键词和术语表 |
| **DIGEST.md** | Game Theory 系列精华长文阅读 |
| **PROGRESS.md** | 项目进度追踪与路线图 |
| **实战案例** | CASE-001 第三次世界大战催化阶段分析、CASE-002 地缘经济展望 2026-2027 |

---

## 快速开始

### 方式 A：克隆并安装

```powershell
git clone https://github.com/chundada/psychohistory.git
cd psychohistory
PowerShell -ExecutionPolicy Bypass .\_install_skills.ps1
```

### 方式 B：配合任意 AI 使用

将 `PSYCHOHISTORY_SYSTEM_PROMPT.md` 粘贴为系统提示，AI 将自动：

1. 激活心理史学家身份
2. 从技能库中选取 2-4 个相关技能
3. 执行**多重框架汇聚验证**
4. 使用思维陷阱清单进行自我校准
5. 输出**条件式预测**，附带明确的边界条件

### 核心工作流

```
Step 1: 定位博弈       → 地缘政治三定律 + 邻近法则
Step 2: 评估力量       → 非对称法则 + EOC 三维模型
Step 3: 检查信号       → 帝国衰退三指标 + 精英过剩
Step 4: 解码叙事       → 末法汇聚 + 末世论编码
Step 5: 多重验证       → 多重框架汇聚验证法 ⭐
Step 6: 校准偏见       → 7 个 Failure Mode Skills
```

---

## 仓库结构

```
Psychohistory/
├── PSYCHOHISTORY_SYSTEM_PROMPT.md   ⬅ 角色激活提示
├── skills/                            ⬅ 149 个结构化 Skill 文件
│   ├── ph-origin-*.md                 Psychohistory Origin（6）
│   ├── gt-*.md                        Game Theory（52）
│   ├── sh-*.md                        Secret History（46）
│   ├── gs-*.md                        Geo-Strategy（35）
│   └── interview-*.md                 Interview（10）
├── cases/                             ⬅ 实战分析案例
├── QUICK_START.md                     ⬅ 场景→技能速查表
├── DIGEST.md                          ⬅ 精华阅读
├── INDEX.md                           ⬅ Zettelkasten 索引
├── PROGRESS.md                        ⬅ 项目进度追踪
├── CLAUDE.md                          ⬅ AI 工作区配置
├── extractors/                        ⬅ 7 路检索式提取器 Prompt
├── methodology/                       ⬅ 蒸馏流水线 SOP（8 篇）
├── templates/                         ⬅ 输出模板
├── series/                            ⬅ 各系列源数据
│   ├── psychohistory-origin/          Origin 系列
│   ├── game-theory/                   Game Theory 系列
│   ├── geo-strategy/                  Geo-Strategy 系列
│   ├── secret-history/                Secret History 系列
│   └── interview-jang-letstalk/       Interview 系列
├── SPEC.md                            ⬅ 设计规范
├── MOC-心理史学总览.md                ⬅ Obsidian 图谱入口
├── MOC-系列目录.md                    ⬅ 系列索引
├── MOC-核心方法论.md                   ⬅ 方法论索引
└── MOC-Game-Theory.md                 ⬅ Game Theory 入口
```

---

## 学术脉络

心理史学作为分析框架，其思想渊源可追溯至：

- **Isaac Asimov《基地》系列**：提出心理史学概念，以统计数学预测人类社会未来
- **Peter Turchin 历史动力学（Cliodynamics）**：精英过剩崩溃模型、Asabiyyah 凝聚力理论
- **Karl Marx 历史唯物主义**：文学评论界认为心理史学与历史唯物主义存在相似之处，两者都认为人类社会发展轨迹有客观规律可循
- **Halford Mackinder 心脏地带理论**：地缘政治三定律的理论基础
- **Thomas Kuhn 范式转换**：制度硬化与文明衰落的科学哲学对应

---

## 许可

本项目采用 MIT 许可协议——详见 [LICENSE](LICENSE) 文件。

---

<p align="center">
  149 个心理史学模型 · 5 个系列 · 持续扩张中<br/>
  <em>"预测的目的不是为了预见未来——而是让未来变得更好。"</em>
</p>