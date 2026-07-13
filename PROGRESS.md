---
tags: [psychohistory, core]
type: "progress"
---
# 📊 Psychohistory - 项目进度追踪

> 最后更新: 2026-07-13
> 核心方法论 v3.0: **检索式提取**（取代旧的两阶段摘要提取）

---

## 🗺️ 路线图总览

```mermaid
gantt
    title Psychohistory 蒸馏路线图
    dateFormat  YYYY-MM-DD
    axisFormat  %m/%d
    
    section Phase 1 - 架构搭建
    设计蒸馏流水线           :done, 2026-07-13, 1d
    创建提取器+模板          :done, 2026-07-13, 1d
    创建 GitHub 仓库         :done, 2026-07-13, 1d
    
    section Phase 2 - Pilot: Game Theory
    下载字幕/转录文本        :done, 2026-07-13, 1d
    ⭐ 检索式提取 (7路)     :active, 2026-07-13, 2d
    四重验证 + 筛选          :2026-07-15, 1d
    RIA++ 构造 Skill         :2026-07-16, 2d
    压力测试 + 交付           :2026-07-18, 1d

    section Phase 3 - 扩展
    Civilization 系列(59集)  :2026-07-20, 7d
    Secret History 系列(27集):2026-07-27, 5d
    Geo-Strategy 系列(19集)  :2026-08-01, 3d
```

---

## ✅ 已完成

### 📋 架构设计 (`SPEC.md`)

- [x] 6 阶段蒸馏流水线定义
- [x] **检索式提取架构**（核心创新：无中间摘要）
- [x] 7 路检索信号表
- [x] 四重验证机制（V1-V4）
- [x] 跨系列 Zettelkasten 链接方案

### 📝 方法论文档 (8篇)

- [x] `00-overview.md` — 全景概览（v3.0）
- [x] `01-stage0-series-understand.md` — 系列理解
- [x] `02-stage1-retrieval-extract.md` — ⭐ 检索式提取
- [x] `03-stage1.5-quadruple-verify.md` — 四重验证
- [x] `04-stage2-ria-plus.md` — RIA++ 构造
- [x] `05-stage3-cross-series-link.md` — 跨系列链接
- [x] `06-stage4-pressure-test.md` — 压力测试
- [x] `07-stage5-deliver.md` — 交付

### 🎯 提取器 Prompt (7个，含检索信号表)

- [x] `01-game-theory-extractor.md` — 博弈模型
- [x] `02-geopolitics-extractor.md` — 地缘法则
- [x] `03-civilization-extractor.md` — 文明规律
- [x] `04-religion-extractor.md` — 宗教叙事
- [x] `05-predictive-extractor.md` — ⭐ 预测模型
- [x] `06-failure-extractor.md` — 反例陷阱
- [x] `07-glossary-extractor.md` — 术语词典

### 📄 输出模板 (4个)

- [x] `SERIES_OVERVIEW.md.template`
- [x] `SKILL.md.template`
- [x] `PSYCHOHISTORY_INDEX.md.template`
- [x] `test-prompts.json.template`

### 🌐 GitHub 仓库

- [x] 仓库创建完成
- [x] 初始提交（架构文档 + 提取器 + 模板）
- [x] Game Theory 29 集字幕全部下载并推送

---

## 🔵 进行中

### Game Theory 系列 (Pilot) — 检索式提取

```
阶段: Stage 1 — 检索式提取 (Retrieval-based Extraction)
输入: 29 集原始 VTT 字幕（零压缩）
方法: 以 7 路检索信号扫描全文 → 定位上下文 → 直接剪裁
输出: candidates/ 目录（按提取器分组）
```

**即将开始**：7 个提取器并行运行，从完整字幕中检索方法论。

#### 剧集清单（字幕已就绪）

| # | 标题 | 时长 | 字幕 | 提取状态 |
|---|---|---|---|---|
| 1 | The Dating Game | 50min | ✅ VTT | ⏳ |
| 2 | Why Schools Suck | 49min | ✅ VTT | ⏳ |
| 3 | Rich Dad, Poor Dad | 54min | ✅ VTT | ⏳ |
| 4 | The Immigration Trap | 46min | ✅ VTT | ⏳ |
| 5 | The World Game | 57min | ✅ VTT | ⏳ |
| 6 | The World's Bank | 45min | ✅ VTT | ⏳ |
| 7 | America's Game | 49min | ✅ VTT | ⏳ |
| 8 | Communist Specter | 55min | ✅ VTT | ⏳ |
| 9 | The US-Iran War | 45min | ✅ VTT | ⏳ |
| 10 | The Law of Asymmetry | 54min | ✅ VTT | ⏳ |
| 11 | The Law of Escalation | 61min | ✅ VTT | ⏳ |
| 12 | The Law of Eschatological Convergence | 66min | ✅ VTT | ⏳ |
| 13 | Epstein's World | 50min | ✅ VTT | ⏳ |
| 14 | The Law of Proximity | 50min | ✅ VTT | ⏳ |
| 15 | The Return of History | 50min | ✅ VTT | ⏳ |
| 16 | Pax Judaica Rising | 67min | ✅ VTT | ⏳ |
| 17 | The Great Reset | 58min | ✅ VTT | ⏳ |
| 18 | Trump World Order | 49min | ✅ VTT | ⏳ |
| 19 | The Hollywood-Pentagon Complex | 54min | ✅ VTT | ⏳ |
| 20 | Mid-Term Examination | 83min | ✅ VTT | ⏳ |
| 21 | World War Trump | 59min | ✅ VTT | ⏳ |
| 22 | Twilight of the Nation-State | 56min | ✅ VTT | ⏳ |
| 23 | The WWIII Chessboard | 60min | ✅ VTT | ⏳ |
| 24 | The AI Apocalypse | 64min | ✅ VTT | ⏳ |
| 25 | Trump Visits China | 73min | ✅ VTT | ⏳ |
| 26 | The Holy Empire of AI | 67min | ✅ VTT | ⏳ |
| 27 | Putin Enters the Chat | 73min | ✅ VTT | ⏳ |
| 28 | Predictive History | 76min | ✅ VTT | ⏳ |
| 29 | Final Examination | 120min | ✅ VTT | ⏳ |

---

## ⏳ 待处理

| 系列 | 集数 | 预计 Skills | 优先级 |
|---|---|---|---|
| 📜 Civilization | 59 | 25-35 | ⭐⭐⭐ |
| 🔮 Secret History | 27 | 15-20 | ⭐⭐⭐ |
| 🗺️ Geo-Strategy | 19 | 12-18 | ⭐⭐ |
| 📚 Great Books | 13 | 8-12 | ⭐⭐ |
| 🔥 Dante | 12 | 8-10 | ⭐ |
| 🌍 Geo-Strategy Updates | 8 | 3-5 | ⭐ |

---

## 📌 方法论版本记录

| 版本 | 日期 | 变更 |
|------|------|------|
| v3.0 | 2026-07-13 | ⭐ **检索式提取**：删除两阶段摘要提取，改为"检索信号→上下文剪裁" |
| v2.0 | 2026-07-13 | 初始：两阶段摘要提取架构 |

---

## 📌 持续注入流程

当新视频发布时：

1. 确定视频属于哪个系列
2. 下载字幕 → `transcripts/` 目录
3. 运行该系列对应提取器的检索信号扫描
4. 新候选与现有候选池合并 → 跑四重验证
5. 更新 INDEX.md + 重新建立 Zettelkasten 链接
6. 重新部署到 skills 目录
