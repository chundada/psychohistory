---
tags: [psychohistory, methodology]
stage: "Stage 0"
status: "complete"
---
# RIA-TV++ 知识蒸馏管道全景概览

> **适配场景**：YouTube 系列视频 → 可复用 AI Skills
> **核心方法**：检索式提取（Retrieval-based Extraction）

---

## 一、管道总览

```
┌─────────────────────────────────────────────────────────────────┐
│                  RIA+ 知识蒸馏管道（3 阶段）                       │
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
│  Stage 2: RIA+ 构建 (内嵌验证) ⭐                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 写每个 SKILL.md 时自然三问判断：                           │   │
│  │ ① 有原文引用？ ② 有可操作步骤？ ③ 知道何时不该用？          │   │
│  │ R(原文) → I(方法论) → A(应用+执行) → B(边界)               │   │
│  │ → skills/ 目录                                              │   │
│  └──────────────────────┬───────────────────────────────────┘   │
│                         ▼                                       │
│  Stage 3: 交付 (Delivery)                                      │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ DIGEST.md + INDEX.md + 安装到 skills/ 目录                │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### v4.0 → v4.1 改进

| 改动 | v4.0 | v4.1 |
|------|------|------|
| 阶段数 | 6 | **3** |
| Stage 1.5 | 独立验证阶段（98% 空转） | **已废弃**，改为内嵌 |
| RIA 字段 | 6（R/I/A1/A2/E/B） | **4（R/I/A/B）** |
| Stage 3-5 | 三个独立阶段 | **合并为 Stage 3** |
| 压力测试 | 416 测试/系列，无人执行 | **已废弃** |

---

## 二、与书籍蒸馏管道的六大关键差异

| 维度 | 书籍蒸馏（原版） | 视频系列蒸馏（本版） |
|------|-----------------|-------------------|
| **输入单元** | 全书（章节连续） | 每集一个独立 VTT 文件，按系列聚合 |
| **提取方式** | 通读后概括提取 | **检索式提取**：信号定位 + 上下文裁剪 |
| **提取器数量** | 5 个提取器 | **7 个提取器** |
| **验证维度** | 三重验证（V1-V3） | **四重验证**（新增 V4 系统兼容性） |
| **系列融合** | 无跨章节依赖分析 | 跨剧集一致性检查（V1 核心环节） |
| **交付物** | 单篇 SKILL.md | SERIES_OVERVIEW.md + INDEX.md + DIGEST.md 三层 |

---

## 三、核心设计原则

### 3.1 保真优先（Fidelity First）
**不经过中间摘要**。提取器直接从原文剪裁，每个候选输出的 `[source]` 字段必须包含原始 VTT 文件名和时间戳范围，确保可追溯。

### 3.2 检索式而非通读式（Search, Don't Read）
每个提取器不尝试"理解"全文，而是以专属检索信号（关键词/模式/概念线索）定位高价值段落，在命中处展开上下文阅读。这避免了长篇文本中的精度衰减。

### 3.3 可操作性（Actionability）
每个技能必须回答"我什么时候用、怎么用、什么时候不用"。A2（触发条件）和 B（边界条件）不可空缺。

### 3.4 系统兼容性（System Compatibility）
V4 验证确保新技能不与已有技能冲突。若冲突，优先修改新技能而非已有技能。

### 3.5 渐进式投入（Progressive Investment）
每次只处理一个系列。新系列处理完毕后，与已有 skills 做 Zettelkasten 链接即可融入体系。

---

## 四、目录结构约定

```
Psychohistory/
├── methodology/           # 管道各阶段说明
│   ├── 00-overview.md
│   ├── 01-stage0-series-understand.md
│   ├── 02-stage1-retrieval-extract.md
│   ├── 03-stage1.5-quadruple-verify.md
│   ├── 04-stage2-ria-plus.md
│   ├── 05-stage3-cross-series-link.md
│   ├── 06-stage4-pressure-test.md
│   └── 07-stage5-deliver.md
├── templates/             # 模板文件
│   ├── SERIES_OVERVIEW.md.template
│   ├── SKILL.md.template
│   ├── PSYCHOHISTORY_INDEX.md.template
│   └── test-prompts.json.template
├── extractors/            # 7 个检索式提取器定义（含检索信号表）
│   ├── 01-game-theory-extractor.md
│   ├── 02-geopolitics-extractor.md
│   ├── 03-civilization-extractor.md
│   ├── 04-religion-extractor.md
│   ├── 05-predictive-extractor.md
│   ├── 06-failure-extractor.md
│   └── 07-glossary-extractor.md
├── series/                # 各系列源数据
│   └── game-theory/
│       ├── transcripts/   # VTT 原始字幕（全文检索源）
│       ├── candidates/    # 检索式提取结果
│       ├── rejected/      # 四重验证淘汰
│       └── skills/        # RIA++ 构建后的 Skill 产出
├── skills/                # 输出目录：已发布的 SKILL.md 文件（跨系列）
├── INDEX.md               # 主索引（跨系列链接）
└── DIGEST.md              # 精华阅读（自动生成）
```

---

## 五、质量门禁（Quality Gates）

| 关卡 | 阶段 | 通过标准 |
|------|------|---------|
| QG1 | Stage 0 完成 | SERIES_OVERVIEW.md 包含所有必填字段（见模板） |
| QG2 | Stage 1 完成 | 7 个提取器各产生至少 5 个候选，每个候选含 [source] 引用 |
| QG3 | Stage 1.5 完成 | rejected/ 目录包含每个拒绝项的具体原因 |
| QG4 | Stage 2 完成 | 每篇 SKILL.md 的 R 段含可核实的原文引用 |
| QG5 | Stage 3 完成 | INDEX.md Mermaid 图可编译无报错 |
| QG6 | Stage 4 完成 | 压力测试通过率 >= 80% |
| QG7 | Stage 5 完成 | DIGEST.md 字数在 5000-10000 之间 |

---

## 六、工作量估算

| 阶段 | 估算耗时 | 注意 |
|------|---------|------|
| Stage 0 | 30-60 min | 浏览播放列表、初步主题分类 |
| Stage 1（检索式提取）| 60-90 min/系列 | 每个提取器独立运行，可并行 |
| Stage 1.5 | 15-30 min/系列 | V4 只需检查 3-5 个关键接口点 |
| Stage 2 | 20-30 min/技能 | 复用模板减少格式耗时 |
| Stage 3 | 15-20 min/系列 | 只创建确实存在的依赖关系 |
| Stage 4 | 10-15 min/技能 | 测试提示可复用类似技能的模式 |
| Stage 5 | 10-15 min/系列 | DIGEST 从各 SKILL 自动拼接 |

---

## 七、快速开始

```bash
# 1. 进入 Psychohistory 工作目录
cd Psychohistory/

# 2. 准备系列源数据
series/<series-name>/transcripts/  # 放入 VTT 字幕文件

# 3. 从 Stage 0 开始：阅读 SERIES_OVERVIEW.md.template
# 4. 进入 Stage 1：以检索信号扫描完整字幕
# 5. Stage 1.5 → Stage 2 → Stage 3 → Stage 4 → Stage 5
```

---

*本文档对应 RIA-TV++ 管道 v8.0，核心改进：以检索式提取替代两阶段摘要提取，6 系列 199 个 Skill 已完成。*
