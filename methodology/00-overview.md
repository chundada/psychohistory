# RIA-TV++ 知识蒸馏管道全景概览

> **适配场景**：YouTube 系列视频 → 可复用思维技能（Skills）
> **来源方法**：仓颉技能 RIA-TV++ 管道
> **关键差异**：本书籍蒸馏管道的六大区别，见下方

---

## 一、管道总览

```
┌─────────────────────────────────────────────────────────────────┐
│                  RIA-TV++ 知识蒸馏管道（6 阶段）                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Stage 0: 系列理解 (Series Understanding)                         │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 列出所有剧集 → 识别主题弧 → 提取核心论点 → SERIES_OVERVIEW.md │   │
│  └──────────────────────┬───────────────────────────────────┘   │
│                         ▼                                       │
│  Stage 1: 两阶段并行提取 (Two-Phase Parallel Extraction)          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Phase 1: 轻量提取（每集 ~500 字关键框架）                   │   │
│  │ Phase 2: 7 个并行提取器 → candidates/ 目录                  │   │
│  └──────────────────────┬───────────────────────────────────┘   │
│                         ▼                                       │
│  Stage 1.5: 四重验证 (Quadruple Verification)                    │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ V1 跨剧集一致性 │ V2 预测能力 │ V3 独特性 │ V4 系统兼容性   │   │
│  │ → verified.md + rejected/                                    │   │
│  └──────────────────────┬───────────────────────────────────┘   │
│                         ▼                                       │
│  Stage 2: RIA++ 构建 (RIA++ Construction)                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ R │ I │ A1 │ A2 │ E │ B → SKILL.md                        │   │
│  └──────────────────────┬───────────────────────────────────┘   │
│                         ▼                                       │
│  Stage 3: 跨系列链接 (Cross-Series Zettelkasten Linking)          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ depends-on │ contrasts-with │ composes-with                │   │
│  │ → INDEX.md（含 Mermaid 流程图）                              │   │
│  └──────────────────────┬───────────────────────────────────┘   │
│                         ▼                                       │
│  Stage 4: 压力测试 (Pressure Test)                                │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ test-prompts.json → 盲测 → 通过率 <80% 则重做 Stage 2       │   │
│  └──────────────────────┬───────────────────────────────────┘   │
│                         ▼                                       │
│  Stage 5: 交付 (Delivery)                                       │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ DIGEST.md (5000-10000 字)                                  │   │
│  │ 安装到 ~/.claude/skills/Psychohistory/                     │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 二、与书籍蒸馏管道的六大关键差异

| 维度 | 书籍蒸馏（原版） | 视频系列蒸馏（本版） |
|------|-----------------|-------------------|
| **输入单元** | 全书（章节连续） | 每集一个独立章节，但按主题弧分组 |
| **阶段流程** | 单阶段提取 → 验证 → RIA | **两阶段提取**：先轻量后深度 |
| **提取器数量** | 5 个提取器 | **7 个提取器**（新增场景适配器 + 执行检查器） |
| **验证维度** | 三重验证（V1-V3） | **四重验证**（新增 V4 系统兼容性） |
| **系列融合** | 无跨章节依赖分析 | **显示跨剧集一致性检查**（V1 核心环节） |
| **交付物** | 单篇 SKILL.md | SERIES_OVERVIEW.md + INDEX.md + DIGEST.md 三层 |

---

## 三、核心设计原则

### 3.1 保真优先（Fidelity First）
每一篇 SKILL 必须以视频中的确切表述为锚点。R 字段必须包含可核实的直接引用，禁止"AI 幻觉式总结"。

### 3.2 可操作性（Actionability）
每个技能必须回答"我什么时候用、怎么用、什么时候不用"三个问题。A2（触发条件）和 B（边界条件）不可空缺。

### 3.3 系统兼容性（System Compatibility）
V4 验证确保新技能不与已有技能产生矛盾。若冲突，优先修改新技能而非已有技能。

### 3.4 渐进式投入（Progressive Investment）
Stage 1 Phase 1 的轻量提取可在 10-15 分钟内完成整系列扫描，避免在无价值的系列上投入深度提取资源。

---

## 四、目录结构约定

```
Psychohistory/
├── methodology/           # ← 本文档所在目录，管道各阶段说明
│   ├── 00-overview.md
│   ├── 01-stage0-series-understand.md
│   ├── 02-stage1-parallel-extract.md
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
├── extractors/            # 7 个提取器定义
│   ├── extractor-01-core-framework.md
│   ├── extractor-02-decision-protocol.md
│   ├── extractor-03-mental-model.md
│   ├── extractor-04-anti-pattern.md
│   ├── extractor-05-case-study.md
│   ├── extractor-06-scenario-adapter.md
│   └── extractor-07-execution-checker.md
├── skills/                # 输出目录：已发布的 SKILL.md 文件
├── INDEX.md               # 主索引（跨系列链接）
└── DIGEST.md              # 精华阅读（自动生成）
```

---

## 五、质量门禁（Quality Gates）

| 关卡 | 阶段 | 通过标准 |
|------|------|---------|
| QG1 | Stage 0 完成 | SERIES_OVERVIEW.md 包含所有必填字段（见模板） |
| QG2 | Stage 1 完成 | 每集至少有 1 个候选技能进入 candidates/ |
| QG3 | Stage 1.5 完成 | rejected/ 目录包含每个拒绝项的具体原因 |
| QG4 | Stage 2 完成 | 每篇 SKILL.md 通过质量检查表（见模板） |
| QG5 | Stage 3 完成 | INDEX.md Mermaid 图可编译无报错 |
| QG6 | Stage 4 完成 | 压力测试通过率 >= 80% |
| QG7 | Stage 5 完成 | DIGEST.md 字数在 5000-10000 之间 |

---

## 六、工作量估算

| 阶段 | 估算耗时 | 加速策略 |
|------|---------|---------|
| Stage 0 | 30-60 min | 先看系列简介 / 播放列表描述 |
| Stage 1 Phase 1 | 10-15 min/系列 | 只记框架，不做深度提取 |
| Stage 1 Phase 2 | 30-45 min/集 | 可并行处理多集 |
| Stage 1.5 | 15-30 min/系列 | V4 只需检查 3-5 个关键接口点 |
| Stage 2 | 20-30 min/技能 | 复用模板减少格式耗时 |
| Stage 3 | 15-20 min/系列 | 只创建确实存在的依赖关系 |
| Stage 4 | 10-15 min/技能 | 测试提示可复用类似技能的模式 |
| Stage 5 | 10-15 min/系列 | DIGEST 从各 SKILL 自动拼接 |

**完整系列（20-30 集）总耗时**：约 8-15 小时（取决于视频复杂度和并行度）

---

## 七、快速开始

```bash
# 1. 进入 Psychohistory 工作目录
cd Psychohistory/

# 2. 创建新系列工作区
mkdir -p workspace/<series-name>/{phase1,phase2,candidates,verified,rejected,skills}

# 3. 从 Stage 0 开始
cp templates/SERIES_OVERVIEW.md.template workspace/<series-name>/SERIES_OVERVIEW.md
# 编辑 SERIES_OVERVIEW.md → 运行 Stage 1
```

---

*本文档对应 RIA-TV++ 管道 v2.0，适配 YouTube 视频系列知识蒸馏场景。*
