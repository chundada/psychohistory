---
tags: [psychohistory, methodology]
stage: "overview"
status: "current"
---
# RIA 知识蒸馏管道全景概览

> **适配场景**：YouTube 系列视频 → 可复用 AI Skills
> **核心方法**：检索式提取（Retrieval-based Extraction）
> **流水线固定为 3 步**：Stage 0 系列理解 → Stage 1 检索式提取 → Stage 2 RIA 构造（内嵌验证）
> **已废弃环节（Stage 1.5 独立四重验证、Stage 4 压力测试、Stage 5 交付等）见 `_archive/`。**

---

## 一、管道总览

```
┌─────────────────────────────────────────────────────────────────┐
│                  RIA 知识蒸馏管道（3 步）                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Stage 0: 系列理解 (Series Understanding)                         │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 列出剧集 → 分组主题弧 → 识别核心论点 → SERIES_OVERVIEW.md  │   │
│  └──────────────────────┬───────────────────────────────────┘   │
│                         ▼                                       │
│  Stage 1: 检索式提取 (Retrieval-based Extraction) ⭐              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 7 路提取器以检索信号定位原文段落                              │   │
│  │ 不通读、不摘要、直接在完整上下文中剪裁                        │   │
│  │ 每个提取结果含 [source] = 原文精确引用                        │   │
│  │ → candidates/ 目录                                           │   │
│  └──────────────────────┬───────────────────────────────────┘   │
│                         ▼                                       │
│  Stage 2: RIA 构建（内嵌验证）⭐                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 写每个 SKILL.md 时自然三问判断：                           │   │
│  │ ① 有原文引用？ ② 有可操作步骤？ ③ 知道何时不该用？          │   │
│  │ R(原文) → I(方法论) → A(应用+执行) → B(边界)               │   │
│  │ → skills/ 目录                                              │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  （蒸馏完成后：跨系列链接，将技能接入 Zettelkasten 知识网络，       │
│    见 05-stage3-cross-series-link.md）                            │
└─────────────────────────────────────────────────────────────────┘
```

### 版本沿革（为何是 3 步）

| 改动 | 旧版（v4.0） | 现行 |
|------|------|------|
| 阶段数 | 6 | **3** |
| Stage 1.5 | 独立验证阶段（pilot 实测 98% 空转） | **已废弃**，验证内嵌至 Stage 2 |
| RIA 字段 | 6（R/I/A1/A2/E/B） | **4（R/I/A/B）** |
| Stage 4 压力测试 | 416 测试/系列，无人执行 | **已废弃** |
| Stage 5 交付 | 独立阶段 | **已废弃**（交付并入常规流程） |

> 七层汇聚验证（`convergence-verify.md`）是 **AI 调用技能库分析问题时**的方法，不属于本蒸馏流水线。

---

## 二、与书籍蒸馏管道的关键差异

| 维度 | 书籍蒸馏（原版） | 视频系列蒸馏（本版） |
|------|-----------------|-------------------|
| **输入单元** | 全书（章节连续） | 每集一个独立 VTT 文件，按系列聚合 |
| **提取方式** | 通读后概括提取 | **检索式提取**：信号定位 + 上下文裁剪 |
| **提取器数量** | 5 个提取器 | **7 个提取器**（小系列可选 3-5 个） |
| **验证方式** | 独立验证阶段 | **内嵌验证**：写 SKILL.md 时自然完成三问判断 |
| **系列融合** | 无跨章节依赖分析 | 跨剧集一致性检查（内嵌验证核心环节） |
| **交付物** | 单篇 SKILL.md | SERIES_OVERVIEW.md + INDEX.md + DIGEST.md 三层 |

---

## 三、核心设计原则

### 3.1 保真优先（Fidelity First）
**不经过中间摘要**。提取器直接从原文剪裁，每个候选输出的 `[source]` 字段必须包含原始 VTT 文件名和时间戳范围，确保可追溯。

### 3.2 检索式而非通读式（Search, Don't Read）
每个提取器不尝试"理解"全文，而是以专属检索信号（关键词/模式/概念线索）定位高价值段落，在命中处展开上下文阅读。这避免了长篇文本中的精度衰减。**信号词语言必须与源字幕原文一致**（英文 VTT 用英文信号词），命中后再做中文解读。

### 3.3 可操作性（Actionability）
每个技能必须回答"我什么时候用、怎么用、什么时候不用"。A（应用）和 B（边界条件）不可空缺。

### 3.4 系统兼容性（System Compatibility）
内嵌验证确保新技能不与已有技能冲突。若冲突，优先修改新技能而非已有技能。

### 3.5 渐进式投入（Progressive Investment）
每次只处理一个系列。新系列处理完毕后，与已有 skills 做 Zettelkasten 链接即可融入体系。

---

## 四、目录结构约定

```
Psychohistory/
├── methodology/           # 管道各阶段说明（3 步流水线）
│   ├── 00-overview.md                        # 本文件
│   ├── 01-stage0-series-understand.md        # Stage 0：系列理解
│   ├── 02-stage1-retrieval-extract.md        # Stage 1：检索式提取
│   ├── 04-stage2-ria-plus.md                 # Stage 2：RIA 构造（内嵌验证）
│   ├── 05-stage3-cross-series-link.md        # 蒸馏后：跨系列链接
│   ├── convergence-verify.md                 # AI 调用时的七层汇聚验证（非蒸馏阶段）
│   └── _archive/                             # ⚠️ 已废弃环节存档，勿再执行
│       ├── 03-stage1.5-quadruple-verify.md   # 已废弃：独立四重验证（内嵌至 Stage 2）
│       ├── 06-stage4-pressure-test.md        # 已废弃：压力测试（从未执行）
│       ├── 07-stage5-deliver.md              # 已废弃：独立交付阶段
│       └── test-prompts.json.template        # 已废弃：压力测试配套模板
├── templates/             # 模板文件
│   ├── SERIES_OVERVIEW.md.template
│   ├── SKILL.md.template
│   └── PSYCHOHISTORY_INDEX.md.template
├── extractors/            # 7 个检索式提取器定义（含检索信号表，唯一事实源）
│   ├── 01-game-theory-extractor.md
│   ├── 02-geopolitics-extractor.md
│   ├── 03-civilization-extractor.md
│   ├── 04-religion-extractor.md
│   ├── 05-predictive-extractor.md
│   ├── 06-finance-economy-extractor.md        # E6 现役（v4.2 起）
│   ├── 07-glossary-extractor.md
│   └── deprecated-06-failure-extractor.md     # ⚠️ 已废弃（v4.2）：反例陷阱防护内嵌至 Stage 2
├── series/                # 各系列源数据
│   └── <series-name>/
│       ├── transcripts/   # VTT 原始字幕（全文检索源）
│       ├── candidates/    # 检索式提取结果
│       └── skills/        # RIA 构建后的 Skill 产出
├── skills/                # 输出目录：已发布的 SKILL.md 文件（跨系列）
├── INDEX.md               # 主索引（跨系列链接）
└── DIGEST.md              # 精华阅读
```

---

## 五、质量门禁（Quality Gates）

| 关卡 | 阶段 | 通过标准 |
|------|------|---------|
| QG1 | Stage 0 完成 | SERIES_OVERVIEW.md 包含所有必填字段（见模板） |
| QG2 | Stage 1 完成 | 每个运行的提取器各产生至少 5 个候选，每个候选含 [source] 引用 |
| QG3 | Stage 2 完成 | 每篇 SKILL.md 的 R 段含可核实的原文引用；三问判断全部通过 |
| QG4 | 跨系列链接完成 | INDEX.md Mermaid 图可编译无报错 |

> 旧版 QG（Stage 1.5 / Stage 4 / Stage 5 关卡）已随对应环节一并废弃，见 `_archive/`。

---

## 六、工作量估算

| 阶段 | 估算耗时 | 注意 |
|------|---------|------|
| Stage 0 | 30-60 min | 浏览播放列表、初步主题分类 |
| Stage 1（检索式提取）| 60-90 min/系列 | 每个提取器独立运行，可并行；小系列只跑 3-5 个提取器 |
| Stage 2 | 20-30 min/技能 | 复用模板减少格式耗时；验证内嵌完成，无额外阶段 |
| 跨系列链接 | 15-20 min/系列 | 只创建确实存在的依赖关系 |

---

## 七、快速开始

```bash
# 1. 进入 Psychohistory 工作目录
cd Psychohistory/

# 2. 准备系列源数据
series/<series-name>/transcripts/  # 放入 VTT 字幕文件

# 3. Stage 0：按 templates/SERIES_OVERVIEW.md.template 完成系列理解
# 4. Stage 1：以检索信号扫描完整字幕（信号表见 extractors/ 目录）
# 5. Stage 2：构造 RIA 技能（模板见 templates/SKILL.md.template），三问内嵌验证
# 6. 完成后做跨系列链接，更新 INDEX.md
```

---

*本文档对应现行 3 步 RIA 蒸馏管道（Stage 0 → 1 → 2）。已废弃环节存档于 `_archive/`；AI 调用技能库时的七层汇聚验证见 `convergence-verify.md`（唯一事实源为 `PSYCHOHISTORY_SYSTEM_PROMPT.md`）。*
